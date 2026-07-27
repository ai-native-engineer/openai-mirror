<!-- source: https://developers.openai.com/api/reference/typescript/resources/beta/subresources/responses/methods/create/ -->
<!-- part of: https://developers.openai.com/api/reference/typescript/resources/beta/subresources/responses/methods/create/ -->

<!-- chunk-start -->

pending\_safety\_checks: Array<PendingSafetyCheck>

The pending safety checks for the computer call.

id: string

The ID of the pending safety check.

code?: string | null

The type of the pending safety check.

message?: string | null

Details about the pending safety check.

status: "in\_progress" | "completed" | "incomplete"

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

type: "computer\_call"

The type of the computer call. Always `computer_call`.

action?: [BetaComputerAction](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_computer_action%20%3E%20(schema))

A click action.

Click { button, type, x, 2 more }

A click action.

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

[
  { x: 100, y: 200 },
  { x: 200, y: 300 }
]

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

Flattened batched actions for `computer_use`. Each action includes an
`type` discriminator and action-specific fields.

Click { button, type, x, 2 more }

A click action.

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

[
  { x: 100, y: 200 },
  { x: 200, y: 300 }
]

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

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

ComputerCallOutput { call\_id, output, type, 4 more }

The output of a computer tool call.

call\_id: string

The ID of the computer tool call that produced the output.

maxLength64

minLength1

output: [BetaResponseComputerToolCallOutputScreenshot](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_computer_tool_call_output_screenshot%20%3E%20(schema)) { type, file\_id, image\_url }

A computer screenshot image used with the computer use tool.

type: "computer\_screenshot"

Specifies the event type. For a computer screenshot, this property is
always set to `computer_screenshot`.

file\_id?: string

The identifier of an uploaded file that contains the screenshot.

image\_url?: string

The URL of the screenshot image.

formaturi

type: "computer\_call\_output"

The type of the computer tool call output. Always `computer_call_output`.

id?: string | null

The ID of the computer tool call output.

acknowledged\_safety\_checks?: Array<AcknowledgedSafetyCheck> | null

The safety checks reported by the API that have been acknowledged by the developer.

id: string

The ID of the pending safety check.

code?: string | null

The type of the pending safety check.

message?: string | null

Details about the pending safety check.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

status?: "in\_progress" | "completed" | "incomplete" | null

The status of the message input. One of `in_progress`, `completed`, or `incomplete`. Populated when input items are returned via API.

"in\_progress"

"completed"

"incomplete"

BetaResponseFunctionWebSearch { id, action, status, 2 more }

The results of a web search tool call. See the
[web search guide](https://platform.openai.com/docs/guides/tools-web-search) for more information.

id: string

The unique ID of the web search tool call.

action: Search { type, queries, query, sources }  | OpenPage { type, url }  | FindInPage { pattern, type, url }

An object describing the specific action taken in this web search call.
Includes details on how the model used the web (search, open\_page, find\_in\_page).

Search { type, queries, query, sources }

Action type “search” - Performs a web search query.

type: "search"

The action type.

queries?: Array<string>

The search queries.

Deprecatedquery?: string

The search query.

sources?: Array<Source>

The sources used in the search.

type: "url"

The type of source. Always `url`.

url: string

The URL of the source.

formaturi

OpenPage { type, url }

Action type “open\_page” - Opens a specific URL from search results.

type: "open\_page"

The action type.

url?: string | null

The URL opened by the model.

formaturi

FindInPage { pattern, type, url }

Action type “find\_in\_page”: Searches for a pattern within a loaded page.

pattern: string

The pattern or text to search for within the page.

type: "find\_in\_page"

The action type.

url: string

The URL of the page searched for the pattern.

formaturi

status: "in\_progress" | "searching" | "completed" | "failed"

The status of the web search tool call.

"in\_progress"

"searching"

"completed"

"failed"

type: "web\_search\_call"

The type of the web search tool call. Always `web_search_call`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

BetaResponseFunctionToolCall { arguments, call\_id, name, 6 more }

A tool call to run a function. See the
[function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.

arguments: string

A JSON string of the arguments to pass to the function.

call\_id: string

The unique ID of the function tool call generated by the model.

name: string

The name of the function to run.

type: "function\_call"

The type of the function tool call. Always `function_call`.

id?: string

The unique ID of the function tool call.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

caller?: Direct { type }  | Program { caller\_id, type }  | null

The execution context that produced this tool call.

Direct { type }

type: "direct"

Program { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

type: "program"

namespace?: string

The namespace of the function to run.

status?: "in\_progress" | "completed" | "incomplete"

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

FunctionCallOutput { call\_id, output, type, 4 more }

The output of a function tool call.

call\_id: string

The unique ID of the function tool call generated by the model.

maxLength64

minLength1

output: string | [BetaResponseFunctionCallOutputItemList](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_call_output_item_list%20%3E%20(schema)) { , ,  }

Text, image, or file output of the function tool call.

string

BetaResponseFunctionCallOutputItemList = Array<[BetaResponseFunctionCallOutputItem](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_call_output_item%20%3E%20(schema))>

An array of content outputs (text, image, file) for the function tool call.

BetaResponseInputTextContent { text, type, prompt\_cache\_breakpoint }

A text input to the model.

text: string

The text input to the model.

maxLength10485760

type: "input\_text"

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint?: PromptCacheBreakpoint | null

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

BetaResponseInputImageContent { type, detail, file\_id, 2 more }

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision)

type: "input\_image"

The type of the input item. Always `input_image`.

detail?: "low" | "high" | "auto" | "original" | null

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

"low"

"high"

"auto"

"original"

file\_id?: string | null

The ID of the file to be sent to the model.

image\_url?: string | null

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

maxLength20971520

formaturi

prompt\_cache\_breakpoint?: PromptCacheBreakpoint | null

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

BetaResponseInputFileContent { type, detail, file\_data, 4 more }

A file input to the model.

type: "input\_file"

The type of the input item. Always `input_file`.

detail?: "auto" | "low" | "high"

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

"auto"

"low"

"high"

file\_data?: string | null

The base64-encoded data of the file to be sent to the model.

maxLength73400320

file\_id?: string | null

The ID of the file to be sent to the model.

file\_url?: string | null

The URL of the file to be sent to the model.

formaturi

filename?: string | null

The name of the file to be sent to the model.

prompt\_cache\_breakpoint?: PromptCacheBreakpoint | null

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

type: "function\_call\_output"

The type of the function tool call output. Always `function_call_output`.

id?: string | null

The unique ID of the function tool call output. Populated when this item is returned via API.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

caller?: Direct { type }  | Program { caller\_id, type }  | null

The execution context that produced this tool call.

Direct { type }

type: "direct"

The caller type. Always `direct`.

Program { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

maxLength64

minLength1

type: "program"

The caller type. Always `program`.

status?: "in\_progress" | "completed" | "incomplete" | null

The status of the item. One of `in_progress`, `completed`, or `incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

AgentMessage { author, content, recipient, 3 more }

A message routed between agents.

author: string

The sending agent identity.

content: Array<[BetaResponseInputTextContent](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_text_content%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  | [BetaResponseInputImageContent](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_image_content%20%3E%20(schema)) { type, detail, file\_id, 2 more }  | EncryptedContent { encrypted\_content, type } >

Plaintext, image, or encrypted content sent between agents.

BetaResponseInputTextContent { text, type, prompt\_cache\_breakpoint }

A text input to the model.

text: string

The text input to the model.

maxLength10485760

type: "input\_text"

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint?: PromptCacheBreakpoint | null

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

BetaResponseInputImageContent { type, detail, file\_id, 2 more }

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision)

type: "input\_image"

The type of the input item. Always `input_image`.

detail?: "low" | "high" | "auto" | "original" | null

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

"low"

"high"

"auto"

"original"

file\_id?: string | null

The ID of the file to be sent to the model.

image\_url?: string | null

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

maxLength20971520

formaturi

prompt\_cache\_breakpoint?: PromptCacheBreakpoint | null

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

EncryptedContent { encrypted\_content, type }

Opaque encrypted content that Responses API decrypts inside trusted model execution.

encrypted\_content: string

Opaque encrypted content.

maxLength10485760

type: "encrypted\_content"

The type of the input item. Always `encrypted_content`.

recipient: string

The destination agent identity.

type: "agent\_message"

The item type. Always `agent_message`.

id?: string | null

The unique ID of this agent message item.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

MultiAgentCall { action, arguments, call\_id, 3 more }

action: "spawn\_agent" | "interrupt\_agent" | "list\_agents" | 3 more

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

The unique ID linking this call to its output.

maxLength64

minLength1

type: "multi\_agent\_call"

The item type. Always `multi_agent_call`.

id?: string | null

The unique ID of this multi-agent call.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

MultiAgentCallOutput { action, call\_id, output, 3 more }

action: "spawn\_agent" | "interrupt\_agent" | "list\_agents" | 3 more

The multi-agent action that produced this result.

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

call\_id: string

The unique ID of the multi-agent call.

maxLength64

minLength1

output: Array<Output>

Text output returned by the multi-agent action.

text: string

The text content.

maxLength10485760

type: "output\_text"

The content type. Always `output_text`.

annotations?: Array<FileCitation { file\_id, filename, index, type }  | URLCitation { end\_index, start\_index, title, 2 more }  | ContainerFileCitation { container\_id, end\_index, file\_id, 3 more } >

Citations associated with the text content.

FileCitation { file\_id, filename, index, type }

file\_id: string

The ID of the file.

filename: string

The filename of the file cited.

index: number

The index of the file in the list of files.

minimum0

type: "file\_citation"

The citation type. Always `file_citation`.

URLCitation { end\_index, start\_index, title, 2 more }

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

formaturi

ContainerFileCitation { container\_id, end\_index, file\_id, 3 more }

container\_id: string

The ID of the container.

end\_index: number

The index of the last character of the citation in the message.

minimum0

file\_id: string

The ID of the container file.

filename: string

The filename of the container file cited.

start\_index: number

The index of the first character of the citation in the message.

minimum0

type: "container\_file\_citation"

The citation type. Always `container_file_citation`.

type: "multi\_agent\_call\_output"

The item type. Always `multi_agent_call_output`.

id?: string | null

The unique ID of this multi-agent call output.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

ToolSearchCall { arguments, type, id, 4 more }

arguments: unknown

The arguments supplied to the tool search call.

type: "tool\_search\_call"

The item type. Always `tool_search_call`.

id?: string | null

The unique ID of this tool search call.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

call\_id?: string | null

The unique ID of the tool search call generated by the model.

maxLength64

minLength1

execution?: "server" | "client"

Whether tool search was executed by the server or by the client.

"server"

"client"

status?: "in\_progress" | "completed" | "incomplete" | null

The status of the tool search call.

"in\_progress"

"completed"

"incomplete"

BetaResponseToolSearchOutputItemParam { tools, type, id, 4 more }

tools: Array<[BetaTool](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))>

The loaded tool definitions returned by the tool search output.

BetaFunctionTool { name, parameters, strict, 5 more }

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

name: string

The name of the function to call.

parameters: Record<string, unknown> | null

A JSON schema object describing the parameters of the function.

strict: boolean | null

Whether strict parameter validation is enforced for this function tool.

type: "function"

The type of the function tool. Always `function`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this function is deferred and loaded via tool search.

description?: string | null

A description of the function. Used by the model to determine whether or not to call the function.

output\_schema?: Record<string, unknown> | null

A JSON schema object describing the JSON value encoded in string outputs for this function.

BetaFileSearchTool { type, vector\_store\_ids, filters, 2 more }

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

type: "file\_search"

The type of the file search tool. Always `file_search`.

vector\_store\_ids: Array<string>

The IDs of the vector stores to search.

filters?: ComparisonFilter { key, type, value }  | CompoundFilter { filters, type }  | null

A filter to apply.

ComparisonFilter { key, type, value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: string

The key to compare against the value.

type: "eq" | "ne" | "gt" | 5 more

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: string | number | boolean | Array<string | number>

The value to compare against the attribute key; supports string, number, or boolean types.

string

number

boolean

Array<string | number>

string

number

CompoundFilter { filters, type }

Combine multiple filters using `and` or `or`.

filters: Array<ComparisonFilter { key, type, value }  | unknown>

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

ComparisonFilter { key, type, value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: string

The key to compare against the value.

type: "eq" | "ne" | "gt" | 5 more

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: string | number | boolean | Array<string | number>

The value to compare against the attribute key; supports string, number, or boolean types.

string

number

boolean

Array<string | number>

string

number

unknown

type: "and" | "or"

Type of operation: `and` or `or`.

"and"

"or"

max\_num\_results?: number

The maximum number of results to return. This number should be between 1 and 50 inclusive.

ranking\_options?: RankingOptions { hybrid\_search, ranker, score\_threshold }

Ranking options for search.

hybrid\_search?: HybridSearch { embedding\_weight, text\_weight }

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

embedding\_weight: number

The weight of the embedding in the reciprocal ranking fusion.

text\_weight: number

The weight of the text in the reciprocal ranking fusion.

ranker?: "auto" | "default-2024-11-15"

The ranker to use for the file search.

"auto"

"default-2024-11-15"

score\_threshold?: number

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

BetaComputerTool { type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

type: "computer"

The type of the computer tool. Always `computer`.

BetaComputerUsePreviewTool { display\_height, display\_width, environment, type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

display\_height: number

The height of the computer display.

display\_width: number

The width of the computer display.

environment: "windows" | "mac" | "linux" | 2 more

The type of computer environment to control.

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: "computer\_use\_preview"

The type of the computer use tool. Always `computer_use_preview`.

BetaWebSearchTool { type, filters, search\_context\_size, user\_location }

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: "web\_search" | "web\_search\_2025\_08\_26"

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

"web\_search"

"web\_search\_2025\_08\_26"

filters?: Filters | null

Filters for the search.

allowed\_domains?: Array<string> | null

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

search\_context\_size?: "low" | "medium" | "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

"low"

"medium"

"high"

user\_location?: UserLocation | null

The approximate location of the user.

city?: string | null

Free text input for the city of the user, e.g. `San Francisco`.

country?: string | null

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region?: string | null

Free text input for the region of the user, e.g. `California`.

timezone?: string | null

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

type?: "approximate"

The type of location approximation. Always `approximate`.

Mcp { server\_label, type, allowed\_callers, 9 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: string

A label for this MCP server, used to identify it in tool calls.

type: "mcp"

The type of the MCP tool. Always `mcp`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

allowed\_tools?: Array<string> | McpToolFilter { read\_only, tool\_names }  | null

List of allowed tool names or a filter object.

Array<string>

McpToolFilter { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

authorization?: string

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

connector\_id?: "connector\_dropbox" | "connector\_gmail" | "connector\_googlecalendar" | 5 more

Identifier for service connectors, like those available in ChatGPT. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided. Learn more
about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

Currently supported `connector_id` values are:

* Dropbox: `connector_dropbox`
* Gmail: `connector_gmail`
* Google Calendar: `connector_googlecalendar`
* Google Drive: `connector_googledrive`
* Microsoft Teams: `connector_microsoftteams`
* Outlook Calendar: `connector_outlookcalendar`
* Outlook Email: `connector_outlookemail`
* SharePoint: `connector_sharepoint`

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading?: boolean

Whether this MCP tool is deferred and discovered via tool search.

headers?: Record<string, string> | null

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

require\_approval?: McpToolApprovalFilter { always, never }  | "always" | "never" | null

Specify which of the MCP server’s tools require approval.

McpToolApprovalFilter { always, never }

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

always?: Always { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

never?: Never { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

"always" | "never"

"always"

"never"

server\_description?: string

Optional description of the MCP server, used to provide more context.

server\_url?: string

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

tunnel\_id?: string

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

CodeInterpreter { container, type, allowed\_callers }

A tool that runs Python code to help generate a response to a prompt.

container: string | CodeInterpreterToolAuto { type, file\_ids, memory\_limit, network\_policy }

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

string

CodeInterpreterToolAuto { type, file\_ids, memory\_limit, network\_policy }

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

type: "auto"

Always `auto`.

file\_ids?: Array<string>

An optional list of uploaded files to make available to your code.

memory\_limit?: "1g" | "4g" | "16g" | "64g" | null

The memory limit for the code interpreter container.

"1g"

"4g"

"16g"

"64g"

network\_policy?: [BetaContainerNetworkPolicyDisabled](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  | [BetaContainerNetworkPolicyAllowlist](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

BetaContainerNetworkPolicyDisabled { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

BetaContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array<string>

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets?: Array<[BetaContainerNetworkPolicyDomainSecret](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } >

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

minLength1

name: string

The name of the secret to inject for the domain.

minLength1

value: string

The secret value to inject for the domain.

maxLength10485760

minLength1

type: "code\_interpreter"

The type of the code interpreter tool. Always `code_interpreter`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

ProgrammaticToolCalling { type }

type: "programmatic\_tool\_calling"

The type of the tool. Always `programmatic_tool_calling`.

ImageGeneration { type, action, background, 9 more }

A tool that generates images using the GPT image models.

type: "image\_generation"

The type of the image generation tool. Always `image_generation`.

action?: "generate" | "edit" | "auto"

Whether to generate a new image or edit an existing image. Default: `auto`.

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

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

"high"

"low"

input\_image\_mask?: InputImageMask { file\_id, image\_url }

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

file\_id?: string

File ID for the mask image.

image\_url?: string

Base64-encoded mask image.

model?: (string & {}) | "gpt-image-1" | "gpt-image-1-mini" | "gpt-image-2" | 3 more

The image generation model to use. Default: `gpt-image-1`.

(string & {})

"gpt-image-1" | "gpt-image-1-mini" | "gpt-image-2" | 3 more

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation?: "auto" | "low"

Moderation level for the generated image. Default: `auto`.

"auto"

"low"

output\_compression?: number

Compression level for the output image. Default: 100.

minimum0

maximum100

output\_format?: "png" | "webp" | "jpeg"

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

"png"

"webp"

"jpeg"

partial\_images?: number

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

quality?: "low" | "medium" | "high" | "auto"

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

"low"

"medium"

"high"

"auto"

size?: (string & {}) | "1024x1024" | "1024x1536" | "1536x1024" | "auto"

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

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

A tool that allows the model to execute shell commands.

type: "shell"

The type of the shell tool. Always `shell`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

environment?: [BetaContainerAuto](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_auto%20%3E%20(schema)) { type, file\_ids, memory\_limit, 2 more }  | [BetaLocalEnvironment](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_environment%20%3E%20(schema)) { type, skills }  | [BetaContainerReference](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_reference%20%3E%20(schema)) { container\_id, type }  | null

BetaContainerAuto { type, file\_ids, memory\_limit, 2 more }

type: "container\_auto"

Automatically creates a container for this request

file\_ids?: Array<string>

An optional list of uploaded files to make available to your code.

memory\_limit?: "1g" | "4g" | "16g" | "64g" | null

The memory limit for the container.

"1g"

"4g"

"16g"

"64g"

network\_policy?: [BetaContainerNetworkPolicyDisabled](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  | [BetaContainerNetworkPolicyAllowlist](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

BetaContainerNetworkPolicyDisabled { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

BetaContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array<string>

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets?: Array<[BetaContainerNetworkPolicyDomainSecret](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } >

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

minLength1

name: string

The name of the secret to inject for the domain.

minLength1

value: string

The secret value to inject for the domain.

maxLength10485760

minLength1

skills?: Array<[BetaSkillReference](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_skill_reference%20%3E%20(schema)) { skill\_id, type, version }  | [BetaInlineSkill](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill%20%3E%20(schema)) { description, name, source, type } >

An optional list of skills referenced by id or inline data.

BetaSkillReference { skill\_id, type, version }

skill\_id: string

The ID of the referenced skill.

maxLength64

minLength1

type: "skill\_reference"

References a skill created with the /v1/skills endpoint.

version?: string

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

BetaInlineSkill { description, name, source, type }

description: string

The description of the skill.

name: string

The name of the skill.

source: [BetaInlineSkillSource](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema)) { data, media\_type, type }

Inline skill payload

data: string

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

media\_type: "application/zip"

The media type of the inline skill payload. Must be `application/zip`.

type: "base64"

The type of the inline skill source. Must be `base64`.

type: "inline"

Defines an inline skill for this request.

BetaLocalEnvironment { type, skills }

type: "local"

Use a local computer environment.

skills?: Array<[BetaLocalSkill](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema)) { description, name, path } >

An optional list of skills.

description: string

The description of the skill.

name: string

The name of the skill.

path: string

The path to the directory containing the skill.

BetaContainerReference { container\_id, type }

container\_id: string

The ID of the referenced container.

type: "container\_reference"

References a container created with the /v1/containers endpoint

BetaCustomTool { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this tool should be deferred and discovered via tool search.

description?: string

Optional description of the custom tool, used to provide more context.

format?: Text { type }  | Grammar { definition, syntax, type }

The input format for the custom tool. Default is unconstrained text.

Text { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar { definition, syntax, type }

A grammar defined by the user.

definition: string

The grammar definition.

syntax: "lark" | "regex"

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: "grammar"

Grammar format. Always `grammar`.

BetaNamespaceTool { description, name, tools, type }

Groups function/custom tools under a shared namespace.

description: string

A description of the namespace shown to the model.

minLength1

name: string

The namespace name used in tool calls (for example, `crm`).

minLength1

tools: Array<Function { name, type, allowed\_callers, 5 more }  | [BetaCustomTool](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_custom_tool%20%3E%20(schema)) { name, type, allowed\_callers, 3 more } >

The function/custom tools available inside this namespace.

Function { name, type, allowed\_callers, 5 more }

name: string

maxLength128

minLength1

type: "function"

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this function should be deferred and discovered via tool search.

description?: string | null

output\_schema?: Record<string, unknown> | null

A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

parameters?: unknown

strict?: boolean | null

Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

BetaCustomTool { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this tool should be deferred and discovered via tool search.

description?: string

Optional description of the custom tool, used to provide more context.

format?: Text { type }  | Grammar { definition, syntax, type }

The input format for the custom tool. Default is unconstrained text.

Text { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar { definition, syntax, type }

A grammar defined by the user.

definition: string

The grammar definition.

syntax: "lark" | "regex"

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: "grammar"

Grammar format. Always `grammar`.

type: "namespace"

The type of the tool. Always `namespace`.

BetaToolSearchTool { type, description, execution, parameters }

Hosted or BYOT tool search configuration for deferred tools.

type: "tool\_search"

The type of the tool. Always `tool_search`.

description?: string | null

Description shown to the model for a client-executed tool search tool.

execution?: "server" | "client"

Whether tool search is executed by the server or by the client.

"server"

"client"

parameters?: unknown

Parameter schema for a client-executed tool search tool.

BetaWebSearchPreviewTool { type, search\_content\_types, search\_context\_size, user\_location }

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: "web\_search\_preview" | "web\_search\_preview\_2025\_03\_11"

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types?: Array<"text" | "image">

"text"

"image"

search\_context\_size?: "low" | "medium" | "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

"low"

"medium"

"high"

user\_location?: UserLocation | null

The user’s location.

type: "approximate"

The type of location approximation. Always `approximate`.

city?: string | null

Free text input for the city of the user, e.g. `San Francisco`.

country?: string | null

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region?: string | null

Free text input for the region of the user, e.g. `California`.

timezone?: string | null

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

BetaApplyPatchTool { type, allowed\_callers }

Allows the assistant to create, delete, or update files using unified diffs.

type: "apply\_patch"

The type of the tool. Always `apply_patch`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

type: "tool\_search\_output"

The item type. Always `tool_search_output`.

id?: string | null

The unique ID of this tool search output.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

call\_id?: string | null

The unique ID of the tool search call generated by the model.

maxLength64

minLength1

execution?: "server" | "client"

Whether tool search was executed by the server or by the client.

"server"

"client"

status?: "in\_progress" | "completed" | "incomplete" | null

The status of the tool search output.

"in\_progress"

"completed"

"incomplete"

AdditionalTools { role, tools, type, 2 more }

role: "developer"

The role that provided the additional tools. Only `developer` is supported.

tools: Array<[BetaTool](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))>

A list of additional tools made available at this item.

BetaFunctionTool { name, parameters, strict, 5 more }

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

name: string

The name of the function to call.

parameters: Record<string, unknown> | null

A JSON schema object describing the parameters of the function.

strict: boolean | null

Whether strict parameter validation is enforced for this function tool.

type: "function"

The type of the function tool. Always `function`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this function is deferred and loaded via tool search.

description?: string | null

A description of the function. Used by the model to determine whether or not to call the function.

output\_schema?: Record<string, unknown> | null

A JSON schema object describing the JSON value encoded in string outputs for this function.

BetaFileSearchTool { type, vector\_store\_ids, filters, 2 more }

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

type: "file\_search"

The type of the file search tool. Always `file_search`.

vector\_store\_ids: Array<string>

The IDs of the vector stores to search.

filters?: ComparisonFilter { key, type, value }  | CompoundFilter { filters, type }  | null

A filter to apply.

ComparisonFilter { key, type, value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: string

The key to compare against the value.

type: "eq" | "ne" | "gt" | 5 more

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: string | number | boolean | Array<string | number>

The value to compare against the attribute key; supports string, number, or boolean types.

string

number

boolean

Array<string | number>

string

number

CompoundFilter { filters, type }

Combine multiple filters using `and` or `or`.

filters: Array<ComparisonFilter { key, type, value }  | unknown>

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

ComparisonFilter { key, type, value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: string

The key to compare against the value.

type: "eq" | "ne" | "gt" | 5 more

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: string | number | boolean | Array<string | number>

The value to compare against the attribute key; supports string, number, or boolean types.

string

number

boolean

Array<string | number>

string

number

unknown

type: "and" | "or"

Type of operation: `and` or `or`.

"and"

"or"

max\_num\_results?: number

The maximum number of results to return. This number should be between 1 and 50 inclusive.

ranking\_options?: RankingOptions { hybrid\_search, ranker, score\_threshold }

Ranking options for search.

hybrid\_search?: HybridSearch { embedding\_weight, text\_weight }

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

embedding\_weight: number

The weight of the embedding in the reciprocal ranking fusion.

text\_weight: number

The weight of the text in the reciprocal ranking fusion.

ranker?: "auto" | "default-2024-11-15"

The ranker to use for the file search.

"auto"

"default-2024-11-15"

score\_threshold?: number

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

BetaComputerTool { type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

type: "computer"

The type of the computer tool. Always `computer`.

BetaComputerUsePreviewTool { display\_height, display\_width, environment, type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

display\_height: number

The height of the computer display.

display\_width: number

The width of the computer display.

environment: "windows" | "mac" | "linux" | 2 more

The type of computer environment to control.

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: "computer\_use\_preview"

The type of the computer use tool. Always `computer_use_preview`.

BetaWebSearchTool { type, filters, search\_context\_size, user\_location }

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: "web\_search" | "web\_search\_2025\_08\_26"

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

"web\_search"

"web\_search\_2025\_08\_26"

filters?: Filters | null

Filters for the search.

allowed\_domains?: Array<string> | null

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

search\_context\_size?: "low" | "medium" | "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

"low"

"medium"

"high"

user\_location?: UserLocation | null

The approximate location of the user.

city?: string | null

Free text input for the city of the user, e.g. `San Francisco`.

country?: string | null

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region?: string | null

Free text input for the region of the user, e.g. `California`.

timezone?: string | null

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

type?: "approximate"

The type of location approximation. Always `approximate`.

Mcp { server\_label, type, allowed\_callers, 9 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: string

A label for this MCP server, used to identify it in tool calls.

type: "mcp"

The type of the MCP tool. Always `mcp`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

allowed\_tools?: Array<string> | McpToolFilter { read\_only, tool\_names }  | null

List of allowed tool names or a filter object.

Array<string>

McpToolFilter { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

authorization?: string

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

connector\_id?: "connector\_dropbox" | "connector\_gmail" | "connector\_googlecalendar" | 5 more

Identifier for service connectors, like those available in ChatGPT. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided. Learn more
about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

Currently supported `connector_id` values are:

* Dropbox: `connector_dropbox`
* Gmail: `connector_gmail`
* Google Calendar: `connector_googlecalendar`
* Google Drive: `connector_googledrive`
* Microsoft Teams: `connector_microsoftteams`
* Outlook Calendar: `connector_outlookcalendar`
* Outlook Email: `connector_outlookemail`
* SharePoint: `connector_sharepoint`

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading?: boolean

Whether this MCP tool is deferred and discovered via tool search.

headers?: Record<string, string> | null

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

require\_approval?: McpToolApprovalFilter { always, never }  | "always" | "never" | null

Specify which of the MCP server’s tools require approval.

McpToolApprovalFilter { always, never }

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

always?: Always { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

never?: Never { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

"always" | "never"

"always"

"never"

server\_description?: string

Optional description of the MCP server, used to provide more context.

server\_url?: string

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

tunnel\_id?: string

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

CodeInterpreter { container, type, allowed\_callers }

A tool that runs Python code to help generate a response to a prompt.

container: string | CodeInterpreterToolAuto { type, file\_ids, memory\_limit, network\_policy }

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

string

CodeInterpreterToolAuto { type, file\_ids, memory\_limit, network\_policy }

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

type: "auto"

Always `auto`.

file\_ids?: Array<string>

An optional list of uploaded files to make available to your code.

memory\_limit?: "1g" | "4g" | "16g" | "64g" | null

The memory limit for the code interpreter container.

"1g"

"4g"

"16g"

"64g"

network\_policy?: [BetaContainerNetworkPolicyDisabled](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  | [BetaContainerNetworkPolicyAllowlist](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

BetaContainerNetworkPolicyDisabled { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

BetaContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array<string>

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets?: Array<[BetaContainerNetworkPolicyDomainSecret](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } >

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

minLength1

name: string

The name of the secret to inject for the domain.

minLength1

value: string

The secret value to inject for the domain.

maxLength10485760

minLength1

type: "code\_interpreter"

The type of the code interpreter tool. Always `code_interpreter`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

ProgrammaticToolCalling { type }

type: "programmatic\_tool\_calling"

The type of the tool. Always `programmatic_tool_calling`.

ImageGeneration { type, action, background, 9 more }

A tool that generates images using the GPT image models.

type: "image\_generation"

The type of the image generation tool. Always `image_generation`.

action?: "generate" | "edit" | "auto"

Whether to generate a new image or edit an existing image. Default: `auto`.

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

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

"high"

"low"

input\_image\_mask?: InputImageMask { file\_id, image\_url }

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

file\_id?: string

File ID for the mask image.

image\_url?: string

Base64-encoded mask image.

model?: (string & {}) | "gpt-image-1" | "gpt-image-1-mini" | "gpt-image-2" | 3 more

The image generation model to use. Default: `gpt-image-1`.

(string & {})

"gpt-image-1" | "gpt-image-1-mini" | "gpt-image-2" | 3 more

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation?: "auto" | "low"

Moderation level for the generated image. Default: `auto`.

"auto"

"low"

output\_compression?: number

Compression level for the output image. Default: 100.

minimum0

maximum100

output\_format?: "png" | "webp" | "jpeg"

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

"png"

"webp"

"jpeg"

partial\_images?: number

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

quality?: "low" | "medium" | "high" | "auto"

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

"low"

"medium"

"high"

"auto"

size?: (string & {}) | "1024x1024" | "1024x1536" | "1536x1024" | "auto"

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

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

A tool that allows the model to execute shell commands.

type: "shell"

The type of the shell tool. Always `shell`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

environment?: [BetaContainerAuto](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_auto%20%3E%20(schema)) { type, file\_ids, memory\_limit, 2 more }  | [BetaLocalEnvironment](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_environment%20%3E%20(schema)) { type, skills }  | [BetaContainerReference](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_reference%20%3E%20(schema)) { container\_id, type }  | null

BetaContainerAuto { type, file\_ids, memory\_limit, 2 more }

type: "container\_auto"

Automatically creates a container for this request

file\_ids?: Array<string>

An optional list of uploaded files to make available to your code.

memory\_limit?: "1g" | "4g" | "16g" | "64g" | null

The memory limit for the container.

"1g"

"4g"

"16g"

"64g"

network\_policy?: [BetaContainerNetworkPolicyDisabled](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  | [BetaContainerNetworkPolicyAllowlist](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

BetaContainerNetworkPolicyDisabled { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

BetaContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array<string>

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets?: Array<[BetaContainerNetworkPolicyDomainSecret](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } >

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

minLength1

name: string

The name of the secret to inject for the domain.

minLength1

value: string

The secret value to inject for the domain.

maxLength10485760

minLength1

skills?: Array<[BetaSkillReference](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_skill_reference%20%3E%20(schema)) { skill\_id, type, version }  | [BetaInlineSkill](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill%20%3E%20(schema)) { description, name, source, type } >

An optional list of skills referenced by id or inline data.

BetaSkillReference { skill\_id, type, version }

skill\_id: string

The ID of the referenced skill.

maxLength64

minLength1

type: "skill\_reference"

References a skill created with the /v1/skills endpoint.

version?: string

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

BetaInlineSkill { description, name, source, type }

description: string

The description of the skill.

name: string

The name of the skill.

source: [BetaInlineSkillSource](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema)) { data, media\_type, type }

Inline skill payload

data: string

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

media\_type: "application/zip"

The media type of the inline skill payload. Must be `application/zip`.

type: "base64"

The type of the inline skill source. Must be `base64`.

type: "inline"

Defines an inline skill for this request.

BetaLocalEnvironment { type, skills }

type: "local"

Use a local computer environment.

skills?: Array<[BetaLocalSkill](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema)) { description, name, path } >

An optional list of skills.

description: string

The description of the skill.

name: string

The name of the skill.

path: string

The path to the directory containing the skill.

BetaContainerReference { container\_id, type }

container\_id: string

The ID of the referenced container.

type: "container\_reference"

References a container created with the /v1/containers endpoint

BetaCustomTool { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this tool should be deferred and discovered via tool search.

description?: string

Optional description of the custom tool, used to provide more context.

format?: Text { type }  | Grammar { definition, syntax, type }

The input format for the custom tool. Default is unconstrained text.

Text { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar { definition, syntax, type }

A grammar defined by the user.

definition: string

The grammar definition.

syntax: "lark" | "regex"

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: "grammar"

Grammar format. Always `grammar`.

BetaNamespaceTool { description, name, tools, type }

Groups function/custom tools under a shared namespace.

description: string

A description of the namespace shown to the model.

minLength1

name: string

The namespace name used in tool calls (for example, `crm`).

minLength1

tools: Array<Function { name, type, allowed\_callers, 5 more }  | [BetaCustomTool](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_custom_tool%20%3E%20(schema)) { name, type, allowed\_callers, 3 more } >

The function/custom tools available inside this namespace.

Function { name, type, allowed\_callers, 5 more }

name: string

maxLength128

minLength1

type: "function"

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this function should be deferred and discovered via tool search.

description?: string | null

output\_schema?: Record<string, unknown> | null

A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

parameters?: unknown

strict?: boolean | null

Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

BetaCustomTool { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this tool should be deferred and discovered via tool search.

description?: string

Optional description of the custom tool, used to provide more context.

format?: Text { type }  | Grammar { definition, syntax, type }

The input format for the custom tool. Default is unconstrained text.

Text { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar { definition, syntax, type }

A grammar defined by the user.

definition: string

The grammar definition.

syntax: "lark" | "regex"

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: "grammar"

Grammar format. Always `grammar`.

type: "namespace"

The type of the tool. Always `namespace`.

BetaToolSearchTool { type, description, execution, parameters }

Hosted or BYOT tool search configuration for deferred tools.

type: "tool\_search"

The type of the tool. Always `tool_search`.

description?: string | null

Description shown to the model for a client-executed tool search tool.

execution?: "server" | "client"

Whether tool search is executed by the server or by the client.

"server"

"client"

parameters?: unknown

Parameter schema for a client-executed tool search tool.

BetaWebSearchPreviewTool { type, search\_content\_types, search\_context\_size, user\_location }

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: "web\_search\_preview" | "web\_search\_preview\_2025\_03\_11"

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types?: Array<"text" | "image">

"text"

"image"

search\_context\_size?: "low" | "medium" | "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

"low"

"medium"

"high"

user\_location?: UserLocation | null

The user’s location.

type: "approximate"

The type of location approximation. Always `approximate`.

city?: string | null

Free text input for the city of the user, e.g. `San Francisco`.

country?: string | null

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region?: string | null

Free text input for the region of the user, e.g. `California`.

timezone?: string | null

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

BetaApplyPatchTool { type, allowed\_callers }

Allows the assistant to create, delete, or update files using unified diffs.

type: "apply\_patch"

The type of the tool. Always `apply_patch`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

type: "additional\_tools"

The item type. Always `additional_tools`.

id?: string | null

The unique ID of this additional tools item.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

BetaResponseReasoningItem { id, summary, type, 4 more }

A description of the chain of thought used by a reasoning model while generating
a response. Be sure to include these items in your `input` to the Responses API
for subsequent turns of a conversation if you are manually
[managing context](https://platform.openai.com/docs/guides/conversation-state).

id: string

The unique identifier of the reasoning content.

summary: Array<Summary>

Reasoning summary content.

text: string

A summary of the reasoning output from the model so far.

type: "summary\_text"

The type of the object. Always `summary_text`.

type: "reasoning"

The type of the object. Always `reasoning`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

content?: Array<Content>

Reasoning text content.

text: string

The reasoning text from the model.

type: "reasoning\_text"

The type of the reasoning text. Always `reasoning_text`.

encrypted\_content?: string | null

The encrypted content of the reasoning item. This is populated by default
for reasoning items returned by `POST /v1/responses` and WebSocket
`response.create` requests.

status?: "in\_progress" | "completed" | "incomplete"

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

BetaResponseCompactionItemParam { encrypted\_content, type, id, agent }

A compaction item generated by the [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).

encrypted\_content: string

The encrypted content of the compaction summary.

maxLength10485760

type: "compaction"

The type of the item. Always `compaction`.

id?: string | null

The ID of the compaction item.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

ImageGenerationCall { id, result, status, 2 more }

An image generation request made by the model.

id: string

The unique ID of the image generation call.

result: string | null

The generated image encoded in base64.

status: "in\_progress" | "completed" | "generating" | "failed"

The status of the image generation call.

"in\_progress"

"completed"

"generating"

"failed"

type: "image\_generation\_call"

The type of the image generation call. Always `image_generation_call`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

BetaResponseCodeInterpreterToolCall { id, code, container\_id, 4 more }

A tool call to run code.

id: string

The unique ID of the code interpreter tool call.

code: string | null

The code to run, or null if not available.

container\_id: string

The ID of the container used to run the code.

outputs: Array<Logs { logs, type }  | Image { type, url } > | null

The outputs generated by the code interpreter, such as logs or images.
Can be null if no outputs are available.

Logs { logs, type }

The logs output from the code interpreter.

logs: string

The logs output from the code interpreter.

type: "logs"

The type of the output. Always `logs`.

Image { type, url }

The image output from the code interpreter.

type: "image"

The type of the output. Always `image`.

url: string

The URL of the image output from the code interpreter.

formaturi

status: "in\_progress" | "completed" | "incomplete" | 2 more

The status of the code interpreter tool call. Valid values are `in_progress`, `completed`, `incomplete`, `interpreting`, and `failed`.

"in\_progress"

"completed"

"incomplete"

"interpreting"

"failed"

type: "code\_interpreter\_call"

The type of the code interpreter tool call. Always `code_interpreter_call`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

LocalShellCall { id, action, call\_id, 3 more }

A tool call to run a command on the local shell.

id: string

The unique ID of the local shell call.

action: Action { command, env, type, 3 more }

Execute a shell command on the server.

command: Array<string>

The command to run.

env: Record<string, string>

Environment variables to set for the command.

type: "exec"

The type of the local shell action. Always `exec`.

timeout\_ms?: number | null

Optional timeout in milliseconds for the command.

user?: string | null

Optional user to run the command as.

working\_directory?: string | null

Optional working directory to run the command in.

call\_id: string

The unique ID of the local shell tool call generated by the model.

status: "in\_progress" | "completed" | "incomplete"

The status of the local shell call.

"in\_progress"

"completed"

"incomplete"

type: "local\_shell\_call"

The type of the local shell call. Always `local_shell_call`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

LocalShellCallOutput { id, output, type, 2 more }

The output of a local shell tool call.

id: string

The unique ID of the local shell tool call generated by the model.

output: string

A JSON string of the output of the local shell tool call.

type: "local\_shell\_call\_output"

The type of the local shell tool call output. Always `local_shell_call_output`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

status?: "in\_progress" | "completed" | "incomplete" | null

The status of the item. One of `in_progress`, `completed`, or `incomplete`.

"in\_progress"

"completed"

"incomplete"

ShellCall { action, call\_id, type, 5 more }

A tool representing a request to execute one or more shell commands.

action: Action { commands, max\_output\_length, timeout\_ms }

The shell commands and limits that describe how to run the tool call.

commands: Array<string>

Ordered shell commands for the execution environment to run.

max\_output\_length?: number | null

Maximum number of UTF-8 characters to capture from combined stdout and stderr output.

timeout\_ms?: number | null

Maximum wall-clock time in milliseconds to allow the shell commands to run.

call\_id: string

The unique ID of the shell tool call generated by the model.

maxLength64

minLength1

type: "shell\_call"

The type of the item. Always `shell_call`.

id?: string | null

The unique ID of the shell tool call. Populated when this item is returned via API.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

caller?: Direct { type }  | Program { caller\_id, type }  | null

The execution context that produced this tool call.

Direct { type }

type: "direct"

The caller type. Always `direct`.

Program { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

maxLength64

minLength1

type: "program"

The caller type. Always `program`.

environment?: [BetaLocalEnvironment](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_environment%20%3E%20(schema)) { type, skills }  | [BetaContainerReference](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_reference%20%3E%20(schema)) { container\_id, type }  | null

The environment to execute the shell commands in.

BetaLocalEnvironment { type, skills }

type: "local"

Use a local computer environment.

skills?: Array<[BetaLocalSkill](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema)) { description, name, path } >

An optional list of skills.

description: string

The description of the skill.

name: string

The name of the skill.

path: string

The path to the directory containing the skill.

BetaContainerReference { container\_id, type }

container\_id: string

The ID of the referenced container.

type: "container\_reference"

References a container created with the /v1/containers endpoint

status?: "in\_progress" | "completed" | "incomplete" | null

The status of the shell call. One of `in_progress`, `completed`, or `incomplete`.

"in\_progress"

"completed"

"incomplete"

ShellCallOutput { call\_id, output, type, 5 more }

The streamed output items emitted by a shell tool call.

call\_id: string

The unique ID of the shell tool call generated by the model.

maxLength64

minLength1

output: Array<[BetaResponseFunctionShellCallOutputContent](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_shell_call_output_content%20%3E%20(schema)) { outcome, stderr, stdout } >

Captured chunks of stdout and stderr output, along with their associated outcomes.

outcome: Timeout { type }  | Exit { exit\_code, type }

The exit or timeout outcome associated with this shell call.

Timeout { type }

Indicates that the shell call exceeded its configured time limit.

type: "timeout"

The outcome type. Always `timeout`.

Exit { exit\_code, type }

Indicates that the shell commands finished and returned an exit code.

exit\_code: number

The exit code returned by the shell process.

type: "exit"

The outcome type. Always `exit`.

stderr: string

Captured stderr output for the shell call.

maxLength10485760

stdout: string

Captured stdout output for the shell call.

maxLength10485760

type: "shell\_call\_output"

The type of the item. Always `shell_call_output`.

id?: string | null

The unique ID of the shell tool call output. Populated when this item is returned via API.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

caller?: Direct { type }  | Program { caller\_id, type }  | null

The execution context that produced this tool call.

Direct { type }

type: "direct"

The caller type. Always `direct`.

Program { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

maxLength64

minLength1

type: "program"

The caller type. Always `program`.

max\_output\_length?: number | null

The maximum number of UTF-8 characters captured for this shell call’s combined output.

status?: "in\_progress" | "completed" | "incomplete" | null

The status of the shell call output.

"in\_progress"

"completed"

"incomplete"

ApplyPatchCall { call\_id, operation, status, 4 more }

A tool call representing a request to create, delete, or update files using diff patches.

call\_id: string

The unique ID of the apply patch tool call generated by the model.

maxLength64

minLength1

operation: CreateFile { diff, path, type }  | DeleteFile { path, type }  | UpdateFile { diff, path, type }

The specific create, delete, or update instruction for the apply\_patch tool call.

CreateFile { diff, path, type }

Instruction for creating a new file via the apply\_patch tool.

diff: string

Unified diff content to apply when creating the file.

maxLength10485760

path: string

Path of the file to create relative to the workspace root.

minLength1

type: "create\_file"

The operation type. Always `create_file`.

DeleteFile { path, type }

Instruction for deleting an existing file via the apply\_patch tool.

path: string

Path of the file to delete relative to the workspace root.

minLength1

type: "delete\_file"

The operation type. Always `delete_file`.

UpdateFile { diff, path, type }

Instruction for updating an existing file via the apply\_patch tool.

diff: string

Unified diff content to apply to the existing file.

maxLength10485760

path: string

Path of the file to update relative to the workspace root.

minLength1

type: "update\_file"

The operation type. Always `update_file`.

status: "in\_progress" | "completed"

The status of the apply patch tool call. One of `in_progress` or `completed`.

"in\_progress"

"completed"

type: "apply\_patch\_call"

The type of the item. Always `apply_patch_call`.

id?: string | null

The unique ID of the apply patch tool call. Populated when this item is returned via API.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

caller?: Direct { type }  | Program { caller\_id, type }  | null

The execution context that produced this tool call.

Direct { type }

type: "direct"

The caller type. Always `direct`.

Program { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

maxLength64

minLength1

type: "program"

The caller type. Always `program`.

ApplyPatchCallOutput { call\_id, status, type, 4 more }

The streamed output emitted by an apply patch tool call.

call\_id: string

The unique ID of the apply patch tool call generated by the model.

maxLength64

minLength1

status: "completed" | "failed"

The status of the apply patch tool call output. One of `completed` or `failed`.

"completed"

"failed"

type: "apply\_patch\_call\_output"

The type of the item. Always `apply_patch_call_output`.

id?: string | null

The unique ID of the apply patch tool call output. Populated when this item is returned via API.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

caller?: Direct { type }  | Program { caller\_id, type }  | null

The execution context that produced this tool call.

Direct { type }

type: "direct"

The caller type. Always `direct`.

Program { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

maxLength64

minLength1

type: "program"

The caller type. Always `program`.

output?: string | null

Optional human-readable log text from the apply patch tool (e.g., patch results or errors).

maxLength10485760

McpListTools { id, server\_label, tools, 3 more }

A list of tools available on an MCP server.

id: string

The unique ID of the list.

server\_label: string

The label of the MCP server.

tools: Array<Tool>

The tools available on the server.

input\_schema: unknown

The JSON schema describing the tool’s input.

name: string

The name of the tool.

annotations?: unknown

Additional annotations about the tool.

description?: string | null

The description of the tool.

type: "mcp\_list\_tools"

The type of the item. Always `mcp_list_tools`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

error?: string | null

Error message if the server could not list tools.

McpApprovalRequest { id, arguments, name, 3 more }

A request for human approval of a tool invocation.

id: string

The unique ID of the approval request.

arguments: string

A JSON string of arguments for the tool.

name: string

The name of the tool to run.

server\_label: string

The label of the MCP server making the request.

type: "mcp\_approval\_request"

The type of the item. Always `mcp_approval_request`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

McpApprovalResponse { approval\_request\_id, approve, type, 3 more }

A response to an MCP approval request.

approval\_request\_id: string

The ID of the approval request being answered.

approve: boolean

Whether the request was approved.

type: "mcp\_approval\_response"

The type of the item. Always `mcp_approval_response`.

id?: string | null

The unique ID of the approval response

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

reason?: string | null

Optional reason for the decision.

McpCall { id, arguments, name, 7 more }

An invocation of a tool on an MCP server.

id: string

The unique ID of the tool call.

arguments: string

A JSON string of the arguments passed to the tool.

name: string

The name of the tool that was run.

server\_label: string

The label of the MCP server running the tool.

type: "mcp\_call"

The type of the item. Always `mcp_call`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

approval\_request\_id?: string | null

Unique identifier for the MCP tool call approval request.
Include this value in a subsequent `mcp_approval_response` input to approve or reject the corresponding tool call.

error?: string | null

The error from the tool call, if any.

output?: string | null

The output from the tool call.

status?: "in\_progress" | "completed" | "incomplete" | 2 more

The status of the tool call. One of `in_progress`, `completed`, `incomplete`, `calling`, or `failed`.

"in\_progress"

"completed"

"incomplete"

"calling"

"failed"

BetaResponseCustomToolCallOutput { call\_id, output, type, 3 more }

The output of a custom tool call from your code, being sent back to the model.

call\_id: string

The call ID, used to map this custom tool call output to a custom tool call.

output: string | Array<[BetaResponseInputText](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_text%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  | [BetaResponseInputImage](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_image%20%3E%20(schema)) { detail, type, file\_id, 2 more }  | [BetaResponseInputFile](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_file%20%3E%20(schema)) { type, detail, file\_data, 4 more } >

The output from the custom tool call generated by your code.
Can be a string or an list of output content.

string

Array<[BetaResponseInputText](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_text%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  | [BetaResponseInputImage](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_image%20%3E%20(schema)) { detail, type, file\_id, 2 more }  | [BetaResponseInputFile](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_file%20%3E%20(schema)) { type, detail, file\_data, 4 more } >

BetaResponseInputText { text, type, prompt\_cache\_breakpoint }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

BetaResponseInputImage { detail, type, file\_id, 2 more }

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: "low" | "high" | "auto" | "original"

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

"low"

"high"

"auto"

"original"

type: "input\_image"

The type of the input item. Always `input_image`.

file\_id?: string | null

The ID of the file to be sent to the model.

image\_url?: string | null

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

BetaResponseInputFile { type, detail, file\_data, 4 more }

A file input to the model.

type: "input\_file"

The type of the input item. Always `input_file`.

detail?: "auto" | "low" | "high"

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

"auto"

"low"

"high"

file\_data?: string

The content of the file to be sent to the model.

file\_id?: string | null

The ID of the file to be sent to the model.

file\_url?: string

The URL of the file to be sent to the model.

formaturi

filename?: string

The name of the file to be sent to the model.

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

type: "custom\_tool\_call\_output"

The type of the custom tool call output. Always `custom_tool_call_output`.

id?: string

The unique ID of the custom tool call output in the OpenAI platform.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

caller?: Direct { type }  | Program { caller\_id, type }  | null

The execution context that produced this tool call.

Direct { type }

type: "direct"

The caller type. Always `direct`.

Program { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

maxLength64

minLength1

type: "program"

The caller type. Always `program`.

BetaResponseCustomToolCall { call\_id, input, name, 5 more }

A call to a custom tool created by the model.

call\_id: string

An identifier used to map this custom tool call to a tool call output.

input: string

The input for the custom tool call generated by the model.

name: string

The name of the custom tool being called.

type: "custom\_tool\_call"

The type of the custom tool call. Always `custom_tool_call`.

id?: string

The unique ID of the custom tool call in the OpenAI platform.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

caller?: Direct { type }  | Program { caller\_id, type }  | null

The execution context that produced this tool call.

Direct { type }

type: "direct"

Program { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

type: "program"

namespace?: string

The namespace of the custom tool being called.

CompactionTrigger { type, agent }

Compacts the current context. Must be the final input item.

type: "compaction\_trigger"

The type of the item. Always `compaction_trigger`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

ItemReference { id, agent, type }

An internal identifier for an item to reference.

id: string

The ID of the item to reference.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

type?: "item\_reference" | null

The type of item to reference. Always `item_reference`.

Program { id, call\_id, code, 3 more }

id: string

The unique ID of this program item.

call\_id: string

The stable call ID of the program item.

maxLength64

minLength1

code: string

The JavaScript source executed by programmatic tool calling.

maxLength10485760

fingerprint: string

Opaque program replay fingerprint that must be round-tripped.

maxLength10485760

type: "program"

The item type. Always `program`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

ProgramOutput { id, call\_id, result, 3 more }

id: string

The unique ID of this program output item.

call\_id: string

The call ID of the program item.

maxLength64

minLength1

result: string

The result produced by the program item.

maxLength10485760

status: "completed" | "incomplete"

The terminal status of the program output.

"completed"

"incomplete"

type: "program\_output"

The item type. Always `program_output`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

metadata: Record<string, string> | null

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: "gpt-5.6-sol" | "gpt-5.6-terra" | "gpt-5.6-luna" | 92 more | (string & {})

Model ID used to generate the response, like `gpt-4o` or `o3`. OpenAI
offers a wide range of models with different capabilities, performance
characteristics, and price points. Refer to the [model guide](https://platform.openai.com/docs/models)
to browse and compare available models.

"gpt-5.6-sol" | "gpt-5.6-terra" | "gpt-5.6-luna" | 92 more

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

(string & {})

object: "response"

The object type of this resource - always set to `response`.

output: Array<[BetaResponseOutputItem](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_item%20%3E%20(schema))>

An array of content items generated by the model.

* The length and order of items in the `output` array is dependent
  on the model’s response.
* Rather than accessing the first item in the `output` array and
  assuming it’s an `assistant` message with the content generated by
  the model, you might consider using the `output_text` property where
  supported in SDKs.

BetaResponseOutputMessage { id, content, role, 4 more }

An output message from the model.

id: string

The unique ID of the output message.

content: Array<[BetaResponseOutputText](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_text%20%3E%20(schema)) { annotations, text, type, logprobs }  | [BetaResponseOutputRefusal](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_refusal%20%3E%20(schema)) { refusal, type } >

The content of the output message.

BetaResponseOutputText { annotations, text, type, logprobs }

A text output from the model.

annotations: Array<FileCitation { file\_id, filename, index, type }  | URLCitation { end\_index, start\_index, title, 2 more }  | ContainerFileCitation { container\_id, end\_index, file\_id, 3 more }  | FilePath { file\_id, index, type } >

The annotations of the text output.

FileCitation { file\_id, filename, index, type }

A citation to a file.

file\_id: string

The ID of the file.

filename: string

The filename of the file cited.

index: number

The index of the file in the list of files.

type: "file\_citation"

The type of the file citation. Always `file_citation`.

URLCitation { end\_index, start\_index, title, 2 more }

A citation for a web resource used to generate a model response.

end\_index: number

The index of the last character of the URL citation in the message.

start\_index: number

The index of the first character of the URL citation in the message.

title: string

The title of the web resource.

type: "url\_citation"

The type of the URL citation. Always `url_citation`.

url: string

The URL of the web resource.

formaturi

ContainerFileCitation { container\_id, end\_index, file\_id, 3 more }

A citation for a container file used to generate a model response.

container\_id: string

The ID of the container file.

end\_index: number

The index of the last character of the container file citation in the message.

file\_id: string

The ID of the file.

filename: string

The filename of the container file cited.

start\_index: number

The index of the first character of the container file citation in the message.

type: "container\_file\_citation"

The type of the container file citation. Always `container_file_citation`.

FilePath { file\_id, index, type }

A path to a file.

file\_id: string

The ID of the file.

index: number

The index of the file in the list of files.

type: "file\_path"

The type of the file path. Always `file_path`.

text: string

The text output from the model.

type: "output\_text"

The type of the output text. Always `output_text`.

logprobs?: Array<Logprob>

token: string

bytes: Array<number>

logprob: number

top\_logprobs: Array<TopLogprob>

token: string

bytes: Array<number>

logprob: number

BetaResponseOutputRefusal { refusal, type }

A refusal from the model.

refusal: string

The refusal explanation from the model.

type: "refusal"

The type of the refusal. Always `refusal`.

role: "assistant"

The role of the output message. Always `assistant`.

status: "in\_progress" | "completed" | "incomplete"

The status of the message input. One of `in_progress`, `completed`, or
`incomplete`. Populated when input items are returned via API.

"in\_progress"

"completed"

"incomplete"

type: "message"

The type of the output message. Always `message`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

phase?: "commentary" | "final\_answer" | null

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

"commentary"

"final\_answer"

BetaResponseFileSearchToolCall { id, queries, status, 3 more }

The results of a file search tool call. See the
[file search guide](https://platform.openai.com/docs/guides/tools-file-search) for more information.

id: string

The unique ID of the file search tool call.

queries: Array<string>

The queries used to search for files.

status: "in\_progress" | "searching" | "completed" | 2 more

The status of the file search tool call. One of `in_progress`,
`searching`, `incomplete` or `failed`,

"in\_progress"

"searching"

"completed"

"incomplete"

"failed"

type: "file\_search\_call"

The type of the file search tool call. Always `file_search_call`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

results?: Array<Result> | null

The results of the file search tool call.

attributes?: Record<string, string | number | boolean> | null

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.

string

number

boolean

file\_id?: string

The unique ID of the file.

filename?: string

The name of the file.

score?: number

The relevance score of the file - a value between 0 and 1.

formatfloat

text?: string

The text that was retrieved from the file.

BetaResponseFunctionToolCall { arguments, call\_id, name, 6 more }

A tool call to run a function. See the
[function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.

arguments: string

A JSON string of the arguments to pass to the function.

call\_id: string

The unique ID of the function tool call generated by the model.

name: string

The name of the function to run.

type: "function\_call"

The type of the function tool call. Always `function_call`.

id?: string

The unique ID of the function tool call.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

caller?: Direct { type }  | Program { caller\_id, type }  | null

The execution context that produced this tool call.

Direct { type }

type: "direct"

Program { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

type: "program"

namespace?: string

The namespace of the function to run.

status?: "in\_progress" | "completed" | "incomplete"

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

BetaResponseFunctionToolCallOutputItem { id, call\_id, output, 5 more }

id: string

The unique ID of the function call tool output.

call\_id: string

The unique ID of the function tool call generated by the model.

output: string | Array<[BetaResponseInputText](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_text%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  | [BetaResponseInputImage](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_image%20%3E%20(schema)) { detail, type, file\_id, 2 more }  | [BetaResponseInputFile](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_file%20%3E%20(schema)) { type, detail, file\_data, 4 more } >

The output from the function call generated by your code.
Can be a string or an list of output content.

string

Array<[BetaResponseInputText](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_text%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  | [BetaResponseInputImage](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_image%20%3E%20(schema)) { detail, type, file\_id, 2 more }  | [BetaResponseInputFile](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_file%20%3E%20(schema)) { type, detail, file\_data, 4 more } >

BetaResponseInputText { text, type, prompt\_cache\_breakpoint }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

BetaResponseInputImage { detail, type, file\_id, 2 more }

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: "low" | "high" | "auto" | "original"

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

"low"

"high"

"auto"

"original"

type: "input\_image"

The type of the input item. Always `input_image`.

file\_id?: string | null

The ID of the file to be sent to the model.

image\_url?: string | null

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

BetaResponseInputFile { type, detail, file\_data, 4 more }

A file input to the model.

type: "input\_file"

The type of the input item. Always `input_file`.

detail?: "auto" | "low" | "high"

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

"auto"

"low"

"high"

file\_data?: string

The content of the file to be sent to the model.

file\_id?: string | null

The ID of the file to be sent to the model.

file\_url?: string

The URL of the file to be sent to the model.

formaturi

filename?: string

The name of the file to be sent to the model.

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

status: "in\_progress" | "completed" | "incomplete"

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

type: "function\_call\_output"

The type of the function tool call output. Always `function_call_output`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

caller?: Direct { type }  | Program { caller\_id, type }  | null

The execution context that produced this tool call.

Direct { type }

type: "direct"

The caller type. Always `direct`.

Program { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

maxLength64

minLength1

type: "program"

The caller type. Always `program`.

created\_by?: string

The identifier of the actor that created the item.

AgentMessage { id, author, content, 3 more }

id: string

The unique ID of the agent message.

author: string

The sending agent identity.

content: Array<[BetaResponseInputText](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_text%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  | [BetaResponseOutputText](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_text%20%3E%20(schema)) { annotations, text, type, logprobs }  | Text { text, type }  | 7 more>

Encrypted content sent between agents.

BetaResponseInputText { text, type, prompt\_cache\_breakpoint }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

BetaResponseOutputText { annotations, text, type, logprobs }

A text output from the model.

annotations: Array<FileCitation { file\_id, filename, index, type }  | URLCitation { end\_index, start\_index, title, 2 more }  | ContainerFileCitation { container\_id, end\_index, file\_id, 3 more }  | FilePath { file\_id, index, type } >

The annotations of the text output.

FileCitation { file\_id, filename, index, type }

A citation to a file.

file\_id: string

The ID of the file.

filename: string

The filename of the file cited.

index: number

The index of the file in the list of files.

type: "file\_citation"

The type of the file citation. Always `file_citation`.

URLCitation { end\_index, start\_index, title, 2 more }

A citation for a web resource used to generate a model response.

end\_index: number

The index of the last character of the URL citation in the message.

start\_index: number

The index of the first character of the URL citation in the message.

title: string

The title of the web resource.

type: "url\_citation"

The type of the URL citation. Always `url_citation`.

url: string

The URL of the web resource.

formaturi

ContainerFileCitation { container\_id, end\_index, file\_id, 3 more }

A citation for a container file used to generate a model response.

container\_id: string

The ID of the container file.

end\_index: number

The index of the last character of the container file citation in the message.

file\_id: string

The ID of the file.

filename: string

The filename of the container file cited.

start\_index: number

The index of the first character of the container file citation in the message.

type: "container\_file\_citation"

The type of the container file citation. Always `container_file_citation`.

FilePath { file\_id, index, type }

A path to a file.

file\_id: string

The ID of the file.

index: number

The index of the file in the list of files.

type: "file\_path"

The type of the file path. Always `file_path`.

text: string

The text output from the model.

type: "output\_text"

The type of the output text. Always `output_text`.

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

A summary of the reasoning output from the model so far.

type: "summary\_text"

The type of the object. Always `summary_text`.

ReasoningText { text, type }

Reasoning text from the model.

text: string

The reasoning text from the model.

type: "reasoning\_text"

The type of the reasoning text. Always `reasoning_text`.

BetaResponseOutputRefusal { refusal, type }

A refusal from the model.

refusal: string

The refusal explanation from the model.

type: "refusal"

The type of the refusal. Always `refusal`.

BetaResponseInputImage { detail, type, file\_id, 2 more }

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: "low" | "high" | "auto" | "original"

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

"low"

"high"

"auto"

"original"

type: "input\_image"

The type of the input item. Always `input_image`.

file\_id?: string | null

The ID of the file to be sent to the model.

image\_url?: string | null

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

ComputerScreenshot { detail, file\_id, image\_url, 2 more }

A screenshot of a computer.

detail: "low" | "high" | "auto" | "original"

The detail level of the screenshot image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

"low"

"high"

"auto"

"original"

file\_id: string | null

The identifier of an uploaded file that contains the screenshot.

image\_url: string | null

The URL of the screenshot image.

formaturi

type: "computer\_screenshot"

Specifies the event type. For a computer screenshot, this property is always set to `computer_screenshot`.

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

BetaResponseInputFile { type, detail, file\_data, 4 more }

A file input to the model.

type: "input\_file"

The type of the input item. Always `input_file`.

detail?: "auto" | "low" | "high"

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

"auto"

"low"

"high"

file\_data?: string

The content of the file to be sent to the model.

file\_id?: string | null

The ID of the file to be sent to the model.

file\_url?: string

The URL of the file to be sent to the model.

formaturi

filename?: string

The name of the file to be sent to the model.

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

EncryptedContent { encrypted\_content, type }

Opaque encrypted content that Responses API decrypts inside trusted model execution.

encrypted\_content: string

Opaque encrypted content.

type: "encrypted\_content"

The type of the input item. Always `encrypted_content`.

recipient: string

The destination agent identity.

type: "agent\_message"

The type of the item. Always `agent_message`.

agent?: Agent { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

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

The unique ID linking this call to its output.

type: "multi\_agent\_call"

The type of the multi-agent call. Always `multi_agent_call`.

agent?: Agent { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

MultiAgentCallOutput { id, action, call\_id, 3 more }

id: string

The unique ID of the multi-agent call output item.

action: "spawn\_agent" | "interrupt\_agent" | "list\_agents" | 3 more

The multi-agent action that produced this result.

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

call\_id: string

The unique ID of the multi-agent call.

output: Array<[BetaResponseOutputText](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_text%20%3E%20(schema)) { annotations, text, type, logprobs } >

Text output returned by the multi-agent action.

annotations: Array<FileCitation { file\_id, filename, index, type }  | URLCitation { end\_index, start\_index, title, 2 more }  | ContainerFileCitation { container\_id, end\_index, file\_id, 3 more }  | FilePath { file\_id, index, type } >

The annotations of the text output.

FileCitation { file\_id, filename, index, type }

A citation to a file.

file\_id: string

The ID of the file.

filename: string

The filename of the file cited.

index: number

The index of the file in the list of files.

type: "file\_citation"

The type of the file citation. Always `file_citation`.

URLCitation { end\_index, start\_index, title, 2 more }

A citation for a web resource used to generate a model response.

end\_index: number

The index of the last character of the URL citation in the message.

start\_index: number

The index of the first character of the URL citation in the message.

title: string

The title of the web resource.

type: "url\_citation"

The type of the URL citation. Always `url_citation`.

url: string

The URL of the web resource.

formaturi

ContainerFileCitation { container\_id, end\_index, file\_id, 3 more }

A citation for a container file used to generate a model response.

container\_id: string

The ID of the container file.

end\_index: number

The index of the last character of the container file citation in the message.

file\_id: string

The ID of the file.

filename: string

The filename of the container file cited.

start\_index: number

The index of the first character of the container file citation in the message.

type: "container\_file\_citation"

The type of the container file citation. Always `container_file_citation`.

FilePath { file\_id, index, type }

A path to a file.

file\_id: string

The ID of the file.

index: number

The index of the file in the list of files.

type: "file\_path"

The type of the file path. Always `file_path`.

text: string

The text output from the model.

type: "output\_text"

The type of the output text. Always `output_text`.

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

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

BetaResponseFunctionWebSearch { id, action, status, 2 more }

The results of a web search tool call. See the
[web search guide](https://platform.openai.com/docs/guides/tools-web-search) for more information.

id: string

The unique ID of the web search tool call.

action: Search { type, queries, query, sources }  | OpenPage { type, url }  | FindInPage { pattern, type, url }

An object describing the specific action taken in this web search call.
Includes details on how the model used the web (search, open\_page, find\_in\_page).

Search { type, queries, query, sources }

Action type “search” - Performs a web search query.

type: "search"

The action type.

queries?: Array<string>

The search queries.

Deprecatedquery?: string

The search query.

sources?: Array<Source>

The sources used in the search.

type: "url"

The type of source. Always `url`.

url: string

The URL of the source.

formaturi

OpenPage { type, url }

Action type “open\_page” - Opens a specific URL from search results.

type: "open\_page"

The action type.

url?: string | null

The URL opened by the model.

formaturi

FindInPage { pattern, type, url }

Action type “find\_in\_page”: Searches for a pattern within a loaded page.

pattern: string

The pattern or text to search for within the page.

type: "find\_in\_page"

The action type.

url: string

The URL of the page searched for the pattern.

formaturi

status: "in\_progress" | "searching" | "completed" | "failed"

The status of the web search tool call.

"in\_progress"

"searching"

"completed"

"failed"

type: "web\_search\_call"

The type of the web search tool call. Always `web_search_call`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

BetaResponseComputerToolCall { id, call\_id, pending\_safety\_checks, 5 more }

A tool call to a computer use tool. See the
[computer use guide](https://platform.openai.com/docs/guides/tools-computer-use) for more information.

id: string

The unique ID of the computer call.

call\_id: string

An identifier used when responding to the tool call with output.

pending\_safety\_checks: Array<PendingSafetyCheck>

The pending safety checks for the computer call.

id: string

The ID of the pending safety check.

code?: string | null

The type of the pending safety check.

message?: string | null

Details about the pending safety check.

status: "in\_progress" | "completed" | "incomplete"

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

type: "computer\_call"

The type of the computer call. Always `computer_call`.

action?: [BetaComputerAction](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_computer_action%20%3E%20(schema))

A click action.

Click { button, type, x, 2 more }

A click action.

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

[
  { x: 100, y: 200 },
  { x: 200, y: 300 }
]

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

Flattened batched actions for `computer_use`. Each action includes an
`type` discriminator and action-specific fields.

Click { button, type, x, 2 more }

A click action.

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

[
  { x: 100, y: 200 },
  { x: 200, y: 300 }
]

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

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

BetaResponseComputerToolCallOutputItem { id, call\_id, output, 5 more }

id: string

The unique ID of the computer call tool output.

call\_id: string

The ID of the computer tool call that produced the output.

output: [BetaResponseComputerToolCallOutputScreenshot](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_computer_tool_call_output_screenshot%20%3E%20(schema)) { type, file\_id, image\_url }

A computer screenshot image used with the computer use tool.

type: "computer\_screenshot"

Specifies the event type. For a computer screenshot, this property is
always set to `computer_screenshot`.

file\_id?: string

The identifier of an uploaded file that contains the screenshot.

image\_url?: string

The URL of the screenshot image.

formaturi

status: "completed" | "incomplete" | "failed" | "in\_progress"

The status of the message input. One of `in_progress`, `completed`, or
`incomplete`. Populated when input items are returned via API.

"completed"

"incomplete"

"failed"

"in\_progress"

type: "computer\_call\_output"

The type of the computer tool call output. Always `computer_call_output`.

acknowledged\_safety\_checks?: Array<AcknowledgedSafetyCheck>

The safety checks reported by the API that have been acknowledged by the
developer.

id: string

The ID of the pending safety check.

code?: string | null

The type of the pending safety check.

message?: string | null

Details about the pending safety check.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

created\_by?: string

The identifier of the actor that created the item.

BetaResponseReasoningItem { id, summary, type, 4 more }

A description of the chain of thought used by a reasoning model while generating
a response. Be sure to include these items in your `input` to the Responses API
for subsequent turns of a conversation if you are manually
[managing context](https://platform.openai.com/docs/guides/conversation-state).

id: string

The unique identifier of the reasoning content.

summary: Array<Summary>

Reasoning summary content.

text: string

A summary of the reasoning output from the model so far.

type: "summary\_text"

The type of the object. Always `summary_text`.

type: "reasoning"

The type of the object. Always `reasoning`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

content?: Array<Content>

Reasoning text content.

text: string

The reasoning text from the model.

type: "reasoning\_text"

The type of the reasoning text. Always `reasoning_text`.

encrypted\_content?: string | null

The encrypted content of the reasoning item. This is populated by default
for reasoning items returned by `POST /v1/responses` and WebSocket
`response.create` requests.

status?: "in\_progress" | "completed" | "incomplete"

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

Program { id, call\_id, code, 3 more }

id: string

The unique ID of the program item.

call\_id: string

The stable call ID of the program item.

code: string

The JavaScript source executed by programmatic tool calling.

fingerprint: string

Opaque program replay fingerprint that must be round-tripped.

type: "program"

The type of the item. Always `program`.

agent?: Agent { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

ProgramOutput { id, call\_id, result, 3 more }

id: string

The unique ID of the program output item.

call\_id: string

The call ID of the program item.

result: string

The result produced by the program item.

status: "completed" | "incomplete"

The terminal status of the program output item.

"completed"

"incomplete"

type: "program\_output"

The type of the item. Always `program_output`.

agent?: Agent { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

BetaResponseToolSearchCall { id, arguments, call\_id, 5 more }

id: string

The unique ID of the tool search call item.

arguments: unknown

Arguments used for the tool search call.

call\_id: string | null

The unique ID of the tool search call generated by the model.

execution: "server" | "client"

Whether tool search was executed by the server or by the client.

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

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

created\_by?: string

The identifier of the actor that created the item.

BetaResponseToolSearchOutputItem { id, call\_id, execution, 5 more }

id: string

The unique ID of the tool search output item.

call\_id: string | null

The unique ID of the tool search call generated by the model.

execution: "server" | "client"

Whether tool search was executed by the server or by the client.

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

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

name: string

The name of the function to call.

parameters: Record<string, unknown> | null

A JSON schema object describing the parameters of the function.

strict: boolean | null

Whether strict parameter validation is enforced for this function tool.

type: "function"

The type of the function tool. Always `function`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this function is deferred and loaded via tool search.

description?: string | null

A description of the function. Used by the model to determine whether or not to call the function.

output\_schema?: Record<string, unknown> | null

A JSON schema object describing the JSON value encoded in string outputs for this function.

BetaFileSearchTool { type, vector\_store\_ids, filters, 2 more }

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

type: "file\_search"

The type of the file search tool. Always `file_search`.

vector\_store\_ids: Array<string>

The IDs of the vector stores to search.

filters?: ComparisonFilter { key, type, value }  | CompoundFilter { filters, type }  | null

A filter to apply.

ComparisonFilter { key, type, value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: string

The key to compare against the value.

type: "eq" | "ne" | "gt" | 5 more

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: string | number | boolean | Array<string | number>

The value to compare against the attribute key; supports string, number, or boolean types.

string

number

boolean

Array<string | number>

string

number

CompoundFilter { filters, type }

Combine multiple filters using `and` or `or`.

filters: Array<ComparisonFilter { key, type, value }  | unknown>

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

ComparisonFilter { key, type, value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: string

The key to compare against the value.

type: "eq" | "ne" | "gt" | 5 more

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: string | number | boolean | Array<string | number>

The value to compare against the attribute key; supports string, number, or boolean types.

string

number

boolean

Array<string | number>

string

number

unknown

type: "and" | "or"

Type of operation: `and` or `or`.

"and"

"or"

max\_num\_results?: number

The maximum number of results to return. This number should be between 1 and 50 inclusive.

ranking\_options?: RankingOptions { hybrid\_search, ranker, score\_threshold }

Ranking options for search.

hybrid\_search?: HybridSearch { embedding\_weight, text\_weight }

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

embedding\_weight: number

The weight of the embedding in the reciprocal ranking fusion.

text\_weight: number

The weight of the text in the reciprocal ranking fusion.

ranker?: "auto" | "default-2024-11-15"

The ranker to use for the file search.

"auto"

"default-2024-11-15"

score\_threshold?: number

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

BetaComputerTool { type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

type: "computer"

The type of the computer tool. Always `computer`.

BetaComputerUsePreviewTool { display\_height, display\_width, environment, type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

display\_height: number

The height of the computer display.

display\_width: number

The width of the computer display.

environment: "windows" | "mac" | "linux" | 2 more

The type of computer environment to control.

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: "computer\_use\_preview"

The type of the computer use tool. Always `computer_use_preview`.

BetaWebSearchTool { type, filters, search\_context\_size, user\_location }

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: "web\_search" | "web\_search\_2025\_08\_26"

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

"web\_search"

"web\_search\_2025\_08\_26"

filters?: Filters | null

Filters for the search.

allowed\_domains?: Array<string> | null

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

search\_context\_size?: "low" | "medium" | "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

"low"

"medium"

"high"

user\_location?: UserLocation | null

The approximate location of the user.

city?: string | null

Free text input for the city of the user, e.g. `San Francisco`.

country?: string | null

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region?: string | null

Free text input for the region of the user, e.g. `California`.

timezone?: string | null

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

type?: "approximate"

The type of location approximation. Always `approximate`.

Mcp { server\_label, type, allowed\_callers, 9 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: string

A label for this MCP server, used to identify it in tool calls.

type: "mcp"

The type of the MCP tool. Always `mcp`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

allowed\_tools?: Array<string> | McpToolFilter { read\_only, tool\_names }  | null

List of allowed tool names or a filter object.

Array<string>

McpToolFilter { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

authorization?: string

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

connector\_id?: "connector\_dropbox" | "connector\_gmail" | "connector\_googlecalendar" | 5 more

Identifier for service connectors, like those available in ChatGPT. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided. Learn more
about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

Currently supported `connector_id` values are:

* Dropbox: `connector_dropbox`
* Gmail: `connector_gmail`
* Google Calendar: `connector_googlecalendar`
* Google Drive: `connector_googledrive`
* Microsoft Teams: `connector_microsoftteams`
* Outlook Calendar: `connector_outlookcalendar`
* Outlook Email: `connector_outlookemail`
* SharePoint: `connector_sharepoint`

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading?: boolean

Whether this MCP tool is deferred and discovered via tool search.

headers?: Record<string, string> | null

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

require\_approval?: McpToolApprovalFilter { always, never }  | "always" | "never" | null

Specify which of the MCP server’s tools require approval.

McpToolApprovalFilter { always, never }

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

always?: Always { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

never?: Never { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

"always" | "never"

"always"

"never"

server\_description?: string

Optional description of the MCP server, used to provide more context.

server\_url?: string

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

tunnel\_id?: string

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

CodeInterpreter { container, type, allowed\_callers }

A tool that runs Python code to help generate a response to a prompt.

container: string | CodeInterpreterToolAuto { type, file\_ids, memory\_limit, network\_policy }

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

string

CodeInterpreterToolAuto { type, file\_ids, memory\_limit, network\_policy }

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

type: "auto"

Always `auto`.

file\_ids?: Array<string>

An optional list of uploaded files to make available to your code.

memory\_limit?: "1g" | "4g" | "16g" | "64g" | null

The memory limit for the code interpreter container.

"1g"

"4g"

"16g"

"64g"

network\_policy?: [BetaContainerNetworkPolicyDisabled](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  | [BetaContainerNetworkPolicyAllowlist](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

BetaContainerNetworkPolicyDisabled { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

BetaContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array<string>

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets?: Array<[BetaContainerNetworkPolicyDomainSecret](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } >

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

minLength1

name: string

The name of the secret to inject for the domain.

minLength1

value: string

The secret value to inject for the domain.

maxLength10485760

minLength1

type: "code\_interpreter"

The type of the code interpreter tool. Always `code_interpreter`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

ProgrammaticToolCalling { type }

type: "programmatic\_tool\_calling"

The type of the tool. Always `programmatic_tool_calling`.

ImageGeneration { type, action, background, 9 more }

A tool that generates images using the GPT image models.

type: "image\_generation"

The type of the image generation tool. Always `image_generation`.

action?: "generate" | "edit" | "auto"

Whether to generate a new image or edit an existing image. Default: `auto`.

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

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

"high"

"low"

input\_image\_mask?: InputImageMask { file\_id, image\_url }

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

file\_id?: string

File ID for the mask image.

image\_url?: string

Base64-encoded mask image.

model?: (string & {}) | "gpt-image-1" | "gpt-image-1-mini" | "gpt-image-2" | 3 more

The image generation model to use. Default: `gpt-image-1`.

(string & {})

"gpt-image-1" | "gpt-image-1-mini" | "gpt-image-2" | 3 more

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation?: "auto" | "low"

Moderation level for the generated image. Default: `auto`.

"auto"

"low"

output\_compression?: number

Compression level for the output image. Default: 100.

minimum0

maximum100

output\_format?: "png" | "webp" | "jpeg"

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

"png"

"webp"

"jpeg"

partial\_images?: number

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

quality?: "low" | "medium" | "high" | "auto"

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

"low"

"medium"

"high"

"auto"

size?: (string & {}) | "1024x1024" | "1024x1536" | "1536x1024" | "auto"

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

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

A tool that allows the model to execute shell commands.

type: "shell"

The type of the shell tool. Always `shell`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

environment?: [BetaContainerAuto](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_auto%20%3E%20(schema)) { type, file\_ids, memory\_limit, 2 more }  | [BetaLocalEnvironment](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_environment%20%3E%20(schema)) { type, skills }  | [BetaContainerReference](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_reference%20%3E%20(schema)) { container\_id, type }  | null

BetaContainerAuto { type, file\_ids, memory\_limit, 2 more }

type: "container\_auto"

Automatically creates a container for this request

file\_ids?: Array<string>

An optional list of uploaded files to make available to your code.

memory\_limit?: "1g" | "4g" | "16g" | "64g" | null

The memory limit for the container.

"1g"

"4g"

"16g"

"64g"

network\_policy?: [BetaContainerNetworkPolicyDisabled](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  | [BetaContainerNetworkPolicyAllowlist](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

BetaContainerNetworkPolicyDisabled { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

BetaContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array<string>

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets?: Array<[BetaContainerNetworkPolicyDomainSecret](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } >

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

minLength1

name: string

The name of the secret to inject for the domain.

minLength1

value: string

The secret value to inject for the domain.

maxLength10485760

minLength1

skills?: Array<[BetaSkillReference](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_skill_reference%20%3E%20(schema)) { skill\_id, type, version }  | [BetaInlineSkill](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill%20%3E%20(schema)) { description, name, source, type } >

An optional list of skills referenced by id or inline data.

BetaSkillReference { skill\_id, type, version }

skill\_id: string

The ID of the referenced skill.

maxLength64

minLength1

type: "skill\_reference"

References a skill created with the /v1/skills endpoint.

version?: string

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

BetaInlineSkill { description, name, source, type }

description: string

The description of the skill.

name: string

The name of the skill.

source: [BetaInlineSkillSource](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema)) { data, media\_type, type }

Inline skill payload

data: string

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

media\_type: "application/zip"

The media type of the inline skill payload. Must be `application/zip`.

type: "base64"

The type of the inline skill source. Must be `base64`.

type: "inline"

Defines an inline skill for this request.

BetaLocalEnvironment { type, skills }

type: "local"

Use a local computer environment.

skills?: Array<[BetaLocalSkill](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema)) { description, name, path } >

An optional list of skills.

description: string

The description of the skill.

name: string

The name of the skill.

path: string

The path to the directory containing the skill.

BetaContainerReference { container\_id, type }

container\_id: string

The ID of the referenced container.

type: "container\_reference"

References a container created with the /v1/containers endpoint

BetaCustomTool { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this tool should be deferred and discovered via tool search.

description?: string

Optional description of the custom tool, used to provide more context.

format?: Text { type }  | Grammar { definition, syntax, type }

The input format for the custom tool. Default is unconstrained text.

Text { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar { definition, syntax, type }

A grammar defined by the user.

definition: string

The grammar definition.

syntax: "lark" | "regex"

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: "grammar"

Grammar format. Always `grammar`.

BetaNamespaceTool { description, name, tools, type }

Groups function/custom tools under a shared namespace.

description: string

A description of the namespace shown to the model.

minLength1

name: string

The namespace name used in tool calls (for example, `crm`).

minLength1

tools: Array<Function { name, type, allowed\_callers, 5 more }  | [BetaCustomTool](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_custom_tool%20%3E%20(schema)) { name, type, allowed\_callers, 3 more } >

The function/custom tools available inside this namespace.

Function { name, type, allowed\_callers, 5 more }

name: string

maxLength128

minLength1

type: "function"

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this function should be deferred and discovered via tool search.

description?: string | null

output\_schema?: Record<string, unknown> | null

A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

parameters?: unknown

strict?: boolean | null

Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

BetaCustomTool { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this tool should be deferred and discovered via tool search.

description?: string

Optional description of the custom tool, used to provide more context.

format?: Text { type }  | Grammar { definition, syntax, type }

The input format for the custom tool. Default is unconstrained text.

Text { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar { definition, syntax, type }

A grammar defined by the user.

definition: string

The grammar definition.

syntax: "lark" | "regex"

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: "grammar"

Grammar format. Always `grammar`.

type: "namespace"

The type of the tool. Always `namespace`.

BetaToolSearchTool { type, description, execution, parameters }

Hosted or BYOT tool search configuration for deferred tools.

type: "tool\_search"

The type of the tool. Always `tool_search`.

description?: string | null

Description shown to the model for a client-executed tool search tool.

execution?: "server" | "client"

Whether tool search is executed by the server or by the client.

"server"

"client"

parameters?: unknown

Parameter schema for a client-executed tool search tool.

BetaWebSearchPreviewTool { type, search\_content\_types, search\_context\_size, user\_location }

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: "web\_search\_preview" | "web\_search\_preview\_2025\_03\_11"

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types?: Array<"text" | "image">

"text"

"image"

search\_context\_size?: "low" | "medium" | "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

"low"

"medium"

"high"

user\_location?: UserLocation | null

The user’s location.

type: "approximate"

The type of location approximation. Always `approximate`.

city?: string | null

Free text input for the city of the user, e.g. `San Francisco`.

country?: string | null

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region?: string | null

Free text input for the region of the user, e.g. `California`.

timezone?: string | null

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

BetaApplyPatchTool { type, allowed\_callers }

Allows the assistant to create, delete, or update files using unified diffs.

type: "apply\_patch"

The type of the tool. Always `apply_patch`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

type: "tool\_search\_output"

The type of the item. Always `tool_search_output`.

agent?: Agent { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

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

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

name: string

The name of the function to call.

parameters: Record<string, unknown> | null

A JSON schema object describing the parameters of the function.

strict: boolean | null

Whether strict parameter validation is enforced for this function tool.

type: "function"

The type of the function tool. Always `function`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this function is deferred and loaded via tool search.

description?: string | null

A description of the function. Used by the model to determine whether or not to call the function.

output\_schema?: Record<string, unknown> | null

A JSON schema object describing the JSON value encoded in string outputs for this function.

BetaFileSearchTool { type, vector\_store\_ids, filters, 2 more }

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

type: "file\_search"

The type of the file search tool. Always `file_search`.

vector\_store\_ids: Array<string>

The IDs of the vector stores to search.

filters?: ComparisonFilter { key, type, value }  | CompoundFilter { filters, type }  | null

A filter to apply.

ComparisonFilter { key, type, value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: string

The key to compare against the value.

type: "eq" | "ne" | "gt" | 5 more

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: string | number | boolean | Array<string | number>

The value to compare against the attribute key; supports string, number, or boolean types.

string

number

boolean

Array<string | number>

string

number

CompoundFilter { filters, type }

Combine multiple filters using `and` or `or`.

filters: Array<ComparisonFilter { key, type, value }  | unknown>

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

ComparisonFilter { key, type, value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: string

The key to compare against the value.

type: "eq" | "ne" | "gt" | 5 more

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: string | number | boolean | Array<string | number>

The value to compare against the attribute key; supports string, number, or boolean types.

string

number

boolean

Array<string | number>

string

number

unknown

type: "and" | "or"

Type of operation: `and` or `or`.

"and"

"or"

max\_num\_results?: number

The maximum number of results to return. This number should be between 1 and 50 inclusive.

ranking\_options?: RankingOptions { hybrid\_search, ranker, score\_threshold }

Ranking options for search.

hybrid\_search?: HybridSearch { embedding\_weight, text\_weight }

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

embedding\_weight: number

The weight of the embedding in the reciprocal ranking fusion.

text\_weight: number

The weight of the text in the reciprocal ranking fusion.

ranker?: "auto" | "default-2024-11-15"

The ranker to use for the file search.

"auto"

"default-2024-11-15"

score\_threshold?: number

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

BetaComputerTool { type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

type: "computer"

The type of the computer tool. Always `computer`.

BetaComputerUsePreviewTool { display\_height, display\_width, environment, type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

display\_height: number

The height of the computer display.

display\_width: number

The width of the computer display.

environment: "windows" | "mac" | "linux" | 2 more

The type of computer environment to control.

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: "computer\_use\_preview"

The type of the computer use tool. Always `computer_use_preview`.

BetaWebSearchTool { type, filters, search\_context\_size, user\_location }

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: "web\_search" | "web\_search\_2025\_08\_26"

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

"web\_search"

"web\_search\_2025\_08\_26"

filters?: Filters | null

Filters for the search.

allowed\_domains?: Array<string> | null

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

search\_context\_size?: "low" | "medium" | "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

"low"

"medium"

"high"

user\_location?: UserLocation | null

The approximate location of the user.

city?: string | null

Free text input for the city of the user, e.g. `San Francisco`.

country?: string | null

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region?: string | null

Free text input for the region of the user, e.g. `California`.

timezone?: string | null

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

type?: "approximate"

The type of location approximation. Always `approximate`.

Mcp { server\_label, type, allowed\_callers, 9 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: string

A label for this MCP server, used to identify it in tool calls.

type: "mcp"

The type of the MCP tool. Always `mcp`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

allowed\_tools?: Array<string> | McpToolFilter { read\_only, tool\_names }  | null

List of allowed tool names or a filter object.

Array<string>

McpToolFilter { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

authorization?: string

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

connector\_id?: "connector\_dropbox" | "connector\_gmail" | "connector\_googlecalendar" | 5 more

Identifier for service connectors, like those available in ChatGPT. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided. Learn more
about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

Currently supported `connector_id` values are:

* Dropbox: `connector_dropbox`
* Gmail: `connector_gmail`
* Google Calendar: `connector_googlecalendar`
* Google Drive: `connector_googledrive`
* Microsoft Teams: `connector_microsoftteams`
* Outlook Calendar: `connector_outlookcalendar`
* Outlook Email: `connector_outlookemail`
* SharePoint: `connector_sharepoint`

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading?: boolean

Whether this MCP tool is deferred and discovered via tool search.

headers?: Record<string, string> | null

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

require\_approval?: McpToolApprovalFilter { always, never }  | "always" | "never" | null

Specify which of the MCP server’s tools require approval.

McpToolApprovalFilter { always, never }

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

always?: Always { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

never?: Never { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

"always" | "never"

"always"

"never"

server\_description?: string

Optional description of the MCP server, used to provide more context.

server\_url?: string

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

tunnel\_id?: string

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

CodeInterpreter { container, type, allowed\_callers }

A tool that runs Python code to help generate a response to a prompt.

container: string | CodeInterpreterToolAuto { type, file\_ids, memory\_limit, network\_policy }

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

string

CodeInterpreterToolAuto { type, file\_ids, memory\_limit, network\_policy }

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

type: "auto"

Always `auto`.

file\_ids?: Array<string>

An optional list of uploaded files to make available to your code.

memory\_limit?: "1g" | "4g" | "16g" | "64g" | null

The memory limit for the code interpreter container.

"1g"

"4g"

"16g"

"64g"

network\_policy?: [BetaContainerNetworkPolicyDisabled](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  | [BetaContainerNetworkPolicyAllowlist](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

BetaContainerNetworkPolicyDisabled { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

BetaContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array<string>

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets?: Array<[BetaContainerNetworkPolicyDomainSecret](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } >

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

minLength1

name: string

The name of the secret to inject for the domain.

minLength1

value: string

The secret value to inject for the domain.

maxLength10485760

minLength1

type: "code\_interpreter"

The type of the code interpreter tool. Always `code_interpreter`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

ProgrammaticToolCalling { type }

type: "programmatic\_tool\_calling"

The type of the tool. Always `programmatic_tool_calling`.

ImageGeneration { type, action, background, 9 more }

A tool that generates images using the GPT image models.

type: "image\_generation"

The type of the image generation tool. Always `image_generation`.

action?: "generate" | "edit" | "auto"

Whether to generate a new image or edit an existing image. Default: `auto`.

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

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

"high"

"low"

input\_image\_mask?: InputImageMask { file\_id, image\_url }

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

file\_id?: string

File ID for the mask image.

image\_url?: string

Base64-encoded mask image.

model?: (string & {}) | "gpt-image-1" | "gpt-image-1-mini" | "gpt-image-2" | 3 more

The image generation model to use. Default: `gpt-image-1`.

(string & {})

"gpt-image-1" | "gpt-image-1-mini" | "gpt-image-2" | 3 more

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation?: "auto" | "low"

Moderation level for the generated image. Default: `auto`.

"auto"

"low"

output\_compression?: number

Compression level for the output image. Default: 100.

minimum0

maximum100

output\_format?: "png" | "webp" | "jpeg"

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

"png"

"webp"

"jpeg"

partial\_images?: number

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

quality?: "low" | "medium" | "high" | "auto"

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

"low"

"medium"

"high"

"auto"

size?: (string & {}) | "1024x1024" | "1024x1536" | "1536x1024" | "auto"

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

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

A tool that allows the model to execute shell commands.

type: "shell"

The type of the shell tool. Always `shell`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

environment?: [BetaContainerAuto](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_auto%20%3E%20(schema)) { type, file\_ids, memory\_limit, 2 more }  | [BetaLocalEnvironment](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_environment%20%3E%20(schema)) { type, skills }  | [BetaContainerReference](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_reference%20%3E%20(schema)) { container\_id, type }  | null

BetaContainerAuto { type, file\_ids, memory\_limit, 2 more }

type: "container\_auto"

Automatically creates a container for this request

file\_ids?: Array<string>

An optional list of uploaded files to make available to your code.

memory\_limit?: "1g" | "4g" | "16g" | "64g" | null

The memory limit for the container.

"1g"

"4g"

"16g"

"64g"

network\_policy?: [BetaContainerNetworkPolicyDisabled](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  | [BetaContainerNetworkPolicyAllowlist](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

BetaContainerNetworkPolicyDisabled { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

BetaContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array<string>

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets?: Array<[BetaContainerNetworkPolicyDomainSecret](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } >

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

minLength1

name: string

The name of the secret to inject for the domain.

minLength1

value: string

The secret value to inject for the domain.

maxLength10485760

minLength1

skills?: Array<[BetaSkillReference](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_skill_reference%20%3E%20(schema)) { skill\_id, type, version }  | [BetaInlineSkill](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill%20%3E%20(schema)) { description, name, source, type } >

An optional list of skills referenced by id or inline data.

BetaSkillReference { skill\_id, type, version }

skill\_id: string

The ID of the referenced skill.

maxLength64

minLength1

type: "skill\_reference"

References a skill created with the /v1/skills endpoint.

version?: string

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

BetaInlineSkill { description, name, source, type }

description: string

The description of the skill.

name: string

The name of the skill.

source: [BetaInlineSkillSource](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema)) { data, media\_type, type }

Inline skill payload

data: string

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

media\_type: "application/zip"

The media type of the inline skill payload. Must be `application/zip`.

type: "base64"

The type of the inline skill source. Must be `base64`.

type: "inline"

Defines an inline skill for this request.

BetaLocalEnvironment { type, skills }

type: "local"

Use a local computer environment.

skills?: Array<[BetaLocalSkill](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema)) { description, name, path } >

An optional list of skills.

description: string

The description of the skill.

name: string

The name of the skill.

path: string

The path to the directory containing the skill.

BetaContainerReference { container\_id, type }

container\_id: string

The ID of the referenced container.

type: "container\_reference"

References a container created with the /v1/containers endpoint

BetaCustomTool { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this tool should be deferred and discovered via tool search.

description?: string

Optional description of the custom tool, used to provide more context.

format?: Text { type }  | Grammar { definition, syntax, type }

The input format for the custom tool. Default is unconstrained text.

Text { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar { definition, syntax, type }

A grammar defined by the user.

definition: string

The grammar definition.

syntax: "lark" | "regex"

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: "grammar"

Grammar format. Always `grammar`.

BetaNamespaceTool { description, name, tools, type }

Groups function/custom tools under a shared namespace.

description: string

A description of the namespace shown to the model.

minLength1

name: string

The namespace name used in tool calls (for example, `crm`).

minLength1

tools: Array<Function { name, type, allowed\_callers, 5 more }  | [BetaCustomTool](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_custom_tool%20%3E%20(schema)) { name, type, allowed\_callers, 3 more } >

The function/custom tools available inside this namespace.

Function { name, type, allowed\_callers, 5 more }

name: string

maxLength128

minLength1

type: "function"

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this function should be deferred and discovered via tool search.

description?: string | null

output\_schema?: Record<string, unknown> | null

A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

parameters?: unknown

strict?: boolean | null

Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

BetaCustomTool { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this tool should be deferred and discovered via tool search.

description?: string

Optional description of the custom tool, used to provide more context.

format?: Text { type }  | Grammar { definition, syntax, type }

The input format for the custom tool. Default is unconstrained text.

Text { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar { definition, syntax, type }

A grammar defined by the user.

definition: string

The grammar definition.

syntax: "lark" | "regex"

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: "grammar"

Grammar format. Always `grammar`.

type: "namespace"

The type of the tool. Always `namespace`.

BetaToolSearchTool { type, description, execution, parameters }

Hosted or BYOT tool search configuration for deferred tools.

type: "tool\_search"

The type of the tool. Always `tool_search`.

description?: string | null

Description shown to the model for a client-executed tool search tool.

execution?: "server" | "client"

Whether tool search is executed by the server or by the client.

"server"

"client"

parameters?: unknown

Parameter schema for a client-executed tool search tool.

BetaWebSearchPreviewTool { type, search\_content\_types, search\_context\_size, user\_location }

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: "web\_search\_preview" | "web\_search\_preview\_2025\_03\_11"

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types?: Array<"text" | "image">

"text"

"image"

search\_context\_size?: "low" | "medium" | "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

"low"

"medium"

"high"

user\_location?: UserLocation | null

The user’s location.

type: "approximate"

The type of location approximation. Always `approximate`.

city?: string | null

Free text input for the city of the user, e.g. `San Francisco`.

country?: string | null

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region?: string | null

Free text input for the region of the user, e.g. `California`.

timezone?: string | null

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

BetaApplyPatchTool { type, allowed\_callers }

Allows the assistant to create, delete, or update files using unified diffs.

type: "apply\_patch"

The type of the tool. Always `apply_patch`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

type: "additional\_tools"

The type of the item. Always `additional_tools`.

agent?: Agent { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

BetaResponseCompactionItem { id, encrypted\_content, type, 2 more }

A compaction item generated by the [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).

id: string

The unique ID of the compaction item.

encrypted\_content: string

The encrypted content that was produced by compaction.

type: "compaction"

The type of the item. Always `compaction`.

agent?: Agent { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

created\_by?: string

The identifier of the actor that created the item.

ImageGenerationCall { id, result, status, 2 more }

An image generation request made by the model.

id: string

The unique ID of the image generation call.

result: string | null

The generated image encoded in base64.

status: "in\_progress" | "completed" | "generating" | "failed"

The status of the image generation call.

"in\_progress"

"completed"

"generating"

"failed"

type: "image\_generation\_call"

The type of the image generation call. Always `image_generation_call`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

BetaResponseCodeInterpreterToolCall { id, code, container\_id, 4 more }

A tool call to run code.

id: string

The unique ID of the code interpreter tool call.

code: string | null

The code to run, or null if not available.

container\_id: string

The ID of the container used to run the code.

outputs: Array<Logs { logs, type }  | Image { type, url } > | null

The outputs generated by the code interpreter, such as logs or images.
Can be null if no outputs are available.

Logs { logs, type }

The logs output from the code interpreter.

logs: string

The logs output from the code interpreter.

type: "logs"

The type of the output. Always `logs`.

Image { type, url }

The image output from the code interpreter.

type: "image"

The type of the output. Always `image`.

url: string

The URL of the image output from the code interpreter.

formaturi

status: "in\_progress" | "completed" | "incomplete" | 2 more

The status of the code interpreter tool call. Valid values are `in_progress`, `completed`, `incomplete`, `interpreting`, and `failed`.

"in\_progress"

"completed"

"incomplete"

"interpreting"

"failed"

type: "code\_interpreter\_call"

The type of the code interpreter tool call. Always `code_interpreter_call`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

LocalShellCall { id, action, call\_id, 3 more }

A tool call to run a command on the local shell.

id: string

The unique ID of the local shell call.

action: Action { command, env, type, 3 more }

Execute a shell command on the server.

command: Array<string>

The command to run.

env: Record<string, string>

Environment variables to set for the command.

type: "exec"

The type of the local shell action. Always `exec`.

timeout\_ms?: number | null

Optional timeout in milliseconds for the command.

user?: string | null

Optional user to run the command as.

working\_directory?: string | null

Optional working directory to run the command in.

call\_id: string

The unique ID of the local shell tool call generated by the model.

status: "in\_progress" | "completed" | "incomplete"

The status of the local shell call.

"in\_progress"

"completed"

"incomplete"

type: "local\_shell\_call"

The type of the local shell call. Always `local_shell_call`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

LocalShellCallOutput { id, output, type, 2 more }

The output of a local shell tool call.

id: string

The unique ID of the local shell tool call generated by the model.

output: string

A JSON string of the output of the local shell tool call.

type: "local\_shell\_call\_output"

The type of the local shell tool call output. Always `local_shell_call_output`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

status?: "in\_progress" | "completed" | "incomplete" | null

The status of the item. One of `in_progress`, `completed`, or `incomplete`.

"in\_progress"

"completed"

"incomplete"

BetaResponseFunctionShellToolCall { id, action, call\_id, 6 more }

A tool call that executes one or more shell commands in a managed environment.

id: string

The unique ID of the shell tool call. Populated when this item is returned via API.

action: Action { commands, max\_output\_length, timeout\_ms }

The shell commands and limits that describe how to run the tool call.

commands: Array<string>

max\_output\_length: number | null

Optional maximum number of characters to return from each command.

timeout\_ms: number | null

Optional timeout in milliseconds for the commands.

call\_id: string

The unique ID of the shell tool call generated by the model.

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

The status of the shell call. One of `in_progress`, `completed`, or `incomplete`.

"in\_progress"

"completed"

"incomplete"

type: "shell\_call"

The type of the item. Always `shell_call`.

agent?: Agent { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

caller?: Direct { type }  | Program { caller\_id, type }  | null

The execution context that produced this tool call.

Direct { type }

type: "direct"

Program { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

type: "program"

created\_by?: string

The ID of the entity that created this tool call.

BetaResponseFunctionShellToolCallOutput { id, call\_id, max\_output\_length, 6 more }

The output of a shell tool call that was emitted.

id: string

The unique ID of the shell call output. Populated when this item is returned via API.

call\_id: string

The unique ID of the shell tool call generated by the model.

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

Indicates that the shell commands finished and returned an exit code.

exit\_code: number

Exit code from the shell process.

type: "exit"

The outcome type. Always `exit`.

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

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

caller?: Direct { type }  | Program { caller\_id, type }  | null

The execution context that produced this tool call.

Direct { type }

type: "direct"

Program { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

type: "program"

created\_by?: string

The identifier of the actor that created the item.

BetaResponseApplyPatchToolCall { id, call\_id, operation, 5 more }

A tool call that applies file diffs by creating, deleting, or updating files.

id: string

The unique ID of the apply patch tool call. Populated when this item is returned via API.

call\_id: string

The unique ID of the apply patch tool call generated by the model.

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

The status of the apply patch tool call. One of `in_progress` or `completed`.

"in\_progress"

"completed"

type: "apply\_patch\_call"

The type of the item. Always `apply_patch_call`.

agent?: Agent { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

caller?: Direct { type }  | Program { caller\_id, type }  | null

The execution context that produced this tool call.

Direct { type }

type: "direct"

Program { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

type: "program"

created\_by?: string

The ID of the entity that created this tool call.

BetaResponseApplyPatchToolCallOutput { id, call\_id, status, 5 more }

The output emitted by an apply patch tool call.

id: string

The unique ID of the apply patch tool call output. Populated when this item is returned via API.

call\_id: string

The unique ID of the apply patch tool call generated by the model.

status: "completed" | "failed"

The status of the apply patch tool call output. One of `completed` or `failed`.

"completed"

"failed"

type: "apply\_patch\_call\_output"

The type of the item. Always `apply_patch_call_output`.

agent?: Agent { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

caller?: Direct { type }  | Program { caller\_id, type }  | null

The execution context that produced this tool call.

Direct { type }

type: "direct"

Program { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

type: "program"

created\_by?: string

The ID of the entity that created this tool call output.

output?: string | null

Optional textual output returned by the apply patch tool.

McpCall { id, arguments, name, 7 more }

An invocation of a tool on an MCP server.

id: string

The unique ID of the tool call.

arguments: string

A JSON string of the arguments passed to the tool.

name: string

The name of the tool that was run.

server\_label: string

The label of the MCP server running the tool.

type: "mcp\_call"

The type of the item. Always `mcp_call`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

approval\_request\_id?: string | null

Unique identifier for the MCP tool call approval request.
Include this value in a subsequent `mcp_approval_response` input to approve or reject the corresponding tool call.

error?: string | null

The error from the tool call, if any.

output?: string | null

The output from the tool call.

status?: "in\_progress" | "completed" | "incomplete" | 2 more

The status of the tool call. One of `in_progress`, `completed`, `incomplete`, `calling`, or `failed`.

"in\_progress"

"completed"

"incomplete"

"calling"

"failed"

McpListTools { id, server\_label, tools, 3 more }

A list of tools available on an MCP server.

id: string

The unique ID of the list.

server\_label: string

The label of the MCP server.

tools: Array<Tool>

The tools available on the server.

input\_schema: unknown

The JSON schema describing the tool’s input.

name: string

The name of the tool.

annotations?: unknown

Additional annotations about the tool.

description?: string | null

The description of the tool.

type: "mcp\_list\_tools"

The type of the item. Always `mcp_list_tools`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

error?: string | null

Error message if the server could not list tools.

McpApprovalRequest { id, arguments, name, 3 more }

A request for human approval of a tool invocation.

id: string

The unique ID of the approval request.

arguments: string

A JSON string of arguments for the tool.

name: string

The name of the tool to run.

server\_label: string

The label of the MCP server making the request.

type: "mcp\_approval\_request"

The type of the item. Always `mcp_approval_request`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

McpApprovalResponse { id, approval\_request\_id, approve, 3 more }

A response to an MCP approval request.

id: string

The unique ID of the approval response

approval\_request\_id: string

The ID of the approval request being answered.

approve: boolean

Whether the request was approved.

type: "mcp\_approval\_response"

The type of the item. Always `mcp_approval_response`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

reason?: string | null

Optional reason for the decision.

BetaResponseCustomToolCall { call\_id, input, name, 5 more }

A call to a custom tool created by the model.

call\_id: string

An identifier used to map this custom tool call to a tool call output.

input: string

The input for the custom tool call generated by the model.

name: string

The name of the custom tool being called.

type: "custom\_tool\_call"

The type of the custom tool call. Always `custom_tool_call`.

id?: string

The unique ID of the custom tool call in the OpenAI platform.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

caller?: Direct { type }  | Program { caller\_id, type }  | null

The execution context that produced this tool call.

Direct { type }

type: "direct"

Program { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

type: "program"

namespace?: string

The namespace of the custom tool being called.

BetaResponseCustomToolCallOutputItem extends [BetaResponseCustomToolCallOutput](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_custom_tool_call_output%20%3E%20(schema)) { call\_id, output, type, 3 more }  { id, status, created\_by }

The output of a custom tool call from your code, being sent back to the model.

id: string

The unique ID of the custom tool call output item.

status: "in\_progress" | "completed" | "incomplete"

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

created\_by?: string

The identifier of the actor that created the item.

parallel\_tool\_calls: boolean

Whether to allow the model to run tool calls in parallel.

temperature: number | null

What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.
We generally recommend altering this or `top_p` but not both.

minimum0

maximum2

tool\_choice: [BetaToolChoiceOptions](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool_choice_options%20%3E%20(schema)) | [BetaToolChoiceAllowed](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool_choice_allowed%20%3E%20(schema)) { mode, tools, type }  | [BetaToolChoiceTypes](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool_choice_types%20%3E%20(schema)) { type }  | 6 more

How the model should select which tool (or tools) to use when generating
a response. See the `tools` parameter to see how to specify which tools
the model can call.

BetaToolChoiceOptions = "none" | "auto" | "required"

Controls which (if any) tool is called by the model.

`none` means the model will not call any tool and instead generates a message.

`auto` means the model can pick between generating a message or calling one or
more tools.

`required` means the model must call one or more tools.

"none"

"auto"

"required"

BetaToolChoiceAllowed { mode, tools, type }

Constrains the tools available to the model to a pre-defined set.

mode: "auto" | "required"

Constrains the tools available to the model to a pre-defined set.

`auto` allows the model to pick from among the allowed tools and generate a
message.

`required` requires the model to call one or more of the allowed tools.

"auto"

"required"

tools: Array<Record<string, unknown>>

A list of tool definitions that the model should be allowed to call.

For the Responses API, the list of tool definitions might look like:

[
  { "type": "function", "name": "get_weather" },
  { "type": "mcp", "server_label": "deepwiki" },
  { "type": "image_generation" }
]

type: "allowed\_tools"

Allowed tool configuration type. Always `allowed_tools`.

BetaToolChoiceTypes { type }

Indicates that the model should use a built-in tool to generate a response.
[Learn more about built-in tools](https://platform.openai.com/docs/guides/tools).

type: "file\_search" | "web\_search\_preview" | "computer" | 5 more

The type of hosted tool the model should to use. Learn more about
[built-in tools](https://platform.openai.com/docs/guides/tools).

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

BetaToolChoiceFunction { name, type }

Use this option to force the model to call a specific function.

name: string

The name of the function to call.

type: "function"

For function calling, the type is always `function`.

BetaToolChoiceMcp { server\_label, type, name }

Use this option to force the model to call a specific tool on a remote MCP server.

server\_label: string

The label of the MCP server to use.

type: "mcp"

For MCP tools, the type is always `mcp`.

name?: string | null

The name of the tool to call on the server.

BetaToolChoiceCustom { name, type }

Use this option to force the model to call a specific custom tool.

name: string

The name of the custom tool to call.

type: "custom"

For custom tool calling, the type is always `custom`.

BetaSpecificProgrammaticToolCallingParam { type }

type: "programmatic\_tool\_calling"

The tool to call. Always `programmatic_tool_calling`.

BetaToolChoiceApplyPatch { type }

Forces the model to call the apply\_patch tool when executing a tool call.

type: "apply\_patch"

The tool to call. Always `apply_patch`.

BetaToolChoiceShell { type }

Forces the model to call the shell tool when a tool call is required.

type: "shell"

The tool to call. Always `shell`.

tools: Array<[BetaTool](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))>

An array of tools the model may call while generating a response. You
can specify which tool to use by setting the `tool_choice` parameter.

We support the following categories of tools:

* **Built-in tools**: Tools that are provided by OpenAI that extend the
  model’s capabilities, like [web search](https://platform.openai.com/docs/guides/tools-web-search)
  or [file search](https://platform.openai.com/docs/guides/tools-file-search). Learn more about
  [built-in tools](https://platform.openai.com/docs/guides/tools).
* **MCP Tools**: Integrations with third-party systems via custom MCP servers
  or predefined connectors such as Google Drive and SharePoint. Learn more about
  [MCP Tools](https://platform.openai.com/docs/guides/tools-connectors-mcp).
* **Function calls (custom tools)**: Functions that are defined by you,
  enabling the model to call your own code with strongly typed arguments
  and outputs. Learn more about
  [function calling](https://platform.openai.com/docs/guides/function-calling). You can also use
  custom tools to call your own code.

BetaFunctionTool { name, parameters, strict, 5 more }

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

name: string

The name of the function to call.

parameters: Record<string, unknown> | null

A JSON schema object describing the parameters of the function.

strict: boolean | null

Whether strict parameter validation is enforced for this function tool.

type: "function"

The type of the function tool. Always `function`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this function is deferred and loaded via tool search.

description?: string | null

A description of the function. Used by the model to determine whether or not to call the function.

output\_schema?: Record<string, unknown> | null

A JSON schema object describing the JSON value encoded in string outputs for this function.

BetaFileSearchTool { type, vector\_store\_ids, filters, 2 more }

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

type: "file\_search"

The type of the file search tool. Always `file_search`.

vector\_store\_ids: Array<string>

The IDs of the vector stores to search.

filters?: ComparisonFilter { key, type, value }  | CompoundFilter { filters, type }  | null

A filter to apply.

ComparisonFilter { key, type, value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: string

The key to compare against the value.

type: "eq" | "ne" | "gt" | 5 more

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: string | number | boolean | Array<string | number>

The value to compare against the attribute key; supports string, number, or boolean types.

string

number

boolean

Array<string | number>

string

number

CompoundFilter { filters, type }

Combine multiple filters using `and` or `or`.

filters: Array<ComparisonFilter { key, type, value }  | unknown>

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

ComparisonFilter { key, type, value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: string

The key to compare against the value.

type: "eq" | "ne" | "gt" | 5 more

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: string | number | boolean | Array<string | number>

The value to compare against the attribute key; supports string, number, or boolean types.

string

number

boolean

Array<string | number>

string

number

unknown

type: "and" | "or"

Type of operation: `and` or `or`.

"and"

"or"

max\_num\_results?: number

The maximum number of results to return. This number should be between 1 and 50 inclusive.

ranking\_options?: RankingOptions { hybrid\_search, ranker, score\_threshold }

Ranking options for search.

hybrid\_search?: HybridSearch { embedding\_weight, text\_weight }

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

embedding\_weight: number

The weight of the embedding in the reciprocal ranking fusion.

text\_weight: number

The weight of the text in the reciprocal ranking fusion.

ranker?: "auto" | "default-2024-11-15"

The ranker to use for the file search.

"auto"

"default-2024-11-15"

score\_threshold?: number

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

BetaComputerTool { type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

type: "computer"

The type of the computer tool. Always `computer`.

BetaComputerUsePreviewTool { display\_height, display\_width, environment, type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

display\_height: number

The height of the computer display.

display\_width: number

The width of the computer display.

environment: "windows" | "mac" | "linux" | 2 more

The type of computer environment to control.

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: "computer\_use\_preview"

The type of the computer use tool. Always `computer_use_preview`.

BetaWebSearchTool { type, filters, search\_context\_size, user\_location }

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: "web\_search" | "web\_search\_2025\_08\_26"

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

"web\_search"

"web\_search\_2025\_08\_26"

filters?: Filters | null

Filters for the search.

allowed\_domains?: Array<string> | null

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

search\_context\_size?: "low" | "medium" | "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

"low"

"medium"

"high"

user\_location?: UserLocation | null

The approximate location of the user.

city?: string | null

Free text input for the city of the user, e.g. `San Francisco`.

country?: string | null

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region?: string | null

Free text input for the region of the user, e.g. `California`.

timezone?: string | null

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

type?: "approximate"

The type of location approximation. Always `approximate`.

Mcp { server\_label, type, allowed\_callers, 9 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: string

A label for this MCP server, used to identify it in tool calls.

type: "mcp"

The type of the MCP tool. Always `mcp`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

allowed\_tools?: Array<string> | McpToolFilter { read\_only, tool\_names }  | null

List of allowed tool names or a filter object.

Array<string>

McpToolFilter { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

authorization?: string

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

connector\_id?: "connector\_dropbox" | "connector\_gmail" | "connector\_googlecalendar" | 5 more

Identifier for service connectors, like those available in ChatGPT. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided. Learn more
about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

Currently supported `connector_id` values are:

* Dropbox: `connector_dropbox`
* Gmail: `connector_gmail`
* Google Calendar: `connector_googlecalendar`
* Google Drive: `connector_googledrive`
* Microsoft Teams: `connector_microsoftteams`
* Outlook Calendar: `connector_outlookcalendar`
* Outlook Email: `connector_outlookemail`
* SharePoint: `connector_sharepoint`

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading?: boolean

Whether this MCP tool is deferred and discovered via tool search.

headers?: Record<string, string> | null

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

require\_approval?: McpToolApprovalFilter { always, never }  | "always" | "never" | null

Specify which of the MCP server’s tools require approval.

McpToolApprovalFilter { always, never }

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

always?: Always { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

never?: Never { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

"always" | "never"

"always"

"never"

server\_description?: string

Optional description of the MCP server, used to provide more context.

server\_url?: string

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

tunnel\_id?: string

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

CodeInterpreter { container, type, allowed\_callers }

A tool that runs Python code to help generate a response to a prompt.

container: string | CodeInterpreterToolAuto { type, file\_ids, memory\_limit, network\_policy }

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

string

CodeInterpreterToolAuto { type, file\_ids, memory\_limit, network\_policy }

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

type: "auto"

Always `auto`.

file\_ids?: Array<string>

An optional list of uploaded files to make available to your code.

memory\_limit?: "1g" | "4g" | "16g" | "64g" | null

The memory limit for the code interpreter container.

"1g"

"4g"

"16g"

"64g"

network\_policy?: [BetaContainerNetworkPolicyDisabled](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  | [BetaContainerNetworkPolicyAllowlist](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

BetaContainerNetworkPolicyDisabled { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

BetaContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array<string>

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets?: Array<[BetaContainerNetworkPolicyDomainSecret](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } >

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

minLength1

name: string

The name of the secret to inject for the domain.

minLength1

value: string

The secret value to inject for the domain.

maxLength10485760

minLength1

type: "code\_interpreter"

The type of the code interpreter tool. Always `code_interpreter`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

ProgrammaticToolCalling { type }

type: "programmatic\_tool\_calling"

The type of the tool. Always `programmatic_tool_calling`.

ImageGeneration { type, action, background, 9 more }

A tool that generates images using the GPT image models.

type: "image\_generation"

The type of the image generation tool. Always `image_generation`.

action?: "generate" | "edit" | "auto"

Whether to generate a new image or edit an existing image. Default: `auto`.

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

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

"high"

"low"

input\_image\_mask?: InputImageMask { file\_id, image\_url }

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

file\_id?: string

File ID for the mask image.

image\_url?: string

Base64-encoded mask image.

model?: (string & {}) | "gpt-image-1" | "gpt-image-1-mini" | "gpt-image-2" | 3 more

The image generation model to use. Default: `gpt-image-1`.

(string & {})

"gpt-image-1" | "gpt-image-1-mini" | "gpt-image-2" | 3 more

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation?: "auto" | "low"

Moderation level for the generated image. Default: `auto`.

"auto"

"low"

output\_compression?: number

Compression level for the output image. Default: 100.

minimum0

maximum100

output\_format?: "png" | "webp" | "jpeg"

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

"png"

"webp"

"jpeg"

partial\_images?: number

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

quality?: "low" | "medium" | "high" | "auto"

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

"low"

"medium"

"high"

"auto"

size?: (string & {}) | "1024x1024" | "1024x1536" | "1536x1024" | "auto"

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

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

A tool that allows the model to execute shell commands.

type: "shell"

The type of the shell tool. Always `shell`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

environment?: [BetaContainerAuto](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_auto%20%3E%20(schema)) { type, file\_ids, memory\_limit, 2 more }  | [BetaLocalEnvironment](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_environment%20%3E%20(schema)) { type, skills }  | [BetaContainerReference](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_reference%20%3E%20(schema)) { container\_id, type }  | null

BetaContainerAuto { type, file\_ids, memory\_limit, 2 more }

type: "container\_auto"

Automatically creates a container for this request

file\_ids?: Array<string>

An optional list of uploaded files to make available to your code.

memory\_limit?: "1g" | "4g" | "16g" | "64g" | null

The memory limit for the container.

"1g"

"4g"

"16g"

"64g"

network\_policy?: [BetaContainerNetworkPolicyDisabled](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  | [BetaContainerNetworkPolicyAllowlist](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

BetaContainerNetworkPolicyDisabled { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

BetaContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array<string>

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets?: Array<[BetaContainerNetworkPolicyDomainSecret](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } >

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

minLength1

name: string

The name of the secret to inject for the domain.

minLength1

value: string

The secret value to inject for the domain.

maxLength10485760

minLength1

skills?: Array<[BetaSkillReference](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_skill_reference%20%3E%20(schema)) { skill\_id, type, version }  | [BetaInlineSkill](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill%20%3E%20(schema)) { description, name, source, type } >

An optional list of skills referenced by id or inline data.

BetaSkillReference { skill\_id, type, version }

skill\_id: string

The ID of the referenced skill.

maxLength64

minLength1

type: "skill\_reference"

References a skill created with the /v1/skills endpoint.

version?: string

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

BetaInlineSkill { description, name, source, type }

description: string

The description of the skill.

name: string

The name of the skill.

source: [BetaInlineSkillSource](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema)) { data, media\_type, type }

Inline skill payload

data: string

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

media\_type: "application/zip"

The media type of the inline skill payload. Must be `application/zip`.

type: "base64"

The type of the inline skill source. Must be `base64`.

type: "inline"

Defines an inline skill for this request.

BetaLocalEnvironment { type, skills }

type: "local"

Use a local computer environment.

skills?: Array<[BetaLocalSkill](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema)) { description, name, path } >

An optional list of skills.

description: string

The description of the skill.

name: string

The name of the skill.

path: string

The path to the directory containing the skill.

BetaContainerReference { container\_id, type }

container\_id: string

The ID of the referenced container.

type: "container\_reference"

References a container created with the /v1/containers endpoint

BetaCustomTool { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this tool should be deferred and discovered via tool search.

description?: string

Optional description of the custom tool, used to provide more context.

format?: Text { type }  | Grammar { definition, syntax, type }

The input format for the custom tool. Default is unconstrained text.

Text { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar { definition, syntax, type }

A grammar defined by the user.

definition: string

The grammar definition.

syntax: "lark" | "regex"

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: "grammar"

Grammar format. Always `grammar`.

BetaNamespaceTool { description, name, tools, type }

Groups function/custom tools under a shared namespace.

description: string

A description of the namespace shown to the model.

minLength1

name: string

The namespace name used in tool calls (for example, `crm`).

minLength1

tools: Array<Function { name, type, allowed\_callers, 5 more }  | [BetaCustomTool](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_custom_tool%20%3E%20(schema)) { name, type, allowed\_callers, 3 more } >

The function/custom tools available inside this namespace.

Function { name, type, allowed\_callers, 5 more }

name: string

maxLength128

minLength1

type: "function"

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this function should be deferred and discovered via tool search.

description?: string | null

output\_schema?: Record<string, unknown> | null

A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

parameters?: unknown

strict?: boolean | null

Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

BetaCustomTool { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this tool should be deferred and discovered via tool search.

description?: string

Optional description of the custom tool, used to provide more context.

format?: Text { type }  | Grammar { definition, syntax, type }

The input format for the custom tool. Default is unconstrained text.

Text { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar { definition, syntax, type }

A grammar defined by the user.

definition: string

The grammar definition.

syntax: "lark" | "regex"

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: "grammar"

Grammar format. Always `grammar`.

type: "namespace"

The type of the tool. Always `namespace`.

BetaToolSearchTool { type, description, execution, parameters }

Hosted or BYOT tool search configuration for deferred tools.

type: "tool\_search"

The type of the tool. Always `tool_search`.

description?: string | null

Description shown to the model for a client-executed tool search tool.

execution?: "server" | "client"

Whether tool search is executed by the server or by the client.

"server"

"client"

parameters?: unknown

Parameter schema for a client-executed tool search tool.

BetaWebSearchPreviewTool { type, search\_content\_types, search\_context\_size, user\_location }

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: "web\_search\_preview" | "web\_search\_preview\_2025\_03\_11"

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types?: Array<"text" | "image">

"text"

"image"

search\_context\_size?: "low" | "medium" | "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

"low"

"medium"

"high"

user\_location?: UserLocation | null

The user’s location.

type: "approximate"

The type of location approximation. Always `approximate`.

city?: string | null

Free text input for the city of the user, e.g. `San Francisco`.

country?: string | null

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region?: string | null

Free text input for the region of the user, e.g. `California`.

timezone?: string | null

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

BetaApplyPatchTool { type, allowed\_callers }

Allows the assistant to create, delete, or update files using unified diffs.

type: "apply\_patch"

The type of the tool. Always `apply_patch`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

top\_p: number | null

An alternative to sampling with temperature, called nucleus sampling,
where the model considers the results of the tokens with top\_p probability
mass. So 0.1 means only the tokens comprising the top 10% probability mass
are considered.

We generally recommend altering this or `temperature` but not both.

minimum0

maximum1

background?: boolean | null

Whether to run the model response in the background.
[Learn more](https://platform.openai.com/docs/guides/background).

completed\_at?: number | null

Unix timestamp (in seconds) of when this Response was completed.
Only present when the status is `completed`.

formatunixtime

conversation?: Conversation | null

The conversation that this response belonged to. Input items and output items from this response were automatically added to this conversation.

id: string

The unique ID of the conversation that this response was associated with.

max\_output\_tokens?: number | null

An upper bound for the number of tokens that can be generated for a response, including visible output tokens and [reasoning tokens](https://platform.openai.com/docs/guides/reasoning).

max\_tool\_calls?: number | null

The maximum number of total calls to built-in tools that can be processed in a response. This maximum number applies across all built-in tool calls, not per individual tool. Any further attempts to call a tool by the model will be ignored.

moderation?: Moderation | null

Moderation results for the response input and output, if moderated completions were requested.

input: ModerationResult { categories, category\_applied\_input\_types, category\_scores, 3 more }  | Error { code, message, type }

Moderation for the response input.

ModerationResult { categories, category\_applied\_input\_types, category\_scores, 3 more }

A moderation result produced for the response input or output.

categories: Record<string, boolean>

A dictionary of moderation categories to booleans, True if the input is flagged under this category.

category\_applied\_input\_types: Record<string, Array<"text" | "image">>

Which modalities of input are reflected by the score for each category.

"text"

"image"

category\_scores: Record<string, number>

A dictionary of moderation categories to scores.

flagged: boolean

A boolean indicating whether the content was flagged by any category.

model: string

The moderation model that produced this result.

type: "moderation\_result"

The object type, which was always `moderation_result` for successful moderation results.

Error { code, message, type }

An error produced while attempting moderation for the response input or output.

code: string

The error code.

message: string

The error message.

type: "error"

The object type, which was always `error` for moderation failures.

output: ModerationResult { categories, category\_applied\_input\_types, category\_scores, 3 more }  | Error { code, message, type }

Moderation for the response output.

ModerationResult { categories, category\_applied\_input\_types, category\_scores, 3 more }

A moderation result produced for the response input or output.

categories: Record<string, boolean>

A dictionary of moderation categories to booleans, True if the input is flagged under this category.

category\_applied\_input\_types: Record<string, Array<"text" | "image">>

Which modalities of input are reflected by the score for each category.

"text"

"image"

category\_scores: Record<string, number>

A dictionary of moderation categories to scores.

flagged: boolean

A boolean indicating whether the content was flagged by any category.

model: string

The moderation model that produced this result.

type: "moderation\_result"

The object type, which was always `moderation_result` for successful moderation results.

Error { code, message, type }

An error produced while attempting moderation for the response input or output.

code: string

The error code.

message: string

The error message.

type: "error"

The object type, which was always `error` for moderation failures.

previous\_response\_id?: string | null

The unique ID of the previous response to the model. Use this to
create multi-turn conversations. Learn more about
[conversation state](https://platform.openai.com/docs/guides/conversation-state). Cannot be used in conjunction with `conversation`.

prompt?: [BetaResponsePrompt](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_prompt%20%3E%20(schema)) { id, variables, version }  | null

Reference to a prompt template and its variables.
[Learn more](https://platform.openai.com/docs/guides/text?api-mode=responses#reusable-prompts).

id: string

The unique identifier of the prompt template to use.

variables?: Record<string, string | [BetaResponseInputText](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_text%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  | [BetaResponseInputImage](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_image%20%3E%20(schema)) { detail, type, file\_id, 2 more }  | [BetaResponseInputFile](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_file%20%3E%20(schema)) { type, detail, file\_data, 4 more } > | null

Optional map of values to substitute in for variables in your
prompt. The substitution values can either be strings, or other
Response input types like images or files.

string

BetaResponseInputText { text, type, prompt\_cache\_breakpoint }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

BetaResponseInputImage { detail, type, file\_id, 2 more }

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: "low" | "high" | "auto" | "original"

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

"low"

"high"

"auto"

"original"

type: "input\_image"

The type of the input item. Always `input_image`.

file\_id?: string | null

The ID of the file to be sent to the model.

image\_url?: string | null

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

BetaResponseInputFile { type, detail, file\_data, 4 more }

A file input to the model.

type: "input\_file"

The type of the input item. Always `input_file`.

detail?: "auto" | "low" | "high"

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

"auto"

"low"

"high"

file\_data?: string

The content of the file to be sent to the model.

file\_id?: string | null

The ID of the file to be sent to the model.

file\_url?: string

The URL of the file to be sent to the model.

formaturi

filename?: string

The name of the file to be sent to the model.

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

version?: string | null

Optional version of the prompt template.

prompt\_cache\_key?: string | null

Used by OpenAI to cache responses for similar requests to optimize your cache hit rates. Replaces the `user` field. [Learn more](https://platform.openai.com/docs/guides/prompt-caching).

prompt\_cache\_options?: PromptCacheOptions { mode, ttl }

The prompt-caching options that were applied to the response. Supported for `gpt-5.6` and later models.

mode: "implicit" | "explicit"

Whether implicit prompt-cache breakpoints were enabled.

"implicit"

"explicit"

ttl: "30m"

The minimum lifetime applied to each cache breakpoint.

Deprecatedprompt\_cache\_retention?: "in\_memory" | "24h" | null

Deprecated. Use `prompt_cache_options.ttl` instead.

The retention policy for the prompt cache. Set to `24h` to enable extended prompt caching, which keeps cached prefixes active for longer, up to a maximum of 24 hours. [Learn more](https://platform.openai.com/docs/guides/prompt-caching#prompt-cache-retention).
This field expresses a maximum retention policy, while
`prompt_cache_options.ttl` expresses a minimum cache lifetime. The two
fields are independent and do not interact.
For `gpt-5.5`, `gpt-5.5-pro`, and future models, only `24h` is supported.

For older models that support both `in_memory` and `24h`, the default depends on your organization’s data retention policy:

* Organizations without ZDR enabled default to `24h`.
* Organizations with ZDR enabled default to `in_memory` when `prompt_cache_retention` is not specified.

"in\_memory"

"24h"

reasoning?: Reasoning | null

**gpt-5 and o-series models only**

Configuration options for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).

context?: "auto" | "current\_turn" | "all\_turns" | null

Controls which reasoning items are rendered back to the model on later turns.
If omitted or set to `auto`, the model determines the context mode. The
`gpt-5.6` model family defaults to `all_turns`; earlier models default to
`current_turn`.

When returned on a response, this is the effective reasoning context mode
used for the response.

"auto"

"current\_turn"

"all\_turns"

effort?: "none" | "minimal" | "low" | 4 more | null

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

Deprecatedgenerate\_summary?: "auto" | "concise" | "detailed" | null

**Deprecated:** use `summary` instead.

A summary of the reasoning performed by the model. This can be
useful for debugging and understanding the model’s reasoning process.
One of `auto`, `concise`, or `detailed`.

"auto"

"concise"

"detailed"

mode?: (string & {}) | "standard" | "pro"

Controls the reasoning execution mode for the request.

When returned on a response, this is the effective execution mode.

(string & {})

"standard" | "pro"

"standard"

"pro"

summary?: "auto" | "concise" | "detailed" | null

A summary of the reasoning performed by the model. This can be
useful for debugging and understanding the model’s reasoning process.
One of `auto`, `concise`, or `detailed`.

`concise` is supported for `computer-use-preview` models and all reasoning models after `gpt-5`.

"auto"

"concise"

"detailed"

safety\_identifier?: string | null

A stable identifier used to help detect users of your application that may be violating OpenAI’s usage policies.
The IDs should be a string that uniquely identifies each user, with a maximum length of 64 characters. We recommend hashing their username or email address, in order to avoid sending us any identifying information. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).

maxLength64

service\_tier?: "auto" | "default" | "flex" | 2 more | null

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

status?: [BetaResponseStatus](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_status%20%3E%20(schema))

The status of the response generation. One of `completed`, `failed`,
`in_progress`, `cancelled`, `queued`, or `incomplete`.

"completed"

"failed"

"in\_progress"

"cancelled"

"queued"

"incomplete"

text?: [BetaResponseTextConfig](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_text_config%20%3E%20(schema)) { format, verbosity }

Configuration options for a text response from the model. Can be plain
text or structured JSON data. Learn more:

* [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
* [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

format?: [BetaResponseFormatTextConfig](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_format_text_config%20%3E%20(schema))

An object specifying the format that the model must output.

Configuring `{ "type": "json_schema" }` enables Structured Outputs,
which ensures the model will match your supplied JSON schema. Learn more in the
[Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

The default format is `{ "type": "text" }` with no additional options.

**Not recommended for gpt-4o and newer models:**

Setting to `{ "type": "json_object" }` enables the older JSON mode, which
ensures the message the model generates is valid JSON. Using `json_schema`
is preferred for models that support it.

Text { type }

Default response format. Used to generate text responses.

type: "text"

The type of response format being defined. Always `text`.

BetaResponseFormatTextJSONSchemaConfig { name, schema, type, 2 more }

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

name: string

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

schema: Record<string, unknown>

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

type: "json\_schema"

The type of response format being defined. Always `json_schema`.

description?: string

A description of what the response format is for, used by the model to
determine how to respond in the format.

strict?: boolean | null

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

JSONObject { type }

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type: "json\_object"

The type of response format being defined. Always `json_object`.

verbosity?: "low" | "medium" | "high" | null

Constrains the verbosity of the model’s response. Lower values will result in
more concise responses, while higher values will result in more verbose responses.
Currently supported values are `low`, `medium`, and `high`. The default is
`medium`.

"low"

"medium"

"high"

top\_logprobs?: number | null

An integer between 0 and 20 specifying the maximum number of most likely
tokens to return at each token position, each with an associated log
probability. In some cases, the number of returned tokens may be fewer than
requested.

minimum0

maximum20

truncation?: "auto" | "disabled" | null

The truncation strategy to use for the model response.

* `auto`: If the input to this Response exceeds
  the model’s context window size, the model will truncate the
  response to fit the context window by dropping items from the beginning of the conversation.
* `disabled` (default): If the input size will exceed the context window
  size for a model, the request will fail with a 400 error.

"auto"

"disabled"

usage?: [BetaResponseUsage](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_usage%20%3E%20(schema)) { input\_tokens, input\_tokens\_details, output\_tokens, 2 more }

Represents token usage details including input tokens, output tokens,
a breakdown of output tokens, and the total tokens used.

input\_tokens: number

The number of input tokens.

input\_tokens\_details: InputTokensDetails { cache\_write\_tokens, cached\_tokens }

A detailed breakdown of the input tokens.

cache\_write\_tokens: number

The number of input tokens that were written to the cache.

cached\_tokens: number

The number of tokens that were retrieved from the cache.
[More on prompt caching](https://platform.openai.com/docs/guides/prompt-caching).

output\_tokens: number

The number of output tokens.

output\_tokens\_details: OutputTokensDetails { reasoning\_tokens }

A detailed breakdown of the output tokens.

reasoning\_tokens: number

The number of reasoning tokens.

total\_tokens: number

The total number of tokens used.

Deprecateduser?: string

This field is being replaced by `safety_identifier` and `prompt_cache_key`. Use `prompt_cache_key` instead to maintain caching optimizations.
A stable identifier for your end-users.
Used to boost cache hit rates by better bucketing similar requests and to help OpenAI detect and prevent abuse. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).

sequence\_number: number

The sequence number for this event.

type: "response.created"

The type of the event. Always `response.created`.

agent?: Agent | null

The agent that owns this multi-agent streaming event.

agent\_name: string

The canonical name of the agent that produced this item.

BetaResponseErrorEvent { code, message, param, 3 more }

Emitted when an error occurs.

code: string | null

The error code.

message: string

The error message.

param: string | null

The error parameter.

sequence\_number: number

The sequence number of this event.

type: "error"

The type of the event. Always `error`.

agent?: Agent | null

The agent that owns this multi-agent streaming event.

agent\_name: string

The canonical name of the agent that produced this item.

BetaResponseFileSearchCallCompletedEvent { item\_id, output\_index, sequence\_number, 2 more }

Emitted when a file search call is completed (results found).

item\_id: string

The ID of the output item that the file search call is initiated.

output\_index: number

The index of the output item that the file search call is initiated.

sequence\_number: number

The sequence number of this event.

type: "response.file\_search\_call.completed"

The type of the event. Always `response.file_search_call.completed`.

agent?: Agent | null

The agent that owns this multi-agent streaming event.

agent\_name: string

The canonical name of the agent that produced this item.

BetaResponseFileSearchCallInProgressEvent { item\_id, output\_index, sequence\_number, 2 more }

Emitted when a file search call is initiated.

item\_id: string

The ID of the output item that the file search call is initiated.

output\_index: number

The index of the output item that the file search call is initiated.

sequence\_number: number

The sequence number of this event.

type: "response.file\_search\_call.in\_progress"

The type of the event. Always `response.file_search_call.in_progress`.

agent?: Agent | null

The agent that owns this multi-agent streaming event.

agent\_name: string

The canonical name of the agent that produced this item.

BetaResponseFileSearchCallSearchingEvent { item\_id, output\_index, sequence\_number, 2 more }

Emitted when a file search is currently searching.

item\_id: string

The ID of the output item that the file search call is initiated.

output\_index: number

The index of the output item that the file search call is searching.

sequence\_number: number

The sequence number of this event.

type: "response.file\_search\_call.searching"

The type of the event. Always `response.file_search_call.searching`.

agent?: Agent | null

The agent that owns this multi-agent streaming event.

agent\_name: string

The canonical name of the agent that produced this item.

BetaResponseFunctionCallArgumentsDeltaEvent { delta, item\_id, output\_index, 3 more }

Emitted when there is a partial function-call arguments delta.

delta: string

The function-call arguments delta that is added.

item\_id: string

The ID of the output item that the function-call arguments delta is added to.

output\_index: number

The index of the output item that the function-call arguments delta is added to.

sequence\_number: number

The sequence number of this event.

type: "response.function\_call\_arguments.delta"

The type of the event. Always `response.function_call_arguments.delta`.

agent?: Agent | null

The agent that owns this multi-agent streaming event.

agent\_name: string

The canonical name of the agent that produced this item.

BetaResponseFunctionCallArgumentsDoneEvent { arguments, item\_id, name, 4 more }

Emitted when function-call arguments are finalized.

arguments: string

The function-call arguments.

item\_id: string

The ID of the item.

name: string

The name of the function that was called.

output\_index: number

The index of the output item.

sequence\_number: number

The sequence number of this event.

type: "response.function\_call\_arguments.done"

agent?: Agent | null

The agent that owns this multi-agent streaming event.

agent\_name: string

The canonical name of the agent that produced this item.

BetaResponseInProgressEvent { response, sequence\_number, type, agent }

Emitted when the response is in progress.

response: [BetaResponse](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema)) { id, created\_at, error, 31 more }

The response that is in progress.

id: string

Unique identifier for this Response.

created\_at: number

Unix timestamp (in seconds) of when this Response was created.

formatunixtime

error: [BetaResponseError](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_error%20%3E%20(schema)) { code, message }  | null

An error object returned when the model fails to generate a Response.

code: "server\_error" | "rate\_limit\_exceeded" | "invalid\_prompt" | 17 more

The error code for the response.

"server\_error"

"rate\_limit\_exceeded"

"invalid\_prompt"

"data\_residency\_mismatch"

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

incomplete\_details: IncompleteDetails | null

Details about why the response is incomplete.

reason?: "max\_output\_tokens" | "content\_filter"

The reason why the response is incomplete.

"max\_output\_tokens"

"content\_filter"

instructions: string | Array<[BetaResponseInputItem](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_item%20%3E%20(schema))> | null

A system (or developer) message inserted into the model’s context.

When using along with `previous_response_id`, the instructions from a previous
response will not be carried over to the next response. This makes it simple
to swap out system (or developer) messages in new responses.

string

Array<[BetaResponseInputItem](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_item%20%3E%20(schema))>

BetaEasyInputMessage { content, role, phase, type }

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: string | [BetaResponseInputMessageContentList](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_message_content_list%20%3E%20(schema)) { , ,  }

Text, image, or audio input to the model, used to generate a response.
Can also contain previous assistant responses.

string

BetaResponseInputMessageContentList = Array<[BetaResponseInputContent](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_content%20%3E%20(schema))>

A list of one or many input items to the model, containing different content
types.

BetaResponseInputText { text, type, prompt\_cache\_breakpoint }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

BetaResponseInputImage { detail, type, file\_id, 2 more }

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: "low" | "high" | "auto" | "original"

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

"low"

"high"

"auto"

"original"

type: "input\_image"

The type of the input item. Always `input_image`.

file\_id?: string | null

The ID of the file to be sent to the model.

image\_url?: string | null

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

BetaResponseInputFile { type, detail, file\_data, 4 more }

A file input to the model.

type: "input\_file"

The type of the input item. Always `input_file`.

detail?: "auto" | "low" | "high"

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

"auto"

"low"

"high"

file\_data?: string

The content of the file to be sent to the model.

file\_id?: string | null

The ID of the file to be sent to the model.

file\_url?: string

The URL of the file to be sent to the model.

formaturi

filename?: string

The name of the file to be sent to the model.

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

role: "user" | "assistant" | "system" | "developer"

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

"user"

"assistant"

"system"

"developer"

phase?: "commentary" | "final\_answer" | null

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

"commentary"

"final\_answer"

type?: "message"

The type of the message input. Always `message`.

Message { content, role, agent, 2 more }

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role.

content: [BetaResponseInputMessageContentList](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_message_content_list%20%3E%20(schema)) { , ,  }

A list of one or many input items to the model, containing different content
types.

BetaResponseInputText { text, type, prompt\_cache\_breakpoint }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

BetaResponseInputImage { detail, type, file\_id, 2 more }

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: "low" | "high" | "auto" | "original"

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

"low"

"high"

"auto"

"original"

type: "input\_image"

The type of the input item. Always `input_image`.

file\_id?: string | null

The ID of the file to be sent to the model.

image\_url?: string | null

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

BetaResponseInputFile { type, detail, file\_data, 4 more }

A file input to the model.

type: "input\_file"

The type of the input item. Always `input_file`.

detail?: "auto" | "low" | "high"

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

"auto"

"low"

"high"

file\_data?: string

The content of the file to be sent to the model.

file\_id?: string | null

The ID of the file to be sent to the model.

file\_url?: string

The URL of the file to be sent to the model.

formaturi

filename?: string

The name of the file to be sent to the model.

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

role: "user" | "system" | "developer"

The role of the message input. One of `user`, `system`, or `developer`.

"user"

"system"

"developer"

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

status?: "in\_progress" | "completed" | "incomplete"

The status of item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

type?: "message"

The type of the message input. Always set to `message`.

BetaResponseOutputMessage { id, content, role, 4 more }

An output message from the model.

id: string

The unique ID of the output message.

content: Array<[BetaResponseOutputText](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_text%20%3E%20(schema)) { annotations, text, type, logprobs }  | [BetaResponseOutputRefusal](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_refusal%20%3E%20(schema)) { refusal, type } >

The content of the output message.

BetaResponseOutputText { annotations, text, type, logprobs }

A text output from the model.

annotations: Array<FileCitation { file\_id, filename, index, type }  | URLCitation { end\_index, start\_index, title, 2 more }  | ContainerFileCitation { container\_id, end\_index, file\_id, 3 more }  | FilePath { file\_id, index, type } >

The annotations of the text output.

FileCitation { file\_id, filename, index, type }

A citation to a file.

file\_id: string

The ID of the file.

filename: string

The filename of the file cited.

index: number

The index of the file in the list of files.

type: "file\_citation"

The type of the file citation. Always `file_citation`.

URLCitation { end\_index, start\_index, title, 2 more }

A citation for a web resource used to generate a model response.

end\_index: number

The index of the last character of the URL citation in the message.

start\_index: number

The index of the first character of the URL citation in the message.

title: string

The title of the web resource.

type: "url\_citation"

The type of the URL citation. Always `url_citation`.

url: string

The URL of the web resource.

formaturi

ContainerFileCitation { container\_id, end\_index, file\_id, 3 more }

A citation for a container file used to generate a model response.

container\_id: string

The ID of the container file.

end\_index: number

The index of the last character of the container file citation in the message.

file\_id: string

The ID of the file.

filename: string

The filename of the container file cited.

start\_index: number

The index of the first character of the container file citation in the message.

type: "container\_file\_citation"

The type of the container file citation. Always `container_file_citation`.

FilePath { file\_id, index, type }

A path to a file.

file\_id: string

The ID of the file.

index: number

The index of the file in the list of files.

type: "file\_path"

The type of the file path. Always `file_path`.

text: string

The text output from the model.

type: "output\_text"

The type of the output text. Always `output_text`.

logprobs?: Array<Logprob>

token: string

bytes: Array<number>

logprob: number

top\_logprobs: Array<TopLogprob>

token: string

bytes: Array<number>

logprob: number

BetaResponseOutputRefusal { refusal, type }

A refusal from the model.

refusal: string

The refusal explanation from the model.

type: "refusal"

The type of the refusal. Always `refusal`.

role: "assistant"

The role of the output message. Always `assistant`.

status: "in\_progress" | "completed" | "incomplete"

The status of the message input. One of `in_progress`, `completed`, or
`incomplete`. Populated when input items are returned via API.

"in\_progress"

"completed"

"incomplete"

type: "message"

The type of the output message. Always `message`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

phase?: "commentary" | "final\_answer" | null

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

"commentary"

"final\_answer"

BetaResponseFileSearchToolCall { id, queries, status, 3 more }

The results of a file search tool call. See the
[file search guide](https://platform.openai.com/docs/guides/tools-file-search) for more information.

id: string

The unique ID of the file search tool call.

queries: Array<string>

The queries used to search for files.

status: "in\_progress" | "searching" | "completed" | 2 more

The status of the file search tool call. One of `in_progress`,
`searching`, `incomplete` or `failed`,

"in\_progress"

"searching"

"completed"

"incomplete"

"failed"

type: "file\_search\_call"

The type of the file search tool call. Always `file_search_call`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

results?: Array<Result> | null

The results of the file search tool call.

attributes?: Record<string, string | number | boolean> | null

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.

string

number

boolean

file\_id?: string

The unique ID of the file.

filename?: string

The name of the file.

score?: number

The relevance score of the file - a value between 0 and 1.

formatfloat

text?: string

The text that was retrieved from the file.

BetaResponseComputerToolCall { id, call\_id, pending\_safety\_checks, 5 more }

A tool call to a computer use tool. See the
[computer use guide](https://platform.openai.com/docs/guides/tools-computer-use) for more information.

id: string

The unique ID of the computer call.

call\_id: string

An identifier used when responding to the tool call with output.

pending\_safety\_checks: Array<PendingSafetyCheck>

The pending safety checks for the computer call.

id: string

The ID of the pending safety check.

code?: string | null

The type of the pending safety check.

message?: string | null

Details about the pending safety check.

status: "in\_progress" | "completed" | "incomplete"

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

type: "computer\_call"

The type of the computer call. Always `computer_call`.

action?: [BetaComputerAction](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_computer_action%20%3E%20(schema))

A click action.

Click { button, type, x, 2 more }

A click action.

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

[
  { x: 100, y: 200 },
  { x: 200, y: 300 }
]

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

Flattened batched actions for `computer_use`. Each action includes an
`type` discriminator and action-specific fields.

Click { button, type, x, 2 more }

A click action.

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

[
  { x: 100, y: 200 },
  { x: 200, y: 300 }
]

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

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

ComputerCallOutput { call\_id, output, type, 4 more }

The output of a computer tool call.

call\_id: string

The ID of the computer tool call that produced the output.

maxLength64

minLength1

output: [BetaResponseComputerToolCallOutputScreenshot](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_computer_tool_call_output_screenshot%20%3E%20(schema)) { type, file\_id, image\_url }

A computer screenshot image used with the computer use tool.

type: "computer\_screenshot"

Specifies the event type. For a computer screenshot, this property is
always set to `computer_screenshot`.

file\_id?: string

The identifier of an uploaded file that contains the screenshot.

image\_url?: string

The URL of the screenshot image.

formaturi

type: "computer\_call\_output"

The type of the computer tool call output. Always `computer_call_output`.

id?: string | null

The ID of the computer tool call output.

acknowledged\_safety\_checks?: Array<AcknowledgedSafetyCheck> | null

The safety checks reported by the API that have been acknowledged by the developer.

id: string

The ID of the pending safety check.

code?: string | null

The type of the pending safety check.

message?: string | null

Details about the pending safety check.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

status?: "in\_progress" | "completed" | "incomplete" | null

The status of the message input. One of `in_progress`, `completed`, or `incomplete`. Populated when input items are returned via API.

"in\_progress"

"completed"

"incomplete"

BetaResponseFunctionWebSearch { id, action, status, 2 more }

The results of a web search tool call. See the
[web search guide](https://platform.openai.com/docs/guides/tools-web-search) for more information.

id: string

The unique ID of the web search tool call.

action: Search { type, queries, query, sources }  | OpenPage { type, url }  | FindInPage { pattern, type, url }

An object describing the specific action taken in this web search call.
Includes details on how the model used the web (search, open\_page, find\_in\_page).

Search { type, queries, query, sources }

Action type “search” - Performs a web search query.

type: "search"

The action type.

queries?: Array<string>

The search queries.

Deprecatedquery?: string

The search query.

sources?: Array<Source>

The sources used in the search.

type: "url"

The type of source. Always `url`.

url: string

The URL of the source.

formaturi

OpenPage { type, url }

Action type “open\_page” - Opens a specific URL from search results.

type: "open\_page"

The action type.

url?: string | null

The URL opened by the model.

formaturi

FindInPage { pattern, type, url }

Action type “find\_in\_page”: Searches for a pattern within a loaded page.

pattern: string

The pattern or text to search for within the page.

type: "find\_in\_page"

The action type.

url: string

The URL of the page searched for the pattern.

formaturi

status: "in\_progress" | "searching" | "completed" | "failed"

The status of the web search tool call.

"in\_progress"

"searching"

"completed"

"failed"

type: "web\_search\_call"

The type of the web search tool call. Always `web_search_call`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

BetaResponseFunctionToolCall { arguments, call\_id, name, 6 more }

A tool call to run a function. See the
[function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.

arguments: string

A JSON string of the arguments to pass to the function.

call\_id: string

The unique ID of the function tool call generated by the model.

name: string

The name of the function to run.

type: "function\_call"

The type of the function tool call. Always `function_call`.

id?: string

The unique ID of the function tool call.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

caller?: Direct { type }  | Program { caller\_id, type }  | null

The execution context that produced this tool call.

Direct { type }

type: "direct"

Program { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

type: "program"

namespace?: string

The namespace of the function to run.

status?: "in\_progress" | "completed" | "incomplete"

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

FunctionCallOutput { call\_id, output, type, 4 more }

The output of a function tool call.

call\_id: string

The unique ID of the function tool call generated by the model.

maxLength64

minLength1

output: string | [BetaResponseFunctionCallOutputItemList](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_call_output_item_list%20%3E%20(schema)) { , ,  }

Text, image, or file output of the function tool call.

string

BetaResponseFunctionCallOutputItemList = Array<[BetaResponseFunctionCallOutputItem](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_call_output_item%20%3E%20(schema))>

An array of content outputs (text, image, file) for the function tool call.

BetaResponseInputTextContent { text, type, prompt\_cache\_breakpoint }

A text input to the model.

text: string

The text input to the model.

maxLength10485760

type: "input\_text"

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint?: PromptCacheBreakpoint | null

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

BetaResponseInputImageContent { type, detail, file\_id, 2 more }

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision)

type: "input\_image"

The type of the input item. Always `input_image`.

detail?: "low" | "high" | "auto" | "original" | null

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

"low"

"high"

"auto"

"original"

file\_id?: string | null

The ID of the file to be sent to the model.

image\_url?: string | null

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

maxLength20971520

formaturi

prompt\_cache\_breakpoint?: PromptCacheBreakpoint | null

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

BetaResponseInputFileContent { type, detail, file\_data, 4 more }

A file input to the model.

type: "input\_file"

The type of the input item. Always `input_file`.

detail?: "auto" | "low" | "high"

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

"auto"

"low"

"high"

file\_data?: string | null

The base64-encoded data of the file to be sent to the model.

maxLength73400320

file\_id?: string | null

The ID of the file to be sent to the model.

file\_url?: string | null

The URL of the file to be sent to the model.

formaturi

filename?: string | null

The name of the file to be sent to the model.

prompt\_cache\_breakpoint?: PromptCacheBreakpoint | null

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

type: "function\_call\_output"

The type of the function tool call output. Always `function_call_output`.

id?: string | null

The unique ID of the function tool call output. Populated when this item is returned via API.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

caller?: Direct { type }  | Program { caller\_id, type }  | null

The execution context that produced this tool call.

Direct { type }

type: "direct"

The caller type. Always `direct`.

Program { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

maxLength64

minLength1

type: "program"

The caller type. Always `program`.

status?: "in\_progress" | "completed" | "incomplete" | null

The status of the item. One of `in_progress`, `completed`, or `incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

AgentMessage { author, content, recipient, 3 more }

A message routed between agents.

author: string

The sending agent identity.

content: Array<[BetaResponseInputTextContent](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_text_content%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  | [BetaResponseInputImageContent](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_image_content%20%3E%20(schema)) { type, detail, file\_id, 2 more }  | EncryptedContent { encrypted\_content, type } >

Plaintext, image, or encrypted content sent between agents.

BetaResponseInputTextContent { text, type, prompt\_cache\_breakpoint }

A text input to the model.

text: string

The text input to the model.

maxLength10485760

type: "input\_text"

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint?: PromptCacheBreakpoint | null

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

BetaResponseInputImageContent { type, detail, file\_id, 2 more }

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision)

type: "input\_image"

The type of the input item. Always `input_image`.

detail?: "low" | "high" | "auto" | "original" | null

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

"low"

"high"

"auto"

"original"

file\_id?: string | null

The ID of the file to be sent to the model.

image\_url?: string | null

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

maxLength20971520

formaturi

prompt\_cache\_breakpoint?: PromptCacheBreakpoint | null

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

EncryptedContent { encrypted\_content, type }

Opaque encrypted content that Responses API decrypts inside trusted model execution.

encrypted\_content: string

Opaque encrypted content.

maxLength10485760

type: "encrypted\_content"

The type of the input item. Always `encrypted_content`.

recipient: string

The destination agent identity.

type: "agent\_message"

The item type. Always `agent_message`.

id?: string | null

The unique ID of this agent message item.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

MultiAgentCall { action, arguments, call\_id, 3 more }

action: "spawn\_agent" | "interrupt\_agent" | "list\_agents" | 3 more

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

The unique ID linking this call to its output.

maxLength64

minLength1

type: "multi\_agent\_call"

The item type. Always `multi_agent_call`.

id?: string | null

The unique ID of this multi-agent call.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

MultiAgentCallOutput { action, call\_id, output, 3 more }

action: "spawn\_agent" | "interrupt\_agent" | "list\_agents" | 3 more

The multi-agent action that produced this result.

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

call\_id: string

The unique ID of the multi-agent call.

maxLength64

minLength1

output: Array<Output>

Text output returned by the multi-agent action.

text: string

The text content.

maxLength10485760

type: "output\_text"

The content type. Always `output_text`.

annotations?: Array<FileCitation { file\_id, filename, index, type }  | URLCitation { end\_index, start\_index, title, 2 more }  | ContainerFileCitation { container\_id, end\_index, file\_id, 3 more } >

Citations associated with the text content.

FileCitation { file\_id, filename, index, type }

file\_id: string

The ID of the file.

filename: string

The filename of the file cited.

index: number

The index of the file in the list of files.

minimum0

type: "file\_citation"

The citation type. Always `file_citation`.

URLCitation { end\_index, start\_index, title, 2 more }

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

formaturi

ContainerFileCitation { container\_id, end\_index, file\_id, 3 more }

container\_id: string

The ID of the container.

end\_index: number

The index of the last character of the citation in the message.

minimum0

file\_id: string

The ID of the container file.

filename: string

The filename of the container file cited.

start\_index: number

The index of the first character of the citation in the message.

minimum0

type: "container\_file\_citation"

The citation type. Always `container_file_citation`.

type: "multi\_agent\_call\_output"

The item type. Always `multi_agent_call_output`.

id?: string | null

The unique ID of this multi-agent call output.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

ToolSearchCall { arguments, type, id, 4 more }

arguments: unknown

The arguments supplied to the tool search call.

type: "tool\_search\_call"

The item type. Always `tool_search_call`.

id?: string | null

The unique ID of this tool search call.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

call\_id?: string | null

The unique ID of the tool search call generated by the model.

maxLength64

minLength1

execution?: "server" | "client"

Whether tool search was executed by the server or by the client.

"server"

"client"

status?: "in\_progress" | "completed" | "incomplete" | null

The status of the tool search call.

"in\_progress"

"completed"

"incomplete"

BetaResponseToolSearchOutputItemParam { tools, type, id, 4 more }

tools: Array<[BetaTool](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))>

The loaded tool definitions returned by the tool search output.

BetaFunctionTool { name, parameters, strict, 5 more }

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

name: string

The name of the function to call.

parameters: Record<string, unknown> | null

A JSON schema object describing the parameters of the function.

strict: boolean | null

Whether strict parameter validation is enforced for this function tool.

type: "function"

The type of the function tool. Always `function`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this function is deferred and loaded via tool search.

description?: string | null

A description of the function. Used by the model to determine whether or not to call the function.

output\_schema?: Record<string, unknown> | null

A JSON schema object describing the JSON value encoded in string outputs for this function.

BetaFileSearchTool { type, vector\_store\_ids, filters, 2 more }

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

type: "file\_search"

The type of the file search tool. Always `file_search`.

vector\_store\_ids: Array<string>

The IDs of the vector stores to search.

filters?: ComparisonFilter { key, type, value }  | CompoundFilter { filters, type }  | null

A filter to apply.

ComparisonFilter { key, type, value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: string

The key to compare against the value.

type: "eq" | "ne" | "gt" | 5 more

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: string | number | boolean | Array<string | number>

The value to compare against the attribute key; supports string, number, or boolean types.

string

number

boolean

Array<string | number>

string

number

CompoundFilter { filters, type }

Combine multiple filters using `and` or `or`.

filters: Array<ComparisonFilter { key, type, value }  | unknown>

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

ComparisonFilter { key, type, value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: string

The key to compare against the value.

type: "eq" | "ne" | "gt" | 5 more

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: string | number | boolean | Array<string | number>

The value to compare against the attribute key; supports string, number, or boolean types.

string

number

boolean

Array<string | number>

string

number

unknown

type: "and" | "or"

Type of operation: `and` or `or`.

"and"

"or"

max\_num\_results?: number

The maximum number of results to return. This number should be between 1 and 50 inclusive.

ranking\_options?: RankingOptions { hybrid\_search, ranker, score\_threshold }

Ranking options for search.

hybrid\_search?: HybridSearch { embedding\_weight, text\_weight }

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

embedding\_weight: number

The weight of the embedding in the reciprocal ranking fusion.

text\_weight: number

The weight of the text in the reciprocal ranking fusion.

ranker?: "auto" | "default-2024-11-15"

The ranker to use for the file search.

"auto"

"default-2024-11-15"

score\_threshold?: number

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

BetaComputerTool { type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

type: "computer"

The type of the computer tool. Always `computer`.

BetaComputerUsePreviewTool { display\_height, display\_width, environment, type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

display\_height: number

The height of the computer display.

display\_width: number

The width of the computer display.

environment: "windows" | "mac" | "linux" | 2 more

The type of computer environment to control.

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: "computer\_use\_preview"

The type of the computer use tool. Always `computer_use_preview`.

BetaWebSearchTool { type, filters, search\_context\_size, user\_location }

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: "web\_search" | "web\_search\_2025\_08\_26"

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

"web\_search"

"web\_search\_2025\_08\_26"

filters?: Filters | null

Filters for the search.

allowed\_domains?: Array<string> | null

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

search\_context\_size?: "low" | "medium" | "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

"low"

"medium"

"high"

user\_location?: UserLocation | null

The approximate location of the user.

city?: string | null

Free text input for the city of the user, e.g. `San Francisco`.

country?: string | null

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region?: string | null

Free text input for the region of the user, e.g. `California`.

timezone?: string | null

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

type?: "approximate"

The type of location approximation. Always `approximate`.

Mcp { server\_label, type, allowed\_callers, 9 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: string

A label for this MCP server, used to identify it in tool calls.

type: "mcp"

The type of the MCP tool. Always `mcp`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

allowed\_tools?: Array<string> | McpToolFilter { read\_only, tool\_names }  | null

List of allowed tool names or a filter object.

Array<string>

McpToolFilter { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

authorization?: string

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

connector\_id?: "connector\_dropbox" | "connector\_gmail" | "connector\_googlecalendar" | 5 more

Identifier for service connectors, like those available in ChatGPT. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided. Learn more
about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

Currently supported `connector_id` values are:

* Dropbox: `connector_dropbox`
* Gmail: `connector_gmail`
* Google Calendar: `connector_googlecalendar`
* Google Drive: `connector_googledrive`
* Microsoft Teams: `connector_microsoftteams`
* Outlook Calendar: `connector_outlookcalendar`
* Outlook Email: `connector_outlookemail`
* SharePoint: `connector_sharepoint`

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading?: boolean

Whether this MCP tool is deferred and discovered via tool search.

headers?: Record<string, string> | null

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

require\_approval?: McpToolApprovalFilter { always, never }  | "always" | "never" | null

Specify which of the MCP server’s tools require approval.

McpToolApprovalFilter { always, never }

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

always?: Always { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

never?: Never { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

"always" | "never"

"always"

"never"

server\_description?: string

Optional description of the MCP server, used to provide more context.

server\_url?: string

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

tunnel\_id?: string

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

CodeInterpreter { container, type, allowed\_callers }

A tool that runs Python code to help generate a response to a prompt.

container: string | CodeInterpreterToolAuto { type, file\_ids, memory\_limit, network\_policy }

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

string

CodeInterpreterToolAuto { type, file\_ids, memory\_limit, network\_policy }

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

type: "auto"

Always `auto`.

file\_ids?: Array<string>

An optional list of uploaded files to make available to your code.

memory\_limit?: "1g" | "4g" | "16g" | "64g" | null

The memory limit for the code interpreter container.

"1g"

"4g"

"16g"

"64g"

network\_policy?: [BetaContainerNetworkPolicyDisabled](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  | [BetaContainerNetworkPolicyAllowlist](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

BetaContainerNetworkPolicyDisabled { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

BetaContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array<string>

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets?: Array<[BetaContainerNetworkPolicyDomainSecret](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } >

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

minLength1

name: string

The name of the secret to inject for the domain.

minLength1

value: string

The secret value to inject for the domain.

maxLength10485760

minLength1

type: "code\_interpreter"

The type of the code interpreter tool. Always `code_interpreter`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

ProgrammaticToolCalling { type }

type: "programmatic\_tool\_calling"

The type of the tool. Always `programmatic_tool_calling`.

ImageGeneration { type, action, background, 9 more }

A tool that generates images using the GPT image models.

type: "image\_generation"

The type of the image generation tool. Always `image_generation`.

action?: "generate" | "edit" | "auto"

Whether to generate a new image or edit an existing image. Default: `auto`.

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

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

"high"

"low"

input\_image\_mask?: InputImageMask { file\_id, image\_url }

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

file\_id?: string

File ID for the mask image.

image\_url?: string

Base64-encoded mask image.

model?: (string & {}) | "gpt-image-1" | "gpt-image-1-mini" | "gpt-image-2" | 3 more

The image generation model to use. Default: `gpt-image-1`.

(string & {})

"gpt-image-1" | "gpt-image-1-mini" | "gpt-image-2" | 3 more

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation?: "auto" | "low"

Moderation level for the generated image. Default: `auto`.

"auto"

"low"

output\_compression?: number

Compression level for the output image. Default: 100.

minimum0

maximum100

output\_format?: "png" | "webp" | "jpeg"

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

"png"

"webp"

"jpeg"

partial\_images?: number

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

quality?: "low" | "medium" | "high" | "auto"

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

"low"

"medium"

"high"

"auto"

size?: (string & {}) | "1024x1024" | "1024x1536" | "1536x1024" | "auto"

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

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

A tool that allows the model to execute shell commands.

type: "shell"

The type of the shell tool. Always `shell`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

environment?: [BetaContainerAuto](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_auto%20%3E%20(schema)) { type, file\_ids, memory\_limit, 2 more }  | [BetaLocalEnvironment](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_environment%20%3E%20(schema)) { type, skills }  | [BetaContainerReference](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_reference%20%3E%20(schema)) { container\_id, type }  | null

BetaContainerAuto { type, file\_ids, memory\_limit, 2 more }

type: "container\_auto"

Automatically creates a container for this request

file\_ids?: Array<string>

An optional list of uploaded files to make available to your code.

memory\_limit?: "1g" | "4g" | "16g" | "64g" | null

The memory limit for the container.

"1g"

"4g"

"16g"

"64g"

network\_policy?: [BetaContainerNetworkPolicyDisabled](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  | [BetaContainerNetworkPolicyAllowlist](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

BetaContainerNetworkPolicyDisabled { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

BetaContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array<string>

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets?: Array<[BetaContainerNetworkPolicyDomainSecret](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } >

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

minLength1

name: string

The name of the secret to inject for the domain.

minLength1

value: string

The secret value to inject for the domain.

maxLength10485760

minLength1

skills?: Array<[BetaSkillReference](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_skill_reference%20%3E%20(schema)) { skill\_id, type, version }  | [BetaInlineSkill](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill%20%3E%20(schema)) { description, name, source, type } >

An optional list of skills referenced by id or inline data.

BetaSkillReference { skill\_id, type, version }

skill\_id: string

The ID of the referenced skill.

maxLength64

minLength1

type: "skill\_reference"

References a skill created with the /v1/skills endpoint.

version?: string

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

BetaInlineSkill { description, name, source, type }

description: string

The description of the skill.

name: string

The name of the skill.

source: [BetaInlineSkillSource](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema)) { data, media\_type, type }

Inline skill payload

data: string

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

media\_type: "application/zip"

The media type of the inline skill payload. Must be `application/zip`.

type: "base64"

The type of the inline skill source. Must be `base64`.

type: "inline"

Defines an inline skill for this request.

BetaLocalEnvironment { type, skills }

type: "local"

Use a local computer environment.

skills?: Array<[BetaLocalSkill](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema)) { description, name, path } >

An optional list of skills.

description: string

The description of the skill.

name: string

The name of the skill.

path: string

The path to the directory containing the skill.

BetaContainerReference { container\_id, type }

container\_id: string

The ID of the referenced container.

type: "container\_reference"

References a container created with the /v1/containers endpoint

BetaCustomTool { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this tool should be deferred and discovered via tool search.

description?: string

Optional description of the custom tool, used to provide more context.

format?: Text { type }  | Grammar { definition, syntax, type }

The input format for the custom tool. Default is unconstrained text.

Text { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar { definition, syntax, type }

A grammar defined by the user.

definition: string

The grammar definition.

syntax: "lark" | "regex"

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: "grammar"

Grammar format. Always `grammar`.

BetaNamespaceTool { description, name, tools, type }

Groups function/custom tools under a shared namespace.

description: string

A description of the namespace shown to the model.

minLength1

name: string

The namespace name used in tool calls (for example, `crm`).

minLength1

tools: Array<Function { name, type, allowed\_callers, 5 more }  | [BetaCustomTool](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_custom_tool%20%3E%20(schema)) { name, type, allowed\_callers, 3 more } >

The function/custom tools available inside this namespace.

Function { name, type, allowed\_callers, 5 more }

name: string

maxLength128

minLength1

type: "function"

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this function should be deferred and discovered via tool search.

description?: string | null

output\_schema?: Record<string, unknown> | null

A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

parameters?: unknown

strict?: boolean | null

Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

BetaCustomTool { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this tool should be deferred and discovered via tool search.

description?: string

Optional description of the custom tool, used to provide more context.

format?: Text { type }  | Grammar { definition, syntax, type }

The input format for the custom tool. Default is unconstrained text.

Text { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar { definition, syntax, type }

A grammar defined by the user.

definition: string

The grammar definition.

syntax: "lark" | "regex"

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: "grammar"

Grammar format. Always `grammar`.

type: "namespace"

The type of the tool. Always `namespace`.

BetaToolSearchTool { type, description, execution, parameters }

Hosted or BYOT tool search configuration for deferred tools.

type: "tool\_search"

The type of the tool. Always `tool_search`.

description?: string | null

Description shown to the model for a client-executed tool search tool.

execution?: "server" | "client"

Whether tool search is executed by the server or by the client.

"server"

"client"

parameters?: unknown

Parameter schema for a client-executed tool search tool.

BetaWebSearchPreviewTool { type, search\_content\_types, search\_context\_size, user\_location }

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: "web\_search\_preview" | "web\_search\_preview\_2025\_03\_11"

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types?: Array<"text" | "image">

"text"

"image"

search\_context\_size?: "low" | "medium" | "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

"low"

"medium"

"high"

user\_location?: UserLocation | null

The user’s location.

type: "approximate"

The type of location approximation. Always `approximate`.

city?: string | null

Free text input for the city of the user, e.g. `San Francisco`.

country?: string | null

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region?: string | null

Free text input for the region of the user, e.g. `California`.

timezone?: string | null

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

BetaApplyPatchTool { type, allowed\_callers }

Allows the assistant to create, delete, or update files using unified diffs.

type: "apply\_patch"

The type of the tool. Always `apply_patch`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

type: "tool\_search\_output"

The item type. Always `tool_search_output`.

id?: string | null

The unique ID of this tool search output.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

call\_id?: string | null

The unique ID of the tool search call generated by the model.

maxLength64

minLength1

execution?: "server" | "client"

Whether tool search was executed by the server or by the client.

"server"

"client"

status?: "in\_progress" | "completed" | "incomplete" | null

The status of the tool search output.

"in\_progress"

"completed"

"incomplete"

AdditionalTools { role, tools, type, 2 more }

role: "developer"

The role that provided the additional tools. Only `developer` is supported.

tools: Array<[BetaTool](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))>

A list of additional tools made available at this item.

BetaFunctionTool { name, parameters, strict, 5 more }

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

name: string

The name of the function to call.

parameters: Record<string, unknown> | null

A JSON schema object describing the parameters of the function.

strict: boolean | null

Whether strict parameter validation is enforced for this function tool.

type: "function"

The type of the function tool. Always `function`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this function is deferred and loaded via tool search.

description?: string | null

A description of the function. Used by the model to determine whether or not to call the function.

output\_schema?: Record<string, unknown> | null

A JSON schema object describing the JSON value encoded in string outputs for this function.

BetaFileSearchTool { type, vector\_store\_ids, filters, 2 more }

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

type: "file\_search"

The type of the file search tool. Always `file_search`.

vector\_store\_ids: Array<string>

The IDs of the vector stores to search.

filters?: ComparisonFilter { key, type, value }  | CompoundFilter { filters, type }  | null

A filter to apply.

ComparisonFilter { key, type, value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: string

The key to compare against the value.

type: "eq" | "ne" | "gt" | 5 more

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: string | number | boolean | Array<string | number>

The value to compare against the attribute key; supports string, number, or boolean types.

string

number

boolean

Array<string | number>

string

number

CompoundFilter { filters, type }

Combine multiple filters using `and` or `or`.

filters: Array<ComparisonFilter { key, type, value }  | unknown>

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

ComparisonFilter { key, type, value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: string

The key to compare against the value.

type: "eq" | "ne" | "gt" | 5 more

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: string | number | boolean | Array<string | number>

The value to compare against the attribute key; supports string, number, or boolean types.

string

number

boolean

Array<string | number>

string

number

unknown

type: "and" | "or"

Type of operation: `and` or `or`.

"and"

"or"

max\_num\_results?: number

The maximum number of results to return. This number should be between 1 and 50 inclusive.

ranking\_options?: RankingOptions { hybrid\_search, ranker, score\_threshold }

Ranking options for search.

hybrid\_search?: HybridSearch { embedding\_weight, text\_weight }

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

embedding\_weight: number

The weight of the embedding in the reciprocal ranking fusion.

text\_weight: number

The weight of the text in the reciprocal ranking fusion.

ranker?: "auto" | "default-2024-11-15"

The ranker to use for the file search.

"auto"

"default-2024-11-15"

score\_threshold?: number

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

BetaComputerTool { type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

type: "computer"

The type of the computer tool. Always `computer`.

BetaComputerUsePreviewTool { display\_height, display\_width, environment, type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

display\_height: number

The height of the computer display.

display\_width: number

The width of the computer display.

environment: "windows" | "mac" | "linux" | 2 more

The type of computer environment to control.

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: "computer\_use\_preview"

The type of the computer use tool. Always `computer_use_preview`.

BetaWebSearchTool { type, filters, search\_context\_size, user\_location }

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: "web\_search" | "web\_search\_2025\_08\_26"

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

"web\_search"

"web\_search\_2025\_08\_26"

filters?: Filters | null

Filters for the search.

allowed\_domains?: Array<string> | null

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

search\_context\_size?: "low" | "medium" | "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

"low"

"medium"

"high"

user\_location?: UserLocation | null

The approximate location of the user.

city?: string | null

Free text input for the city of the user, e.g. `San Francisco`.

country?: string | null

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region?: string | null

Free text input for the region of the user, e.g. `California`.

timezone?: string | null

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

type?: "approximate"

The type of location approximation. Always `approximate`.

Mcp { server\_label, type, allowed\_callers, 9 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: string

A label for this MCP server, used to identify it in tool calls.

type: "mcp"

The type of the MCP tool. Always `mcp`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

allowed\_tools?: Array<string> | McpToolFilter { read\_only, tool\_names }  | null

List of allowed tool names or a filter object.

Array<string>

McpToolFilter { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

authorization?: string

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

connector\_id?: "connector\_dropbox" | "connector\_gmail" | "connector\_googlecalendar" | 5 more

Identifier for service connectors, like those available in ChatGPT. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided. Learn more
about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

Currently supported `connector_id` values are:

* Dropbox: `connector_dropbox`
* Gmail: `connector_gmail`
* Google Calendar: `connector_googlecalendar`
* Google Drive: `connector_googledrive`
* Microsoft Teams: `connector_microsoftteams`
* Outlook Calendar: `connector_outlookcalendar`
* Outlook Email: `connector_outlookemail`
* SharePoint: `connector_sharepoint`

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading?: boolean

Whether this MCP tool is deferred and discovered via tool search.

headers?: Record<string, string> | null

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

require\_approval?: McpToolApprovalFilter { always, never }  | "always" | "never" | null

Specify which of the MCP server’s tools require approval.

McpToolApprovalFilter { always, never }

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

always?: Always { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

never?: Never { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

"always" | "never"

"always"

"never"

server\_description?: string

Optional description of the MCP server, used to provide more context.

server\_url?: string

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

tunnel\_id?: string

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

CodeInterpreter { container, type, allowed\_callers }

A tool that runs Python code to help generate a response to a prompt.

container: string | CodeInterpreterToolAuto { type, file\_ids, memory\_limit, network\_policy }

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

string

CodeInterpreterToolAuto { type, file\_ids, memory\_limit, network\_policy }

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

type: "auto"

Always `auto`.

file\_ids?: Array<string>

An optional list of uploaded files to make available to your code.

memory\_limit?: "1g" | "4g" | "16g" | "64g" | null

The memory limit for the code interpreter container.

"1g"

"4g"

"16g"

"64g"

network\_policy?: [BetaContainerNetworkPolicyDisabled](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  | [BetaContainerNetworkPolicyAllowlist](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

BetaContainerNetworkPolicyDisabled { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

BetaContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array<string>

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets?: Array<[BetaContainerNetworkPolicyDomainSecret](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } >

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

minLength1

name: string

The name of the secret to inject for the domain.

minLength1

value: string

The secret value to inject for the domain.

maxLength10485760

minLength1

type: "code\_interpreter"

The type of the code interpreter tool. Always `code_interpreter`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

ProgrammaticToolCalling { type }

type: "programmatic\_tool\_calling"

The type of the tool. Always `programmatic_tool_calling`.

ImageGeneration { type, action, background, 9 more }

A tool that generates images using the GPT image models.

type: "image\_generation"

The type of the image generation tool. Always `image_generation`.

action?: "generate" | "edit" | "auto"

Whether to generate a new image or edit an existing image. Default: `auto`.

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

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

"high"

"low"

input\_image\_mask?: InputImageMask { file\_id, image\_url }

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

file\_id?: string

File ID for the mask image.

image\_url?: string

Base64-encoded mask image.

model?: (string & {}) | "gpt-image-1" | "gpt-image-1-mini" | "gpt-image-2" | 3 more

The image generation model to use. Default: `gpt-image-1`.

(string & {})

"gpt-image-1" | "gpt-image-1-mini" | "gpt-image-2" | 3 more

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation?: "auto" | "low"

Moderation level for the generated image. Default: `auto`.

"auto"

"low"

output\_compression?: number

Compression level for the output image. Default: 100.

minimum0

maximum100

output\_format?: "png" | "webp" | "jpeg"

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

"png"

"webp"

"jpeg"

partial\_images?: number

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

quality?: "low" | "medium" | "high" | "auto"

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

"low"

"medium"

"high"

"auto"

size?: (string & {}) | "1024x1024" | "1024x1536" | "1536x1024" | "auto"

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

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

A tool that allows the model to execute shell commands.

type: "shell"

The type of the shell tool. Always `shell`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

environment?: [BetaContainerAuto](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_auto%20%3E%20(schema)) { type, file\_ids, memory\_limit, 2 more }  | [BetaLocalEnvironment](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_environment%20%3E%20(schema)) { type, skills }  | [BetaContainerReference](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_reference%20%3E%20(schema)) { container\_id, type }  | null

BetaContainerAuto { type, file\_ids, memory\_limit, 2 more }

type: "container\_auto"

Automatically creates a container for this request

file\_ids?: Array<string>

An optional list of uploaded files to make available to your code.

memory\_limit?: "1g" | "4g" | "16g" | "64g" | null

The memory limit for the container.

"1g"

"4g"

"16g"

"64g"

network\_policy?: [BetaContainerNetworkPolicyDisabled](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  | [BetaContainerNetworkPolicyAllowlist](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

BetaContainerNetworkPolicyDisabled { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

BetaContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array<string>

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets?: Array<[BetaContainerNetworkPolicyDomainSecret](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } >

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

minLength1

name: string

The name of the secret to inject for the domain.

minLength1

value: string

The secret value to inject for the domain.

maxLength10485760

minLength1

skills?: Array<[BetaSkillReference](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_skill_reference%20%3E%20(schema)) { skill\_id, type, version }  | [BetaInlineSkill](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill%20%3E%20(schema)) { description, name, source, type } >

An optional list of skills referenced by id or inline data.

BetaSkillReference { skill\_id, type, version }

skill\_id: string

The ID of the referenced skill.

maxLength64

minLength1

type: "skill\_reference"

References a skill created with the /v1/skills endpoint.

version?: string

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

BetaInlineSkill { description, name, source, type }

description: string

The description of the skill.

name: string

The name of the skill.

source: [BetaInlineSkillSource](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema)) { data, media\_type, type }

Inline skill payload

data: string

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

media\_type: "application/zip"

The media type of the inline skill payload. Must be `application/zip`.

type: "base64"

The type of the inline skill source. Must be `base64`.

type: "inline"

Defines an inline skill for this request.

BetaLocalEnvironment { type, skills }

type: "local"

Use a local computer environment.

skills?: Array<[BetaLocalSkill](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema)) { description, name, path } >

An optional list of skills.

description: string

The description of the skill.

name: string

The name of the skill.

path: string

The path to the directory containing the skill.

BetaContainerReference { container\_id, type }

container\_id: string

The ID of the referenced container.

type: "container\_reference"

References a container created with the /v1/containers endpoint

BetaCustomTool { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this tool should be deferred and discovered via tool search.

description?: string

Optional description of the custom tool, used to provide more context.

format?: Text { type }  | Grammar { definition, syntax, type }

The input format for the custom tool. Default is unconstrained text.

Text { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar { definition, syntax, type }

A grammar defined by the user.

definition: string

The grammar definition.

syntax: "lark" | "regex"

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: "grammar"

Grammar format. Always `grammar`.

BetaNamespaceTool { description, name, tools, type }

Groups function/custom tools under a shared namespace.

description: string

A description of the namespace shown to the model.

minLength1

name: string

The namespace name used in tool calls (for example, `crm`).

minLength1

tools: Array<Function { name, type, allowed\_callers, 5 more }  | [BetaCustomTool](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_custom_tool%20%3E%20(schema)) { name, type, allowed\_callers, 3 more } >

The function/custom tools available inside this namespace.

Function { name, type, allowed\_callers, 5 more }

name: string

maxLength128

minLength1

type: "function"

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this function should be deferred and discovered via tool search.

description?: string | null

output\_schema?: Record<string, unknown> | null

A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

parameters?: unknown

strict?: boolean | null

Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

BetaCustomTool { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this tool should be deferred and discovered via tool search.

description?: string

Optional description of the custom tool, used to provide more context.

format?: Text { type }  | Grammar { definition, syntax, type }

The input format for the custom tool. Default is unconstrained text.

Text { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar { definition, syntax, type }

A grammar defined by the user.

definition: string

The grammar definition.

syntax: "lark" | "regex"

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: "grammar"

Grammar format. Always `grammar`.

type: "namespace"

The type of the tool. Always `namespace`.

BetaToolSearchTool { type, description, execution, parameters }

Hosted or BYOT tool search configuration for deferred tools.

type: "tool\_search"

The type of the tool. Always `tool_search`.

description?: string | null

Description shown to the model for a client-executed tool search tool.

execution?: "server" | "client"

Whether tool search is executed by the server or by the client.

"server"

"client"

parameters?: unknown

Parameter schema for a client-executed tool search tool.

BetaWebSearchPreviewTool { type, search\_content\_types, search\_context\_size, user\_location }

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: "web\_search\_preview" | "web\_search\_preview\_2025\_03\_11"

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types?: Array<"text" | "image">

"text"

"image"

search\_context\_size?: "low" | "medium" | "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

"low"

"medium"

"high"

user\_location?: UserLocation | null

The user’s location.

type: "approximate"

The type of location approximation. Always `approximate`.

city?: string | null

Free text input for the city of the user, e.g. `San Francisco`.

country?: string | null

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region?: string | null

Free text input for the region of the user, e.g. `California`.

timezone?: string | null

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

BetaApplyPatchTool { type, allowed\_callers }

Allows the assistant to create, delete, or update files using unified diffs.

type: "apply\_patch"

The type of the tool. Always `apply_patch`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

type: "additional\_tools"

The item type. Always `additional_tools`.

id?: string | null

The unique ID of this additional tools item.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

BetaResponseReasoningItem { id, summary, type, 4 more }

A description of the chain of thought used by a reasoning model while generating
a response. Be sure to include these items in your `input` to the Responses API
for subsequent turns of a conversation if you are manually
[managing context](https://platform.openai.com/docs/guides/conversation-state).

id: string

The unique identifier of the reasoning content.

summary: Array<Summary>

Reasoning summary content.

text: string

A summary of the reasoning output from the model so far.

type: "summary\_text"

The type of the object. Always `summary_text`.

type: "reasoning"

The type of the object. Always `reasoning`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

content?: Array<Content>

Reasoning text content.

text: string

The reasoning text from the model.

type: "reasoning\_text"

The type of the reasoning text. Always `reasoning_text`.

encrypted\_content?: string | null

The encrypted content of the reasoning item. This is populated by default
for reasoning items returned by `POST /v1/responses` and WebSocket
`response.create` requests.

status?: "in\_progress" | "completed" | "incomplete"

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

BetaResponseCompactionItemParam { encrypted\_content, type, id, agent }

A compaction item generated by the [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).

encrypted\_content: string

The encrypted content of the compaction summary.

maxLength10485760

type: "compaction"

The type of the item. Always `compaction`.

id?: string | null

The ID of the compaction item.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

ImageGenerationCall { id, result, status, 2 more }

An image generation request made by the model.

id: string

The unique ID of the image generation call.

result: string | null

The generated image encoded in base64.

status: "in\_progress" | "completed" | "generating" | "failed"

The status of the image generation call.

"in\_progress"

"completed"

"generating"

"failed"

type: "image\_generation\_call"

The type of the image generation call. Always `image_generation_call`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

BetaResponseCodeInterpreterToolCall { id, code, container\_id, 4 more }

A tool call to run code.

id: string

The unique ID of the code interpreter tool call.

code: string | null

The code to run, or null if not available.

container\_id: string

The ID of the container used to run the code.

outputs: Array<Logs { logs, type }  | Image { type, url } > | null

The outputs generated by the code interpreter, such as logs or images.
Can be null if no outputs are available.

Logs { logs, type }

The logs output from the code interpreter.

logs: string

The logs output from the code interpreter.

type: "logs"

The type of the output. Always `logs`.

Image { type, url }

The image output from the code interpreter.

type: "image"

The type of the output. Always `image`.

url: string

The URL of the image output from the code interpreter.

formaturi

status: "in\_progress" | "completed" | "incomplete" | 2 more

The status of the code interpreter tool call. Valid values are `in_progress`, `completed`, `incomplete`, `interpreting`, and `failed`.

"in\_progress"

"completed"

"incomplete"

"interpreting"

"failed"

type: "code\_interpreter\_call"

The type of the code interpreter tool call. Always `code_interpreter_call`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

LocalShellCall { id, action, call\_id, 3 more }

A tool call to run a command on the local shell.

id: string

The unique ID of the local shell call.

action: Action { command, env, type, 3 more }

Execute a shell command on the server.

command: Array<string>

The command to run.

env: Record<string, string>

Environment variables to set for the command.

type: "exec"

The type of the local shell action. Always `exec`.

timeout\_ms?: number | null

Optional timeout in milliseconds for the command.

user?: string | null

Optional user to run the command as.

working\_directory?: string | null

Optional working directory to run the command in.

call\_id: string

The unique ID of the local shell tool call generated by the model.

status: "in\_progress" | "completed" | "incomplete"

The status of the local shell call.

"in\_progress"

"completed"

"incomplete"

type: "local\_shell\_call"

The type of the local shell call. Always `local_shell_call`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

LocalShellCallOutput { id, output, type, 2 more }

The output of a local shell tool call.

id: string

The unique ID of the local shell tool call generated by the model.

output: string

A JSON string of the output of the local shell tool call.

type: "local\_shell\_call\_output"

The type of the local shell tool call output. Always `local_shell_call_output`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

status?: "in\_progress" | "completed" | "incomplete" | null

The status of the item. One of `in_progress`, `completed`, or `incomplete`.

"in\_progress"

"completed"

"incomplete"

ShellCall { action, call\_id, type, 5 more }

A tool representing a request to execute one or more shell commands.

action: Action { commands, max\_output\_length, timeout\_ms }

The shell commands and limits that describe how to run the tool call.

commands: Array<string>

Ordered shell commands for the execution environment to run.

max\_output\_length?: number | null

Maximum number of UTF-8 characters to capture from combined stdout and stderr output.

timeout\_ms?: number | null

Maximum wall-clock time in milliseconds to allow the shell commands to run.

call\_id: string

The unique ID of the shell tool call generated by the model.

maxLength64

minLength1

type: "shell\_call"

The type of the item. Always `shell_call`.

id?: string | null

The unique ID of the shell tool call. Populated when this item is returned via API.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

caller?: Direct { type }  | Program { caller\_id, type }  | null

The execution context that produced this tool call.

Direct { type }

type: "direct"

The caller type. Always `direct`.

Program { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

maxLength64

minLength1

type: "program"

The caller type. Always `program`.

environment?: [BetaLocalEnvironment](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_environment%20%3E%20(schema)) { type, skills }  | [BetaContainerReference](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_reference%20%3E%20(schema)) { container\_id, type }  | null

The environment to execute the shell commands in.

BetaLocalEnvironment { type, skills }

type: "local"

Use a local computer environment.

skills?: Array<[BetaLocalSkill](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema)) { description, name, path } >

An optional list of skills.

description: string

The description of the skill.

name: string

The name of the skill.

path: string

The path to the directory containing the skill.

BetaContainerReference { container\_id, type }

container\_id: string

The ID of the referenced container.

type: "container\_reference"

References a container created with the /v1/containers endpoint

status?: "in\_progress" | "completed" | "incomplete" | null

The status of the shell call. One of `in_progress`, `completed`, or `incomplete`.

"in\_progress"

"completed"

"incomplete"

ShellCallOutput { call\_id, output, type, 5 more }

The streamed output items emitted by a shell tool call.

call\_id: string

The unique ID of the shell tool call generated by the model.

maxLength64

minLength1

output: Array<[BetaResponseFunctionShellCallOutputContent](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_shell_call_output_content%20%3E%20(schema)) { outcome, stderr, stdout } >

Captured chunks of stdout and stderr output, along with their associated outcomes.

outcome: Timeout { type }  | Exit { exit\_code, type }

The exit or timeout outcome associated with this shell call.

Timeout { type }

Indicates that the shell call exceeded its configured time limit.

type: "timeout"

The outcome type. Always `timeout`.

Exit { exit\_code, type }

Indicates that the shell commands finished and returned an exit code.

exit\_code: number

The exit code returned by the shell process.

type: "exit"

The outcome type. Always `exit`.

stderr: string

Captured stderr output for the shell call.

maxLength10485760

stdout: string

Captured stdout output for the shell call.

maxLength10485760

type: "shell\_call\_output"

The type of the item. Always `shell_call_output`.

id?: string | null

The unique ID of the shell tool call output. Populated when this item is returned via API.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

caller?: Direct { type }  | Program { caller\_id, type }  | null

The execution context that produced this tool call.

Direct { type }

type: "direct"

The caller type. Always `direct`.

Program { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

maxLength64

minLength1

type: "program"

The caller type. Always `program`.

max\_output\_length?: number | null

The maximum number of UTF-8 characters captured for this shell call’s combined output.

status?: "in\_progress" | "completed" | "incomplete" | null

The status of the shell call output.

"in\_progress"

"completed"

"incomplete"

ApplyPatchCall { call\_id, operation, status, 4 more }

A tool call representing a request to create, delete, or update files using diff patches.

call\_id: string

The unique ID of the apply patch tool call generated by the model.

maxLength64

minLength1

operation: CreateFile { diff, path, type }  | DeleteFile { path, type }  | UpdateFile { diff, path, type }

The specific create, delete, or update instruction for the apply\_patch tool call.

CreateFile { diff, path, type }

Instruction for creating a new file via the apply\_patch tool.

diff: string

Unified diff content to apply when creating the file.

maxLength10485760

path: string

Path of the file to create relative to the workspace root.

minLength1

type: "create\_file"

The operation type. Always `create_file`.

DeleteFile { path, type }

Instruction for deleting an existing file via the apply\_patch tool.

path: string

Path of the file to delete relative to the workspace root.

minLength1

type: "delete\_file"

The operation type. Always `delete_file`.

UpdateFile { diff, path, type }

Instruction for updating an existing file via the apply\_patch tool.

diff: string

Unified diff content to apply to the existing file.

maxLength10485760

path: string

Path of the file to update relative to the workspace root.

minLength1

type: "update\_file"

The operation type. Always `update_file`.

status: "in\_progress" | "completed"

The status of the apply patch tool call. One of `in_progress` or `completed`.

"in\_progress"

"completed"

type: "apply\_patch\_call"

The type of the item. Always `apply_patch_call`.

id?: string | null

The unique ID of the apply patch tool call. Populated when this item is returned via API.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

caller?: Direct { type }  | Program { caller\_id, type }  | null

The execution context that produced this tool call.

Direct { type }

type: "direct"

The caller type. Always `direct`.

Program { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

maxLength64

minLength1

type: "program"

The caller type. Always `program`.

ApplyPatchCallOutput { call\_id, status, type, 4 more }

The streamed output emitted by an apply patch tool call.

call\_id: string

The unique ID of the apply patch tool call generated by the model.

maxLength64

minLength1

status: "completed" | "failed"

The status of the apply patch tool call output. One of `completed` or `failed`.

"completed"

"failed"

type: "apply\_patch\_call\_output"

The type of the item. Always `apply_patch_call_output`.

id?: string | null

The unique ID of the apply patch tool call output. Populated when this item is returned via API.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

caller?: Direct { type }  | Program { caller\_id, type }  | null

The execution context that produced this tool call.

Direct { type }

type: "direct"

The caller type. Always `direct`.

Program { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

maxLength64

minLength1

type: "program"

The caller type. Always `program`.

output?: string | null

Optional human-readable log text from the apply patch tool (e.g., patch results or errors).

maxLength10485760

McpListTools { id, server\_label, tools, 3 more }

A list of tools available on an MCP server.

id: string

The unique ID of the list.

server\_label: string

The label of the MCP server.

tools: Array<Tool>

The tools available on the server.

input\_schema: unknown

The JSON schema describing the tool’s input.

name: string

The name of the tool.

annotations?: unknown

Additional annotations about the tool.

description?: string | null

The description of the tool.

type: "mcp\_list\_tools"

The type of the item. Always `mcp_list_tools`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

error?: string | null

Error message if the server could not list tools.

McpApprovalRequest { id, arguments, name, 3 more }

A request for human approval of a tool invocation.

id: string

The unique ID of the approval request.

arguments: string

A JSON string of arguments for the tool.

name: string

The name of the tool to run.

server\_label: string

The label of the MCP server making the request.

type: "mcp\_approval\_request"

The type of the item. Always `mcp_approval_request`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

McpApprovalResponse { approval\_request\_id, approve, type, 3 more }

A response to an MCP approval request.

approval\_request\_id: string

The ID of the approval request being answered.

approve: boolean

Whether the request was approved.

type: "mcp\_approval\_response"

The type of the item. Always `mcp_approval_response`.

id?: string | null

The unique ID of the approval response

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

reason?: string | null

Optional reason for the decision.

McpCall { id, arguments, name, 7 more }

An invocation of a tool on an MCP server.

id: string

The unique ID of the tool call.

arguments: string

A JSON string of the arguments passed to the tool.

name: string

The name of the tool that was run.

server\_label: string

The label of the MCP server running the tool.

type: "mcp\_call"

The type of the item. Always `mcp_call`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

approval\_request\_id?: string | null

Unique identifier for the MCP tool call approval request.
Include this value in a subsequent `mcp_approval_response` input to approve or reject the corresponding tool call.

error?: string | null

The error from the tool call, if any.

output?: string | null

The output from the tool call.

status?: "in\_progress" | "completed" | "incomplete" | 2 more

The status of the tool call. One of `in_progress`, `completed`, `incomplete`, `calling`, or `failed`.

"in\_progress"

"completed"

"incomplete"

"calling"

"failed"

BetaResponseCustomToolCallOutput { call\_id, output, type, 3 more }

The output of a custom tool call from your code, being sent back to the model.

call\_id: string

The call ID, used to map this custom tool call output to a custom tool call.

output: string | Array<[BetaResponseInputText](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_text%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  | [BetaResponseInputImage](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_image%20%3E%20(schema)) { detail, type, file\_id, 2 more }  | [BetaResponseInputFile](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_file%20%3E%20(schema)) { type, detail, file\_data, 4 more } >

The output from the custom tool call generated by your code.
Can be a string or an list of output content.

string

Array<[BetaResponseInputText](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_text%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  | [BetaResponseInputImage](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_image%20%3E%20(schema)) { detail, type, file\_id, 2 more }  | [BetaResponseInputFile](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_file%20%3E%20(schema)) { type, detail, file\_data, 4 more } >

BetaResponseInputText { text, type, prompt\_cache\_breakpoint }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

BetaResponseInputImage { detail, type, file\_id, 2 more }

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: "low" | "high" | "auto" | "original"

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

"low"

"high"

"auto"

"original"

type: "input\_image"

The type of the input item. Always `input_image`.

file\_id?: string | null

The ID of the file to be sent to the model.

image\_url?: string | null

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

BetaResponseInputFile { type, detail, file\_data, 4 more }

A file input to the model.

type: "input\_file"

The type of the input item. Always `input_file`.

detail?: "auto" | "low" | "high"

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

"auto"

"low"

"high"

file\_data?: string

The content of the file to be sent to the model.

file\_id?: string | null

The ID of the file to be sent to the model.

file\_url?: string

The URL of the file to be sent to the model.

formaturi

filename?: string

The name of the file to be sent to the model.

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

type: "custom\_tool\_call\_output"

The type of the custom tool call output. Always `custom_tool_call_output`.

id?: string

The unique ID of the custom tool call output in the OpenAI platform.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

caller?: Direct { type }  | Program { caller\_id, type }  | null

The execution context that produced this tool call.

Direct { type }

type: "direct"

The caller type. Always `direct`.

Program { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

maxLength64

minLength1

type: "program"

The caller type. Always `program`.

BetaResponseCustomToolCall { call\_id, input, name, 5 more }

A call to a custom tool created by the model.

call\_id: string

An identifier used to map this custom tool call to a tool call output.

input: string

The input for the custom tool call generated by the model.

name: string

The name of the custom tool being called.

type: "custom\_tool\_call"

The type of the custom tool call. Always `custom_tool_call`.

id?: string

The unique ID of the custom tool call in the OpenAI platform.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

caller?: Direct { type }  | Program { caller\_id, type }  | null

The execution context that produced this tool call.

Direct { type }

type: "direct"

Program { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

type: "program"

namespace?: string

The namespace of the custom tool being called.

CompactionTrigger { type, agent }

Compacts the current context. Must be the final input item.

type: "compaction\_trigger"

The type of the item. Always `compaction_trigger`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

ItemReference { id, agent, type }

An internal identifier for an item to reference.

id: string

The ID of the item to reference.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

type?: "item\_reference" | null

The type of item to reference. Always `item_reference`.

Program { id, call\_id, code, 3 more }

id: string

The unique ID of this program item.

call\_id: string

The stable call ID of the program item.

maxLength64

minLength1

code: string

The JavaScript source executed by programmatic tool calling.

maxLength10485760

fingerprint: string

Opaque program replay fingerprint that must be round-tripped.

maxLength10485760

type: "program"

The item type. Always `program`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

ProgramOutput { id, call\_id, result, 3 more }

id: string

The unique ID of this program output item.

call\_id: string

The call ID of the program item.

maxLength64

minLength1

result: string

The result produced by the program item.

maxLength10485760

status: "completed" | "incomplete"

The terminal status of the program output.

"completed"

"incomplete"

type: "program\_output"

The item type. Always `program_output`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

metadata: Record<string, string> | null

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: "gpt-5.6-sol" | "gpt-5.6-terra" | "gpt-5.6-luna" | 92 more | (string & {})

Model ID used to generate the response, like `gpt-4o` or `o3`. OpenAI
offers a wide range of models with different capabilities, performance
characteristics, and price points. Refer to the [model guide](https://platform.openai.com/docs/models)
to browse and compare available models.

"gpt-5.6-sol" | "gpt-5.6-terra" | "gpt-5.6-luna" | 92 more

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

(string & {})

object: "response"

The object type of this resource - always set to `response`.

output: Array<[BetaResponseOutputItem](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_item%20%3E%20(schema))>

An array of content items generated by the model.

* The length and order of items in the `output` array is dependent
  on the model’s response.
* Rather than accessing the first item in the `output` array and
  assuming it’s an `assistant` message with the content generated by
  the model, you might consider using the `output_text` property where
  supported in SDKs.

BetaResponseOutputMessage { id, content, role, 4 more }

An output message from the model.

id: string

The unique ID of the output message.

content: Array<[BetaResponseOutputText](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_text%20%3E%20(schema)) { annotations, text, type, logprobs }  | [BetaResponseOutputRefusal](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_refusal%20%3E%20(schema)) { refusal, type } >

The content of the output message.

BetaResponseOutputText { annotations, text, type, logprobs }

A text output from the model.

annotations: Array<FileCitation { file\_id, filename, index, type }  | URLCitation { end\_index, start\_index, title, 2 more }  | ContainerFileCitation { container\_id, end\_index, file\_id, 3 more }  | FilePath { file\_id, index, type } >

The annotations of the text output.

FileCitation { file\_id, filename, index, type }

A citation to a file.

file\_id: string

The ID of the file.

filename: string

The filename of the file cited.

index: number

The index of the file in the list of files.

type: "file\_citation"

The type of the file citation. Always `file_citation`.

URLCitation { end\_index, start\_index, title, 2 more }

A citation for a web resource used to generate a model response.

end\_index: number

The index of the last character of the URL citation in the message.

start\_index: number

The index of the first character of the URL citation in the message.

title: string

The title of the web resource.

type: "url\_citation"

The type of the URL citation. Always `url_citation`.

url: string

The URL of the web resource.

formaturi

ContainerFileCitation { container\_id, end\_index, file\_id, 3 more }

A citation for a container file used to generate a model response.

container\_id: string

The ID of the container file.

end\_index: number

The index of the last character of the container file citation in the message.

file\_id: string

The ID of the file.

filename: string

The filename of the container file cited.

start\_index: number

The index of the first character of the container file citation in the message.

type: "container\_file\_citation"

The type of the container file citation. Always `container_file_citation`.

FilePath { file\_id, index, type }

A path to a file.

file\_id: string

The ID of the file.

index: number

The index of the file in the list of files.

type: "file\_path"

The type of the file path. Always `file_path`.

text: string

The text output from the model.

type: "output\_text"

The type of the output text. Always `output_text`.

logprobs?: Array<Logprob>

token: string

bytes: Array<number>

logprob: number

top\_logprobs: Array<TopLogprob>

token: string

bytes: Array<number>

logprob: number

BetaResponseOutputRefusal { refusal, type }

A refusal from the model.

refusal: string

The refusal explanation from the model.

type: "refusal"

The type of the refusal. Always `refusal`.

role: "assistant"

The role of the output message. Always `assistant`.

status: "in\_progress" | "completed" | "incomplete"

The status of the message input. One of `in_progress`, `completed`, or
`incomplete`. Populated when input items are returned via API.

"in\_progress"

"completed"

"incomplete"

type: "message"

The type of the output message. Always `message`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

phase?: "commentary" | "final\_answer" | null

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

"commentary"

"final\_answer"

BetaResponseFileSearchToolCall { id, queries, status, 3 more }

The results of a file search tool call. See the
[file search guide](https://platform.openai.com/docs/guides/tools-file-search) for more information.

id: string

The unique ID of the file search tool call.

queries: Array<string>

The queries used to search for files.

status: "in\_progress" | "searching" | "completed" | 2 more

The status of the file search tool call. One of `in_progress`,
`searching`, `incomplete` or `failed`,

"in\_progress"

"searching"

"completed"

"incomplete"

"failed"

type: "file\_search\_call"

The type of the file search tool call. Always `file_search_call`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

results?: Array<Result> | null

The results of the file search tool call.

attributes?: Record<string, string | number | boolean> | null

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.

string

number

boolean

file\_id?: string

The unique ID of the file.

filename?: string

The name of the file.

score?: number

The relevance score of the file - a value between 0 and 1.

formatfloat

text?: string

The text that was retrieved from the file.

BetaResponseFunctionToolCall { arguments, call\_id, name, 6 more }

A tool call to run a function. See the
[function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.

arguments: string

A JSON string of the arguments to pass to the function.

call\_id: string

The unique ID of the function tool call generated by the model.

name: string

The name of the function to run.

type: "function\_call"

The type of the function tool call. Always `function_call`.

id?: string

The unique ID of the function tool call.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

caller?: Direct { type }  | Program { caller\_id, type }  | null

The execution context that produced this tool call.

Direct { type }

type: "direct"

Program { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

type: "program"

namespace?: string

The namespace of the function to run.

status?: "in\_progress" | "completed" | "incomplete"

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

BetaResponseFunctionToolCallOutputItem { id, call\_id, output, 5 more }

id: string

The unique ID of the function call tool output.

call\_id: string

The unique ID of the function tool call generated by the model.

output: string | Array<[BetaResponseInputText](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_text%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  | [BetaResponseInputImage](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_image%20%3E%20(schema)) { detail, type, file\_id, 2 more }  | [BetaResponseInputFile](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_file%20%3E%20(schema)) { type, detail, file\_data, 4 more } >

The output from the function call generated by your code.
Can be a string or an list of output content.

string

Array<[BetaResponseInputText](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_text%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  | [BetaResponseInputImage](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_image%20%3E%20(schema)) { detail, type, file\_id, 2 more }  | [BetaResponseInputFile](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_file%20%3E%20(schema)) { type, detail, file\_data, 4 more } >

BetaResponseInputText { text, type, prompt\_cache\_breakpoint }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

BetaResponseInputImage { detail, type, file\_id, 2 more }

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: "low" | "high" | "auto" | "original"

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

"low"

"high"

"auto"

"original"

type: "input\_image"

The type of the input item. Always `input_image`.

file\_id?: string | null

The ID of the file to be sent to the model.

image\_url?: string | null

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

BetaResponseInputFile { type, detail, file\_data, 4 more }

A file input to the model.

type: "input\_file"

The type of the input item. Always `input_file`.

detail?: "auto" | "low" | "high"

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

"auto"

"low"

"high"

file\_data?: string

The content of the file to be sent to the model.

file\_id?: string | null

The ID of the file to be sent to the model.

file\_url?: string

The URL of the file to be sent to the model.

formaturi

filename?: string

The name of the file to be sent to the model.

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

status: "in\_progress" | "completed" | "incomplete"

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

type: "function\_call\_output"

The type of the function tool call output. Always `function_call_output`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

caller?: Direct { type }  | Program { caller\_id, type }  | null

The execution context that produced this tool call.

Direct { type }

type: "direct"

The caller type. Always `direct`.

Program { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

maxLength64

minLength1

type: "program"

The caller type. Always `program`.

created\_by?: string

The identifier of the actor that created the item.

AgentMessage { id, author, content, 3 more }

id: string

The unique ID of the agent message.

author: string

The sending agent identity.

content: Array<[BetaResponseInputText](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_text%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  | [BetaResponseOutputText](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_text%20%3E%20(schema)) { annotations, text, type, logprobs }  | Text { text, type }  | 7 more>

Encrypted content sent between agents.

BetaResponseInputText { text, type, prompt\_cache\_breakpoint }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

BetaResponseOutputText { annotations, text, type, logprobs }

A text output from the model.

annotations: Array<FileCitation { file\_id, filename, index, type }  | URLCitation { end\_index, start\_index, title, 2 more }  | ContainerFileCitation { container\_id, end\_index, file\_id, 3 more }  | FilePath { file\_id, index, type } >

The annotations of the text output.

FileCitation { file\_id, filename, index, type }

A citation to a file.

file\_id: string

The ID of the file.

filename: string

The filename of the file cited.

index: number

The index of the file in the list of files.

type: "file\_citation"

The type of the file citation. Always `file_citation`.

URLCitation { end\_index, start\_index, title, 2 more }

A citation for a web resource used to generate a model response.

end\_index: number

The index of the last character of the URL citation in the message.

start\_index: number

The index of the first character of the URL citation in the message.

title: string

The title of the web resource.

type: "url\_citation"

The type of the URL citation. Always `url_citation`.

url: string

The URL of the web resource.

formaturi

ContainerFileCitation { container\_id, end\_index, file\_id, 3 more }

A citation for a container file used to generate a model response.

container\_id: string

The ID of the container file.

end\_index: number

The index of the last character of the container file citation in the message.

file\_id: string

The ID of the file.

filename: string

The filename of the container file cited.

start\_index: number

The index of the first character of the container file citation in the message.

type: "container\_file\_citation"

The type of the container file citation. Always `container_file_citation`.

FilePath { file\_id, index, type }

A path to a file.

file\_id: string

The ID of the file.

index: number

The index of the file in the list of files.

type: "file\_path"

The type of the file path. Always `file_path`.

text: string

The text output from the model.

type: "output\_text"

The type of the output text. Always `output_text`.

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

A summary of the reasoning output from the model so far.

type: "summary\_text"

The type of the object. Always `summary_text`.

ReasoningText { text, type }

Reasoning text from the model.

text: string

The reasoning text from the model.

type: "reasoning\_text"

The type of the reasoning text. Always `reasoning_text`.

BetaResponseOutputRefusal { refusal, type }

A refusal from the model.

refusal: string

The refusal explanation from the model.

type: "refusal"

The type of the refusal. Always `refusal`.

BetaResponseInputImage { detail, type, file\_id, 2 more }

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: "low" | "high" | "auto" | "original"

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

"low"

"high"

"auto"

"original"

type: "input\_image"

The type of the input item. Always `input_image`.

file\_id?: string | null

The ID of the file to be sent to the model.

image\_url?: string | null

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

ComputerScreenshot { detail, file\_id, image\_url, 2 more }

A screenshot of a computer.

detail: "low" | "high" | "auto" | "original"

The detail level of the screenshot image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

"low"

"high"

"auto"

"original"

file\_id: string | null

The identifier of an uploaded file that contains the screenshot.

image\_url: string | null

The URL of the screenshot image.

formaturi

type: "computer\_screenshot"

Specifies the event type. For a computer screenshot, this property is always set to `computer_screenshot`.

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

BetaResponseInputFile { type, detail, file\_data, 4 more }

A file input to the model.

type: "input\_file"

The type of the input item. Always `input_file`.

detail?: "auto" | "low" | "high"

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

"auto"

"low"

"high"

file\_data?: string

The content of the file to be sent to the model.

file\_id?: string | null

The ID of the file to be sent to the model.

file\_url?: string

The URL of the file to be sent to the model.

formaturi

filename?: string

The name of the file to be sent to the model.

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

EncryptedContent { encrypted\_content, type }

Opaque encrypted content that Responses API decrypts inside trusted model execution.

encrypted\_content: string

Opaque encrypted content.

type: "encrypted\_content"

The type of the input item. Always `encrypted_content`.

recipient: string

The destination agent identity.

type: "agent\_message"

The type of the item. Always `agent_message`.

agent?: Agent { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

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

The unique ID linking this call to its output.

type: "multi\_agent\_call"

The type of the multi-agent call. Always `multi_agent_call`.

agent?: Agent { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

MultiAgentCallOutput { id, action, call\_id, 3 more }

id: string

The unique ID of the multi-agent call output item.

action: "spawn\_agent" | "interrupt\_agent" | "list\_agents" | 3 more

The multi-agent action that produced this result.

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

call\_id: string

The unique ID of the multi-agent call.

output: Array<[BetaResponseOutputText](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_text%20%3E%20(schema)) { annotations, text, type, logprobs } >

Text output returned by the multi-agent action.

annotations: Array<FileCitation { file\_id, filename, index, type }  | URLCitation { end\_index, start\_index, title, 2 more }  | ContainerFileCitation { container\_id, end\_index, file\_id, 3 more }  | FilePath { file\_id, index, type } >

The annotations of the text output.

FileCitation { file\_id, filename, index, type }

A citation to a file.

file\_id: string

The ID of the file.

filename: string

The filename of the file cited.

index: number

The index of the file in the list of files.

type: "file\_citation"

The type of the file citation. Always `file_citation`.

URLCitation { end\_index, start\_index, title, 2 more }

A citation for a web resource used to generate a model response.

end\_index: number

The index of the last character of the URL citation in the message.

start\_index: number

The index of the first character of the URL citation in the message.

title: string

The title of the web resource.

type: "url\_citation"

The type of the URL citation. Always `url_citation`.

url: string

The URL of the web resource.

formaturi

ContainerFileCitation { container\_id, end\_index, file\_id, 3 more }

A citation for a container file used to generate a model response.

container\_id: string

The ID of the container file.

end\_index: number

The index of the last character of the container file citation in the message.

file\_id: string

The ID of the file.

filename: string

The filename of the container file cited.

start\_index: number

The index of the first character of the container file citation in the message.

type: "container\_file\_citation"

The type of the container file citation. Always `container_file_citation`.

FilePath { file\_id, index, type }

A path to a file.

file\_id: string

The ID of the file.

index: number

The index of the file in the list of files.

type: "file\_path"

The type of the file path. Always `file_path`.

text: string

The text output from the model.

type: "output\_text"

The type of the output text. Always `output_text`.

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

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

BetaResponseFunctionWebSearch { id, action, status, 2 more }

The results of a web search tool call. See the
[web search guide](https://platform.openai.com/docs/guides/tools-web-search) for more information.

id: string

The unique ID of the web search tool call.

action: Search { type, queries, query, sources }  | OpenPage { type, url }  | FindInPage { pattern, type, url }

An object describing the specific action taken in this web search call.
Includes details on how the model used the web (search, open\_page, find\_in\_page).

Search { type, queries, query, sources }

Action type “search” - Performs a web search query.

type: "search"

The action type.

queries?: Array<string>

The search queries.

Deprecatedquery?: string

The search query.

sources?: Array<Source>

The sources used in the search.

type: "url"

The type of source. Always `url`.

url: string

The URL of the source.

formaturi

OpenPage { type, url }

Action type “open\_page” - Opens a specific URL from search results.

type: "open\_page"

The action type.

url?: string | null

The URL opened by the model.

formaturi

FindInPage { pattern, type, url }

Action type “find\_in\_page”: Searches for a pattern within a loaded page.

pattern: string

The pattern or text to search for within the page.

type: "find\_in\_page"

The action type.

url: string

The URL of the page searched for the pattern.

formaturi

status: "in\_progress" | "searching" | "completed" | "failed"

The status of the web search tool call.

"in\_progress"

"searching"

"completed"

"failed"

type: "web\_search\_call"

The type of the web search tool call. Always `web_search_call`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

BetaResponseComputerToolCall { id, call\_id, pending\_safety\_checks, 5 more }

A tool call to a computer use tool. See the
[computer use guide](https://platform.openai.com/docs/guides/tools-computer-use) for more information.

id: string

The unique ID of the computer call.

call\_id: string

An identifier used when responding to the tool call with output.

pending\_safety\_checks: Array<PendingSafetyCheck>

The pending safety checks for the computer call.

id: string

The ID of the pending safety check.

code?: string | null

The type of the pending safety check.

message?: string | null

Details about the pending safety check.

status: "in\_progress" | "completed" | "incomplete"

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

type: "computer\_call"

The type of the computer call. Always `computer_call`.

action?: [BetaComputerAction](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_computer_action%20%3E%20(schema))

A click action.

Click { button, type, x, 2 more }

A click action.

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

[
  { x: 100, y: 200 },
  { x: 200, y: 300 }
]

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

Flattened batched actions for `computer_use`. Each action includes an
`type` discriminator and action-specific fields.

Click { button, type, x, 2 more }

A click action.

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

[
  { x: 100, y: 200 },
  { x: 200, y: 300 }
]

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

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

BetaResponseComputerToolCallOutputItem { id, call\_id, output, 5 more }

id: string

The unique ID of the computer call tool output.

call\_id: string

The ID of the computer tool call that produced the output.

output: [BetaResponseComputerToolCallOutputScreenshot](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_computer_tool_call_output_screenshot%20%3E%20(schema)) { type, file\_id, image\_url }

A computer screenshot image used with the computer use tool.

type: "computer\_screenshot"

Specifies the event type. For a computer screenshot, this property is
always set to `computer_screenshot`.

file\_id?: string

The identifier of an uploaded file that contains the screenshot.

image\_url?: string

The URL of the screenshot image.

formaturi

status: "completed" | "incomplete" | "failed" | "in\_progress"

The status of the message input. One of `in_progress`, `completed`, or
`incomplete`. Populated when input items are returned via API.

"completed"

"incomplete"

"failed"

"in\_progress"

type: "computer\_call\_output"

The type of the computer tool call output. Always `computer_call_output`.

acknowledged\_safety\_checks?: Array<AcknowledgedSafetyCheck>

The safety checks reported by the API that have been acknowledged by the
developer.

id: string

The ID of the pending safety check.

code?: string | null

The type of the pending safety check.

message?: string | null

Details about the pending safety check.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

created\_by?: string

The identifier of the actor that created the item.

BetaResponseReasoningItem { id, summary, type, 4 more }

A description of the chain of thought used by a reasoning model while generating
a response. Be sure to include these items in your `input` to the Responses API
for subsequent turns of a conversation if you are manually
[managing context](https://platform.openai.com/docs/guides/conversation-state).

id: string

The unique identifier of the reasoning content.

summary: Array<Summary>

Reasoning summary content.

text: string

A summary of the reasoning output from the model so far.

type: "summary\_text"

The type of the object. Always `summary_text`.

type: "reasoning"

The type of the object. Always `reasoning`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

content?: Array<Content>

Reasoning text content.

text: string

The reasoning text from the model.

type: "reasoning\_text"

The type of the reasoning text. Always `reasoning_text`.

encrypted\_content?: string | null

The encrypted content of the reasoning item. This is populated by default
for reasoning items returned by `POST /v1/responses` and WebSocket
`response.create` requests.

status?: "in\_progress" | "completed" | "incomplete"

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

Program { id, call\_id, code, 3 more }

id: string

The unique ID of the program item.

call\_id: string

The stable call ID of the program item.

code: string

The JavaScript source executed by programmatic tool calling.

fingerprint: string

Opaque program replay fingerprint that must be round-tripped.

type: "program"

The type of the item. Always `program`.

agent?: Agent { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

ProgramOutput { id, call\_id, result, 3 more }

id: string

The unique ID of the program output item.

call\_id: string

The call ID of the program item.

result: string

The result produced by the program item.

status: "completed" | "incomplete"

The terminal status of the program output item.

"completed"

"incomplete"

type: "program\_output"

The type of the item. Always `program_output`.

agent?: Agent { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

BetaResponseToolSearchCall { id, arguments, call\_id, 5 more }

id: string

The unique ID of the tool search call item.

arguments: unknown

Arguments used for the tool search call.

call\_id: string | null

The unique ID of the tool search call generated by the model.

execution: "server" | "client"

Whether tool search was executed by the server or by the client.

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

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

created\_by?: string

The identifier of the actor that created the item.

BetaResponseToolSearchOutputItem { id, call\_id, execution, 5 more }

id: string

The unique ID of the tool search output item.

call\_id: string | null

The unique ID of the tool search call generated by the model.

execution: "server" | "client"

Whether tool search was executed by the server or by the client.

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

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

name: string

The name of the function to call.

parameters: Record<string, unknown> | null

A JSON schema object describing the parameters of the function.

strict: boolean | null

Whether strict parameter validation is enforced for this function tool.

type: "function"

The type of the function tool. Always `function`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this function is deferred and loaded via tool search.

description?: string | null

A description of the function. Used by the model to determine whether or not to call the function.

output\_schema?: Record<string, unknown> | null

A JSON schema object describing the JSON value encoded in string outputs for this function.

BetaFileSearchTool { type, vector\_store\_ids, filters, 2 more }

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

type: "file\_search"

The type of the file search tool. Always `file_search`.

vector\_store\_ids: Array<string>

The IDs of the vector stores to search.

filters?: ComparisonFilter { key, type, value }  | CompoundFilter { filters, type }  | null

A filter to apply.

ComparisonFilter { key, type, value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: string

The key to compare against the value.

type: "eq" | "ne" | "gt" | 5 more

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: string | number | boolean | Array<string | number>

The value to compare against the attribute key; supports string, number, or boolean types.

string

number

boolean

Array<string | number>

string

number

CompoundFilter { filters, type }

Combine multiple filters using `and` or `or`.

filters: Array<ComparisonFilter { key, type, value }  | unknown>

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

ComparisonFilter { key, type, value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: string

The key to compare against the value.

type: "eq" | "ne" | "gt" | 5 more

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: string | number | boolean | Array<string | number>

The value to compare against the attribute key; supports string, number, or boolean types.

string

number

boolean

Array<string | number>

string

number

unknown

type: "and" | "or"

Type of operation: `and` or `or`.

"and"

"or"

max\_num\_results?: number

The maximum number of results to return. This number should be between 1 and 50 inclusive.

ranking\_options?: RankingOptions { hybrid\_search, ranker, score\_threshold }

Ranking options for search.

hybrid\_search?: HybridSearch { embedding\_weight, text\_weight }

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

embedding\_weight: number

The weight of the embedding in the reciprocal ranking fusion.

text\_weight: number

The weight of the text in the reciprocal ranking fusion.

ranker?: "auto" | "default-2024-11-15"

The ranker to use for the file search.

"auto"

"default-2024-11-15"

score\_threshold?: number

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

BetaComputerTool { type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

type: "computer"

The type of the computer tool. Always `computer`.

BetaComputerUsePreviewTool { display\_height, display\_width, environment, type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

display\_height: number

The height of the computer display.

display\_width: number

The width of the computer display.

environment: "windows" | "mac" | "linux" | 2 more

The type of computer environment to control.

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: "computer\_use\_preview"

The type of the computer use tool. Always `computer_use_preview`.

BetaWebSearchTool { type, filters, search\_context\_size, user\_location }

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: "web\_search" | "web\_search\_2025\_08\_26"

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

"web\_search"

"web\_search\_2025\_08\_26"

filters?: Filters | null

Filters for the search.

allowed\_domains?: Array<string> | null

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

search\_context\_size?: "low" | "medium" | "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

"low"

"medium"

"high"

user\_location?: UserLocation | null

The approximate location of the user.

city?: string | null

Free text input for the city of the user, e.g. `San Francisco`.

country?: string | null

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region?: string | null

Free text input for the region of the user, e.g. `California`.

timezone?: string | null

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

type?: "approximate"

The type of location approximation. Always `approximate`.

Mcp { server\_label, type, allowed\_callers, 9 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: string

A label for this MCP server, used to identify it in tool calls.

type: "mcp"

The type of the MCP tool. Always `mcp`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

allowed\_tools?: Array<string> | McpToolFilter { read\_only, tool\_names }  | null

List of allowed tool names or a filter object.

Array<string>

McpToolFilter { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

authorization?: string

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

connector\_id?: "connector\_dropbox" | "connector\_gmail" | "connector\_googlecalendar" | 5 more

Identifier for service connectors, like those available in ChatGPT. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided. Learn more
about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

Currently supported `connector_id` values are:

* Dropbox: `connector_dropbox`
* Gmail: `connector_gmail`
* Google Calendar: `connector_googlecalendar`
* Google Drive: `connector_googledrive`
* Microsoft Teams: `connector_microsoftteams`
* Outlook Calendar: `connector_outlookcalendar`
* Outlook Email: `connector_outlookemail`
* SharePoint: `connector_sharepoint`

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading?: boolean

Whether this MCP tool is deferred and discovered via tool search.

headers?: Record<string, string> | null

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

require\_approval?: McpToolApprovalFilter { always, never }  | "always" | "never" | null

Specify which of the MCP server’s tools require approval.

McpToolApprovalFilter { always, never }

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

always?: Always { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

never?: Never { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

"always" | "never"

"always"

"never"

server\_description?: string

Optional description of the MCP server, used to provide more context.

server\_url?: string

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

tunnel\_id?: string

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

CodeInterpreter { container, type, allowed\_callers }

A tool that runs Python code to help generate a response to a prompt.

container: string | CodeInterpreterToolAuto { type, file\_ids, memory\_limit, network\_policy }

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

string

CodeInterpreterToolAuto { type, file\_ids, memory\_limit, network\_policy }

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

type: "auto"

Always `auto`.

file\_ids?: Array<string>

An optional list of uploaded files to make available to your code.

memory\_limit?: "1g" | "4g" | "16g" | "64g" | null

The memory limit for the code interpreter container.

"1g"

"4g"

"16g"

"64g"

network\_policy?: [BetaContainerNetworkPolicyDisabled](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  | [BetaContainerNetworkPolicyAllowlist](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

BetaContainerNetworkPolicyDisabled { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

BetaContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array<string>

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets?: Array<[BetaContainerNetworkPolicyDomainSecret](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } >

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

minLength1

name: string

The name of the secret to inject for the domain.

minLength1

value: string

The secret value to inject for the domain.

maxLength10485760

minLength1

type: "code\_interpreter"

The type of the code interpreter tool. Always `code_interpreter`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

ProgrammaticToolCalling { type }

type: "programmatic\_tool\_calling"

The type of the tool. Always `programmatic_tool_calling`.

ImageGeneration { type, action, background, 9 more }

A tool that generates images using the GPT image models.

type: "image\_generation"

The type of the image generation tool. Always `image_generation`.

action?: "generate" | "edit" | "auto"

Whether to generate a new image or edit an existing image. Default: `auto`.

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

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

"high"

"low"

input\_image\_mask?: InputImageMask { file\_id, image\_url }

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

file\_id?: string

File ID for the mask image.

image\_url?: string

Base64-encoded mask image.

model?: (string & {}) | "gpt-image-1" | "gpt-image-1-mini" | "gpt-image-2" | 3 more

The image generation model to use. Default: `gpt-image-1`.

(string & {})

"gpt-image-1" | "gpt-image-1-mini" | "gpt-image-2" | 3 more

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation?: "auto" | "low"

Moderation level for the generated image. Default: `auto`.

"auto"

"low"

output\_compression?: number

Compression level for the output image. Default: 100.

minimum0

maximum100

output\_format?: "png" | "webp" | "jpeg"

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

"png"

"webp"

"jpeg"

partial\_images?: number

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

quality?: "low" | "medium" | "high" | "auto"

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

"low"

"medium"

"high"

"auto"

size?: (string & {}) | "1024x1024" | "1024x1536" | "1536x1024" | "auto"

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

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

A tool that allows the model to execute shell commands.

type: "shell"

The type of the shell tool. Always `shell`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

environment?: [BetaContainerAuto](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_auto%20%3E%20(schema)) { type, file\_ids, memory\_limit, 2 more }  | [BetaLocalEnvironment](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_environment%20%3E%20(schema)) { type, skills }  | [BetaContainerReference](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_reference%20%3E%20(schema)) { container\_id, type }  | null

BetaContainerAuto { type, file\_ids, memory\_limit, 2 more }

type: "container\_auto"

Automatically creates a container for this request

file\_ids?: Array<string>

An optional list of uploaded files to make available to your code.

memory\_limit?: "1g" | "4g" | "16g" | "64g" | null

The memory limit for the container.

"1g"

"4g"

"16g"

"64g"

network\_policy?: [BetaContainerNetworkPolicyDisabled](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  | [BetaContainerNetworkPolicyAllowlist](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

BetaContainerNetworkPolicyDisabled { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

BetaContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array<string>

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets?: Array<[BetaContainerNetworkPolicyDomainSecret](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } >

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

minLength1

name: string

The name of the secret to inject for the domain.

minLength1

value: string

The secret value to inject for the domain.

maxLength10485760

minLength1

skills?: Array<[BetaSkillReference](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_skill_reference%20%3E%20(schema)) { skill\_id, type, version }  | [BetaInlineSkill](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill%20%3E%20(schema)) { description, name, source, type } >

An optional list of skills referenced by id or inline data.

BetaSkillReference { skill\_id, type, version }

skill\_id: string

The ID of the referenced skill.

maxLength64

minLength1

type: "skill\_reference"

References a skill created with the /v1/skills endpoint.

version?: string

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

BetaInlineSkill { description, name, source, type }

description: string

The description of the skill.

name: string

The name of the skill.

source: [BetaInlineSkillSource](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema)) { data, media\_type, type }

Inline skill payload

data: string

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

media\_type: "application/zip"

The media type of the inline skill payload. Must be `application/zip`.

type: "base64"

The type of the inline skill source. Must be `base64`.

type: "inline"

Defines an inline skill for this request.

BetaLocalEnvironment { type, skills }

type: "local"

Use a local computer environment.

skills?: Array<[BetaLocalSkill](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema)) { description, name, path } >

An optional list of skills.

description: string

The description of the skill.

name: string

The name of the skill.

path: string

The path to the directory containing the skill.

BetaContainerReference { container\_id, type }

container\_id: string

The ID of the referenced container.

type: "container\_reference"

References a container created with the /v1/containers endpoint

BetaCustomTool { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this tool should be deferred and discovered via tool search.

description?: string

Optional description of the custom tool, used to provide more context.

format?: Text { type }  | Grammar { definition, syntax, type }

The input format for the custom tool. Default is unconstrained text.

Text { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar { definition, syntax, type }

A grammar defined by the user.

definition: string

The grammar definition.

syntax: "lark" | "regex"

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: "grammar"

Grammar format. Always `grammar`.

BetaNamespaceTool { description, name, tools, type }

Groups function/custom tools under a shared namespace.

description: string

A description of the namespace shown to the model.

minLength1

name: string

The namespace name used in tool calls (for example, `crm`).

minLength1

tools: Array<Function { name, type, allowed\_callers, 5 more }  | [BetaCustomTool](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_custom_tool%20%3E%20(schema)) { name, type, allowed\_callers, 3 more } >

The function/custom tools available inside this namespace.

Function { name, type, allowed\_callers, 5 more }

name: string

maxLength128

minLength1

type: "function"

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this function should be deferred and discovered via tool search.

description?: string | null

output\_schema?: Record<string, unknown> | null

A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

parameters?: unknown

strict?: boolean | null

Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

BetaCustomTool { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this tool should be deferred and discovered via tool search.

description?: string

Optional description of the custom tool, used to provide more context.

format?: Text { type }  | Grammar { definition, syntax, type }

The input format for the custom tool. Default is unconstrained text.

Text { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar { definition, syntax, type }

A grammar defined by the user.

definition: string

The grammar definition.

syntax: "lark" | "regex"

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: "grammar"

Grammar format. Always `grammar`.

type: "namespace"

The type of the tool. Always `namespace`.

BetaToolSearchTool { type, description, execution, parameters }

Hosted or BYOT tool search configuration for deferred tools.

type: "tool\_search"

The type of the tool. Always `tool_search`.

description?: string | null

Description shown to the model for a client-executed tool search tool.

execution?: "server" | "client"

Whether tool search is executed by the server or by the client.

"server"

"client"

parameters?: unknown

Parameter schema for a client-executed tool search tool.

BetaWebSearchPreviewTool { type, search\_content\_types, search\_context\_size, user\_location }

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: "web\_search\_preview" | "web\_search\_preview\_2025\_03\_11"

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types?: Array<"text" | "image">

"text"

"image"

search\_context\_size?: "low" | "medium" | "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

"low"

"medium"

"high"

user\_location?: UserLocation | null

The user’s location.

type: "approximate"

The type of location approximation. Always `approximate`.

city?: string | null

Free text input for the city of the user, e.g. `San Francisco`.

country?: string | null

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region?: string | null

Free text input for the region of the user, e.g. `California`.

timezone?: string | null

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

BetaApplyPatchTool { type, allowed\_callers }

Allows the assistant to create, delete, or update files using unified diffs.

type: "apply\_patch"

The type of the tool. Always `apply_patch`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

type: "tool\_search\_output"

The type of the item. Always `tool_search_output`.

agent?: Agent { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

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

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

name: string

The name of the function to call.

parameters: Record<string, unknown> | null

A JSON schema object describing the parameters of the function.

strict: boolean | null

Whether strict parameter validation is enforced for this function tool.

type: "function"

The type of the function tool. Always `function`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this function is deferred and loaded via tool search.

description?: string | null

A description of the function. Used by the model to determine whether or not to call the function.

output\_schema?: Record<string, unknown> | null

A JSON schema object describing the JSON value encoded in string outputs for this function.

BetaFileSearchTool { type, vector\_store\_ids, filters, 2 more }

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

type: "file\_search"

The type of the file search tool. Always `file_search`.

vector\_store\_ids: Array<string>

The IDs of the vector stores to search.

filters?: ComparisonFilter { key, type, value }  | CompoundFilter { filters, type }  | null

A filter to apply.

ComparisonFilter { key, type, value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: string

The key to compare against the value.

type: "eq" | "ne" | "gt" | 5 more

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: string | number | boolean | Array<string | number>

The value to compare against the attribute key; supports string, number, or boolean types.

string

number

boolean

Array<string | number>

string

number

CompoundFilter { filters, type }

Combine multiple filters using `and` or `or`.

filters: Array<ComparisonFilter { key, type, value }  | unknown>

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

ComparisonFilter { key, type, value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: string

The key to compare against the value.

type: "eq" | "ne" | "gt" | 5 more

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: string | number | boolean | Array<string | number>

The value to compare against the attribute key; supports string, number, or boolean types.

string

number

boolean

Array<string | number>

string

number

unknown

type: "and" | "or"

Type of operation: `and` or `or`.

"and"

"or"

max\_num\_results?: number

The maximum number of results to return. This number should be between 1 and 50 inclusive.

ranking\_options?: RankingOptions { hybrid\_search, ranker, score\_threshold }

Ranking options for search.

hybrid\_search?: HybridSearch { embedding\_weight, text\_weight }

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

embedding\_weight: number

The weight of the embedding in the reciprocal ranking fusion.

text\_weight: number

The weight of the text in the reciprocal ranking fusion.

ranker?: "auto" | "default-2024-11-15"

The ranker to use for the file search.

"auto"

"default-2024-11-15"

score\_threshold?: number

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

BetaComputerTool { type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

type: "computer"

The type of the computer tool. Always `computer`.

BetaComputerUsePreviewTool { display\_height, display\_width, environment, type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

display\_height: number

The height of the computer display.

display\_width: number

The width of the computer display.

environment: "windows" | "mac" | "linux" | 2 more

The type of computer environment to control.

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: "computer\_use\_preview"

The type of the computer use tool. Always `computer_use_preview`.

BetaWebSearchTool { type, filters, search\_context\_size, user\_location }

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: "web\_search" | "web\_search\_2025\_08\_26"

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

"web\_search"

"web\_search\_2025\_08\_26"

filters?: Filters | null

Filters for the search.

allowed\_domains?: Array<string> | null

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

search\_context\_size?: "low" | "medium" | "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

"low"

"medium"

"high"

user\_location?: UserLocation | null

The approximate location of the user.

city?: string | null

Free text input for the city of the user, e.g. `San Francisco`.

country?: string | null

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region?: string | null

Free text input for the region of the user, e.g. `California`.

timezone?: string | null

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

type?: "approximate"

The type of location approximation. Always `approximate`.

Mcp { server\_label, type, allowed\_callers, 9 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: string

A label for this MCP server, used to identify it in tool calls.

type: "mcp"

The type of the MCP tool. Always `mcp`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

allowed\_tools?: Array<string> | McpToolFilter { read\_only, tool\_names }  | null

List of allowed tool names or a filter object.

Array<string>

McpToolFilter { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

authorization?: string

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

connector\_id?: "connector\_dropbox" | "connector\_gmail" | "connector\_googlecalendar" | 5 more

Identifier for service connectors, like those available in ChatGPT. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided. Learn more
about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

Currently supported `connector_id` values are:

* Dropbox: `connector_dropbox`
* Gmail: `connector_gmail`
* Google Calendar: `connector_googlecalendar`
* Google Drive: `connector_googledrive`
* Microsoft Teams: `connector_microsoftteams`
* Outlook Calendar: `connector_outlookcalendar`
* Outlook Email: `connector_outlookemail`
* SharePoint: `connector_sharepoint`

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading?: boolean

Whether this MCP tool is deferred and discovered via tool search.

headers?: Record<string, string> | null

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

require\_approval?: McpToolApprovalFilter { always, never }  | "always" | "never" | null

Specify which of the MCP server’s tools require approval.

McpToolApprovalFilter { always, never }

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

always?: Always { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

never?: Never { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

"always" | "never"

"always"

"never"

server\_description?: string

Optional description of the MCP server, used to provide more context.

server\_url?: string

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

tunnel\_id?: string

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

CodeInterpreter { container, type, allowed\_callers }

A tool that runs Python code to help generate a response to a prompt.

container: string | CodeInterpreterToolAuto { type, file\_ids, memory\_limit, network\_policy }

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

string

CodeInterpreterToolAuto { type, file\_ids, memory\_limit, network\_policy }

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

type: "auto"

Always `auto`.

file\_ids?: Array<string>

An optional list of uploaded files to make available to your code.

memory\_limit?: "1g" | "4g" | "16g" | "64g" | null

The memory limit for the code interpreter container.

"1g"

"4g"

"16g"

"64g"

network\_policy?: [BetaContainerNetworkPolicyDisabled](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  | [BetaContainerNetworkPolicyAllowlist](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

BetaContainerNetworkPolicyDisabled { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

BetaContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array<string>

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets?: Array<[BetaContainerNetworkPolicyDomainSecret](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } >

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

minLength1

name: string

The name of the secret to inject for the domain.

minLength1

value: string

The secret value to inject for the domain.

maxLength10485760

minLength1

type: "code\_interpreter"

The type of the code interpreter tool. Always `code_interpreter`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

ProgrammaticToolCalling { type }

type: "programmatic\_tool\_calling"

The type of the tool. Always `programmatic_tool_calling`.

ImageGeneration { type, action, background, 9 more }

A tool that generates images using the GPT image models.

type: "image\_generation"

The type of the image generation tool. Always `image_generation`.

action?: "generate" | "edit" | "auto"

Whether to generate a new image or edit an existing image. Default: `auto`.

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

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

"high"

"low"

input\_image\_mask?: InputImageMask { file\_id, image\_url }

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

file\_id?: string

File ID for the mask image.

image\_url?: string

Base64-encoded mask image.

model?: (string & {}) | "gpt-image-1" | "gpt-image-1-mini" | "gpt-image-2" | 3 more

The image generation model to use. Default: `gpt-image-1`.

(string & {})

"gpt-image-1" | "gpt-image-1-mini" | "gpt-image-2" | 3 more

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation?: "auto" | "low"

Moderation level for the generated image. Default: `auto`.

"auto"

"low"

output\_compression?: number

Compression level for the output image. Default: 100.

minimum0

maximum100

output\_format?: "png" | "webp" | "jpeg"

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

"png"

"webp"

"jpeg"

partial\_images?: number

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

quality?: "low" | "medium" | "high" | "auto"

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

"low"

"medium"

"high"

"auto"

size?: (string & {}) | "1024x1024" | "1024x1536" | "1536x1024" | "auto"

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

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

A tool that allows the model to execute shell commands.

type: "shell"

The type of the shell tool. Always `shell`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

environment?: [BetaContainerAuto](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_auto%20%3E%20(schema)) { type, file\_ids, memory\_limit, 2 more }  | [BetaLocalEnvironment](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_environment%20%3E%20(schema)) { type, skills }  | [BetaContainerReference](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_reference%20%3E%20(schema)) { container\_id, type }  | null

BetaContainerAuto { type, file\_ids, memory\_limit, 2 more }

type: "container\_auto"

Automatically creates a container for this request

file\_ids?: Array<string>

An optional list of uploaded files to make available to your code.

memory\_limit?: "1g" | "4g" | "16g" | "64g" | null

The memory limit for the container.

"1g"

"4g"

"16g"

"64g"

network\_policy?: [BetaContainerNetworkPolicyDisabled](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  | [BetaContainerNetworkPolicyAllowlist](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

BetaContainerNetworkPolicyDisabled { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

BetaContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array<string>

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets?: Array<[BetaContainerNetworkPolicyDomainSecret](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } >

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

minLength1

name: string

The name of the secret to inject for the domain.

minLength1

value: string

The secret value to inject for the domain.

maxLength10485760

minLength1

skills?: Array<[BetaSkillReference](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_skill_reference%20%3E%20(schema)) { skill\_id, type, version }  | [BetaInlineSkill](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill%20%3E%20(schema)) { description, name, source, type } >

An optional list of skills referenced by id or inline data.

BetaSkillReference { skill\_id, type, version }

skill\_id: string

The ID of the referenced skill.

maxLength64

minLength1

type: "skill\_reference"

References a skill created with the /v1/skills endpoint.

version?: string

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

BetaInlineSkill { description, name, source, type }

description: string

The description of the skill.

name: string

The name of the skill.

source: [BetaInlineSkillSource](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema)) { data, media\_type, type }

Inline skill payload

data: string

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

media\_type: "application/zip"

The media type of the inline skill payload. Must be `application/zip`.

type: "base64"

The type of the inline skill source. Must be `base64`.

type: "inline"

Defines an inline skill for this request.

BetaLocalEnvironment { type, skills }

type: "local"

Use a local computer environment.

skills?: Array<[BetaLocalSkill](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema)) { description, name, path } >

An optional list of skills.

description: string

The description of the skill.

name: string

The name of the skill.

path: string

The path to the directory containing the skill.

BetaContainerReference { container\_id, type }

container\_id: string

The ID of the referenced container.

type: "container\_reference"

References a container created with the /v1/containers endpoint

BetaCustomTool { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this tool should be deferred and discovered via tool search.

description?: string

Optional description of the custom tool, used to provide more context.

format?: Text { type }  | Grammar { definition, syntax, type }

The input format for the custom tool. Default is unconstrained text.

Text { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar { definition, syntax, type }

A grammar defined by the user.

definition: string

The grammar definition.

syntax: "lark" | "regex"

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: "grammar"

Grammar format. Always `grammar`.

BetaNamespaceTool { description, name, tools, type }

Groups function/custom tools under a shared namespace.

description: string

A description of the namespace shown to the model.

minLength1

name: string

The namespace name used in tool calls (for example, `crm`).

minLength1

tools: Array<Function { name, type, allowed\_callers, 5 more }  | [BetaCustomTool](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_custom_tool%20%3E%20(schema)) { name, type, allowed\_callers, 3 more } >

The function/custom tools available inside this namespace.

Function { name, type, allowed\_callers, 5 more }

name: string

maxLength128

minLength1

type: "function"

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this function should be deferred and discovered via tool search.

description?: string | null

output\_schema?: Record<string, unknown> | null

A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

parameters?: unknown

strict?: boolean | null

Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

BetaCustomTool { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this tool should be deferred and discovered via tool search.

description?: string

Optional description of the custom tool, used to provide more context.

format?: Text { type }  | Grammar { definition, syntax, type }

The input format for the custom tool. Default is unconstrained text.

Text { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar { definition, syntax, type }

A grammar defined by the user.

definition: string

The grammar definition.

syntax: "lark" | "regex"

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: "grammar"

Grammar format. Always `grammar`.

type: "namespace"

The type of the tool. Always `namespace`.

BetaToolSearchTool { type, description, execution, parameters }

Hosted or BYOT tool search configuration for deferred tools.

type: "tool\_search"

The type of the tool. Always `tool_search`.

description?: string | null

Description shown to the model for a client-executed tool search tool.

execution?: "server" | "client"

Whether tool search is executed by the server or by the client.

"server"

"client"

parameters?: unknown

Parameter schema for a client-executed tool search tool.

BetaWebSearchPreviewTool { type, search\_content\_types, search\_context\_size, user\_location }

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: "web\_search\_preview" | "web\_search\_preview\_2025\_03\_11"

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types?: Array<"text" | "image">

"text"

"image"

search\_context\_size?: "low" | "medium" | "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

"low"

"medium"

"high"

user\_location?: UserLocation | null

The user’s location.

type: "approximate"

The type of location approximation. Always `approximate`.

city?: string | null

Free text input for the city of the user, e.g. `San Francisco`.

country?: string | null

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region?: string | null

Free text input for the region of the user, e.g. `California`.

timezone?: string | null

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

BetaApplyPatchTool { type, allowed\_callers }

Allows the assistant to create, delete, or update files using unified diffs.

type: "apply\_patch"

The type of the tool. Always `apply_patch`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

type: "additional\_tools"

The type of the item. Always `additional_tools`.

agent?: Agent { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

BetaResponseCompactionItem { id, encrypted\_content, type, 2 more }

A compaction item generated by the [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).

id: string

The unique ID of the compaction item.

encrypted\_content: string

The encrypted content that was produced by compaction.

type: "compaction"

The type of the item. Always `compaction`.

agent?: Agent { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

created\_by?: string

The identifier of the actor that created the item.

ImageGenerationCall { id, result, status, 2 more }

An image generation request made by the model.

id: string

The unique ID of the image generation call.

result: string | null

The generated image encoded in base64.

status: "in\_progress" | "completed" | "generating" | "failed"

The status of the image generation call.

"in\_progress"

"completed"

"generating"

"failed"

type: "image\_generation\_call"

The type of the image generation call. Always `image_generation_call`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

BetaResponseCodeInterpreterToolCall { id, code, container\_id, 4 more }

A tool call to run code.

id: string

The unique ID of the code interpreter tool call.

code: string | null

The code to run, or null if not available.

container\_id: string

The ID of the container used to run the code.

outputs: Array<Logs { logs, type }  | Image { type, url } > | null

The outputs generated by the code interpreter, such as logs or images.
Can be null if no outputs are available.

Logs { logs, type }

The logs output from the code interpreter.

logs: string

The logs output from the code interpreter.

type: "logs"

The type of the output. Always `logs`.

Image { type, url }

The image output from the code interpreter.

type: "image"

The type of the output. Always `image`.

url: string

The URL of the image output from the code interpreter.

formaturi

status: "in\_progress" | "completed" | "incomplete" | 2 more

The status of the code interpreter tool call. Valid values are `in_progress`, `completed`, `incomplete`, `interpreting`, and `failed`.

"in\_progress"

"completed"

"incomplete"

"interpreting"

"failed"

type: "code\_interpreter\_call"

The type of the code interpreter tool call. Always `code_interpreter_call`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

LocalShellCall { id, action, call\_id, 3 more }

A tool call to run a command on the local shell.

id: string

The unique ID of the local shell call.

action: Action { command, env, type, 3 more }

Execute a shell command on the server.

command: Array<string>

The command to run.

env: Record<string, string>

Environment variables to set for the command.

type: "exec"

The type of the local shell action. Always `exec`.

timeout\_ms?: number | null

Optional timeout in milliseconds for the command.

user?: string | null

Optional user to run the command as.

working\_directory?: string | null

Optional working directory to run the command in.

call\_id: string

The unique ID of the local shell tool call generated by the model.

status: "in\_progress" | "completed" | "incomplete"

The status of the local shell call.

"in\_progress"

"completed"

"incomplete"

type: "local\_shell\_call"

The type of the local shell call. Always `local_shell_call`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

LocalShellCallOutput { id, output, type, 2 more }

The output of a local shell tool call.

id: string

The unique ID of the local shell tool call generated by the model.

output: string

A JSON string of the output of the local shell tool call.

type: "local\_shell\_call\_output"

The type of the local shell tool call output. Always `local_shell_call_output`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

status?: "in\_progress" | "completed" | "incomplete" | null

The status of the item. One of `in_progress`, `completed`, or `incomplete`.

"in\_progress"

"completed"

"incomplete"

BetaResponseFunctionShellToolCall { id, action, call\_id, 6 more }

A tool call that executes one or more shell commands in a managed environment.

id: string

The unique ID of the shell tool call. Populated when this item is returned via API.

action: Action { commands, max\_output\_length, timeout\_ms }

The shell commands and limits that describe how to run the tool call.

commands: Array<string>

max\_output\_length: number | null

Optional maximum number of characters to return from each command.

timeout\_ms: number | null

Optional timeout in milliseconds for the commands.

call\_id: string

The unique ID of the shell tool call generated by the model.

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

The status of the shell call. One of `in_progress`, `completed`, or `incomplete`.

"in\_progress"

"completed"

"incomplete"

type: "shell\_call"

The type of the item. Always `shell_call`.

agent?: Agent { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

caller?: Direct { type }  | Program { caller\_id, type }  | null

The execution context that produced this tool call.

Direct { type }

type: "direct"

Program { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

type: "program"

created\_by?: string

The ID of the entity that created this tool call.

BetaResponseFunctionShellToolCallOutput { id, call\_id, max\_output\_length, 6 more }

The output of a shell tool call that was emitted.

id: string

The unique ID of the shell call output. Populated when this item is returned via API.

call\_id: string

The unique ID of the shell tool call generated by the model.

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

Indicates that the shell commands finished and returned an exit code.

exit\_code: number

Exit code from the shell process.

type: "exit"

The outcome type. Always `exit`.

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

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

caller?: Direct { type }  | Program { caller\_id, type }  | null

The execution context that produced this tool call.

Direct { type }

type: "direct"

Program { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

type: "program"

created\_by?: string

The identifier of the actor that created the item.

BetaResponseApplyPatchToolCall { id, call\_id, operation, 5 more }

A tool call that applies file diffs by creating, deleting, or updating files.

id: string

The unique ID of the apply patch tool call. Populated when this item is returned via API.

call\_id: string

The unique ID of the apply patch tool call generated by the model.

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

The status of the apply patch tool call. One of `in_progress` or `completed`.

"in\_progress"

"completed"

type: "apply\_patch\_call"

The type of the item. Always `apply_patch_call`.

agent?: Agent { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

caller?: Direct { type }  | Program { caller\_id, type }  | null

The execution context that produced this tool call.

Direct { type }

type: "direct"

Program { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

type: "program"

created\_by?: string

The ID of the entity that created this tool call.

BetaResponseApplyPatchToolCallOutput { id, call\_id, status, 5 more }

The output emitted by an apply patch tool call.

id: string

The unique ID of the apply patch tool call output. Populated when this item is returned via API.

call\_id: string

The unique ID of the apply patch tool call generated by the model.

status: "completed" | "failed"

The status of the apply patch tool call output. One of `completed` or `failed`.

"completed"

"failed"

type: "apply\_patch\_call\_output"

The type of the item. Always `apply_patch_call_output`.

agent?: Agent { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

caller?: Direct { type }  | Program { caller\_id, type }  | null

The execution context that produced this tool call.

Direct { type }

type: "direct"

Program { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

type: "program"

created\_by?: string

The ID of the entity that created this tool call output.

output?: string | null

Optional textual output returned by the apply patch tool.

McpCall { id, arguments, name, 7 more }

An invocation of a tool on an MCP server.

id: string

The unique ID of the tool call.

arguments: string

A JSON string of the arguments passed to the tool.

name: string

The name of the tool that was run.

server\_label: string

The label of the MCP server running the tool.

type: "mcp\_call"

The type of the item. Always `mcp_call`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

approval\_request\_id?: string | null

Unique identifier for the MCP tool call approval request.
Include this value in a subsequent `mcp_approval_response` input to approve or reject the corresponding tool call.

error?: string | null

The error from the tool call, if any.

output?: string | null

The output from the tool call.

status?: "in\_progress" | "completed" | "incomplete" | 2 more

The status of the tool call. One of `in_progress`, `completed`, `incomplete`, `calling`, or `failed`.

"in\_progress"

"completed"

"incomplete"

"calling"

"failed"

McpListTools { id, server\_label, tools, 3 more }

A list of tools available on an MCP server.

id: string

The unique ID of the list.

server\_label: string

The label of the MCP server.

tools: Array<Tool>

The tools available on the server.

input\_schema: unknown

The JSON schema describing the tool’s input.

name: string

The name of the tool.

annotations?: unknown

Additional annotations about the tool.

description?: string | null

The description of the tool.

type: "mcp\_list\_tools"

The type of the item. Always `mcp_list_tools`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

error?: string | null

Error message if the server could not list tools.

McpApprovalRequest { id, arguments, name, 3 more }

A request for human approval of a tool invocation.

id: string

The unique ID of the approval request.

arguments: string

A JSON string of arguments for the tool.

name: string

The name of the tool to run.

server\_label: string

The label of the MCP server making the request.

type: "mcp\_approval\_request"

The type of the item. Always `mcp_approval_request`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

McpApprovalResponse { id, approval\_request\_id, approve, 3 more }

A response to an MCP approval request.

id: string

The unique ID of the approval response

approval\_request\_id: string

The ID of the approval request being answered.

approve: boolean

Whether the request was approved.

type: "mcp\_approval\_response"

The type of the item. Always `mcp_approval_response`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

reason?: string | null

Optional reason for the decision.

BetaResponseCustomToolCall { call\_id, input, name, 5 more }

A call to a custom tool created by the model.

call\_id: string

An identifier used to map this custom tool call to a tool call output.

input: string

The input for the custom tool call generated by the model.

name: string

The name of the custom tool being called.

type: "custom\_tool\_call"

The type of the custom tool call. Always `custom_tool_call`.

id?: string

The unique ID of the custom tool call in the OpenAI platform.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

caller?: Direct { type }  | Program { caller\_id, type }  | null

The execution context that produced this tool call.

Direct { type }

type: "direct"

Program { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

type: "program"

namespace?: string

The namespace of the custom tool being called.

BetaResponseCustomToolCallOutputItem extends [BetaResponseCustomToolCallOutput](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_custom_tool_call_output%20%3E%20(schema)) { call\_id, output, type, 3 more }  { id, status, created\_by }

The output of a custom tool call from your code, being sent back to the model.

id: string

The unique ID of the custom tool call output item.

status: "in\_progress" | "completed" | "incomplete"

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

created\_by?: string

The identifier of the actor that created the item.

parallel\_tool\_calls: boolean

Whether to allow the model to run tool calls in parallel.

temperature: number | null

What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.
We generally recommend altering this or `top_p` but not both.

minimum0

maximum2

tool\_choice: [BetaToolChoiceOptions](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool_choice_options%20%3E%20(schema)) | [BetaToolChoiceAllowed](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool_choice_allowed%20%3E%20(schema)) { mode, tools, type }  | [BetaToolChoiceTypes](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool_choice_types%20%3E%20(schema)) { type }  | 6 more

How the model should select which tool (or tools) to use when generating
a response. See the `tools` parameter to see how to specify which tools
the model can call.

BetaToolChoiceOptions = "none" | "auto" | "required"

Controls which (if any) tool is called by the model.

`none` means the model will not call any tool and instead generates a message.

`auto` means the model can pick between generating a message or calling one or
more tools.

`required` means the model must call one or more tools.

"none"

"auto"

"required"

BetaToolChoiceAllowed { mode, tools, type }

Constrains the tools available to the model to a pre-defined set.

mode: "auto" | "required"

Constrains the tools available to the model to a pre-defined set.

`auto` allows the model to pick from among the allowed tools and generate a
message.

`required` requires the model to call one or more of the allowed tools.

"auto"

"required"

tools: Array<Record<string, unknown>>

A list of tool definitions that the model should be allowed to call.

For the Responses API, the list of tool definitions might look like:

[
  { "type": "function", "name": "get_weather" },
  { "type": "mcp", "server_label": "deepwiki" },
  { "type": "image_generation" }
]

type: "allowed\_tools"

Allowed tool configuration type. Always `allowed_tools`.

BetaToolChoiceTypes { type }

Indicates that the model should use a built-in tool to generate a response.
[Learn more about built-in tools](https://platform.openai.com/docs/guides/tools).

type: "file\_search" | "web\_search\_preview" | "computer" | 5 more

The type of hosted tool the model should to use. Learn more about
[built-in tools](https://platform.openai.com/docs/guides/tools).

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

BetaToolChoiceFunction { name, type }

Use this option to force the model to call a specific function.

name: string

The name of the function to call.

type: "function"

For function calling, the type is always `function`.

BetaToolChoiceMcp { server\_label, type, name }

Use this option to force the model to call a specific tool on a remote MCP server.

server\_label: string

The label of the MCP server to use.

type: "mcp"

For MCP tools, the type is always `mcp`.

name?: string | null

The name of the tool to call on the server.

BetaToolChoiceCustom { name, type }

Use this option to force the model to call a specific custom tool.

name: string

The name of the custom tool to call.

type: "custom"

For custom tool calling, the type is always `custom`.

BetaSpecificProgrammaticToolCallingParam { type }

type: "programmatic\_tool\_calling"

The tool to call. Always `programmatic_tool_calling`.

BetaToolChoiceApplyPatch { type }

Forces the model to call the apply\_patch tool when executing a tool call.

type: "apply\_patch"

The tool to call. Always `apply_patch`.

BetaToolChoiceShell { type }

Forces the model to call the shell tool when a tool call is required.

type: "shell"

The tool to call. Always `shell`.

tools: Array<[BetaTool](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))>

An array of tools the model may call while generating a response. You
can specify which tool to use by setting the `tool_choice` parameter.

We support the following categories of tools:

* **Built-in tools**: Tools that are provided by OpenAI that extend the
  model’s capabilities, like [web search](https://platform.openai.com/docs/guides/tools-web-search)
  or [file search](https://platform.openai.com/docs/guides/tools-file-search). Learn more about
  [built-in tools](https://platform.openai.com/docs/guides/tools).
* **MCP Tools**: Integrations with third-party systems via custom MCP servers
  or predefined connectors such as Google Drive and SharePoint. Learn more about
  [MCP Tools](https://platform.openai.com/docs/guides/tools-connectors-mcp).
* **Function calls (custom tools)**: Functions that are defined by you,
  enabling the model to call your own code with strongly typed arguments
  and outputs. Learn more about
  [function calling](https://platform.openai.com/docs/guides/function-calling). You can also use
  custom tools to call your own code.

BetaFunctionTool { name, parameters, strict, 5 more }

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

name: string

The name of the function to call.

parameters: Record<string, unknown> | null

A JSON schema object describing the parameters of the function.

strict: boolean | null

Whether strict parameter validation is enforced for this function tool.

type: "function"

The type of the function tool. Always `function`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this function is deferred and loaded via tool search.

description?: string | null

A description of the function. Used by the model to determine whether or not to call the function.

output\_schema?: Record<string, unknown> | null

A JSON schema object describing the JSON value encoded in string outputs for this function.

BetaFileSearchTool { type, vector\_store\_ids, filters, 2 more }

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

type: "file\_search"

The type of the file search tool. Always `file_search`.

vector\_store\_ids: Array<string>

The IDs of the vector stores to search.

filters?: ComparisonFilter { key, type, value }  | CompoundFilter { filters, type }  | null

A filter to apply.

ComparisonFilter { key, type, value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: string

The key to compare against the value.

type: "eq" | "ne" | "gt" | 5 more

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: string | number | boolean | Array<string | number>

The value to compare against the attribute key; supports string, number, or boolean types.

string

number

boolean

Array<string | number>

string

number

CompoundFilter { filters, type }

Combine multiple filters using `and` or `or`.

filters: Array<ComparisonFilter { key, type, value }  | unknown>

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

ComparisonFilter { key, type, value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: string

The key to compare against the value.

type: "eq" | "ne" | "gt" | 5 more

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: string | number | boolean | Array<string | number>

The value to compare against the attribute key; supports string, number, or boolean types.

string

number

boolean

Array<string | number>

string

number

unknown

type: "and" | "or"

Type of operation: `and` or `or`.

"and"

"or"

max\_num\_results?: number

The maximum number of results to return. This number should be between 1 and 50 inclusive.

ranking\_options?: RankingOptions { hybrid\_search, ranker, score\_threshold }

Ranking options for search.

hybrid\_search?: HybridSearch { embedding\_weight, text\_weight }

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

embedding\_weight: number

The weight of the embedding in the reciprocal ranking fusion.

text\_weight: number

The weight of the text in the reciprocal ranking fusion.

ranker?: "auto" | "default-2024-11-15"

The ranker to use for the file search.

"auto"

"default-2024-11-15"

score\_threshold?: number

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

BetaComputerTool { type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

type: "computer"

The type of the computer tool. Always `computer`.

BetaComputerUsePreviewTool { display\_height, display\_width, environment, type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

display\_height: number

The height of the computer display.

display\_width: number

The width of the computer display.

environment: "windows" | "mac" | "linux" | 2 more

The type of computer environment to control.

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: "computer\_use\_preview"

The type of the computer use tool. Always `computer_use_preview`.

BetaWebSearchTool { type, filters, search\_context\_size, user\_location }

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: "web\_search" | "web\_search\_2025\_08\_26"

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

"web\_search"

"web\_search\_2025\_08\_26"

filters?: Filters | null

Filters for the search.

allowed\_domains?: Array<string> | null

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

search\_context\_size?: "low" | "medium" | "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

"low"

"medium"

"high"

user\_location?: UserLocation | null

The approximate location of the user.

city?: string | null

Free text input for the city of the user, e.g. `San Francisco`.

country?: string | null

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region?: string | null

Free text input for the region of the user, e.g. `California`.

timezone?: string | null

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

type?: "approximate"

The type of location approximation. Always `approximate`.

Mcp { server\_label, type, allowed\_callers, 9 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: string

A label for this MCP server, used to identify it in tool calls.

type: "mcp"

The type of the MCP tool. Always `mcp`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

allowed\_tools?: Array<string> | McpToolFilter { read\_only, tool\_names }  | null

List of allowed tool names or a filter object.

Array<string>

McpToolFilter { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

authorization?: string

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

connector\_id?: "connector\_dropbox" | "connector\_gmail" | "connector\_googlecalendar" | 5 more

Identifier for service connectors, like those available in ChatGPT. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided. Learn more
about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

Currently supported `connector_id` values are:

* Dropbox: `connector_dropbox`
* Gmail: `connector_gmail`
* Google Calendar: `connector_googlecalendar`
* Google Drive: `connector_googledrive`
* Microsoft Teams: `connector_microsoftteams`
* Outlook Calendar: `connector_outlookcalendar`
* Outlook Email: `connector_outlookemail`
* SharePoint: `connector_sharepoint`

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading?: boolean

Whether this MCP tool is deferred and discovered via tool search.

headers?: Record<string, string> | null

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

require\_approval?: McpToolApprovalFilter { always, never }  | "always" | "never" | null

Specify which of the MCP server’s tools require approval.

McpToolApprovalFilter { always, never }

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

always?: Always { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

never?: Never { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

"always" | "never"

"always"

"never"

server\_description?: string

Optional description of the MCP server, used to provide more context.

server\_url?: string

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

tunnel\_id?: string

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

CodeInterpreter { container, type, allowed\_callers }

A tool that runs Python code to help generate a response to a prompt.

container: string | CodeInterpreterToolAuto { type, file\_ids, memory\_limit, network\_policy }

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

string

CodeInterpreterToolAuto { type, file\_ids, memory\_limit, network\_policy }

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

type: "auto"

Always `auto`.

file\_ids?: Array<string>

An optional list of uploaded files to make available to your code.

memory\_limit?: "1g" | "4g" | "16g" | "64g" | null

The memory limit for the code interpreter container.

"1g"

"4g"

"16g"

"64g"

network\_policy?: [BetaContainerNetworkPolicyDisabled](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  | [BetaContainerNetworkPolicyAllowlist](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

BetaContainerNetworkPolicyDisabled { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

BetaContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array<string>

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets?: Array<[BetaContainerNetworkPolicyDomainSecret](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } >

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

minLength1

name: string

The name of the secret to inject for the domain.

minLength1

value: string

The secret value to inject for the domain.

maxLength10485760

minLength1

type: "code\_interpreter"

The type of the code interpreter tool. Always `code_interpreter`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

ProgrammaticToolCalling { type }

type: "programmatic\_tool\_calling"

The type of the tool. Always `programmatic_tool_calling`.

ImageGeneration { type, action, background, 9 more }

A tool that generates images using the GPT image models.

type: "image\_generation"

The type of the image generation tool. Always `image_generation`.

action?: "generate" | "edit" | "auto"

Whether to generate a new image or edit an existing image. Default: `auto`.

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

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

"high"

"low"

input\_image\_mask?: InputImageMask { file\_id, image\_url }

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

file\_id?: string

File ID for the mask image.

image\_url?: string

Base64-encoded mask image.

model?: (string & {}) | "gpt-image-1" | "gpt-image-1-mini" | "gpt-image-2" | 3 more

The image generation model to use. Default: `gpt-image-1`.

(string & {})

"gpt-image-1" | "gpt-image-1-mini" | "gpt-image-2" | 3 more

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation?: "auto" | "low"

Moderation level for the generated image. Default: `auto`.

"auto"

"low"

output\_compression?: number

Compression level for the output image. Default: 100.

minimum0

maximum100

output\_format?: "png" | "webp" | "jpeg"

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

"png"

"webp"

"jpeg"

partial\_images?: number

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

quality?: "low" | "medium" | "high" | "auto"

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

"low"

"medium"

"high"

"auto"

size?: (string & {}) | "1024x1024" | "1024x1536" | "1536x1024" | "auto"

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

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

A tool that allows the model to execute shell commands.

type: "shell"

The type of the shell tool. Always `shell`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

environment?: [BetaContainerAuto](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_auto%20%3E%20(schema)) { type, file\_ids, memory\_limit, 2 more }  | [BetaLocalEnvironment](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_environment%20%3E%20(schema)) { type, skills }  | [BetaContainerReference](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_reference%20%3E%20(schema)) { container\_id, type }  | null

BetaContainerAuto { type, file\_ids, memory\_limit, 2 more }

type: "container\_auto"

Automatically creates a container for this request

file\_ids?: Array<string>

An optional list of uploaded files to make available to your code.

memory\_limit?: "1g" | "4g" | "16g" | "64g" | null

The memory limit for the container.

"1g"

"4g"

"16g"

"64g"

network\_policy?: [BetaContainerNetworkPolicyDisabled](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  | [BetaContainerNetworkPolicyAllowlist](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

BetaContainerNetworkPolicyDisabled { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

BetaContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array<string>

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets?: Array<[BetaContainerNetworkPolicyDomainSecret](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } >

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

minLength1

name: string

The name of the secret to inject for the domain.

minLength1

value: string

The secret value to inject for the domain.

maxLength10485760

minLength1

skills?: Array<[BetaSkillReference](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_skill_reference%20%3E%20(schema)) { skill\_id, type, version }  | [BetaInlineSkill](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill%20%3E%20(schema)) { description, name, source, type } >

An optional list of skills referenced by id or inline data.

BetaSkillReference { skill\_id, type, version }

skill\_id: string

The ID of the referenced skill.

maxLength64

minLength1

type: "skill\_reference"

References a skill created with the /v1/skills endpoint.

version?: string

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

BetaInlineSkill { description, name, source, type }

description: string

The description of the skill.

name: string

The name of the skill.

source: [BetaInlineSkillSource](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema)) { data, media\_type, type }

Inline skill payload

data: string

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

media\_type: "application/zip"

The media type of the inline skill payload. Must be `application/zip`.

type: "base64"

The type of the inline skill source. Must be `base64`.

type: "inline"

Defines an inline skill for this request.

BetaLocalEnvironment { type, skills }

type: "local"

Use a local computer environment.

skills?: Array<[BetaLocalSkill](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema)) { description, name, path } >

An optional list of skills.

description: string

The description of the skill.

name: string

The name of the skill.

path: string

The path to the directory containing the skill.

BetaContainerReference { container\_id, type }

container\_id: string

The ID of the referenced container.

type: "container\_reference"

References a container created with the /v1/containers endpoint

BetaCustomTool { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this tool should be deferred and discovered via tool search.

description?: string

Optional description of the custom tool, used to provide more context.

format?: Text { type }  | Grammar { definition, syntax, type }

The input format for the custom tool. Default is unconstrained text.

Text { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar { definition, syntax, type }

A grammar defined by the user.

definition: string

The grammar definition.

syntax: "lark" | "regex"

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: "grammar"

Grammar format. Always `grammar`.

BetaNamespaceTool { description, name, tools, type }

Groups function/custom tools under a shared namespace.

description: string

A description of the namespace shown to the model.

minLength1

name: string

The namespace name used in tool calls (for example, `crm`).

minLength1

tools: Array<Function { name, type, allowed\_callers, 5 more }  | [BetaCustomTool](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_custom_tool%20%3E%20(schema)) { name, type, allowed\_callers, 3 more } >

The function/custom tools available inside this namespace.

Function { name, type, allowed\_callers, 5 more }

name: string

maxLength128

minLength1

type: "function"

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this function should be deferred and discovered via tool search.

description?: string | null

output\_schema?: Record<string, unknown> | null

A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

parameters?: unknown

strict?: boolean | null

Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

BetaCustomTool { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this tool should be deferred and discovered via tool search.

description?: string

Optional description of the custom tool, used to provide more context.

format?: Text { type }  | Grammar { definition, syntax, type }

The input format for the custom tool. Default is unconstrained text.

Text { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar { definition, syntax, type }

A grammar defined by the user.

definition: string

The grammar definition.

syntax: "lark" | "regex"

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: "grammar"

Grammar format. Always `grammar`.

type: "namespace"

The type of the tool. Always `namespace`.

BetaToolSearchTool { type, description, execution, parameters }

Hosted or BYOT tool search configuration for deferred tools.

type: "tool\_search"

The type of the tool. Always `tool_search`.

description?: string | null

Description shown to the model for a client-executed tool search tool.

execution?: "server" | "client"

Whether tool search is executed by the server or by the client.

"server"

"client"

parameters?: unknown

Parameter schema for a client-executed tool search tool.

BetaWebSearchPreviewTool { type, search\_content\_types, search\_context\_size, user\_location }

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: "web\_search\_preview" | "web\_search\_preview\_2025\_03\_11"

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types?: Array<"text" | "image">

"text"

"image"

search\_context\_size?: "low" | "medium" | "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

"low"

"medium"

"high"

user\_location?: UserLocation | null

The user’s location.

type: "approximate"

The type of location approximation. Always `approximate`.

city?: string | null

Free text input for the city of the user, e.g. `San Francisco`.

country?: string | null

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region?: string | null

Free text input for the region of the user, e.g. `California`.

timezone?: string | null

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

BetaApplyPatchTool { type, allowed\_callers }

Allows the assistant to create, delete, or update files using unified diffs.

type: "apply\_patch"

The type of the tool. Always `apply_patch`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

top\_p: number | null

An alternative to sampling with temperature, called nucleus sampling,
where the model considers the results of the tokens with top\_p probability
mass. So 0.1 means only the tokens comprising the top 10% probability mass
are considered.

We generally recommend altering this or `temperature` but not both.

minimum0

maximum1

background?: boolean | null

Whether to run the model response in the background.
[Learn more](https://platform.openai.com/docs/guides/background).

completed\_at?: number | null

Unix timestamp (in seconds) of when this Response was completed.
Only present when the status is `completed`.

formatunixtime

conversation?: Conversation | null

The conversation that this response belonged to. Input items and output items from this response were automatically added to this conversation.

id: string

The unique ID of the conversation that this response was associated with.

max\_output\_tokens?: number | null

An upper bound for the number of tokens that can be generated for a response, including visible output tokens and [reasoning tokens](https://platform.openai.com/docs/guides/reasoning).

max\_tool\_calls?: number | null

The maximum number of total calls to built-in tools that can be processed in a response. This maximum number applies across all built-in tool calls, not per individual tool. Any further attempts to call a tool by the model will be ignored.

moderation?: Moderation | null

Moderation results for the response input and output, if moderated completions were requested.

input: ModerationResult { categories, category\_applied\_input\_types, category\_scores, 3 more }  | Error { code, message, type }

Moderation for the response input.

ModerationResult { categories, category\_applied\_input\_types, category\_scores, 3 more }

A moderation result produced for the response input or output.

categories: Record<string, boolean>

A dictionary of moderation categories to booleans, True if the input is flagged under this category.

category\_applied\_input\_types: Record<string, Array<"text" | "image">>

Which modalities of input are reflected by the score for each category.

"text"

"image"

category\_scores: Record<string, number>

A dictionary of moderation categories to scores.

flagged: boolean

A boolean indicating whether the content was flagged by any category.

model: string

The moderation model that produced this result.

type: "moderation\_result"

The object type, which was always `moderation_result` for successful moderation results.

Error { code, message, type }

An error produced while attempting moderation for the response input or output.

code: string

The error code.

message: string

The error message.

type: "error"

The object type, which was always `error` for moderation failures.

output: ModerationResult { categories, category\_applied\_input\_types, category\_scores, 3 more }  | Error { code, message, type }

Moderation for the response output.

ModerationResult { categories, category\_applied\_input\_types, category\_scores, 3 more }

A moderation result produced for the response input or output.

categories: Record<string, boolean>

A dictionary of moderation categories to booleans, True if the input is flagged under this category.

category\_applied\_input\_types: Record<string, Array<"text" | "image">>

Which modalities of input are reflected by the score for each category.

"text"

"image"

category\_scores: Record<string, number>

A dictionary of moderation categories to scores.

flagged: boolean

A boolean indicating whether the content was flagged by any category.

model: string

The moderation model that produced this result.

type: "moderation\_result"

The object type, which was always `moderation_result` for successful moderation results.

Error { code, message, type }

An error produced while attempting moderation for the response input or output.

code: string

The error code.

message: string

The error message.

type: "error"

The object type, which was always `error` for moderation failures.

previous\_response\_id?: string | null

The unique ID of the previous response to the model. Use this to
create multi-turn conversations. Learn more about
[conversation state](https://platform.openai.com/docs/guides/conversation-state). Cannot be used in conjunction with `conversation`.

prompt?: [BetaResponsePrompt](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_prompt%20%3E%20(schema)) { id, variables, version }  | null

Reference to a prompt template and its variables.
[Learn more](https://platform.openai.com/docs/guides/text?api-mode=responses#reusable-prompts).

id: string

The unique identifier of the prompt template to use.

variables?: Record<string, string | [BetaResponseInputText](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_text%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  | [BetaResponseInputImage](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_image%20%3E%20(schema)) { detail, type, file\_id, 2 more }  | [BetaResponseInputFile](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_file%20%3E%20(schema)) { type, detail, file\_data, 4 more } > | null

Optional map of values to substitute in for variables in your
prompt. The substitution values can either be strings, or other
Response input types like images or files.

string

BetaResponseInputText { text, type, prompt\_cache\_breakpoint }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

BetaResponseInputImage { detail, type, file\_id, 2 more }

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: "low" | "high" | "auto" | "original"

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

"low"

"high"

"auto"

"original"

type: "input\_image"

The type of the input item. Always `input_image`.

file\_id?: string | null

The ID of the file to be sent to the model.

image\_url?: string | null

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

BetaResponseInputFile { type, detail, file\_data, 4 more }

A file input to the model.

type: "input\_file"

The type of the input item. Always `input_file`.

detail?: "auto" | "low" | "high"

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

"auto"

"low"

"high"

file\_data?: string

The content of the file to be sent to the model.

file\_id?: string | null

The ID of the file to be sent to the model.

file\_url?: string

The URL of the file to be sent to the model.

formaturi

filename?: string

The name of the file to be sent to the model.

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

version?: string | null

Optional version of the prompt template.

prompt\_cache\_key?: string | null

Used by OpenAI to cache responses for similar requests to optimize your cache hit rates. Replaces the `user` field. [Learn more](https://platform.openai.com/docs/guides/prompt-caching).

prompt\_cache\_options?: PromptCacheOptions { mode, ttl }

The prompt-caching options that were applied to the response. Supported for `gpt-5.6` and later models.

mode: "implicit" | "explicit"

Whether implicit prompt-cache breakpoints were enabled.

"implicit"

"explicit"

ttl: "30m"

The minimum lifetime applied to each cache breakpoint.

Deprecatedprompt\_cache\_retention?: "in\_memory" | "24h" | null

Deprecated. Use `prompt_cache_options.ttl` instead.

The retention policy for the prompt cache. Set to `24h` to enable extended prompt caching, which keeps cached prefixes active for longer, up to a maximum of 24 hours. [Learn more](https://platform.openai.com/docs/guides/prompt-caching#prompt-cache-retention).
This field expresses a maximum retention policy, while
`prompt_cache_options.ttl` expresses a minimum cache lifetime. The two
fields are independent and do not interact.
For `gpt-5.5`, `gpt-5.5-pro`, and future models, only `24h` is supported.

For older models that support both `in_memory` and `24h`, the default depends on your organization’s data retention policy:

* Organizations without ZDR enabled default to `24h`.
* Organizations with ZDR enabled default to `in_memory` when `prompt_cache_retention` is not specified.

"in\_memory"

"24h"

reasoning?: Reasoning | null

**gpt-5 and o-series models only**

Configuration options for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).

context?: "auto" | "current\_turn" | "all\_turns" | null

Controls which reasoning items are rendered back to the model on later turns.
If omitted or set to `auto`, the model determines the context mode. The
`gpt-5.6` model family defaults to `all_turns`; earlier models default to
`current_turn`.

When returned on a response, this is the effective reasoning context mode
used for the response.

"auto"

"current\_turn"

"all\_turns"

effort?: "none" | "minimal" | "low" | 4 more | null

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

Deprecatedgenerate\_summary?: "auto" | "concise" | "detailed" | null

**Deprecated:** use `summary` instead.

A summary of the reasoning performed by the model. This can be
useful for debugging and understanding the model’s reasoning process.
One of `auto`, `concise`, or `detailed`.

"auto"

"concise"

"detailed"

mode?: (string & {}) | "standard" | "pro"

Controls the reasoning execution mode for the request.

When returned on a response, this is the effective execution mode.

(string & {})

"standard" | "pro"

"standard"

"pro"

summary?: "auto" | "concise" | "detailed" | null

A summary of the reasoning performed by the model. This can be
useful for debugging and understanding the model’s reasoning process.
One of `auto`, `concise`, or `detailed`.

`concise` is supported for `computer-use-preview` models and all reasoning models after `gpt-5`.

"auto"

"concise"

"detailed"

safety\_identifier?: string | null

A stable identifier used to help detect users of your application that may be violating OpenAI’s usage policies.
The IDs should be a string that uniquely identifies each user, with a maximum length of 64 characters. We recommend hashing their username or email address, in order to avoid sending us any identifying information. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).

maxLength64

service\_tier?: "auto" | "default" | "flex" | 2 more | null

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

status?: [BetaResponseStatus](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_status%20%3E%20(schema))

The status of the response generation. One of `completed`, `failed`,
`in_progress`, `cancelled`, `queued`, or `incomplete`.

"completed"

"failed"

"in\_progress"

"cancelled"

"queued"

"incomplete"

text?: [BetaResponseTextConfig](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_text_config%20%3E%20(schema)) { format, verbosity }

Configuration options for a text response from the model. Can be plain
text or structured JSON data. Learn more:

* [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
* [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

format?: [BetaResponseFormatTextConfig](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_format_text_config%20%3E%20(schema))

An object specifying the format that the model must output.

Configuring `{ "type": "json_schema" }` enables Structured Outputs,
which ensures the model will match your supplied JSON schema. Learn more in the
[Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

The default format is `{ "type": "text" }` with no additional options.

**Not recommended for gpt-4o and newer models:**

Setting to `{ "type": "json_object" }` enables the older JSON mode, which
ensures the message the model generates is valid JSON. Using `json_schema`
is preferred for models that support it.

Text { type }

Default response format. Used to generate text responses.

type: "text"

The type of response format being defined. Always `text`.

BetaResponseFormatTextJSONSchemaConfig { name, schema, type, 2 more }

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

name: string

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

schema: Record<string, unknown>

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

type: "json\_schema"

The type of response format being defined. Always `json_schema`.

description?: string

A description of what the response format is for, used by the model to
determine how to respond in the format.

strict?: boolean | null

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

JSONObject { type }

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type: "json\_object"

The type of response format being defined. Always `json_object`.

verbosity?: "low" | "medium" | "high" | null

Constrains the verbosity of the model’s response. Lower values will result in
more concise responses, while higher values will result in more verbose responses.
Currently supported values are `low`, `medium`, and `high`. The default is
`medium`.

"low"

"medium"

"high"

top\_logprobs?: number | null

An integer between 0 and 20 specifying the maximum number of most likely
tokens to return at each token position, each with an associated log
probability. In some cases, the number of returned tokens may be fewer than
requested.

minimum0

maximum20

truncation?: "auto" | "disabled" | null

The truncation strategy to use for the model response.

* `auto`: If the input to this Response exceeds
  the model’s context window size, the model will truncate the
  response to fit the context window by dropping items from the beginning of the conversation.
* `disabled` (default): If the input size will exceed the context window
  size for a model, the request will fail with a 400 error.

"auto"

"disabled"

usage?: [BetaResponseUsage](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_usage%20%3E%20(schema)) { input\_tokens, input\_tokens\_details, output\_tokens, 2 more }

Represents token usage details including input tokens, output tokens,
a breakdown of output tokens, and the total tokens used.

input\_tokens: number

The number of input tokens.

input\_tokens\_details: InputTokensDetails { cache\_write\_tokens, cached\_tokens }

A detailed breakdown of the input tokens.

cache\_write\_tokens: number

The number of input tokens that were written to the cache.

cached\_tokens: number

The number of tokens that were retrieved from the cache.
[More on prompt caching](https://platform.openai.com/docs/guides/prompt-caching).

output\_tokens: number

The number of output tokens.

output\_tokens\_details: OutputTokensDetails { reasoning\_tokens }

A detailed breakdown of the output tokens.

reasoning\_tokens: number

The number of reasoning tokens.

total\_tokens: number

The total number of tokens used.

Deprecateduser?: string

This field is being replaced by `safety_identifier` and `prompt_cache_key`. Use `prompt_cache_key` instead to maintain caching optimizations.
A stable identifier for your end-users.
Used to boost cache hit rates by better bucketing similar requests and to help OpenAI detect and prevent abuse. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).

sequence\_number: number

The sequence number of this event.

type: "response.in\_progress"

The type of the event. Always `response.in_progress`.

agent?: Agent | null

The agent that owns this multi-agent streaming event.

agent\_name: string

The canonical name of the agent that produced this item.

BetaResponseFailedEvent { response, sequence\_number, type, agent }

An event that is emitted when a response fails.

response: [BetaResponse](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema)) { id, created\_at, error, 31 more }

The response that failed.

id: string

Unique identifier for this Response.

created\_at: number

Unix timestamp (in seconds) of when this Response was created.

formatunixtime

error: [BetaResponseError](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_error%20%3E%20(schema)) { code, message }  | null

An error object returned when the model fails to generate a Response.

code: "server\_error" | "rate\_limit\_exceeded" | "invalid\_prompt" | 17 more

The error code for the response.

"server\_error"

"rate\_limit\_exceeded"

"invalid\_prompt"

"data\_residency\_mismatch"

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

incomplete\_details: IncompleteDetails | null

Details about why the response is incomplete.

reason?: "max\_output\_tokens" | "content\_filter"

The reason why the response is incomplete.

"max\_output\_tokens"

"content\_filter"

instructions: string | Array<[BetaResponseInputItem](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_item%20%3E%20(schema))> | null

A system (or developer) message inserted into the model’s context.

When using along with `previous_response_id`, the instructions from a previous
response will not be carried over to the next response. This makes it simple
to swap out system (or developer) messages in new responses.

string

Array<[BetaResponseInputItem](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_item%20%3E%20(schema))>

BetaEasyInputMessage { content, role, phase, type }

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: string | [BetaResponseInputMessageContentList](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_message_content_list%20%3E%20(schema)) { , ,  }

Text, image, or audio input to the model, used to generate a response.
Can also contain previous assistant responses.

string

BetaResponseInputMessageContentList = Array<[BetaResponseInputContent](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_content%20%3E%20(schema))>

A list of one or many input items to the model, containing different content
types.

BetaResponseInputText { text, type, prompt\_cache\_breakpoint }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

BetaResponseInputImage { detail, type, file\_id, 2 more }

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: "low" | "high" | "auto" | "original"

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

"low"

"high"

"auto"

"original"

type: "input\_image"

The type of the input item. Always `input_image`.

file\_id?: string | null

The ID of the file to be sent to the model.

image\_url?: string | null

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

BetaResponseInputFile { type, detail, file\_data, 4 more }

A file input to the model.

type: "input\_file"

The type of the input item. Always `input_file`.

detail?: "auto" | "low" | "high"

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

"auto"

"low"

"high"

file\_data?: string

The content of the file to be sent to the model.

file\_id?: string | null

The ID of the file to be sent to the model.

file\_url?: string

The URL of the file to be sent to the model.

formaturi

filename?: string

The name of the file to be sent to the model.

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

role: "user" | "assistant" | "system" | "developer"

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

"user"

"assistant"

"system"

"developer"

phase?: "commentary" | "final\_answer" | null

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

"commentary"

"final\_answer"

type?: "message"

The type of the message input. Always `message`.

Message { content, role, agent, 2 more }

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role.

content: [BetaResponseInputMessageContentList](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_message_content_list%20%3E%20(schema)) { , ,  }

A list of one or many input items to the model, containing different content
types.

BetaResponseInputText { text, type, prompt\_cache\_breakpoint }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

BetaResponseInputImage { detail, type, file\_id, 2 more }

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: "low" | "high" | "auto" | "original"

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

"low"

"high"

"auto"

"original"

type: "input\_image"

The type of the input item. Always `input_image`.

file\_id?: string | null

The ID of the file to be sent to the model.

image\_url?: string | null

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

BetaResponseInputFile { type, detail, file\_data, 4 more }

A file input to the model.

type: "input\_file"

The type of the input item. Always `input_file`.

detail?: "auto" | "low" | "high"

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

"auto"

"low"

"high"

file\_data?: string

The content of the file to be sent to the model.

file\_id?: string | null

The ID of the file to be sent to the model.

file\_url?: string

The URL of the file to be sent to the model.

formaturi

filename?: string

The name of the file to be sent to the model.

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

role: "user" | "system" | "developer"

The role of the message input. One of `user`, `system`, or `developer`.

"user"

"system"

"developer"

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

status?: "in\_progress" | "completed" | "incomplete"

The status of item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

type?: "message"

The type of the message input. Always set to `message`.

BetaResponseOutputMessage { id, content, role, 4 more }

An output message from the model.

id: string

The unique ID of the output message.

content: Array<[BetaResponseOutputText](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_text%20%3E%20(schema)) { annotations, text, type, logprobs }  | [BetaResponseOutputRefusal](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_refusal%20%3E%20(schema)) { refusal, type } >

The content of the output message.

BetaResponseOutputText { annotations, text, type, logprobs }

A text output from the model.

annotations: Array<FileCitation { file\_id, filename, index, type }  | URLCitation { end\_index, start\_index, title, 2 more }  | ContainerFileCitation { container\_id, end\_index, file\_id, 3 more }  | FilePath { file\_id, index, type } >

The annotations of the text output.

FileCitation { file\_id, filename, index, type }

A citation to a file.

file\_id: string

The ID of the file.

filename: string

The filename of the file cited.

index: number

The index of the file in the list of files.

type: "file\_citation"

The type of the file citation. Always `file_citation`.

URLCitation { end\_index, start\_index, title, 2 more }

A citation for a web resource used to generate a model response.

end\_index: number

The index of the last character of the URL citation in the message.

start\_index: number

The index of the first character of the URL citation in the message.

title: string

The title of the web resource.

type: "url\_citation"

The type of the URL citation. Always `url_citation`.

url: string

The URL of the web resource.

formaturi

ContainerFileCitation { container\_id, end\_index, file\_id, 3 more }

A citation for a container file used to generate a model response.

container\_id: string

The ID of the container file.

end\_index: number

The index of the last character of the container file citation in the message.

file\_id: string

The ID of the file.

filename: string

The filename of the container file cited.

start\_index: number

The index of the first character of the container file citation in the message.

type: "container\_file\_citation"

The type of the container file citation. Always `container_file_citation`.

FilePath { file\_id, index, type }

A path to a file.

file\_id: string

The ID of the file.

index: number

The index of the file in the list of files.

type: "file\_path"

The type of the file path. Always `file_path`.

text: string

The text output from the model.

type: "output\_text"

The type of the output text. Always `output_text`.

logprobs?: Array<Logprob>

token: string

bytes: Array<number>

logprob: number

top\_logprobs: Array<TopLogprob>

token: string

bytes: Array<number>

logprob: number

BetaResponseOutputRefusal { refusal, type }

A refusal from the model.

refusal: string

The refusal explanation from the model.

type: "refusal"

The type of the refusal. Always `refusal`.

role: "assistant"

The role of the output message. Always `assistant`.

status: "in\_progress" | "completed" | "incomplete"

The status of the message input. One of `in_progress`, `completed`, or
`incomplete`. Populated when input items are returned via API.

"in\_progress"

"completed"

"incomplete"

type: "message"

The type of the output message. Always `message`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

phase?: "commentary" | "final\_answer" | null

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

"commentary"

"final\_answer"

BetaResponseFileSearchToolCall { id, queries, status, 3 more }

The results of a file search tool call. See the
[file search guide](https://platform.openai.com/docs/guides/tools-file-search) for more information.

id: string

The unique ID of the file search tool call.

queries: Array<string>

The queries used to search for files.

status: "in\_progress" | "searching" | "completed" | 2 more

The status of the file search tool call. One of `in_progress`,
`searching`, `incomplete` or `failed`,

"in\_progress"

"searching"

"completed"

"incomplete"

"failed"

type: "file\_search\_call"

The type of the file search tool call. Always `file_search_call`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

results?: Array<Result> | null

The results of the file search tool call.

attributes?: Record<string, string | number | boolean> | null

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.

string

number

boolean

file\_id?: string

The unique ID of the file.

filename?: string

The name of the file.

score?: number

The relevance score of the file - a value between 0 and 1.

formatfloat

text?: string

The text that was retrieved from the file.

BetaResponseComputerToolCall { id, call\_id, pending\_safety\_checks, 5 more }

A tool call to a computer use tool. See the
[computer use guide](https://platform.openai.com/docs/guides/tools-computer-use) for more information.

id: string

The unique ID of the computer call.

call\_id: string

An identifier used when responding to the tool call with output.

pending\_safety\_checks: Array<PendingSafetyCheck>

The pending safety checks for the computer call.

id: string

The ID of the pending safety check.

code?: string | null

The type of the pending safety check.

message?: string | null

Details about the pending safety check.

status: "in\_progress" | "completed" | "incomplete"

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

type: "computer\_call"

The type of the computer call. Always `computer_call`.

action?: [BetaComputerAction](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_computer_action%20%3E%20(schema))

A click action.

Click { button, type, x, 2 more }

A click action.

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

[
  { x: 100, y: 200 },
  { x: 200, y: 300 }
]

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

Flattened batched actions for `computer_use`. Each action includes an
`type` discriminator and action-specific fields.

Click { button, type, x, 2 more }

A click action.

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

[
  { x: 100, y: 200 },
  { x: 200, y: 300 }
]

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

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

ComputerCallOutput { call\_id, output, type, 4 more }

The output of a computer tool call.

call\_id: string

The ID of the computer tool call that produced the output.

maxLength64

minLength1

output: [BetaResponseComputerToolCallOutputScreenshot](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_computer_tool_call_output_screenshot%20%3E%20(schema)) { type, file\_id, image\_url }

A computer screenshot image used with the computer use tool.

type: "computer\_screenshot"

Specifies the event type. For a computer screenshot, this property is
always set to `computer_screenshot`.

file\_id?: string

The identifier of an uploaded file that contains the screenshot.

image\_url?: string

The URL of the screenshot image.

formaturi

type: "computer\_call\_output"

The type of the computer tool call output. Always `computer_call_output`.

id?: string | null

The ID of the computer tool call output.

acknowledged\_safety\_checks?: Array<AcknowledgedSafetyCheck> | null

The safety checks reported by the API that have been acknowledged by the developer.

id: string

The ID of the pending safety check.

code?: string | null

The type of the pending safety check.

message?: string | null

Details about the pending safety check.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

status?: "in\_progress" | "completed" | "incomplete" | null

The status of the message input. One of `in_progress`, `completed`, or `incomplete`. Populated when input items are returned via API.

"in\_progress"

"completed"

"incomplete"

BetaResponseFunctionWebSearch { id, action, status, 2 more }

The results of a web search tool call. See the
[web search guide](https://platform.openai.com/docs/guides/tools-web-search) for more information.

id: string

The unique ID of the web search tool call.

action: Search { type, queries, query, sources }  | OpenPage { type, url }  | FindInPage { pattern, type, url }

An object describing the specific action taken in this web search call.
Includes details on how the model used the web (search, open\_page, find\_in\_page).

Search { type, queries, query, sources }

Action type “search” - Performs a web search query.

type: "search"

The action type.

queries?: Array<string>

The search queries.

Deprecatedquery?: string

The search query.

sources?: Array<Source>

The sources used in the search.

type: "url"

The type of source. Always `url`.

url: string

The URL of the source.

formaturi

OpenPage { type, url }

Action type “open\_page” - Opens a specific URL from search results.

type: "open\_page"

The action type.

url?: string | null

The URL opened by the model.

formaturi

FindInPage { pattern, type, url }

Action type “find\_in\_page”: Searches for a pattern within a loaded page.

pattern: string

The pattern or text to search for within the page.

type: "find\_in\_page"

The action type.

url: string

The URL of the page searched for the pattern.

formaturi

status: "in\_progress" | "searching" | "completed" | "failed"

The status of the web search tool call.

"in\_progress"

"searching"

"completed"

"failed"

type: "web\_search\_call"

The type of the web search tool call. Always `web_search_call`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

BetaResponseFunctionToolCall { arguments, call\_id, name, 6 more }

A tool call to run a function. See the
[function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.

arguments: string

A JSON string of the arguments to pass to the function.

call\_id: string

The unique ID of the function tool call generated by the model.

name: string

The name of the function to run.

type: "function\_call"

The type of the function tool call. Always `function_call`.

id?: string

The unique ID of the function tool call.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

caller?: Direct { type }  | Program { caller\_id, type }  | null

The execution context that produced this tool call.

Direct { type }

type: "direct"

Program { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

type: "program"

namespace?: string

The namespace of the function to run.

status?: "in\_progress" | "completed" | "incomplete"

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

FunctionCallOutput { call\_id, output, type, 4 more }

The output of a function tool call.

call\_id: string

The unique ID of the function tool call generated by the model.

maxLength64

minLength1

output: string | [BetaResponseFunctionCallOutputItemList](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_call_output_item_list%20%3E%20(schema)) { , ,  }

Text, image, or file output of the function tool call.

string

BetaResponseFunctionCallOutputItemList = Array<[BetaResponseFunctionCallOutputItem](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_call_output_item%20%3E%20(schema))>

An array of content outputs (text, image, file) for the function tool call.

BetaResponseInputTextContent { text, type, prompt\_cache\_breakpoint }

A text input to the model.

text: string

The text input to the model.

maxLength10485760

type: "input\_text"

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint?: PromptCacheBreakpoint | null

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

BetaResponseInputImageContent { type, detail, file\_id, 2 more }

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision)

type: "input\_image"

The type of the input item. Always `input_image`.

detail?: "low" | "high" | "auto" | "original" | null

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

"low"

"high"

"auto"

"original"

file\_id?: string | null

The ID of the file to be sent to the model.

image\_url?: string | null

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

maxLength20971520

formaturi

prompt\_cache\_breakpoint?: PromptCacheBreakpoint | null

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

BetaResponseInputFileContent { type, detail, file\_data, 4 more }

A file input to the model.

type: "input\_file"

The type of the input item. Always `input_file`.

detail?: "auto" | "low" | "high"

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

"auto"

"low"

"high"

file\_data?: string | null

The base64-encoded data of the file to be sent to the model.

maxLength73400320

file\_id?: string | null

The ID of the file to be sent to the model.

file\_url?: string | null

The URL of the file to be sent to the model.

formaturi

filename?: string | null

The name of the file to be sent to the model.

prompt\_cache\_breakpoint?: PromptCacheBreakpoint | null

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

type: "function\_call\_output"

The type of the function tool call output. Always `function_call_output`.

id?: string | null

The unique ID of the function tool call output. Populated when this item is returned via API.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

caller?: Direct { type }  | Program { caller\_id, type }  | null

The execution context that produced this tool call.

Direct { type }

type: "direct"

The caller type. Always `direct`.

Program { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

maxLength64

minLength1

type: "program"

The caller type. Always `program`.

status?: "in\_progress" | "completed" | "incomplete" | null

The status of the item. One of `in_progress`, `completed`, or `incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

AgentMessage { author, content, recipient, 3 more }

A message routed between agents.

author: string

The sending agent identity.

content: Array<[BetaResponseInputTextContent](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_text_content%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  | [BetaResponseInputImageContent](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_image_content%20%3E%20(schema)) { type, detail, file\_id, 2 more }  | EncryptedContent { encrypted\_content, type } >

Plaintext, image, or encrypted content sent between agents.

BetaResponseInputTextContent { text, type, prompt\_cache\_breakpoint }

A text input to the model.

text: string

The text input to the model.

maxLength10485760

type: "input\_text"

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint?: PromptCacheBreakpoint | null

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

BetaResponseInputImageContent { type, detail, file\_id, 2 more }

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision)

type: "input\_image"

The type of the input item. Always `input_image`.

detail?: "low" | "high" | "auto" | "original" | null

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

"low"

"high"

"auto"

"original"

file\_id?: string | null

The ID of the file to be sent to the model.

image\_url?: string | null

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

maxLength20971520

formaturi

prompt\_cache\_breakpoint?: PromptCacheBreakpoint | null

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

EncryptedContent { encrypted\_content, type }

Opaque encrypted content that Responses API decrypts inside trusted model execution.

encrypted\_content: string

Opaque encrypted content.

maxLength10485760

type: "encrypted\_content"

The type of the input item. Always `encrypted_content`.

recipient: string

The destination agent identity.

type: "agent\_message"

The item type. Always `agent_message`.

id?: string | null

The unique ID of this agent message item.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

MultiAgentCall { action, arguments, call\_id, 3 more }

action: "spawn\_agent" | "interrupt\_agent" | "list\_agents" | 3 more

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

The unique ID linking this call to its output.

maxLength64

minLength1

type: "multi\_agent\_call"

The item type. Always `multi_agent_call`.

id?: string | null

The unique ID of this multi-agent call.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

MultiAgentCallOutput { action, call\_id, output, 3 more }

action: "spawn\_agent" | "interrupt\_agent" | "list\_agents" | 3 more

The multi-agent action that produced this result.

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

call\_id: string

The unique ID of the multi-agent call.

maxLength64

minLength1

output: Array<Output>

Text output returned by the multi-agent action.

text: string

The text content.

maxLength10485760

type: "output\_text"

The content type. Always `output_text`.

annotations?: Array<FileCitation { file\_id, filename, index, type }  | URLCitation { end\_index, start\_index, title, 2 more }  | ContainerFileCitation { container\_id, end\_index, file\_id, 3 more } >

Citations associated with the text content.

FileCitation { file\_id, filename, index, type }

file\_id: string

The ID of the file.

filename: string

The filename of the file cited.

index: number

The index of the file in the list of files.

minimum0

type: "file\_citation"

The citation type. Always `file_citation`.

URLCitation { end\_index, start\_index, title, 2 more }

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

formaturi

ContainerFileCitation { container\_id, end\_index, file\_id, 3 more }

container\_id: string

The ID of the container.

end\_index: number

The index of the last character of the citation in the message.

minimum0

file\_id: string

The ID of the container file.

filename: string

The filename of the container file cited.

start\_index: number

The index of the first character of the citation in the message.

minimum0

type: "container\_file\_citation"

The citation type. Always `container_file_citation`.

type: "multi\_agent\_call\_output"

The item type. Always `multi_agent_call_output`.

id?: string | null

The unique ID of this multi-agent call output.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

ToolSearchCall { arguments, type, id, 4 more }

arguments: unknown

The arguments supplied to the tool search call.

type: "tool\_search\_call"

The item type. Always `tool_search_call`.

id?: string | null

The unique ID of this tool search call.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

call\_id?: string | null

The unique ID of the tool search call generated by the model.

maxLength64

minLength1

execution?: "server" | "client"

Whether tool search was executed by the server or by the client.

"server"

"client"

status?: "in\_progress" | "completed" | "incomplete" | null

The status of the tool search call.

"in\_progress"

"completed"

"incomplete"

BetaResponseToolSearchOutputItemParam { tools, type, id, 4 more }

tools: Array<[BetaTool](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))>

The loaded tool definitions returned by the tool search output.

BetaFunctionTool { name, parameters, strict, 5 more }

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

name: string

The name of the function to call.

parameters: Record<string, unknown> | null

A JSON schema object describing the parameters of the function.

strict: boolean | null

Whether strict parameter validation is enforced for this function tool.

type: "function"

The type of the function tool. Always `function`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this function is deferred and loaded via tool search.

description?: string | null

A description of the function. Used by the model to determine whether or not to call the function.

output\_schema?: Record<string, unknown> | null

A JSON schema object describing the JSON value encoded in string outputs for this function.

BetaFileSearchTool { type, vector\_store\_ids, filters, 2 more }

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

type: "file\_search"

The type of the file search tool. Always `file_search`.

vector\_store\_ids: Array<string>

The IDs of the vector stores to search.

filters?: ComparisonFilter { key, type, value }  | CompoundFilter { filters, type }  | null

A filter to apply.

ComparisonFilter { key, type, value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: string

The key to compare against the value.

type: "eq" | "ne" | "gt" | 5 more

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: string | number | boolean | Array<string | number>

The value to compare against the attribute key; supports string, number, or boolean types.

string

number

boolean

Array<string | number>

string

number

CompoundFilter { filters, type }

Combine multiple filters using `and` or `or`.

filters: Array<ComparisonFilter { key, type, value }  | unknown>

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

ComparisonFilter { key, type, value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: string

The key to compare against the value.

type: "eq" | "ne" | "gt" | 5 more

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: string | number | boolean | Array<string | number>

The value to compare against the attribute key; supports string, number, or boolean types.

string

number

boolean

Array<string | number>

string

number

unknown

type: "and" | "or"

Type of operation: `and` or `or`.

"and"

"or"

max\_num\_results?: number

The maximum number of results to return. This number should be between 1 and 50 inclusive.

ranking\_options?: RankingOptions { hybrid\_search, ranker, score\_threshold }

Ranking options for search.

hybrid\_search?: HybridSearch { embedding\_weight, text\_weight }

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

embedding\_weight: number

The weight of the embedding in the reciprocal ranking fusion.

text\_weight: number

The weight of the text in the reciprocal ranking fusion.

ranker?: "auto" | "default-2024-11-15"

The ranker to use for the file search.

"auto"

"default-2024-11-15"

score\_threshold?: number

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

BetaComputerTool { type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

type: "computer"

The type of the computer tool. Always `computer`.

BetaComputerUsePreviewTool { display\_height, display\_width, environment, type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

display\_height: number

The height of the computer display.

display\_width: number

The width of the computer display.

environment: "windows" | "mac" | "linux" | 2 more

The type of computer environment to control.

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: "computer\_use\_preview"

The type of the computer use tool. Always `computer_use_preview`.

BetaWebSearchTool { type, filters, search\_context\_size, user\_location }

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: "web\_search" | "web\_search\_2025\_08\_26"

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

"web\_search"

"web\_search\_2025\_08\_26"

filters?: Filters | null

Filters for the search.

allowed\_domains?: Array<string> | null

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

search\_context\_size?: "low" | "medium" | "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

"low"

"medium"

"high"

user\_location?: UserLocation | null

The approximate location of the user.

city?: string | null

Free text input for the city of the user, e.g. `San Francisco`.

country?: string | null

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region?: string | null

Free text input for the region of the user, e.g. `California`.

timezone?: string | null

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

type?: "approximate"

The type of location approximation. Always `approximate`.

Mcp { server\_label, type, allowed\_callers, 9 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: string

A label for this MCP server, used to identify it in tool calls.

type: "mcp"

The type of the MCP tool. Always `mcp`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

allowed\_tools?: Array<string> | McpToolFilter { read\_only, tool\_names }  | null

List of allowed tool names or a filter object.

Array<string>

McpToolFilter { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

authorization?: string

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

connector\_id?: "connector\_dropbox" | "connector\_gmail" | "connector\_googlecalendar" | 5 more

Identifier for service connectors, like those available in ChatGPT. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided. Learn more
about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

Currently supported `connector_id` values are:

* Dropbox: `connector_dropbox`
* Gmail: `connector_gmail`
* Google Calendar: `connector_googlecalendar`
* Google Drive: `connector_googledrive`
* Microsoft Teams: `connector_microsoftteams`
* Outlook Calendar: `connector_outlookcalendar`
* Outlook Email: `connector_outlookemail`
* SharePoint: `connector_sharepoint`

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading?: boolean

Whether this MCP tool is deferred and discovered via tool search.

headers?: Record<string, string> | null

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

require\_approval?: McpToolApprovalFilter { always, never }  | "always" | "never" | null

Specify which of the MCP server’s tools require approval.

McpToolApprovalFilter { always, never }

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

always?: Always { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

never?: Never { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

"always" | "never"

"always"

"never"

server\_description?: string

Optional description of the MCP server, used to provide more context.

server\_url?: string

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

tunnel\_id?: string

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

CodeInterpreter { container, type, allowed\_callers }

A tool that runs Python code to help generate a response to a prompt.

container: string | CodeInterpreterToolAuto { type, file\_ids, memory\_limit, network\_policy }

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

string

CodeInterpreterToolAuto { type, file\_ids, memory\_limit, network\_policy }

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

type: "auto"

Always `auto`.

file\_ids?: Array<string>

An optional list of uploaded files to make available to your code.

memory\_limit?: "1g" | "4g" | "16g" | "64g" | null

The memory limit for the code interpreter container.

"1g"

"4g"

"16g"

"64g"

network\_policy?: [BetaContainerNetworkPolicyDisabled](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  | [BetaContainerNetworkPolicyAllowlist](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

BetaContainerNetworkPolicyDisabled { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

BetaContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array<string>

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets?: Array<[BetaContainerNetworkPolicyDomainSecret](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } >

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

minLength1

name: string

The name of the secret to inject for the domain.

minLength1

value: string

The secret value to inject for the domain.

maxLength10485760

minLength1

type: "code\_interpreter"

The type of the code interpreter tool. Always `code_interpreter`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

ProgrammaticToolCalling { type }

type: "programmatic\_tool\_calling"

The type of the tool. Always `programmatic_tool_calling`.

ImageGeneration { type, action, background, 9 more }

A tool that generates images using the GPT image models.

type: "image\_generation"

The type of the image generation tool. Always `image_generation`.

action?: "generate" | "edit" | "auto"

Whether to generate a new image or edit an existing image. Default: `auto`.

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

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

"high"

"low"

input\_image\_mask?: InputImageMask { file\_id, image\_url }

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

file\_id?: string

File ID for the mask image.

image\_url?: string

Base64-encoded mask image.

model?: (string & {}) | "gpt-image-1" | "gpt-image-1-mini" | "gpt-image-2" | 3 more

The image generation model to use. Default: `gpt-image-1`.

(string & {})

"gpt-image-1" | "gpt-image-1-mini" | "gpt-image-2" | 3 more

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation?: "auto" | "low"

Moderation level for the generated image. Default: `auto`.

"auto"

"low"

output\_compression?: number

Compression level for the output image. Default: 100.

minimum0

maximum100

output\_format?: "png" | "webp" | "jpeg"

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

"png"

"webp"

"jpeg"

partial\_images?: number

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

quality?: "low" | "medium" | "high" | "auto"

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

"low"

"medium"

"high"

"auto"

size?: (string & {}) | "1024x1024" | "1024x1536" | "1536x1024" | "auto"

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

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

A tool that allows the model to execute shell commands.

type: "shell"

The type of the shell tool. Always `shell`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

environment?: [BetaContainerAuto](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_auto%20%3E%20(schema)) { type, file\_ids, memory\_limit, 2 more }  | [BetaLocalEnvironment](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_environment%20%3E%20(schema)) { type, skills }  | [BetaContainerReference](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_reference%20%3E%20(schema)) { container\_id, type }  | null

BetaContainerAuto { type, file\_ids, memory\_limit, 2 more }

type: "container\_auto"

Automatically creates a container for this request

file\_ids?: Array<string>

An optional list of uploaded files to make available to your code.

memory\_limit?: "1g" | "4g" | "16g" | "64g" | null

The memory limit for the container.

"1g"

"4g"

"16g"

"64g"

network\_policy?: [BetaContainerNetworkPolicyDisabled](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  | [BetaContainerNetworkPolicyAllowlist](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

BetaContainerNetworkPolicyDisabled { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

BetaContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array<string>

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets?: Array<[BetaContainerNetworkPolicyDomainSecret](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } >

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

minLength1

name: string

The name of the secret to inject for the domain.

minLength1

value: string

The secret value to inject for the domain.

maxLength10485760

minLength1

skills?: Array<[BetaSkillReference](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_skill_reference%20%3E%20(schema)) { skill\_id, type, version }  | [BetaInlineSkill](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill%20%3E%20(schema)) { description, name, source, type } >

An optional list of skills referenced by id or inline data.

BetaSkillReference { skill\_id, type, version }

skill\_id: string

The ID of the referenced skill.

maxLength64

minLength1

type: "skill\_reference"

References a skill created with the /v1/skills endpoint.

version?: string

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

BetaInlineSkill { description, name, source, type }

description: string

The description of the skill.

name: string

The name of the skill.

source: [BetaInlineSkillSource](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema)) { data, media\_type, type }

Inline skill payload

data: string

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

media\_type: "application/zip"

The media type of the inline skill payload. Must be `application/zip`.

type: "base64"

The type of the inline skill source. Must be `base64`.

type: "inline"

Defines an inline skill for this request.

BetaLocalEnvironment { type, skills }

type: "local"

Use a local computer environment.

skills?: Array<[BetaLocalSkill](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema)) { description, name, path } >

An optional list of skills.

description: string

The description of the skill.

name: string

The name of the skill.

path: string

The path to the directory containing the skill.

BetaContainerReference { container\_id, type }

container\_id: string

The ID of the referenced container.

type: "container\_reference"

References a container created with the /v1/containers endpoint

BetaCustomTool { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this tool should be deferred and discovered via tool search.

description?: string

Optional description of the custom tool, used to provide more context.

format?: Text { type }  | Grammar { definition, syntax, type }

The input format for the custom tool. Default is unconstrained text.

Text { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar { definition, syntax, type }

A grammar defined by the user.

definition: string

The grammar definition.

syntax: "lark" | "regex"

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: "grammar"

Grammar format. Always `grammar`.

BetaNamespaceTool { description, name, tools, type }

Groups function/custom tools under a shared namespace.

description: string

A description of the namespace shown to the model.

minLength1

name: string

The namespace name used in tool calls (for example, `crm`).

minLength1

tools: Array<Function { name, type, allowed\_callers, 5 more }  | [BetaCustomTool](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_custom_tool%20%3E%20(schema)) { name, type, allowed\_callers, 3 more } >

The function/custom tools available inside this namespace.

Function { name, type, allowed\_callers, 5 more }

name: string

maxLength128

minLength1

type: "function"

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this function should be deferred and discovered via tool search.

description?: string | null

output\_schema?: Record<string, unknown> | null

A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

parameters?: unknown

strict?: boolean | null

Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

BetaCustomTool { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this tool should be deferred and discovered via tool search.

description?: string

Optional description of the custom tool, used to provide more context.

format?: Text { type }  | Grammar { definition, syntax, type }

The input format for the custom tool. Default is unconstrained text.

Text { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar { definition, syntax, type }

A grammar defined by the user.

definition: string

The grammar definition.

syntax: "lark" | "regex"

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: "grammar"

Grammar format. Always `grammar`.

type: "namespace"

The type of the tool. Always `namespace`.

BetaToolSearchTool { type, description, execution, parameters }

Hosted or BYOT tool search configuration for deferred tools.

type: "tool\_search"

The type of the tool. Always `tool_search`.

description?: string | null

Description shown to the model for a client-executed tool search tool.

execution?: "server" | "client"

Whether tool search is executed by the server or by the client.

"server"

"client"

parameters?: unknown

Parameter schema for a client-executed tool search tool.

BetaWebSearchPreviewTool { type, search\_content\_types, search\_context\_size, user\_location }

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: "web\_search\_preview" | "web\_search\_preview\_2025\_03\_11"

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types?: Array<"text" | "image">

"text"

"image"

search\_context\_size?: "low" | "medium" | "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

"low"

"medium"

"high"

user\_location?: UserLocation | null

The user’s location.

type: "approximate"

The type of location approximation. Always `approximate`.

city?: string | null

Free text input for the city of the user, e.g. `San Francisco`.

country?: string | null

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region?: string | null

Free text input for the region of the user, e.g. `California`.

timezone?: string | null

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

BetaApplyPatchTool { type, allowed\_callers }

Allows the assistant to create, delete, or update files using unified diffs.

type: "apply\_patch"

The type of the tool. Always `apply_patch`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

type: "tool\_search\_output"

The item type. Always `tool_search_output`.

id?: string | null

The unique ID of this tool search output.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

call\_id?: string | null

The unique ID of the tool search call generated by the model.

maxLength64

minLength1

execution?: "server" | "client"

Whether tool search was executed by the server or by the client.

"server"

"client"

status?: "in\_progress" | "completed" | "incomplete" | null

The status of the tool search output.

"in\_progress"

"completed"

"incomplete"

AdditionalTools { role, tools, type, 2 more }

role: "developer"

The role that provided the additional tools. Only `developer` is supported.

tools: Array<[BetaTool](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))>

A list of additional tools made available at this item.

BetaFunctionTool { name, parameters, strict, 5 more }

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

name: string

The name of the function to call.

parameters: Record<string, unknown> | null

A JSON schema object describing the parameters of the function.

strict: boolean | null

Whether strict parameter validation is enforced for this function tool.

type: "function"

The type of the function tool. Always `function`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this function is deferred and loaded via tool search.

description?: string | null

A description of the function. Used by the model to determine whether or not to call the function.

output\_schema?: Record<string, unknown> | null

A JSON schema object describing the JSON value encoded in string outputs for this function.

BetaFileSearchTool { type, vector\_store\_ids, filters, 2 more }

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

type: "file\_search"

The type of the file search tool. Always `file_search`.

vector\_store\_ids: Array<string>

The IDs of the vector stores to search.

filters?: ComparisonFilter { key, type, value }  | CompoundFilter { filters, type }  | null

A filter to apply.

ComparisonFilter { key, type, value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: string

The key to compare against the value.

type: "eq" | "ne" | "gt" | 5 more

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: string | number | boolean | Array<string | number>

The value to compare against the attribute key; supports string, number, or boolean types.

string

number

boolean

Array<string | number>

string

number

CompoundFilter { filters, type }

Combine multiple filters using `and` or `or`.

filters: Array<ComparisonFilter { key, type, value }  | unknown>

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

ComparisonFilter { key, type, value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: string

The key to compare against the value.

type: "eq" | "ne" | "gt" | 5 more

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: string | number | boolean | Array<string | number>

The value to compare against the attribute key; supports string, number, or boolean types.

string

number

boolean

Array<string | number>

string

number

unknown

type: "and" | "or"

Type of operation: `and` or `or`.

"and"

"or"

max\_num\_results?: number

The maximum number of results to return. This number should be between 1 and 50 inclusive.

ranking\_options?: RankingOptions { hybrid\_search, ranker, score\_threshold }

Ranking options for search.

hybrid\_search?: HybridSearch { embedding\_weight, text\_weight }

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

embedding\_weight: number

The weight of the embedding in the reciprocal ranking fusion.

text\_weight: number

The weight of the text in the reciprocal ranking fusion.

ranker?: "auto" | "default-2024-11-15"

The ranker to use for the file search.

"auto"

"default-2024-11-15"

score\_threshold?: number

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

BetaComputerTool { type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

type: "computer"

The type of the computer tool. Always `computer`.

BetaComputerUsePreviewTool { display\_height, display\_width, environment, type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

display\_height: number

The height of the computer display.

display\_width: number

The width of the computer display.

environment: "windows" | "mac" | "linux" | 2 more

The type of computer environment to control.

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: "computer\_use\_preview"

The type of the computer use tool. Always `computer_use_preview`.

BetaWebSearchTool { type, filters, search\_context\_size, user\_location }

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: "web\_search" | "web\_search\_2025\_08\_26"

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

"web\_search"

"web\_search\_2025\_08\_26"

filters?: Filters | null

Filters for the search.

allowed\_domains?: Array<string> | null

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

search\_context\_size?: "low" | "medium" | "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

"low"

"medium"

"high"

user\_location?: UserLocation | null

The approximate location of the user.

city?: string | null

Free text input for the city of the user, e.g. `San Francisco`.

country?: string | null

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region?: string | null

Free text input for the region of the user, e.g. `California`.

timezone?: string | null

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

type?: "approximate"

The type of location approximation. Always `approximate`.

Mcp { server\_label, type, allowed\_callers, 9 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: string

A label for this MCP server, used to identify it in tool calls.

type: "mcp"

The type of the MCP tool. Always `mcp`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

allowed\_tools?: Array<string> | McpToolFilter { read\_only, tool\_names }  | null

List of allowed tool names or a filter object.

Array<string>

McpToolFilter { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

authorization?: string

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

connector\_id?: "connector\_dropbox" | "connector\_gmail" | "connector\_googlecalendar" | 5 more

Identifier for service connectors, like those available in ChatGPT. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided. Learn more
about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

Currently supported `connector_id` values are:

* Dropbox: `connector_dropbox`
* Gmail: `connector_gmail`
* Google Calendar: `connector_googlecalendar`
* Google Drive: `connector_googledrive`
* Microsoft Teams: `connector_microsoftteams`
* Outlook Calendar: `connector_outlookcalendar`
* Outlook Email: `connector_outlookemail`
* SharePoint: `connector_sharepoint`

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading?: boolean

Whether this MCP tool is deferred and discovered via tool search.

headers?: Record<string, string> | null

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

require\_approval?: McpToolApprovalFilter { always, never }  | "always" | "never" | null

Specify which of the MCP server’s tools require approval.

McpToolApprovalFilter { always, never }

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

always?: Always { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

never?: Never { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

"always" | "never"

"always"

"never"

server\_description?: string

Optional description of the MCP server, used to provide more context.

server\_url?: string

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

tunnel\_id?: string

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

CodeInterpreter { container, type, allowed\_callers }

A tool that runs Python code to help generate a response to a prompt.

container: string | CodeInterpreterToolAuto { type, file\_ids, memory\_limit, network\_policy }

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

string

CodeInterpreterToolAuto { type, file\_ids, memory\_limit, network\_policy }

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

type: "auto"

Always `auto`.

file\_ids?: Array<string>

An optional list of uploaded files to make available to your code.

memory\_limit?: "1g" | "4g" | "16g" | "64g" | null

The memory limit for the code interpreter container.

"1g"

"4g"

"16g"

"64g"

network\_policy?: [BetaContainerNetworkPolicyDisabled](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  | [BetaContainerNetworkPolicyAllowlist](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

BetaContainerNetworkPolicyDisabled { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

BetaContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array<string>

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets?: Array<[BetaContainerNetworkPolicyDomainSecret](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } >

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

minLength1

name: string

The name of the secret to inject for the domain.

minLength1

value: string

The secret value to inject for the domain.

maxLength10485760

minLength1

type: "code\_interpreter"

The type of the code interpreter tool. Always `code_interpreter`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

ProgrammaticToolCalling { type }

type: "programmatic\_tool\_calling"

The type of the tool. Always `programmatic_tool_calling`.

ImageGeneration { type, action, background, 9 more }

A tool that generates images using the GPT image models.

type: "image\_generation"

The type of the image generation tool. Always `image_generation`.

action?: "generate" | "edit" | "auto"

Whether to generate a new image or edit an existing image. Default: `auto`.

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

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

"high"

"low"

input\_image\_mask?: InputImageMask { file\_id, image\_url }

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

file\_id?: string

File ID for the mask image.

image\_url?: string

Base64-encoded mask image.

model?: (string & {}) | "gpt-image-1" | "gpt-image-1-mini" | "gpt-image-2" | 3 more

The image generation model to use. Default: `gpt-image-1`.

(string & {})

"gpt-image-1" | "gpt-image-1-mini" | "gpt-image-2" | 3 more

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation?: "auto" | "low"

Moderation level for the generated image. Default: `auto`.

"auto"

"low"

output\_compression?: number

Compression level for the output image. Default: 100.

minimum0

maximum100

output\_format?: "png" | "webp" | "jpeg"

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

"png"

"webp"

"jpeg"

partial\_images?: number

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

quality?: "low" | "medium" | "high" | "auto"

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

"low"

"medium"

"high"

"auto"

size?: (string & {}) | "1024x1024" | "1024x1536" | "1536x1024" | "auto"

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

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

A tool that allows the model to execute shell commands.

type: "shell"

The type of the shell tool. Always `shell`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

environment?: [BetaContainerAuto](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_auto%20%3E%20(schema)) { type, file\_ids, memory\_limit, 2 more }  | [BetaLocalEnvironment](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_environment%20%3E%20(schema)) { type, skills }  | [BetaContainerReference](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_reference%20%3E%20(schema)) { container\_id, type }  | null

BetaContainerAuto { type, file\_ids, memory\_limit, 2 more }

type: "container\_auto"

Automatically creates a container for this request

file\_ids?: Array<string>

An optional list of uploaded files to make available to your code.

memory\_limit?: "1g" | "4g" | "16g" | "64g" | null

The memory limit for the container.

"1g"

"4g"

"16g"

"64g"

network\_policy?: [BetaContainerNetworkPolicyDisabled](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  | [BetaContainerNetworkPolicyAllowlist](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

BetaContainerNetworkPolicyDisabled { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

BetaContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array<string>

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets?: Array<[BetaContainerNetworkPolicyDomainSecret](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } >

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

minLength1

name: string

The name of the secret to inject for the domain.

minLength1

value: string

The secret value to inject for the domain.

maxLength10485760

minLength1

skills?: Array<[BetaSkillReference](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_skill_reference%20%3E%20(schema)) { skill\_id, type, version }  | [BetaInlineSkill](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill%20%3E%20(schema)) { description, name, source, type } >

An optional list of skills referenced by id or inline data.

BetaSkillReference { skill\_id, type, version }

skill\_id: string

The ID of the referenced skill.

maxLength64

minLength1

type: "skill\_reference"

References a skill created with the /v1/skills endpoint.

version?: string

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

BetaInlineSkill { description, name, source, type }

description: string

The description of the skill.

name: string

The name of the skill.

source: [BetaInlineSkillSource](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema)) { data, media\_type, type }

Inline skill payload

data: string

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

media\_type: "application/zip"

The media type of the inline skill payload. Must be `application/zip`.

type: "base64"

The type of the inline skill source. Must be `base64`.

type: "inline"

Defines an inline skill for this request.

BetaLocalEnvironment { type, skills }

type: "local"

Use a local computer environment.

skills?: Array<[BetaLocalSkill](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema)) { description, name, path } >

An optional list of skills.

description: string

The description of the skill.

name: string

The name of the skill.

path: string

The path to the directory containing the skill.

BetaContainerReference { container\_id, type }

container\_id: string

The ID of the referenced container.

type: "container\_reference"

References a container created with the /v1/containers endpoint

BetaCustomTool { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this tool should be deferred and discovered via tool search.

description?: string

Optional description of the custom tool, used to provide more context.

format?: Text { type }  | Grammar { definition, syntax, type }

The input format for the custom tool. Default is unconstrained text.

Text { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar { definition, syntax, type }

A grammar defined by the user.

definition: string

The grammar definition.

syntax: "lark" | "regex"

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: "grammar"

Grammar format. Always `grammar`.

BetaNamespaceTool { description, name, tools, type }

Groups function/custom tools under a shared namespace.

description: string

A description of the namespace shown to the model.

minLength1

name: string

The namespace name used in tool calls (for example, `crm`).

minLength1

tools: Array<Function { name, type, allowed\_callers, 5 more }  | [BetaCustomTool](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_custom_tool%20%3E%20(schema)) { name, type, allowed\_callers, 3 more } >

The function/custom tools available inside this namespace.

Function { name, type, allowed\_callers, 5 more }

name: string

maxLength128

minLength1

type: "function"

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this function should be deferred and discovered via tool search.

description?: string | null

output\_schema?: Record<string, unknown> | null

A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

parameters?: unknown

strict?: boolean | null

Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

BetaCustomTool { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this tool should be deferred and discovered via tool search.

description?: string

Optional description of the custom tool, used to provide more context.

format?: Text { type }  | Grammar { definition, syntax, type }

The input format for the custom tool. Default is unconstrained text.

Text { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar { definition, syntax, type }

A grammar defined by the user.

definition: string

The grammar definition.

syntax: "lark" | "regex"

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: "grammar"

Grammar format. Always `grammar`.

type: "namespace"

The type of the tool. Always `namespace`.

BetaToolSearchTool { type, description, execution, parameters }

Hosted or BYOT tool search configuration for deferred tools.

type: "tool\_search"

The type of the tool. Always `tool_search`.

description?: string | null

Description shown to the model for a client-executed tool search tool.

execution?: "server" | "client"

Whether tool search is executed by the server or by the client.

"server"

"client"

parameters?: unknown

Parameter schema for a client-executed tool search tool.

BetaWebSearchPreviewTool { type, search\_content\_types, search\_context\_size, user\_location }

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: "web\_search\_preview" | "web\_search\_preview\_2025\_03\_11"

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types?: Array<"text" | "image">

"text"

"image"

search\_context\_size?: "low" | "medium" | "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

"low"

"medium"

"high"

user\_location?: UserLocation | null

The user’s location.

type: "approximate"

The type of location approximation. Always `approximate`.

city?: string | null

Free text input for the city of the user, e.g. `San Francisco`.

country?: string | null

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region?: string | null

Free text input for the region of the user, e.g. `California`.

timezone?: string | null

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

BetaApplyPatchTool { type, allowed\_callers }

Allows the assistant to create, delete, or update files using unified diffs.

type: "apply\_patch"

The type of the tool. Always `apply_patch`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

type: "additional\_tools"

The item type. Always `additional_tools`.

id?: string | null

The unique ID of this additional tools item.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

BetaResponseReasoningItem { id, summary, type, 4 more }

A description of the chain of thought used by a reasoning model while generating
a response. Be sure to include these items in your `input` to the Responses API
for subsequent turns of a conversation if you are manually
[managing context](https://platform.openai.com/docs/guides/conversation-state).

id: string

The unique identifier of the reasoning content.

summary: Array<Summary>

Reasoning summary content.

text: string

A summary of the reasoning output from the model so far.

type: "summary\_text"

The type of the object. Always `summary_text`.

type: "reasoning"

The type of the object. Always `reasoning`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

content?: Array<Content>

Reasoning text content.

text: string

The reasoning text from the model.

type: "reasoning\_text"

The type of the reasoning text. Always `reasoning_text`.

encrypted\_content?: string | null

The encrypted content of the reasoning item. This is populated by default
for reasoning items returned by `POST /v1/responses` and WebSocket
`response.create` requests.

status?: "in\_progress" | "completed" | "incomplete"

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

BetaResponseCompactionItemParam { encrypted\_content, type, id, agent }

A compaction item generated by the [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).

encrypted\_content: string

The encrypted content of the compaction summary.

maxLength10485760

type: "compaction"

The type of the item. Always `compaction`.

id?: string | null

The ID of the compaction item.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

ImageGenerationCall { id, result, status, 2 more }

An image generation request made by the model.

id: string

The unique ID of the image generation call.

result: string | null

The generated image encoded in base64.

status: "in\_progress" | "completed" | "generating" | "failed"

The status of the image generation call.

"in\_progress"

"completed"

"generating"

"failed"

type: "image\_generation\_call"

The type of the image generation call. Always `image_generation_call`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

BetaResponseCodeInterpreterToolCall { id, code, container\_id, 4 more }

A tool call to run code.

id: string

The unique ID of the code interpreter tool call.

code: string | null

The code to run, or null if not available.

container\_id: string

The ID of the container used to run the code.

outputs: Array<Logs { logs, type }  | Image { type, url } > | null

The outputs generated by the code interpreter, such as logs or images.
Can be null if no outputs are available.

Logs { logs, type }

The logs output from the code interpreter.

logs: string

The logs output from the code interpreter.

type: "logs"

The type of the output. Always `logs`.

Image { type, url }

The image output from the code interpreter.

type: "image"

The type of the output. Always `image`.

url: string

The URL of the image output from the code interpreter.

formaturi

status: "in\_progress" | "completed" | "incomplete" | 2 more

The status of the code interpreter tool call. Valid values are `in_progress`, `completed`, `incomplete`, `interpreting`, and `failed`.

"in\_progress"

"completed"

"incomplete"

"interpreting"

"failed"

type: "code\_interpreter\_call"

The type of the code interpreter tool call. Always `code_interpreter_call`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

LocalShellCall { id, action, call\_id, 3 more }

A tool call to run a command on the local shell.

id: string

The unique ID of the local shell call.

action: Action { command, env, type, 3 more }

Execute a shell command on the server.

command: Array<string>

The command to run.

env: Record<string, string>

Environment variables to set for the command.

type: "exec"

The type of the local shell action. Always `exec`.

timeout\_ms?: number | null

Optional timeout in milliseconds for the command.

user?: string | null

Optional user to run the command as.

working\_directory?: string | null

Optional working directory to run the command in.

call\_id: string

The unique ID of the local shell tool call generated by the model.

status: "in\_progress" | "completed" | "incomplete"

The status of the local shell call.

"in\_progress"

"completed"

"incomplete"

type: "local\_shell\_call"

The type of the local shell call. Always `local_shell_call`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

LocalShellCallOutput { id, output, type, 2 more }

The output of a local shell tool call.

id: string

The unique ID of the local shell tool call generated by the model.

output: string

A JSON string of the output of the local shell tool call.

type: "local\_shell\_call\_output"

The type of the local shell tool call output. Always `local_shell_call_output`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

status?: "in\_progress" | "completed" | "incomplete" | null

The status of the item. One of `in_progress`, `completed`, or `incomplete`.

"in\_progress"

"completed"

"incomplete"

ShellCall { action, call\_id, type, 5 more }

A tool representing a request to execute one or more shell commands.

action: Action { commands, max\_output\_length, timeout\_ms }

The shell commands and limits that describe how to run the tool call.

commands: Array<string>

Ordered shell commands for the execution environment to run.

max\_output\_length?: number | null

Maximum number of UTF-8 characters to capture from combined stdout and stderr output.

timeout\_ms?: number | null

Maximum wall-clock time in milliseconds to allow the shell commands to run.

call\_id: string

The unique ID of the shell tool call generated by the model.

maxLength64

minLength1

type: "shell\_call"

The type of the item. Always `shell_call`.

id?: string | null

The unique ID of the shell tool call. Populated when this item is returned via API.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

caller?: Direct { type }  | Program { caller\_id, type }  | null

The execution context that produced this tool call.

Direct { type }

type: "direct"

The caller type. Always `direct`.

Program { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

maxLength64

minLength1

type: "program"

The caller type. Always `program`.

environment?: [BetaLocalEnvironment](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_environment%20%3E%20(schema)) { type, skills }  | [BetaContainerReference](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_reference%20%3E%20(schema)) { container\_id, type }  | null

The environment to execute the shell commands in.

BetaLocalEnvironment { type, skills }

type: "local"

Use a local computer environment.

skills?: Array<[BetaLocalSkill](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema)) { description, name, path } >

An optional list of skills.

description: string

The description of the skill.

name: string

The name of the skill.

path: string

The path to the directory containing the skill.

BetaContainerReference { container\_id, type }

container\_id: string

The ID of the referenced container.

type: "container\_reference"

References a container created with the /v1/containers endpoint

status?: "in\_progress" | "completed" | "incomplete" | null

The status of the shell call. One of `in_progress`, `completed`, or `incomplete`.

"in\_progress"

"completed"

"incomplete"

ShellCallOutput { call\_id, output, type, 5 more }

The streamed output items emitted by a shell tool call.

call\_id: string

The unique ID of the shell tool call generated by the model.

maxLength64

minLength1

output: Array<[BetaResponseFunctionShellCallOutputContent](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_shell_call_output_content%20%3E%20(schema)) { outcome, stderr, stdout } >

Captured chunks of stdout and stderr output, along with their associated outcomes.

outcome: Timeout { type }  | Exit { exit\_code, type }

The exit or timeout outcome associated with this shell call.

Timeout { type }

Indicates that the shell call exceeded its configured time limit.

type: "timeout"

The outcome type. Always `timeout`.

Exit { exit\_code, type }

Indicates that the shell commands finished and returned an exit code.

exit\_code: number

The exit code returned by the shell process.

type: "exit"

The outcome type. Always `exit`.

stderr: string

Captured stderr output for the shell call.

maxLength10485760

stdout: string

Captured stdout output for the shell call.

maxLength10485760

type: "shell\_call\_output"

The type of the item. Always `shell_call_output`.

id?: string | null

The unique ID of the shell tool call output. Populated when this item is returned via API.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

caller?: Direct { type }  | Program { caller\_id, type }  | null

The execution context that produced this tool call.

Direct { type }

type: "direct"

The caller type. Always `direct`.

Program { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

maxLength64

minLength1

type: "program"

The caller type. Always `program`.

max\_output\_length?: number | null

The maximum number of UTF-8 characters captured for this shell call’s combined output.

status?: "in\_progress" | "completed" | "incomplete" | null

The status of the shell call output.

"in\_progress"

"completed"

"incomplete"

ApplyPatchCall { call\_id, operation, status, 4 more }

A tool call representing a request to create, delete, or update files using diff patches.

call\_id: string

The unique ID of the apply patch tool call generated by the model.

maxLength64

minLength1

operation: CreateFile { diff, path, type }  | DeleteFile { path, type }  | UpdateFile { diff, path, type }

The specific create, delete, or update instruction for the apply\_patch tool call.

CreateFile { diff, path, type }

Instruction for creating a new file via the apply\_patch tool.

diff: string

Unified diff content to apply when creating the file.

maxLength10485760

path: string

Path of the file to create relative to the workspace root.

minLength1

type: "create\_file"

The operation type. Always `create_file`.

DeleteFile { path, type }

Instruction for deleting an existing file via the apply\_patch tool.

path: string

Path of the file to delete relative to the workspace root.

minLength1

type: "delete\_file"

The operation type. Always `delete_file`.

UpdateFile { diff, path, type }

Instruction for updating an existing file via the apply\_patch tool.

diff: string

Unified diff content to apply to the existing file.

maxLength10485760

path: string

Path of the file to update relative to the workspace root.

minLength1

type: "update\_file"

The operation type. Always `update_file`.

status: "in\_progress" | "completed"

The status of the apply patch tool call. One of `in_progress` or `completed`.

"in\_progress"

"completed"

type: "apply\_patch\_call"

The type of the item. Always `apply_patch_call`.

id?: string | null

The unique ID of the apply patch tool call. Populated when this item is returned via API.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

caller?: Direct { type }  | Program { caller\_id, type }  | null

The execution context that produced this tool call.

Direct { type }

type: "direct"

The caller type. Always `direct`.

Program { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

maxLength64

minLength1

type: "program"

The caller type. Always `program`.

ApplyPatchCallOutput { call\_id, status, type, 4 more }

The streamed output emitted by an apply patch tool call.

call\_id: string

The unique ID of the apply patch tool call generated by the model.

maxLength64

minLength1

status: "completed" | "failed"

The status of the apply patch tool call output. One of `completed` or `failed`.

"completed"

"failed"

type: "apply\_patch\_call\_output"

The type of the item. Always `apply_patch_call_output`.

id?: string | null

The unique ID of the apply patch tool call output. Populated when this item is returned via API.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

caller?: Direct { type }  | Program { caller\_id, type }  | null

The execution context that produced this tool call.

Direct { type }

type: "direct"

The caller type. Always `direct`.

Program { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

maxLength64

minLength1

type: "program"

The caller type. Always `program`.

output?: string | null

Optional human-readable log text from the apply patch tool (e.g., patch results or errors).

maxLength10485760

McpListTools { id, server\_label, tools, 3 more }

A list of tools available on an MCP server.

id: string

The unique ID of the list.

server\_label: string

The label of the MCP server.

tools: Array<Tool>

The tools available on the server.

input\_schema: unknown

The JSON schema describing the tool’s input.

name: string

The name of the tool.

annotations?: unknown

Additional annotations about the tool.

description?: string | null

The description of the tool.

type: "mcp\_list\_tools"

The type of the item. Always `mcp_list_tools`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

error?: string | null

Error message if the server could not list tools.

McpApprovalRequest { id, arguments, name, 3 more }

A request for human approval of a tool invocation.

id: string

The unique ID of the approval request.

arguments: string

A JSON string of arguments for the tool.

name: string

The name of the tool to run.

server\_label: string

The label of the MCP server making the request.

type: "mcp\_approval\_request"

The type of the item. Always `mcp_approval_request`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

McpApprovalResponse { approval\_request\_id, approve, type, 3 more }

A response to an MCP approval request.

approval\_request\_id: string

The ID of the approval request being answered.

approve: boolean

Whether the request was approved.

type: "mcp\_approval\_response"

The type of the item. Always `mcp_approval_response`.

id?: string | null

The unique ID of the approval response

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

reason?: string | null

Optional reason for the decision.

McpCall { id, arguments, name, 7 more }

An invocation of a tool on an MCP server.

id: string

The unique ID of the tool call.

arguments: string

A JSON string of the arguments passed to the tool.

name: string

The name of the tool that was run.

server\_label: string

The label of the MCP server running the tool.

type: "mcp\_call"

The type of the item. Always `mcp_call`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

approval\_request\_id?: string | null

Unique identifier for the MCP tool call approval request.
Include this value in a subsequent `mcp_approval_response` input to approve or reject the corresponding tool call.

error?: string | null

The error from the tool call, if any.

output?: string | null

The output from the tool call.

status?: "in\_progress" | "completed" | "incomplete" | 2 more

The status of the tool call. One of `in_progress`, `completed`, `incomplete`, `calling`, or `failed`.

"in\_progress"

"completed"

"incomplete"

"calling"

"failed"

BetaResponseCustomToolCallOutput { call\_id, output, type, 3 more }

The output of a custom tool call from your code, being sent back to the model.

call\_id: string

The call ID, used to map this custom tool call output to a custom tool call.

output: string | Array<[BetaResponseInputText](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_text%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  | [BetaResponseInputImage](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_image%20%3E%20(schema)) { detail, type, file\_id, 2 more }  | [BetaResponseInputFile](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_file%20%3E%20(schema)) { type, detail, file\_data, 4 more } >

The output from the custom tool call generated by your code.
Can be a string or an list of output content.

string

Array<[BetaResponseInputText](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_text%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  | [BetaResponseInputImage](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_image%20%3E%20(schema)) { detail, type, file\_id, 2 more }  | [BetaResponseInputFile](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_file%20%3E%20(schema)) { type, detail, file\_data, 4 more } >

BetaResponseInputText { text, type, prompt\_cache\_breakpoint }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

BetaResponseInputImage { detail, type, file\_id, 2 more }

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: "low" | "high" | "auto" | "original"

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

"low"

"high"

"auto"

"original"

type: "input\_image"

The type of the input item. Always `input_image`.

file\_id?: string | null

The ID of the file to be sent to the model.

image\_url?: string | null

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

BetaResponseInputFile { type, detail, file\_data, 4 more }

A file input to the model.

type: "input\_file"

The type of the input item. Always `input_file`.

detail?: "auto" | "low" | "high"

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

"auto"

"low"

"high"

file\_data?: string

The content of the file to be sent to the model.

file\_id?: string | null

The ID of the file to be sent to the model.

file\_url?: string

The URL of the file to be sent to the model.

formaturi

filename?: string

The name of the file to be sent to the model.

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

type: "custom\_tool\_call\_output"

The type of the custom tool call output. Always `custom_tool_call_output`.

id?: string

The unique ID of the custom tool call output in the OpenAI platform.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

caller?: Direct { type }  | Program { caller\_id, type }  | null

The execution context that produced this tool call.

Direct { type }

type: "direct"

The caller type. Always `direct`.

Program { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

maxLength64

minLength1

type: "program"

The caller type. Always `program`.

BetaResponseCustomToolCall { call\_id, input, name, 5 more }

A call to a custom tool created by the model.

call\_id: string

An identifier used to map this custom tool call to a tool call output.

input: string

The input for the custom tool call generated by the model.

name: string

The name of the custom tool being called.

type: "custom\_tool\_call"

The type of the custom tool call. Always `custom_tool_call`.

id?: string

The unique ID of the custom tool call in the OpenAI platform.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

caller?: Direct { type }  | Program { caller\_id, type }  | null

The execution context that produced this tool call.

Direct { type }

type: "direct"

Program { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

type: "program"

namespace?: string

The namespace of the custom tool being called.

CompactionTrigger { type, agent }

Compacts the current context. Must be the final input item.

type: "compaction\_trigger"

The type of the item. Always `compaction_trigger`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

ItemReference { id, agent, type }

An internal identifier for an item to reference.

id: string

The ID of the item to reference.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

type?: "item\_reference" | null

The type of item to reference. Always `item_reference`.

Program { id, call\_id, code, 3 more }

id: string

The unique ID of this program item.

call\_id: string

The stable call ID of the program item.

maxLength64

minLength1

code: string

The JavaScript source executed by programmatic tool calling.

maxLength10485760

fingerprint: string

Opaque program replay fingerprint that must be round-tripped.

maxLength10485760

type: "program"

The item type. Always `program`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

ProgramOutput { id, call\_id, result, 3 more }

id: string

The unique ID of this program output item.

call\_id: string

The call ID of the program item.

maxLength64

minLength1

result: string

The result produced by the program item.

maxLength10485760

status: "completed" | "incomplete"

The terminal status of the program output.

"completed"

"incomplete"

type: "program\_output"

The item type. Always `program_output`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

metadata: Record<string, string> | null

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: "gpt-5.6-sol" | "gpt-5.6-terra" | "gpt-5.6-luna" | 92 more | (string & {})

Model ID used to generate the response, like `gpt-4o` or `o3`. OpenAI
offers a wide range of models with different capabilities, performance
characteristics, and price points. Refer to the [model guide](https://platform.openai.com/docs/models)
to browse and compare available models.

"gpt-5.6-sol" | "gpt-5.6-terra" | "gpt-5.6-luna" | 92 more

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

(string & {})

object: "response"

The object type of this resource - always set to `response`.

output: Array<[BetaResponseOutputItem](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_item%20%3E%20(schema))>

An array of content items generated by the model.

* The length and order of items in the `output` array is dependent
  on the model’s response.
* Rather than accessing the first item in the `output` array and
  assuming it’s an `assistant` message with the content generated by
  the model, you might consider using the `output_text` property where
  supported in SDKs.

BetaResponseOutputMessage { id, content, role, 4 more }

An output message from the model.

id: string

The unique ID of the output message.

content: Array<[BetaResponseOutputText](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_text%20%3E%20(schema)) { annotations, text, type, logprobs }  | [BetaResponseOutputRefusal](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_refusal%20%3E%20(schema)) { refusal, type } >

The content of the output message.

BetaResponseOutputText { annotations, text, type, logprobs }

A text output from the model.

annotations: Array<FileCitation { file\_id, filename, index, type }  | URLCitation { end\_index, start\_index, title, 2 more }  | ContainerFileCitation { container\_id, end\_index, file\_id, 3 more }  | FilePath { file\_id, index, type } >

The annotations of the text output.

FileCitation { file\_id, filename, index, type }

A citation to a file.

file\_id: string

The ID of the file.

filename: string

The filename of the file cited.

index: number

The index of the file in the list of files.

type: "file\_citation"

The type of the file citation. Always `file_citation`.

URLCitation { end\_index, start\_index, title, 2 more }

A citation for a web resource used to generate a model response.

end\_index: number

The index of the last character of the URL citation in the message.

start\_index: number

The index of the first character of the URL citation in the message.

title: string

The title of the web resource.

type: "url\_citation"

The type of the URL citation. Always `url_citation`.

url: string

The URL of the web resource.

formaturi

ContainerFileCitation { container\_id, end\_index, file\_id, 3 more }

A citation for a container file used to generate a model response.

container\_id: string

The ID of the container file.

end\_index: number

The index of the last character of the container file citation in the message.

file\_id: string

The ID of the file.

filename: string

The filename of the container file cited.

start\_index: number

The index of the first character of the container file citation in the message.

type: "container\_file\_citation"

The type of the container file citation. Always `container_file_citation`.

FilePath { file\_id, index, type }

A path to a file.

file\_id: string

The ID of the file.

index: number

The index of the file in the list of files.

type: "file\_path"

The type of the file path. Always `file_path`.

text: string

The text output from the model.

type: "output\_text"

The type of the output text. Always `output_text`.

logprobs?: Array<Logprob>

token: string

bytes: Array<number>

logprob: number

top\_logprobs: Array<TopLogprob>

token: string

bytes: Array<number>

logprob: number

BetaResponseOutputRefusal { refusal, type }

A refusal from the model.

refusal: string

The refusal explanation from the model.

type: "refusal"

The type of the refusal. Always `refusal`.

role: "assistant"

The role of the output message. Always `assistant`.

status: "in\_progress" | "completed" | "incomplete"

The status of the message input. One of `in_progress`, `completed`, or
`incomplete`. Populated when input items are returned via API.

"in\_progress"

"completed"

"incomplete"

type: "message"

The type of the output message. Always `message`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

phase?: "commentary" | "final\_answer" | null

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

"commentary"

"final\_answer"

BetaResponseFileSearchToolCall { id, queries, status, 3 more }

The results of a file search tool call. See the
[file search guide](https://platform.openai.com/docs/guides/tools-file-search) for more information.

id: string

The unique ID of the file search tool call.

queries: Array<string>

The queries used to search for files.

status: "in\_progress" | "searching" | "completed" | 2 more

The status of the file search tool call. One of `in_progress`,
`searching`, `incomplete` or `failed`,

"in\_progress"

"searching"

"completed"

"incomplete"

"failed"

type: "file\_search\_call"

The type of the file search tool call. Always `file_search_call`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

results?: Array<Result> | null

The results of the file search tool call.

attributes?: Record<string, string | number | boolean> | null

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.

string

number

boolean

file\_id?: string

The unique ID of the file.

filename?: string

The name of the file.

score?: number

The relevance score of the file - a value between 0 and 1.

formatfloat

text?: string

The text that was retrieved from the file.

BetaResponseFunctionToolCall { arguments, call\_id, name, 6 more }

A tool call to run a function. See the
[function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.

arguments: string

A JSON string of the arguments to pass to the function.

call\_id: string

The unique ID of the function tool call generated by the model.

name: string

The name of the function to run.

type: "function\_call"

The type of the function tool call. Always `function_call`.

id?: string

The unique ID of the function tool call.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

caller?: Direct { type }  | Program { caller\_id, type }  | null

The execution context that produced this tool call.

Direct { type }

type: "direct"

Program { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

type: "program"

namespace?: string

The namespace of the function to run.

status?: "in\_progress" | "completed" | "incomplete"

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

BetaResponseFunctionToolCallOutputItem { id, call\_id, output, 5 more }

id: string

The unique ID of the function call tool output.

call\_id: string

The unique ID of the function tool call generated by the model.

output: string | Array<[BetaResponseInputText](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_text%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  | [BetaResponseInputImage](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_image%20%3E%20(schema)) { detail, type, file\_id, 2 more }  | [BetaResponseInputFile](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_file%20%3E%20(schema)) { type, detail, file\_data, 4 more } >

The output from the function call generated by your code.
Can be a string or an list of output content.

string

Array<[BetaResponseInputText](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_text%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  | [BetaResponseInputImage](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_image%20%3E%20(schema)) { detail, type, file\_id, 2 more }  | [BetaResponseInputFile](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_file%20%3E%20(schema)) { type, detail, file\_data, 4 more } >

BetaResponseInputText { text, type, prompt\_cache\_breakpoint }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

BetaResponseInputImage { detail, type, file\_id, 2 more }

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: "low" | "high" | "auto" | "original"

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

"low"

"high"

"auto"

"original"

type: "input\_image"

The type of the input item. Always `input_image`.

file\_id?: string | null

The ID of the file to be sent to the model.

image\_url?: string | null

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

BetaResponseInputFile { type, detail, file\_data, 4 more }

A file input to the model.

type: "input\_file"

The type of the input item. Always `input_file`.

detail?: "auto" | "low" | "high"

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

"auto"

"low"

"high"

file\_data?: string

The content of the file to be sent to the model.

file\_id?: string | null

The ID of the file to be sent to the model.

file\_url?: string

The URL of the file to be sent to the model.

formaturi

filename?: string

The name of the file to be sent to the model.

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

status: "in\_progress" | "completed" | "incomplete"

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

type: "function\_call\_output"

The type of the function tool call output. Always `function_call_output`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

caller?: Direct { type }  | Program { caller\_id, type }  | null

The execution context that produced this tool call.

Direct { type }

type: "direct"

The caller type. Always `direct`.

Program { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

maxLength64

minLength1

type: "program"

The caller type. Always `program`.

created\_by?: string

The identifier of the actor that created the item.

AgentMessage { id, author, content, 3 more }

id: string

The unique ID of the agent message.

author: string

The sending agent identity.

content: Array<[BetaResponseInputText](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_text%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  | [BetaResponseOutputText](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_text%20%3E%20(schema)) { annotations, text, type, logprobs }  | Text { text, type }  | 7 more>

Encrypted content sent between agents.

BetaResponseInputText { text, type, prompt\_cache\_breakpoint }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

BetaResponseOutputText { annotations, text, type, logprobs }

A text output from the model.

annotations: Array<FileCitation { file\_id, filename, index, type }  | URLCitation { end\_index, start\_index, title, 2 more }  | ContainerFileCitation { container\_id, end\_index, file\_id, 3 more }  | FilePath { file\_id, index, type } >

The annotations of the text output.

FileCitation { file\_id, filename, index, type }

A citation to a file.

file\_id: string

The ID of the file.

filename: string

The filename of the file cited.

index: number

The index of the file in the list of files.

type: "file\_citation"

The type of the file citation. Always `file_citation`.

URLCitation { end\_index, start\_index, title, 2 more }

A citation for a web resource used to generate a model response.

end\_index: number

The index of the last character of the URL citation in the message.

start\_index: number

The index of the first character of the URL citation in the message.

title: string

The title of the web resource.

type: "url\_citation"

The type of the URL citation. Always `url_citation`.

url: string

The URL of the web resource.

formaturi

ContainerFileCitation { container\_id, end\_index, file\_id, 3 more }

A citation for a container file used to generate a model response.

container\_id: string

The ID of the container file.

end\_index: number

The index of the last character of the container file citation in the message.

file\_id: string

The ID of the file.

filename: string

The filename of the container file cited.

start\_index: number

The index of the first character of the container file citation in the message.

type: "container\_file\_citation"

The type of the container file citation. Always `container_file_citation`.

FilePath { file\_id, index, type }

A path to a file.

file\_id: string

The ID of the file.

index: number

The index of the file in the list of files.

type: "file\_path"

The type of the file path. Always `file_path`.

text: string

The text output from the model.

type: "output\_text"

The type of the output text. Always `output_text`.

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

A summary of the reasoning output from the model so far.

type: "summary\_text"

The type of the object. Always `summary_text`.

ReasoningText { text, type }

Reasoning text from the model.

text: string

The reasoning text from the model.

type: "reasoning\_text"

The type of the reasoning text. Always `reasoning_text`.

BetaResponseOutputRefusal { refusal, type }

A refusal from the model.

refusal: string

The refusal explanation from the model.

type: "refusal"

The type of the refusal. Always `refusal`.

BetaResponseInputImage { detail, type, file\_id, 2 more }

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: "low" | "high" | "auto" | "original"

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

"low"

"high"

"auto"

"original"

type: "input\_image"

The type of the input item. Always `input_image`.

file\_id?: string | null

The ID of the file to be sent to the model.

image\_url?: string | null

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

ComputerScreenshot { detail, file\_id, image\_url, 2 more }

A screenshot of a computer.

detail: "low" | "high" | "auto" | "original"

The detail level of the screenshot image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

"low"

"high"

"auto"

"original"

file\_id: string | null

The identifier of an uploaded file that contains the screenshot.

image\_url: string | null

The URL of the screenshot image.

formaturi

type: "computer\_screenshot"

Specifies the event type. For a computer screenshot, this property is always set to `computer_screenshot`.

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

BetaResponseInputFile { type, detail, file\_data, 4 more }

A file input to the model.

type: "input\_file"

The type of the input item. Always `input_file`.

detail?: "auto" | "low" | "high"

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

"auto"

"low"

"high"

file\_data?: string

The content of the file to be sent to the model.

file\_id?: string | null

The ID of the file to be sent to the model.

file\_url?: string

The URL of the file to be sent to the model.

formaturi

filename?: string

The name of the file to be sent to the model.

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

EncryptedContent { encrypted\_content, type }

Opaque encrypted content that Responses API decrypts inside trusted model execution.

encrypted\_content: string

Opaque encrypted content.

type: "encrypted\_content"

The type of the input item. Always `encrypted_content`.

recipient: string

The destination agent identity.

type: "agent\_message"

The type of the item. Always `agent_message`.

agent?: Agent { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

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

The unique ID linking this call to its output.

type: "multi\_agent\_call"

The type of the multi-agent call. Always `multi_agent_call`.

agent?: Agent { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

MultiAgentCallOutput { id, action, call\_id, 3 more }

id: string

The unique ID of the multi-agent call output item.

action: "spawn\_agent" | "interrupt\_agent" | "list\_agents" | 3 more

The multi-agent action that produced this result.

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

call\_id: string

The unique ID of the multi-agent call.

output: Array<[BetaResponseOutputText](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_text%20%3E%20(schema)) { annotations, text, type, logprobs } >

Text output returned by the multi-agent action.

annotations: Array<FileCitation { file\_id, filename, index, type }  | URLCitation { end\_index, start\_index, title, 2 more }  | ContainerFileCitation { container\_id, end\_index, file\_id, 3 more }  | FilePath { file\_id, index, type } >

The annotations of the text output.

FileCitation { file\_id, filename, index, type }

A citation to a file.

file\_id: string

The ID of the file.

filename: string

The filename of the file cited.

index: number

The index of the file in the list of files.

type: "file\_citation"

The type of the file citation. Always `file_citation`.

URLCitation { end\_index, start\_index, title, 2 more }

A citation for a web resource used to generate a model response.

end\_index: number

The index of the last character of the URL citation in the message.

start\_index: number

The index of the first character of the URL citation in the message.

title: string

The title of the web resource.

type: "url\_citation"

The type of the URL citation. Always `url_citation`.

url: string

The URL of the web resource.

formaturi

ContainerFileCitation { container\_id, end\_index, file\_id, 3 more }

A citation for a container file used to generate a model response.

container\_id: string

The ID of the container file.

end\_index: number

The index of the last character of the container file citation in the message.

file\_id: string

The ID of the file.

filename: string

The filename of the container file cited.

start\_index: number

The index of the first character of the container file citation in the message.

type: "container\_file\_citation"

The type of the container file citation. Always `container_file_citation`.

FilePath { file\_id, index, type }

A path to a file.

file\_id: string

The ID of the file.

index: number

The index of the file in the list of files.

type: "file\_path"

The type of the file path. Always `file_path`.

text: string

The text output from the model.

type: "output\_text"

The type of the output text. Always `output_text`.

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

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

BetaResponseFunctionWebSearch { id, action, status, 2 more }

The results of a web search tool call. See the
[web search guide](https://platform.openai.com/docs/guides/tools-web-search) for more information.

id: string

The unique ID of the web search tool call.

action: Search { type, queries, query, sources }  | OpenPage { type, url }  | FindInPage { pattern, type, url }

An object describing the specific action taken in this web search call.
Includes details on how the model used the web (search, open\_page, find\_in\_page).

Search { type, queries, query, sources }

Action type “search” - Performs a web search query.

type: "search"

The action type.

queries?: Array<string>

The search queries.

Deprecatedquery?: string

The search query.

sources?: Array<Source>

The sources used in the search.

type: "url"

The type of source. Always `url`.

url: string

The URL of the source.

formaturi

OpenPage { type, url }

Action type “open\_page” - Opens a specific URL from search results.

type: "open\_page"

The action type.

url?: string | null

The URL opened by the model.

formaturi

FindInPage { pattern, type, url }

Action type “find\_in\_page”: Searches for a pattern within a loaded page.

pattern: string

The pattern or text to search for within the page.

type: "find\_in\_page"

The action type.

url: string

The URL of the page searched for the pattern.

formaturi

status: "in\_progress" | "searching" | "completed" | "failed"

The status of the web search tool call.

"in\_progress"

"searching"

"completed"

"failed"

type: "web\_search\_call"

The type of the web search tool call. Always `web_search_call`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

BetaResponseComputerToolCall { id, call\_id, pending\_safety\_checks, 5 more }

A tool call to a computer use tool. See the
[computer use guide](https://platform.openai.com/docs/guides/tools-computer-use) for more information.

id: string

The unique ID of the computer call.

call\_id: string

An identifier used when responding to the tool call with output.

pending\_safety\_checks: Array<PendingSafetyCheck>

The pending safety checks for the computer call.

id: string

The ID of the pending safety check.

code?: string | null

The type of the pending safety check.

message?: string | null

Details about the pending safety check.

status: "in\_progress" | "completed" | "incomplete"

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

type: "computer\_call"

The type of the computer call. Always `computer_call`.

action?: [BetaComputerAction](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_computer_action%20%3E%20(schema))

A click action.

Click { button, type, x, 2 more }

A click action.

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

[
  { x: 100, y: 200 },
  { x: 200, y: 300 }
]

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

Flattened batched actions for `computer_use`. Each action includes an
`type` discriminator and action-specific fields.

Click { button, type, x, 2 more }

A click action.

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

[
  { x: 100, y: 200 },
  { x: 200, y: 300 }
]

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

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

BetaResponseComputerToolCallOutputItem { id, call\_id, output, 5 more }

id: string

The unique ID of the computer call tool output.

call\_id: string

The ID of the computer tool call that produced the output.

output: [BetaResponseComputerToolCallOutputScreenshot](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_computer_tool_call_output_screenshot%20%3E%20(schema)) { type, file\_id, image\_url }

A computer screenshot image used with the computer use tool.

type: "computer\_screenshot"

Specifies the event type. For a computer screenshot, this property is
always set to `computer_screenshot`.

file\_id?: string

The identifier of an uploaded file that contains the screenshot.

image\_url?: string

The URL of the screenshot image.

formaturi

status: "completed" | "incomplete" | "failed" | "in\_progress"

The status of the message input. One of `in_progress`, `completed`, or
`incomplete`. Populated when input items are returned via API.

"completed"

"incomplete"

"failed"

"in\_progress"

type: "computer\_call\_output"

The type of the computer tool call output. Always `computer_call_output`.

acknowledged\_safety\_checks?: Array<AcknowledgedSafetyCheck>

The safety checks reported by the API that have been acknowledged by the
developer.

id: string

The ID of the pending safety check.

code?: string | null

The type of the pending safety check.

message?: string | null

Details about the pending safety check.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

created\_by?: string

The identifier of the actor that created the item.

BetaResponseReasoningItem { id, summary, type, 4 more }

A description of the chain of thought used by a reasoning model while generating
a response. Be sure to include these items in your `input` to the Responses API
for subsequent turns of a conversation if you are manually
[managing context](https://platform.openai.com/docs/guides/conversation-state).

id: string

The unique identifier of the reasoning content.

summary: Array<Summary>

Reasoning summary content.

text: string

A summary of the reasoning output from the model so far.

type: "summary\_text"

The type of the object. Always `summary_text`.

type: "reasoning"

The type of the object. Always `reasoning`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

content?: Array<Content>

Reasoning text content.

text: string

The reasoning text from the model.

type: "reasoning\_text"

The type of the reasoning text. Always `reasoning_text`.

encrypted\_content?: string | null

The encrypted content of the reasoning item. This is populated by default
for reasoning items returned by `POST /v1/responses` and WebSocket
`response.create` requests.

status?: "in\_progress" | "completed" | "incomplete"

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

Program { id, call\_id, code, 3 more }

id: string

The unique ID of the program item.

call\_id: string

The stable call ID of the program item.

code: string

The JavaScript source executed by programmatic tool calling.

fingerprint: string

Opaque program replay fingerprint that must be round-tripped.

type: "program"

The type of the item. Always `program`.

agent?: Agent { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

ProgramOutput { id, call\_id, result, 3 more }

id: string

The unique ID of the program output item.

call\_id: string

The call ID of the program item.

result: string

The result produced by the program item.

status: "completed" | "incomplete"

The terminal status of the program output item.

"completed"

"incomplete"

type: "program\_output"

The type of the item. Always `program_output`.

agent?: Agent { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

BetaResponseToolSearchCall { id, arguments, call\_id, 5 more }

id: string

The unique ID of the tool search call item.

arguments: unknown

Arguments used for the tool search call.

call\_id: string | null

The unique ID of the tool search call generated by the model.

execution: "server" | "client"

Whether tool search was executed by the server or by the client.

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

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

created\_by?: string

The identifier of the actor that created the item.

BetaResponseToolSearchOutputItem { id, call\_id, execution, 5 more }

id: string

The unique ID of the tool search output item.

call\_id: string | null

The unique ID of the tool search call generated by the model.

execution: "server" | "client"

Whether tool search was executed by the server or by the client.

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

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

name: string

The name of the function to call.

parameters: Record<string, unknown> | null

A JSON schema object describing the parameters of the function.

strict: boolean | null

Whether strict parameter validation is enforced for this function tool.

type: "function"

The type of the function tool. Always `function`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this function is deferred and loaded via tool search.

description?: string | null

A description of the function. Used by the model to determine whether or not to call the function.

output\_schema?: Record<string, unknown> | null

A JSON schema object describing the JSON value encoded in string outputs for this function.

BetaFileSearchTool { type, vector\_store\_ids, filters, 2 more }

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

type: "file\_search"

The type of the file search tool. Always `file_search`.

vector\_store\_ids: Array<string>

The IDs of the vector stores to search.

filters?: ComparisonFilter { key, type, value }  | CompoundFilter { filters, type }  | null

A filter to apply.

ComparisonFilter { key, type, value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: string

The key to compare against the value.

type: "eq" | "ne" | "gt" | 5 more

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: string | number | boolean | Array<string | number>

The value to compare against the attribute key; supports string, number, or boolean types.

string

number

boolean

Array<string | number>

string

number

CompoundFilter { filters, type }

Combine multiple filters using `and` or `or`.

filters: Array<ComparisonFilter { key, type, value }  | unknown>

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

ComparisonFilter { key, type, value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: string

The key to compare against the value.

type: "eq" | "ne" | "gt" | 5 more

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: string | number | boolean | Array<string | number>

The value to compare against the attribute key; supports string, number, or boolean types.

string

number

boolean

Array<string | number>

string

number

unknown

type: "and" | "or"

Type of operation: `and` or `or`.

"and"

"or"

max\_num\_results?: number

The maximum number of results to return. This number should be between 1 and 50 inclusive.

ranking\_options?: RankingOptions { hybrid\_search, ranker, score\_threshold }

Ranking options for search.

hybrid\_search?: HybridSearch { embedding\_weight, text\_weight }

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

embedding\_weight: number

The weight of the embedding in the reciprocal ranking fusion.

text\_weight: number

The weight of the text in the reciprocal ranking fusion.

ranker?: "auto" | "default-2024-11-15"

The ranker to use for the file search.

"auto"

"default-2024-11-15"

score\_threshold?: number

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

BetaComputerTool { type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

type: "computer"

The type of the computer tool. Always `computer`.

BetaComputerUsePreviewTool { display\_height, display\_width, environment, type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

display\_height: number

The height of the computer display.

display\_width: number

The width of the computer display.

environment: "windows" | "mac" | "linux" | 2 more

The type of computer environment to control.

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: "computer\_use\_preview"

The type of the computer use tool. Always `computer_use_preview`.

BetaWebSearchTool { type, filters, search\_context\_size, user\_location }

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: "web\_search" | "web\_search\_2025\_08\_26"

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

"web\_search"

"web\_search\_2025\_08\_26"

filters?: Filters | null

Filters for the search.

allowed\_domains?: Array<string> | null

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

search\_context\_size?: "low" | "medium" | "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

"low"

"medium"

"high"

user\_location?: UserLocation | null

The approximate location of the user.

city?: string | null

Free text input for the city of the user, e.g. `San Francisco`.

country?: string | null

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region?: string | null

Free text input for the region of the user, e.g. `California`.

timezone?: string | null

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

type?: "approximate"

The type of location approximation. Always `approximate`.

Mcp { server\_label, type, allowed\_callers, 9 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: string

A label for this MCP server, used to identify it in tool calls.

type: "mcp"

The type of the MCP tool. Always `mcp`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

allowed\_tools?: Array<string> | McpToolFilter { read\_only, tool\_names }  | null

List of allowed tool names or a filter object.

Array<string>

McpToolFilter { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

authorization?: string

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

connector\_id?: "connector\_dropbox" | "connector\_gmail" | "connector\_googlecalendar" | 5 more

Identifier for service connectors, like those available in ChatGPT. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided. Learn more
about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

Currently supported `connector_id` values are:

* Dropbox: `connector_dropbox`
* Gmail: `connector_gmail`
* Google Calendar: `connector_googlecalendar`
* Google Drive: `connector_googledrive`
* Microsoft Teams: `connector_microsoftteams`
* Outlook Calendar: `connector_outlookcalendar`
* Outlook Email: `connector_outlookemail`
* SharePoint: `connector_sharepoint`

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading?: boolean

Whether this MCP tool is deferred and discovered via tool search.

headers?: Record<string, string> | null

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

require\_approval?: McpToolApprovalFilter { always, never }  | "always" | "never" | null

Specify which of the MCP server’s tools require approval.

McpToolApprovalFilter { always, never }

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

always?: Always { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

never?: Never { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

"always" | "never"

"always"

"never"

server\_description?: string

Optional description of the MCP server, used to provide more context.

server\_url?: string

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

tunnel\_id?: string

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

CodeInterpreter { container, type, allowed\_callers }

A tool that runs Python code to help generate a response to a prompt.

container: string | CodeInterpreterToolAuto { type, file\_ids, memory\_limit, network\_policy }

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

string

CodeInterpreterToolAuto { type, file\_ids, memory\_limit, network\_policy }

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

type: "auto"

Always `auto`.

file\_ids?: Array<string>

An optional list of uploaded files to make available to your code.

memory\_limit?: "1g" | "4g" | "16g" | "64g" | null

The memory limit for the code interpreter container.

"1g"

"4g"

"16g"

"64g"

network\_policy?: [BetaContainerNetworkPolicyDisabled](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  | [BetaContainerNetworkPolicyAllowlist](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

BetaContainerNetworkPolicyDisabled { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

BetaContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array<string>

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets?: Array<[BetaContainerNetworkPolicyDomainSecret](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } >

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

minLength1

name: string

The name of the secret to inject for the domain.

minLength1

value: string

The secret value to inject for the domain.

maxLength10485760

minLength1

type: "code\_interpreter"

The type of the code interpreter tool. Always `code_interpreter`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

ProgrammaticToolCalling { type }

type: "programmatic\_tool\_calling"

The type of the tool. Always `programmatic_tool_calling`.

ImageGeneration { type, action, background, 9 more }

A tool that generates images using the GPT image models.

type: "image\_generation"

The type of the image generation tool. Always `image_generation`.

action?: "generate" | "edit" | "auto"

Whether to generate a new image or edit an existing image. Default: `auto`.

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

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

"high"

"low"

input\_image\_mask?: InputImageMask { file\_id, image\_url }

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

file\_id?: string

File ID for the mask image.

image\_url?: string

Base64-encoded mask image.

model?: (string & {}) | "gpt-image-1" | "gpt-image-1-mini" | "gpt-image-2" | 3 more

The image generation model to use. Default: `gpt-image-1`.

(string & {})

"gpt-image-1" | "gpt-image-1-mini" | "gpt-image-2" | 3 more

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation?: "auto" | "low"

Moderation level for the generated image. Default: `auto`.

"auto"

"low"

output\_compression?: number

Compression level for the output image. Default: 100.

minimum0

maximum100

output\_format?: "png" | "webp" | "jpeg"

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

"png"

"webp"

"jpeg"

partial\_images?: number

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

quality?: "low" | "medium" | "high" | "auto"

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

"low"

"medium"

"high"

"auto"

size?: (string & {}) | "1024x1024" | "1024x1536" | "1536x1024" | "auto"

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

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

A tool that allows the model to execute shell commands.

type: "shell"

The type of the shell tool. Always `shell`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

environment?: [BetaContainerAuto](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_auto%20%3E%20(schema)) { type, file\_ids, memory\_limit, 2 more }  | [BetaLocalEnvironment](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_environment%20%3E%20(schema)) { type, skills }  | [BetaContainerReference](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_reference%20%3E%20(schema)) { container\_id, type }  | null

BetaContainerAuto { type, file\_ids, memory\_limit, 2 more }

type: "container\_auto"

Automatically creates a container for this request

file\_ids?: Array<string>

An optional list of uploaded files to make available to your code.

memory\_limit?: "1g" | "4g" | "16g" | "64g" | null

The memory limit for the container.

"1g"

"4g"

"16g"

"64g"

network\_policy?: [BetaContainerNetworkPolicyDisabled](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  | [BetaContainerNetworkPolicyAllowlist](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

BetaContainerNetworkPolicyDisabled { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

BetaContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array<string>

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets?: Array<[BetaContainerNetworkPolicyDomainSecret](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } >

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

minLength1

name: string

The name of the secret to inject for the domain.

minLength1

value: string

The secret value to inject for the domain.

maxLength10485760

minLength1

skills?: Array<[BetaSkillReference](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_skill_reference%20%3E%20(schema)) { skill\_id, type, version }  | [BetaInlineSkill](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill%20%3E%20(schema)) { description, name, source, type } >

An optional list of skills referenced by id or inline data.

BetaSkillReference { skill\_id, type, version }

skill\_id: string

The ID of the referenced skill.

maxLength64

minLength1

type: "skill\_reference"

References a skill created with the /v1/skills endpoint.

version?: string

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

BetaInlineSkill { description, name, source, type }

description: string

The description of the skill.

name: string

The name of the skill.

source: [BetaInlineSkillSource](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema)) { data, media\_type, type }

Inline skill payload

data: string

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

media\_type: "application/zip"

The media type of the inline skill payload. Must be `application/zip`.

type: "base64"

The type of the inline skill source. Must be `base64`.

type: "inline"

Defines an inline skill for this request.

BetaLocalEnvironment { type, skills }

type: "local"

Use a local computer environment.

skills?: Array<[BetaLocalSkill](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema)) { description, name, path } >

An optional list of skills.

description: string

The description of the skill.

name: string

The name of the skill.

path: string

The path to the directory containing the skill.

BetaContainerReference { container\_id, type }

container\_id: string

The ID of the referenced container.

type: "container\_reference"

References a container created with the /v1/containers endpoint

BetaCustomTool { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this tool should be deferred and discovered via tool search.

description?: string

Optional description of the custom tool, used to provide more context.

format?: Text { type }  | Grammar { definition, syntax, type }

The input format for the custom tool. Default is unconstrained text.

Text { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar { definition, syntax, type }

A grammar defined by the user.

definition: string

The grammar definition.

syntax: "lark" | "regex"

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: "grammar"

Grammar format. Always `grammar`.

BetaNamespaceTool { description, name, tools, type }

Groups function/custom tools under a shared namespace.

description: string

A description of the namespace shown to the model.

minLength1

name: string

The namespace name used in tool calls (for example, `crm`).

minLength1

tools: Array<Function { name, type, allowed\_callers, 5 more }  | [BetaCustomTool](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_custom_tool%20%3E%20(schema)) { name, type, allowed\_callers, 3 more } >

The function/custom tools available inside this namespace.

Function { name, type, allowed\_callers, 5 more }

name: string

maxLength128

minLength1

type: "function"

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this function should be deferred and discovered via tool search.

description?: string | null

output\_schema?: Record<string, unknown> | null

A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

parameters?: unknown

strict?: boolean | null

Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

BetaCustomTool { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this tool should be deferred and discovered via tool search.

description?: string

Optional description of the custom tool, used to provide more context.

format?: Text { type }  | Grammar { definition, syntax, type }

The input format for the custom tool. Default is unconstrained text.

Text { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar { definition, syntax, type }

A grammar defined by the user.

definition: string

The grammar definition.

syntax: "lark" | "regex"

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: "grammar"

Grammar format. Always `grammar`.

type: "namespace"

The type of the tool. Always `namespace`.

BetaToolSearchTool { type, description, execution, parameters }

Hosted or BYOT tool search configuration for deferred tools.

type: "tool\_search"

The type of the tool. Always `tool_search`.

description?: string | null

Description shown to the model for a client-executed tool search tool.

execution?: "server" | "client"

Whether tool search is executed by the server or by the client.

"server"

"client"

parameters?: unknown

Parameter schema for a client-executed tool search tool.

BetaWebSearchPreviewTool { type, search\_content\_types, search\_context\_size, user\_location }

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: "web\_search\_preview" | "web\_search\_preview\_2025\_03\_11"

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types?: Array<"text" | "image">

"text"

"image"

search\_context\_size?: "low" | "medium" | "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

"low"

"medium"

"high"

user\_location?: UserLocation | null

The user’s location.

type: "approximate"

The type of location approximation. Always `approximate`.

city?: string | null

Free text input for the city of the user, e.g. `San Francisco`.

country?: string | null

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region?: string | null

Free text input for the region of the user, e.g. `California`.

timezone?: string | null

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

BetaApplyPatchTool { type, allowed\_callers }

Allows the assistant to create, delete, or update files using unified diffs.

type: "apply\_patch"

The type of the tool. Always `apply_patch`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

type: "tool\_search\_output"

The type of the item. Always `tool_search_output`.

agent?: Agent { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

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

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

name: string

The name of the function to call.

parameters: Record<string, unknown> | null

A JSON schema object describing the parameters of the function.

strict: boolean | null

Whether strict parameter validation is enforced for this function tool.

type: "function"

The type of the function tool. Always `function`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this function is deferred and loaded via tool search.

description?: string | null

A description of the function. Used by the model to determine whether or not to call the function.

output\_schema?: Record<string, unknown> | null

A JSON schema object describing the JSON value encoded in string outputs for this function.

BetaFileSearchTool { type, vector\_store\_ids, filters, 2 more }

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

type: "file\_search"

The type of the file search tool. Always `file_search`.

vector\_store\_ids: Array<string>

The IDs of the vector stores to search.

filters?: ComparisonFilter { key, type, value }  | CompoundFilter { filters, type }  | null

A filter to apply.

ComparisonFilter { key, type, value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: string

The key to compare against the value.

type: "eq" | "ne" | "gt" | 5 more

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: string | number | boolean | Array<string | number>

The value to compare against the attribute key; supports string, number, or boolean types.

string

number

boolean

Array<string | number>

string

number

CompoundFilter { filters, type }

Combine multiple filters using `and` or `or`.

filters: Array<ComparisonFilter { key, type, value }  | unknown>

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

ComparisonFilter { key, type, value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: string

The key to compare against the value.

type: "eq" | "ne" | "gt" | 5 more

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: string | number | boolean | Array<string | number>

The value to compare against the attribute key; supports string, number, or boolean types.

string

number

boolean

Array<string | number>

string

number

unknown

type: "and" | "or"

Type of operation: `and` or `or`.

"and"

"or"

max\_num\_results?: number

The maximum number of results to return. This number should be between 1 and 50 inclusive.

ranking\_options?: RankingOptions { hybrid\_search, ranker, score\_threshold }

Ranking options for search.

hybrid\_search?: HybridSearch { embedding\_weight, text\_weight }

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

embedding\_weight: number

The weight of the embedding in the reciprocal ranking fusion.

text\_weight: number

The weight of the text in the reciprocal ranking fusion.

ranker?: "auto" | "default-2024-11-15"

The ranker to use for the file search.

"auto"

"default-2024-11-15"

score\_threshold?: number

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

BetaComputerTool { type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

type: "computer"

The type of the computer tool. Always `computer`.

BetaComputerUsePreviewTool { display\_height, display\_width, environment, type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

display\_height: number

The height of the computer display.

display\_width: number

The width of the computer display.

environment: "windows" | "mac" | "linux" | 2 more

The type of computer environment to control.

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: "computer\_use\_preview"

The type of the computer use tool. Always `computer_use_preview`.

BetaWebSearchTool { type, filters, search\_context\_size, user\_location }

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: "web\_search" | "web\_search\_2025\_08\_26"

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

"web\_search"

"web\_search\_2025\_08\_26"

filters?: Filters | null

Filters for the search.

allowed\_domains?: Array<string> | null

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

search\_context\_size?: "low" | "medium" | "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

"low"

"medium"

"high"

user\_location?: UserLocation | null

The approximate location of the user.

city?: string | null

Free text input for the city of the user, e.g. `San Francisco`.

country?: string | null

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region?: string | null

Free text input for the region of the user, e.g. `California`.

timezone?: string | null

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

type?: "approximate"

The type of location approximation. Always `approximate`.

Mcp { server\_label, type, allowed\_callers, 9 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: string

A label for this MCP server, used to identify it in tool calls.

type: "mcp"

The type of the MCP tool. Always `mcp`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

allowed\_tools?: Array<string> | McpToolFilter { read\_only, tool\_names }  | null

List of allowed tool names or a filter object.

Array<string>

McpToolFilter { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

authorization?: string

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

connector\_id?: "connector\_dropbox" | "connector\_gmail" | "connector\_googlecalendar" | 5 more

Identifier for service connectors, like those available in ChatGPT. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided. Learn more
about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

Currently supported `connector_id` values are:

* Dropbox: `connector_dropbox`
* Gmail: `connector_gmail`
* Google Calendar: `connector_googlecalendar`
* Google Drive: `connector_googledrive`
* Microsoft Teams: `connector_microsoftteams`
* Outlook Calendar: `connector_outlookcalendar`
* Outlook Email: `connector_outlookemail`
* SharePoint: `connector_sharepoint`

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading?: boolean

Whether this MCP tool is deferred and discovered via tool search.

headers?: Record<string, string> | null

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

require\_approval?: McpToolApprovalFilter { always, never }  | "always" | "never" | null

Specify which of the MCP server’s tools require approval.

McpToolApprovalFilter { always, never }

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

always?: Always { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

never?: Never { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

"always" | "never"

"always"

"never"

server\_description?: string

Optional description of the MCP server, used to provide more context.

server\_url?: string

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

tunnel\_id?: string

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

CodeInterpreter { container, type, allowed\_callers }

A tool that runs Python code to help generate a response to a prompt.

container: string | CodeInterpreterToolAuto { type, file\_ids, memory\_limit, network\_policy }

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

string

CodeInterpreterToolAuto { type, file\_ids, memory\_limit, network\_policy }

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

type: "auto"

Always `auto`.

file\_ids?: Array<string>

An optional list of uploaded files to make available to your code.

memory\_limit?: "1g" | "4g" | "16g" | "64g" | null

The memory limit for the code interpreter container.

"1g"

"4g"

"16g"

"64g"

network\_policy?: [BetaContainerNetworkPolicyDisabled](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  | [BetaContainerNetworkPolicyAllowlist](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

BetaContainerNetworkPolicyDisabled { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

BetaContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array<string>

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets?: Array<[BetaContainerNetworkPolicyDomainSecret](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } >

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

minLength1

name: string

The name of the secret to inject for the domain.

minLength1

value: string

The secret value to inject for the domain.

maxLength10485760

minLength1

type: "code\_interpreter"

The type of the code interpreter tool. Always `code_interpreter`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

ProgrammaticToolCalling { type }

type: "programmatic\_tool\_calling"

The type of the tool. Always `programmatic_tool_calling`.

ImageGeneration { type, action, background, 9 more }

A tool that generates images using the GPT image models.

type: "image\_generation"

The type of the image generation tool. Always `image_generation`.

action?: "generate" | "edit" | "auto"

Whether to generate a new image or edit an existing image. Default: `auto`.

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

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

"high"

"low"

input\_image\_mask?: InputImageMask { file\_id, image\_url }

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

file\_id?: string

File ID for the mask image.

image\_url?: string

Base64-encoded mask image.

model?: (string & {}) | "gpt-image-1" | "gpt-image-1-mini" | "gpt-image-2" | 3 more

The image generation model to use. Default: `gpt-image-1`.

(string & {})

"gpt-image-1" | "gpt-image-1-mini" | "gpt-image-2" | 3 more

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation?: "auto" | "low"

Moderation level for the generated image. Default: `auto`.

"auto"

"low"

output\_compression?: number

Compression level for the output image. Default: 100.

minimum0

maximum100

output\_format?: "png" | "webp" | "jpeg"

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

"png"

"webp"

"jpeg"

partial\_images?: number

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

quality?: "low" | "medium" | "high" | "auto"

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

"low"

"medium"

"high"

"auto"

size?: (string & {}) | "1024x1024" | "1024x1536" | "1536x1024" | "auto"

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

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

A tool that allows the model to execute shell commands.

type: "shell"

The type of the shell tool. Always `shell`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

environment?: [BetaContainerAuto](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_auto%20%3E%20(schema)) { type, file\_ids, memory\_limit, 2 more }  | [BetaLocalEnvironment](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_environment%20%3E%20(schema)) { type, skills }  | [BetaContainerReference](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_reference%20%3E%20(schema)) { container\_id, type }  | null

BetaContainerAuto { type, file\_ids, memory\_limit, 2 more }

type: "container\_auto"

Automatically creates a container for this request

file\_ids?: Array<string>

An optional list of uploaded files to make available to your code.

memory\_limit?: "1g" | "4g" | "16g" | "64g" | null

The memory limit for the container.

"1g"

"4g"

"16g"

"64g"

network\_policy?: [BetaContainerNetworkPolicyDisabled](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  | [BetaContainerNetworkPolicyAllowlist](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

BetaContainerNetworkPolicyDisabled { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

BetaContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array<string>

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets?: Array<[BetaContainerNetworkPolicyDomainSecret](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } >

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

minLength1

name: string

The name of the secret to inject for the domain.

minLength1

value: string

The secret value to inject for the domain.

maxLength10485760

minLength1

skills?: Array<[BetaSkillReference](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_skill_reference%20%3E%20(schema)) { skill\_id, type, version }  | [BetaInlineSkill](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill%20%3E%20(schema)) { description, name, source, type } >

An optional list of skills referenced by id or inline data.

BetaSkillReference { skill\_id, type, version }

skill\_id: string

The ID of the referenced skill.

maxLength64

minLength1

type: "skill\_reference"

References a skill created with the /v1/skills endpoint.

version?: string

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

BetaInlineSkill { description, name, source, type }

description: string

The description of the skill.

name: string

The name of the skill.

source: [BetaInlineSkillSource](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema)) { data, media\_type, type }

Inline skill payload

data: string

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

media\_type: "application/zip"

The media type of the inline skill payload. Must be `application/zip`.

type: "base64"

The type of the inline skill source. Must be `base64`.

type: "inline"

Defines an inline skill for this request.

BetaLocalEnvironment { type, skills }

type: "local"

Use a local computer environment.

skills?: Array<[BetaLocalSkill](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema)) { description, name, path } >

An optional list of skills.

description: string

The description of the skill.

name: string

The name of the skill.

path: string

The path to the directory containing the skill.

BetaContainerReference { container\_id, type }

container\_id: string

The ID of the referenced container.

type: "container\_reference"

References a container created with the /v1/containers endpoint

BetaCustomTool { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this tool should be deferred and discovered via tool search.

description?: string

Optional description of the custom tool, used to provide more context.

format?: Text { type }  | Grammar { definition, syntax, type }

The input format for the custom tool. Default is unconstrained text.

Text { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar { definition, syntax, type }

A grammar defined by the user.

definition: string

The grammar definition.

syntax: "lark" | "regex"

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: "grammar"

Grammar format. Always `grammar`.

BetaNamespaceTool { description, name, tools, type }

Groups function/custom tools under a shared namespace.

description: string

A description of the namespace shown to the model.

minLength1

name: string

The namespace name used in tool calls (for example, `crm`).

minLength1

tools: Array<Function { name, type, allowed\_callers, 5 more }  | [BetaCustomTool](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_custom_tool%20%3E%20(schema)) { name, type, allowed\_callers, 3 more } >

The function/custom tools available inside this namespace.

Function { name, type, allowed\_callers, 5 more }

name: string

maxLength128

minLength1

type: "function"

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this function should be deferred and discovered via tool search.

description?: string | null

output\_schema?: Record<string, unknown> | null

A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

parameters?: unknown

strict?: boolean | null

Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

BetaCustomTool { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this tool should be deferred and discovered via tool search.

description?: string

Optional description of the custom tool, used to provide more context.

format?: Text { type }  | Grammar { definition, syntax, type }

The input format for the custom tool. Default is unconstrained text.

Text { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar { definition, syntax, type }

A grammar defined by the user.

definition: string

The grammar definition.

syntax: "lark" | "regex"

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: "grammar"

Grammar format. Always `grammar`.

type: "namespace"

The type of the tool. Always `namespace`.

BetaToolSearchTool { type, description, execution, parameters }

Hosted or BYOT tool search configuration for deferred tools.

type: "tool\_search"

The type of the tool. Always `tool_search`.

description?: string | null

Description shown to the model for a client-executed tool search tool.

execution?: "server" | "client"

Whether tool search is executed by the server or by the client.

"server"

"client"

parameters?: unknown

Parameter schema for a client-executed tool search tool.

BetaWebSearchPreviewTool { type, search\_content\_types, search\_context\_size, user\_location }

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: "web\_search\_preview" | "web\_search\_preview\_2025\_03\_11"

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types?: Array<"text" | "image">

"text"

"image"

search\_context\_size?: "low" | "medium" | "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

"low"

"medium"

"high"

user\_location?: UserLocation | null

The user’s location.

type: "approximate"

The type of location approximation. Always `approximate`.

city?: string | null

Free text input for the city of the user, e.g. `San Francisco`.

country?: string | null

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region?: string | null

Free text input for the region of the user, e.g. `California`.

timezone?: string | null

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

BetaApplyPatchTool { type, allowed\_callers }

Allows the assistant to create, delete, or update files using unified diffs.

type: "apply\_patch"

The type of the tool. Always `apply_patch`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

type: "additional\_tools"

The type of the item. Always `additional_tools`.

agent?: Agent { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

BetaResponseCompactionItem { id, encrypted\_content, type, 2 more }

A compaction item generated by the [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).

id: string

The unique ID of the compaction item.

encrypted\_content: string

The encrypted content that was produced by compaction.

type: "compaction"

The type of the item. Always `compaction`.

agent?: Agent { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

created\_by?: string

The identifier of the actor that created the item.

ImageGenerationCall { id, result, status, 2 more }

An image generation request made by the model.

id: string

The unique ID of the image generation call.

result: string | null

The generated image encoded in base64.

status: "in\_progress" | "completed" | "generating" | "failed"

The status of the image generation call.

"in\_progress"

"completed"

"generating"

"failed"

type: "image\_generation\_call"

The type of the image generation call. Always `image_generation_call`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

BetaResponseCodeInterpreterToolCall { id, code, container\_id, 4 more }

A tool call to run code.

id: string

The unique ID of the code interpreter tool call.

code: string | null

The code to run, or null if not available.

container\_id: string

The ID of the container used to run the code.

outputs: Array<Logs { logs, type }  | Image { type, url } > | null

The outputs generated by the code interpreter, such as logs or images.
Can be null if no outputs are available.

Logs { logs, type }

The logs output from the code interpreter.

logs: string

The logs output from the code interpreter.

type: "logs"

The type of the output. Always `logs`.

Image { type, url }

The image output from the code interpreter.

type: "image"

The type of the output. Always `image`.

url: string

The URL of the image output from the code interpreter.

formaturi

status: "in\_progress" | "completed" | "incomplete" | 2 more

The status of the code interpreter tool call. Valid values are `in_progress`, `completed`, `incomplete`, `interpreting`, and `failed`.

"in\_progress"

"completed"

"incomplete"

"interpreting"

"failed"

type: "code\_interpreter\_call"

The type of the code interpreter tool call. Always `code_interpreter_call`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

LocalShellCall { id, action, call\_id, 3 more }

A tool call to run a command on the local shell.

id: string

The unique ID of the local shell call.

action: Action { command, env, type, 3 more }

Execute a shell command on the server.

command: Array<string>

The command to run.

env: Record<string, string>

Environment variables to set for the command.

type: "exec"

The type of the local shell action. Always `exec`.

timeout\_ms?: number | null

Optional timeout in milliseconds for the command.

user?: string | null

Optional user to run the command as.
