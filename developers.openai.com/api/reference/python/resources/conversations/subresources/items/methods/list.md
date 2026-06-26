<!-- source: https://developers.openai.com/api/reference/python/resources/conversations/subresources/items/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Conversations](/api/reference/python/resources/conversations)

[Items](/api/reference/python/resources/conversations/subresources/items)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List items

conversations.items.list(strconversation\_id, ItemListParams\*\*kwargs)  -> SyncConversationCursorPage[[ConversationItem](/api/reference/python/resources/conversations#(resource)%20conversations.items%20%3E%20(model)%20conversation_item%20%3E%20(schema))]

GET/conversations/{conversation\_id}/items

List all items for a conversation with the given ID.

##### ParametersExpand Collapse

conversation\_id: str

after: Optional[str]

An item ID to list items after, used in pagination.

include: Optional[List[[ResponseIncludable](/api/reference/python/resources/responses#(resource)%20responses%20%3E%20(model)%20response_includable%20%3E%20(schema))]]

Specify additional output data to include in the model response. Currently supported values are:

* `web_search_call.action.sources`: Include the sources of the web search tool call.
* `code_interpreter_call.outputs`: Includes the outputs of python code execution in code interpreter tool call items.
* `computer_call_output.output.image_url`: Include image urls from the computer call output.
* `file_search_call.results`: Include the search results of the file search tool call.
* `message.input_image.image_url`: Include image urls from the input message.
* `message.output_text.logprobs`: Include logprobs with assistant messages.
* `reasoning.encrypted_content`: Includes an encrypted version of reasoning tokens in reasoning item outputs. This enables reasoning items to be used in multi-turn conversations when using the Responses API statelessly (like when the `store` parameter is set to `false`, or when an organization is enrolled in the zero data retention program).

One of the following:

"file\_search\_call.results"

"web\_search\_call.results"

"web\_search\_call.action.sources"

"message.input\_image.image\_url"

"computer\_call\_output.output.image\_url"

"code\_interpreter\_call.outputs"

"reasoning.encrypted\_content"

"message.output\_text.logprobs"

limit: Optional[int]

A limit on the number of objects to be returned. Limit can range between
1 and 100, and the default is 20.

order: Optional[Literal["asc", "desc"]]

The order to return the input items in. Default is `desc`.

* `asc`: Return the input items in ascending order.
* `desc`: Return the input items in descending order.

One of the following:

"asc"

"desc"

##### ReturnsExpand Collapse

[ConversationItem](/api/reference/python/resources/conversations#(resource)%20conversations.items%20%3E%20(model)%20conversation_item%20%3E%20(schema))

A single item within a conversation. The set of possible types are the same as the `output` type of a [Response object](https://platform.openai.com/docs/api-reference/responses/object#responses/object-output).

One of the following:

class Message: …

A message to or from the model.

id: str

The unique ID of the message.

content: List[Content]

The content of the message

One of the following:

class ResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

class ResponseOutputText: …

A text output from the model.

annotations: List[Annotation]

The annotations of the text output.

One of the following:

class AnnotationFileCitation: …

A citation to a file.

file\_id: str

The ID of the file.

filename: str

The filename of the file cited.

index: int

The index of the file in the list of files.

type: Literal["file\_citation"]

The type of the file citation. Always `file_citation`.

class AnnotationURLCitation: …

A citation for a web resource used to generate a model response.

end\_index: int

The index of the last character of the URL citation in the message.

start\_index: int

The index of the first character of the URL citation in the message.

title: str

The title of the web resource.

type: Literal["url\_citation"]

The type of the URL citation. Always `url_citation`.

url: str

The URL of the web resource.

formaturi

class AnnotationContainerFileCitation: …

A citation for a container file used to generate a model response.

container\_id: str

The ID of the container file.

end\_index: int

The index of the last character of the container file citation in the message.

file\_id: str

The ID of the file.

filename: str

The filename of the container file cited.

start\_index: int

The index of the first character of the container file citation in the message.

type: Literal["container\_file\_citation"]

The type of the container file citation. Always `container_file_citation`.

class AnnotationFilePath: …

A path to a file.

file\_id: str

The ID of the file.

index: int

The index of the file in the list of files.

type: Literal["file\_path"]

The type of the file path. Always `file_path`.

text: str

The text output from the model.

type: Literal["output\_text"]

The type of the output text. Always `output_text`.

logprobs: Optional[List[Logprob]]

token: str

bytes: List[int]

logprob: float

top\_logprobs: List[LogprobTopLogprob]

token: str

bytes: List[int]

logprob: float

class TextContent: …

A text content.

text: str

type: Literal["text"]

class SummaryTextContent: …

A summary text from the model.

text: str

A summary of the reasoning output from the model so far.

type: Literal["summary\_text"]

The type of the object. Always `summary_text`.

class ContentReasoningText: …

Reasoning text from the model.

text: str

The reasoning text from the model.

type: Literal["reasoning\_text"]

The type of the reasoning text. Always `reasoning_text`.

class ResponseOutputRefusal: …

A refusal from the model.

refusal: str

The refusal explanation from the model.

type: Literal["refusal"]

The type of the refusal. Always `refusal`.

class ResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

One of the following:

"low"

"high"

"auto"

"original"

type: Literal["input\_image"]

The type of the input item. Always `input_image`.

file\_id: Optional[str]

The ID of the file to be sent to the model.

image\_url: Optional[str]

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

class ComputerScreenshotContent: …

A screenshot of a computer.

detail: Literal["low", "high", "auto", "original"]

The detail level of the screenshot image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

One of the following:

"low"

"high"

"auto"

"original"

file\_id: Optional[str]

The identifier of an uploaded file that contains the screenshot.

image\_url: Optional[str]

The URL of the screenshot image.

formaturi

type: Literal["computer\_screenshot"]

Specifies the event type. For a computer screenshot, this property is always set to `computer_screenshot`.

class ResponseInputFile: …

A file input to the model.

type: Literal["input\_file"]

The type of the input item. Always `input_file`.

detail: Optional[Literal["low", "high"]]

The detail level of the file to be sent to the model. Use `low` for the default rendering behavior, or `high` to render the file at higher quality. Defaults to `low`.

One of the following:

"low"

"high"

file\_data: Optional[str]

The content of the file to be sent to the model.

file\_id: Optional[str]

The ID of the file to be sent to the model.

file\_url: Optional[str]

The URL of the file to be sent to the model.

formaturi

filename: Optional[str]

The name of the file to be sent to the model.

role: Literal["unknown", "user", "assistant", 5 more]

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

status: Literal["in\_progress", "completed", "incomplete"]

The status of item. One of `in_progress`, `completed`, or `incomplete`. Populated when items are returned via API.

One of the following:

"in\_progress"

"completed"

"incomplete"

type: Literal["message"]

The type of the message. Always set to `message`.

phase: Optional[Literal["commentary", "final\_answer"]]

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`). For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

One of the following:

"commentary"

"final\_answer"

class ResponseFunctionToolCallItem: …

A tool call to run a function. See the
[function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.

id: str

The unique ID of the function tool call.

status: Literal["in\_progress", "completed", "incomplete"]

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

One of the following:

"in\_progress"

"completed"

"incomplete"

created\_by: Optional[str]

The identifier of the actor that created the item.

class ResponseFunctionToolCallOutputItem: …

id: str

The unique ID of the function call tool output.

call\_id: str

The unique ID of the function tool call generated by the model.

output: Union[str, List[OutputOutputContentList]]

The output from the function call generated by your code.
Can be a string or an list of output content.

One of the following:

str

A string of the output of the function call.

List[OutputOutputContentList]

Text, image, or file output of the function call.

One of the following:

class ResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

class ResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

One of the following:

"low"

"high"

"auto"

"original"

type: Literal["input\_image"]

The type of the input item. Always `input_image`.

file\_id: Optional[str]

The ID of the file to be sent to the model.

image\_url: Optional[str]

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

class ResponseInputFile: …

A file input to the model.

type: Literal["input\_file"]

The type of the input item. Always `input_file`.

detail: Optional[Literal["low", "high"]]

The detail level of the file to be sent to the model. Use `low` for the default rendering behavior, or `high` to render the file at higher quality. Defaults to `low`.

One of the following:

"low"

"high"

file\_data: Optional[str]

The content of the file to be sent to the model.

file\_id: Optional[str]

The ID of the file to be sent to the model.

file\_url: Optional[str]

The URL of the file to be sent to the model.

formaturi

filename: Optional[str]

The name of the file to be sent to the model.

status: Literal["in\_progress", "completed", "incomplete"]

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

One of the following:

"in\_progress"

"completed"

"incomplete"

type: Literal["function\_call\_output"]

The type of the function tool call output. Always `function_call_output`.

created\_by: Optional[str]

The identifier of the actor that created the item.

class ResponseFileSearchToolCall: …

The results of a file search tool call. See the
[file search guide](https://platform.openai.com/docs/guides/tools-file-search) for more information.

id: str

The unique ID of the file search tool call.

queries: List[str]

The queries used to search for files.

status: Literal["in\_progress", "searching", "completed", 2 more]

The status of the file search tool call. One of `in_progress`,
`searching`, `incomplete` or `failed`,

One of the following:

"in\_progress"

"searching"

"completed"

"incomplete"

"failed"

type: Literal["file\_search\_call"]

The type of the file search tool call. Always `file_search_call`.

results: Optional[List[Result]]

The results of the file search tool call.

attributes: Optional[Dict[str, Union[str, float, bool]]]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.

One of the following:

str

float

bool

file\_id: Optional[str]

The unique ID of the file.

filename: Optional[str]

The name of the file.

score: Optional[float]

The relevance score of the file - a value between 0 and 1.

formatfloat

text: Optional[str]

The text that was retrieved from the file.

class ResponseFunctionWebSearch: …

The results of a web search tool call. See the
[web search guide](https://platform.openai.com/docs/guides/tools-web-search) for more information.

id: str

The unique ID of the web search tool call.

action: Action

An object describing the specific action taken in this web search call.
Includes details on how the model used the web (search, open\_page, find\_in\_page).

One of the following:

class ActionSearch: …

Action type “search” - Performs a web search query.

type: Literal["search"]

The action type.

queries: Optional[List[str]]

The search queries.

Deprecatedquery: Optional[str]

The search query.

sources: Optional[List[ActionSearchSource]]

The sources used in the search.

type: Literal["url"]

The type of source. Always `url`.

url: str

The URL of the source.

formaturi

class ActionOpenPage: …

Action type “open\_page” - Opens a specific URL from search results.

type: Literal["open\_page"]

The action type.

url: Optional[str]

The URL opened by the model.

formaturi

class ActionFindInPage: …

Action type “find\_in\_page”: Searches for a pattern within a loaded page.

pattern: str

The pattern or text to search for within the page.

type: Literal["find\_in\_page"]

The action type.

url: str

The URL of the page searched for the pattern.

formaturi

status: Literal["in\_progress", "searching", "completed", "failed"]

The status of the web search tool call.

One of the following:

"in\_progress"

"searching"

"completed"

"failed"

type: Literal["web\_search\_call"]

The type of the web search tool call. Always `web_search_call`.

class ImageGenerationCall: …

An image generation request made by the model.

id: str

The unique ID of the image generation call.

result: Optional[str]

The generated image encoded in base64.

status: Literal["in\_progress", "completed", "generating", "failed"]

The status of the image generation call.

One of the following:

"in\_progress"

"completed"

"generating"

"failed"

type: Literal["image\_generation\_call"]

The type of the image generation call. Always `image_generation_call`.

class ResponseComputerToolCall: …

A tool call to a computer use tool. See the
[computer use guide](https://platform.openai.com/docs/guides/tools-computer-use) for more information.

id: str

The unique ID of the computer call.

call\_id: str

An identifier used when responding to the tool call with output.

pending\_safety\_checks: List[PendingSafetyCheck]

The pending safety checks for the computer call.

id: str

The ID of the pending safety check.

code: Optional[str]

The type of the pending safety check.

message: Optional[str]

Details about the pending safety check.

status: Literal["in\_progress", "completed", "incomplete"]

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

One of the following:

"in\_progress"

"completed"

"incomplete"

type: Literal["computer\_call"]

The type of the computer call. Always `computer_call`.

action: Optional[Action]

A click action.

One of the following:

class ActionClick: …

A click action.

button: Literal["left", "right", "wheel", 2 more]

Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

One of the following:

"left"

"right"

"wheel"

"back"

"forward"

type: Literal["click"]

Specifies the event type. For a click action, this property is always `click`.

x: int

The x-coordinate where the click occurred.

y: int

The y-coordinate where the click occurred.

keys: Optional[List[str]]

The keys being held while clicking.

class ActionDoubleClick: …

A double click action.

keys: Optional[List[str]]

The keys being held while double-clicking.

type: Literal["double\_click"]

Specifies the event type. For a double click action, this property is always set to `double_click`.

x: int

The x-coordinate where the double click occurred.

y: int

The y-coordinate where the double click occurred.

class ActionDrag: …

A drag action.

path: List[ActionDragPath]

An array of coordinates representing the path of the drag action. Coordinates will appear as an array of objects, eg

[
  { x: 100, y: 200 },
  { x: 200, y: 300 }
]

x: int

The x-coordinate.

y: int

The y-coordinate.

type: Literal["drag"]

Specifies the event type. For a drag action, this property is always set to `drag`.

keys: Optional[List[str]]

The keys being held while dragging the mouse.

class ActionKeypress: …

A collection of keypresses the model would like to perform.

keys: List[str]

The combination of keys the model is requesting to be pressed. This is an array of strings, each representing a key.

type: Literal["keypress"]

Specifies the event type. For a keypress action, this property is always set to `keypress`.

class ActionMove: …

A mouse move action.

type: Literal["move"]

Specifies the event type. For a move action, this property is always set to `move`.

x: int

The x-coordinate to move to.

y: int

The y-coordinate to move to.

keys: Optional[List[str]]

The keys being held while moving the mouse.

class ActionScreenshot: …

A screenshot action.

type: Literal["screenshot"]

Specifies the event type. For a screenshot action, this property is always set to `screenshot`.

class ActionScroll: …

A scroll action.

scroll\_x: int

The horizontal scroll distance.

scroll\_y: int

The vertical scroll distance.

type: Literal["scroll"]

Specifies the event type. For a scroll action, this property is always set to `scroll`.

x: int

The x-coordinate where the scroll occurred.

y: int

The y-coordinate where the scroll occurred.

keys: Optional[List[str]]

The keys being held while scrolling.

class ActionType: …

An action to type in text.

text: str

The text to type.

type: Literal["type"]

Specifies the event type. For a type action, this property is always set to `type`.

class ActionWait: …

A wait action.

type: Literal["wait"]

Specifies the event type. For a wait action, this property is always set to `wait`.

actions: Optional[ComputerActionList]

Flattened batched actions for `computer_use`. Each action includes an
`type` discriminator and action-specific fields.

One of the following:

class Click: …

A click action.

button: Literal["left", "right", "wheel", 2 more]

Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

One of the following:

"left"

"right"

"wheel"

"back"

"forward"

type: Literal["click"]

Specifies the event type. For a click action, this property is always `click`.

x: int

The x-coordinate where the click occurred.

y: int

The y-coordinate where the click occurred.

keys: Optional[List[str]]

The keys being held while clicking.

class DoubleClick: …

A double click action.

keys: Optional[List[str]]

The keys being held while double-clicking.

type: Literal["double\_click"]

Specifies the event type. For a double click action, this property is always set to `double_click`.

x: int

The x-coordinate where the double click occurred.

y: int

The y-coordinate where the double click occurred.

class Drag: …

A drag action.

path: List[DragPath]

An array of coordinates representing the path of the drag action. Coordinates will appear as an array of objects, eg

[
  { x: 100, y: 200 },
  { x: 200, y: 300 }
]

x: int

The x-coordinate.

y: int

The y-coordinate.

type: Literal["drag"]

Specifies the event type. For a drag action, this property is always set to `drag`.

keys: Optional[List[str]]

The keys being held while dragging the mouse.

class Keypress: …

A collection of keypresses the model would like to perform.

keys: List[str]

The combination of keys the model is requesting to be pressed. This is an array of strings, each representing a key.

type: Literal["keypress"]

Specifies the event type. For a keypress action, this property is always set to `keypress`.

class Move: …

A mouse move action.

type: Literal["move"]

Specifies the event type. For a move action, this property is always set to `move`.

x: int

The x-coordinate to move to.

y: int

The y-coordinate to move to.

keys: Optional[List[str]]

The keys being held while moving the mouse.

class Screenshot: …

A screenshot action.

type: Literal["screenshot"]

Specifies the event type. For a screenshot action, this property is always set to `screenshot`.

class Scroll: …

A scroll action.

scroll\_x: int

The horizontal scroll distance.

scroll\_y: int

The vertical scroll distance.

type: Literal["scroll"]

Specifies the event type. For a scroll action, this property is always set to `scroll`.

x: int

The x-coordinate where the scroll occurred.

y: int

The y-coordinate where the scroll occurred.

keys: Optional[List[str]]

The keys being held while scrolling.

class Type: …

An action to type in text.

text: str

The text to type.

type: Literal["type"]

Specifies the event type. For a type action, this property is always set to `type`.

class Wait: …

A wait action.

type: Literal["wait"]

Specifies the event type. For a wait action, this property is always set to `wait`.

class ResponseComputerToolCallOutputItem: …

id: str

The unique ID of the computer call tool output.

call\_id: str

The ID of the computer tool call that produced the output.

output: [ResponseComputerToolCallOutputScreenshot](/api/reference/python/resources/responses#(resource)%20responses%20%3E%20(model)%20response_computer_tool_call_output_screenshot%20%3E%20(schema))

A computer screenshot image used with the computer use tool.

type: Literal["computer\_screenshot"]

Specifies the event type. For a computer screenshot, this property is
always set to `computer_screenshot`.

file\_id: Optional[str]

The identifier of an uploaded file that contains the screenshot.

image\_url: Optional[str]

The URL of the screenshot image.

formaturi

status: Literal["completed", "incomplete", "failed", "in\_progress"]

The status of the message input. One of `in_progress`, `completed`, or
`incomplete`. Populated when input items are returned via API.

One of the following:

"completed"

"incomplete"

"failed"

"in\_progress"

type: Literal["computer\_call\_output"]

The type of the computer tool call output. Always `computer_call_output`.

acknowledged\_safety\_checks: Optional[List[AcknowledgedSafetyCheck]]

The safety checks reported by the API that have been acknowledged by the
developer.

id: str

The ID of the pending safety check.

code: Optional[str]

The type of the pending safety check.

message: Optional[str]

Details about the pending safety check.

created\_by: Optional[str]

The identifier of the actor that created the item.

class ResponseToolSearchCall: …

id: str

The unique ID of the tool search call item.

arguments: object

Arguments used for the tool search call.

call\_id: Optional[str]

The unique ID of the tool search call generated by the model.

execution: Literal["server", "client"]

Whether tool search was executed by the server or by the client.

One of the following:

"server"

"client"

status: Literal["in\_progress", "completed", "incomplete"]

The status of the tool search call item that was recorded.

One of the following:

"in\_progress"

"completed"

"incomplete"

type: Literal["tool\_search\_call"]

The type of the item. Always `tool_search_call`.

created\_by: Optional[str]

The identifier of the actor that created the item.

class ResponseToolSearchOutputItem: …

id: str

The unique ID of the tool search output item.

call\_id: Optional[str]

The unique ID of the tool search call generated by the model.

execution: Literal["server", "client"]

Whether tool search was executed by the server or by the client.

One of the following:

"server"

"client"

status: Literal["in\_progress", "completed", "incomplete"]

The status of the tool search output item that was recorded.

One of the following:

"in\_progress"

"completed"

"incomplete"

tools: List[[Tool](/api/reference/python/resources/responses#(resource)%20responses%20%3E%20(model)%20tool%20%3E%20(schema))]

The loaded tool definitions returned by tool search.

One of the following:

class FunctionTool: …

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

name: str

The name of the function to call.

parameters: Optional[Dict[str, object]]

A JSON schema object describing the parameters of the function.

strict: Optional[bool]

Whether to enforce strict parameter validation. Default `true`.

type: Literal["function"]

The type of the function tool. Always `function`.

defer\_loading: Optional[bool]

Whether this function is deferred and loaded via tool search.

description: Optional[str]

A description of the function. Used by the model to determine whether or not to call the function.

class FileSearchTool: …

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

type: Literal["file\_search"]

The type of the file search tool. Always `file_search`.

vector\_store\_ids: List[str]

The IDs of the vector stores to search.

filters: Optional[Filters]

A filter to apply.

One of the following:

class ComparisonFilter: …

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: str

The key to compare against the value.

type: Literal["eq", "ne", "gt", 5 more]

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

value: Union[str, float, bool, List[Union[str, float]]]

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

str

float

bool

List[Union[str, float]]

One of the following:

str

float

class CompoundFilter: …

Combine multiple filters using `and` or `or`.

filters: List[Filter]

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

One of the following:

class ComparisonFilter: …

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: str

The key to compare against the value.

type: Literal["eq", "ne", "gt", 5 more]

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

value: Union[str, float, bool, List[Union[str, float]]]

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

str

float

bool

List[Union[str, float]]

One of the following:

str

float

object

type: Literal["and", "or"]

Type of operation: `and` or `or`.

One of the following:

"and"

"or"

max\_num\_results: Optional[int]

The maximum number of results to return. This number should be between 1 and 50 inclusive.

ranking\_options: Optional[RankingOptions]

Ranking options for search.

hybrid\_search: Optional[RankingOptionsHybridSearch]

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

embedding\_weight: float

The weight of the embedding in the reciprocal ranking fusion.

text\_weight: float

The weight of the text in the reciprocal ranking fusion.

ranker: Optional[Literal["auto", "default-2024-11-15"]]

The ranker to use for the file search.

One of the following:

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

class ComputerTool: …

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

type: Literal["computer"]

The type of the computer tool. Always `computer`.

class ComputerUsePreviewTool: …

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

display\_height: int

The height of the computer display.

display\_width: int

The width of the computer display.

environment: Literal["windows", "mac", "linux", 2 more]

The type of computer environment to control.

One of the following:

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

The type of the computer use tool. Always `computer_use_preview`.

class WebSearchTool: …

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

One of the following:

"web\_search"

"web\_search\_2025\_08\_26"

filters: Optional[Filters]

Filters for the search.

allowed\_domains: Optional[List[str]]

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

search\_context\_size: Optional[Literal["low", "medium", "high"]]

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

The approximate location of the user.

city: Optional[str]

Free text input for the city of the user, e.g. `San Francisco`.

country: Optional[str]

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region: Optional[str]

Free text input for the region of the user, e.g. `California`.

timezone: Optional[str]

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

type: Optional[Literal["approximate"]]

The type of location approximation. Always `approximate`.

class Mcp: …

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: str

A label for this MCP server, used to identify it in tool calls.

type: Literal["mcp"]

The type of the MCP tool. Always `mcp`.

allowed\_tools: Optional[McpAllowedTools]

List of allowed tool names or a filter object.

One of the following:

List[str]

A string array of allowed tool names

class McpAllowedToolsMcpToolFilter: …

A filter object to specify which tools are allowed.

read\_only: Optional[bool]

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names: Optional[List[str]]

List of allowed tool names.

authorization: Optional[str]

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

connector\_id: Optional[Literal["connector\_dropbox", "connector\_gmail", "connector\_googlecalendar", 5 more]]

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

defer\_loading: Optional[bool]

Whether this MCP tool is deferred and discovered via tool search.

headers: Optional[Dict[str, str]]

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

require\_approval: Optional[McpRequireApproval]

Specify which of the MCP server’s tools require approval.

One of the following:

class McpRequireApprovalMcpToolApprovalFilter: …

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

always: Optional[McpRequireApprovalMcpToolApprovalFilterAlways]

A filter object to specify which tools are allowed.

read\_only: Optional[bool]

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names: Optional[List[str]]

List of allowed tool names.

never: Optional[McpRequireApprovalMcpToolApprovalFilterNever]

A filter object to specify which tools are allowed.

read\_only: Optional[bool]

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names: Optional[List[str]]

List of allowed tool names.

Literal["always", "never"]

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

One of the following:

"always"

"never"

server\_description: Optional[str]

Optional description of the MCP server, used to provide more context.

server\_url: Optional[str]

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

tunnel\_id: Optional[str]

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

class CodeInterpreter: …

A tool that runs Python code to help generate a response to a prompt.

container: CodeInterpreterContainer

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

One of the following:

str

The container ID.

class CodeInterpreterContainerCodeInterpreterToolAuto: …

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

type: Literal["auto"]

Always `auto`.

file\_ids: Optional[List[str]]

An optional list of uploaded files to make available to your code.

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

The memory limit for the code interpreter container.

One of the following:

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

Network access policy for the container.

One of the following:

class ContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

Disable outbound network access. Always `disabled`.

class ContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

A list of allowed domains when type is `allowlist`.

type: Literal["allowlist"]

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: Optional[List[[ContainerNetworkPolicyDomainSecret](/api/reference/python/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema))]]

Optional domain-scoped secrets for allowlisted domains.

domain: str

The domain associated with the secret.

minLength1

name: str

The name of the secret to inject for the domain.

minLength1

value: str

The secret value to inject for the domain.

maxLength10485760

minLength1

type: Literal["code\_interpreter"]

The type of the code interpreter tool. Always `code_interpreter`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

The type of the image generation tool. Always `image_generation`.

action: Optional[Literal["generate", "edit", "auto"]]

Whether to generate a new image or edit an existing image. Default: `auto`.

One of the following:

"generate"

"edit"

"auto"

background: Optional[Literal["transparent", "opaque", "auto"]]

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

input\_fidelity: Optional[Literal["high", "low"]]

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

One of the following:

"high"

"low"

input\_image\_mask: Optional[ImageGenerationInputImageMask]

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

file\_id: Optional[str]

File ID for the mask image.

image\_url: Optional[str]

Base64-encoded mask image.

model: Optional[Union[str, Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more], null]]

The image generation model to use. Default: `gpt-image-1`.

One of the following:

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

The image generation model to use. Default: `gpt-image-1`.

One of the following:

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

Moderation level for the generated image. Default: `auto`.

One of the following:

"auto"

"low"

output\_compression: Optional[int]

Compression level for the output image. Default: 100.

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

One of the following:

"png"

"webp"

"jpeg"

partial\_images: Optional[int]

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

quality: Optional[Literal["low", "medium", "high", "auto"]]

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

One of the following:

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

One of the following:

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

One of the following:

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class FunctionShellTool: …

A tool that allows the model to execute shell commands.

type: Literal["shell"]

The type of the shell tool. Always `shell`.

environment: Optional[Environment]

One of the following:

class ContainerAuto: …

type: Literal["container\_auto"]

Automatically creates a container for this request

file\_ids: Optional[List[str]]

An optional list of uploaded files to make available to your code.

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

The memory limit for the container.

One of the following:

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

Network access policy for the container.

One of the following:

class ContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

Disable outbound network access. Always `disabled`.

class ContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

A list of allowed domains when type is `allowlist`.

type: Literal["allowlist"]

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: Optional[List[[ContainerNetworkPolicyDomainSecret](/api/reference/python/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema))]]

Optional domain-scoped secrets for allowlisted domains.

domain: str

The domain associated with the secret.

minLength1

name: str

The name of the secret to inject for the domain.

minLength1

value: str

The secret value to inject for the domain.

maxLength10485760

minLength1

skills: Optional[List[Skill]]

An optional list of skills referenced by id or inline data.

One of the following:

class SkillReference: …

skill\_id: str

The ID of the referenced skill.

maxLength64

minLength1

type: Literal["skill\_reference"]

References a skill created with the /v1/skills endpoint.

version: Optional[str]

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

class InlineSkill: …

description: str

The description of the skill.

name: str

The name of the skill.

source: [InlineSkillSource](/api/reference/python/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill_source%20%3E%20(schema))

Inline skill payload

data: str

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

media\_type: Literal["application/zip"]

The media type of the inline skill payload. Must be `application/zip`.

type: Literal["base64"]

The type of the inline skill source. Must be `base64`.

type: Literal["inline"]

Defines an inline skill for this request.

class LocalEnvironment: …

type: Literal["local"]

Use a local computer environment.

skills: Optional[List[[LocalSkill](/api/reference/python/resources/responses#(resource)%20responses%20%3E%20(model)%20local_skill%20%3E%20(schema))]]

An optional list of skills.

description: str

The description of the skill.

name: str

The name of the skill.

path: str

The path to the directory containing the skill.

class ContainerReference: …

container\_id: str

The ID of the referenced container.

type: Literal["container\_reference"]

References a container created with the /v1/containers endpoint

class CustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

The name of the custom tool, used to identify it in tool calls.

type: Literal["custom"]

The type of the custom tool. Always `custom`.

defer\_loading: Optional[bool]

Whether this tool should be deferred and discovered via tool search.

description: Optional[str]

Optional description of the custom tool, used to provide more context.

format: Optional[CustomToolInputFormat]

The input format for the custom tool. Default is unconstrained text.

One of the following:

class Text: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class Grammar: …

A grammar defined by the user.

definition: str

The grammar definition.

syntax: Literal["lark", "regex"]

The syntax of the grammar definition. One of `lark` or `regex`.

One of the following:

"lark"

"regex"

type: Literal["grammar"]

Grammar format. Always `grammar`.

class NamespaceTool: …

Groups function/custom tools under a shared namespace.

description: str

A description of the namespace shown to the model.

minLength1

name: str

The namespace name used in tool calls (for example, `crm`).

minLength1

tools: List[Tool]

The function/custom tools available inside this namespace.

One of the following:

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

defer\_loading: Optional[bool]

Whether this function should be deferred and discovered via tool search.

description: Optional[str]

parameters: Optional[object]

strict: Optional[bool]

class CustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

The name of the custom tool, used to identify it in tool calls.

type: Literal["custom"]

The type of the custom tool. Always `custom`.

defer\_loading: Optional[bool]

Whether this tool should be deferred and discovered via tool search.

description: Optional[str]

Optional description of the custom tool, used to provide more context.

format: Optional[CustomToolInputFormat]

The input format for the custom tool. Default is unconstrained text.

One of the following:

class Text: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class Grammar: …

A grammar defined by the user.

definition: str

The grammar definition.

syntax: Literal["lark", "regex"]

The syntax of the grammar definition. One of `lark` or `regex`.

One of the following:

"lark"

"regex"

type: Literal["grammar"]

Grammar format. Always `grammar`.

type: Literal["namespace"]

The type of the tool. Always `namespace`.

class ToolSearchTool: …

Hosted or BYOT tool search configuration for deferred tools.

type: Literal["tool\_search"]

The type of the tool. Always `tool_search`.

description: Optional[str]

Description shown to the model for a client-executed tool search tool.

execution: Optional[Literal["server", "client"]]

Whether tool search is executed by the server or by the client.

One of the following:

"server"

"client"

parameters: Optional[object]

Parameter schema for a client-executed tool search tool.

class WebSearchPreviewTool: …

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

One of the following:

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

One of the following:

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

The user’s location.

type: Literal["approximate"]

The type of location approximation. Always `approximate`.

city: Optional[str]

Free text input for the city of the user, e.g. `San Francisco`.

country: Optional[str]

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region: Optional[str]

Free text input for the region of the user, e.g. `California`.

timezone: Optional[str]

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

class ApplyPatchTool: …

Allows the assistant to create, delete, or update files using unified diffs.

type: Literal["apply\_patch"]

The type of the tool. Always `apply_patch`.

type: Literal["tool\_search\_output"]

The type of the item. Always `tool_search_output`.

created\_by: Optional[str]

The identifier of the actor that created the item.

class AdditionalTools: …

id: str

The unique ID of the additional tools item.

role: Literal["unknown", "user", "assistant", 5 more]

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

tools: List[[Tool](/api/reference/python/resources/responses#(resource)%20responses%20%3E%20(model)%20tool%20%3E%20(schema))]

The additional tool definitions made available at this item.

One of the following:

class FunctionTool: …

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

name: str

The name of the function to call.

parameters: Optional[Dict[str, object]]

A JSON schema object describing the parameters of the function.

strict: Optional[bool]

Whether to enforce strict parameter validation. Default `true`.

type: Literal["function"]

The type of the function tool. Always `function`.

defer\_loading: Optional[bool]

Whether this function is deferred and loaded via tool search.

description: Optional[str]

A description of the function. Used by the model to determine whether or not to call the function.

class FileSearchTool: …

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

type: Literal["file\_search"]

The type of the file search tool. Always `file_search`.

vector\_store\_ids: List[str]

The IDs of the vector stores to search.

filters: Optional[Filters]

A filter to apply.

One of the following:

class ComparisonFilter: …

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: str

The key to compare against the value.

type: Literal["eq", "ne", "gt", 5 more]

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

value: Union[str, float, bool, List[Union[str, float]]]

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

str

float

bool

List[Union[str, float]]

One of the following:

str

float

class CompoundFilter: …

Combine multiple filters using `and` or `or`.

filters: List[Filter]

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

One of the following:

class ComparisonFilter: …

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: str

The key to compare against the value.

type: Literal["eq", "ne", "gt", 5 more]

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

value: Union[str, float, bool, List[Union[str, float]]]

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

str

float

bool

List[Union[str, float]]

One of the following:

str

float

object

type: Literal["and", "or"]

Type of operation: `and` or `or`.

One of the following:

"and"

"or"

max\_num\_results: Optional[int]

The maximum number of results to return. This number should be between 1 and 50 inclusive.

ranking\_options: Optional[RankingOptions]

Ranking options for search.

hybrid\_search: Optional[RankingOptionsHybridSearch]

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

embedding\_weight: float

The weight of the embedding in the reciprocal ranking fusion.

text\_weight: float

The weight of the text in the reciprocal ranking fusion.

ranker: Optional[Literal["auto", "default-2024-11-15"]]

The ranker to use for the file search.

One of the following:

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

class ComputerTool: …

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

type: Literal["computer"]

The type of the computer tool. Always `computer`.

class ComputerUsePreviewTool: …

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

display\_height: int

The height of the computer display.

display\_width: int

The width of the computer display.

environment: Literal["windows", "mac", "linux", 2 more]

The type of computer environment to control.

One of the following:

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

The type of the computer use tool. Always `computer_use_preview`.

class WebSearchTool: …

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

One of the following:

"web\_search"

"web\_search\_2025\_08\_26"

filters: Optional[Filters]

Filters for the search.

allowed\_domains: Optional[List[str]]

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

search\_context\_size: Optional[Literal["low", "medium", "high"]]

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

The approximate location of the user.

city: Optional[str]

Free text input for the city of the user, e.g. `San Francisco`.

country: Optional[str]

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region: Optional[str]

Free text input for the region of the user, e.g. `California`.

timezone: Optional[str]

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

type: Optional[Literal["approximate"]]

The type of location approximation. Always `approximate`.

class Mcp: …

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: str

A label for this MCP server, used to identify it in tool calls.

type: Literal["mcp"]

The type of the MCP tool. Always `mcp`.

allowed\_tools: Optional[McpAllowedTools]

List of allowed tool names or a filter object.

One of the following:

List[str]

A string array of allowed tool names

class McpAllowedToolsMcpToolFilter: …

A filter object to specify which tools are allowed.

read\_only: Optional[bool]

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names: Optional[List[str]]

List of allowed tool names.

authorization: Optional[str]

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

connector\_id: Optional[Literal["connector\_dropbox", "connector\_gmail", "connector\_googlecalendar", 5 more]]

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

defer\_loading: Optional[bool]

Whether this MCP tool is deferred and discovered via tool search.

headers: Optional[Dict[str, str]]

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

require\_approval: Optional[McpRequireApproval]

Specify which of the MCP server’s tools require approval.

One of the following:

class McpRequireApprovalMcpToolApprovalFilter: …

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

always: Optional[McpRequireApprovalMcpToolApprovalFilterAlways]

A filter object to specify which tools are allowed.

read\_only: Optional[bool]

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names: Optional[List[str]]

List of allowed tool names.

never: Optional[McpRequireApprovalMcpToolApprovalFilterNever]

A filter object to specify which tools are allowed.

read\_only: Optional[bool]

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names: Optional[List[str]]

List of allowed tool names.

Literal["always", "never"]

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

One of the following:

"always"

"never"

server\_description: Optional[str]

Optional description of the MCP server, used to provide more context.

server\_url: Optional[str]

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

tunnel\_id: Optional[str]

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

class CodeInterpreter: …

A tool that runs Python code to help generate a response to a prompt.

container: CodeInterpreterContainer

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

One of the following:

str

The container ID.

class CodeInterpreterContainerCodeInterpreterToolAuto: …

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

type: Literal["auto"]

Always `auto`.

file\_ids: Optional[List[str]]

An optional list of uploaded files to make available to your code.

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

The memory limit for the code interpreter container.

One of the following:

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

Network access policy for the container.

One of the following:

class ContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

Disable outbound network access. Always `disabled`.

class ContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

A list of allowed domains when type is `allowlist`.

type: Literal["allowlist"]

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: Optional[List[[ContainerNetworkPolicyDomainSecret](/api/reference/python/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema))]]

Optional domain-scoped secrets for allowlisted domains.

domain: str

The domain associated with the secret.

minLength1

name: str

The name of the secret to inject for the domain.

minLength1

value: str

The secret value to inject for the domain.

maxLength10485760

minLength1

type: Literal["code\_interpreter"]

The type of the code interpreter tool. Always `code_interpreter`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

The type of the image generation tool. Always `image_generation`.

action: Optional[Literal["generate", "edit", "auto"]]

Whether to generate a new image or edit an existing image. Default: `auto`.

One of the following:

"generate"

"edit"

"auto"

background: Optional[Literal["transparent", "opaque", "auto"]]

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

input\_fidelity: Optional[Literal["high", "low"]]

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

One of the following:

"high"

"low"

input\_image\_mask: Optional[ImageGenerationInputImageMask]

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

file\_id: Optional[str]

File ID for the mask image.

image\_url: Optional[str]

Base64-encoded mask image.

model: Optional[Union[str, Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more], null]]

The image generation model to use. Default: `gpt-image-1`.

One of the following:

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

The image generation model to use. Default: `gpt-image-1`.

One of the following:

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

Moderation level for the generated image. Default: `auto`.

One of the following:

"auto"

"low"

output\_compression: Optional[int]

Compression level for the output image. Default: 100.

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

One of the following:

"png"

"webp"

"jpeg"

partial\_images: Optional[int]

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

quality: Optional[Literal["low", "medium", "high", "auto"]]

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

One of the following:

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

One of the following:

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

One of the following:

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class FunctionShellTool: …

A tool that allows the model to execute shell commands.

type: Literal["shell"]

The type of the shell tool. Always `shell`.

environment: Optional[Environment]

One of the following:

class ContainerAuto: …

type: Literal["container\_auto"]

Automatically creates a container for this request

file\_ids: Optional[List[str]]

An optional list of uploaded files to make available to your code.

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

The memory limit for the container.

One of the following:

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

Network access policy for the container.

One of the following:

class ContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

Disable outbound network access. Always `disabled`.

class ContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

A list of allowed domains when type is `allowlist`.

type: Literal["allowlist"]

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: Optional[List[[ContainerNetworkPolicyDomainSecret](/api/reference/python/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema))]]

Optional domain-scoped secrets for allowlisted domains.

domain: str

The domain associated with the secret.

minLength1

name: str

The name of the secret to inject for the domain.

minLength1

value: str

The secret value to inject for the domain.

maxLength10485760

minLength1

skills: Optional[List[Skill]]

An optional list of skills referenced by id or inline data.

One of the following:

class SkillReference: …

skill\_id: str

The ID of the referenced skill.

maxLength64

minLength1

type: Literal["skill\_reference"]

References a skill created with the /v1/skills endpoint.

version: Optional[str]

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

class InlineSkill: …

description: str

The description of the skill.

name: str

The name of the skill.

source: [InlineSkillSource](/api/reference/python/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill_source%20%3E%20(schema))

Inline skill payload

data: str

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

media\_type: Literal["application/zip"]

The media type of the inline skill payload. Must be `application/zip`.

type: Literal["base64"]

The type of the inline skill source. Must be `base64`.

type: Literal["inline"]

Defines an inline skill for this request.

class LocalEnvironment: …

type: Literal["local"]

Use a local computer environment.

skills: Optional[List[[LocalSkill](/api/reference/python/resources/responses#(resource)%20responses%20%3E%20(model)%20local_skill%20%3E%20(schema))]]

An optional list of skills.

description: str

The description of the skill.

name: str

The name of the skill.

path: str

The path to the directory containing the skill.

class ContainerReference: …

container\_id: str

The ID of the referenced container.

type: Literal["container\_reference"]

References a container created with the /v1/containers endpoint

class CustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

The name of the custom tool, used to identify it in tool calls.

type: Literal["custom"]

The type of the custom tool. Always `custom`.

defer\_loading: Optional[bool]

Whether this tool should be deferred and discovered via tool search.

description: Optional[str]

Optional description of the custom tool, used to provide more context.

format: Optional[CustomToolInputFormat]

The input format for the custom tool. Default is unconstrained text.

One of the following:

class Text: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class Grammar: …

A grammar defined by the user.

definition: str

The grammar definition.

syntax: Literal["lark", "regex"]

The syntax of the grammar definition. One of `lark` or `regex`.

One of the following:

"lark"

"regex"

type: Literal["grammar"]

Grammar format. Always `grammar`.

class NamespaceTool: …

Groups function/custom tools under a shared namespace.

description: str

A description of the namespace shown to the model.

minLength1

name: str

The namespace name used in tool calls (for example, `crm`).

minLength1

tools: List[Tool]

The function/custom tools available inside this namespace.

One of the following:

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

defer\_loading: Optional[bool]

Whether this function should be deferred and discovered via tool search.

description: Optional[str]

parameters: Optional[object]

strict: Optional[bool]

class CustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

The name of the custom tool, used to identify it in tool calls.

type: Literal["custom"]

The type of the custom tool. Always `custom`.

defer\_loading: Optional[bool]

Whether this tool should be deferred and discovered via tool search.

description: Optional[str]

Optional description of the custom tool, used to provide more context.

format: Optional[CustomToolInputFormat]

The input format for the custom tool. Default is unconstrained text.

One of the following:

class Text: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class Grammar: …

A grammar defined by the user.

definition: str

The grammar definition.

syntax: Literal["lark", "regex"]

The syntax of the grammar definition. One of `lark` or `regex`.

One of the following:

"lark"

"regex"

type: Literal["grammar"]

Grammar format. Always `grammar`.

type: Literal["namespace"]

The type of the tool. Always `namespace`.

class ToolSearchTool: …

Hosted or BYOT tool search configuration for deferred tools.

type: Literal["tool\_search"]

The type of the tool. Always `tool_search`.

description: Optional[str]

Description shown to the model for a client-executed tool search tool.

execution: Optional[Literal["server", "client"]]

Whether tool search is executed by the server or by the client.

One of the following:

"server"

"client"

parameters: Optional[object]

Parameter schema for a client-executed tool search tool.

class WebSearchPreviewTool: …

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

One of the following:

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

One of the following:

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

The user’s location.

type: Literal["approximate"]

The type of location approximation. Always `approximate`.

city: Optional[str]

Free text input for the city of the user, e.g. `San Francisco`.

country: Optional[str]

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region: Optional[str]

Free text input for the region of the user, e.g. `California`.

timezone: Optional[str]

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

class ApplyPatchTool: …

Allows the assistant to create, delete, or update files using unified diffs.

type: Literal["apply\_patch"]

The type of the tool. Always `apply_patch`.

type: Literal["additional\_tools"]

The type of the item. Always `additional_tools`.

class ResponseReasoningItem: …

A description of the chain of thought used by a reasoning model while generating
a response. Be sure to include these items in your `input` to the Responses API
for subsequent turns of a conversation if you are manually
[managing context](https://platform.openai.com/docs/guides/conversation-state).

id: str

The unique identifier of the reasoning content.

summary: List[Summary]

Reasoning summary content.

text: str

A summary of the reasoning output from the model so far.

type: Literal["summary\_text"]

The type of the object. Always `summary_text`.

type: Literal["reasoning"]

The type of the object. Always `reasoning`.

content: Optional[List[Content]]

Reasoning text content.

text: str

The reasoning text from the model.

type: Literal["reasoning\_text"]

The type of the reasoning text. Always `reasoning_text`.

encrypted\_content: Optional[str]

The encrypted content of the reasoning item - populated when a response is
generated with `reasoning.encrypted_content` in the `include` parameter.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

One of the following:

"in\_progress"

"completed"

"incomplete"

class ResponseCompactionItem: …

A compaction item generated by the [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).

id: str

The unique ID of the compaction item.

encrypted\_content: str

The encrypted content that was produced by compaction.

type: Literal["compaction"]

The type of the item. Always `compaction`.

created\_by: Optional[str]

The identifier of the actor that created the item.

class ResponseCodeInterpreterToolCall: …

A tool call to run code.

id: str

The unique ID of the code interpreter tool call.

code: Optional[str]

The code to run, or null if not available.

container\_id: str

The ID of the container used to run the code.

outputs: Optional[List[Output]]

The outputs generated by the code interpreter, such as logs or images.
Can be null if no outputs are available.

One of the following:

class OutputLogs: …

The logs output from the code interpreter.

logs: str

The logs output from the code interpreter.

type: Literal["logs"]

The type of the output. Always `logs`.

class OutputImage: …

The image output from the code interpreter.

type: Literal["image"]

The type of the output. Always `image`.

url: str

The URL of the image output from the code interpreter.

formaturi

status: Literal["in\_progress", "completed", "incomplete", 2 more]

The status of the code interpreter tool call. Valid values are `in_progress`, `completed`, `incomplete`, `interpreting`, and `failed`.

One of the following:

"in\_progress"

"completed"

"incomplete"

"interpreting"

"failed"

type: Literal["code\_interpreter\_call"]

The type of the code interpreter tool call. Always `code_interpreter_call`.

class LocalShellCall: …

A tool call to run a command on the local shell.

id: str

The unique ID of the local shell call.

action: LocalShellCallAction

Execute a shell command on the server.

command: List[str]

The command to run.

env: Dict[str, str]

Environment variables to set for the command.

type: Literal["exec"]

The type of the local shell action. Always `exec`.

timeout\_ms: Optional[int]

Optional timeout in milliseconds for the command.

user: Optional[str]

Optional user to run the command as.

working\_directory: Optional[str]

Optional working directory to run the command in.

call\_id: str

The unique ID of the local shell tool call generated by the model.

status: Literal["in\_progress", "completed", "incomplete"]

The status of the local shell call.

One of the following:

"in\_progress"

"completed"

"incomplete"

type: Literal["local\_shell\_call"]

The type of the local shell call. Always `local_shell_call`.

class LocalShellCallOutput: …

The output of a local shell tool call.

id: str

The unique ID of the local shell tool call generated by the model.

output: str

A JSON string of the output of the local shell tool call.

type: Literal["local\_shell\_call\_output"]

The type of the local shell tool call output. Always `local_shell_call_output`.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the item. One of `in_progress`, `completed`, or `incomplete`.

One of the following:

"in\_progress"

"completed"

"incomplete"

class ResponseFunctionShellToolCall: …

A tool call that executes one or more shell commands in a managed environment.

id: str

The unique ID of the shell tool call. Populated when this item is returned via API.

action: Action

The shell commands and limits that describe how to run the tool call.

commands: List[str]

max\_output\_length: Optional[int]

Optional maximum number of characters to return from each command.

timeout\_ms: Optional[int]

Optional timeout in milliseconds for the commands.

call\_id: str

The unique ID of the shell tool call generated by the model.

environment: Optional[Environment]

Represents the use of a local environment to perform shell actions.

One of the following:

class ResponseLocalEnvironment: …

Represents the use of a local environment to perform shell actions.

type: Literal["local"]

The environment type. Always `local`.

class ResponseContainerReference: …

Represents a container created with /v1/containers.

container\_id: str

type: Literal["container\_reference"]

The environment type. Always `container_reference`.

status: Literal["in\_progress", "completed", "incomplete"]

The status of the shell call. One of `in_progress`, `completed`, or `incomplete`.

One of the following:

"in\_progress"

"completed"

"incomplete"

type: Literal["shell\_call"]

The type of the item. Always `shell_call`.

created\_by: Optional[str]

The ID of the entity that created this tool call.

class ResponseFunctionShellToolCallOutput: …

The output of a shell tool call that was emitted.

id: str

The unique ID of the shell call output. Populated when this item is returned via API.

call\_id: str

The unique ID of the shell tool call generated by the model.

max\_output\_length: Optional[int]

The maximum length of the shell command output. This is generated by the model and should be passed back with the raw output.

output: List[Output]

An array of shell call output contents

outcome: OutputOutcome

Represents either an exit outcome (with an exit code) or a timeout outcome for a shell call output chunk.

One of the following:

class OutputOutcomeTimeout: …

Indicates that the shell call exceeded its configured time limit.

type: Literal["timeout"]

The outcome type. Always `timeout`.

class OutputOutcomeExit: …

Indicates that the shell commands finished and returned an exit code.

exit\_code: int

Exit code from the shell process.

type: Literal["exit"]

The outcome type. Always `exit`.

stderr: str

The standard error output that was captured.

stdout: str

The standard output that was captured.

created\_by: Optional[str]

The identifier of the actor that created the item.

status: Literal["in\_progress", "completed", "incomplete"]

The status of the shell call output. One of `in_progress`, `completed`, or `incomplete`.

One of the following:

"in\_progress"

"completed"

"incomplete"

type: Literal["shell\_call\_output"]

The type of the shell call output. Always `shell_call_output`.

created\_by: Optional[str]

The identifier of the actor that created the item.

class ResponseApplyPatchToolCall: …

A tool call that applies file diffs by creating, deleting, or updating files.

id: str

The unique ID of the apply patch tool call. Populated when this item is returned via API.

call\_id: str

The unique ID of the apply patch tool call generated by the model.

operation: Operation

One of the create\_file, delete\_file, or update\_file operations applied via apply\_patch.

One of the following:

class OperationCreateFile: …

Instruction describing how to create a file via the apply\_patch tool.

diff: str

Diff to apply.

path: str

Path of the file to create.

type: Literal["create\_file"]

Create a new file with the provided diff.

class OperationDeleteFile: …

Instruction describing how to delete a file via the apply\_patch tool.

path: str

Path of the file to delete.

type: Literal["delete\_file"]

Delete the specified file.

class OperationUpdateFile: …

Instruction describing how to update a file via the apply\_patch tool.

diff: str

Diff to apply.

path: str

Path of the file to update.

type: Literal["update\_file"]

Update an existing file with the provided diff.

status: Literal["in\_progress", "completed"]

The status of the apply patch tool call. One of `in_progress` or `completed`.

One of the following:

"in\_progress"

"completed"

type: Literal["apply\_patch\_call"]

The type of the item. Always `apply_patch_call`.

created\_by: Optional[str]

The ID of the entity that created this tool call.

class ResponseApplyPatchToolCallOutput: …

The output emitted by an apply patch tool call.

id: str

The unique ID of the apply patch tool call output. Populated when this item is returned via API.

call\_id: str

The unique ID of the apply patch tool call generated by the model.

status: Literal["completed", "failed"]

The status of the apply patch tool call output. One of `completed` or `failed`.

One of the following:

"completed"

"failed"

type: Literal["apply\_patch\_call\_output"]

The type of the item. Always `apply_patch_call_output`.

created\_by: Optional[str]

The ID of the entity that created this tool call output.

output: Optional[str]

Optional textual output returned by the apply patch tool.

class McpListTools: …

A list of tools available on an MCP server.

id: str

The unique ID of the list.

server\_label: str

The label of the MCP server.

tools: List[McpListToolsTool]

The tools available on the server.

input\_schema: object

The JSON schema describing the tool’s input.

name: str

The name of the tool.

annotations: Optional[object]

Additional annotations about the tool.

description: Optional[str]

The description of the tool.

type: Literal["mcp\_list\_tools"]

The type of the item. Always `mcp_list_tools`.

error: Optional[str]

Error message if the server could not list tools.

class McpApprovalRequest: …

A request for human approval of a tool invocation.

id: str

The unique ID of the approval request.

arguments: str

A JSON string of arguments for the tool.

name: str

The name of the tool to run.

server\_label: str

The label of the MCP server making the request.

type: Literal["mcp\_approval\_request"]

The type of the item. Always `mcp_approval_request`.

class McpApprovalResponse: …

A response to an MCP approval request.

id: str

The unique ID of the approval response

approval\_request\_id: str

The ID of the approval request being answered.

approve: bool

Whether the request was approved.

type: Literal["mcp\_approval\_response"]

The type of the item. Always `mcp_approval_response`.

reason: Optional[str]

Optional reason for the decision.

class McpCall: …

An invocation of a tool on an MCP server.

id: str

The unique ID of the tool call.

arguments: str

A JSON string of the arguments passed to the tool.

name: str

The name of the tool that was run.

server\_label: str

The label of the MCP server running the tool.

type: Literal["mcp\_call"]

The type of the item. Always `mcp_call`.

approval\_request\_id: Optional[str]

Unique identifier for the MCP tool call approval request.
Include this value in a subsequent `mcp_approval_response` input to approve or reject the corresponding tool call.

error: Optional[str]

The error from the tool call, if any.

output: Optional[str]

The output from the tool call.

status: Optional[Literal["in\_progress", "completed", "incomplete", 2 more]]

The status of the tool call. One of `in_progress`, `completed`, `incomplete`, `calling`, or `failed`.

One of the following:

"in\_progress"

"completed"

"incomplete"

"calling"

"failed"

class ResponseCustomToolCall: …

A call to a custom tool created by the model.

call\_id: str

An identifier used to map this custom tool call to a tool call output.

input: str

The input for the custom tool call generated by the model.

name: str

The name of the custom tool being called.

type: Literal["custom\_tool\_call"]

The type of the custom tool call. Always `custom_tool_call`.

id: Optional[str]

The unique ID of the custom tool call in the OpenAI platform.

namespace: Optional[str]

The namespace of the custom tool being called.

class ResponseCustomToolCallOutput: …

The output of a custom tool call from your code, being sent back to the model.

call\_id: str

The call ID, used to map this custom tool call output to a custom tool call.

output: Union[str, List[OutputOutputContentList]]

The output from the custom tool call generated by your code.
Can be a string or an list of output content.

One of the following:

str

A string of the output of the custom tool call.

List[OutputOutputContentList]

Text, image, or file output of the custom tool call.

One of the following:

class ResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

class ResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

One of the following:

"low"

"high"

"auto"

"original"

type: Literal["input\_image"]

The type of the input item. Always `input_image`.

file\_id: Optional[str]

The ID of the file to be sent to the model.

image\_url: Optional[str]

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

class ResponseInputFile: …

A file input to the model.

type: Literal["input\_file"]

The type of the input item. Always `input_file`.

detail: Optional[Literal["low", "high"]]

The detail level of the file to be sent to the model. Use `low` for the default rendering behavior, or `high` to render the file at higher quality. Defaults to `low`.

One of the following:

"low"

"high"

file\_data: Optional[str]

The content of the file to be sent to the model.

file\_id: Optional[str]

The ID of the file to be sent to the model.

file\_url: Optional[str]

The URL of the file to be sent to the model.

formaturi

filename: Optional[str]

The name of the file to be sent to the model.

type: Literal["custom\_tool\_call\_output"]

The type of the custom tool call output. Always `custom_tool_call_output`.

id: Optional[str]

The unique ID of the custom tool call output in the OpenAI platform.

### List items

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

items = client.conversations.items.list("conv_123", limit=10)
print(items.data)

  "object": "list",
  "data": [
      "type": "message",
      "id": "msg_abc",
      "status": "completed",
      "role": "user",
      "content": [
        {"type": "input_text", "text": "Hello!"}
      ]
  ],
  "first_id": "msg_abc",
  "last_id": "msg_abc",
  "has_more": false

##### Returns Examples

  "object": "list",
  "data": [
      "type": "message",
      "id": "msg_abc",
      "status": "completed",
      "role": "user",
      "content": [
        {"type": "input_text", "text": "Hello!"}
      ]
  ],
  "first_id": "msg_abc",
  "last_id": "msg_abc",
  "has_more": false
