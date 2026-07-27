<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/responses/methods/create/ -->
<!-- part of: https://developers.openai.com/api/reference/python/resources/beta/subresources/responses/methods/create/ -->

<!-- chunk-start -->

[API Reference](/api/reference/python)

[Beta](/api/reference/python/resources/beta)

[Responses](/api/reference/python/resources/beta/subresources/responses)

# Create a model response

beta.responses.create(ResponseCreateParams\*\*kwargs)  -> [BetaResponse](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema))

POST/responses

Creates a model response. Provide [text](https://platform.openai.com/docs/guides/text) or
[image](https://platform.openai.com/docs/guides/images) inputs to generate [text](https://platform.openai.com/docs/guides/text)
or [JSON](https://platform.openai.com/docs/guides/structured-outputs) outputs. Have the model call
your own [custom code](https://platform.openai.com/docs/guides/function-calling) or use built-in
[tools](https://platform.openai.com/docs/guides/tools) like [web search](https://platform.openai.com/docs/guides/tools-web-search)
or [file search](https://platform.openai.com/docs/guides/tools-file-search) to use your own data
as input for the model’s response.

##### ParametersExpand Collapse

background: Optional[bool]

Whether to run the model response in the background.
[Learn more](https://platform.openai.com/docs/guides/background).

context\_management: Optional[Iterable[ContextManagement]]

Context management configuration for this request.

type: str

The context management entry type. Currently only ‘compaction’ is supported.

compact\_threshold: Optional[int]

Token threshold at which compaction should be triggered for this entry.

minimum1000

conversation: Optional[[Conversation](/api/reference/python/resources/beta/subresources/responses/methods/create#(resource)%20beta.responses%20%3E%20(method)%20create%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20conversation%20%3E%20(schema))]

The conversation that this response belongs to. Items from this conversation are prepended to `input_items` for this response request.
Input items and output items from this response are automatically added to this conversation after this response completes.

str

The unique ID of the conversation.

class BetaResponseConversationParam: …

The conversation that this response belongs to.

id: str

The unique ID of the conversation.

include: Optional[List[[BetaResponseIncludable](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_includable%20%3E%20(schema))]]

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

input: Optional[Union[str, [BetaResponseInputParam](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input%20%3E%20(schema))]]

Text, image, or file inputs to the model, used to generate a response.

Learn more:

* [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
* [Image inputs](https://platform.openai.com/docs/guides/images)
* [File inputs](https://platform.openai.com/docs/guides/pdf-files)
* [Conversation state](https://platform.openai.com/docs/guides/conversation-state)
* [Function calling](https://platform.openai.com/docs/guides/function-calling)

str

A text input to the model, equivalent to a text input with the
`user` role.

Iterable[[BetaResponseInputItemParam](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_item%20%3E%20(schema))]

class BetaEasyInputMessage: …

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: Union[str, [BetaResponseInputMessageContentList](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_message_content_list%20%3E%20(schema))]

Text, image, or audio input to the model, used to generate a response.
Can also contain previous assistant responses.

str

A text input to the model.

List[[BetaResponseInputContent](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_content%20%3E%20(schema))]

class BetaResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

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

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class BetaResponseInputFile: …

A file input to the model.

type: Literal["input\_file"]

The type of the input item. Always `input_file`.

detail: Optional[Literal["auto", "low", "high"]]

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

"auto"

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

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

role: Literal["user", "assistant", "system", "developer"]

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

"user"

"assistant"

"system"

"developer"

phase: Optional[Literal["commentary", "final\_answer"]]

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

"commentary"

"final\_answer"

type: Optional[Literal["message"]]

The type of the message input. Always `message`.

class Message: …

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role.

content: [BetaResponseInputMessageContentList](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_message_content_list%20%3E%20(schema))

A list of one or many input items to the model, containing different content
types.

class BetaResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

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

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class BetaResponseInputFile: …

A file input to the model.

type: Literal["input\_file"]

The type of the input item. Always `input_file`.

detail: Optional[Literal["auto", "low", "high"]]

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

"auto"

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

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

role: Literal["user", "system", "developer"]

The role of the message input. One of `user`, `system`, or `developer`.

"user"

"system"

"developer"

agent: Optional[MessageAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

type: Optional[Literal["message"]]

The type of the message input. Always set to `message`.

class BetaResponseOutputMessage: …

An output message from the model.

id: str

The unique ID of the output message.

content: List[Content]

The content of the output message.

class BetaResponseOutputText: …

A text output from the model.

annotations: List[Annotation]

The annotations of the text output.

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

class BetaResponseOutputRefusal: …

A refusal from the model.

refusal: str

The refusal explanation from the model.

type: Literal["refusal"]

The type of the refusal. Always `refusal`.

role: Literal["assistant"]

The role of the output message. Always `assistant`.

status: Literal["in\_progress", "completed", "incomplete"]

The status of the message input. One of `in_progress`, `completed`, or
`incomplete`. Populated when input items are returned via API.

"in\_progress"

"completed"

"incomplete"

type: Literal["message"]

The type of the output message. Always `message`.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

phase: Optional[Literal["commentary", "final\_answer"]]

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

"commentary"

"final\_answer"

class BetaResponseFileSearchToolCall: …

The results of a file search tool call. See the
[file search guide](https://platform.openai.com/docs/guides/tools-file-search) for more information.

id: str

The unique ID of the file search tool call.

queries: List[str]

The queries used to search for files.

status: Literal["in\_progress", "searching", "completed", 2 more]

The status of the file search tool call. One of `in_progress`,
`searching`, `incomplete` or `failed`,

"in\_progress"

"searching"

"completed"

"incomplete"

"failed"

type: Literal["file\_search\_call"]

The type of the file search tool call. Always `file_search_call`.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

results: Optional[List[Result]]

The results of the file search tool call.

attributes: Optional[Dict[str, Union[str, float, bool]]]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.

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

class BetaResponseComputerToolCall: …

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

"in\_progress"

"completed"

"incomplete"

type: Literal["computer\_call"]

The type of the computer call. Always `computer_call`.

action: Optional[BetaComputerAction]

A click action.

class Click: …

A click action.

button: Literal["left", "right", "wheel", 2 more]

Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

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

actions: Optional[BetaComputerActionList]

Flattened batched actions for `computer_use`. Each action includes an
`type` discriminator and action-specific fields.

class Click: …

A click action.

button: Literal["left", "right", "wheel", 2 more]

Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

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

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class ComputerCallOutput: …

The output of a computer tool call.

call\_id: str

The ID of the computer tool call that produced the output.

maxLength64

minLength1

output: [BetaResponseComputerToolCallOutputScreenshot](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_computer_tool_call_output_screenshot%20%3E%20(schema))

A computer screenshot image used with the computer use tool.

type: Literal["computer\_screenshot"]

Specifies the event type. For a computer screenshot, this property is
always set to `computer_screenshot`.

file\_id: Optional[str]

The identifier of an uploaded file that contains the screenshot.

image\_url: Optional[str]

The URL of the screenshot image.

formaturi

type: Literal["computer\_call\_output"]

The type of the computer tool call output. Always `computer_call_output`.

id: Optional[str]

The ID of the computer tool call output.

acknowledged\_safety\_checks: Optional[List[ComputerCallOutputAcknowledgedSafetyCheck]]

The safety checks reported by the API that have been acknowledged by the developer.

id: str

The ID of the pending safety check.

code: Optional[str]

The type of the pending safety check.

message: Optional[str]

Details about the pending safety check.

agent: Optional[ComputerCallOutputAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the message input. One of `in_progress`, `completed`, or `incomplete`. Populated when input items are returned via API.

"in\_progress"

"completed"

"incomplete"

class BetaResponseFunctionWebSearch: …

The results of a web search tool call. See the
[web search guide](https://platform.openai.com/docs/guides/tools-web-search) for more information.

id: str

The unique ID of the web search tool call.

action: Action

An object describing the specific action taken in this web search call.
Includes details on how the model used the web (search, open\_page, find\_in\_page).

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

"in\_progress"

"searching"

"completed"

"failed"

type: Literal["web\_search\_call"]

The type of the web search tool call. Always `web_search_call`.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class BetaResponseFunctionToolCall: …

A tool call to run a function. See the
[function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.

arguments: str

A JSON string of the arguments to pass to the function.

call\_id: str

The unique ID of the function tool call generated by the model.

name: str

The name of the function to run.

type: Literal["function\_call"]

The type of the function tool call. Always `function_call`.

id: Optional[str]

The unique ID of the function tool call.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

caller: Optional[Caller]

The execution context that produced this tool call.

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

The call ID of the program item that produced this tool call.

type: Literal["program"]

namespace: Optional[str]

The namespace of the function to run.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

class FunctionCallOutput: …

The output of a function tool call.

call\_id: str

The unique ID of the function tool call generated by the model.

maxLength64

minLength1

output: Union[str, [BetaResponseFunctionCallOutputItemList](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_call_output_item_list%20%3E%20(schema))]

Text, image, or file output of the function tool call.

str

A JSON string of the output of the function tool call.

List[[BetaResponseFunctionCallOutputItem](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_call_output_item%20%3E%20(schema))]

class BetaResponseInputTextContent: …

A text input to the model.

text: str

The text input to the model.

maxLength10485760

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class BetaResponseInputImageContent: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision)

type: Literal["input\_image"]

The type of the input item. Always `input_image`.

detail: Optional[Literal["low", "high", "auto", "original"]]

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

"low"

"high"

"auto"

"original"

file\_id: Optional[str]

The ID of the file to be sent to the model.

image\_url: Optional[str]

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

maxLength20971520

formaturi

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class BetaResponseInputFileContent: …

A file input to the model.

type: Literal["input\_file"]

The type of the input item. Always `input_file`.

detail: Optional[Literal["auto", "low", "high"]]

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

"auto"

"low"

"high"

file\_data: Optional[str]

The base64-encoded data of the file to be sent to the model.

maxLength73400320

file\_id: Optional[str]

The ID of the file to be sent to the model.

file\_url: Optional[str]

The URL of the file to be sent to the model.

formaturi

filename: Optional[str]

The name of the file to be sent to the model.

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

type: Literal["function\_call\_output"]

The type of the function tool call output. Always `function_call_output`.

id: Optional[str]

The unique ID of the function tool call output. Populated when this item is returned via API.

agent: Optional[FunctionCallOutputAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

caller: Optional[FunctionCallOutputCaller]

The execution context that produced this tool call.

class FunctionCallOutputCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class FunctionCallOutputCallerProgram: …

caller\_id: str

The call ID of the program item that produced this tool call.

maxLength64

minLength1

type: Literal["program"]

The caller type. Always `program`.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the item. One of `in_progress`, `completed`, or `incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

class AgentMessage: …

A message routed between agents.

author: str

The sending agent identity.

content: List[AgentMessageContent]

Plaintext, image, or encrypted content sent between agents.

class BetaResponseInputTextContent: …

A text input to the model.

text: str

The text input to the model.

maxLength10485760

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class BetaResponseInputImageContent: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision)

type: Literal["input\_image"]

The type of the input item. Always `input_image`.

detail: Optional[Literal["low", "high", "auto", "original"]]

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

"low"

"high"

"auto"

"original"

file\_id: Optional[str]

The ID of the file to be sent to the model.

image\_url: Optional[str]

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

maxLength20971520

formaturi

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class AgentMessageContentEncryptedContent: …

Opaque encrypted content that Responses API decrypts inside trusted model execution.

encrypted\_content: str

Opaque encrypted content.

maxLength10485760

type: Literal["encrypted\_content"]

The type of the input item. Always `encrypted_content`.

recipient: str

The destination agent identity.

type: Literal["agent\_message"]

The item type. Always `agent_message`.

id: Optional[str]

The unique ID of this agent message item.

agent: Optional[AgentMessageAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class MultiAgentCall: …

action: Literal["spawn\_agent", "interrupt\_agent", "list\_agents", 3 more]

The multi-agent action that was executed.

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

arguments: str

The action arguments as a JSON string.

call\_id: str

The unique ID linking this call to its output.

maxLength64

minLength1

type: Literal["multi\_agent\_call"]

The item type. Always `multi_agent_call`.

id: Optional[str]

The unique ID of this multi-agent call.

agent: Optional[MultiAgentCallAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class MultiAgentCallOutput: …

action: Literal["spawn\_agent", "interrupt\_agent", "list\_agents", 3 more]

The multi-agent action that produced this result.

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

call\_id: str

The unique ID of the multi-agent call.

maxLength64

minLength1

output: List[MultiAgentCallOutputOutput]

Text output returned by the multi-agent action.

text: str

The text content.

maxLength10485760

type: Literal["output\_text"]

The content type. Always `output_text`.

annotations: Optional[List[MultiAgentCallOutputOutputAnnotation]]

Citations associated with the text content.

class MultiAgentCallOutputOutputAnnotationFileCitation: …

file\_id: str

The ID of the file.

filename: str

The filename of the file cited.

index: int

The index of the file in the list of files.

minimum0

type: Literal["file\_citation"]

The citation type. Always `file_citation`.

class MultiAgentCallOutputOutputAnnotationURLCitation: …

end\_index: int

The index of the last character of the citation in the message.

minimum0

start\_index: int

The index of the first character of the citation in the message.

minimum0

title: str

The title of the cited resource.

type: Literal["url\_citation"]

The citation type. Always `url_citation`.

url: str

The URL of the cited resource.

formaturi

class MultiAgentCallOutputOutputAnnotationContainerFileCitation: …

container\_id: str

The ID of the container.

end\_index: int

The index of the last character of the citation in the message.

minimum0

file\_id: str

The ID of the container file.

filename: str

The filename of the container file cited.

start\_index: int

The index of the first character of the citation in the message.

minimum0

type: Literal["container\_file\_citation"]

The citation type. Always `container_file_citation`.

type: Literal["multi\_agent\_call\_output"]

The item type. Always `multi_agent_call_output`.

id: Optional[str]

The unique ID of this multi-agent call output.

agent: Optional[MultiAgentCallOutputAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class ToolSearchCall: …

arguments: object

The arguments supplied to the tool search call.

type: Literal["tool\_search\_call"]

The item type. Always `tool_search_call`.

id: Optional[str]

The unique ID of this tool search call.

agent: Optional[ToolSearchCallAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

call\_id: Optional[str]

The unique ID of the tool search call generated by the model.

maxLength64

minLength1

execution: Optional[Literal["server", "client"]]

Whether tool search was executed by the server or by the client.

"server"

"client"

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the tool search call.

"in\_progress"

"completed"

"incomplete"

class BetaResponseToolSearchOutputItemParam: …

tools: List[[BetaTool](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))]

The loaded tool definitions returned by the tool search output.

class BetaFunctionTool: …

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

name: str

The name of the function to call.

parameters: Optional[Dict[str, object]]

A JSON schema object describing the parameters of the function.

strict: Optional[bool]

Whether strict parameter validation is enforced for this function tool.

type: Literal["function"]

The type of the function tool. Always `function`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: Optional[bool]

Whether this function is deferred and loaded via tool search.

description: Optional[str]

A description of the function. Used by the model to determine whether or not to call the function.

output\_schema: Optional[Dict[str, object]]

A JSON schema object describing the JSON value encoded in string outputs for this function.

class BetaFileSearchTool: …

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

type: Literal["file\_search"]

The type of the file search tool. Always `file_search`.

vector\_store\_ids: List[str]

The IDs of the vector stores to search.

filters: Optional[Filters]

A filter to apply.

class FiltersComparisonFilter: …

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

str

float

bool

List[Union[str, float]]

str

float

class FiltersCompoundFilter: …

Combine multiple filters using `and` or `or`.

filters: List[FiltersCompoundFilterFilter]

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

class FiltersCompoundFilterFilterComparisonFilter: …

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

str

float

bool

List[Union[str, float]]

str

float

object

type: Literal["and", "or"]

Type of operation: `and` or `or`.

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

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

class BetaComputerTool: …

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

type: Literal["computer"]

The type of the computer tool. Always `computer`.

class BetaComputerUsePreviewTool: …

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

display\_height: int

The height of the computer display.

display\_width: int

The width of the computer display.

environment: Literal["windows", "mac", "linux", 2 more]

The type of computer environment to control.

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

The type of the computer use tool. Always `computer_use_preview`.

class BetaWebSearchTool: …

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

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

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

allowed\_tools: Optional[McpAllowedTools]

List of allowed tool names or a filter object.

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

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

A list of allowed domains when type is `allowlist`.

type: Literal["allowlist"]

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

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

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

class ProgrammaticToolCalling: …

type: Literal["programmatic\_tool\_calling"]

The type of the tool. Always `programmatic_tool_calling`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

The type of the image generation tool. Always `image_generation`.

action: Optional[Literal["generate", "edit", "auto"]]

Whether to generate a new image or edit an existing image. Default: `auto`.

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

"transparent"

"opaque"

"auto"

input\_fidelity: Optional[Literal["high", "low"]]

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

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

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

The image generation model to use. Default: `gpt-image-1`.

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

Moderation level for the generated image. Default: `auto`.

"auto"

"low"

output\_compression: Optional[int]

Compression level for the output image. Default: 100.

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

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

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool: …

A tool that allows the model to execute shell commands.

type: Literal["shell"]

The type of the shell tool. Always `shell`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

environment: Optional[Environment]

class BetaContainerAuto: …

type: Literal["container\_auto"]

Automatically creates a container for this request

file\_ids: Optional[List[str]]

An optional list of uploaded files to make available to your code.

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

The memory limit for the container.

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

A list of allowed domains when type is `allowlist`.

type: Literal["allowlist"]

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

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

class BetaSkillReference: …

skill\_id: str

The ID of the referenced skill.

maxLength64

minLength1

type: Literal["skill\_reference"]

References a skill created with the /v1/skills endpoint.

version: Optional[str]

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

class BetaInlineSkill: …

description: str

The description of the skill.

name: str

The name of the skill.

source: [BetaInlineSkillSource](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

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

class BetaLocalEnvironment: …

type: Literal["local"]

Use a local computer environment.

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

An optional list of skills.

description: str

The description of the skill.

name: str

The name of the skill.

path: str

The path to the directory containing the skill.

class BetaContainerReference: …

container\_id: str

The ID of the referenced container.

type: Literal["container\_reference"]

References a container created with the /v1/containers endpoint

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

The name of the custom tool, used to identify it in tool calls.

type: Literal["custom"]

The type of the custom tool. Always `custom`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: Optional[bool]

Whether this tool should be deferred and discovered via tool search.

description: Optional[str]

Optional description of the custom tool, used to provide more context.

format: Optional[Format]

The input format for the custom tool. Default is unconstrained text.

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

A grammar defined by the user.

definition: str

The grammar definition.

syntax: Literal["lark", "regex"]

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: Literal["grammar"]

Grammar format. Always `grammar`.

class BetaNamespaceTool: …

Groups function/custom tools under a shared namespace.

description: str

A description of the namespace shown to the model.

minLength1

name: str

The namespace name used in tool calls (for example, `crm`).

minLength1

tools: List[Tool]

The function/custom tools available inside this namespace.

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: Optional[bool]

Whether this function should be deferred and discovered via tool search.

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

parameters: Optional[object]

strict: Optional[bool]

Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

The name of the custom tool, used to identify it in tool calls.

type: Literal["custom"]

The type of the custom tool. Always `custom`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: Optional[bool]

Whether this tool should be deferred and discovered via tool search.

description: Optional[str]

Optional description of the custom tool, used to provide more context.

format: Optional[Format]

The input format for the custom tool. Default is unconstrained text.

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

A grammar defined by the user.

definition: str

The grammar definition.

syntax: Literal["lark", "regex"]

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: Literal["grammar"]

Grammar format. Always `grammar`.

type: Literal["namespace"]

The type of the tool. Always `namespace`.

class BetaToolSearchTool: …

Hosted or BYOT tool search configuration for deferred tools.

type: Literal["tool\_search"]

The type of the tool. Always `tool_search`.

description: Optional[str]

Description shown to the model for a client-executed tool search tool.

execution: Optional[Literal["server", "client"]]

Whether tool search is executed by the server or by the client.

"server"

"client"

parameters: Optional[object]

Parameter schema for a client-executed tool search tool.

class BetaWebSearchPreviewTool: …

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

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

class BetaApplyPatchTool: …

Allows the assistant to create, delete, or update files using unified diffs.

type: Literal["apply\_patch"]

The type of the tool. Always `apply_patch`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

type: Literal["tool\_search\_output"]

The item type. Always `tool_search_output`.

id: Optional[str]

The unique ID of this tool search output.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

call\_id: Optional[str]

The unique ID of the tool search call generated by the model.

maxLength64

minLength1

execution: Optional[Literal["server", "client"]]

Whether tool search was executed by the server or by the client.

"server"

"client"

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the tool search output.

"in\_progress"

"completed"

"incomplete"

class AdditionalTools: …

role: Literal["developer"]

The role that provided the additional tools. Only `developer` is supported.

tools: List[[BetaTool](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))]

A list of additional tools made available at this item.

class BetaFunctionTool: …

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

name: str

The name of the function to call.

parameters: Optional[Dict[str, object]]

A JSON schema object describing the parameters of the function.

strict: Optional[bool]

Whether strict parameter validation is enforced for this function tool.

type: Literal["function"]

The type of the function tool. Always `function`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: Optional[bool]

Whether this function is deferred and loaded via tool search.

description: Optional[str]

A description of the function. Used by the model to determine whether or not to call the function.

output\_schema: Optional[Dict[str, object]]

A JSON schema object describing the JSON value encoded in string outputs for this function.

class BetaFileSearchTool: …

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

type: Literal["file\_search"]

The type of the file search tool. Always `file_search`.

vector\_store\_ids: List[str]

The IDs of the vector stores to search.

filters: Optional[Filters]

A filter to apply.

class FiltersComparisonFilter: …

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

str

float

bool

List[Union[str, float]]

str

float

class FiltersCompoundFilter: …

Combine multiple filters using `and` or `or`.

filters: List[FiltersCompoundFilterFilter]

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

class FiltersCompoundFilterFilterComparisonFilter: …

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

str

float

bool

List[Union[str, float]]

str

float

object

type: Literal["and", "or"]

Type of operation: `and` or `or`.

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

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

class BetaComputerTool: …

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

type: Literal["computer"]

The type of the computer tool. Always `computer`.

class BetaComputerUsePreviewTool: …

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

display\_height: int

The height of the computer display.

display\_width: int

The width of the computer display.

environment: Literal["windows", "mac", "linux", 2 more]

The type of computer environment to control.

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

The type of the computer use tool. Always `computer_use_preview`.

class BetaWebSearchTool: …

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

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

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

allowed\_tools: Optional[McpAllowedTools]

List of allowed tool names or a filter object.

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

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

A list of allowed domains when type is `allowlist`.

type: Literal["allowlist"]

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

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

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

class ProgrammaticToolCalling: …

type: Literal["programmatic\_tool\_calling"]

The type of the tool. Always `programmatic_tool_calling`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

The type of the image generation tool. Always `image_generation`.

action: Optional[Literal["generate", "edit", "auto"]]

Whether to generate a new image or edit an existing image. Default: `auto`.

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

"transparent"

"opaque"

"auto"

input\_fidelity: Optional[Literal["high", "low"]]

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

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

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

The image generation model to use. Default: `gpt-image-1`.

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

Moderation level for the generated image. Default: `auto`.

"auto"

"low"

output\_compression: Optional[int]

Compression level for the output image. Default: 100.

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

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

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool: …

A tool that allows the model to execute shell commands.

type: Literal["shell"]

The type of the shell tool. Always `shell`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

environment: Optional[Environment]

class BetaContainerAuto: …

type: Literal["container\_auto"]

Automatically creates a container for this request

file\_ids: Optional[List[str]]

An optional list of uploaded files to make available to your code.

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

The memory limit for the container.

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

A list of allowed domains when type is `allowlist`.

type: Literal["allowlist"]

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

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

class BetaSkillReference: …

skill\_id: str

The ID of the referenced skill.

maxLength64

minLength1

type: Literal["skill\_reference"]

References a skill created with the /v1/skills endpoint.

version: Optional[str]

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

class BetaInlineSkill: …

description: str

The description of the skill.

name: str

The name of the skill.

source: [BetaInlineSkillSource](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

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

class BetaLocalEnvironment: …

type: Literal["local"]

Use a local computer environment.

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

An optional list of skills.

description: str

The description of the skill.

name: str

The name of the skill.

path: str

The path to the directory containing the skill.

class BetaContainerReference: …

container\_id: str

The ID of the referenced container.

type: Literal["container\_reference"]

References a container created with the /v1/containers endpoint

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

The name of the custom tool, used to identify it in tool calls.

type: Literal["custom"]

The type of the custom tool. Always `custom`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: Optional[bool]

Whether this tool should be deferred and discovered via tool search.

description: Optional[str]

Optional description of the custom tool, used to provide more context.

format: Optional[Format]

The input format for the custom tool. Default is unconstrained text.

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

A grammar defined by the user.

definition: str

The grammar definition.

syntax: Literal["lark", "regex"]

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: Literal["grammar"]

Grammar format. Always `grammar`.

class BetaNamespaceTool: …

Groups function/custom tools under a shared namespace.

description: str

A description of the namespace shown to the model.

minLength1

name: str

The namespace name used in tool calls (for example, `crm`).

minLength1

tools: List[Tool]

The function/custom tools available inside this namespace.

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: Optional[bool]

Whether this function should be deferred and discovered via tool search.

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

parameters: Optional[object]

strict: Optional[bool]

Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

The name of the custom tool, used to identify it in tool calls.

type: Literal["custom"]

The type of the custom tool. Always `custom`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: Optional[bool]

Whether this tool should be deferred and discovered via tool search.

description: Optional[str]

Optional description of the custom tool, used to provide more context.

format: Optional[Format]

The input format for the custom tool. Default is unconstrained text.

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

A grammar defined by the user.

definition: str

The grammar definition.

syntax: Literal["lark", "regex"]

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: Literal["grammar"]

Grammar format. Always `grammar`.

type: Literal["namespace"]

The type of the tool. Always `namespace`.

class BetaToolSearchTool: …

Hosted or BYOT tool search configuration for deferred tools.

type: Literal["tool\_search"]

The type of the tool. Always `tool_search`.

description: Optional[str]

Description shown to the model for a client-executed tool search tool.

execution: Optional[Literal["server", "client"]]

Whether tool search is executed by the server or by the client.

"server"

"client"

parameters: Optional[object]

Parameter schema for a client-executed tool search tool.

class BetaWebSearchPreviewTool: …

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

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

class BetaApplyPatchTool: …

Allows the assistant to create, delete, or update files using unified diffs.

type: Literal["apply\_patch"]

The type of the tool. Always `apply_patch`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

type: Literal["additional\_tools"]

The item type. Always `additional_tools`.

id: Optional[str]

The unique ID of this additional tools item.

agent: Optional[AdditionalToolsAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class BetaResponseReasoningItem: …

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

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

content: Optional[List[Content]]

Reasoning text content.

text: str

The reasoning text from the model.

type: Literal["reasoning\_text"]

The type of the reasoning text. Always `reasoning_text`.

encrypted\_content: Optional[str]

The encrypted content of the reasoning item. This is populated by default
for reasoning items returned by `POST /v1/responses` and WebSocket
`response.create` requests.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

class BetaResponseCompactionItemParam: …

A compaction item generated by the [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).

encrypted\_content: str

The encrypted content of the compaction summary.

maxLength10485760

type: Literal["compaction"]

The type of the item. Always `compaction`.

id: Optional[str]

The ID of the compaction item.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class ImageGenerationCall: …

An image generation request made by the model.

id: str

The unique ID of the image generation call.

result: Optional[str]

The generated image encoded in base64.

status: Literal["in\_progress", "completed", "generating", "failed"]

The status of the image generation call.

"in\_progress"

"completed"

"generating"

"failed"

type: Literal["image\_generation\_call"]

The type of the image generation call. Always `image_generation_call`.

agent: Optional[ImageGenerationCallAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class BetaResponseCodeInterpreterToolCall: …

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

"in\_progress"

"completed"

"incomplete"

"interpreting"

"failed"

type: Literal["code\_interpreter\_call"]

The type of the code interpreter tool call. Always `code_interpreter_call`.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

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

"in\_progress"

"completed"

"incomplete"

type: Literal["local\_shell\_call"]

The type of the local shell call. Always `local_shell_call`.

agent: Optional[LocalShellCallAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class LocalShellCallOutput: …

The output of a local shell tool call.

id: str

The unique ID of the local shell tool call generated by the model.

output: str

A JSON string of the output of the local shell tool call.

type: Literal["local\_shell\_call\_output"]

The type of the local shell tool call output. Always `local_shell_call_output`.

agent: Optional[LocalShellCallOutputAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the item. One of `in_progress`, `completed`, or `incomplete`.

"in\_progress"

"completed"

"incomplete"

class ShellCall: …

A tool representing a request to execute one or more shell commands.

action: ShellCallAction

The shell commands and limits that describe how to run the tool call.

commands: List[str]

Ordered shell commands for the execution environment to run.

max\_output\_length: Optional[int]

Maximum number of UTF-8 characters to capture from combined stdout and stderr output.

timeout\_ms: Optional[int]

Maximum wall-clock time in milliseconds to allow the shell commands to run.

call\_id: str

The unique ID of the shell tool call generated by the model.

maxLength64

minLength1

type: Literal["shell\_call"]

The type of the item. Always `shell_call`.

id: Optional[str]

The unique ID of the shell tool call. Populated when this item is returned via API.

agent: Optional[ShellCallAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

caller: Optional[ShellCallCaller]

The execution context that produced this tool call.

class ShellCallCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class ShellCallCallerProgram: …

caller\_id: str

The call ID of the program item that produced this tool call.

maxLength64

minLength1

type: Literal["program"]

The caller type. Always `program`.

environment: Optional[ShellCallEnvironment]

The environment to execute the shell commands in.

class BetaLocalEnvironment: …

type: Literal["local"]

Use a local computer environment.

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

An optional list of skills.

description: str

The description of the skill.

name: str

The name of the skill.

path: str

The path to the directory containing the skill.

class BetaContainerReference: …

container\_id: str

The ID of the referenced container.

type: Literal["container\_reference"]

References a container created with the /v1/containers endpoint

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the shell call. One of `in_progress`, `completed`, or `incomplete`.

"in\_progress"

"completed"

"incomplete"

class ShellCallOutput: …

The streamed output items emitted by a shell tool call.

call\_id: str

The unique ID of the shell tool call generated by the model.

maxLength64

minLength1

output: List[[BetaResponseFunctionShellCallOutputContent](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_shell_call_output_content%20%3E%20(schema))]

Captured chunks of stdout and stderr output, along with their associated outcomes.

outcome: Outcome

The exit or timeout outcome associated with this shell call.

class OutcomeTimeout: …

Indicates that the shell call exceeded its configured time limit.

type: Literal["timeout"]

The outcome type. Always `timeout`.

class OutcomeExit: …

Indicates that the shell commands finished and returned an exit code.

exit\_code: int

The exit code returned by the shell process.

type: Literal["exit"]

The outcome type. Always `exit`.

stderr: str

Captured stderr output for the shell call.

maxLength10485760

stdout: str

Captured stdout output for the shell call.

maxLength10485760

type: Literal["shell\_call\_output"]

The type of the item. Always `shell_call_output`.

id: Optional[str]

The unique ID of the shell tool call output. Populated when this item is returned via API.

agent: Optional[ShellCallOutputAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

caller: Optional[ShellCallOutputCaller]

The execution context that produced this tool call.

class ShellCallOutputCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class ShellCallOutputCallerProgram: …

caller\_id: str

The call ID of the program item that produced this tool call.

maxLength64

minLength1

type: Literal["program"]

The caller type. Always `program`.

max\_output\_length: Optional[int]

The maximum number of UTF-8 characters captured for this shell call’s combined output.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the shell call output.

"in\_progress"

"completed"

"incomplete"

class ApplyPatchCall: …

A tool call representing a request to create, delete, or update files using diff patches.

call\_id: str

The unique ID of the apply patch tool call generated by the model.

maxLength64

minLength1

operation: ApplyPatchCallOperation

The specific create, delete, or update instruction for the apply\_patch tool call.

class ApplyPatchCallOperationCreateFile: …

Instruction for creating a new file via the apply\_patch tool.

diff: str

Unified diff content to apply when creating the file.

maxLength10485760

path: str

Path of the file to create relative to the workspace root.

minLength1

type: Literal["create\_file"]

The operation type. Always `create_file`.

class ApplyPatchCallOperationDeleteFile: …

Instruction for deleting an existing file via the apply\_patch tool.

path: str

Path of the file to delete relative to the workspace root.

minLength1

type: Literal["delete\_file"]

The operation type. Always `delete_file`.

class ApplyPatchCallOperationUpdateFile: …

Instruction for updating an existing file via the apply\_patch tool.

diff: str

Unified diff content to apply to the existing file.

maxLength10485760

path: str

Path of the file to update relative to the workspace root.

minLength1

type: Literal["update\_file"]

The operation type. Always `update_file`.

status: Literal["in\_progress", "completed"]

The status of the apply patch tool call. One of `in_progress` or `completed`.

"in\_progress"

"completed"

type: Literal["apply\_patch\_call"]

The type of the item. Always `apply_patch_call`.

id: Optional[str]

The unique ID of the apply patch tool call. Populated when this item is returned via API.

agent: Optional[ApplyPatchCallAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

caller: Optional[ApplyPatchCallCaller]

The execution context that produced this tool call.

class ApplyPatchCallCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class ApplyPatchCallCallerProgram: …

caller\_id: str

The call ID of the program item that produced this tool call.

maxLength64

minLength1

type: Literal["program"]

The caller type. Always `program`.

class ApplyPatchCallOutput: …

The streamed output emitted by an apply patch tool call.

call\_id: str

The unique ID of the apply patch tool call generated by the model.

maxLength64

minLength1

status: Literal["completed", "failed"]

The status of the apply patch tool call output. One of `completed` or `failed`.

"completed"

"failed"

type: Literal["apply\_patch\_call\_output"]

The type of the item. Always `apply_patch_call_output`.

id: Optional[str]

The unique ID of the apply patch tool call output. Populated when this item is returned via API.

agent: Optional[ApplyPatchCallOutputAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

caller: Optional[ApplyPatchCallOutputCaller]

The execution context that produced this tool call.

class ApplyPatchCallOutputCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class ApplyPatchCallOutputCallerProgram: …

caller\_id: str

The call ID of the program item that produced this tool call.

maxLength64

minLength1

type: Literal["program"]

The caller type. Always `program`.

output: Optional[str]

Optional human-readable log text from the apply patch tool (e.g., patch results or errors).

maxLength10485760

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

agent: Optional[McpListToolsAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

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

agent: Optional[McpApprovalRequestAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class McpApprovalResponse: …

A response to an MCP approval request.

approval\_request\_id: str

The ID of the approval request being answered.

approve: bool

Whether the request was approved.

type: Literal["mcp\_approval\_response"]

The type of the item. Always `mcp_approval_response`.

id: Optional[str]

The unique ID of the approval response

agent: Optional[McpApprovalResponseAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

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

agent: Optional[McpCallAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

approval\_request\_id: Optional[str]

Unique identifier for the MCP tool call approval request.
Include this value in a subsequent `mcp_approval_response` input to approve or reject the corresponding tool call.

error: Optional[str]

The error from the tool call, if any.

output: Optional[str]

The output from the tool call.

status: Optional[Literal["in\_progress", "completed", "incomplete", 2 more]]

The status of the tool call. One of `in_progress`, `completed`, `incomplete`, `calling`, or `failed`.

"in\_progress"

"completed"

"incomplete"

"calling"

"failed"

class BetaResponseCustomToolCallOutput: …

The output of a custom tool call from your code, being sent back to the model.

call\_id: str

The call ID, used to map this custom tool call output to a custom tool call.

output: Union[str, List[OutputOutputContentList]]

The output from the custom tool call generated by your code.
Can be a string or an list of output content.

str

A string of the output of the custom tool call.

List[OutputOutputContentList]

Text, image, or file output of the custom tool call.

class BetaResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

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

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class BetaResponseInputFile: …

A file input to the model.

type: Literal["input\_file"]

The type of the input item. Always `input_file`.

detail: Optional[Literal["auto", "low", "high"]]

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

"auto"

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

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

type: Literal["custom\_tool\_call\_output"]

The type of the custom tool call output. Always `custom_tool_call_output`.

id: Optional[str]

The unique ID of the custom tool call output in the OpenAI platform.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

caller: Optional[Caller]

The execution context that produced this tool call.

class CallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class CallerProgram: …

caller\_id: str

The call ID of the program item that produced this tool call.

maxLength64

minLength1

type: Literal["program"]

The caller type. Always `program`.

class BetaResponseCustomToolCall: …

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

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

caller: Optional[Caller]

The execution context that produced this tool call.

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

The call ID of the program item that produced this tool call.

type: Literal["program"]

namespace: Optional[str]

The namespace of the custom tool being called.

class CompactionTrigger: …

Compacts the current context. Must be the final input item.

type: Literal["compaction\_trigger"]

The type of the item. Always `compaction_trigger`.

agent: Optional[CompactionTriggerAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class ItemReference: …

An internal identifier for an item to reference.

id: str

The ID of the item to reference.

agent: Optional[ItemReferenceAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

type: Optional[Literal["item\_reference"]]

The type of item to reference. Always `item_reference`.

class Program: …

id: str

The unique ID of this program item.

call\_id: str

The stable call ID of the program item.

maxLength64

minLength1

code: str

The JavaScript source executed by programmatic tool calling.

maxLength10485760

fingerprint: str

Opaque program replay fingerprint that must be round-tripped.

maxLength10485760

type: Literal["program"]

The item type. Always `program`.

agent: Optional[ProgramAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class ProgramOutput: …

id: str

The unique ID of this program output item.

call\_id: str

The call ID of the program item.

maxLength64

minLength1

result: str

The result produced by the program item.

maxLength10485760

status: Literal["completed", "incomplete"]

The terminal status of the program output.

"completed"

"incomplete"

type: Literal["program\_output"]

The item type. Always `program_output`.

agent: Optional[ProgramOutputAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

instructions: Optional[str]

A system (or developer) message inserted into the model’s context.

When using along with `previous_response_id`, the instructions from a previous
response will not be carried over to the next response. This makes it simple
to swap out system (or developer) messages in new responses.

max\_output\_tokens: Optional[int]

An upper bound for the number of tokens that can be generated for a response, including visible output tokens and [reasoning tokens](https://platform.openai.com/docs/guides/reasoning).

minimum16

max\_tool\_calls: Optional[int]

The maximum number of total calls to built-in tools that can be processed in a response. This maximum number applies across all built-in tool calls, not per individual tool. Any further attempts to call a tool by the model will be ignored.

metadata: Optional[Dict[str, str]]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: Optional[Union[Literal["gpt-5.6-sol", "gpt-5.6-terra", "gpt-5.6-luna", 92 more], str]]

Model ID used to generate the response, like `gpt-4o` or `o3`. OpenAI
offers a wide range of models with different capabilities, performance
characteristics, and price points. Refer to the [model guide](https://platform.openai.com/docs/models)
to browse and compare available models.

Literal["gpt-5.6-sol", "gpt-5.6-terra", "gpt-5.6-luna", 92 more]

Model ID used to generate the response, like `gpt-4o` or `o3`. OpenAI
offers a wide range of models with different capabilities, performance
characteristics, and price points. Refer to the [model guide](https://platform.openai.com/docs/models)
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

str

moderation: Optional[[Moderation](/api/reference/python/resources/beta/subresources/responses/methods/create#(resource)%20beta.responses%20%3E%20(method)%20create%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20moderation%20%3E%20(schema))]

Configuration for running moderation on the input and output of this response.

model: str

The moderation model to use for moderated completions, e.g. ‘omni-moderation-latest’.

policy: Optional[ModerationPolicy]

The policy to apply to moderated response input and output.

input: Optional[ModerationPolicyInput]

The moderation policy for the response input.

mode: Literal["score", "block"]

"score"

"block"

output: Optional[ModerationPolicyOutput]

The moderation policy for the response output.

mode: Literal["score", "block"]

"score"

"block"

multi\_agent: Optional[[MultiAgent](/api/reference/python/resources/beta/subresources/responses/methods/create#(resource)%20beta.responses%20%3E%20(method)%20create%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20multi_agent%20%3E%20(schema))]

Configuration for server-hosted multi-agent execution.

enabled: bool

Whether to enable server-hosted multi-agent execution for this response.

max\_concurrent\_subagents: Optional[int]

`max_concurrent_subagents` sets the maximum number of subagents that can be active simultaneously across the entire agent tree. It includes all descendants—children, grandchildren, and deeper subagents—but excludes the root agent.
The API does not impose a fixed upper bound on this setting. The default is `3`, which is recommended for most workloads. Multi-agent runs also have no fixed limit on tree depth or the total number of subagents created during a run.

minimum1

parallel\_tool\_calls: Optional[bool]

Whether to allow the model to run tool calls in parallel.

previous\_response\_id: Optional[str]

The unique ID of the previous response to the model. Use this to
create multi-turn conversations. Learn more about
[conversation state](https://platform.openai.com/docs/guides/conversation-state). Cannot be used in conjunction with `conversation`.

prompt: Optional[BetaResponsePromptParam]

Reference to a prompt template and its variables.
[Learn more](https://platform.openai.com/docs/guides/text?api-mode=responses#reusable-prompts).

id: str

The unique identifier of the prompt template to use.

variables: Optional[Dict[str, Variables]]

Optional map of values to substitute in for variables in your
prompt. The substitution values can either be strings, or other
Response input types like images or files.

str

class BetaResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

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

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class BetaResponseInputFile: …

A file input to the model.

type: Literal["input\_file"]

The type of the input item. Always `input_file`.

detail: Optional[Literal["auto", "low", "high"]]

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

"auto"

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

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

version: Optional[str]

Optional version of the prompt template.

prompt\_cache\_key: Optional[str]

Used by OpenAI to cache responses for similar requests to optimize your cache hit rates. Replaces the `user` field. [Learn more](https://platform.openai.com/docs/guides/prompt-caching).

prompt\_cache\_options: Optional[[PromptCacheOptions](/api/reference/python/resources/beta/subresources/responses/methods/create#(resource)%20beta.responses%20%3E%20(method)%20create%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20prompt_cache_options%20%3E%20(schema))]

Options for prompt caching. Supported for `gpt-5.6` and later models. By default, OpenAI automatically chooses one implicit cache breakpoint. You can add explicit breakpoints to content blocks with `prompt_cache_breakpoint`. Each request can write up to four breakpoints. For cache matching, OpenAI considers up to the latest 80 breakpoints in the conversation, without a content-block lookback limit. Set `mode` to `explicit` to disable the implicit breakpoint. The `ttl` defaults to `30m`, which is currently the only supported value. See the [prompt caching guide](https://platform.openai.com/docs/guides/prompt-caching) for current details.

mode: Optional[Literal["implicit", "explicit"]]

Controls whether OpenAI automatically creates an implicit cache breakpoint. Defaults to `implicit`. With `implicit`, OpenAI creates one implicit breakpoint and writes up to the latest three explicit breakpoints in the request. With `explicit`, OpenAI does not create an implicit breakpoint and writes up to the latest four explicit breakpoints. If there are no explicit breakpoints, the request does not use prompt caching.

"implicit"

"explicit"

ttl: Optional[Literal["30m"]]

The minimum lifetime applied to every implicit and explicit cache breakpoint written by the request. Defaults to `30m`, which is currently the only supported value. The backend may retain cache entries for longer.

Deprecatedprompt\_cache\_retention: Optional[Literal["in\_memory", "24h"]]

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

reasoning: Optional[[Reasoning](/api/reference/python/resources/beta/subresources/responses/methods/create#(resource)%20beta.responses%20%3E%20(method)%20create%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20reasoning%20%3E%20(schema))]

**gpt-5 and o-series models only**

Configuration options for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).

context: Optional[Literal["auto", "current\_turn", "all\_turns"]]

Controls which reasoning items are rendered back to the model on later turns.
If omitted or set to `auto`, the model determines the context mode. The
`gpt-5.6` model family defaults to `all_turns`; earlier models default to
`current_turn`.

When returned on a response, this is the effective reasoning context mode
used for the response.

"auto"

"current\_turn"

"all\_turns"

effort: Optional[Literal["none", "minimal", "low", 4 more]]

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

Deprecatedgenerate\_summary: Optional[Literal["auto", "concise", "detailed"]]

**Deprecated:** use `summary` instead.

A summary of the reasoning performed by the model. This can be
useful for debugging and understanding the model’s reasoning process.
One of `auto`, `concise`, or `detailed`.

"auto"

"concise"

"detailed"

mode: Optional[Union[str, Literal["standard", "pro"]]]

Controls the reasoning execution mode for the request.

When returned on a response, this is the effective execution mode.

str

Literal["standard", "pro"]

Controls the reasoning execution mode for the request.

When returned on a response, this is the effective execution mode.

"standard"

"pro"

summary: Optional[Literal["auto", "concise", "detailed"]]

A summary of the reasoning performed by the model. This can be
useful for debugging and understanding the model’s reasoning process.
One of `auto`, `concise`, or `detailed`.

`concise` is supported for `computer-use-preview` models and all reasoning models after `gpt-5`.

"auto"

"concise"

"detailed"

safety\_identifier: Optional[str]

A stable identifier used to help detect users of your application that may be violating OpenAI’s usage policies.
The IDs should be a string that uniquely identifies each user, with a maximum length of 64 characters. We recommend hashing their username or email address, in order to avoid sending us any identifying information. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).

maxLength64

service\_tier: Optional[Literal["auto", "default", "flex", 2 more]]

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

store: Optional[bool]

Whether to store the generated model response for later retrieval via
API.

stream: Optional[Literal[false]]

If set to true, the model response data will be streamed to the client
as it is generated using [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format).
See the [Streaming section below](https://platform.openai.com/docs/api-reference/responses-streaming)
for more information.

stream\_options: Optional[[StreamOptions](/api/reference/python/resources/beta/subresources/responses/methods/create#(resource)%20beta.responses%20%3E%20(method)%20create%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20stream_options%20%3E%20(schema))]

Options for streaming responses. Only set this when you set `stream: true`.

include\_obfuscation: Optional[bool]

When true, stream obfuscation will be enabled. Stream obfuscation adds
random characters to an `obfuscation` field on streaming delta events to
normalize payload sizes as a mitigation to certain side-channel attacks.
These obfuscation fields are included by default, but add a small amount
of overhead to the data stream. You can set `include_obfuscation` to
false to optimize for bandwidth if you trust the network links between
your application and the OpenAI API.

temperature: Optional[float]

What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.
We generally recommend altering this or `top_p` but not both.

minimum0

maximum2

text: Optional[[BetaResponseTextConfigParam](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_text_config%20%3E%20(schema))]

Configuration options for a text response from the model. Can be plain
text or structured JSON data. Learn more:

* [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
* [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

format: Optional[BetaResponseFormatTextConfig]

An object specifying the format that the model must output.

Configuring `{ "type": "json_schema" }` enables Structured Outputs,
which ensures the model will match your supplied JSON schema. Learn more in the
[Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

The default format is `{ "type": "text" }` with no additional options.

**Not recommended for gpt-4o and newer models:**

Setting to `{ "type": "json_object" }` enables the older JSON mode, which
ensures the message the model generates is valid JSON. Using `json_schema`
is preferred for models that support it.

class Text: …

Default response format. Used to generate text responses.

type: Literal["text"]

The type of response format being defined. Always `text`.

class BetaResponseFormatTextJSONSchemaConfig: …

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

name: str

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

schema: Dict[str, object]

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

type: Literal["json\_schema"]

The type of response format being defined. Always `json_schema`.

description: Optional[str]

A description of what the response format is for, used by the model to
determine how to respond in the format.

strict: Optional[bool]

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

class JSONObject: …

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type: Literal["json\_object"]

The type of response format being defined. Always `json_object`.

verbosity: Optional[Literal["low", "medium", "high"]]

Constrains the verbosity of the model’s response. Lower values will result in
more concise responses, while higher values will result in more verbose responses.
Currently supported values are `low`, `medium`, and `high`. The default is
`medium`.

"low"

"medium"

"high"

tool\_choice: Optional[[ToolChoice](/api/reference/python/resources/beta/subresources/responses/methods/create#(resource)%20beta.responses%20%3E%20(method)%20create%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20tool_choice%20%3E%20(schema))]

How the model should select which tool (or tools) to use when generating
a response. See the `tools` parameter to see how to specify which tools
the model can call.

Literal["none", "auto", "required"]

"none"

"auto"

"required"

class BetaToolChoiceAllowed: …

Constrains the tools available to the model to a pre-defined set.

mode: Literal["auto", "required"]

Constrains the tools available to the model to a pre-defined set.

`auto` allows the model to pick from among the allowed tools and generate a
message.

`required` requires the model to call one or more of the allowed tools.

"auto"

"required"

tools: List[Dict[str, object]]

A list of tool definitions that the model should be allowed to call.

For the Responses API, the list of tool definitions might look like:

[
  { "type": "function", "name": "get_weather" },
  { "type": "mcp", "server_label": "deepwiki" },
  { "type": "image_generation" }
]

type: Literal["allowed\_tools"]

Allowed tool configuration type. Always `allowed_tools`.

class BetaToolChoiceTypes: …

Indicates that the model should use a built-in tool to generate a response.
[Learn more about built-in tools](https://platform.openai.com/docs/guides/tools).

type: Literal["file\_search", "web\_search\_preview", "computer", 5 more]

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

class BetaToolChoiceFunction: …

Use this option to force the model to call a specific function.

name: str

The name of the function to call.

type: Literal["function"]

For function calling, the type is always `function`.

class BetaToolChoiceMcp: …

Use this option to force the model to call a specific tool on a remote MCP server.

server\_label: str

The label of the MCP server to use.

type: Literal["mcp"]

For MCP tools, the type is always `mcp`.

name: Optional[str]

The name of the tool to call on the server.

class BetaToolChoiceCustom: …

Use this option to force the model to call a specific custom tool.

name: str

The name of the custom tool to call.

type: Literal["custom"]

For custom tool calling, the type is always `custom`.

class ToolChoiceBetaSpecificProgrammaticToolCallingParam: …

type: Literal["programmatic\_tool\_calling"]

The tool to call. Always `programmatic_tool_calling`.

class BetaToolChoiceApplyPatch: …

Forces the model to call the apply\_patch tool when executing a tool call.

type: Literal["apply\_patch"]

The tool to call. Always `apply_patch`.

class BetaToolChoiceShell: …

Forces the model to call the shell tool when a tool call is required.

type: Literal["shell"]

The tool to call. Always `shell`.

tools: Optional[Iterable[[BetaToolParam](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))]]

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

class BetaFunctionTool: …

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

name: str

The name of the function to call.

parameters: Optional[Dict[str, object]]

A JSON schema object describing the parameters of the function.

strict: Optional[bool]

Whether strict parameter validation is enforced for this function tool.

type: Literal["function"]

The type of the function tool. Always `function`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: Optional[bool]

Whether this function is deferred and loaded via tool search.

description: Optional[str]

A description of the function. Used by the model to determine whether or not to call the function.

output\_schema: Optional[Dict[str, object]]

A JSON schema object describing the JSON value encoded in string outputs for this function.

class BetaFileSearchTool: …

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

type: Literal["file\_search"]

The type of the file search tool. Always `file_search`.

vector\_store\_ids: List[str]

The IDs of the vector stores to search.

filters: Optional[Filters]

A filter to apply.

class FiltersComparisonFilter: …

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

str

float

bool

List[Union[str, float]]

str

float

class FiltersCompoundFilter: …

Combine multiple filters using `and` or `or`.

filters: List[FiltersCompoundFilterFilter]

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

class FiltersCompoundFilterFilterComparisonFilter: …

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

str

float

bool

List[Union[str, float]]

str

float

object

type: Literal["and", "or"]

Type of operation: `and` or `or`.

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

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

class BetaComputerTool: …

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

type: Literal["computer"]

The type of the computer tool. Always `computer`.

class BetaComputerUsePreviewTool: …

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

display\_height: int

The height of the computer display.

display\_width: int

The width of the computer display.

environment: Literal["windows", "mac", "linux", 2 more]

The type of computer environment to control.

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

The type of the computer use tool. Always `computer_use_preview`.

class BetaWebSearchTool: …

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

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

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

allowed\_tools: Optional[McpAllowedTools]

List of allowed tool names or a filter object.

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

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

A list of allowed domains when type is `allowlist`.

type: Literal["allowlist"]

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

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

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

class ProgrammaticToolCalling: …

type: Literal["programmatic\_tool\_calling"]

The type of the tool. Always `programmatic_tool_calling`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

The type of the image generation tool. Always `image_generation`.

action: Optional[Literal["generate", "edit", "auto"]]

Whether to generate a new image or edit an existing image. Default: `auto`.

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

"transparent"

"opaque"

"auto"

input\_fidelity: Optional[Literal["high", "low"]]

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

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

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

The image generation model to use. Default: `gpt-image-1`.

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

Moderation level for the generated image. Default: `auto`.

"auto"

"low"

output\_compression: Optional[int]

Compression level for the output image. Default: 100.

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

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

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool: …

A tool that allows the model to execute shell commands.

type: Literal["shell"]

The type of the shell tool. Always `shell`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

environment: Optional[Environment]

class BetaContainerAuto: …

type: Literal["container\_auto"]

Automatically creates a container for this request

file\_ids: Optional[List[str]]

An optional list of uploaded files to make available to your code.

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

The memory limit for the container.

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

A list of allowed domains when type is `allowlist`.

type: Literal["allowlist"]

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

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

class BetaSkillReference: …

skill\_id: str

The ID of the referenced skill.

maxLength64

minLength1

type: Literal["skill\_reference"]

References a skill created with the /v1/skills endpoint.

version: Optional[str]

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

class BetaInlineSkill: …

description: str

The description of the skill.

name: str

The name of the skill.

source: [BetaInlineSkillSource](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

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

class BetaLocalEnvironment: …

type: Literal["local"]

Use a local computer environment.

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

An optional list of skills.

description: str

The description of the skill.

name: str

The name of the skill.

path: str

The path to the directory containing the skill.

class BetaContainerReference: …

container\_id: str

The ID of the referenced container.

type: Literal["container\_reference"]

References a container created with the /v1/containers endpoint

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

The name of the custom tool, used to identify it in tool calls.

type: Literal["custom"]

The type of the custom tool. Always `custom`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: Optional[bool]

Whether this tool should be deferred and discovered via tool search.

description: Optional[str]

Optional description of the custom tool, used to provide more context.

format: Optional[Format]

The input format for the custom tool. Default is unconstrained text.

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

A grammar defined by the user.

definition: str

The grammar definition.

syntax: Literal["lark", "regex"]

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: Literal["grammar"]

Grammar format. Always `grammar`.

class BetaNamespaceTool: …

Groups function/custom tools under a shared namespace.

description: str

A description of the namespace shown to the model.

minLength1

name: str

The namespace name used in tool calls (for example, `crm`).

minLength1

tools: List[Tool]

The function/custom tools available inside this namespace.

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: Optional[bool]

Whether this function should be deferred and discovered via tool search.

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

parameters: Optional[object]

strict: Optional[bool]

Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

The name of the custom tool, used to identify it in tool calls.

type: Literal["custom"]

The type of the custom tool. Always `custom`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: Optional[bool]

Whether this tool should be deferred and discovered via tool search.

description: Optional[str]

Optional description of the custom tool, used to provide more context.

format: Optional[Format]

The input format for the custom tool. Default is unconstrained text.

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

A grammar defined by the user.

definition: str

The grammar definition.

syntax: Literal["lark", "regex"]

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: Literal["grammar"]

Grammar format. Always `grammar`.

type: Literal["namespace"]

The type of the tool. Always `namespace`.

class BetaToolSearchTool: …

Hosted or BYOT tool search configuration for deferred tools.

type: Literal["tool\_search"]

The type of the tool. Always `tool_search`.

description: Optional[str]

Description shown to the model for a client-executed tool search tool.

execution: Optional[Literal["server", "client"]]

Whether tool search is executed by the server or by the client.

"server"

"client"

parameters: Optional[object]

Parameter schema for a client-executed tool search tool.

class BetaWebSearchPreviewTool: …

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

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

class BetaApplyPatchTool: …

Allows the assistant to create, delete, or update files using unified diffs.

type: Literal["apply\_patch"]

The type of the tool. Always `apply_patch`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

top\_logprobs: Optional[int]

An integer between 0 and 20 specifying the maximum number of most likely
tokens to return at each token position, each with an associated log
probability. In some cases, the number of returned tokens may be fewer than
requested.

minimum0

maximum20

top\_p: Optional[float]

An alternative to sampling with temperature, called nucleus sampling,
where the model considers the results of the tokens with top\_p probability
mass. So 0.1 means only the tokens comprising the top 10% probability mass
are considered.

We generally recommend altering this or `temperature` but not both.

minimum0

maximum1

Deprecatedtruncation: Optional[Literal["auto", "disabled"]]

The truncation strategy to use for the model response.

* `auto`: If the input to this Response exceeds
  the model’s context window size, the model will truncate the
  response to fit the context window by dropping items from the beginning of the conversation.
* `disabled` (default): If the input size will exceed the context window
  size for a model, the request will fail with a 400 error.

"auto"

"disabled"

Deprecateduser: Optional[str]

This field is being replaced by `safety_identifier` and `prompt_cache_key`. Use `prompt_cache_key` instead to maintain caching optimizations.
A stable identifier for your end-users.
Used to boost cache hit rates by better bucketing similar requests and to help OpenAI detect and prevent abuse. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).

betas: Optional[List[Literal["responses\_multi\_agent=v1"]]]

class BetaResponse: …

id: str

Unique identifier for this Response.

created\_at: float

Unix timestamp (in seconds) of when this Response was created.

formatunixtime

error: Optional[BetaResponseError]

An error object returned when the model fails to generate a Response.

code: Literal["server\_error", "rate\_limit\_exceeded", "invalid\_prompt", 17 more]

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

message: str

A human-readable description of the error.

incomplete\_details: Optional[IncompleteDetails]

Details about why the response is incomplete.

reason: Optional[Literal["max\_output\_tokens", "content\_filter"]]

The reason why the response is incomplete.

"max\_output\_tokens"

"content\_filter"

instructions: Union[str, List[[BetaResponseInputItem](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_item%20%3E%20(schema))], null]

A system (or developer) message inserted into the model’s context.

When using along with `previous_response_id`, the instructions from a previous
response will not be carried over to the next response. This makes it simple
to swap out system (or developer) messages in new responses.

str

A text input to the model, equivalent to a text input with the
`developer` role.

List[[BetaResponseInputItem](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_item%20%3E%20(schema))]

A list of one or many input items to the model, containing
different content types.

class BetaEasyInputMessage: …

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: Union[str, [BetaResponseInputMessageContentList](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_message_content_list%20%3E%20(schema))]

Text, image, or audio input to the model, used to generate a response.
Can also contain previous assistant responses.

str

A text input to the model.

List[[BetaResponseInputContent](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_content%20%3E%20(schema))]

class BetaResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

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

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class BetaResponseInputFile: …

A file input to the model.

type: Literal["input\_file"]

The type of the input item. Always `input_file`.

detail: Optional[Literal["auto", "low", "high"]]

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

"auto"

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

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

role: Literal["user", "assistant", "system", "developer"]

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

"user"

"assistant"

"system"

"developer"

phase: Optional[Literal["commentary", "final\_answer"]]

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

"commentary"

"final\_answer"

type: Optional[Literal["message"]]

The type of the message input. Always `message`.

class Message: …

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role.

content: [BetaResponseInputMessageContentList](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_message_content_list%20%3E%20(schema))

A list of one or many input items to the model, containing different content
types.

class BetaResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

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

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class BetaResponseInputFile: …

A file input to the model.

type: Literal["input\_file"]

The type of the input item. Always `input_file`.

detail: Optional[Literal["auto", "low", "high"]]

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

"auto"

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

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

role: Literal["user", "system", "developer"]

The role of the message input. One of `user`, `system`, or `developer`.

"user"

"system"

"developer"

agent: Optional[MessageAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

type: Optional[Literal["message"]]

The type of the message input. Always set to `message`.

class BetaResponseOutputMessage: …

An output message from the model.

id: str

The unique ID of the output message.

content: List[Content]

The content of the output message.

class BetaResponseOutputText: …

A text output from the model.

annotations: List[Annotation]

The annotations of the text output.

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

class BetaResponseOutputRefusal: …

A refusal from the model.

refusal: str

The refusal explanation from the model.

type: Literal["refusal"]

The type of the refusal. Always `refusal`.

role: Literal["assistant"]

The role of the output message. Always `assistant`.

status: Literal["in\_progress", "completed", "incomplete"]

The status of the message input. One of `in_progress`, `completed`, or
`incomplete`. Populated when input items are returned via API.

"in\_progress"

"completed"

"incomplete"

type: Literal["message"]

The type of the output message. Always `message`.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

phase: Optional[Literal["commentary", "final\_answer"]]

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

"commentary"

"final\_answer"

class BetaResponseFileSearchToolCall: …

The results of a file search tool call. See the
[file search guide](https://platform.openai.com/docs/guides/tools-file-search) for more information.

id: str

The unique ID of the file search tool call.

queries: List[str]

The queries used to search for files.

status: Literal["in\_progress", "searching", "completed", 2 more]

The status of the file search tool call. One of `in_progress`,
`searching`, `incomplete` or `failed`,

"in\_progress"

"searching"

"completed"

"incomplete"

"failed"

type: Literal["file\_search\_call"]

The type of the file search tool call. Always `file_search_call`.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

results: Optional[List[Result]]

The results of the file search tool call.

attributes: Optional[Dict[str, Union[str, float, bool]]]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.

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

class BetaResponseComputerToolCall: …

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

"in\_progress"

"completed"

"incomplete"

type: Literal["computer\_call"]

The type of the computer call. Always `computer_call`.

action: Optional[BetaComputerAction]

A click action.

class Click: …

A click action.

button: Literal["left", "right", "wheel", 2 more]

Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

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

actions: Optional[BetaComputerActionList]

Flattened batched actions for `computer_use`. Each action includes an
`type` discriminator and action-specific fields.

class Click: …

A click action.

button: Literal["left", "right", "wheel", 2 more]

Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

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

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class ComputerCallOutput: …

The output of a computer tool call.

call\_id: str

The ID of the computer tool call that produced the output.

maxLength64

minLength1

output: [BetaResponseComputerToolCallOutputScreenshot](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_computer_tool_call_output_screenshot%20%3E%20(schema))

A computer screenshot image used with the computer use tool.

type: Literal["computer\_screenshot"]

Specifies the event type. For a computer screenshot, this property is
always set to `computer_screenshot`.

file\_id: Optional[str]

The identifier of an uploaded file that contains the screenshot.

image\_url: Optional[str]

The URL of the screenshot image.

formaturi

type: Literal["computer\_call\_output"]

The type of the computer tool call output. Always `computer_call_output`.

id: Optional[str]

The ID of the computer tool call output.

acknowledged\_safety\_checks: Optional[List[ComputerCallOutputAcknowledgedSafetyCheck]]

The safety checks reported by the API that have been acknowledged by the developer.

id: str

The ID of the pending safety check.

code: Optional[str]

The type of the pending safety check.

message: Optional[str]

Details about the pending safety check.

agent: Optional[ComputerCallOutputAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the message input. One of `in_progress`, `completed`, or `incomplete`. Populated when input items are returned via API.

"in\_progress"

"completed"

"incomplete"

class BetaResponseFunctionWebSearch: …

The results of a web search tool call. See the
[web search guide](https://platform.openai.com/docs/guides/tools-web-search) for more information.

id: str

The unique ID of the web search tool call.

action: Action

An object describing the specific action taken in this web search call.
Includes details on how the model used the web (search, open\_page, find\_in\_page).

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

"in\_progress"

"searching"

"completed"

"failed"

type: Literal["web\_search\_call"]

The type of the web search tool call. Always `web_search_call`.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class BetaResponseFunctionToolCall: …

A tool call to run a function. See the
[function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.

arguments: str

A JSON string of the arguments to pass to the function.

call\_id: str

The unique ID of the function tool call generated by the model.

name: str

The name of the function to run.

type: Literal["function\_call"]

The type of the function tool call. Always `function_call`.

id: Optional[str]

The unique ID of the function tool call.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

caller: Optional[Caller]

The execution context that produced this tool call.

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

The call ID of the program item that produced this tool call.

type: Literal["program"]

namespace: Optional[str]

The namespace of the function to run.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

class FunctionCallOutput: …

The output of a function tool call.

call\_id: str

The unique ID of the function tool call generated by the model.

maxLength64

minLength1

output: Union[str, [BetaResponseFunctionCallOutputItemList](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_call_output_item_list%20%3E%20(schema))]

Text, image, or file output of the function tool call.

str

A JSON string of the output of the function tool call.

List[[BetaResponseFunctionCallOutputItem](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_call_output_item%20%3E%20(schema))]

class BetaResponseInputTextContent: …

A text input to the model.

text: str

The text input to the model.

maxLength10485760

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class BetaResponseInputImageContent: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision)

type: Literal["input\_image"]

The type of the input item. Always `input_image`.

detail: Optional[Literal["low", "high", "auto", "original"]]

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

"low"

"high"

"auto"

"original"

file\_id: Optional[str]

The ID of the file to be sent to the model.

image\_url: Optional[str]

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

maxLength20971520

formaturi

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class BetaResponseInputFileContent: …

A file input to the model.

type: Literal["input\_file"]

The type of the input item. Always `input_file`.

detail: Optional[Literal["auto", "low", "high"]]

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

"auto"

"low"

"high"

file\_data: Optional[str]

The base64-encoded data of the file to be sent to the model.

maxLength73400320

file\_id: Optional[str]

The ID of the file to be sent to the model.

file\_url: Optional[str]

The URL of the file to be sent to the model.

formaturi

filename: Optional[str]

The name of the file to be sent to the model.

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

type: Literal["function\_call\_output"]

The type of the function tool call output. Always `function_call_output`.

id: Optional[str]

The unique ID of the function tool call output. Populated when this item is returned via API.

agent: Optional[FunctionCallOutputAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

caller: Optional[FunctionCallOutputCaller]

The execution context that produced this tool call.

class FunctionCallOutputCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class FunctionCallOutputCallerProgram: …

caller\_id: str

The call ID of the program item that produced this tool call.

maxLength64

minLength1

type: Literal["program"]

The caller type. Always `program`.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the item. One of `in_progress`, `completed`, or `incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

class AgentMessage: …

A message routed between agents.

author: str

The sending agent identity.

content: List[AgentMessageContent]

Plaintext, image, or encrypted content sent between agents.

class BetaResponseInputTextContent: …

A text input to the model.

text: str

The text input to the model.

maxLength10485760

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class BetaResponseInputImageContent: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision)

type: Literal["input\_image"]

The type of the input item. Always `input_image`.

detail: Optional[Literal["low", "high", "auto", "original"]]

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

"low"

"high"

"auto"

"original"

file\_id: Optional[str]

The ID of the file to be sent to the model.

image\_url: Optional[str]

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

maxLength20971520

formaturi

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class AgentMessageContentEncryptedContent: …

Opaque encrypted content that Responses API decrypts inside trusted model execution.

encrypted\_content: str

Opaque encrypted content.

maxLength10485760

type: Literal["encrypted\_content"]

The type of the input item. Always `encrypted_content`.

recipient: str

The destination agent identity.

type: Literal["agent\_message"]

The item type. Always `agent_message`.

id: Optional[str]

The unique ID of this agent message item.

agent: Optional[AgentMessageAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class MultiAgentCall: …

action: Literal["spawn\_agent", "interrupt\_agent", "list\_agents", 3 more]

The multi-agent action that was executed.

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

arguments: str

The action arguments as a JSON string.

call\_id: str

The unique ID linking this call to its output.

maxLength64

minLength1

type: Literal["multi\_agent\_call"]

The item type. Always `multi_agent_call`.

id: Optional[str]

The unique ID of this multi-agent call.

agent: Optional[MultiAgentCallAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class MultiAgentCallOutput: …

action: Literal["spawn\_agent", "interrupt\_agent", "list\_agents", 3 more]

The multi-agent action that produced this result.

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

call\_id: str

The unique ID of the multi-agent call.

maxLength64

minLength1

output: List[MultiAgentCallOutputOutput]

Text output returned by the multi-agent action.

text: str

The text content.

maxLength10485760

type: Literal["output\_text"]

The content type. Always `output_text`.

annotations: Optional[List[MultiAgentCallOutputOutputAnnotation]]

Citations associated with the text content.

class MultiAgentCallOutputOutputAnnotationFileCitation: …

file\_id: str

The ID of the file.

filename: str

The filename of the file cited.

index: int

The index of the file in the list of files.

minimum0

type: Literal["file\_citation"]

The citation type. Always `file_citation`.

class MultiAgentCallOutputOutputAnnotationURLCitation: …

end\_index: int

The index of the last character of the citation in the message.

minimum0

start\_index: int

The index of the first character of the citation in the message.

minimum0

title: str

The title of the cited resource.

type: Literal["url\_citation"]

The citation type. Always `url_citation`.

url: str

The URL of the cited resource.

formaturi

class MultiAgentCallOutputOutputAnnotationContainerFileCitation: …

container\_id: str

The ID of the container.

end\_index: int

The index of the last character of the citation in the message.

minimum0

file\_id: str

The ID of the container file.

filename: str

The filename of the container file cited.

start\_index: int

The index of the first character of the citation in the message.

minimum0

type: Literal["container\_file\_citation"]

The citation type. Always `container_file_citation`.

type: Literal["multi\_agent\_call\_output"]

The item type. Always `multi_agent_call_output`.

id: Optional[str]

The unique ID of this multi-agent call output.

agent: Optional[MultiAgentCallOutputAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class ToolSearchCall: …

arguments: object

The arguments supplied to the tool search call.

type: Literal["tool\_search\_call"]

The item type. Always `tool_search_call`.

id: Optional[str]

The unique ID of this tool search call.

agent: Optional[ToolSearchCallAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

call\_id: Optional[str]

The unique ID of the tool search call generated by the model.

maxLength64

minLength1

execution: Optional[Literal["server", "client"]]

Whether tool search was executed by the server or by the client.

"server"

"client"

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the tool search call.

"in\_progress"

"completed"

"incomplete"

class BetaResponseToolSearchOutputItemParam: …

tools: List[[BetaTool](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))]

The loaded tool definitions returned by the tool search output.

class BetaFunctionTool: …

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

name: str

The name of the function to call.

parameters: Optional[Dict[str, object]]

A JSON schema object describing the parameters of the function.

strict: Optional[bool]

Whether strict parameter validation is enforced for this function tool.

type: Literal["function"]

The type of the function tool. Always `function`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: Optional[bool]

Whether this function is deferred and loaded via tool search.

description: Optional[str]

A description of the function. Used by the model to determine whether or not to call the function.

output\_schema: Optional[Dict[str, object]]

A JSON schema object describing the JSON value encoded in string outputs for this function.

class BetaFileSearchTool: …

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

type: Literal["file\_search"]

The type of the file search tool. Always `file_search`.

vector\_store\_ids: List[str]

The IDs of the vector stores to search.

filters: Optional[Filters]

A filter to apply.

class FiltersComparisonFilter: …

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

str

float

bool

List[Union[str, float]]

str

float

class FiltersCompoundFilter: …

Combine multiple filters using `and` or `or`.

filters: List[FiltersCompoundFilterFilter]

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

class FiltersCompoundFilterFilterComparisonFilter: …

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

str

float

bool

List[Union[str, float]]

str

float

object

type: Literal["and", "or"]

Type of operation: `and` or `or`.

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

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

class BetaComputerTool: …

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

type: Literal["computer"]

The type of the computer tool. Always `computer`.

class BetaComputerUsePreviewTool: …

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

display\_height: int

The height of the computer display.

display\_width: int

The width of the computer display.

environment: Literal["windows", "mac", "linux", 2 more]

The type of computer environment to control.

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

The type of the computer use tool. Always `computer_use_preview`.

class BetaWebSearchTool: …

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

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

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

allowed\_tools: Optional[McpAllowedTools]

List of allowed tool names or a filter object.

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

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

A list of allowed domains when type is `allowlist`.

type: Literal["allowlist"]

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

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

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

class ProgrammaticToolCalling: …

type: Literal["programmatic\_tool\_calling"]

The type of the tool. Always `programmatic_tool_calling`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

The type of the image generation tool. Always `image_generation`.

action: Optional[Literal["generate", "edit", "auto"]]

Whether to generate a new image or edit an existing image. Default: `auto`.

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

"transparent"

"opaque"

"auto"

input\_fidelity: Optional[Literal["high", "low"]]

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

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

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

The image generation model to use. Default: `gpt-image-1`.

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

Moderation level for the generated image. Default: `auto`.

"auto"

"low"

output\_compression: Optional[int]

Compression level for the output image. Default: 100.

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

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

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool: …

A tool that allows the model to execute shell commands.

type: Literal["shell"]

The type of the shell tool. Always `shell`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

environment: Optional[Environment]

class BetaContainerAuto: …

type: Literal["container\_auto"]

Automatically creates a container for this request

file\_ids: Optional[List[str]]

An optional list of uploaded files to make available to your code.

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

The memory limit for the container.

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

A list of allowed domains when type is `allowlist`.

type: Literal["allowlist"]

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

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

class BetaSkillReference: …

skill\_id: str

The ID of the referenced skill.

maxLength64

minLength1

type: Literal["skill\_reference"]

References a skill created with the /v1/skills endpoint.

version: Optional[str]

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

class BetaInlineSkill: …

description: str

The description of the skill.

name: str

The name of the skill.

source: [BetaInlineSkillSource](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

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

class BetaLocalEnvironment: …

type: Literal["local"]

Use a local computer environment.

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

An optional list of skills.

description: str

The description of the skill.

name: str

The name of the skill.

path: str

The path to the directory containing the skill.

class BetaContainerReference: …

container\_id: str

The ID of the referenced container.

type: Literal["container\_reference"]

References a container created with the /v1/containers endpoint

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

The name of the custom tool, used to identify it in tool calls.

type: Literal["custom"]

The type of the custom tool. Always `custom`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: Optional[bool]

Whether this tool should be deferred and discovered via tool search.

description: Optional[str]

Optional description of the custom tool, used to provide more context.

format: Optional[Format]

The input format for the custom tool. Default is unconstrained text.

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

A grammar defined by the user.

definition: str

The grammar definition.

syntax: Literal["lark", "regex"]

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: Literal["grammar"]

Grammar format. Always `grammar`.

class BetaNamespaceTool: …

Groups function/custom tools under a shared namespace.

description: str

A description of the namespace shown to the model.

minLength1

name: str

The namespace name used in tool calls (for example, `crm`).

minLength1

tools: List[Tool]

The function/custom tools available inside this namespace.

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: Optional[bool]

Whether this function should be deferred and discovered via tool search.

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

parameters: Optional[object]

strict: Optional[bool]

Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

The name of the custom tool, used to identify it in tool calls.

type: Literal["custom"]

The type of the custom tool. Always `custom`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: Optional[bool]

Whether this tool should be deferred and discovered via tool search.

description: Optional[str]

Optional description of the custom tool, used to provide more context.

format: Optional[Format]

The input format for the custom tool. Default is unconstrained text.

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

A grammar defined by the user.

definition: str

The grammar definition.

syntax: Literal["lark", "regex"]

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: Literal["grammar"]

Grammar format. Always `grammar`.

type: Literal["namespace"]

The type of the tool. Always `namespace`.

class BetaToolSearchTool: …

Hosted or BYOT tool search configuration for deferred tools.

type: Literal["tool\_search"]

The type of the tool. Always `tool_search`.

description: Optional[str]

Description shown to the model for a client-executed tool search tool.

execution: Optional[Literal["server", "client"]]

Whether tool search is executed by the server or by the client.

"server"

"client"

parameters: Optional[object]

Parameter schema for a client-executed tool search tool.

class BetaWebSearchPreviewTool: …

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

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

class BetaApplyPatchTool: …

Allows the assistant to create, delete, or update files using unified diffs.

type: Literal["apply\_patch"]

The type of the tool. Always `apply_patch`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

type: Literal["tool\_search\_output"]

The item type. Always `tool_search_output`.

id: Optional[str]

The unique ID of this tool search output.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

call\_id: Optional[str]

The unique ID of the tool search call generated by the model.

maxLength64

minLength1

execution: Optional[Literal["server", "client"]]

Whether tool search was executed by the server or by the client.

"server"

"client"

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the tool search output.

"in\_progress"

"completed"

"incomplete"

class AdditionalTools: …

role: Literal["developer"]

The role that provided the additional tools. Only `developer` is supported.

tools: List[[BetaTool](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))]

A list of additional tools made available at this item.

class BetaFunctionTool: …

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

name: str

The name of the function to call.

parameters: Optional[Dict[str, object]]

A JSON schema object describing the parameters of the function.

strict: Optional[bool]

Whether strict parameter validation is enforced for this function tool.

type: Literal["function"]

The type of the function tool. Always `function`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: Optional[bool]

Whether this function is deferred and loaded via tool search.

description: Optional[str]

A description of the function. Used by the model to determine whether or not to call the function.

output\_schema: Optional[Dict[str, object]]

A JSON schema object describing the JSON value encoded in string outputs for this function.

class BetaFileSearchTool: …

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

type: Literal["file\_search"]

The type of the file search tool. Always `file_search`.

vector\_store\_ids: List[str]

The IDs of the vector stores to search.

filters: Optional[Filters]

A filter to apply.

class FiltersComparisonFilter: …

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

str

float

bool

List[Union[str, float]]

str

float

class FiltersCompoundFilter: …

Combine multiple filters using `and` or `or`.

filters: List[FiltersCompoundFilterFilter]

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

class FiltersCompoundFilterFilterComparisonFilter: …

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

str

float

bool

List[Union[str, float]]

str

float

object

type: Literal["and", "or"]

Type of operation: `and` or `or`.

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

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

class BetaComputerTool: …

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

type: Literal["computer"]

The type of the computer tool. Always `computer`.

class BetaComputerUsePreviewTool: …

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

display\_height: int

The height of the computer display.

display\_width: int

The width of the computer display.

environment: Literal["windows", "mac", "linux", 2 more]

The type of computer environment to control.

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

The type of the computer use tool. Always `computer_use_preview`.

class BetaWebSearchTool: …

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

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

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

allowed\_tools: Optional[McpAllowedTools]

List of allowed tool names or a filter object.

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

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

A list of allowed domains when type is `allowlist`.

type: Literal["allowlist"]

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

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

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

class ProgrammaticToolCalling: …

type: Literal["programmatic\_tool\_calling"]

The type of the tool. Always `programmatic_tool_calling`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

The type of the image generation tool. Always `image_generation`.

action: Optional[Literal["generate", "edit", "auto"]]

Whether to generate a new image or edit an existing image. Default: `auto`.

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

"transparent"

"opaque"

"auto"

input\_fidelity: Optional[Literal["high", "low"]]

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

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

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

The image generation model to use. Default: `gpt-image-1`.

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

Moderation level for the generated image. Default: `auto`.

"auto"

"low"

output\_compression: Optional[int]

Compression level for the output image. Default: 100.

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

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

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool: …

A tool that allows the model to execute shell commands.

type: Literal["shell"]

The type of the shell tool. Always `shell`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

environment: Optional[Environment]

class BetaContainerAuto: …

type: Literal["container\_auto"]

Automatically creates a container for this request

file\_ids: Optional[List[str]]

An optional list of uploaded files to make available to your code.

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

The memory limit for the container.

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

A list of allowed domains when type is `allowlist`.

type: Literal["allowlist"]

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

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

class BetaSkillReference: …

skill\_id: str

The ID of the referenced skill.

maxLength64

minLength1

type: Literal["skill\_reference"]

References a skill created with the /v1/skills endpoint.

version: Optional[str]

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

class BetaInlineSkill: …

description: str

The description of the skill.

name: str

The name of the skill.

source: [BetaInlineSkillSource](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

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

class BetaLocalEnvironment: …

type: Literal["local"]

Use a local computer environment.

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

An optional list of skills.

description: str

The description of the skill.

name: str

The name of the skill.

path: str

The path to the directory containing the skill.

class BetaContainerReference: …

container\_id: str

The ID of the referenced container.

type: Literal["container\_reference"]

References a container created with the /v1/containers endpoint

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

The name of the custom tool, used to identify it in tool calls.

type: Literal["custom"]

The type of the custom tool. Always `custom`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: Optional[bool]

Whether this tool should be deferred and discovered via tool search.

description: Optional[str]

Optional description of the custom tool, used to provide more context.

format: Optional[Format]

The input format for the custom tool. Default is unconstrained text.

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

A grammar defined by the user.

definition: str

The grammar definition.

syntax: Literal["lark", "regex"]

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: Literal["grammar"]

Grammar format. Always `grammar`.

class BetaNamespaceTool: …

Groups function/custom tools under a shared namespace.

description: str

A description of the namespace shown to the model.

minLength1

name: str

The namespace name used in tool calls (for example, `crm`).

minLength1

tools: List[Tool]

The function/custom tools available inside this namespace.

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: Optional[bool]

Whether this function should be deferred and discovered via tool search.

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

parameters: Optional[object]

strict: Optional[bool]

Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

The name of the custom tool, used to identify it in tool calls.

type: Literal["custom"]

The type of the custom tool. Always `custom`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: Optional[bool]

Whether this tool should be deferred and discovered via tool search.

description: Optional[str]

Optional description of the custom tool, used to provide more context.

format: Optional[Format]

The input format for the custom tool. Default is unconstrained text.

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

A grammar defined by the user.

definition: str

The grammar definition.

syntax: Literal["lark", "regex"]

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: Literal["grammar"]

Grammar format. Always `grammar`.

type: Literal["namespace"]

The type of the tool. Always `namespace`.

class BetaToolSearchTool: …

Hosted or BYOT tool search configuration for deferred tools.

type: Literal["tool\_search"]

The type of the tool. Always `tool_search`.

description: Optional[str]

Description shown to the model for a client-executed tool search tool.

execution: Optional[Literal["server", "client"]]

Whether tool search is executed by the server or by the client.

"server"

"client"

parameters: Optional[object]

Parameter schema for a client-executed tool search tool.

class BetaWebSearchPreviewTool: …

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

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

class BetaApplyPatchTool: …

Allows the assistant to create, delete, or update files using unified diffs.

type: Literal["apply\_patch"]

The type of the tool. Always `apply_patch`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

type: Literal["additional\_tools"]

The item type. Always `additional_tools`.

id: Optional[str]

The unique ID of this additional tools item.

agent: Optional[AdditionalToolsAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class BetaResponseReasoningItem: …

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

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

content: Optional[List[Content]]

Reasoning text content.

text: str

The reasoning text from the model.

type: Literal["reasoning\_text"]

The type of the reasoning text. Always `reasoning_text`.

encrypted\_content: Optional[str]

The encrypted content of the reasoning item. This is populated by default
for reasoning items returned by `POST /v1/responses` and WebSocket
`response.create` requests.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

class BetaResponseCompactionItemParam: …

A compaction item generated by the [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).

encrypted\_content: str

The encrypted content of the compaction summary.

maxLength10485760

type: Literal["compaction"]

The type of the item. Always `compaction`.

id: Optional[str]

The ID of the compaction item.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class ImageGenerationCall: …

An image generation request made by the model.

id: str

The unique ID of the image generation call.

result: Optional[str]

The generated image encoded in base64.

status: Literal["in\_progress", "completed", "generating", "failed"]

The status of the image generation call.

"in\_progress"

"completed"

"generating"

"failed"

type: Literal["image\_generation\_call"]

The type of the image generation call. Always `image_generation_call`.

agent: Optional[ImageGenerationCallAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class BetaResponseCodeInterpreterToolCall: …

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

"in\_progress"

"completed"

"incomplete"

"interpreting"

"failed"

type: Literal["code\_interpreter\_call"]

The type of the code interpreter tool call. Always `code_interpreter_call`.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

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

"in\_progress"

"completed"

"incomplete"

type: Literal["local\_shell\_call"]

The type of the local shell call. Always `local_shell_call`.

agent: Optional[LocalShellCallAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class LocalShellCallOutput: …

The output of a local shell tool call.

id: str

The unique ID of the local shell tool call generated by the model.

output: str

A JSON string of the output of the local shell tool call.

type: Literal["local\_shell\_call\_output"]

The type of the local shell tool call output. Always `local_shell_call_output`.

agent: Optional[LocalShellCallOutputAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the item. One of `in_progress`, `completed`, or `incomplete`.

"in\_progress"

"completed"

"incomplete"

class ShellCall: …

A tool representing a request to execute one or more shell commands.

action: ShellCallAction

The shell commands and limits that describe how to run the tool call.

commands: List[str]

Ordered shell commands for the execution environment to run.

max\_output\_length: Optional[int]

Maximum number of UTF-8 characters to capture from combined stdout and stderr output.

timeout\_ms: Optional[int]

Maximum wall-clock time in milliseconds to allow the shell commands to run.

call\_id: str

The unique ID of the shell tool call generated by the model.

maxLength64

minLength1

type: Literal["shell\_call"]

The type of the item. Always `shell_call`.

id: Optional[str]

The unique ID of the shell tool call. Populated when this item is returned via API.

agent: Optional[ShellCallAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

caller: Optional[ShellCallCaller]

The execution context that produced this tool call.

class ShellCallCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class ShellCallCallerProgram: …

caller\_id: str

The call ID of the program item that produced this tool call.

maxLength64

minLength1

type: Literal["program"]

The caller type. Always `program`.

environment: Optional[ShellCallEnvironment]

The environment to execute the shell commands in.

class BetaLocalEnvironment: …

type: Literal["local"]

Use a local computer environment.

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

An optional list of skills.

description: str

The description of the skill.

name: str

The name of the skill.

path: str

The path to the directory containing the skill.

class BetaContainerReference: …

container\_id: str

The ID of the referenced container.

type: Literal["container\_reference"]

References a container created with the /v1/containers endpoint

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the shell call. One of `in_progress`, `completed`, or `incomplete`.

"in\_progress"

"completed"

"incomplete"

class ShellCallOutput: …

The streamed output items emitted by a shell tool call.

call\_id: str

The unique ID of the shell tool call generated by the model.

maxLength64

minLength1

output: List[[BetaResponseFunctionShellCallOutputContent](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_shell_call_output_content%20%3E%20(schema))]

Captured chunks of stdout and stderr output, along with their associated outcomes.

outcome: Outcome

The exit or timeout outcome associated with this shell call.

class OutcomeTimeout: …

Indicates that the shell call exceeded its configured time limit.

type: Literal["timeout"]

The outcome type. Always `timeout`.

class OutcomeExit: …

Indicates that the shell commands finished and returned an exit code.

exit\_code: int

The exit code returned by the shell process.

type: Literal["exit"]

The outcome type. Always `exit`.

stderr: str

Captured stderr output for the shell call.

maxLength10485760

stdout: str

Captured stdout output for the shell call.

maxLength10485760

type: Literal["shell\_call\_output"]

The type of the item. Always `shell_call_output`.

id: Optional[str]

The unique ID of the shell tool call output. Populated when this item is returned via API.

agent: Optional[ShellCallOutputAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

caller: Optional[ShellCallOutputCaller]

The execution context that produced this tool call.

class ShellCallOutputCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class ShellCallOutputCallerProgram: …

caller\_id: str

The call ID of the program item that produced this tool call.

maxLength64

minLength1

type: Literal["program"]

The caller type. Always `program`.

max\_output\_length: Optional[int]

The maximum number of UTF-8 characters captured for this shell call’s combined output.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the shell call output.

"in\_progress"

"completed"

"incomplete"

class ApplyPatchCall: …

A tool call representing a request to create, delete, or update files using diff patches.

call\_id: str

The unique ID of the apply patch tool call generated by the model.

maxLength64

minLength1

operation: ApplyPatchCallOperation

The specific create, delete, or update instruction for the apply\_patch tool call.

class ApplyPatchCallOperationCreateFile: …

Instruction for creating a new file via the apply\_patch tool.

diff: str

Unified diff content to apply when creating the file.

maxLength10485760

path: str

Path of the file to create relative to the workspace root.

minLength1

type: Literal["create\_file"]

The operation type. Always `create_file`.

class ApplyPatchCallOperationDeleteFile: …

Instruction for deleting an existing file via the apply\_patch tool.

path: str

Path of the file to delete relative to the workspace root.

minLength1

type: Literal["delete\_file"]

The operation type. Always `delete_file`.

class ApplyPatchCallOperationUpdateFile: …

Instruction for updating an existing file via the apply\_patch tool.

diff: str

Unified diff content to apply to the existing file.

maxLength10485760

path: str

Path of the file to update relative to the workspace root.

minLength1

type: Literal["update\_file"]

The operation type. Always `update_file`.

status: Literal["in\_progress", "completed"]

The status of the apply patch tool call. One of `in_progress` or `completed`.

"in\_progress"

"completed"

type: Literal["apply\_patch\_call"]

The type of the item. Always `apply_patch_call`.

id: Optional[str]

The unique ID of the apply patch tool call. Populated when this item is returned via API.

agent: Optional[ApplyPatchCallAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

caller: Optional[ApplyPatchCallCaller]

The execution context that produced this tool call.

class ApplyPatchCallCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class ApplyPatchCallCallerProgram: …

caller\_id: str

The call ID of the program item that produced this tool call.

maxLength64

minLength1

type: Literal["program"]

The caller type. Always `program`.

class ApplyPatchCallOutput: …

The streamed output emitted by an apply patch tool call.

call\_id: str

The unique ID of the apply patch tool call generated by the model.

maxLength64

minLength1

status: Literal["completed", "failed"]

The status of the apply patch tool call output. One of `completed` or `failed`.

"completed"

"failed"

type: Literal["apply\_patch\_call\_output"]

The type of the item. Always `apply_patch_call_output`.

id: Optional[str]

The unique ID of the apply patch tool call output. Populated when this item is returned via API.

agent: Optional[ApplyPatchCallOutputAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

caller: Optional[ApplyPatchCallOutputCaller]

The execution context that produced this tool call.

class ApplyPatchCallOutputCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class ApplyPatchCallOutputCallerProgram: …

caller\_id: str

The call ID of the program item that produced this tool call.

maxLength64

minLength1

type: Literal["program"]

The caller type. Always `program`.

output: Optional[str]

Optional human-readable log text from the apply patch tool (e.g., patch results or errors).

maxLength10485760

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

agent: Optional[McpListToolsAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

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

agent: Optional[McpApprovalRequestAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class McpApprovalResponse: …

A response to an MCP approval request.

approval\_request\_id: str

The ID of the approval request being answered.

approve: bool

Whether the request was approved.

type: Literal["mcp\_approval\_response"]

The type of the item. Always `mcp_approval_response`.

id: Optional[str]

The unique ID of the approval response

agent: Optional[McpApprovalResponseAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

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

agent: Optional[McpCallAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

approval\_request\_id: Optional[str]

Unique identifier for the MCP tool call approval request.
Include this value in a subsequent `mcp_approval_response` input to approve or reject the corresponding tool call.

error: Optional[str]

The error from the tool call, if any.

output: Optional[str]

The output from the tool call.

status: Optional[Literal["in\_progress", "completed", "incomplete", 2 more]]

The status of the tool call. One of `in_progress`, `completed`, `incomplete`, `calling`, or `failed`.

"in\_progress"

"completed"

"incomplete"

"calling"

"failed"

class BetaResponseCustomToolCallOutput: …

The output of a custom tool call from your code, being sent back to the model.

call\_id: str

The call ID, used to map this custom tool call output to a custom tool call.

output: Union[str, List[OutputOutputContentList]]

The output from the custom tool call generated by your code.
Can be a string or an list of output content.

str

A string of the output of the custom tool call.

List[OutputOutputContentList]

Text, image, or file output of the custom tool call.

class BetaResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

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

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class BetaResponseInputFile: …

A file input to the model.

type: Literal["input\_file"]

The type of the input item. Always `input_file`.

detail: Optional[Literal["auto", "low", "high"]]

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

"auto"

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

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

type: Literal["custom\_tool\_call\_output"]

The type of the custom tool call output. Always `custom_tool_call_output`.

id: Optional[str]

The unique ID of the custom tool call output in the OpenAI platform.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

caller: Optional[Caller]

The execution context that produced this tool call.

class CallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class CallerProgram: …

caller\_id: str

The call ID of the program item that produced this tool call.

maxLength64

minLength1

type: Literal["program"]

The caller type. Always `program`.

class BetaResponseCustomToolCall: …

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

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

caller: Optional[Caller]

The execution context that produced this tool call.

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

The call ID of the program item that produced this tool call.

type: Literal["program"]

namespace: Optional[str]

The namespace of the custom tool being called.

class CompactionTrigger: …

Compacts the current context. Must be the final input item.

type: Literal["compaction\_trigger"]

The type of the item. Always `compaction_trigger`.

agent: Optional[CompactionTriggerAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class ItemReference: …

An internal identifier for an item to reference.

id: str

The ID of the item to reference.

agent: Optional[ItemReferenceAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

type: Optional[Literal["item\_reference"]]

The type of item to reference. Always `item_reference`.

class Program: …

id: str

The unique ID of this program item.

call\_id: str

The stable call ID of the program item.

maxLength64

minLength1

code: str

The JavaScript source executed by programmatic tool calling.

maxLength10485760

fingerprint: str

Opaque program replay fingerprint that must be round-tripped.

maxLength10485760

type: Literal["program"]

The item type. Always `program`.

agent: Optional[ProgramAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class ProgramOutput: …

id: str

The unique ID of this program output item.

call\_id: str

The call ID of the program item.

maxLength64

minLength1

result: str

The result produced by the program item.

maxLength10485760

status: Literal["completed", "incomplete"]

The terminal status of the program output.

"completed"

"incomplete"

type: Literal["program\_output"]

The item type. Always `program_output`.

agent: Optional[ProgramOutputAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

metadata: Optional[Dict[str, str]]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: Union[Literal["gpt-5.6-sol", "gpt-5.6-terra", "gpt-5.6-luna", 92 more], str]

Model ID used to generate the response, like `gpt-4o` or `o3`. OpenAI
offers a wide range of models with different capabilities, performance
characteristics, and price points. Refer to the [model guide](https://platform.openai.com/docs/models)
to browse and compare available models.

Literal["gpt-5.6-sol", "gpt-5.6-terra", "gpt-5.6-luna", 92 more]

Model ID used to generate the response, like `gpt-4o` or `o3`. OpenAI
offers a wide range of models with different capabilities, performance
characteristics, and price points. Refer to the [model guide](https://platform.openai.com/docs/models)
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

str

object: Literal["response"]

The object type of this resource - always set to `response`.

output: List[[BetaResponseOutputItem](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_item%20%3E%20(schema))]

An array of content items generated by the model.

* The length and order of items in the `output` array is dependent
  on the model’s response.
* Rather than accessing the first item in the `output` array and
  assuming it’s an `assistant` message with the content generated by
  the model, you might consider using the `output_text` property where
  supported in SDKs.

class BetaResponseOutputMessage: …

An output message from the model.

id: str

The unique ID of the output message.

content: List[Content]

The content of the output message.

class BetaResponseOutputText: …

A text output from the model.

annotations: List[Annotation]

The annotations of the text output.

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

class BetaResponseOutputRefusal: …

A refusal from the model.

refusal: str

The refusal explanation from the model.

type: Literal["refusal"]

The type of the refusal. Always `refusal`.

role: Literal["assistant"]

The role of the output message. Always `assistant`.

status: Literal["in\_progress", "completed", "incomplete"]

The status of the message input. One of `in_progress`, `completed`, or
`incomplete`. Populated when input items are returned via API.

"in\_progress"

"completed"

"incomplete"

type: Literal["message"]

The type of the output message. Always `message`.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

phase: Optional[Literal["commentary", "final\_answer"]]

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

"commentary"

"final\_answer"

class BetaResponseFileSearchToolCall: …

The results of a file search tool call. See the
[file search guide](https://platform.openai.com/docs/guides/tools-file-search) for more information.

id: str

The unique ID of the file search tool call.

queries: List[str]

The queries used to search for files.

status: Literal["in\_progress", "searching", "completed", 2 more]

The status of the file search tool call. One of `in_progress`,
`searching`, `incomplete` or `failed`,

"in\_progress"

"searching"

"completed"

"incomplete"

"failed"

type: Literal["file\_search\_call"]

The type of the file search tool call. Always `file_search_call`.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

results: Optional[List[Result]]

The results of the file search tool call.

attributes: Optional[Dict[str, Union[str, float, bool]]]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.

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

class BetaResponseFunctionToolCall: …

A tool call to run a function. See the
[function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.

arguments: str

A JSON string of the arguments to pass to the function.

call\_id: str

The unique ID of the function tool call generated by the model.

name: str

The name of the function to run.

type: Literal["function\_call"]

The type of the function tool call. Always `function_call`.

id: Optional[str]

The unique ID of the function tool call.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

caller: Optional[Caller]

The execution context that produced this tool call.

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

The call ID of the program item that produced this tool call.

type: Literal["program"]

namespace: Optional[str]

The namespace of the function to run.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

class BetaResponseFunctionToolCallOutputItem: …

id: str

The unique ID of the function call tool output.

call\_id: str

The unique ID of the function tool call generated by the model.

output: Union[str, List[OutputOutputContentList]]

The output from the function call generated by your code.
Can be a string or an list of output content.

str

A string of the output of the function call.

List[OutputOutputContentList]

Text, image, or file output of the function call.

class BetaResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

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

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class BetaResponseInputFile: …

A file input to the model.

type: Literal["input\_file"]

The type of the input item. Always `input_file`.

detail: Optional[Literal["auto", "low", "high"]]

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

"auto"

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

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

status: Literal["in\_progress", "completed", "incomplete"]

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

type: Literal["function\_call\_output"]

The type of the function tool call output. Always `function_call_output`.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

caller: Optional[Caller]

The execution context that produced this tool call.

class CallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class CallerProgram: …

caller\_id: str

The call ID of the program item that produced this tool call.

maxLength64

minLength1

type: Literal["program"]

The caller type. Always `program`.

created\_by: Optional[str]

The identifier of the actor that created the item.

class AgentMessage: …

id: str

The unique ID of the agent message.

author: str

The sending agent identity.

content: List[AgentMessageContent]

Encrypted content sent between agents.

class BetaResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class BetaResponseOutputText: …

A text output from the model.

annotations: List[Annotation]

The annotations of the text output.

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

class AgentMessageContentText: …

A text content.

text: str

type: Literal["text"]

class AgentMessageContentSummaryText: …

A summary text from the model.

text: str

A summary of the reasoning output from the model so far.

type: Literal["summary\_text"]

The type of the object. Always `summary_text`.

class AgentMessageContentReasoningText: …

Reasoning text from the model.

text: str

The reasoning text from the model.

type: Literal["reasoning\_text"]

The type of the reasoning text. Always `reasoning_text`.

class BetaResponseOutputRefusal: …

A refusal from the model.

refusal: str

The refusal explanation from the model.

type: Literal["refusal"]

The type of the refusal. Always `refusal`.

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

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

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class AgentMessageContentComputerScreenshot: …

A screenshot of a computer.

detail: Literal["low", "high", "auto", "original"]

The detail level of the screenshot image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

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

prompt\_cache\_breakpoint: Optional[AgentMessageContentComputerScreenshotPromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class BetaResponseInputFile: …

A file input to the model.

type: Literal["input\_file"]

The type of the input item. Always `input_file`.

detail: Optional[Literal["auto", "low", "high"]]

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

"auto"

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

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class AgentMessageContentEncryptedContent: …

Opaque encrypted content that Responses API decrypts inside trusted model execution.

encrypted\_content: str

Opaque encrypted content.

type: Literal["encrypted\_content"]

The type of the input item. Always `encrypted_content`.

recipient: str

The destination agent identity.

type: Literal["agent\_message"]

The type of the item. Always `agent_message`.

agent: Optional[AgentMessageAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class MultiAgentCall: …

id: str

The unique ID of the multi-agent call item.

action: Literal["spawn\_agent", "interrupt\_agent", "list\_agents", 3 more]

The multi-agent action to execute.

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

arguments: str

The JSON string of arguments generated for the action.

call\_id: str

The unique ID linking this call to its output.

type: Literal["multi\_agent\_call"]

The type of the multi-agent call. Always `multi_agent_call`.

agent: Optional[MultiAgentCallAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class MultiAgentCallOutput: …

id: str

The unique ID of the multi-agent call output item.

action: Literal["spawn\_agent", "interrupt\_agent", "list\_agents", 3 more]

The multi-agent action that produced this result.

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

call\_id: str

The unique ID of the multi-agent call.

output: List[[BetaResponseOutputText](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_text%20%3E%20(schema))]

Text output returned by the multi-agent action.

annotations: List[Annotation]

The annotations of the text output.

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

type: Literal["multi\_agent\_call\_output"]

The type of the multi-agent result. Always `multi_agent_call_output`.

agent: Optional[MultiAgentCallOutputAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class BetaResponseFunctionWebSearch: …

The results of a web search tool call. See the
[web search guide](https://platform.openai.com/docs/guides/tools-web-search) for more information.

id: str

The unique ID of the web search tool call.

action: Action

An object describing the specific action taken in this web search call.
Includes details on how the model used the web (search, open\_page, find\_in\_page).

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

"in\_progress"

"searching"

"completed"

"failed"

type: Literal["web\_search\_call"]

The type of the web search tool call. Always `web_search_call`.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class BetaResponseComputerToolCall: …

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

"in\_progress"

"completed"

"incomplete"

type: Literal["computer\_call"]

The type of the computer call. Always `computer_call`.

action: Optional[BetaComputerAction]

A click action.

class Click: …

A click action.

button: Literal["left", "right", "wheel", 2 more]

Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

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

actions: Optional[BetaComputerActionList]

Flattened batched actions for `computer_use`. Each action includes an
`type` discriminator and action-specific fields.

class Click: …

A click action.

button: Literal["left", "right", "wheel", 2 more]

Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

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

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class BetaResponseComputerToolCallOutputItem: …

id: str

The unique ID of the computer call tool output.

call\_id: str

The ID of the computer tool call that produced the output.

output: [BetaResponseComputerToolCallOutputScreenshot](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_computer_tool_call_output_screenshot%20%3E%20(schema))

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

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

created\_by: Optional[str]

The identifier of the actor that created the item.

class BetaResponseReasoningItem: …

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

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

content: Optional[List[Content]]

Reasoning text content.

text: str

The reasoning text from the model.

type: Literal["reasoning\_text"]

The type of the reasoning text. Always `reasoning_text`.

encrypted\_content: Optional[str]

The encrypted content of the reasoning item. This is populated by default
for reasoning items returned by `POST /v1/responses` and WebSocket
`response.create` requests.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

class Program: …

id: str

The unique ID of the program item.

call\_id: str

The stable call ID of the program item.

code: str

The JavaScript source executed by programmatic tool calling.

fingerprint: str

Opaque program replay fingerprint that must be round-tripped.

type: Literal["program"]

The type of the item. Always `program`.

agent: Optional[ProgramAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class ProgramOutput: …

id: str

The unique ID of the program output item.

call\_id: str

The call ID of the program item.

result: str

The result produced by the program item.

status: Literal["completed", "incomplete"]

The terminal status of the program output item.

"completed"

"incomplete"

type: Literal["program\_output"]

The type of the item. Always `program_output`.

agent: Optional[ProgramOutputAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class BetaResponseToolSearchCall: …

id: str

The unique ID of the tool search call item.

arguments: object

Arguments used for the tool search call.

call\_id: Optional[str]

The unique ID of the tool search call generated by the model.

execution: Literal["server", "client"]

Whether tool search was executed by the server or by the client.

"server"

"client"

status: Literal["in\_progress", "completed", "incomplete"]

The status of the tool search call item that was recorded.

"in\_progress"

"completed"

"incomplete"

type: Literal["tool\_search\_call"]

The type of the item. Always `tool_search_call`.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

created\_by: Optional[str]

The identifier of the actor that created the item.

class BetaResponseToolSearchOutputItem: …

id: str

The unique ID of the tool search output item.

call\_id: Optional[str]

The unique ID of the tool search call generated by the model.

execution: Literal["server", "client"]

Whether tool search was executed by the server or by the client.

"server"

"client"

status: Literal["in\_progress", "completed", "incomplete"]

The status of the tool search output item that was recorded.

"in\_progress"

"completed"

"incomplete"

tools: List[[BetaTool](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))]

The loaded tool definitions returned by tool search.

class BetaFunctionTool: …

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

name: str

The name of the function to call.

parameters: Optional[Dict[str, object]]

A JSON schema object describing the parameters of the function.

strict: Optional[bool]

Whether strict parameter validation is enforced for this function tool.

type: Literal["function"]

The type of the function tool. Always `function`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: Optional[bool]

Whether this function is deferred and loaded via tool search.

description: Optional[str]

A description of the function. Used by the model to determine whether or not to call the function.

output\_schema: Optional[Dict[str, object]]

A JSON schema object describing the JSON value encoded in string outputs for this function.

class BetaFileSearchTool: …

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

type: Literal["file\_search"]

The type of the file search tool. Always `file_search`.

vector\_store\_ids: List[str]

The IDs of the vector stores to search.

filters: Optional[Filters]

A filter to apply.

class FiltersComparisonFilter: …

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

str

float

bool

List[Union[str, float]]

str

float

class FiltersCompoundFilter: …

Combine multiple filters using `and` or `or`.

filters: List[FiltersCompoundFilterFilter]

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

class FiltersCompoundFilterFilterComparisonFilter: …

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

str

float

bool

List[Union[str, float]]

str

float

object

type: Literal["and", "or"]

Type of operation: `and` or `or`.

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

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

class BetaComputerTool: …

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

type: Literal["computer"]

The type of the computer tool. Always `computer`.

class BetaComputerUsePreviewTool: …

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

display\_height: int

The height of the computer display.

display\_width: int

The width of the computer display.

environment: Literal["windows", "mac", "linux", 2 more]

The type of computer environment to control.

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

The type of the computer use tool. Always `computer_use_preview`.

class BetaWebSearchTool: …

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

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

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

allowed\_tools: Optional[McpAllowedTools]

List of allowed tool names or a filter object.

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

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

A list of allowed domains when type is `allowlist`.

type: Literal["allowlist"]

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

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

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

class ProgrammaticToolCalling: …

type: Literal["programmatic\_tool\_calling"]

The type of the tool. Always `programmatic_tool_calling`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

The type of the image generation tool. Always `image_generation`.

action: Optional[Literal["generate", "edit", "auto"]]

Whether to generate a new image or edit an existing image. Default: `auto`.

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

"transparent"

"opaque"

"auto"

input\_fidelity: Optional[Literal["high", "low"]]

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

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

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

The image generation model to use. Default: `gpt-image-1`.

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

Moderation level for the generated image. Default: `auto`.

"auto"

"low"

output\_compression: Optional[int]

Compression level for the output image. Default: 100.

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

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

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool: …

A tool that allows the model to execute shell commands.

type: Literal["shell"]

The type of the shell tool. Always `shell`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

environment: Optional[Environment]

class BetaContainerAuto: …

type: Literal["container\_auto"]

Automatically creates a container for this request

file\_ids: Optional[List[str]]

An optional list of uploaded files to make available to your code.

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

The memory limit for the container.

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

A list of allowed domains when type is `allowlist`.

type: Literal["allowlist"]

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

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

class BetaSkillReference: …

skill\_id: str

The ID of the referenced skill.

maxLength64

minLength1

type: Literal["skill\_reference"]

References a skill created with the /v1/skills endpoint.

version: Optional[str]

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

class BetaInlineSkill: …

description: str

The description of the skill.

name: str

The name of the skill.

source: [BetaInlineSkillSource](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

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

class BetaLocalEnvironment: …

type: Literal["local"]

Use a local computer environment.

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

An optional list of skills.

description: str

The description of the skill.

name: str

The name of the skill.

path: str

The path to the directory containing the skill.

class BetaContainerReference: …

container\_id: str

The ID of the referenced container.

type: Literal["container\_reference"]

References a container created with the /v1/containers endpoint

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

The name of the custom tool, used to identify it in tool calls.

type: Literal["custom"]

The type of the custom tool. Always `custom`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: Optional[bool]

Whether this tool should be deferred and discovered via tool search.

description: Optional[str]

Optional description of the custom tool, used to provide more context.

format: Optional[Format]

The input format for the custom tool. Default is unconstrained text.

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

A grammar defined by the user.

definition: str

The grammar definition.

syntax: Literal["lark", "regex"]

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: Literal["grammar"]

Grammar format. Always `grammar`.

class BetaNamespaceTool: …

Groups function/custom tools under a shared namespace.

description: str

A description of the namespace shown to the model.

minLength1

name: str

The namespace name used in tool calls (for example, `crm`).

minLength1

tools: List[Tool]

The function/custom tools available inside this namespace.

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: Optional[bool]

Whether this function should be deferred and discovered via tool search.

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

parameters: Optional[object]

strict: Optional[bool]

Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

The name of the custom tool, used to identify it in tool calls.

type: Literal["custom"]

The type of the custom tool. Always `custom`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: Optional[bool]

Whether this tool should be deferred and discovered via tool search.

description: Optional[str]

Optional description of the custom tool, used to provide more context.

format: Optional[Format]

The input format for the custom tool. Default is unconstrained text.

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

A grammar defined by the user.

definition: str

The grammar definition.

syntax: Literal["lark", "regex"]

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: Literal["grammar"]

Grammar format. Always `grammar`.

type: Literal["namespace"]

The type of the tool. Always `namespace`.

class BetaToolSearchTool: …

Hosted or BYOT tool search configuration for deferred tools.

type: Literal["tool\_search"]

The type of the tool. Always `tool_search`.

description: Optional[str]

Description shown to the model for a client-executed tool search tool.

execution: Optional[Literal["server", "client"]]

Whether tool search is executed by the server or by the client.

"server"

"client"

parameters: Optional[object]

Parameter schema for a client-executed tool search tool.

class BetaWebSearchPreviewTool: …

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

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

class BetaApplyPatchTool: …

Allows the assistant to create, delete, or update files using unified diffs.

type: Literal["apply\_patch"]

The type of the tool. Always `apply_patch`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

type: Literal["tool\_search\_output"]

The type of the item. Always `tool_search_output`.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

created\_by: Optional[str]

The identifier of the actor that created the item.

class AdditionalTools: …

id: str

The unique ID of the additional tools item.

role: Literal["unknown", "user", "assistant", 5 more]

The role that provided the additional tools.

"unknown"

"user"

"assistant"

"system"

"critic"

"discriminator"

"developer"

"tool"

tools: List[[BetaTool](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))]

The additional tool definitions made available at this item.

class BetaFunctionTool: …

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

name: str

The name of the function to call.

parameters: Optional[Dict[str, object]]

A JSON schema object describing the parameters of the function.

strict: Optional[bool]

Whether strict parameter validation is enforced for this function tool.

type: Literal["function"]

The type of the function tool. Always `function`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: Optional[bool]

Whether this function is deferred and loaded via tool search.

description: Optional[str]

A description of the function. Used by the model to determine whether or not to call the function.

output\_schema: Optional[Dict[str, object]]

A JSON schema object describing the JSON value encoded in string outputs for this function.

class BetaFileSearchTool: …

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

type: Literal["file\_search"]

The type of the file search tool. Always `file_search`.

vector\_store\_ids: List[str]

The IDs of the vector stores to search.

filters: Optional[Filters]

A filter to apply.

class FiltersComparisonFilter: …

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

str

float

bool

List[Union[str, float]]

str

float

class FiltersCompoundFilter: …

Combine multiple filters using `and` or `or`.

filters: List[FiltersCompoundFilterFilter]

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

class FiltersCompoundFilterFilterComparisonFilter: …

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

str

float

bool

List[Union[str, float]]

str

float

object

type: Literal["and", "or"]

Type of operation: `and` or `or`.

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

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

class BetaComputerTool: …

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

type: Literal["computer"]

The type of the computer tool. Always `computer`.

class BetaComputerUsePreviewTool: …

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

display\_height: int

The height of the computer display.

display\_width: int

The width of the computer display.

environment: Literal["windows", "mac", "linux", 2 more]

The type of computer environment to control.

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

The type of the computer use tool. Always `computer_use_preview`.

class BetaWebSearchTool: …

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

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

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

allowed\_tools: Optional[McpAllowedTools]

List of allowed tool names or a filter object.

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

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

A list of allowed domains when type is `allowlist`.

type: Literal["allowlist"]

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

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

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

class ProgrammaticToolCalling: …

type: Literal["programmatic\_tool\_calling"]

The type of the tool. Always `programmatic_tool_calling`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

The type of the image generation tool. Always `image_generation`.

action: Optional[Literal["generate", "edit", "auto"]]

Whether to generate a new image or edit an existing image. Default: `auto`.

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

"transparent"

"opaque"

"auto"

input\_fidelity: Optional[Literal["high", "low"]]

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

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

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

The image generation model to use. Default: `gpt-image-1`.

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

Moderation level for the generated image. Default: `auto`.

"auto"

"low"

output\_compression: Optional[int]

Compression level for the output image. Default: 100.

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

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

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool: …

A tool that allows the model to execute shell commands.

type: Literal["shell"]

The type of the shell tool. Always `shell`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

environment: Optional[Environment]

class BetaContainerAuto: …

type: Literal["container\_auto"]

Automatically creates a container for this request

file\_ids: Optional[List[str]]

An optional list of uploaded files to make available to your code.

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

The memory limit for the container.

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

A list of allowed domains when type is `allowlist`.

type: Literal["allowlist"]

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

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

class BetaSkillReference: …

skill\_id: str

The ID of the referenced skill.

maxLength64

minLength1

type: Literal["skill\_reference"]

References a skill created with the /v1/skills endpoint.

version: Optional[str]

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

class BetaInlineSkill: …

description: str

The description of the skill.

name: str

The name of the skill.

source: [BetaInlineSkillSource](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

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

class BetaLocalEnvironment: …

type: Literal["local"]

Use a local computer environment.

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

An optional list of skills.

description: str

The description of the skill.

name: str

The name of the skill.

path: str

The path to the directory containing the skill.

class BetaContainerReference: …

container\_id: str

The ID of the referenced container.

type: Literal["container\_reference"]

References a container created with the /v1/containers endpoint

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

The name of the custom tool, used to identify it in tool calls.

type: Literal["custom"]

The type of the custom tool. Always `custom`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: Optional[bool]

Whether this tool should be deferred and discovered via tool search.

description: Optional[str]

Optional description of the custom tool, used to provide more context.

format: Optional[Format]

The input format for the custom tool. Default is unconstrained text.

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

A grammar defined by the user.

definition: str

The grammar definition.

syntax: Literal["lark", "regex"]

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: Literal["grammar"]

Grammar format. Always `grammar`.

class BetaNamespaceTool: …

Groups function/custom tools under a shared namespace.

description: str

A description of the namespace shown to the model.

minLength1

name: str

The namespace name used in tool calls (for example, `crm`).

minLength1

tools: List[Tool]

The function/custom tools available inside this namespace.

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: Optional[bool]

Whether this function should be deferred and discovered via tool search.

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

parameters: Optional[object]

strict: Optional[bool]

Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

The name of the custom tool, used to identify it in tool calls.

type: Literal["custom"]

The type of the custom tool. Always `custom`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: Optional[bool]

Whether this tool should be deferred and discovered via tool search.

description: Optional[str]

Optional description of the custom tool, used to provide more context.

format: Optional[Format]

The input format for the custom tool. Default is unconstrained text.

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

A grammar defined by the user.

definition: str

The grammar definition.

syntax: Literal["lark", "regex"]

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: Literal["grammar"]

Grammar format. Always `grammar`.

type: Literal["namespace"]

The type of the tool. Always `namespace`.

class BetaToolSearchTool: …

Hosted or BYOT tool search configuration for deferred tools.

type: Literal["tool\_search"]

The type of the tool. Always `tool_search`.

description: Optional[str]

Description shown to the model for a client-executed tool search tool.

execution: Optional[Literal["server", "client"]]

Whether tool search is executed by the server or by the client.

"server"

"client"

parameters: Optional[object]

Parameter schema for a client-executed tool search tool.

class BetaWebSearchPreviewTool: …

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

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

class BetaApplyPatchTool: …

Allows the assistant to create, delete, or update files using unified diffs.

type: Literal["apply\_patch"]

The type of the tool. Always `apply_patch`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

type: Literal["additional\_tools"]

The type of the item. Always `additional_tools`.

agent: Optional[AdditionalToolsAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class BetaResponseCompactionItem: …

A compaction item generated by the [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).

id: str

The unique ID of the compaction item.

encrypted\_content: str

The encrypted content that was produced by compaction.

type: Literal["compaction"]

The type of the item. Always `compaction`.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

created\_by: Optional[str]

The identifier of the actor that created the item.

class ImageGenerationCall: …

An image generation request made by the model.

id: str

The unique ID of the image generation call.

result: Optional[str]

The generated image encoded in base64.

status: Literal["in\_progress", "completed", "generating", "failed"]

The status of the image generation call.

"in\_progress"

"completed"

"generating"

"failed"

type: Literal["image\_generation\_call"]

The type of the image generation call. Always `image_generation_call`.

agent: Optional[ImageGenerationCallAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class BetaResponseCodeInterpreterToolCall: …

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

"in\_progress"

"completed"

"incomplete"

"interpreting"

"failed"

type: Literal["code\_interpreter\_call"]

The type of the code interpreter tool call. Always `code_interpreter_call`.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

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

"in\_progress"

"completed"

"incomplete"

type: Literal["local\_shell\_call"]

The type of the local shell call. Always `local_shell_call`.

agent: Optional[LocalShellCallAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class LocalShellCallOutput: …

The output of a local shell tool call.

id: str

The unique ID of the local shell tool call generated by the model.

output: str

A JSON string of the output of the local shell tool call.

type: Literal["local\_shell\_call\_output"]

The type of the local shell tool call output. Always `local_shell_call_output`.

agent: Optional[LocalShellCallOutputAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the item. One of `in_progress`, `completed`, or `incomplete`.

"in\_progress"

"completed"

"incomplete"

class BetaResponseFunctionShellToolCall: …

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

class BetaResponseLocalEnvironment: …

Represents the use of a local environment to perform shell actions.

type: Literal["local"]

The environment type. Always `local`.

class BetaResponseContainerReference: …

Represents a container created with /v1/containers.

container\_id: str

type: Literal["container\_reference"]

The environment type. Always `container_reference`.

status: Literal["in\_progress", "completed", "incomplete"]

The status of the shell call. One of `in_progress`, `completed`, or `incomplete`.

"in\_progress"

"completed"

"incomplete"

type: Literal["shell\_call"]

The type of the item. Always `shell_call`.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

caller: Optional[Caller]

The execution context that produced this tool call.

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

The call ID of the program item that produced this tool call.

type: Literal["program"]

created\_by: Optional[str]

The ID of the entity that created this tool call.

class BetaResponseFunctionShellToolCallOutput: …

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

"in\_progress"

"completed"

"incomplete"

type: Literal["shell\_call\_output"]

The type of the shell call output. Always `shell_call_output`.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

caller: Optional[Caller]

The execution context that produced this tool call.

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

The call ID of the program item that produced this tool call.

type: Literal["program"]

created\_by: Optional[str]

The identifier of the actor that created the item.

class BetaResponseApplyPatchToolCall: …

A tool call that applies file diffs by creating, deleting, or updating files.

id: str

The unique ID of the apply patch tool call. Populated when this item is returned via API.

call\_id: str

The unique ID of the apply patch tool call generated by the model.

operation: Operation

One of the create\_file, delete\_file, or update\_file operations applied via apply\_patch.

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

"in\_progress"

"completed"

type: Literal["apply\_patch\_call"]

The type of the item. Always `apply_patch_call`.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

caller: Optional[Caller]

The execution context that produced this tool call.

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

The call ID of the program item that produced this tool call.

type: Literal["program"]

created\_by: Optional[str]

The ID of the entity that created this tool call.

class BetaResponseApplyPatchToolCallOutput: …

The output emitted by an apply patch tool call.

id: str

The unique ID of the apply patch tool call output. Populated when this item is returned via API.

call\_id: str

The unique ID of the apply patch tool call generated by the model.

status: Literal["completed", "failed"]

The status of the apply patch tool call output. One of `completed` or `failed`.

"completed"

"failed"

type: Literal["apply\_patch\_call\_output"]

The type of the item. Always `apply_patch_call_output`.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

caller: Optional[Caller]

The execution context that produced this tool call.

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

The call ID of the program item that produced this tool call.

type: Literal["program"]

created\_by: Optional[str]

The ID of the entity that created this tool call output.

output: Optional[str]

Optional textual output returned by the apply patch tool.

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

agent: Optional[McpCallAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

approval\_request\_id: Optional[str]

Unique identifier for the MCP tool call approval request.
Include this value in a subsequent `mcp_approval_response` input to approve or reject the corresponding tool call.

error: Optional[str]

The error from the tool call, if any.

output: Optional[str]

The output from the tool call.

status: Optional[Literal["in\_progress", "completed", "incomplete", 2 more]]

The status of the tool call. One of `in_progress`, `completed`, `incomplete`, `calling`, or `failed`.

"in\_progress"

"completed"

"incomplete"

"calling"

"failed"

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

agent: Optional[McpListToolsAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

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

agent: Optional[McpApprovalRequestAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

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

agent: Optional[McpApprovalResponseAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

reason: Optional[str]

Optional reason for the decision.

class BetaResponseCustomToolCall: …

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

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

caller: Optional[Caller]

The execution context that produced this tool call.

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

The call ID of the program item that produced this tool call.

type: Literal["program"]

namespace: Optional[str]

The namespace of the custom tool being called.

class BetaResponseCustomToolCallOutputItem: …

The output of a custom tool call from your code, being sent back to the model.

id: str

The unique ID of the custom tool call output item.

status: Literal["in\_progress", "completed", "incomplete"]

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

created\_by: Optional[str]

The identifier of the actor that created the item.

parallel\_tool\_calls: bool

Whether to allow the model to run tool calls in parallel.

temperature: Optional[float]

What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.
We generally recommend altering this or `top_p` but not both.

minimum0

maximum2

tool\_choice: ToolChoice

How the model should select which tool (or tools) to use when generating
a response. See the `tools` parameter to see how to specify which tools
the model can call.

Literal["none", "auto", "required"]

"none"

"auto"

"required"

class BetaToolChoiceAllowed: …

Constrains the tools available to the model to a pre-defined set.

mode: Literal["auto", "required"]

Constrains the tools available to the model to a pre-defined set.

`auto` allows the model to pick from among the allowed tools and generate a
message.

`required` requires the model to call one or more of the allowed tools.

"auto"

"required"

tools: List[Dict[str, object]]

A list of tool definitions that the model should be allowed to call.

For the Responses API, the list of tool definitions might look like:

[
  { "type": "function", "name": "get_weather" },
  { "type": "mcp", "server_label": "deepwiki" },
  { "type": "image_generation" }
]

type: Literal["allowed\_tools"]

Allowed tool configuration type. Always `allowed_tools`.

class BetaToolChoiceTypes: …

Indicates that the model should use a built-in tool to generate a response.
[Learn more about built-in tools](https://platform.openai.com/docs/guides/tools).

type: Literal["file\_search", "web\_search\_preview", "computer", 5 more]

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

class BetaToolChoiceFunction: …

Use this option to force the model to call a specific function.

name: str

The name of the function to call.

type: Literal["function"]

For function calling, the type is always `function`.

class BetaToolChoiceMcp: …

Use this option to force the model to call a specific tool on a remote MCP server.

server\_label: str

The label of the MCP server to use.

type: Literal["mcp"]

For MCP tools, the type is always `mcp`.

name: Optional[str]

The name of the tool to call on the server.

class BetaToolChoiceCustom: …

Use this option to force the model to call a specific custom tool.

name: str

The name of the custom tool to call.

type: Literal["custom"]

For custom tool calling, the type is always `custom`.

class ToolChoiceBetaSpecificProgrammaticToolCallingParam: …

type: Literal["programmatic\_tool\_calling"]

The tool to call. Always `programmatic_tool_calling`.

class BetaToolChoiceApplyPatch: …

Forces the model to call the apply\_patch tool when executing a tool call.

type: Literal["apply\_patch"]

The tool to call. Always `apply_patch`.

class BetaToolChoiceShell: …

Forces the model to call the shell tool when a tool call is required.

type: Literal["shell"]

The tool to call. Always `shell`.

tools: List[[BetaTool](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))]

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

class BetaFunctionTool: …

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

name: str

The name of the function to call.

parameters: Optional[Dict[str, object]]

A JSON schema object describing the parameters of the function.

strict: Optional[bool]

Whether strict parameter validation is enforced for this function tool.

type: Literal["function"]

The type of the function tool. Always `function`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: Optional[bool]

Whether this function is deferred and loaded via tool search.

description: Optional[str]

A description of the function. Used by the model to determine whether or not to call the function.

output\_schema: Optional[Dict[str, object]]

A JSON schema object describing the JSON value encoded in string outputs for this function.

class BetaFileSearchTool: …

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

type: Literal["file\_search"]

The type of the file search tool. Always `file_search`.

vector\_store\_ids: List[str]

The IDs of the vector stores to search.

filters: Optional[Filters]

A filter to apply.

class FiltersComparisonFilter: …

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

str

float

bool

List[Union[str, float]]

str

float

class FiltersCompoundFilter: …

Combine multiple filters using `and` or `or`.

filters: List[FiltersCompoundFilterFilter]

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

class FiltersCompoundFilterFilterComparisonFilter: …

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

str

float

bool

List[Union[str, float]]

str

float

object

type: Literal["and", "or"]

Type of operation: `and` or `or`.

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

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

class BetaComputerTool: …

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

type: Literal["computer"]

The type of the computer tool. Always `computer`.

class BetaComputerUsePreviewTool: …

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

display\_height: int

The height of the computer display.

display\_width: int

The width of the computer display.

environment: Literal["windows", "mac", "linux", 2 more]

The type of computer environment to control.

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

The type of the computer use tool. Always `computer_use_preview`.

class BetaWebSearchTool: …

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

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

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

allowed\_tools: Optional[McpAllowedTools]

List of allowed tool names or a filter object.

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

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

A list of allowed domains when type is `allowlist`.

type: Literal["allowlist"]

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

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

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

class ProgrammaticToolCalling: …

type: Literal["programmatic\_tool\_calling"]

The type of the tool. Always `programmatic_tool_calling`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

The type of the image generation tool. Always `image_generation`.

action: Optional[Literal["generate", "edit", "auto"]]

Whether to generate a new image or edit an existing image. Default: `auto`.

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

"transparent"

"opaque"

"auto"

input\_fidelity: Optional[Literal["high", "low"]]

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

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

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

The image generation model to use. Default: `gpt-image-1`.

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

Moderation level for the generated image. Default: `auto`.

"auto"

"low"

output\_compression: Optional[int]

Compression level for the output image. Default: 100.

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

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

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool: …

A tool that allows the model to execute shell commands.

type: Literal["shell"]

The type of the shell tool. Always `shell`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

environment: Optional[Environment]

class BetaContainerAuto: …

type: Literal["container\_auto"]

Automatically creates a container for this request

file\_ids: Optional[List[str]]

An optional list of uploaded files to make available to your code.

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

The memory limit for the container.

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

A list of allowed domains when type is `allowlist`.

type: Literal["allowlist"]

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

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

class BetaSkillReference: …

skill\_id: str

The ID of the referenced skill.

maxLength64

minLength1

type: Literal["skill\_reference"]

References a skill created with the /v1/skills endpoint.

version: Optional[str]

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

class BetaInlineSkill: …

description: str

The description of the skill.

name: str

The name of the skill.

source: [BetaInlineSkillSource](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

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

class BetaLocalEnvironment: …

type: Literal["local"]

Use a local computer environment.

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

An optional list of skills.

description: str

The description of the skill.

name: str

The name of the skill.

path: str

The path to the directory containing the skill.

class BetaContainerReference: …

container\_id: str

The ID of the referenced container.

type: Literal["container\_reference"]

References a container created with the /v1/containers endpoint

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

The name of the custom tool, used to identify it in tool calls.

type: Literal["custom"]

The type of the custom tool. Always `custom`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: Optional[bool]

Whether this tool should be deferred and discovered via tool search.

description: Optional[str]

Optional description of the custom tool, used to provide more context.

format: Optional[Format]

The input format for the custom tool. Default is unconstrained text.

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

A grammar defined by the user.

definition: str

The grammar definition.

syntax: Literal["lark", "regex"]

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: Literal["grammar"]

Grammar format. Always `grammar`.

class BetaNamespaceTool: …

Groups function/custom tools under a shared namespace.

description: str

A description of the namespace shown to the model.

minLength1

name: str

The namespace name used in tool calls (for example, `crm`).

minLength1

tools: List[Tool]

The function/custom tools available inside this namespace.

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: Optional[bool]

Whether this function should be deferred and discovered via tool search.

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

parameters: Optional[object]

strict: Optional[bool]

Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

The name of the custom tool, used to identify it in tool calls.

type: Literal["custom"]

The type of the custom tool. Always `custom`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: Optional[bool]

Whether this tool should be deferred and discovered via tool search.

description: Optional[str]

Optional description of the custom tool, used to provide more context.

format: Optional[Format]

The input format for the custom tool. Default is unconstrained text.

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

A grammar defined by the user.

definition: str

The grammar definition.

syntax: Literal["lark", "regex"]

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: Literal["grammar"]

Grammar format. Always `grammar`.

type: Literal["namespace"]

The type of the tool. Always `namespace`.

class BetaToolSearchTool: …

Hosted or BYOT tool search configuration for deferred tools.

type: Literal["tool\_search"]

The type of the tool. Always `tool_search`.

description: Optional[str]

Description shown to the model for a client-executed tool search tool.

execution: Optional[Literal["server", "client"]]

Whether tool search is executed by the server or by the client.

"server"

"client"

parameters: Optional[object]

Parameter schema for a client-executed tool search tool.

class BetaWebSearchPreviewTool: …

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

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

class BetaApplyPatchTool: …

Allows the assistant to create, delete, or update files using unified diffs.

type: Literal["apply\_patch"]

The type of the tool. Always `apply_patch`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

top\_p: Optional[float]

An alternative to sampling with temperature, called nucleus sampling,
where the model considers the results of the tokens with top\_p probability
mass. So 0.1 means only the tokens comprising the top 10% probability mass
are considered.

We generally recommend altering this or `temperature` but not both.

minimum0

maximum1

background: Optional[bool]

Whether to run the model response in the background.
[Learn more](https://platform.openai.com/docs/guides/background).

completed\_at: Optional[float]

Unix timestamp (in seconds) of when this Response was completed.
Only present when the status is `completed`.

formatunixtime

conversation: Optional[Conversation]

The conversation that this response belonged to. Input items and output items from this response were automatically added to this conversation.

id: str

The unique ID of the conversation that this response was associated with.

max\_output\_tokens: Optional[int]

An upper bound for the number of tokens that can be generated for a response, including visible output tokens and [reasoning tokens](https://platform.openai.com/docs/guides/reasoning).

max\_tool\_calls: Optional[int]

The maximum number of total calls to built-in tools that can be processed in a response. This maximum number applies across all built-in tool calls, not per individual tool. Any further attempts to call a tool by the model will be ignored.

moderation: Optional[Moderation]

Moderation results for the response input and output, if moderated completions were requested.

input: ModerationInput

Moderation for the response input.

class ModerationInputModerationResult: …

A moderation result produced for the response input or output.

categories: Dict[str, bool]

A dictionary of moderation categories to booleans, True if the input is flagged under this category.

category\_applied\_input\_types: Dict[str, List[Literal["text", "image"]]]

Which modalities of input are reflected by the score for each category.

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

class ModerationInputError: …

An error produced while attempting moderation for the response input or output.

code: str

The error code.

message: str

The error message.

type: Literal["error"]

The object type, which was always `error` for moderation failures.

output: ModerationOutput

Moderation for the response output.

class ModerationOutputModerationResult: …

A moderation result produced for the response input or output.

categories: Dict[str, bool]

A dictionary of moderation categories to booleans, True if the input is flagged under this category.

category\_applied\_input\_types: Dict[str, List[Literal["text", "image"]]]

Which modalities of input are reflected by the score for each category.

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

class ModerationOutputError: …

An error produced while attempting moderation for the response input or output.

code: str

The error code.

message: str

The error message.

type: Literal["error"]

The object type, which was always `error` for moderation failures.

previous\_response\_id: Optional[str]

The unique ID of the previous response to the model. Use this to
create multi-turn conversations. Learn more about
[conversation state](https://platform.openai.com/docs/guides/conversation-state). Cannot be used in conjunction with `conversation`.

prompt: Optional[BetaResponsePrompt]

Reference to a prompt template and its variables.
[Learn more](https://platform.openai.com/docs/guides/text?api-mode=responses#reusable-prompts).

id: str

The unique identifier of the prompt template to use.

variables: Optional[Dict[str, Variables]]

Optional map of values to substitute in for variables in your
prompt. The substitution values can either be strings, or other
Response input types like images or files.

str

class BetaResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

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

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class BetaResponseInputFile: …

A file input to the model.

type: Literal["input\_file"]

The type of the input item. Always `input_file`.

detail: Optional[Literal["auto", "low", "high"]]

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

"auto"

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

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

version: Optional[str]

Optional version of the prompt template.

prompt\_cache\_key: Optional[str]

Used by OpenAI to cache responses for similar requests to optimize your cache hit rates. Replaces the `user` field. [Learn more](https://platform.openai.com/docs/guides/prompt-caching).

prompt\_cache\_options: Optional[PromptCacheOptions]

The prompt-caching options that were applied to the response. Supported for `gpt-5.6` and later models.

mode: Literal["implicit", "explicit"]

Whether implicit prompt-cache breakpoints were enabled.

"implicit"

"explicit"

ttl: Literal["30m"]

The minimum lifetime applied to each cache breakpoint.

Deprecatedprompt\_cache\_retention: Optional[Literal["in\_memory", "24h"]]

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

reasoning: Optional[Reasoning]

**gpt-5 and o-series models only**

Configuration options for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).

context: Optional[Literal["auto", "current\_turn", "all\_turns"]]

Controls which reasoning items are rendered back to the model on later turns.
If omitted or set to `auto`, the model determines the context mode. The
`gpt-5.6` model family defaults to `all_turns`; earlier models default to
`current_turn`.

When returned on a response, this is the effective reasoning context mode
used for the response.

"auto"

"current\_turn"

"all\_turns"

effort: Optional[Literal["none", "minimal", "low", 4 more]]

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

Deprecatedgenerate\_summary: Optional[Literal["auto", "concise", "detailed"]]

**Deprecated:** use `summary` instead.

A summary of the reasoning performed by the model. This can be
useful for debugging and understanding the model’s reasoning process.
One of `auto`, `concise`, or `detailed`.

"auto"

"concise"

"detailed"

mode: Optional[Union[str, Literal["standard", "pro"], null]]

Controls the reasoning execution mode for the request.

When returned on a response, this is the effective execution mode.

str

Literal["standard", "pro"]

Controls the reasoning execution mode for the request.

When returned on a response, this is the effective execution mode.

"standard"

"pro"

summary: Optional[Literal["auto", "concise", "detailed"]]

A summary of the reasoning performed by the model. This can be
useful for debugging and understanding the model’s reasoning process.
One of `auto`, `concise`, or `detailed`.

`concise` is supported for `computer-use-preview` models and all reasoning models after `gpt-5`.

"auto"

"concise"

"detailed"

safety\_identifier: Optional[str]

A stable identifier used to help detect users of your application that may be violating OpenAI’s usage policies.
The IDs should be a string that uniquely identifies each user, with a maximum length of 64 characters. We recommend hashing their username or email address, in order to avoid sending us any identifying information. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).

maxLength64

service\_tier: Optional[Literal["auto", "default", "flex", 2 more]]

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

status: Optional[BetaResponseStatus]

The status of the response generation. One of `completed`, `failed`,
`in_progress`, `cancelled`, `queued`, or `incomplete`.

"completed"

"failed"

"in\_progress"

"cancelled"

"queued"

"incomplete"

text: Optional[BetaResponseTextConfig]

Configuration options for a text response from the model. Can be plain
text or structured JSON data. Learn more:

* [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
* [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

format: Optional[BetaResponseFormatTextConfig]

An object specifying the format that the model must output.

Configuring `{ "type": "json_schema" }` enables Structured Outputs,
which ensures the model will match your supplied JSON schema. Learn more in the
[Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

The default format is `{ "type": "text" }` with no additional options.

**Not recommended for gpt-4o and newer models:**

Setting to `{ "type": "json_object" }` enables the older JSON mode, which
ensures the message the model generates is valid JSON. Using `json_schema`
is preferred for models that support it.

class Text: …

Default response format. Used to generate text responses.

type: Literal["text"]

The type of response format being defined. Always `text`.

class BetaResponseFormatTextJSONSchemaConfig: …

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

name: str

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

schema: Dict[str, object]

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

type: Literal["json\_schema"]

The type of response format being defined. Always `json_schema`.

description: Optional[str]

A description of what the response format is for, used by the model to
determine how to respond in the format.

strict: Optional[bool]

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

class JSONObject: …

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type: Literal["json\_object"]

The type of response format being defined. Always `json_object`.

verbosity: Optional[Literal["low", "medium", "high"]]

Constrains the verbosity of the model’s response. Lower values will result in
more concise responses, while higher values will result in more verbose responses.
Currently supported values are `low`, `medium`, and `high`. The default is
`medium`.

"low"

"medium"

"high"

top\_logprobs: Optional[int]

An integer between 0 and 20 specifying the maximum number of most likely
tokens to return at each token position, each with an associated log
probability. In some cases, the number of returned tokens may be fewer than
requested.

minimum0

maximum20

truncation: Optional[Literal["auto", "disabled"]]

The truncation strategy to use for the model response.

* `auto`: If the input to this Response exceeds
  the model’s context window size, the model will truncate the
  response to fit the context window by dropping items from the beginning of the conversation.
* `disabled` (default): If the input size will exceed the context window
  size for a model, the request will fail with a 400 error.

"auto"

"disabled"

usage: Optional[BetaResponseUsage]

Represents token usage details including input tokens, output tokens,
a breakdown of output tokens, and the total tokens used.

input\_tokens: int

The number of input tokens.

input\_tokens\_details: InputTokensDetails

A detailed breakdown of the input tokens.

cache\_write\_tokens: int

The number of input tokens that were written to the cache.

cached\_tokens: int

The number of tokens that were retrieved from the cache.
[More on prompt caching](https://platform.openai.com/docs/guides/prompt-caching).

output\_tokens: int

The number of output tokens.

output\_tokens\_details: OutputTokensDetails

A detailed breakdown of the output tokens.

reasoning\_tokens: int

The number of reasoning tokens.

total\_tokens: int

The total number of tokens used.

Deprecateduser: Optional[str]

This field is being replaced by `safety_identifier` and `prompt_cache_key`. Use `prompt_cache_key` instead to maintain caching optimizations.
A stable identifier for your end-users.
Used to boost cache hit rates by better bucketing similar requests and to help OpenAI detect and prevent abuse. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).

[BetaResponseStreamEvent](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_stream_event%20%3E%20(schema))

Emitted when there is a partial audio response.

class BetaResponseAudioDeltaEvent: …

Emitted when there is a partial audio response.

delta: str

A chunk of Base64 encoded response audio bytes.

sequence\_number: int

A sequence number for this chunk of the stream response.

type: Literal["response.audio.delta"]

The type of the event. Always `response.audio.delta`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

The canonical name of the agent that produced this item.

class BetaResponseAudioDoneEvent: …

Emitted when the audio response is complete.

sequence\_number: int

The sequence number of the delta.

type: Literal["response.audio.done"]

The type of the event. Always `response.audio.done`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

The canonical name of the agent that produced this item.

class BetaResponseAudioTranscriptDeltaEvent: …

Emitted when there is a partial transcript of audio.

delta: str

The partial transcript of the audio response.

sequence\_number: int

The sequence number of this event.

type: Literal["response.audio.transcript.delta"]

The type of the event. Always `response.audio.transcript.delta`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

The canonical name of the agent that produced this item.

class BetaResponseAudioTranscriptDoneEvent: …

Emitted when the full audio transcript is completed.

sequence\_number: int

The sequence number of this event.

type: Literal["response.audio.transcript.done"]

The type of the event. Always `response.audio.transcript.done`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

The canonical name of the agent that produced this item.

class BetaResponseCodeInterpreterCallCodeDeltaEvent: …

Emitted when a partial code snippet is streamed by the code interpreter.

delta: str

The partial code snippet being streamed by the code interpreter.

item\_id: str

The unique identifier of the code interpreter tool call item.

output\_index: int

The index of the output item in the response for which the code is being streamed.

sequence\_number: int

The sequence number of this event, used to order streaming events.

type: Literal["response.code\_interpreter\_call\_code.delta"]

The type of the event. Always `response.code_interpreter_call_code.delta`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

The canonical name of the agent that produced this item.

class BetaResponseCodeInterpreterCallCodeDoneEvent: …

Emitted when the code snippet is finalized by the code interpreter.

code: str

The final code snippet output by the code interpreter.

item\_id: str

The unique identifier of the code interpreter tool call item.

output\_index: int

The index of the output item in the response for which the code is finalized.

sequence\_number: int

The sequence number of this event, used to order streaming events.

type: Literal["response.code\_interpreter\_call\_code.done"]

The type of the event. Always `response.code_interpreter_call_code.done`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

The canonical name of the agent that produced this item.

class BetaResponseCodeInterpreterCallCompletedEvent: …

Emitted when the code interpreter call is completed.

item\_id: str

The unique identifier of the code interpreter tool call item.

output\_index: int

The index of the output item in the response for which the code interpreter call is completed.

sequence\_number: int

The sequence number of this event, used to order streaming events.

type: Literal["response.code\_interpreter\_call.completed"]

The type of the event. Always `response.code_interpreter_call.completed`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

The canonical name of the agent that produced this item.

class BetaResponseCodeInterpreterCallInProgressEvent: …

Emitted when a code interpreter call is in progress.

item\_id: str

The unique identifier of the code interpreter tool call item.

output\_index: int

The index of the output item in the response for which the code interpreter call is in progress.

sequence\_number: int

The sequence number of this event, used to order streaming events.

type: Literal["response.code\_interpreter\_call.in\_progress"]

The type of the event. Always `response.code_interpreter_call.in_progress`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

The canonical name of the agent that produced this item.

class BetaResponseCodeInterpreterCallInterpretingEvent: …

Emitted when the code interpreter is actively interpreting the code snippet.

item\_id: str

The unique identifier of the code interpreter tool call item.

output\_index: int

The index of the output item in the response for which the code interpreter is interpreting code.

sequence\_number: int

The sequence number of this event, used to order streaming events.

type: Literal["response.code\_interpreter\_call.interpreting"]

The type of the event. Always `response.code_interpreter_call.interpreting`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

The canonical name of the agent that produced this item.

class BetaResponseCompletedEvent: …

Emitted when the model response is complete.

response: [BetaResponse](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema))

Properties of the completed response.

id: str

Unique identifier for this Response.

created\_at: float

Unix timestamp (in seconds) of when this Response was created.

formatunixtime

error: Optional[BetaResponseError]

An error object returned when the model fails to generate a Response.

code: Literal["server\_error", "rate\_limit\_exceeded", "invalid\_prompt", 17 more]

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

message: str

A human-readable description of the error.

incomplete\_details: Optional[IncompleteDetails]

Details about why the response is incomplete.

reason: Optional[Literal["max\_output\_tokens", "content\_filter"]]

The reason why the response is incomplete.

"max\_output\_tokens"

"content\_filter"

instructions: Union[str, List[[BetaResponseInputItem](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_item%20%3E%20(schema))], null]

A system (or developer) message inserted into the model’s context.

When using along with `previous_response_id`, the instructions from a previous
response will not be carried over to the next response. This makes it simple
to swap out system (or developer) messages in new responses.

str

A text input to the model, equivalent to a text input with the
`developer` role.

List[[BetaResponseInputItem](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_item%20%3E%20(schema))]

A list of one or many input items to the model, containing
different content types.

class BetaEasyInputMessage: …

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: Union[str, [BetaResponseInputMessageContentList](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_message_content_list%20%3E%20(schema))]

Text, image, or audio input to the model, used to generate a response.
Can also contain previous assistant responses.

str

A text input to the model.

List[[BetaResponseInputContent](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_content%20%3E%20(schema))]

class BetaResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

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

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class BetaResponseInputFile: …

A file input to the model.

type: Literal["input\_file"]

The type of the input item. Always `input_file`.

detail: Optional[Literal["auto", "low", "high"]]

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

"auto"

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

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

role: Literal["user", "assistant", "system", "developer"]

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

"user"

"assistant"

"system"

"developer"

phase: Optional[Literal["commentary", "final\_answer"]]

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

"commentary"

"final\_answer"

type: Optional[Literal["message"]]

The type of the message input. Always `message`.

class Message: …

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role.

content: [BetaResponseInputMessageContentList](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_message_content_list%20%3E%20(schema))

A list of one or many input items to the model, containing different content
types.

class BetaResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

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

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class BetaResponseInputFile: …

A file input to the model.

type: Literal["input\_file"]

The type of the input item. Always `input_file`.

detail: Optional[Literal["auto", "low", "high"]]

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

"auto"

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

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

role: Literal["user", "system", "developer"]

The role of the message input. One of `user`, `system`, or `developer`.

"user"

"system"

"developer"

agent: Optional[MessageAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

type: Optional[Literal["message"]]

The type of the message input. Always set to `message`.

class BetaResponseOutputMessage: …

An output message from the model.

id: str

The unique ID of the output message.

content: List[Content]

The content of the output message.

class BetaResponseOutputText: …

A text output from the model.

annotations: List[Annotation]

The annotations of the text output.

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

class BetaResponseOutputRefusal: …

A refusal from the model.

refusal: str

The refusal explanation from the model.

type: Literal["refusal"]

The type of the refusal. Always `refusal`.

role: Literal["assistant"]

The role of the output message. Always `assistant`.

status: Literal["in\_progress", "completed", "incomplete"]

The status of the message input. One of `in_progress`, `completed`, or
`incomplete`. Populated when input items are returned via API.

"in\_progress"

"completed"

"incomplete"

type: Literal["message"]

The type of the output message. Always `message`.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

phase: Optional[Literal["commentary", "final\_answer"]]

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

"commentary"

"final\_answer"

class BetaResponseFileSearchToolCall: …

The results of a file search tool call. See the
[file search guide](https://platform.openai.com/docs/guides/tools-file-search) for more information.

id: str

The unique ID of the file search tool call.

queries: List[str]

The queries used to search for files.

status: Literal["in\_progress", "searching", "completed", 2 more]

The status of the file search tool call. One of `in_progress`,
`searching`, `incomplete` or `failed`,

"in\_progress"

"searching"

"completed"

"incomplete"

"failed"

type: Literal["file\_search\_call"]

The type of the file search tool call. Always `file_search_call`.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

results: Optional[List[Result]]

The results of the file search tool call.

attributes: Optional[Dict[str, Union[str, float, bool]]]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.

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

class BetaResponseComputerToolCall: …

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

"in\_progress"

"completed"

"incomplete"

type: Literal["computer\_call"]

The type of the computer call. Always `computer_call`.

action: Optional[BetaComputerAction]

A click action.

class Click: …

A click action.

button: Literal["left", "right", "wheel", 2 more]

Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

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

actions: Optional[BetaComputerActionList]

Flattened batched actions for `computer_use`. Each action includes an
`type` discriminator and action-specific fields.

class Click: …

A click action.

button: Literal["left", "right", "wheel", 2 more]

Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

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

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class ComputerCallOutput: …

The output of a computer tool call.

call\_id: str

The ID of the computer tool call that produced the output.

maxLength64

minLength1

output: [BetaResponseComputerToolCallOutputScreenshot](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_computer_tool_call_output_screenshot%20%3E%20(schema))

A computer screenshot image used with the computer use tool.

type: Literal["computer\_screenshot"]

Specifies the event type. For a computer screenshot, this property is
always set to `computer_screenshot`.

file\_id: Optional[str]

The identifier of an uploaded file that contains the screenshot.

image\_url: Optional[str]

The URL of the screenshot image.

formaturi

type: Literal["computer\_call\_output"]

The type of the computer tool call output. Always `computer_call_output`.

id: Optional[str]

The ID of the computer tool call output.

acknowledged\_safety\_checks: Optional[List[ComputerCallOutputAcknowledgedSafetyCheck]]

The safety checks reported by the API that have been acknowledged by the developer.

id: str

The ID of the pending safety check.

code: Optional[str]

The type of the pending safety check.

message: Optional[str]

Details about the pending safety check.

agent: Optional[ComputerCallOutputAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the message input. One of `in_progress`, `completed`, or `incomplete`. Populated when input items are returned via API.

"in\_progress"

"completed"

"incomplete"

class BetaResponseFunctionWebSearch: …

The results of a web search tool call. See the
[web search guide](https://platform.openai.com/docs/guides/tools-web-search) for more information.

id: str

The unique ID of the web search tool call.

action: Action

An object describing the specific action taken in this web search call.
Includes details on how the model used the web (search, open\_page, find\_in\_page).

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

"in\_progress"

"searching"

"completed"

"failed"

type: Literal["web\_search\_call"]

The type of the web search tool call. Always `web_search_call`.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class BetaResponseFunctionToolCall: …

A tool call to run a function. See the
[function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.

arguments: str

A JSON string of the arguments to pass to the function.

call\_id: str

The unique ID of the function tool call generated by the model.

name: str

The name of the function to run.

type: Literal["function\_call"]

The type of the function tool call. Always `function_call`.

id: Optional[str]

The unique ID of the function tool call.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

caller: Optional[Caller]

The execution context that produced this tool call.

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

The call ID of the program item that produced this tool call.

type: Literal["program"]

namespace: Optional[str]

The namespace of the function to run.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

class FunctionCallOutput: …

The output of a function tool call.

call\_id: str

The unique ID of the function tool call generated by the model.

maxLength64

minLength1

output: Union[str, [BetaResponseFunctionCallOutputItemList](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_call_output_item_list%20%3E%20(schema))]

Text, image, or file output of the function tool call.

str

A JSON string of the output of the function tool call.

List[[BetaResponseFunctionCallOutputItem](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_call_output_item%20%3E%20(schema))]

class BetaResponseInputTextContent: …

A text input to the model.

text: str

The text input to the model.

maxLength10485760

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class BetaResponseInputImageContent: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision)

type: Literal["input\_image"]

The type of the input item. Always `input_image`.

detail: Optional[Literal["low", "high", "auto", "original"]]

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

"low"

"high"

"auto"

"original"

file\_id: Optional[str]

The ID of the file to be sent to the model.

image\_url: Optional[str]

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

maxLength20971520

formaturi

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class BetaResponseInputFileContent: …

A file input to the model.

type: Literal["input\_file"]

The type of the input item. Always `input_file`.

detail: Optional[Literal["auto", "low", "high"]]

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

"auto"

"low"

"high"

file\_data: Optional[str]

The base64-encoded data of the file to be sent to the model.

maxLength73400320

file\_id: Optional[str]

The ID of the file to be sent to the model.

file\_url: Optional[str]

The URL of the file to be sent to the model.

formaturi

filename: Optional[str]

The name of the file to be sent to the model.

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

type: Literal["function\_call\_output"]

The type of the function tool call output. Always `function_call_output`.

id: Optional[str]

The unique ID of the function tool call output. Populated when this item is returned via API.

agent: Optional[FunctionCallOutputAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

caller: Optional[FunctionCallOutputCaller]

The execution context that produced this tool call.

class FunctionCallOutputCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class FunctionCallOutputCallerProgram: …

caller\_id: str

The call ID of the program item that produced this tool call.

maxLength64

minLength1

type: Literal["program"]

The caller type. Always `program`.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the item. One of `in_progress`, `completed`, or `incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

class AgentMessage: …

A message routed between agents.

author: str

The sending agent identity.

content: List[AgentMessageContent]

Plaintext, image, or encrypted content sent between agents.

class BetaResponseInputTextContent: …

A text input to the model.

text: str

The text input to the model.

maxLength10485760

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class BetaResponseInputImageContent: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision)

type: Literal["input\_image"]

The type of the input item. Always `input_image`.

detail: Optional[Literal["low", "high", "auto", "original"]]

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

"low"

"high"

"auto"

"original"

file\_id: Optional[str]

The ID of the file to be sent to the model.

image\_url: Optional[str]

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

maxLength20971520

formaturi

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class AgentMessageContentEncryptedContent: …

Opaque encrypted content that Responses API decrypts inside trusted model execution.

encrypted\_content: str

Opaque encrypted content.

maxLength10485760

type: Literal["encrypted\_content"]

The type of the input item. Always `encrypted_content`.

recipient: str

The destination agent identity.

type: Literal["agent\_message"]

The item type. Always `agent_message`.

id: Optional[str]

The unique ID of this agent message item.

agent: Optional[AgentMessageAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class MultiAgentCall: …

action: Literal["spawn\_agent", "interrupt\_agent", "list\_agents", 3 more]

The multi-agent action that was executed.

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

arguments: str

The action arguments as a JSON string.

call\_id: str

The unique ID linking this call to its output.

maxLength64

minLength1

type: Literal["multi\_agent\_call"]

The item type. Always `multi_agent_call`.

id: Optional[str]

The unique ID of this multi-agent call.

agent: Optional[MultiAgentCallAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class MultiAgentCallOutput: …

action: Literal["spawn\_agent", "interrupt\_agent", "list\_agents", 3 more]

The multi-agent action that produced this result.

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

call\_id: str

The unique ID of the multi-agent call.

maxLength64

minLength1

output: List[MultiAgentCallOutputOutput]

Text output returned by the multi-agent action.

text: str

The text content.

maxLength10485760

type: Literal["output\_text"]

The content type. Always `output_text`.

annotations: Optional[List[MultiAgentCallOutputOutputAnnotation]]

Citations associated with the text content.

class MultiAgentCallOutputOutputAnnotationFileCitation: …

file\_id: str

The ID of the file.

filename: str

The filename of the file cited.

index: int

The index of the file in the list of files.

minimum0

type: Literal["file\_citation"]

The citation type. Always `file_citation`.

class MultiAgentCallOutputOutputAnnotationURLCitation: …

end\_index: int

The index of the last character of the citation in the message.

minimum0

start\_index: int

The index of the first character of the citation in the message.

minimum0

title: str

The title of the cited resource.

type: Literal["url\_citation"]

The citation type. Always `url_citation`.

url: str

The URL of the cited resource.

formaturi

class MultiAgentCallOutputOutputAnnotationContainerFileCitation: …

container\_id: str

The ID of the container.

end\_index: int

The index of the last character of the citation in the message.

minimum0

file\_id: str

The ID of the container file.

filename: str

The filename of the container file cited.

start\_index: int

The index of the first character of the citation in the message.

minimum0

type: Literal["container\_file\_citation"]

The citation type. Always `container_file_citation`.

type: Literal["multi\_agent\_call\_output"]

The item type. Always `multi_agent_call_output`.

id: Optional[str]

The unique ID of this multi-agent call output.

agent: Optional[MultiAgentCallOutputAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class ToolSearchCall: …

arguments: object

The arguments supplied to the tool search call.

type: Literal["tool\_search\_call"]

The item type. Always `tool_search_call`.

id: Optional[str]

The unique ID of this tool search call.

agent: Optional[ToolSearchCallAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

call\_id: Optional[str]

The unique ID of the tool search call generated by the model.

maxLength64

minLength1

execution: Optional[Literal["server", "client"]]

Whether tool search was executed by the server or by the client.

"server"

"client"

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the tool search call.

"in\_progress"

"completed"

"incomplete"

class BetaResponseToolSearchOutputItemParam: …

tools: List[[BetaTool](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))]

The loaded tool definitions returned by the tool search output.

class BetaFunctionTool: …

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

name: str

The name of the function to call.

parameters: Optional[Dict[str, object]]

A JSON schema object describing the parameters of the function.

strict: Optional[bool]

Whether strict parameter validation is enforced for this function tool.

type: Literal["function"]

The type of the function tool. Always `function`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: Optional[bool]

Whether this function is deferred and loaded via tool search.

description: Optional[str]

A description of the function. Used by the model to determine whether or not to call the function.

output\_schema: Optional[Dict[str, object]]

A JSON schema object describing the JSON value encoded in string outputs for this function.

class BetaFileSearchTool: …

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

type: Literal["file\_search"]

The type of the file search tool. Always `file_search`.

vector\_store\_ids: List[str]

The IDs of the vector stores to search.

filters: Optional[Filters]

A filter to apply.

class FiltersComparisonFilter: …

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

str

float

bool

List[Union[str, float]]

str

float

class FiltersCompoundFilter: …

Combine multiple filters using `and` or `or`.

filters: List[FiltersCompoundFilterFilter]

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

class FiltersCompoundFilterFilterComparisonFilter: …

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

str

float

bool

List[Union[str, float]]

str

float

object

type: Literal["and", "or"]

Type of operation: `and` or `or`.

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

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

class BetaComputerTool: …

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

type: Literal["computer"]

The type of the computer tool. Always `computer`.

class BetaComputerUsePreviewTool: …

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

display\_height: int

The height of the computer display.

display\_width: int

The width of the computer display.

environment: Literal["windows", "mac", "linux", 2 more]

The type of computer environment to control.

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

The type of the computer use tool. Always `computer_use_preview`.

class BetaWebSearchTool: …

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

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

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

allowed\_tools: Optional[McpAllowedTools]

List of allowed tool names or a filter object.

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

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

A list of allowed domains when type is `allowlist`.

type: Literal["allowlist"]

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

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

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

class ProgrammaticToolCalling: …

type: Literal["programmatic\_tool\_calling"]

The type of the tool. Always `programmatic_tool_calling`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

The type of the image generation tool. Always `image_generation`.

action: Optional[Literal["generate", "edit", "auto"]]

Whether to generate a new image or edit an existing image. Default: `auto`.

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

"transparent"

"opaque"

"auto"

input\_fidelity: Optional[Literal["high", "low"]]

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

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

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

The image generation model to use. Default: `gpt-image-1`.

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

Moderation level for the generated image. Default: `auto`.

"auto"

"low"

output\_compression: Optional[int]

Compression level for the output image. Default: 100.

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

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

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool: …

A tool that allows the model to execute shell commands.

type: Literal["shell"]

The type of the shell tool. Always `shell`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

environment: Optional[Environment]

class BetaContainerAuto: …

type: Literal["container\_auto"]

Automatically creates a container for this request

file\_ids: Optional[List[str]]

An optional list of uploaded files to make available to your code.

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

The memory limit for the container.

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

A list of allowed domains when type is `allowlist`.

type: Literal["allowlist"]

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

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

class BetaSkillReference: …

skill\_id: str

The ID of the referenced skill.

maxLength64

minLength1

type: Literal["skill\_reference"]

References a skill created with the /v1/skills endpoint.

version: Optional[str]

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

class BetaInlineSkill: …

description: str

The description of the skill.

name: str

The name of the skill.

source: [BetaInlineSkillSource](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

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

class BetaLocalEnvironment: …

type: Literal["local"]

Use a local computer environment.

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

An optional list of skills.

description: str

The description of the skill.

name: str

The name of the skill.

path: str

The path to the directory containing the skill.

class BetaContainerReference: …

container\_id: str

The ID of the referenced container.

type: Literal["container\_reference"]

References a container created with the /v1/containers endpoint

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

The name of the custom tool, used to identify it in tool calls.

type: Literal["custom"]

The type of the custom tool. Always `custom`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: Optional[bool]

Whether this tool should be deferred and discovered via tool search.

description: Optional[str]

Optional description of the custom tool, used to provide more context.

format: Optional[Format]

The input format for the custom tool. Default is unconstrained text.

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

A grammar defined by the user.

definition: str

The grammar definition.

syntax: Literal["lark", "regex"]

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: Literal["grammar"]

Grammar format. Always `grammar`.

class BetaNamespaceTool: …

Groups function/custom tools under a shared namespace.

description: str

A description of the namespace shown to the model.

minLength1

name: str

The namespace name used in tool calls (for example, `crm`).

minLength1

tools: List[Tool]

The function/custom tools available inside this namespace.

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: Optional[bool]

Whether this function should be deferred and discovered via tool search.

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

parameters: Optional[object]

strict: Optional[bool]

Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

The name of the custom tool, used to identify it in tool calls.

type: Literal["custom"]

The type of the custom tool. Always `custom`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: Optional[bool]

Whether this tool should be deferred and discovered via tool search.

description: Optional[str]

Optional description of the custom tool, used to provide more context.

format: Optional[Format]

The input format for the custom tool. Default is unconstrained text.

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

A grammar defined by the user.

definition: str

The grammar definition.

syntax: Literal["lark", "regex"]

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: Literal["grammar"]

Grammar format. Always `grammar`.

type: Literal["namespace"]

The type of the tool. Always `namespace`.

class BetaToolSearchTool: …

Hosted or BYOT tool search configuration for deferred tools.

type: Literal["tool\_search"]

The type of the tool. Always `tool_search`.

description: Optional[str]

Description shown to the model for a client-executed tool search tool.

execution: Optional[Literal["server", "client"]]

Whether tool search is executed by the server or by the client.

"server"

"client"

parameters: Optional[object]

Parameter schema for a client-executed tool search tool.

class BetaWebSearchPreviewTool: …

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

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

class BetaApplyPatchTool: …

Allows the assistant to create, delete, or update files using unified diffs.

type: Literal["apply\_patch"]

The type of the tool. Always `apply_patch`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

type: Literal["tool\_search\_output"]

The item type. Always `tool_search_output`.

id: Optional[str]

The unique ID of this tool search output.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

call\_id: Optional[str]

The unique ID of the tool search call generated by the model.

maxLength64

minLength1

execution: Optional[Literal["server", "client"]]

Whether tool search was executed by the server or by the client.

"server"

"client"

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the tool search output.

"in\_progress"

"completed"

"incomplete"

class AdditionalTools: …

role: Literal["developer"]

The role that provided the additional tools. Only `developer` is supported.

tools: List[[BetaTool](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))]

A list of additional tools made available at this item.

class BetaFunctionTool: …

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

name: str

The name of the function to call.

parameters: Optional[Dict[str, object]]

A JSON schema object describing the parameters of the function.

strict: Optional[bool]

Whether strict parameter validation is enforced for this function tool.

type: Literal["function"]

The type of the function tool. Always `function`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: Optional[bool]

Whether this function is deferred and loaded via tool search.

description: Optional[str]

A description of the function. Used by the model to determine whether or not to call the function.

output\_schema: Optional[Dict[str, object]]

A JSON schema object describing the JSON value encoded in string outputs for this function.

class BetaFileSearchTool: …

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

type: Literal["file\_search"]

The type of the file search tool. Always `file_search`.

vector\_store\_ids: List[str]

The IDs of the vector stores to search.

filters: Optional[Filters]

A filter to apply.

class FiltersComparisonFilter: …

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

str

float

bool

List[Union[str, float]]

str

float

class FiltersCompoundFilter: …

Combine multiple filters using `and` or `or`.

filters: List[FiltersCompoundFilterFilter]

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

class FiltersCompoundFilterFilterComparisonFilter: …

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

str

float

bool

List[Union[str, float]]

str

float

object

type: Literal["and", "or"]

Type of operation: `and` or `or`.

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

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

class BetaComputerTool: …

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

type: Literal["computer"]

The type of the computer tool. Always `computer`.

class BetaComputerUsePreviewTool: …

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

display\_height: int

The height of the computer display.

display\_width: int

The width of the computer display.

environment: Literal["windows", "mac", "linux", 2 more]

The type of computer environment to control.

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

The type of the computer use tool. Always `computer_use_preview`.

class BetaWebSearchTool: …

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

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

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

allowed\_tools: Optional[McpAllowedTools]

List of allowed tool names or a filter object.

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

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

A list of allowed domains when type is `allowlist`.

type: Literal["allowlist"]

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

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

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

class ProgrammaticToolCalling: …

type: Literal["programmatic\_tool\_calling"]

The type of the tool. Always `programmatic_tool_calling`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

The type of the image generation tool. Always `image_generation`.

action: Optional[Literal["generate", "edit", "auto"]]

Whether to generate a new image or edit an existing image. Default: `auto`.

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

"transparent"

"opaque"

"auto"

input\_fidelity: Optional[Literal["high", "low"]]

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

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

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

The image generation model to use. Default: `gpt-image-1`.

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

Moderation level for the generated image. Default: `auto`.

"auto"

"low"

output\_compression: Optional[int]

Compression level for the output image. Default: 100.

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

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

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool: …

A tool that allows the model to execute shell commands.

type: Literal["shell"]

The type of the shell tool. Always `shell`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

environment: Optional[Environment]

class BetaContainerAuto: …

type: Literal["container\_auto"]

Automatically creates a container for this request

file\_ids: Optional[List[str]]

An optional list of uploaded files to make available to your code.

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

The memory limit for the container.

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

A list of allowed domains when type is `allowlist`.

type: Literal["allowlist"]

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

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

class BetaSkillReference: …

skill\_id: str

The ID of the referenced skill.

maxLength64

minLength1

type: Literal["skill\_reference"]

References a skill created with the /v1/skills endpoint.

version: Optional[str]

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

class BetaInlineSkill: …

description: str

The description of the skill.

name: str

The name of the skill.

source: [BetaInlineSkillSource](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

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

class BetaLocalEnvironment: …

type: Literal["local"]

Use a local computer environment.

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

An optional list of skills.

description: str

The description of the skill.

name: str

The name of the skill.

path: str

The path to the directory containing the skill.

class BetaContainerReference: …

container\_id: str

The ID of the referenced container.

type: Literal["container\_reference"]

References a container created with the /v1/containers endpoint

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

The name of the custom tool, used to identify it in tool calls.

type: Literal["custom"]

The type of the custom tool. Always `custom`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: Optional[bool]

Whether this tool should be deferred and discovered via tool search.

description: Optional[str]

Optional description of the custom tool, used to provide more context.

format: Optional[Format]

The input format for the custom tool. Default is unconstrained text.

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

A grammar defined by the user.

definition: str

The grammar definition.

syntax: Literal["lark", "regex"]

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: Literal["grammar"]

Grammar format. Always `grammar`.

class BetaNamespaceTool: …

Groups function/custom tools under a shared namespace.

description: str

A description of the namespace shown to the model.

minLength1

name: str

The namespace name used in tool calls (for example, `crm`).

minLength1

tools: List[Tool]

The function/custom tools available inside this namespace.

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: Optional[bool]

Whether this function should be deferred and discovered via tool search.

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

parameters: Optional[object]

strict: Optional[bool]

Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

The name of the custom tool, used to identify it in tool calls.

type: Literal["custom"]

The type of the custom tool. Always `custom`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: Optional[bool]

Whether this tool should be deferred and discovered via tool search.

description: Optional[str]

Optional description of the custom tool, used to provide more context.

format: Optional[Format]

The input format for the custom tool. Default is unconstrained text.

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

A grammar defined by the user.

definition: str

The grammar definition.

syntax: Literal["lark", "regex"]

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: Literal["grammar"]

Grammar format. Always `grammar`.

type: Literal["namespace"]

The type of the tool. Always `namespace`.

class BetaToolSearchTool: …

Hosted or BYOT tool search configuration for deferred tools.

type: Literal["tool\_search"]

The type of the tool. Always `tool_search`.

description: Optional[str]

Description shown to the model for a client-executed tool search tool.

execution: Optional[Literal["server", "client"]]

Whether tool search is executed by the server or by the client.

"server"

"client"

parameters: Optional[object]

Parameter schema for a client-executed tool search tool.

class BetaWebSearchPreviewTool: …

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

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

class BetaApplyPatchTool: …

Allows the assistant to create, delete, or update files using unified diffs.

type: Literal["apply\_patch"]

The type of the tool. Always `apply_patch`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

type: Literal["additional\_tools"]

The item type. Always `additional_tools`.

id: Optional[str]

The unique ID of this additional tools item.

agent: Optional[AdditionalToolsAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class BetaResponseReasoningItem: …

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

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

content: Optional[List[Content]]

Reasoning text content.

text: str

The reasoning text from the model.

type: Literal["reasoning\_text"]

The type of the reasoning text. Always `reasoning_text`.

encrypted\_content: Optional[str]

The encrypted content of the reasoning item. This is populated by default
for reasoning items returned by `POST /v1/responses` and WebSocket
`response.create` requests.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

class BetaResponseCompactionItemParam: …

A compaction item generated by the [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).

encrypted\_content: str

The encrypted content of the compaction summary.

maxLength10485760

type: Literal["compaction"]

The type of the item. Always `compaction`.

id: Optional[str]

The ID of the compaction item.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class ImageGenerationCall: …

An image generation request made by the model.

id: str

The unique ID of the image generation call.

result: Optional[str]

The generated image encoded in base64.

status: Literal["in\_progress", "completed", "generating", "failed"]

The status of the image generation call.

"in\_progress"

"completed"

"generating"

"failed"

type: Literal["image\_generation\_call"]

The type of the image generation call. Always `image_generation_call`.

agent: Optional[ImageGenerationCallAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class BetaResponseCodeInterpreterToolCall: …

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

"in\_progress"

"completed"

"incomplete"

"interpreting"

"failed"

type: Literal["code\_interpreter\_call"]

The type of the code interpreter tool call. Always `code_interpreter_call`.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

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

"in\_progress"

"completed"

"incomplete"

type: Literal["local\_shell\_call"]

The type of the local shell call. Always `local_shell_call`.

agent: Optional[LocalShellCallAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class LocalShellCallOutput: …

The output of a local shell tool call.

id: str

The unique ID of the local shell tool call generated by the model.

output: str

A JSON string of the output of the local shell tool call.

type: Literal["local\_shell\_call\_output"]

The type of the local shell tool call output. Always `local_shell_call_output`.

agent: Optional[LocalShellCallOutputAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the item. One of `in_progress`, `completed`, or `incomplete`.

"in\_progress"

"completed"

"incomplete"

class ShellCall: …

A tool representing a request to execute one or more shell commands.

action: ShellCallAction

The shell commands and limits that describe how to run the tool call.

commands: List[str]

Ordered shell commands for the execution environment to run.

max\_output\_length: Optional[int]

Maximum number of UTF-8 characters to capture from combined stdout and stderr output.

timeout\_ms: Optional[int]

Maximum wall-clock time in milliseconds to allow the shell commands to run.

call\_id: str

The unique ID of the shell tool call generated by the model.

maxLength64

minLength1

type: Literal["shell\_call"]

The type of the item. Always `shell_call`.

id: Optional[str]

The unique ID of the shell tool call. Populated when this item is returned via API.

agent: Optional[ShellCallAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

caller: Optional[ShellCallCaller]

The execution context that produced this tool call.

class ShellCallCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class ShellCallCallerProgram: …

caller\_id: str

The call ID of the program item that produced this tool call.

maxLength64

minLength1

type: Literal["program"]

The caller type. Always `program`.

environment: Optional[ShellCallEnvironment]

The environment to execute the shell commands in.

class BetaLocalEnvironment: …

type: Literal["local"]

Use a local computer environment.

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

An optional list of skills.

description: str

The description of the skill.

name: str

The name of the skill.

path: str

The path to the directory containing the skill.

class BetaContainerReference: …

container\_id: str

The ID of the referenced container.

type: Literal["container\_reference"]

References a container created with the /v1/containers endpoint

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the shell call. One of `in_progress`, `completed`, or `incomplete`.

"in\_progress"

"completed"

"incomplete"

class ShellCallOutput: …

The streamed output items emitted by a shell tool call.

call\_id: str

The unique ID of the shell tool call generated by the model.

maxLength64

minLength1

output: List[[BetaResponseFunctionShellCallOutputContent](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_shell_call_output_content%20%3E%20(schema))]

Captured chunks of stdout and stderr output, along with their associated outcomes.

outcome: Outcome

The exit or timeout outcome associated with this shell call.

class OutcomeTimeout: …

Indicates that the shell call exceeded its configured time limit.

type: Literal["timeout"]

The outcome type. Always `timeout`.

class OutcomeExit: …

Indicates that the shell commands finished and returned an exit code.

exit\_code: int

The exit code returned by the shell process.

type: Literal["exit"]

The outcome type. Always `exit`.

stderr: str

Captured stderr output for the shell call.

maxLength10485760

stdout: str

Captured stdout output for the shell call.

maxLength10485760

type: Literal["shell\_call\_output"]

The type of the item. Always `shell_call_output`.

id: Optional[str]

The unique ID of the shell tool call output. Populated when this item is returned via API.

agent: Optional[ShellCallOutputAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

caller: Optional[ShellCallOutputCaller]

The execution context that produced this tool call.

class ShellCallOutputCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class ShellCallOutputCallerProgram: …

caller\_id: str

The call ID of the program item that produced this tool call.

maxLength64

minLength1

type: Literal["program"]

The caller type. Always `program`.

max\_output\_length: Optional[int]

The maximum number of UTF-8 characters captured for this shell call’s combined output.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the shell call output.

"in\_progress"

"completed"

"incomplete"

class ApplyPatchCall: …

A tool call representing a request to create, delete, or update files using diff patches.

call\_id: str

The unique ID of the apply patch tool call generated by the model.

maxLength64

minLength1

operation: ApplyPatchCallOperation

The specific create, delete, or update instruction for the apply\_patch tool call.

class ApplyPatchCallOperationCreateFile: …

Instruction for creating a new file via the apply\_patch tool.

diff: str

Unified diff content to apply when creating the file.

maxLength10485760

path: str

Path of the file to create relative to the workspace root.

minLength1

type: Literal["create\_file"]

The operation type. Always `create_file`.

class ApplyPatchCallOperationDeleteFile: …

Instruction for deleting an existing file via the apply\_patch tool.

path: str

Path of the file to delete relative to the workspace root.

minLength1

type: Literal["delete\_file"]

The operation type. Always `delete_file`.

class ApplyPatchCallOperationUpdateFile: …

Instruction for updating an existing file via the apply\_patch tool.

diff: str

Unified diff content to apply to the existing file.

maxLength10485760

path: str

Path of the file to update relative to the workspace root.

minLength1

type: Literal["update\_file"]

The operation type. Always `update_file`.

status: Literal["in\_progress", "completed"]

The status of the apply patch tool call. One of `in_progress` or `completed`.

"in\_progress"

"completed"

type: Literal["apply\_patch\_call"]

The type of the item. Always `apply_patch_call`.

id: Optional[str]

The unique ID of the apply patch tool call. Populated when this item is returned via API.

agent: Optional[ApplyPatchCallAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

caller: Optional[ApplyPatchCallCaller]

The execution context that produced this tool call.

class ApplyPatchCallCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class ApplyPatchCallCallerProgram: …

caller\_id: str

The call ID of the program item that produced this tool call.

maxLength64

minLength1

type: Literal["program"]

The caller type. Always `program`.

class ApplyPatchCallOutput: …

The streamed output emitted by an apply patch tool call.

call\_id: str

The unique ID of the apply patch tool call generated by the model.

maxLength64

minLength1

status: Literal["completed", "failed"]

The status of the apply patch tool call output. One of `completed` or `failed`.

"completed"

"failed"

type: Literal["apply\_patch\_call\_output"]

The type of the item. Always `apply_patch_call_output`.

id: Optional[str]

The unique ID of the apply patch tool call output. Populated when this item is returned via API.

agent: Optional[ApplyPatchCallOutputAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

caller: Optional[ApplyPatchCallOutputCaller]

The execution context that produced this tool call.

class ApplyPatchCallOutputCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class ApplyPatchCallOutputCallerProgram: …

caller\_id: str

The call ID of the program item that produced this tool call.

maxLength64

minLength1

type: Literal["program"]

The caller type. Always `program`.

output: Optional[str]

Optional human-readable log text from the apply patch tool (e.g., patch results or errors).

maxLength10485760

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

agent: Optional[McpListToolsAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

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

agent: Optional[McpApprovalRequestAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class McpApprovalResponse: …

A response to an MCP approval request.

approval\_request\_id: str

The ID of the approval request being answered.

approve: bool

Whether the request was approved.

type: Literal["mcp\_approval\_response"]

The type of the item. Always `mcp_approval_response`.

id: Optional[str]

The unique ID of the approval response

agent: Optional[McpApprovalResponseAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

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

agent: Optional[McpCallAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

approval\_request\_id: Optional[str]

Unique identifier for the MCP tool call approval request.
Include this value in a subsequent `mcp_approval_response` input to approve or reject the corresponding tool call.

error: Optional[str]

The error from the tool call, if any.

output: Optional[str]

The output from the tool call.

status: Optional[Literal["in\_progress", "completed", "incomplete", 2 more]]

The status of the tool call. One of `in_progress`, `completed`, `incomplete`, `calling`, or `failed`.

"in\_progress"

"completed"

"incomplete"

"calling"

"failed"

class BetaResponseCustomToolCallOutput: …

The output of a custom tool call from your code, being sent back to the model.

call\_id: str

The call ID, used to map this custom tool call output to a custom tool call.

output: Union[str, List[OutputOutputContentList]]

The output from the custom tool call generated by your code.
Can be a string or an list of output content.

str

A string of the output of the custom tool call.

List[OutputOutputContentList]

Text, image, or file output of the custom tool call.

class BetaResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

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

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class BetaResponseInputFile: …

A file input to the model.

type: Literal["input\_file"]

The type of the input item. Always `input_file`.

detail: Optional[Literal["auto", "low", "high"]]

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

"auto"

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

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

type: Literal["custom\_tool\_call\_output"]

The type of the custom tool call output. Always `custom_tool_call_output`.

id: Optional[str]

The unique ID of the custom tool call output in the OpenAI platform.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

caller: Optional[Caller]

The execution context that produced this tool call.

class CallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class CallerProgram: …

caller\_id: str

The call ID of the program item that produced this tool call.

maxLength64

minLength1

type: Literal["program"]

The caller type. Always `program`.

class BetaResponseCustomToolCall: …

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

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

caller: Optional[Caller]

The execution context that produced this tool call.

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

The call ID of the program item that produced this tool call.

type: Literal["program"]

namespace: Optional[str]

The namespace of the custom tool being called.

class CompactionTrigger: …

Compacts the current context. Must be the final input item.

type: Literal["compaction\_trigger"]

The type of the item. Always `compaction_trigger`.

agent: Optional[CompactionTriggerAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class ItemReference: …

An internal identifier for an item to reference.

id: str

The ID of the item to reference.

agent: Optional[ItemReferenceAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

type: Optional[Literal["item\_reference"]]

The type of item to reference. Always `item_reference`.

class Program: …

id: str

The unique ID of this program item.

call\_id: str

The stable call ID of the program item.

maxLength64

minLength1

code: str

The JavaScript source executed by programmatic tool calling.

maxLength10485760

fingerprint: str

Opaque program replay fingerprint that must be round-tripped.

maxLength10485760

type: Literal["program"]

The item type. Always `program`.

agent: Optional[ProgramAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class ProgramOutput: …

id: str

The unique ID of this program output item.

call\_id: str

The call ID of the program item.

maxLength64

minLength1

result: str

The result produced by the program item.

maxLength10485760

status: Literal["completed", "incomplete"]

The terminal status of the program output.

"completed"

"incomplete"

type: Literal["program\_output"]

The item type. Always `program_output`.

agent: Optional[ProgramOutputAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

metadata: Optional[Dict[str, str]]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: Union[Literal["gpt-5.6-sol", "gpt-5.6-terra", "gpt-5.6-luna", 92 more], str]

Model ID used to generate the response, like `gpt-4o` or `o3`. OpenAI
offers a wide range of models with different capabilities, performance
characteristics, and price points. Refer to the [model guide](https://platform.openai.com/docs/models)
to browse and compare available models.

Literal["gpt-5.6-sol", "gpt-5.6-terra", "gpt-5.6-luna", 92 more]

Model ID used to generate the response, like `gpt-4o` or `o3`. OpenAI
offers a wide range of models with different capabilities, performance
characteristics, and price points. Refer to the [model guide](https://platform.openai.com/docs/models)
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

str

object: Literal["response"]

The object type of this resource - always set to `response`.

output: List[[BetaResponseOutputItem](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_item%20%3E%20(schema))]

An array of content items generated by the model.

* The length and order of items in the `output` array is dependent
  on the model’s response.
* Rather than accessing the first item in the `output` array and
  assuming it’s an `assistant` message with the content generated by
  the model, you might consider using the `output_text` property where
  supported in SDKs.

class BetaResponseOutputMessage: …

An output message from the model.

id: str

The unique ID of the output message.

content: List[Content]

The content of the output message.

class BetaResponseOutputText: …

A text output from the model.

annotations: List[Annotation]

The annotations of the text output.

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

class BetaResponseOutputRefusal: …

A refusal from the model.

refusal: str

The refusal explanation from the model.

type: Literal["refusal"]

The type of the refusal. Always `refusal`.

role: Literal["assistant"]

The role of the output message. Always `assistant`.

status: Literal["in\_progress", "completed", "incomplete"]

The status of the message input. One of `in_progress`, `completed`, or
`incomplete`. Populated when input items are returned via API.

"in\_progress"

"completed"

"incomplete"

type: Literal["message"]

The type of the output message. Always `message`.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

phase: Optional[Literal["commentary", "final\_answer"]]

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

"commentary"

"final\_answer"

class BetaResponseFileSearchToolCall: …

The results of a file search tool call. See the
[file search guide](https://platform.openai.com/docs/guides/tools-file-search) for more information.

id: str

The unique ID of the file search tool call.

queries: List[str]

The queries used to search for files.

status: Literal["in\_progress", "searching", "completed", 2 more]

The status of the file search tool call. One of `in_progress`,
`searching`, `incomplete` or `failed`,

"in\_progress"

"searching"

"completed"

"incomplete"

"failed"

type: Literal["file\_search\_call"]

The type of the file search tool call. Always `file_search_call`.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

results: Optional[List[Result]]

The results of the file search tool call.

attributes: Optional[Dict[str, Union[str, float, bool]]]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.

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

class BetaResponseFunctionToolCall: …

A tool call to run a function. See the
[function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.

arguments: str

A JSON string of the arguments to pass to the function.

call\_id: str

The unique ID of the function tool call generated by the model.

name: str

The name of the function to run.

type: Literal["function\_call"]

The type of the function tool call. Always `function_call`.

id: Optional[str]

The unique ID of the function tool call.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

caller: Optional[Caller]

The execution context that produced this tool call.

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

The call ID of the program item that produced this tool call.

type: Literal["program"]

namespace: Optional[str]

The namespace of the function to run.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

class BetaResponseFunctionToolCallOutputItem: …

id: str

The unique ID of the function call tool output.

call\_id: str

The unique ID of the function tool call generated by the model.

output: Union[str, List[OutputOutputContentList]]

The output from the function call generated by your code.
Can be a string or an list of output content.

str

A string of the output of the function call.

List[OutputOutputContentList]

Text, image, or file output of the function call.

class BetaResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

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

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class BetaResponseInputFile: …

A file input to the model.

type: Literal["input\_file"]

The type of the input item. Always `input_file`.

detail: Optional[Literal["auto", "low", "high"]]

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

"auto"

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

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

status: Literal["in\_progress", "completed", "incomplete"]

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

type: Literal["function\_call\_output"]

The type of the function tool call output. Always `function_call_output`.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

caller: Optional[Caller]

The execution context that produced this tool call.

class CallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class CallerProgram: …

caller\_id: str

The call ID of the program item that produced this tool call.

maxLength64

minLength1

type: Literal["program"]

The caller type. Always `program`.

created\_by: Optional[str]

The identifier of the actor that created the item.

class AgentMessage: …

id: str

The unique ID of the agent message.

author: str

The sending agent identity.

content: List[AgentMessageContent]

Encrypted content sent between agents.

class BetaResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class BetaResponseOutputText: …

A text output from the model.

annotations: List[Annotation]

The annotations of the text output.

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

class AgentMessageContentText: …

A text content.

text: str

type: Literal["text"]

class AgentMessageContentSummaryText: …

A summary text from the model.

text: str

A summary of the reasoning output from the model so far.

type: Literal["summary\_text"]

The type of the object. Always `summary_text`.

class AgentMessageContentReasoningText: …

Reasoning text from the model.

text: str

The reasoning text from the model.

type: Literal["reasoning\_text"]

The type of the reasoning text. Always `reasoning_text`.

class BetaResponseOutputRefusal: …

A refusal from the model.

refusal: str

The refusal explanation from the model.

type: Literal["refusal"]

The type of the refusal. Always `refusal`.

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

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

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class AgentMessageContentComputerScreenshot: …

A screenshot of a computer.

detail: Literal["low", "high", "auto", "original"]

The detail level of the screenshot image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

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

prompt\_cache\_breakpoint: Optional[AgentMessageContentComputerScreenshotPromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class BetaResponseInputFile: …

A file input to the model.

type: Literal["input\_file"]

The type of the input item. Always `input_file`.

detail: Optional[Literal["auto", "low", "high"]]

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

"auto"

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

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class AgentMessageContentEncryptedContent: …

Opaque encrypted content that Responses API decrypts inside trusted model execution.

encrypted\_content: str

Opaque encrypted content.

type: Literal["encrypted\_content"]

The type of the input item. Always `encrypted_content`.

recipient: str

The destination agent identity.

type: Literal["agent\_message"]

The type of the item. Always `agent_message`.

agent: Optional[AgentMessageAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class MultiAgentCall: …

id: str

The unique ID of the multi-agent call item.

action: Literal["spawn\_agent", "interrupt\_agent", "list\_agents", 3 more]

The multi-agent action to execute.

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

arguments: str

The JSON string of arguments generated for the action.

call\_id: str

The unique ID linking this call to its output.

type: Literal["multi\_agent\_call"]

The type of the multi-agent call. Always `multi_agent_call`.

agent: Optional[MultiAgentCallAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class MultiAgentCallOutput: …

id: str

The unique ID of the multi-agent call output item.

action: Literal["spawn\_agent", "interrupt\_agent", "list\_agents", 3 more]

The multi-agent action that produced this result.

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

call\_id: str

The unique ID of the multi-agent call.

output: List[[BetaResponseOutputText](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_text%20%3E%20(schema))]

Text output returned by the multi-agent action.

annotations: List[Annotation]

The annotations of the text output.

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

type: Literal["multi\_agent\_call\_output"]

The type of the multi-agent result. Always `multi_agent_call_output`.

agent: Optional[MultiAgentCallOutputAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class BetaResponseFunctionWebSearch: …

The results of a web search tool call. See the
[web search guide](https://platform.openai.com/docs/guides/tools-web-search) for more information.

id: str

The unique ID of the web search tool call.

action: Action

An object describing the specific action taken in this web search call.
Includes details on how the model used the web (search, open\_page, find\_in\_page).

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

"in\_progress"

"searching"

"completed"

"failed"

type: Literal["web\_search\_call"]

The type of the web search tool call. Always `web_search_call`.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class BetaResponseComputerToolCall: …

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

"in\_progress"

"completed"

"incomplete"

type: Literal["computer\_call"]

The type of the computer call. Always `computer_call`.

action: Optional[BetaComputerAction]

A click action.

class Click: …

A click action.

button: Literal["left", "right", "wheel", 2 more]

Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

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

actions: Optional[BetaComputerActionList]

Flattened batched actions for `computer_use`. Each action includes an
`type` discriminator and action-specific fields.

class Click: …

A click action.

button: Literal["left", "right", "wheel", 2 more]

Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

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

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class BetaResponseComputerToolCallOutputItem: …

id: str

The unique ID of the computer call tool output.

call\_id: str

The ID of the computer tool call that produced the output.

output: [BetaResponseComputerToolCallOutputScreenshot](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_computer_tool_call_output_screenshot%20%3E%20(schema))

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

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

created\_by: Optional[str]

The identifier of the actor that created the item.

class BetaResponseReasoningItem: …

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

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

content: Optional[List[Content]]

Reasoning text content.

text: str

The reasoning text from the model.

type: Literal["reasoning\_text"]

The type of the reasoning text. Always `reasoning_text`.

encrypted\_content: Optional[str]

The encrypted content of the reasoning item. This is populated by default
for reasoning items returned by `POST /v1/responses` and WebSocket
`response.create` requests.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

class Program: …

id: str

The unique ID of the program item.

call\_id: str

The stable call ID of the program item.

code: str

The JavaScript source executed by programmatic tool calling.

fingerprint: str

Opaque program replay fingerprint that must be round-tripped.

type: Literal["program"]

The type of the item. Always `program`.

agent: Optional[ProgramAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class ProgramOutput: …

id: str

The unique ID of the program output item.

call\_id: str

The call ID of the program item.

result: str

The result produced by the program item.

status: Literal["completed", "incomplete"]

The terminal status of the program output item.

"completed"

"incomplete"

type: Literal["program\_output"]

The type of the item. Always `program_output`.

agent: Optional[ProgramOutputAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class BetaResponseToolSearchCall: …

id: str

The unique ID of the tool search call item.

arguments: object

Arguments used for the tool search call.

call\_id: Optional[str]

The unique ID of the tool search call generated by the model.

execution: Literal["server", "client"]

Whether tool search was executed by the server or by the client.

"server"

"client"

status: Literal["in\_progress", "completed", "incomplete"]

The status of the tool search call item that was recorded.

"in\_progress"

"completed"

"incomplete"

type: Literal["tool\_search\_call"]

The type of the item. Always `tool_search_call`.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

created\_by: Optional[str]

The identifier of the actor that created the item.

class BetaResponseToolSearchOutputItem: …

id: str

The unique ID of the tool search output item.

call\_id: Optional[str]

The unique ID of the tool search call generated by the model.

execution: Literal["server", "client"]

Whether tool search was executed by the server or by the client.

"server"

"client"

status: Literal["in\_progress", "completed", "incomplete"]

The status of the tool search output item that was recorded.

"in\_progress"

"completed"

"incomplete"

tools: List[[BetaTool](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))]

The loaded tool definitions returned by tool search.

class BetaFunctionTool: …

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

name: str

The name of the function to call.

parameters: Optional[Dict[str, object]]

A JSON schema object describing the parameters of the function.

strict: Optional[bool]

Whether strict parameter validation is enforced for this function tool.

type: Literal["function"]

The type of the function tool. Always `function`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: Optional[bool]

Whether this function is deferred and loaded via tool search.

description: Optional[str]

A description of the function. Used by the model to determine whether or not to call the function.

output\_schema: Optional[Dict[str, object]]

A JSON schema object describing the JSON value encoded in string outputs for this function.

class BetaFileSearchTool: …

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

type: Literal["file\_search"]

The type of the file search tool. Always `file_search`.

vector\_store\_ids: List[str]

The IDs of the vector stores to search.

filters: Optional[Filters]

A filter to apply.

class FiltersComparisonFilter: …

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

str

float

bool

List[Union[str, float]]

str

float

class FiltersCompoundFilter: …

Combine multiple filters using `and` or `or`.

filters: List[FiltersCompoundFilterFilter]

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

class FiltersCompoundFilterFilterComparisonFilter: …

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

str

float

bool

List[Union[str, float]]

str

float

object

type: Literal["and", "or"]

Type of operation: `and` or `or`.

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

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

class BetaComputerTool: …

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

type: Literal["computer"]

The type of the computer tool. Always `computer`.

class BetaComputerUsePreviewTool: …

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

display\_height: int

The height of the computer display.

display\_width: int

The width of the computer display.

environment: Literal["windows", "mac", "linux", 2 more]

The type of computer environment to control.

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

The type of the computer use tool. Always `computer_use_preview`.

class BetaWebSearchTool: …

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

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

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

allowed\_tools: Optional[McpAllowedTools]

List of allowed tool names or a filter object.

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

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

A list of allowed domains when type is `allowlist`.

type: Literal["allowlist"]

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

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

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

class ProgrammaticToolCalling: …

type: Literal["programmatic\_tool\_calling"]

The type of the tool. Always `programmatic_tool_calling`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

The type of the image generation tool. Always `image_generation`.

action: Optional[Literal["generate", "edit", "auto"]]

Whether to generate a new image or edit an existing image. Default: `auto`.

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

"transparent"

"opaque"

"auto"

input\_fidelity: Optional[Literal["high", "low"]]

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

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

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

The image generation model to use. Default: `gpt-image-1`.

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

Moderation level for the generated image. Default: `auto`.

"auto"

"low"

output\_compression: Optional[int]

Compression level for the output image. Default: 100.

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

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

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool: …

A tool that allows the model to execute shell commands.

type: Literal["shell"]

The type of the shell tool. Always `shell`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

environment: Optional[Environment]

class BetaContainerAuto: …

type: Literal["container\_auto"]

Automatically creates a container for this request

file\_ids: Optional[List[str]]

An optional list of uploaded files to make available to your code.

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

The memory limit for the container.

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

A list of allowed domains when type is `allowlist`.

type: Literal["allowlist"]

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

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

class BetaSkillReference: …

skill\_id: str

The ID of the referenced skill.

maxLength64

minLength1

type: Literal["skill\_reference"]

References a skill created with the /v1/skills endpoint.

version: Optional[str]

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

class BetaInlineSkill: …

description: str

The description of the skill.

name: str

The name of the skill.

source: [BetaInlineSkillSource](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

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

class BetaLocalEnvironment: …

type: Literal["local"]

Use a local computer environment.

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

An optional list of skills.

description: str

The description of the skill.

name: str

The name of the skill.

path: str

The path to the directory containing the skill.

class BetaContainerReference: …

container\_id: str

The ID of the referenced container.

type: Literal["container\_reference"]

References a container created with the /v1/containers endpoint

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

The name of the custom tool, used to identify it in tool calls.

type: Literal["custom"]

The type of the custom tool. Always `custom`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: Optional[bool]

Whether this tool should be deferred and discovered via tool search.

description: Optional[str]

Optional description of the custom tool, used to provide more context.

format: Optional[Format]

The input format for the custom tool. Default is unconstrained text.

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

A grammar defined by the user.

definition: str

The grammar definition.

syntax: Literal["lark", "regex"]

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: Literal["grammar"]

Grammar format. Always `grammar`.

class BetaNamespaceTool: …

Groups function/custom tools under a shared namespace.

description: str

A description of the namespace shown to the model.

minLength1

name: str

The namespace name used in tool calls (for example, `crm`).

minLength1

tools: List[Tool]

The function/custom tools available inside this namespace.

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: Optional[bool]

Whether this function should be deferred and discovered via tool search.

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

parameters: Optional[object]

strict: Optional[bool]

Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

The name of the custom tool, used to identify it in tool calls.

type: Literal["custom"]

The type of the custom tool. Always `custom`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: Optional[bool]

Whether this tool should be deferred and discovered via tool search.

description: Optional[str]

Optional description of the custom tool, used to provide more context.

format: Optional[Format]

The input format for the custom tool. Default is unconstrained text.

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

A grammar defined by the user.

definition: str

The grammar definition.

syntax: Literal["lark", "regex"]

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: Literal["grammar"]

Grammar format. Always `grammar`.

type: Literal["namespace"]

The type of the tool. Always `namespace`.

class BetaToolSearchTool: …

Hosted or BYOT tool search configuration for deferred tools.

type: Literal["tool\_search"]

The type of the tool. Always `tool_search`.

description: Optional[str]

Description shown to the model for a client-executed tool search tool.

execution: Optional[Literal["server", "client"]]

Whether tool search is executed by the server or by the client.

"server"

"client"

parameters: Optional[object]

Parameter schema for a client-executed tool search tool.

class BetaWebSearchPreviewTool: …

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

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

class BetaApplyPatchTool: …

Allows the assistant to create, delete, or update files using unified diffs.

type: Literal["apply\_patch"]

The type of the tool. Always `apply_patch`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

type: Literal["tool\_search\_output"]

The type of the item. Always `tool_search_output`.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

created\_by: Optional[str]

The identifier of the actor that created the item.

class AdditionalTools: …

id: str

The unique ID of the additional tools item.

role: Literal["unknown", "user", "assistant", 5 more]

The role that provided the additional tools.

"unknown"

"user"

"assistant"

"system"

"critic"

"discriminator"

"developer"

"tool"

tools: List[[BetaTool](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))]

The additional tool definitions made available at this item.

class BetaFunctionTool: …

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

name: str

The name of the function to call.

parameters: Optional[Dict[str, object]]

A JSON schema object describing the parameters of the function.

strict: Optional[bool]

Whether strict parameter validation is enforced for this function tool.

type: Literal["function"]

The type of the function tool. Always `function`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: Optional[bool]

Whether this function is deferred and loaded via tool search.

description: Optional[str]

A description of the function. Used by the model to determine whether or not to call the function.

output\_schema: Optional[Dict[str, object]]

A JSON schema object describing the JSON value encoded in string outputs for this function.

class BetaFileSearchTool: …

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

type: Literal["file\_search"]

The type of the file search tool. Always `file_search`.

vector\_store\_ids: List[str]

The IDs of the vector stores to search.

filters: Optional[Filters]

A filter to apply.

class FiltersComparisonFilter: …

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

str

float

bool

List[Union[str, float]]

str

float

class FiltersCompoundFilter: …

Combine multiple filters using `and` or `or`.

filters: List[FiltersCompoundFilterFilter]

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

class FiltersCompoundFilterFilterComparisonFilter: …

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

str

float

bool

List[Union[str, float]]

str

float

object

type: Literal["and", "or"]

Type of operation: `and` or `or`.

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

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

class BetaComputerTool: …

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

type: Literal["computer"]

The type of the computer tool. Always `computer`.

class BetaComputerUsePreviewTool: …

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

display\_height: int

The height of the computer display.

display\_width: int

The width of the computer display.

environment: Literal["windows", "mac", "linux", 2 more]

The type of computer environment to control.

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

The type of the computer use tool. Always `computer_use_preview`.

class BetaWebSearchTool: …

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

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

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

allowed\_tools: Optional[McpAllowedTools]

List of allowed tool names or a filter object.

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

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

A list of allowed domains when type is `allowlist`.

type: Literal["allowlist"]

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

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

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

class ProgrammaticToolCalling: …

type: Literal["programmatic\_tool\_calling"]

The type of the tool. Always `programmatic_tool_calling`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

The type of the image generation tool. Always `image_generation`.

action: Optional[Literal["generate", "edit", "auto"]]

Whether to generate a new image or edit an existing image. Default: `auto`.

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

"transparent"

"opaque"

"auto"

input\_fidelity: Optional[Literal["high", "low"]]

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

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

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

The image generation model to use. Default: `gpt-image-1`.

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

Moderation level for the generated image. Default: `auto`.

"auto"

"low"

output\_compression: Optional[int]

Compression level for the output image. Default: 100.

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

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

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool: …

A tool that allows the model to execute shell commands.

type: Literal["shell"]

The type of the shell tool. Always `shell`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

environment: Optional[Environment]

class BetaContainerAuto: …

type: Literal["container\_auto"]

Automatically creates a container for this request

file\_ids: Optional[List[str]]

An optional list of uploaded files to make available to your code.

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

The memory limit for the container.

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

A list of allowed domains when type is `allowlist`.

type: Literal["allowlist"]

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

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

class BetaSkillReference: …

skill\_id: str

The ID of the referenced skill.

maxLength64

minLength1

type: Literal["skill\_reference"]

References a skill created with the /v1/skills endpoint.

version: Optional[str]

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

class BetaInlineSkill: …

description: str

The description of the skill.

name: str

The name of the skill.

source: [BetaInlineSkillSource](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

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

class BetaLocalEnvironment: …

type: Literal["local"]

Use a local computer environment.

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

An optional list of skills.

description: str

The description of the skill.

name: str

The name of the skill.

path: str

The path to the directory containing the skill.

class BetaContainerReference: …

container\_id: str

The ID of the referenced container.

type: Literal["container\_reference"]

References a container created with the /v1/containers endpoint

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

The name of the custom tool, used to identify it in tool calls.

type: Literal["custom"]

The type of the custom tool. Always `custom`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: Optional[bool]

Whether this tool should be deferred and discovered via tool search.

description: Optional[str]

Optional description of the custom tool, used to provide more context.

format: Optional[Format]

The input format for the custom tool. Default is unconstrained text.

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

A grammar defined by the user.

definition: str

The grammar definition.

syntax: Literal["lark", "regex"]

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: Literal["grammar"]

Grammar format. Always `grammar`.

class BetaNamespaceTool: …

Groups function/custom tools under a shared namespace.

description: str

A description of the namespace shown to the model.

minLength1

name: str

The namespace name used in tool calls (for example, `crm`).

minLength1

tools: List[Tool]

The function/custom tools available inside this namespace.

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: Optional[bool]

Whether this function should be deferred and discovered via tool search.

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

parameters: Optional[object]

strict: Optional[bool]

Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

The name of the custom tool, used to identify it in tool calls.

type: Literal["custom"]

The type of the custom tool. Always `custom`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: Optional[bool]

Whether this tool should be deferred and discovered via tool search.

description: Optional[str]

Optional description of the custom tool, used to provide more context.

format: Optional[Format]

The input format for the custom tool. Default is unconstrained text.

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

A grammar defined by the user.

definition: str

The grammar definition.

syntax: Literal["lark", "regex"]

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: Literal["grammar"]

Grammar format. Always `grammar`.

type: Literal["namespace"]

The type of the tool. Always `namespace`.

class BetaToolSearchTool: …

Hosted or BYOT tool search configuration for deferred tools.

type: Literal["tool\_search"]

The type of the tool. Always `tool_search`.

description: Optional[str]

Description shown to the model for a client-executed tool search tool.

execution: Optional[Literal["server", "client"]]

Whether tool search is executed by the server or by the client.

"server"

"client"

parameters: Optional[object]

Parameter schema for a client-executed tool search tool.

class BetaWebSearchPreviewTool: …

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

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

class BetaApplyPatchTool: …

Allows the assistant to create, delete, or update files using unified diffs.

type: Literal["apply\_patch"]

The type of the tool. Always `apply_patch`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

type: Literal["additional\_tools"]

The type of the item. Always `additional_tools`.

agent: Optional[AdditionalToolsAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class BetaResponseCompactionItem: …

A compaction item generated by the [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).

id: str

The unique ID of the compaction item.

encrypted\_content: str

The encrypted content that was produced by compaction.

type: Literal["compaction"]

The type of the item. Always `compaction`.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

created\_by: Optional[str]

The identifier of the actor that created the item.

class ImageGenerationCall: …

An image generation request made by the model.

id: str

The unique ID of the image generation call.

result: Optional[str]

The generated image encoded in base64.

status: Literal["in\_progress", "completed", "generating", "failed"]

The status of the image generation call.

"in\_progress"

"completed"

"generating"

"failed"

type: Literal["image\_generation\_call"]

The type of the image generation call. Always `image_generation_call`.

agent: Optional[ImageGenerationCallAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class BetaResponseCodeInterpreterToolCall: …

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

"in\_progress"

"completed"

"incomplete"

"interpreting"

"failed"

type: Literal["code\_interpreter\_call"]

The type of the code interpreter tool call. Always `code_interpreter_call`.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

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

"in\_progress"

"completed"

"incomplete"

type: Literal["local\_shell\_call"]

The type of the local shell call. Always `local_shell_call`.

agent: Optional[LocalShellCallAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class LocalShellCallOutput: …

The output of a local shell tool call.

id: str

The unique ID of the local shell tool call generated by the model.

output: str

A JSON string of the output of the local shell tool call.

type: Literal["local\_shell\_call\_output"]

The type of the local shell tool call output. Always `local_shell_call_output`.

agent: Optional[LocalShellCallOutputAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the item. One of `in_progress`, `completed`, or `incomplete`.

"in\_progress"

"completed"

"incomplete"

class BetaResponseFunctionShellToolCall: …

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

class BetaResponseLocalEnvironment: …

Represents the use of a local environment to perform shell actions.

type: Literal["local"]

The environment type. Always `local`.

class BetaResponseContainerReference: …

Represents a container created with /v1/containers.

container\_id: str

type: Literal["container\_reference"]

The environment type. Always `container_reference`.

status: Literal["in\_progress", "completed", "incomplete"]

The status of the shell call. One of `in_progress`, `completed`, or `incomplete`.

"in\_progress"

"completed"

"incomplete"

type: Literal["shell\_call"]

The type of the item. Always `shell_call`.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

caller: Optional[Caller]

The execution context that produced this tool call.

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

The call ID of the program item that produced this tool call.

type: Literal["program"]

created\_by: Optional[str]

The ID of the entity that created this tool call.

class BetaResponseFunctionShellToolCallOutput: …

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

"in\_progress"

"completed"

"incomplete"

type: Literal["shell\_call\_output"]

The type of the shell call output. Always `shell_call_output`.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

caller: Optional[Caller]

The execution context that produced this tool call.

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

The call ID of the program item that produced this tool call.

type: Literal["program"]

created\_by: Optional[str]

The identifier of the actor that created the item.

class BetaResponseApplyPatchToolCall: …

A tool call that applies file diffs by creating, deleting, or updating files.

id: str

The unique ID of the apply patch tool call. Populated when this item is returned via API.

call\_id: str

The unique ID of the apply patch tool call generated by the model.

operation: Operation

One of the create\_file, delete\_file, or update\_file operations applied via apply\_patch.

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

"in\_progress"

"completed"

type: Literal["apply\_patch\_call"]

The type of the item. Always `apply_patch_call`.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

caller: Optional[Caller]

The execution context that produced this tool call.

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

The call ID of the program item that produced this tool call.

type: Literal["program"]

created\_by: Optional[str]

The ID of the entity that created this tool call.

class BetaResponseApplyPatchToolCallOutput: …

The output emitted by an apply patch tool call.

id: str

The unique ID of the apply patch tool call output. Populated when this item is returned via API.

call\_id: str

The unique ID of the apply patch tool call generated by the model.

status: Literal["completed", "failed"]

The status of the apply patch tool call output. One of `completed` or `failed`.

"completed"

"failed"

type: Literal["apply\_patch\_call\_output"]

The type of the item. Always `apply_patch_call_output`.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

caller: Optional[Caller]

The execution context that produced this tool call.

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

The call ID of the program item that produced this tool call.

type: Literal["program"]

created\_by: Optional[str]

The ID of the entity that created this tool call output.

output: Optional[str]

Optional textual output returned by the apply patch tool.

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

agent: Optional[McpCallAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

approval\_request\_id: Optional[str]

Unique identifier for the MCP tool call approval request.
Include this value in a subsequent `mcp_approval_response` input to approve or reject the corresponding tool call.

error: Optional[str]

The error from the tool call, if any.

output: Optional[str]

The output from the tool call.

status: Optional[Literal["in\_progress", "completed", "incomplete", 2 more]]

The status of the tool call. One of `in_progress`, `completed`, `incomplete`, `calling`, or `failed`.

"in\_progress"

"completed"

"incomplete"

"calling"

"failed"

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

agent: Optional[McpListToolsAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

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

agent: Optional[McpApprovalRequestAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

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

agent: Optional[McpApprovalResponseAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

reason: Optional[str]

Optional reason for the decision.

class BetaResponseCustomToolCall: …

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

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

caller: Optional[Caller]

The execution context that produced this tool call.

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

The call ID of the program item that produced this tool call.

type: Literal["program"]

namespace: Optional[str]

The namespace of the custom tool being called.

class BetaResponseCustomToolCallOutputItem: …

The output of a custom tool call from your code, being sent back to the model.

id: str

The unique ID of the custom tool call output item.

status: Literal["in\_progress", "completed", "incomplete"]

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

created\_by: Optional[str]

The identifier of the actor that created the item.

parallel\_tool\_calls: bool

Whether to allow the model to run tool calls in parallel.

temperature: Optional[float]

What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.
We generally recommend altering this or `top_p` but not both.

minimum0

maximum2

tool\_choice: ToolChoice

How the model should select which tool (or tools) to use when generating
a response. See the `tools` parameter to see how to specify which tools
the model can call.

Literal["none", "auto", "required"]

"none"

"auto"

"required"

class BetaToolChoiceAllowed: …

Constrains the tools available to the model to a pre-defined set.

mode: Literal["auto", "required"]

Constrains the tools available to the model to a pre-defined set.

`auto` allows the model to pick from among the allowed tools and generate a
message.

`required` requires the model to call one or more of the allowed tools.

"auto"

"required"

tools: List[Dict[str, object]]

A list of tool definitions that the model should be allowed to call.

For the Responses API, the list of tool definitions might look like:

[
  { "type": "function", "name": "get_weather" },
  { "type": "mcp", "server_label": "deepwiki" },
  { "type": "image_generation" }
]

type: Literal["allowed\_tools"]

Allowed tool configuration type. Always `allowed_tools`.

class BetaToolChoiceTypes: …

Indicates that the model should use a built-in tool to generate a response.
[Learn more about built-in tools](https://platform.openai.com/docs/guides/tools).

type: Literal["file\_search", "web\_search\_preview", "computer", 5 more]

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

class BetaToolChoiceFunction: …

Use this option to force the model to call a specific function.

name: str

The name of the function to call.

type: Literal["function"]

For function calling, the type is always `function`.

class BetaToolChoiceMcp: …

Use this option to force the model to call a specific tool on a remote MCP server.

server\_label: str

The label of the MCP server to use.

type: Literal["mcp"]

For MCP tools, the type is always `mcp`.

name: Optional[str]

The name of the tool to call on the server.

class BetaToolChoiceCustom: …

Use this option to force the model to call a specific custom tool.

name: str

The name of the custom tool to call.

type: Literal["custom"]

For custom tool calling, the type is always `custom`.

class ToolChoiceBetaSpecificProgrammaticToolCallingParam: …

type: Literal["programmatic\_tool\_calling"]

The tool to call. Always `programmatic_tool_calling`.

class BetaToolChoiceApplyPatch: …

Forces the model to call the apply\_patch tool when executing a tool call.

type: Literal["apply\_patch"]

The tool to call. Always `apply_patch`.

class BetaToolChoiceShell: …

Forces the model to call the shell tool when a tool call is required.

type: Literal["shell"]

The tool to call. Always `shell`.

tools: List[[BetaTool](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))]

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

class BetaFunctionTool: …

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

name: str

The name of the function to call.

parameters: Optional[Dict[str, object]]

A JSON schema object describing the parameters of the function.

strict: Optional[bool]

Whether strict parameter validation is enforced for this function tool.

type: Literal["function"]

The type of the function tool. Always `function`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: Optional[bool]

Whether this function is deferred and loaded via tool search.

description: Optional[str]

A description of the function. Used by the model to determine whether or not to call the function.

output\_schema: Optional[Dict[str, object]]

A JSON schema object describing the JSON value encoded in string outputs for this function.

class BetaFileSearchTool: …

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

type: Literal["file\_search"]

The type of the file search tool. Always `file_search`.

vector\_store\_ids: List[str]

The IDs of the vector stores to search.

filters: Optional[Filters]

A filter to apply.

class FiltersComparisonFilter: …

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

str

float

bool

List[Union[str, float]]

str

float

class FiltersCompoundFilter: …

Combine multiple filters using `and` or `or`.

filters: List[FiltersCompoundFilterFilter]

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

class FiltersCompoundFilterFilterComparisonFilter: …

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

str

float

bool

List[Union[str, float]]

str

float

object

type: Literal["and", "or"]

Type of operation: `and` or `or`.

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

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

class BetaComputerTool: …

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

type: Literal["computer"]

The type of the computer tool. Always `computer`.

class BetaComputerUsePreviewTool: …

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

display\_height: int

The height of the computer display.

display\_width: int

The width of the computer display.

environment: Literal["windows", "mac", "linux", 2 more]

The type of computer environment to control.

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

The type of the computer use tool. Always `computer_use_preview`.

class BetaWebSearchTool: …

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

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

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

allowed\_tools: Optional[McpAllowedTools]

List of allowed tool names or a filter object.

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

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

A list of allowed domains when type is `allowlist`.

type: Literal["allowlist"]

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

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

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

class ProgrammaticToolCalling: …

type: Literal["programmatic\_tool\_calling"]

The type of the tool. Always `programmatic_tool_calling`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

The type of the image generation tool. Always `image_generation`.

action: Optional[Literal["generate", "edit", "auto"]]

Whether to generate a new image or edit an existing image. Default: `auto`.

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

"transparent"

"opaque"

"auto"

input\_fidelity: Optional[Literal["high", "low"]]

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

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

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

The image generation model to use. Default: `gpt-image-1`.

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

Moderation level for the generated image. Default: `auto`.

"auto"

"low"

output\_compression: Optional[int]

Compression level for the output image. Default: 100.

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

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

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool: …

A tool that allows the model to execute shell commands.

type: Literal["shell"]

The type of the shell tool. Always `shell`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

environment: Optional[Environment]

class BetaContainerAuto: …

type: Literal["container\_auto"]

Automatically creates a container for this request

file\_ids: Optional[List[str]]

An optional list of uploaded files to make available to your code.

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

The memory limit for the container.

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

A list of allowed domains when type is `allowlist`.

type: Literal["allowlist"]

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

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

class BetaSkillReference: …

skill\_id: str

The ID of the referenced skill.

maxLength64

minLength1

type: Literal["skill\_reference"]

References a skill created with the /v1/skills endpoint.

version: Optional[str]

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

class BetaInlineSkill: …

description: str

The description of the skill.

name: str

The name of the skill.

source: [BetaInlineSkillSource](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

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

class BetaLocalEnvironment: …

type: Literal["local"]

Use a local computer environment.

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

An optional list of skills.

description: str

The description of the skill.

name: str

The name of the skill.

path: str

The path to the directory containing the skill.

class BetaContainerReference: …

container\_id: str

The ID of the referenced container.

type: Literal["container\_reference"]

References a container created with the /v1/containers endpoint

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

The name of the custom tool, used to identify it in tool calls.

type: Literal["custom"]

The type of the custom tool. Always `custom`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: Optional[bool]

Whether this tool should be deferred and discovered via tool search.

description: Optional[str]

Optional description of the custom tool, used to provide more context.

format: Optional[Format]

The input format for the custom tool. Default is unconstrained text.

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

A grammar defined by the user.

definition: str

The grammar definition.

syntax: Literal["lark", "regex"]

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: Literal["grammar"]

Grammar format. Always `grammar`.

class BetaNamespaceTool: …

Groups function/custom tools under a shared namespace.

description: str

A description of the namespace shown to the model.

minLength1

name: str

The namespace name used in tool calls (for example, `crm`).

minLength1

tools: List[Tool]

The function/custom tools available inside this namespace.

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: Optional[bool]

Whether this function should be deferred and discovered via tool search.

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

parameters: Optional[object]

strict: Optional[bool]

Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

The name of the custom tool, used to identify it in tool calls.

type: Literal["custom"]

The type of the custom tool. Always `custom`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: Optional[bool]

Whether this tool should be deferred and discovered via tool search.

description: Optional[str]

Optional description of the custom tool, used to provide more context.

format: Optional[Format]

The input format for the custom tool. Default is unconstrained text.

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

A grammar defined by the user.

definition: str

The grammar definition.

syntax: Literal["lark", "regex"]

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: Literal["grammar"]

Grammar format. Always `grammar`.

type: Literal["namespace"]

The type of the tool. Always `namespace`.

class BetaToolSearchTool: …

Hosted or BYOT tool search configuration for deferred tools.

type: Literal["tool\_search"]

The type of the tool. Always `tool_search`.

description: Optional[str]

Description shown to the model for a client-executed tool search tool.

execution: Optional[Literal["server", "client"]]

Whether tool search is executed by the server or by the client.

"server"

"client"

parameters: Optional[object]

Parameter schema for a client-executed tool search tool.

class BetaWebSearchPreviewTool: …

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

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

class BetaApplyPatchTool: …

Allows the assistant to create, delete, or update files using unified diffs.

type: Literal["apply\_patch"]

The type of the tool. Always `apply_patch`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

top\_p: Optional[float]

An alternative to sampling with temperature, called nucleus sampling,
where the model considers the results of the tokens with top\_p probability
mass. So 0.1 means only the tokens comprising the top 10% probability mass
are considered.

We generally recommend altering this or `temperature` but not both.

minimum0

maximum1

background: Optional[bool]

Whether to run the model response in the background.
[Learn more](https://platform.openai.com/docs/guides/background).

completed\_at: Optional[float]

Unix timestamp (in seconds) of when this Response was completed.
Only present when the status is `completed`.

formatunixtime

conversation: Optional[Conversation]

The conversation that this response belonged to. Input items and output items from this response were automatically added to this conversation.

id: str

The unique ID of the conversation that this response was associated with.

max\_output\_tokens: Optional[int]

An upper bound for the number of tokens that can be generated for a response, including visible output tokens and [reasoning tokens](https://platform.openai.com/docs/guides/reasoning).

max\_tool\_calls: Optional[int]

The maximum number of total calls to built-in tools that can be processed in a response. This maximum number applies across all built-in tool calls, not per individual tool. Any further attempts to call a tool by the model will be ignored.

moderation: Optional[Moderation]

Moderation results for the response input and output, if moderated completions were requested.

input: ModerationInput

Moderation for the response input.

class ModerationInputModerationResult: …

A moderation result produced for the response input or output.

categories: Dict[str, bool]

A dictionary of moderation categories to booleans, True if the input is flagged under this category.

category\_applied\_input\_types: Dict[str, List[Literal["text", "image"]]]

Which modalities of input are reflected by the score for each category.

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

class ModerationInputError: …

An error produced while attempting moderation for the response input or output.

code: str

The error code.

message: str

The error message.

type: Literal["error"]

The object type, which was always `error` for moderation failures.

output: ModerationOutput

Moderation for the response output.

class ModerationOutputModerationResult: …

A moderation result produced for the response input or output.

categories: Dict[str, bool]

A dictionary of moderation categories to booleans, True if the input is flagged under this category.

category\_applied\_input\_types: Dict[str, List[Literal["text", "image"]]]

Which modalities of input are reflected by the score for each category.

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

class ModerationOutputError: …

An error produced while attempting moderation for the response input or output.

code: str

The error code.

message: str

The error message.

type: Literal["error"]

The object type, which was always `error` for moderation failures.

previous\_response\_id: Optional[str]

The unique ID of the previous response to the model. Use this to
create multi-turn conversations. Learn more about
[conversation state](https://platform.openai.com/docs/guides/conversation-state). Cannot be used in conjunction with `conversation`.

prompt: Optional[BetaResponsePrompt]

Reference to a prompt template and its variables.
[Learn more](https://platform.openai.com/docs/guides/text?api-mode=responses#reusable-prompts).

id: str

The unique identifier of the prompt template to use.

variables: Optional[Dict[str, Variables]]

Optional map of values to substitute in for variables in your
prompt. The substitution values can either be strings, or other
Response input types like images or files.

str

class BetaResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

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

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class BetaResponseInputFile: …

A file input to the model.

type: Literal["input\_file"]

The type of the input item. Always `input_file`.

detail: Optional[Literal["auto", "low", "high"]]

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

"auto"

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

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

version: Optional[str]

Optional version of the prompt template.

prompt\_cache\_key: Optional[str]

Used by OpenAI to cache responses for similar requests to optimize your cache hit rates. Replaces the `user` field. [Learn more](https://platform.openai.com/docs/guides/prompt-caching).

prompt\_cache\_options: Optional[PromptCacheOptions]

The prompt-caching options that were applied to the response. Supported for `gpt-5.6` and later models.

mode: Literal["implicit", "explicit"]

Whether implicit prompt-cache breakpoints were enabled.

"implicit"

"explicit"

ttl: Literal["30m"]

The minimum lifetime applied to each cache breakpoint.

Deprecatedprompt\_cache\_retention: Optional[Literal["in\_memory", "24h"]]

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

reasoning: Optional[Reasoning]

**gpt-5 and o-series models only**

Configuration options for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).

context: Optional[Literal["auto", "current\_turn", "all\_turns"]]

Controls which reasoning items are rendered back to the model on later turns.
If omitted or set to `auto`, the model determines the context mode. The
`gpt-5.6` model family defaults to `all_turns`; earlier models default to
`current_turn`.

When returned on a response, this is the effective reasoning context mode
used for the response.

"auto"

"current\_turn"

"all\_turns"

effort: Optional[Literal["none", "minimal", "low", 4 more]]

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

Deprecatedgenerate\_summary: Optional[Literal["auto", "concise", "detailed"]]

**Deprecated:** use `summary` instead.

A summary of the reasoning performed by the model. This can be
useful for debugging and understanding the model’s reasoning process.
One of `auto`, `concise`, or `detailed`.

"auto"

"concise"

"detailed"

mode: Optional[Union[str, Literal["standard", "pro"], null]]

Controls the reasoning execution mode for the request.

When returned on a response, this is the effective execution mode.

str

Literal["standard", "pro"]

Controls the reasoning execution mode for the request.

When returned on a response, this is the effective execution mode.

"standard"

"pro"

summary: Optional[Literal["auto", "concise", "detailed"]]

A summary of the reasoning performed by the model. This can be
useful for debugging and understanding the model’s reasoning process.
One of `auto`, `concise`, or `detailed`.

`concise` is supported for `computer-use-preview` models and all reasoning models after `gpt-5`.

"auto"

"concise"

"detailed"

safety\_identifier: Optional[str]

A stable identifier used to help detect users of your application that may be violating OpenAI’s usage policies.
The IDs should be a string that uniquely identifies each user, with a maximum length of 64 characters. We recommend hashing their username or email address, in order to avoid sending us any identifying information. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).

maxLength64

service\_tier: Optional[Literal["auto", "default", "flex", 2 more]]

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

status: Optional[BetaResponseStatus]

The status of the response generation. One of `completed`, `failed`,
`in_progress`, `cancelled`, `queued`, or `incomplete`.

"completed"

"failed"

"in\_progress"

"cancelled"

"queued"

"incomplete"

text: Optional[BetaResponseTextConfig]

Configuration options for a text response from the model. Can be plain
text or structured JSON data. Learn more:

* [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
* [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

format: Optional[BetaResponseFormatTextConfig]

An object specifying the format that the model must output.

Configuring `{ "type": "json_schema" }` enables Structured Outputs,
which ensures the model will match your supplied JSON schema. Learn more in the
[Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

The default format is `{ "type": "text" }` with no additional options.

**Not recommended for gpt-4o and newer models:**

Setting to `{ "type": "json_object" }` enables the older JSON mode, which
ensures the message the model generates is valid JSON. Using `json_schema`
is preferred for models that support it.

class Text: …

Default response format. Used to generate text responses.

type: Literal["text"]

The type of response format being defined. Always `text`.

class BetaResponseFormatTextJSONSchemaConfig: …

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

name: str

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

schema: Dict[str, object]

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

type: Literal["json\_schema"]

The type of response format being defined. Always `json_schema`.

description: Optional[str]

A description of what the response format is for, used by the model to
determine how to respond in the format.

strict: Optional[bool]

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

class JSONObject: …

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type: Literal["json\_object"]

The type of response format being defined. Always `json_object`.

verbosity: Optional[Literal["low", "medium", "high"]]

Constrains the verbosity of the model’s response. Lower values will result in
more concise responses, while higher values will result in more verbose responses.
Currently supported values are `low`, `medium`, and `high`. The default is
`medium`.

"low"

"medium"

"high"

top\_logprobs: Optional[int]

An integer between 0 and 20 specifying the maximum number of most likely
tokens to return at each token position, each with an associated log
probability. In some cases, the number of returned tokens may be fewer than
requested.

minimum0

maximum20

truncation: Optional[Literal["auto", "disabled"]]

The truncation strategy to use for the model response.

* `auto`: If the input to this Response exceeds
  the model’s context window size, the model will truncate the
  response to fit the context window by dropping items from the beginning of the conversation.
* `disabled` (default): If the input size will exceed the context window
  size for a model, the request will fail with a 400 error.

"auto"

"disabled"

usage: Optional[BetaResponseUsage]

Represents token usage details including input tokens, output tokens,
a breakdown of output tokens, and the total tokens used.

input\_tokens: int

The number of input tokens.

input\_tokens\_details: InputTokensDetails

A detailed breakdown of the input tokens.

cache\_write\_tokens: int

The number of input tokens that were written to the cache.

cached\_tokens: int

The number of tokens that were retrieved from the cache.
[More on prompt caching](https://platform.openai.com/docs/guides/prompt-caching).

output\_tokens: int

The number of output tokens.

output\_tokens\_details: OutputTokensDetails

A detailed breakdown of the output tokens.

reasoning\_tokens: int

The number of reasoning tokens.

total\_tokens: int

The total number of tokens used.

Deprecateduser: Optional[str]

This field is being replaced by `safety_identifier` and `prompt_cache_key`. Use `prompt_cache_key` instead to maintain caching optimizations.
A stable identifier for your end-users.
Used to boost cache hit rates by better bucketing similar requests and to help OpenAI detect and prevent abuse. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).

sequence\_number: int

The sequence number for this event.

type: Literal["response.completed"]

The type of the event. Always `response.completed`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

The canonical name of the agent that produced this item.

class BetaResponseContentPartAddedEvent: …

Emitted when a new content part is added.

content\_index: int

The index of the content part that was added.

item\_id: str

The ID of the output item that the content part was added to.

output\_index: int

The index of the output item that the content part was added to.

part: Part

The content part that was added.

class BetaResponseOutputText: …

A text output from the model.

annotations: List[Annotation]

The annotations of the text output.

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

class BetaResponseOutputRefusal: …

A refusal from the model.

refusal: str

The refusal explanation from the model.

type: Literal["refusal"]

The type of the refusal. Always `refusal`.

class PartReasoningText: …

Reasoning text from the model.

text: str

The reasoning text from the model.

type: Literal["reasoning\_text"]

The type of the reasoning text. Always `reasoning_text`.

sequence\_number: int

The sequence number of this event.

type: Literal["response.content\_part.added"]

The type of the event. Always `response.content_part.added`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

The canonical name of the agent that produced this item.

class BetaResponseContentPartDoneEvent: …

Emitted when a content part is done.

content\_index: int

The index of the content part that is done.

item\_id: str

The ID of the output item that the content part was added to.

output\_index: int

The index of the output item that the content part was added to.

part: Part

The content part that is done.

class BetaResponseOutputText: …

A text output from the model.

annotations: List[Annotation]

The annotations of the text output.

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

class BetaResponseOutputRefusal: …

A refusal from the model.

refusal: str

The refusal explanation from the model.

type: Literal["refusal"]

The type of the refusal. Always `refusal`.

class PartReasoningText: …

Reasoning text from the model.

text: str

The reasoning text from the model.

type: Literal["reasoning\_text"]

The type of the reasoning text. Always `reasoning_text`.

sequence\_number: int

The sequence number of this event.

type: Literal["response.content\_part.done"]

The type of the event. Always `response.content_part.done`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

The canonical name of the agent that produced this item.

class BetaResponseCreatedEvent: …

An event that is emitted when a response is created.

response: [BetaResponse](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema))

The response that was created.

id: str

Unique identifier for this Response.

created\_at: float

Unix timestamp (in seconds) of when this Response was created.

formatunixtime

error: Optional[BetaResponseError]

An error object returned when the model fails to generate a Response.

code: Literal["server\_error", "rate\_limit\_exceeded", "invalid\_prompt", 17 more]

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

message: str

A human-readable description of the error.

incomplete\_details: Optional[IncompleteDetails]

Details about why the response is incomplete.

reason: Optional[Literal["max\_output\_tokens", "content\_filter"]]

The reason why the response is incomplete.

"max\_output\_tokens"

"content\_filter"

instructions: Union[str, List[[BetaResponseInputItem](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_item%20%3E%20(schema))], null]

A system (or developer) message inserted into the model’s context.

When using along with `previous_response_id`, the instructions from a previous
response will not be carried over to the next response. This makes it simple
to swap out system (or developer) messages in new responses.

str

A text input to the model, equivalent to a text input with the
`developer` role.

List[[BetaResponseInputItem](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_item%20%3E%20(schema))]

A list of one or many input items to the model, containing
different content types.

class BetaEasyInputMessage: …

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: Union[str, [BetaResponseInputMessageContentList](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_message_content_list%20%3E%20(schema))]

Text, image, or audio input to the model, used to generate a response.
Can also contain previous assistant responses.

str

A text input to the model.

List[[BetaResponseInputContent](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_content%20%3E%20(schema))]

class BetaResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

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

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class BetaResponseInputFile: …

A file input to the model.

type: Literal["input\_file"]

The type of the input item. Always `input_file`.

detail: Optional[Literal["auto", "low", "high"]]

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

"auto"

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

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

role: Literal["user", "assistant", "system", "developer"]

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

"user"

"assistant"

"system"

"developer"

phase: Optional[Literal["commentary", "final\_answer"]]

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

"commentary"

"final\_answer"

type: Optional[Literal["message"]]

The type of the message input. Always `message`.

class Message: …

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role.

content: [BetaResponseInputMessageContentList](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_message_content_list%20%3E%20(schema))

A list of one or many input items to the model, containing different content
types.

class BetaResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

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

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class BetaResponseInputFile: …

A file input to the model.

type: Literal["input\_file"]

The type of the input item. Always `input_file`.

detail: Optional[Literal["auto", "low", "high"]]

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

"auto"

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

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

role: Literal["user", "system", "developer"]

The role of the message input. One of `user`, `system`, or `developer`.

"user"

"system"

"developer"

agent: Optional[MessageAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

type: Optional[Literal["message"]]

The type of the message input. Always set to `message`.

class BetaResponseOutputMessage: …

An output message from the model.

id: str

The unique ID of the output message.

content: List[Content]

The content of the output message.

class BetaResponseOutputText: …

A text output from the model.

annotations: List[Annotation]

The annotations of the text output.

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

class BetaResponseOutputRefusal: …

A refusal from the model.

refusal: str

The refusal explanation from the model.

type: Literal["refusal"]

The type of the refusal. Always `refusal`.

role: Literal["assistant"]

The role of the output message. Always `assistant`.

status: Literal["in\_progress", "completed", "incomplete"]

The status of the message input. One of `in_progress`, `completed`, or
`incomplete`. Populated when input items are returned via API.

"in\_progress"

"completed"

"incomplete"

type: Literal["message"]

The type of the output message. Always `message`.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

phase: Optional[Literal["commentary", "final\_answer"]]

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

"commentary"

"final\_answer"

class BetaResponseFileSearchToolCall: …

The results of a file search tool call. See the
[file search guide](https://platform.openai.com/docs/guides/tools-file-search) for more information.

id: str

The unique ID of the file search tool call.

queries: List[str]

The queries used to search for files.

status: Literal["in\_progress", "searching", "completed", 2 more]

The status of the file search tool call. One of `in_progress`,
`searching`, `incomplete` or `failed`,

"in\_progress"

"searching"

"completed"

"incomplete"

"failed"

type: Literal["file\_search\_call"]

The type of the file search tool call. Always `file_search_call`.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

results: Optional[List[Result]]

The results of the file search tool call.

attributes: Optional[Dict[str, Union[str, float, bool]]]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.

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

class BetaResponseComputerToolCall: …

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

"in\_progress"

"completed"

"incomplete"

type: Literal["computer\_call"]

The type of the computer call. Always `computer_call`.

action: Optional[BetaComputerAction]

A click action.

class Click: …

A click action.

button: Literal["left", "right", "wheel", 2 more]

Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

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

actions: Optional[BetaComputerActionList]

Flattened batched actions for `computer_use`. Each action includes an
`type` discriminator and action-specific fields.

class Click: …

A click action.

button: Literal["left", "right", "wheel", 2 more]

Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

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

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class ComputerCallOutput: …

The output of a computer tool call.

call\_id: str

The ID of the computer tool call that produced the output.

maxLength64

minLength1

output: [BetaResponseComputerToolCallOutputScreenshot](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_computer_tool_call_output_screenshot%20%3E%20(schema))

A computer screenshot image used with the computer use tool.

type: Literal["computer\_screenshot"]

Specifies the event type. For a computer screenshot, this property is
always set to `computer_screenshot`.

file\_id: Optional[str]

The identifier of an uploaded file that contains the screenshot.

image\_url: Optional[str]

The URL of the screenshot image.

formaturi

type: Literal["computer\_call\_output"]

The type of the computer tool call output. Always `computer_call_output`.

id: Optional[str]

The ID of the computer tool call output.

acknowledged\_safety\_checks: Optional[List[ComputerCallOutputAcknowledgedSafetyCheck]]

The safety checks reported by the API that have been acknowledged by the developer.

id: str

The ID of the pending safety check.

code: Optional[str]

The type of the pending safety check.

message: Optional[str]

Details about the pending safety check.

agent: Optional[ComputerCallOutputAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the message input. One of `in_progress`, `completed`, or `incomplete`. Populated when input items are returned via API.

"in\_progress"

"completed"

"incomplete"

class BetaResponseFunctionWebSearch: …

The results of a web search tool call. See the
[web search guide](https://platform.openai.com/docs/guides/tools-web-search) for more information.

id: str

The unique ID of the web search tool call.

action: Action

An object describing the specific action taken in this web search call.
Includes details on how the model used the web (search, open\_page, find\_in\_page).

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

"in\_progress"

"searching"

"completed"

"failed"

type: Literal["web\_search\_call"]

The type of the web search tool call. Always `web_search_call`.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class BetaResponseFunctionToolCall: …

A tool call to run a function. See the
[function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.

arguments: str

A JSON string of the arguments to pass to the function.

call\_id: str

The unique ID of the function tool call generated by the model.

name: str

The name of the function to run.

type: Literal["function\_call"]

The type of the function tool call. Always `function_call`.

id: Optional[str]

The unique ID of the function tool call.

agent: Optional[Agent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

caller: Optional[Caller]

The execution context that produced this tool call.

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

The call ID of the program item that produced this tool call.

type: Literal["program"]

namespace: Optional[str]

The namespace of the function to run.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

class FunctionCallOutput: …

The output of a function tool call.

call\_id: str

The unique ID of the function tool call generated by the model.

maxLength64

minLength1

output: Union[str, [BetaResponseFunctionCallOutputItemList](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_call_output_item_list%20%3E%20(schema))]

Text, image, or file output of the function tool call.

str

A JSON string of the output of the function tool call.

List[[BetaResponseFunctionCallOutputItem](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_call_output_item%20%3E%20(schema))]

class BetaResponseInputTextContent: …

A text input to the model.

text: str

The text input to the model.

maxLength10485760

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class BetaResponseInputImageContent: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision)

type: Literal["input\_image"]

The type of the input item. Always `input_image`.

detail: Optional[Literal["low", "high", "auto", "original"]]

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

"low"

"high"

"auto"

"original"

file\_id: Optional[str]

The ID of the file to be sent to the model.

image\_url: Optional[str]

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

maxLength20971520

formaturi

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class BetaResponseInputFileContent: …

A file input to the model.

type: Literal["input\_file"]

The type of the input item. Always `input_file`.

detail: Optional[Literal["auto", "low", "high"]]

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

"auto"

"low"

"high"

file\_data: Optional[str]

The base64-encoded data of the file to be sent to the model.

maxLength73400320

file\_id: Optional[str]

The ID of the file to be sent to the model.

file\_url: Optional[str]

The URL of the file to be sent to the model.

formaturi

filename: Optional[str]

The name of the file to be sent to the model.

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

type: Literal["function\_call\_output"]

The type of the function tool call output. Always `function_call_output`.

id: Optional[str]

The unique ID of the function tool call output. Populated when this item is returned via API.

agent: Optional[FunctionCallOutputAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

caller: Optional[FunctionCallOutputCaller]

The execution context that produced this tool call.

class FunctionCallOutputCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class FunctionCallOutputCallerProgram: …

caller\_id: str

The call ID of the program item that produced this tool call.

maxLength64

minLength1

type: Literal["program"]

The caller type. Always `program`.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the item. One of `in_progress`, `completed`, or `incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

class AgentMessage: …

A message routed between agents.

author: str

The sending agent identity.

content: List[AgentMessageContent]

Plaintext, image, or encrypted content sent between agents.

class BetaResponseInputTextContent: …

A text input to the model.

text: str

The text input to the model.

maxLength10485760

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class BetaResponseInputImageContent: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision)

type: Literal["input\_image"]

The type of the input item. Always `input_image`.

detail: Optional[Literal["low", "high", "auto", "original"]]

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

"low"

"high"

"auto"

"original"

file\_id: Optional[str]

The ID of the file to be sent to the model.

image\_url: Optional[str]

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

maxLength20971520

formaturi

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: Literal["explicit"]

The breakpoint mode. Always `explicit`.

class AgentMessageContentEncryptedContent: …

Opaque encrypted content that Responses API decrypts inside trusted model execution.

encrypted\_content: str

Opaque encrypted content.

maxLength10485760

type: Literal["encrypted\_content"]

The type of the input item. Always `encrypted_content`.

recipient: str

The destination agent identity.

type: Literal["agent\_message"]

The item type. Always `agent_message`.

id: Optional[str]

The unique ID of this agent message item.

agent: Optional[AgentMessageAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class MultiAgentCall: …

action: Literal["spawn\_agent", "interrupt\_agent", "list\_agents", 3 more]

The multi-agent action that was executed.

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

arguments: str

The action arguments as a JSON string.

call\_id: str

The unique ID linking this call to its output.

maxLength64

minLength1

type: Literal["multi\_agent\_call"]

The item type. Always `multi_agent_call`.

id: Optional[str]

The unique ID of this multi-agent call.

agent: Optional[MultiAgentCallAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class MultiAgentCallOutput: …

action: Literal["spawn\_agent", "interrupt\_agent", "list\_agents", 3 more]

The multi-agent action that produced this result.

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

call\_id: str

The unique ID of the multi-agent call.

maxLength64

minLength1

output: List[MultiAgentCallOutputOutput]

Text output returned by the multi-agent action.

text: str

The text content.

maxLength10485760

type: Literal["output\_text"]

The content type. Always `output_text`.

annotations: Optional[List[MultiAgentCallOutputOutputAnnotation]]

Citations associated with the text content.

class MultiAgentCallOutputOutputAnnotationFileCitation: …

file\_id: str

The ID of the file.

filename: str

The filename of the file cited.

index: int

The index of the file in the list of files.

minimum0

type: Literal["file\_citation"]

The citation type. Always `file_citation`.

class MultiAgentCallOutputOutputAnnotationURLCitation: …

end\_index: int

The index of the last character of the citation in the message.

minimum0

start\_index: int

The index of the first character of the citation in the message.

minimum0

title: str

The title of the cited resource.

type: Literal["url\_citation"]

The citation type. Always `url_citation`.

url: str

The URL of the cited resource.

formaturi

class MultiAgentCallOutputOutputAnnotationContainerFileCitation: …

container\_id: str

The ID of the container.

end\_index: int

The index of the last character of the citation in the message.

minimum0

file\_id: str

The ID of the container file.

filename: str

The filename of the container file cited.

start\_index: int

The index of the first character of the citation in the message.

minimum0

type: Literal["container\_file\_citation"]

The citation type. Always `container_file_citation`.

type: Literal["multi\_agent\_call\_output"]

The item type. Always `multi_agent_call_output`.

id: Optional[str]

The unique ID of this multi-agent call output.

agent: Optional[MultiAgentCallOutputAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

class ToolSearchCall: …

arguments: object

The arguments supplied to the tool search call.

type: Literal["tool\_search\_call"]

The item type. Always `tool_search_call`.

id: Optional[str]

The unique ID of this tool search call.

agent: Optional[ToolSearchCallAgent]

The agent that produced this item.

agent\_name: str

The canonical name of the agent that produced this item.

call\_id: Optional[str]

The unique ID of the tool search call generated by the model.

maxLength64

minLength1

execution: Optional[Literal["server", "client"]]

Whether tool search was executed by the server or by the client.

"server"

"client"

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the tool search call.

"in\_progress"

"completed"

"incomplete"

class BetaResponseToolSearchOutputItemParam: …

tools: List[[BetaTool](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))]

The loaded tool definitions returned by the tool search output.

class BetaFunctionTool: …

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

name: str

The name of the function to call.

parameters: Optional[Dict[str, object]]

A JSON schema object describing the parameters of the function.

strict: Optional[bool]

Whether strict parameter validation is enforced for this function tool.

type: Literal["function"]

The type of the function tool. Always `function`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: Optional[bool]

Whether this function is deferred and loaded via tool search.

description: Optional[str]

A description of the function. Used by the model to determine whether or not to call the function.

output\_schema: Optional[Dict[str, object]]

A JSON schema object describing the JSON value encoded in string outputs for this function.

class BetaFileSearchTool: …

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

type: Literal["file\_search"]

The type of the file search tool. Always `file_search`.

vector\_store\_ids: List[str]

The IDs of the vector stores to search.

filters: Optional[Filters]

A filter to apply.

class FiltersComparisonFilter: …

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

str

float

bool

List[Union[str, float]]

str

float

class FiltersCompoundFilter: …

Combine multiple filters using `and` or `or`.

filters: List[FiltersCompoundFilterFilter]

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

class FiltersCompoundFilterFilterComparisonFilter: …

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

str

float

bool

List[Union[str, float]]

str

float

object

type: Literal["and", "or"]

Type of operation: `and` or `or`.

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

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

class BetaComputerTool: …

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

type: Literal["computer"]

The type of the computer tool. Always `computer`.

class BetaComputerUsePreviewTool: …

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

display\_height: int

The height of the computer display.

display\_width: int

The width of the computer display.

environment: Literal["windows", "mac", "linux", 2 more]

The type of computer environment to control.

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

The type of the computer use tool. Always `computer_use_preview`.

class BetaWebSearchTool: …

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

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

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

allowed\_tools: Optional[McpAllowedTools]

List of allowed tool names or a filter object.

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

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

A list of allowed domains when type is `allowlist`.

type: Literal["allowlist"]

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

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

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

class ProgrammaticToolCalling: …

type: Literal["programmatic\_tool\_calling"]

The type of the tool. Always `programmatic_tool_calling`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

The type of the image generation tool. Always `image_generation`.

action: Optional[Literal["generate", "edit", "auto"]]

Whether to generate a new image or edit an existing image. Default: `auto`.

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

"transparent"

"opaque"

"auto"

input\_fidelity: Optional[Literal["high", "low"]]

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

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

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

The image generation model to use. Default: `gpt-image-1`.

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

Moderation level for the generated image. Default: `auto`.

"auto"

"low"

output\_compression: Optional[int]

Compression level for the output image. Default: 100.

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

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

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool: …

A tool that allows the model to execute shell commands.

type: Literal["shell"]

The type of the shell tool. Always `shell`.

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

The tool invocation context(s).

"direct"

"programmatic"

environment: Optional[Environment]

class BetaContainerAuto: …

type: Literal["container\_auto"]

Automatically creates a container for this request

file\_ids: Optional[List[str]]

An optional list of uploaded files to make available to your code.

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

The memory limit for the container.

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

A list of allowed domains when type is `allowlist`.

type: Literal["allowlist"]

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

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

class BetaSkillReference: …

skill\_id: str

The ID of the referenced skill.

maxLength64

minLength1

type: Literal["skill\_reference"]

References a skill created with the /v1/skills endpoint.

version: Optional[str]

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

class BetaInlineSkill: …

description: str

The description of the skill.

name: str

The name of the skill.

source: [BetaInlineSkillSource](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

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

class BetaLocalEnvironment: …

type: Literal["local"]

Use a local computer environment.

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

An optional list of skills.

description: str

The description of the skill.

name: str

The name of the skill.

path: str

The path to the directory containing the skill.

class BetaContainerReference: …

container\_id: str

The ID of the referenced container.

type: Literal["container\_reference"]

References a container created with the /v1/containers endpoint

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str
