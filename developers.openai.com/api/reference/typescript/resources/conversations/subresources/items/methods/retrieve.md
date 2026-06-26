<!-- source: https://developers.openai.com/api/reference/typescript/resources/conversations/subresources/items/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Conversations](/api/reference/typescript/resources/conversations)

[Items](/api/reference/typescript/resources/conversations/subresources/items)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve an item

client.conversations.items.retrieve(stringitemID, ItemRetrieveParams { conversation\_id, include } params, RequestOptionsoptions?): [ConversationItem](/api/reference/typescript/resources/conversations#(resource)%20conversations.items%20%3E%20(model)%20conversation_item%20%3E%20(schema))

GET/conversations/{conversation\_id}/items/{item\_id}

Get a single item from a conversation with the given IDs.

##### ParametersExpand Collapse

itemID: string

params: ItemRetrieveParams { conversation\_id, include }

conversation\_id: string

Path param: The ID of the conversation that contains the item.

include?: Array<[ResponseIncludable](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_includable%20%3E%20(schema))>

Query param: Additional fields to include in the response. See the `include`
parameter for [listing Conversation items above](https://platform.openai.com/docs/api-reference/conversations/list-items#conversations_list_items-include) for more information.

One of the following:

"file\_search\_call.results"

"web\_search\_call.results"

"web\_search\_call.action.sources"

"message.input\_image.image\_url"

"computer\_call\_output.output.image\_url"

"code\_interpreter\_call.outputs"

"reasoning.encrypted\_content"

"message.output\_text.logprobs"

##### ReturnsExpand Collapse

ConversationItem = [Message](/api/reference/typescript/resources/conversations#(resource)%20conversations%20%3E%20(model)%20message%20%3E%20(schema)) { id, content, role, 3 more }  | [ResponseFunctionToolCallItem](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_function_tool_call_item%20%3E%20(schema)) { id, status, created\_by }  | [ResponseFunctionToolCallOutputItem](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_function_tool_call_output_item%20%3E%20(schema)) { id, call\_id, output, 3 more }  | 23 more

A single item within a conversation. The set of possible types are the same as the `output` type of a [Response object](https://platform.openai.com/docs/api-reference/responses/object#responses/object-output).

One of the following:

Message { id, content, role, 3 more }

A message to or from the model.

id: string

The unique ID of the message.

content: Array<[ResponseInputText](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text, type }  | [ResponseOutputText](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_output_text%20%3E%20(schema)) { annotations, text, type, logprobs }  | [TextContent](/api/reference/typescript/resources/conversations#(resource)%20conversations%20%3E%20(model)%20text_content%20%3E%20(schema)) { text, type }  | 6 more>

The content of the message

One of the following:

ResponseInputText { text, type }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

ResponseOutputText { annotations, text, type, logprobs }

A text output from the model.

annotations: Array<FileCitation { file\_id, filename, index, type }  | URLCitation { end\_index, start\_index, title, 2 more }  | ContainerFileCitation { container\_id, end\_index, file\_id, 3 more }  | FilePath { file\_id, index, type } >

The annotations of the text output.

One of the following:

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

TextContent { text, type }

A text content.

text: string

type: "text"

SummaryTextContent { text, type }

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

ResponseOutputRefusal { refusal, type }

A refusal from the model.

refusal: string

The refusal explanation from the model.

type: "refusal"

The type of the refusal. Always `refusal`.

ResponseInputImage { detail, type, file\_id, image\_url }

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: "low" | "high" | "auto" | "original"

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

One of the following:

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

ComputerScreenshotContent { detail, file\_id, image\_url, type }

A screenshot of a computer.

detail: "low" | "high" | "auto" | "original"

The detail level of the screenshot image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

One of the following:

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

ResponseInputFile { type, detail, file\_data, 3 more }

A file input to the model.

type: "input\_file"

The type of the input item. Always `input_file`.

detail?: "low" | "high"

The detail level of the file to be sent to the model. Use `low` for the default rendering behavior, or `high` to render the file at higher quality. Defaults to `low`.

One of the following:

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

role: "unknown" | "user" | "assistant" | 5 more

The role of the message. One of `unknown`, `user`, `assistant`, `system`, `critic`, `discriminator`, `developer`, or `tool`.

One of the following:

"unknown"

"user"

"assistant"

"system"

"critic"

"discriminator"

"developer"

"tool"

status: "in\_progress" | "completed" | "incomplete"

The status of item. One of `in_progress`, `completed`, or `incomplete`. Populated when items are returned via API.

One of the following:

"in\_progress"

"completed"

"incomplete"

type: "message"

The type of the message. Always set to `message`.

phase?: "commentary" | "final\_answer" | null

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`). For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

One of the following:

"commentary"

"final\_answer"

ResponseFunctionToolCallItem extends [ResponseFunctionToolCall](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_function_tool_call%20%3E%20(schema)) { arguments, call\_id, name, 4 more }  { id, status, created\_by }

A tool call to run a function. See the
[function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.

id: string

The unique ID of the function tool call.

status: "in\_progress" | "completed" | "incomplete"

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

One of the following:

"in\_progress"

"completed"

"incomplete"

created\_by?: string

The identifier of the actor that created the item.

ResponseFunctionToolCallOutputItem { id, call\_id, output, 3 more }

id: string

The unique ID of the function call tool output.

call\_id: string

The unique ID of the function tool call generated by the model.

output: string | Array<[ResponseInputText](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text, type }  | [ResponseInputImage](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_image%20%3E%20(schema)) { detail, type, file\_id, image\_url }  | [ResponseInputFile](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_file%20%3E%20(schema)) { type, detail, file\_data, 3 more } >

The output from the function call generated by your code.
Can be a string or an list of output content.

One of the following:

string

Array<[ResponseInputText](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text, type }  | [ResponseInputImage](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_image%20%3E%20(schema)) { detail, type, file\_id, image\_url }  | [ResponseInputFile](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_file%20%3E%20(schema)) { type, detail, file\_data, 3 more } >

ResponseInputText { text, type }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

ResponseInputImage { detail, type, file\_id, image\_url }

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: "low" | "high" | "auto" | "original"

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

One of the following:

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

ResponseInputFile { type, detail, file\_data, 3 more }

A file input to the model.

type: "input\_file"

The type of the input item. Always `input_file`.

detail?: "low" | "high"

The detail level of the file to be sent to the model. Use `low` for the default rendering behavior, or `high` to render the file at higher quality. Defaults to `low`.

One of the following:

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

status: "in\_progress" | "completed" | "incomplete"

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

One of the following:

"in\_progress"

"completed"

"incomplete"

type: "function\_call\_output"

The type of the function tool call output. Always `function_call_output`.

created\_by?: string

The identifier of the actor that created the item.

ResponseFileSearchToolCall { id, queries, status, 2 more }

The results of a file search tool call. See the
[file search guide](https://platform.openai.com/docs/guides/tools-file-search) for more information.

id: string

The unique ID of the file search tool call.

queries: Array<string>

The queries used to search for files.

status: "in\_progress" | "searching" | "completed" | 2 more

The status of the file search tool call. One of `in_progress`,
`searching`, `incomplete` or `failed`,

One of the following:

"in\_progress"

"searching"

"completed"

"incomplete"

"failed"

type: "file\_search\_call"

The type of the file search tool call. Always `file_search_call`.

results?: Array<Result> | null

The results of the file search tool call.

attributes?: Record<string, string | number | boolean> | null

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.

One of the following:

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

ResponseFunctionWebSearch { id, action, status, type }

The results of a web search tool call. See the
[web search guide](https://platform.openai.com/docs/guides/tools-web-search) for more information.

id: string

The unique ID of the web search tool call.

action: Search { type, queries, query, sources }  | OpenPage { type, url }  | FindInPage { pattern, type, url }

An object describing the specific action taken in this web search call.
Includes details on how the model used the web (search, open\_page, find\_in\_page).

One of the following:

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

One of the following:

"in\_progress"

"searching"

"completed"

"failed"

type: "web\_search\_call"

The type of the web search tool call. Always `web_search_call`.

ImageGenerationCall { id, result, status, type }

An image generation request made by the model.

id: string

The unique ID of the image generation call.

result: string | null

The generated image encoded in base64.

status: "in\_progress" | "completed" | "generating" | "failed"

The status of the image generation call.

One of the following:

"in\_progress"

"completed"

"generating"

"failed"

type: "image\_generation\_call"

The type of the image generation call. Always `image_generation_call`.

ResponseComputerToolCall { id, call\_id, pending\_safety\_checks, 4 more }

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

One of the following:

"in\_progress"

"completed"

"incomplete"

type: "computer\_call"

The type of the computer call. Always `computer_call`.

action?: Click { button, type, x, 2 more }  | DoubleClick { keys, type, x, y }  | Drag { path, type, keys }  | 6 more

A click action.

One of the following:

Click { button, type, x, 2 more }

A click action.

button: "left" | "right" | "wheel" | 2 more

Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

One of the following:

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

actions?: [ComputerActionList](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20computer_action_list%20%3E%20(schema)) { , , , 6 more }

Flattened batched actions for `computer_use`. Each action includes an
`type` discriminator and action-specific fields.

One of the following:

Click { button, type, x, 2 more }

A click action.

button: "left" | "right" | "wheel" | 2 more

Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

One of the following:

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

ResponseComputerToolCallOutputItem { id, call\_id, output, 4 more }

id: string

The unique ID of the computer call tool output.

call\_id: string

The ID of the computer tool call that produced the output.

output: [ResponseComputerToolCallOutputScreenshot](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_computer_tool_call_output_screenshot%20%3E%20(schema)) { type, file\_id, image\_url }

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

One of the following:

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

created\_by?: string

The identifier of the actor that created the item.

ResponseToolSearchCall { id, arguments, call\_id, 4 more }

id: string

The unique ID of the tool search call item.

arguments: unknown

Arguments used for the tool search call.

call\_id: string | null

The unique ID of the tool search call generated by the model.

execution: "server" | "client"

Whether tool search was executed by the server or by the client.

One of the following:

"server"

"client"

status: "in\_progress" | "completed" | "incomplete"

The status of the tool search call item that was recorded.

One of the following:

"in\_progress"

"completed"

"incomplete"

type: "tool\_search\_call"

The type of the item. Always `tool_search_call`.

created\_by?: string

The identifier of the actor that created the item.

ResponseToolSearchOutputItem { id, call\_id, execution, 4 more }

id: string

The unique ID of the tool search output item.

call\_id: string | null

The unique ID of the tool search call generated by the model.

execution: "server" | "client"

Whether tool search was executed by the server or by the client.

One of the following:

"server"

"client"

status: "in\_progress" | "completed" | "incomplete"

The status of the tool search output item that was recorded.

One of the following:

"in\_progress"

"completed"

"incomplete"

tools: Array<[Tool](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20tool%20%3E%20(schema))>

The loaded tool definitions returned by tool search.

One of the following:

FunctionTool { name, parameters, strict, 3 more }

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

name: string

The name of the function to call.

parameters: Record<string, unknown> | null

A JSON schema object describing the parameters of the function.

strict: boolean | null

Whether to enforce strict parameter validation. Default `true`.

type: "function"

The type of the function tool. Always `function`.

defer\_loading?: boolean

Whether this function is deferred and loaded via tool search.

description?: string | null

A description of the function. Used by the model to determine whether or not to call the function.

FileSearchTool { type, vector\_store\_ids, filters, 2 more }

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

type: "file\_search"

The type of the file search tool. Always `file_search`.

vector\_store\_ids: Array<string>

The IDs of the vector stores to search.

filters?: [ComparisonFilter](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)) { key, type, value }  | [CompoundFilter](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20compound_filter%20%3E%20(schema)) { filters, type }  | null

A filter to apply.

One of the following:

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

One of the following:

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

One of the following:

string

number

boolean

Array<string | number>

string

number

CompoundFilter { filters, type }

Combine multiple filters using `and` or `or`.

filters: Array<[ComparisonFilter](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)) { key, type, value }  | unknown>

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

One of the following:

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

One of the following:

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

One of the following:

string

number

boolean

Array<string | number>

string

number

unknown

type: "and" | "or"

Type of operation: `and` or `or`.

One of the following:

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

One of the following:

"auto"

"default-2024-11-15"

score\_threshold?: number

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

ComputerTool { type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

type: "computer"

The type of the computer tool. Always `computer`.

ComputerUsePreviewTool { display\_height, display\_width, environment, type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

display\_height: number

The height of the computer display.

display\_width: number

The width of the computer display.

environment: "windows" | "mac" | "linux" | 2 more

The type of computer environment to control.

One of the following:

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: "computer\_use\_preview"

The type of the computer use tool. Always `computer_use_preview`.

WebSearchTool { type, filters, search\_context\_size, user\_location }

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: "web\_search" | "web\_search\_2025\_08\_26"

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

One of the following:

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

One of the following:

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

Mcp { server\_label, type, allowed\_tools, 8 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: string

A label for this MCP server, used to identify it in tool calls.

type: "mcp"

The type of the MCP tool. Always `mcp`.

allowed\_tools?: Array<string> | McpToolFilter { read\_only, tool\_names }  | null

List of allowed tool names or a filter object.

One of the following:

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

One of the following:

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

One of the following:

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

CodeInterpreter { container, type }

A tool that runs Python code to help generate a response to a prompt.

container: string | CodeInterpreterToolAuto { type, file\_ids, memory\_limit, network\_policy }

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

One of the following:

string

CodeInterpreterToolAuto { type, file\_ids, memory\_limit, network\_policy }

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

type: "auto"

Always `auto`.

file\_ids?: Array<string>

An optional list of uploaded files to make available to your code.

memory\_limit?: "1g" | "4g" | "16g" | "64g" | null

The memory limit for the code interpreter container.

One of the following:

"1g"

"4g"

"16g"

"64g"

network\_policy?: [ContainerNetworkPolicyDisabled](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_disabled%20%3E%20(schema)) { type }  | [ContainerNetworkPolicyAllowlist](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

One of the following:

ContainerNetworkPolicyDisabled { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

ContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array<string>

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets?: Array<[ContainerNetworkPolicyDomainSecret](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } >

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

ImageGeneration { type, action, background, 9 more }

A tool that generates images using the GPT image models.

type: "image\_generation"

The type of the image generation tool. Always `image_generation`.

action?: "generate" | "edit" | "auto"

Whether to generate a new image or edit an existing image. Default: `auto`.

One of the following:

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

One of the following:

"transparent"

"opaque"

"auto"

input\_fidelity?: "high" | "low" | null

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

One of the following:

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

One of the following:

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

One of the following:

"auto"

"low"

output\_compression?: number

Compression level for the output image. Default: 100.

minimum0

maximum100

output\_format?: "png" | "webp" | "jpeg"

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

One of the following:

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

One of the following:

"low"

"medium"

"high"

"auto"

size?: (string & {}) | "1024x1024" | "1024x1536" | "1536x1024" | "auto"

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

One of the following:

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

FunctionShellTool { type, environment }

A tool that allows the model to execute shell commands.

type: "shell"

The type of the shell tool. Always `shell`.

environment?: [ContainerAuto](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20container_auto%20%3E%20(schema)) { type, file\_ids, memory\_limit, 2 more }  | [LocalEnvironment](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20local_environment%20%3E%20(schema)) { type, skills }  | [ContainerReference](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20container_reference%20%3E%20(schema)) { container\_id, type }  | null

One of the following:

ContainerAuto { type, file\_ids, memory\_limit, 2 more }

type: "container\_auto"

Automatically creates a container for this request

file\_ids?: Array<string>

An optional list of uploaded files to make available to your code.

memory\_limit?: "1g" | "4g" | "16g" | "64g" | null

The memory limit for the container.

One of the following:

"1g"

"4g"

"16g"

"64g"

network\_policy?: [ContainerNetworkPolicyDisabled](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_disabled%20%3E%20(schema)) { type }  | [ContainerNetworkPolicyAllowlist](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

One of the following:

ContainerNetworkPolicyDisabled { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

ContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array<string>

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets?: Array<[ContainerNetworkPolicyDomainSecret](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } >

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

skills?: Array<[SkillReference](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20skill_reference%20%3E%20(schema)) { skill\_id, type, version }  | [InlineSkill](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill%20%3E%20(schema)) { description, name, source, type } >

An optional list of skills referenced by id or inline data.

One of the following:

SkillReference { skill\_id, type, version }

skill\_id: string

The ID of the referenced skill.

maxLength64

minLength1

type: "skill\_reference"

References a skill created with the /v1/skills endpoint.

version?: string

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

InlineSkill { description, name, source, type }

description: string

The description of the skill.

name: string

The name of the skill.

source: [InlineSkillSource](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill_source%20%3E%20(schema)) { data, media\_type, type }

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

LocalEnvironment { type, skills }

type: "local"

Use a local computer environment.

skills?: Array<[LocalSkill](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20local_skill%20%3E%20(schema)) { description, name, path } >

An optional list of skills.

description: string

The description of the skill.

name: string

The name of the skill.

path: string

The path to the directory containing the skill.

ContainerReference { container\_id, type }

container\_id: string

The ID of the referenced container.

type: "container\_reference"

References a container created with the /v1/containers endpoint

CustomTool { name, type, defer\_loading, 2 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

defer\_loading?: boolean

Whether this tool should be deferred and discovered via tool search.

description?: string

Optional description of the custom tool, used to provide more context.

format?: [CustomToolInputFormat](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))

The input format for the custom tool. Default is unconstrained text.

One of the following:

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

One of the following:

"lark"

"regex"

type: "grammar"

Grammar format. Always `grammar`.

NamespaceTool { description, name, tools, type }

Groups function/custom tools under a shared namespace.

description: string

A description of the namespace shown to the model.

minLength1

name: string

The namespace name used in tool calls (for example, `crm`).

minLength1

tools: Array<Function { name, type, defer\_loading, 3 more }  | [CustomTool](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20custom_tool%20%3E%20(schema)) { name, type, defer\_loading, 2 more } >

The function/custom tools available inside this namespace.

One of the following:

Function { name, type, defer\_loading, 3 more }

name: string

maxLength128

minLength1

type: "function"

defer\_loading?: boolean

Whether this function should be deferred and discovered via tool search.

description?: string | null

parameters?: unknown

strict?: boolean | null

CustomTool { name, type, defer\_loading, 2 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

defer\_loading?: boolean

Whether this tool should be deferred and discovered via tool search.

description?: string

Optional description of the custom tool, used to provide more context.

format?: [CustomToolInputFormat](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))

The input format for the custom tool. Default is unconstrained text.

One of the following:

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

One of the following:

"lark"

"regex"

type: "grammar"

Grammar format. Always `grammar`.

type: "namespace"

The type of the tool. Always `namespace`.

ToolSearchTool { type, description, execution, parameters }

Hosted or BYOT tool search configuration for deferred tools.

type: "tool\_search"

The type of the tool. Always `tool_search`.

description?: string | null

Description shown to the model for a client-executed tool search tool.

execution?: "server" | "client"

Whether tool search is executed by the server or by the client.

One of the following:

"server"

"client"

parameters?: unknown

Parameter schema for a client-executed tool search tool.

WebSearchPreviewTool { type, search\_content\_types, search\_context\_size, user\_location }

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: "web\_search\_preview" | "web\_search\_preview\_2025\_03\_11"

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

One of the following:

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types?: Array<"text" | "image">

One of the following:

"text"

"image"

search\_context\_size?: "low" | "medium" | "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

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

ApplyPatchTool { type }

Allows the assistant to create, delete, or update files using unified diffs.

type: "apply\_patch"

The type of the tool. Always `apply_patch`.

type: "tool\_search\_output"

The type of the item. Always `tool_search_output`.

created\_by?: string

The identifier of the actor that created the item.

AdditionalTools { id, role, tools, type }

id: string

The unique ID of the additional tools item.

role: "unknown" | "user" | "assistant" | 5 more

The role that provided the additional tools.

One of the following:

"unknown"

"user"

"assistant"

"system"

"critic"

"discriminator"

"developer"

"tool"

tools: Array<[Tool](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20tool%20%3E%20(schema))>

The additional tool definitions made available at this item.

One of the following:

FunctionTool { name, parameters, strict, 3 more }

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

name: string

The name of the function to call.

parameters: Record<string, unknown> | null

A JSON schema object describing the parameters of the function.

strict: boolean | null

Whether to enforce strict parameter validation. Default `true`.

type: "function"

The type of the function tool. Always `function`.

defer\_loading?: boolean

Whether this function is deferred and loaded via tool search.

description?: string | null

A description of the function. Used by the model to determine whether or not to call the function.

FileSearchTool { type, vector\_store\_ids, filters, 2 more }

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

type: "file\_search"

The type of the file search tool. Always `file_search`.

vector\_store\_ids: Array<string>

The IDs of the vector stores to search.

filters?: [ComparisonFilter](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)) { key, type, value }  | [CompoundFilter](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20compound_filter%20%3E%20(schema)) { filters, type }  | null

A filter to apply.

One of the following:

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

One of the following:

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

One of the following:

string

number

boolean

Array<string | number>

string

number

CompoundFilter { filters, type }

Combine multiple filters using `and` or `or`.

filters: Array<[ComparisonFilter](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)) { key, type, value }  | unknown>

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

One of the following:

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

One of the following:

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

One of the following:

string

number

boolean

Array<string | number>

string

number

unknown

type: "and" | "or"

Type of operation: `and` or `or`.

One of the following:

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

One of the following:

"auto"

"default-2024-11-15"

score\_threshold?: number

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

ComputerTool { type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

type: "computer"

The type of the computer tool. Always `computer`.

ComputerUsePreviewTool { display\_height, display\_width, environment, type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

display\_height: number

The height of the computer display.

display\_width: number

The width of the computer display.

environment: "windows" | "mac" | "linux" | 2 more

The type of computer environment to control.

One of the following:

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: "computer\_use\_preview"

The type of the computer use tool. Always `computer_use_preview`.

WebSearchTool { type, filters, search\_context\_size, user\_location }

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: "web\_search" | "web\_search\_2025\_08\_26"

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

One of the following:

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

One of the following:

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

Mcp { server\_label, type, allowed\_tools, 8 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: string

A label for this MCP server, used to identify it in tool calls.

type: "mcp"

The type of the MCP tool. Always `mcp`.

allowed\_tools?: Array<string> | McpToolFilter { read\_only, tool\_names }  | null

List of allowed tool names or a filter object.

One of the following:

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

One of the following:

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

One of the following:

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

CodeInterpreter { container, type }

A tool that runs Python code to help generate a response to a prompt.

container: string | CodeInterpreterToolAuto { type, file\_ids, memory\_limit, network\_policy }

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

One of the following:

string

CodeInterpreterToolAuto { type, file\_ids, memory\_limit, network\_policy }

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

type: "auto"

Always `auto`.

file\_ids?: Array<string>

An optional list of uploaded files to make available to your code.

memory\_limit?: "1g" | "4g" | "16g" | "64g" | null

The memory limit for the code interpreter container.

One of the following:

"1g"

"4g"

"16g"

"64g"

network\_policy?: [ContainerNetworkPolicyDisabled](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_disabled%20%3E%20(schema)) { type }  | [ContainerNetworkPolicyAllowlist](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

One of the following:

ContainerNetworkPolicyDisabled { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

ContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array<string>

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets?: Array<[ContainerNetworkPolicyDomainSecret](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } >

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

ImageGeneration { type, action, background, 9 more }

A tool that generates images using the GPT image models.

type: "image\_generation"

The type of the image generation tool. Always `image_generation`.

action?: "generate" | "edit" | "auto"

Whether to generate a new image or edit an existing image. Default: `auto`.

One of the following:

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

One of the following:

"transparent"

"opaque"

"auto"

input\_fidelity?: "high" | "low" | null

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

One of the following:

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

One of the following:

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

One of the following:

"auto"

"low"

output\_compression?: number

Compression level for the output image. Default: 100.

minimum0

maximum100

output\_format?: "png" | "webp" | "jpeg"

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

One of the following:

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

One of the following:

"low"

"medium"

"high"

"auto"

size?: (string & {}) | "1024x1024" | "1024x1536" | "1536x1024" | "auto"

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

One of the following:

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

FunctionShellTool { type, environment }

A tool that allows the model to execute shell commands.

type: "shell"

The type of the shell tool. Always `shell`.

environment?: [ContainerAuto](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20container_auto%20%3E%20(schema)) { type, file\_ids, memory\_limit, 2 more }  | [LocalEnvironment](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20local_environment%20%3E%20(schema)) { type, skills }  | [ContainerReference](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20container_reference%20%3E%20(schema)) { container\_id, type }  | null

One of the following:

ContainerAuto { type, file\_ids, memory\_limit, 2 more }

type: "container\_auto"

Automatically creates a container for this request

file\_ids?: Array<string>

An optional list of uploaded files to make available to your code.

memory\_limit?: "1g" | "4g" | "16g" | "64g" | null

The memory limit for the container.

One of the following:

"1g"

"4g"

"16g"

"64g"

network\_policy?: [ContainerNetworkPolicyDisabled](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_disabled%20%3E%20(schema)) { type }  | [ContainerNetworkPolicyAllowlist](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

One of the following:

ContainerNetworkPolicyDisabled { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

ContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array<string>

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets?: Array<[ContainerNetworkPolicyDomainSecret](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } >

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

skills?: Array<[SkillReference](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20skill_reference%20%3E%20(schema)) { skill\_id, type, version }  | [InlineSkill](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill%20%3E%20(schema)) { description, name, source, type } >

An optional list of skills referenced by id or inline data.

One of the following:

SkillReference { skill\_id, type, version }

skill\_id: string

The ID of the referenced skill.

maxLength64

minLength1

type: "skill\_reference"

References a skill created with the /v1/skills endpoint.

version?: string

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

InlineSkill { description, name, source, type }

description: string

The description of the skill.

name: string

The name of the skill.

source: [InlineSkillSource](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill_source%20%3E%20(schema)) { data, media\_type, type }

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

LocalEnvironment { type, skills }

type: "local"

Use a local computer environment.

skills?: Array<[LocalSkill](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20local_skill%20%3E%20(schema)) { description, name, path } >

An optional list of skills.

description: string

The description of the skill.

name: string

The name of the skill.

path: string

The path to the directory containing the skill.

ContainerReference { container\_id, type }

container\_id: string

The ID of the referenced container.

type: "container\_reference"

References a container created with the /v1/containers endpoint

CustomTool { name, type, defer\_loading, 2 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

defer\_loading?: boolean

Whether this tool should be deferred and discovered via tool search.

description?: string

Optional description of the custom tool, used to provide more context.

format?: [CustomToolInputFormat](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))

The input format for the custom tool. Default is unconstrained text.

One of the following:

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

One of the following:

"lark"

"regex"

type: "grammar"

Grammar format. Always `grammar`.

NamespaceTool { description, name, tools, type }

Groups function/custom tools under a shared namespace.

description: string

A description of the namespace shown to the model.

minLength1

name: string

The namespace name used in tool calls (for example, `crm`).

minLength1

tools: Array<Function { name, type, defer\_loading, 3 more }  | [CustomTool](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20custom_tool%20%3E%20(schema)) { name, type, defer\_loading, 2 more } >

The function/custom tools available inside this namespace.

One of the following:

Function { name, type, defer\_loading, 3 more }

name: string

maxLength128

minLength1

type: "function"

defer\_loading?: boolean

Whether this function should be deferred and discovered via tool search.

description?: string | null

parameters?: unknown

strict?: boolean | null

CustomTool { name, type, defer\_loading, 2 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

defer\_loading?: boolean

Whether this tool should be deferred and discovered via tool search.

description?: string

Optional description of the custom tool, used to provide more context.

format?: [CustomToolInputFormat](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))

The input format for the custom tool. Default is unconstrained text.

One of the following:

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

One of the following:

"lark"

"regex"

type: "grammar"

Grammar format. Always `grammar`.

type: "namespace"

The type of the tool. Always `namespace`.

ToolSearchTool { type, description, execution, parameters }

Hosted or BYOT tool search configuration for deferred tools.

type: "tool\_search"

The type of the tool. Always `tool_search`.

description?: string | null

Description shown to the model for a client-executed tool search tool.

execution?: "server" | "client"

Whether tool search is executed by the server or by the client.

One of the following:

"server"

"client"

parameters?: unknown

Parameter schema for a client-executed tool search tool.

WebSearchPreviewTool { type, search\_content\_types, search\_context\_size, user\_location }

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: "web\_search\_preview" | "web\_search\_preview\_2025\_03\_11"

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

One of the following:

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types?: Array<"text" | "image">

One of the following:

"text"

"image"

search\_context\_size?: "low" | "medium" | "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

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

ApplyPatchTool { type }

Allows the assistant to create, delete, or update files using unified diffs.

type: "apply\_patch"

The type of the tool. Always `apply_patch`.

type: "additional\_tools"

The type of the item. Always `additional_tools`.

ResponseReasoningItem { id, summary, type, 3 more }

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

content?: Array<Content>

Reasoning text content.

text: string

The reasoning text from the model.

type: "reasoning\_text"

The type of the reasoning text. Always `reasoning_text`.

encrypted\_content?: string | null

The encrypted content of the reasoning item - populated when a response is
generated with `reasoning.encrypted_content` in the `include` parameter.

status?: "in\_progress" | "completed" | "incomplete"

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

One of the following:

"in\_progress"

"completed"

"incomplete"

ResponseCompactionItem { id, encrypted\_content, type, created\_by }

A compaction item generated by the [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).

id: string

The unique ID of the compaction item.

encrypted\_content: string

The encrypted content that was produced by compaction.

type: "compaction"

The type of the item. Always `compaction`.

created\_by?: string

The identifier of the actor that created the item.

ResponseCodeInterpreterToolCall { id, code, container\_id, 3 more }

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

One of the following:

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

One of the following:

"in\_progress"

"completed"

"incomplete"

"interpreting"

"failed"

type: "code\_interpreter\_call"

The type of the code interpreter tool call. Always `code_interpreter_call`.

LocalShellCall { id, action, call\_id, 2 more }

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

One of the following:

"in\_progress"

"completed"

"incomplete"

type: "local\_shell\_call"

The type of the local shell call. Always `local_shell_call`.

LocalShellCallOutput { id, output, type, status }

The output of a local shell tool call.

id: string

The unique ID of the local shell tool call generated by the model.

output: string

A JSON string of the output of the local shell tool call.

type: "local\_shell\_call\_output"

The type of the local shell tool call output. Always `local_shell_call_output`.

status?: "in\_progress" | "completed" | "incomplete" | null

The status of the item. One of `in_progress`, `completed`, or `incomplete`.

One of the following:

"in\_progress"

"completed"

"incomplete"

ResponseFunctionShellToolCall { id, action, call\_id, 4 more }

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

environment: [ResponseLocalEnvironment](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_local_environment%20%3E%20(schema)) { type }  | [ResponseContainerReference](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_container_reference%20%3E%20(schema)) { container\_id, type }  | null

Represents the use of a local environment to perform shell actions.

One of the following:

ResponseLocalEnvironment { type }

Represents the use of a local environment to perform shell actions.

type: "local"

The environment type. Always `local`.

ResponseContainerReference { container\_id, type }

Represents a container created with /v1/containers.

container\_id: string

type: "container\_reference"

The environment type. Always `container_reference`.

status: "in\_progress" | "completed" | "incomplete"

The status of the shell call. One of `in_progress`, `completed`, or `incomplete`.

One of the following:

"in\_progress"

"completed"

"incomplete"

type: "shell\_call"

The type of the item. Always `shell_call`.

created\_by?: string

The ID of the entity that created this tool call.

ResponseFunctionShellToolCallOutput { id, call\_id, max\_output\_length, 4 more }

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

One of the following:

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

One of the following:

"in\_progress"

"completed"

"incomplete"

type: "shell\_call\_output"

The type of the shell call output. Always `shell_call_output`.

created\_by?: string

The identifier of the actor that created the item.

ResponseApplyPatchToolCall { id, call\_id, operation, 3 more }

A tool call that applies file diffs by creating, deleting, or updating files.

id: string

The unique ID of the apply patch tool call. Populated when this item is returned via API.

call\_id: string

The unique ID of the apply patch tool call generated by the model.

operation: CreateFile { diff, path, type }  | DeleteFile { path, type }  | UpdateFile { diff, path, type }

One of the create\_file, delete\_file, or update\_file operations applied via apply\_patch.

One of the following:

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

One of the following:

"in\_progress"

"completed"

type: "apply\_patch\_call"

The type of the item. Always `apply_patch_call`.

created\_by?: string

The ID of the entity that created this tool call.

ResponseApplyPatchToolCallOutput { id, call\_id, status, 3 more }

The output emitted by an apply patch tool call.

id: string

The unique ID of the apply patch tool call output. Populated when this item is returned via API.

call\_id: string

The unique ID of the apply patch tool call generated by the model.

status: "completed" | "failed"

The status of the apply patch tool call output. One of `completed` or `failed`.

One of the following:

"completed"

"failed"

type: "apply\_patch\_call\_output"

The type of the item. Always `apply_patch_call_output`.

created\_by?: string

The ID of the entity that created this tool call output.

output?: string | null

Optional textual output returned by the apply patch tool.

McpListTools { id, server\_label, tools, 2 more }

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

error?: string | null

Error message if the server could not list tools.

McpApprovalRequest { id, arguments, name, 2 more }

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

McpApprovalResponse { id, approval\_request\_id, approve, 2 more }

A response to an MCP approval request.

id: string

The unique ID of the approval response

approval\_request\_id: string

The ID of the approval request being answered.

approve: boolean

Whether the request was approved.

type: "mcp\_approval\_response"

The type of the item. Always `mcp_approval_response`.

reason?: string | null

Optional reason for the decision.

McpCall { id, arguments, name, 6 more }

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

approval\_request\_id?: string | null

Unique identifier for the MCP tool call approval request.
Include this value in a subsequent `mcp_approval_response` input to approve or reject the corresponding tool call.

error?: string | null

The error from the tool call, if any.

output?: string | null

The output from the tool call.

status?: "in\_progress" | "completed" | "incomplete" | 2 more

The status of the tool call. One of `in_progress`, `completed`, `incomplete`, `calling`, or `failed`.

One of the following:

"in\_progress"

"completed"

"incomplete"

"calling"

"failed"

ResponseCustomToolCall { call\_id, input, name, 3 more }

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

namespace?: string

The namespace of the custom tool being called.

ResponseCustomToolCallOutput { call\_id, output, type, id }

The output of a custom tool call from your code, being sent back to the model.

call\_id: string

The call ID, used to map this custom tool call output to a custom tool call.

output: string | Array<[ResponseInputText](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text, type }  | [ResponseInputImage](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_image%20%3E%20(schema)) { detail, type, file\_id, image\_url }  | [ResponseInputFile](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_file%20%3E%20(schema)) { type, detail, file\_data, 3 more } >

The output from the custom tool call generated by your code.
Can be a string or an list of output content.

One of the following:

string

Array<[ResponseInputText](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text, type }  | [ResponseInputImage](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_image%20%3E%20(schema)) { detail, type, file\_id, image\_url }  | [ResponseInputFile](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_file%20%3E%20(schema)) { type, detail, file\_data, 3 more } >

ResponseInputText { text, type }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

ResponseInputImage { detail, type, file\_id, image\_url }

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: "low" | "high" | "auto" | "original"

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

One of the following:

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

ResponseInputFile { type, detail, file\_data, 3 more }

A file input to the model.

type: "input\_file"

The type of the input item. Always `input_file`.

detail?: "low" | "high"

The detail level of the file to be sent to the model. Use `low` for the default rendering behavior, or `high` to render the file at higher quality. Defaults to `low`.

One of the following:

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

type: "custom\_tool\_call\_output"

The type of the custom tool call output. Always `custom_tool_call_output`.

id?: string

The unique ID of the custom tool call output in the OpenAI platform.

### Retrieve an item

TypeScript

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import OpenAI from "openai";
const client = new OpenAI();

const item = await client.conversations.items.retrieve(
  "conv_123",
  "msg_abc"
);
console.log(item);

  "type": "message",
  "id": "msg_abc",
  "status": "completed",
  "role": "user",
  "content": [
    {"type": "input_text", "text": "Hello!"}
  ]

##### Returns Examples

  "type": "message",
  "id": "msg_abc",
  "status": "completed",
  "role": "user",
  "content": [
    {"type": "input_text", "text": "Hello!"}
  ]
