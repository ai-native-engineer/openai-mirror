<!-- source: https://developers.openai.com/api/reference/ruby/resources/beta/subresources/responses/subresources/input_items/methods/list/ -->

[API Reference](/api/reference/ruby)

[Beta](/api/reference/ruby/resources/beta)

[Responses](/api/reference/ruby/resources/beta/subresources/responses)

[Input Items](/api/reference/ruby/resources/beta/subresources/responses/subresources/input_items)

# List input items

beta.responses.input\_items.list(response\_id, \*\*kwargs) -> CursorPage<[BetaResponseItem](/api/reference/ruby/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_item%20%3E%20(schema))>

GET/responses/{response\_id}/input\_items

Returns a list of input items for a given response.

##### ParametersExpand Collapse

response\_id: String

after: String

An item ID to list items after, used in pagination.

include: Array[[BetaResponseIncludable](/api/reference/ruby/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_includable%20%3E%20(schema))]

Additional fields to include in the response. See the `include`
parameter for Response creation above for more information.

:"file\_search\_call.results"

:"web\_search\_call.results"

:"web\_search\_call.action.sources"

:"message.input\_image.image\_url"

:"computer\_call\_output.output.image\_url"

:"code\_interpreter\_call.outputs"

:"reasoning.encrypted\_content"

:"message.output\_text.logprobs"

limit: Integer

A limit on the number of objects to be returned. Limit can range between
1 and 100, and the default is 20.

order: :asc | :desc

The order to return the input items in. Default is `desc`.

* `asc`: Return the input items in ascending order.
* `desc`: Return the input items in descending order.

:asc

:desc

betas: Array[:"responses\_multi\_agent=v1"]

##### ReturnsExpand Collapse

BetaResponseItem = [BetaResponseInputMessageItem](/api/reference/ruby/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_message_item%20%3E%20(schema)) { id, content, role, 3 more }  | [BetaResponseOutputMessage](/api/reference/ruby/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_message%20%3E%20(schema)) { id, content, role, 4 more }  | [BetaResponseFileSearchToolCall](/api/reference/ruby/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_file_search_tool_call%20%3E%20(schema)) { id, queries, status, 3 more }  | 29 more

Content item used to generate a response.

class BetaResponseInputMessageItem { id, content, role, 3 more }

id: String

The unique ID of the message input.

content: [BetaResponseInputMessageContentList](/api/reference/ruby/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_message_content_list%20%3E%20(schema)) { , ,  }

class BetaResponseInputText { text, type, prompt\_cache\_breakpoint }

text: String

type: :input\_text

prompt\_cache\_breakpoint: PromptCacheBreakpoint{ mode}

mode: :explicit

class BetaResponseInputImage { detail, type, file\_id, 2 more }

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: :low | :high | :auto | :original

:low

:high

:auto

:original

type: :input\_image

file\_id: String

image\_url: String

prompt\_cache\_breakpoint: PromptCacheBreakpoint{ mode}

mode: :explicit

class BetaResponseInputFile { type, detail, file\_data, 4 more }

type: :input\_file

detail: :auto | :low | :high

:auto

:low

:high

file\_data: String

file\_id: String

file\_url: String

filename: String

prompt\_cache\_breakpoint: PromptCacheBreakpoint{ mode}

mode: :explicit

role: :user | :system | :developer

:user

:system

:developer

type: :message

agent: Agent{ agent\_name}

agent\_name: String

status: :in\_progress | :completed | :incomplete

:in\_progress

:completed

:incomplete

class BetaResponseOutputMessage { id, content, role, 4 more }

id: String

content: Array[[BetaResponseOutputText](/api/reference/ruby/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_text%20%3E%20(schema)) { annotations, text, type, logprobs }  | [BetaResponseOutputRefusal](/api/reference/ruby/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_refusal%20%3E%20(schema)) { refusal, type } ]

class BetaResponseOutputText { annotations, text, type, logprobs }

annotations: Array[FileCitation{ file\_id, filename, index, type} | URLCitation{ end\_index, start\_index, title, 2 more} | ContainerFileCitation{ container\_id, end\_index, file\_id, 3 more} | FilePath{ file\_id, index, type}]

class FileCitation { file\_id, filename, index, type }

file\_id: String

filename: String

index: Integer

type: :file\_citation

class URLCitation { end\_index, start\_index, title, 2 more }

end\_index: Integer

start\_index: Integer

title: String

type: :url\_citation

url: String

class ContainerFileCitation { container\_id, end\_index, file\_id, 3 more }

container\_id: String

end\_index: Integer

file\_id: String

filename: String

start\_index: Integer

type: :container\_file\_citation

class FilePath { file\_id, index, type }

file\_id: String

index: Integer

type: :file\_path

text: String

type: :output\_text

logprobs: Array[Logprob{ token, bytes, logprob, top\_logprobs}]

token: String

bytes: Array[Integer]

logprob: Float

top\_logprobs: Array[TopLogprob{ token, bytes, logprob}]

token: String

bytes: Array[Integer]

logprob: Float

class BetaResponseOutputRefusal { refusal, type }

refusal: String

type: :refusal

role: :assistant

status: :in\_progress | :completed | :incomplete

:in\_progress

:completed

:incomplete

type: :message

agent: Agent{ agent\_name}

agent\_name: String

phase: :commentary | :final\_answer

:commentary

:final\_answer

class BetaResponseFileSearchToolCall { id, queries, status, 3 more }

[file search guide](https://platform.openai.com/docs/guides/tools-file-search) for more information.

id: String

queries: Array[String]

status: :in\_progress | :searching | :completed | 2 more

:in\_progress

:searching

:completed

:incomplete

:failed

type: :file\_search\_call

agent: Agent{ agent\_name}

agent\_name: String

results: Array[Result{ attributes, file\_id, filename, 2 more}]

attributes: Hash[Symbol, String | Float | bool]

String = String

Float = Float

UnionMember2 = bool

file\_id: String

filename: String

score: Float

formatfloat

text: String

class BetaResponseComputerToolCall { id, call\_id, pending\_safety\_checks, 5 more }

[computer use guide](https://platform.openai.com/docs/guides/tools-computer-use) for more information.

id: String

call\_id: String

pending\_safety\_checks: Array[PendingSafetyCheck{ id, code, message}]

id: String

code: String

message: String

status: :in\_progress | :completed | :incomplete

:in\_progress

:completed

:incomplete

type: :computer\_call

action: [BetaComputerAction](/api/reference/ruby/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_computer_action%20%3E%20(schema))

class Click { button, type, x, 2 more }

button: :left | :right | :wheel | 2 more

Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

:left

:right

:wheel

:back

:forward

type: :click

Specifies the event type. For a click action, this property is always `click`.

x: Integer

The x-coordinate where the click occurred.

y\_: Integer

The y-coordinate where the click occurred.

keys: Array[String]

The keys being held while clicking.

class DoubleClick { keys, type, x, y\_ }

A double click action.

keys: Array[String]

The keys being held while double-clicking.

type: :double\_click

Specifies the event type. For a double click action, this property is always set to `double_click`.

x: Integer

The x-coordinate where the double click occurred.

y\_: Integer

The y-coordinate where the double click occurred.

class Drag { path, type, keys }

A drag action.

path: Array[Path{ x, y\_}]

An array of coordinates representing the path of the drag action. Coordinates will appear as an array of objects, eg

  { x: 100, y: 200 },
  { x: 200, y: 300 }

x: Integer

The x-coordinate.

y\_: Integer

The y-coordinate.

type: :drag

Specifies the event type. For a drag action, this property is always set to `drag`.

keys: Array[String]

The keys being held while dragging the mouse.

class Keypress { keys, type }

A collection of keypresses the model would like to perform.

keys: Array[String]

The combination of keys the model is requesting to be pressed. This is an array of strings, each representing a key.

type: :keypress

Specifies the event type. For a keypress action, this property is always set to `keypress`.

class Move { type, x, y\_, keys }

A mouse move action.

type: :move

Specifies the event type. For a move action, this property is always set to `move`.

x: Integer

The x-coordinate to move to.

y\_: Integer

The y-coordinate to move to.

keys: Array[String]

The keys being held while moving the mouse.

class Screenshot { type }

A screenshot action.

type: :screenshot

Specifies the event type. For a screenshot action, this property is always set to `screenshot`.

class Scroll { scroll\_x, scroll\_y, type, 3 more }

A scroll action.

scroll\_x: Integer

The horizontal scroll distance.

scroll\_y: Integer

The vertical scroll distance.

type: :scroll

Specifies the event type. For a scroll action, this property is always set to `scroll`.

x: Integer

The x-coordinate where the scroll occurred.

y\_: Integer

The y-coordinate where the scroll occurred.

keys: Array[String]

The keys being held while scrolling.

class Type { text, type }

An action to type in text.

text: String

The text to type.

type: :type

Specifies the event type. For a type action, this property is always set to `type`.

class Wait { type }

A wait action.

type: :wait

Specifies the event type. For a wait action, this property is always set to `wait`.

actions: [BetaComputerActionList](/api/reference/ruby/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_computer_action_list%20%3E%20(schema)) { Click, DoubleClick, Drag, 6 more }

class Click { button, type, x, 2 more }

button: :left | :right | :wheel | 2 more

Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

:left

:right

:wheel

:back

:forward

type: :click

Specifies the event type. For a click action, this property is always `click`.

x: Integer

The x-coordinate where the click occurred.

y\_: Integer

The y-coordinate where the click occurred.

keys: Array[String]

The keys being held while clicking.

class DoubleClick { keys, type, x, y\_ }

A double click action.

keys: Array[String]

The keys being held while double-clicking.

type: :double\_click

Specifies the event type. For a double click action, this property is always set to `double_click`.

x: Integer

The x-coordinate where the double click occurred.

y\_: Integer

The y-coordinate where the double click occurred.

class Drag { path, type, keys }

A drag action.

path: Array[Path{ x, y\_}]

An array of coordinates representing the path of the drag action. Coordinates will appear as an array of objects, eg

  { x: 100, y: 200 },
  { x: 200, y: 300 }

x: Integer

The x-coordinate.

y\_: Integer

The y-coordinate.

type: :drag

Specifies the event type. For a drag action, this property is always set to `drag`.

keys: Array[String]

The keys being held while dragging the mouse.

class Keypress { keys, type }

A collection of keypresses the model would like to perform.

keys: Array[String]

The combination of keys the model is requesting to be pressed. This is an array of strings, each representing a key.

type: :keypress

Specifies the event type. For a keypress action, this property is always set to `keypress`.

class Move { type, x, y\_, keys }

A mouse move action.

type: :move

Specifies the event type. For a move action, this property is always set to `move`.

x: Integer

The x-coordinate to move to.

y\_: Integer

The y-coordinate to move to.

keys: Array[String]

The keys being held while moving the mouse.

class Screenshot { type }

A screenshot action.

type: :screenshot

Specifies the event type. For a screenshot action, this property is always set to `screenshot`.

class Scroll { scroll\_x, scroll\_y, type, 3 more }

A scroll action.

scroll\_x: Integer

The horizontal scroll distance.

scroll\_y: Integer

The vertical scroll distance.

type: :scroll

Specifies the event type. For a scroll action, this property is always set to `scroll`.

x: Integer

The x-coordinate where the scroll occurred.

y\_: Integer

The y-coordinate where the scroll occurred.

keys: Array[String]

The keys being held while scrolling.

class Type { text, type }

An action to type in text.

text: String

The text to type.

type: :type

Specifies the event type. For a type action, this property is always set to `type`.

class Wait { type }

A wait action.

type: :wait

Specifies the event type. For a wait action, this property is always set to `wait`.

agent: Agent{ agent\_name}

agent\_name: String

class BetaResponseComputerToolCallOutputItem { id, call\_id, output, 5 more }

id: String

The unique ID of the computer call tool output.

call\_id: String

output: [BetaResponseComputerToolCallOutputScreenshot](/api/reference/ruby/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_computer_tool_call_output_screenshot%20%3E%20(schema)) { type, file\_id, image\_url }

type: :computer\_screenshot

Specifies the event type. For a computer screenshot, this property is
always set to `computer_screenshot`.

file\_id: String

image\_url: String

status: :completed | :incomplete | :failed | :in\_progress

:completed

:incomplete

:failed

:in\_progress

type: :computer\_call\_output

acknowledged\_safety\_checks: Array[AcknowledgedSafetyCheck{ id, code, message}]

The safety checks reported by the API that have been acknowledged by the
developer.

id: String

code: String

message: String

agent: Agent{ agent\_name}

agent\_name: String

created\_by: String

The identifier of the actor that created the item.

class BetaResponseFunctionWebSearch { id, action, status, 2 more }

[web search guide](https://platform.openai.com/docs/guides/tools-web-search) for more information.

id: String

action: Search{ type, queries, query, sources} | OpenPage{ type, url} | FindInPage{ pattern, type, url}

class Search { type, queries, query, sources }

type: :search

queries: Array[String]

Deprecatedquery: String

sources: Array[Source{ type, url}]

type: :url

url: String

class OpenPage { type, url }

type: :open\_page

url: String

class FindInPage { pattern, type, url }

pattern: String

type: :find\_in\_page

url: String

status: :in\_progress | :searching | :completed | :failed

:in\_progress

:searching

:completed

:failed

type: :web\_search\_call

agent: Agent{ agent\_name}

agent\_name: String

class BetaResponseFunctionToolCallItem { id, status, created\_by }

[function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.

id: String

status: :in\_progress | :completed | :incomplete

:in\_progress

:completed

:incomplete

created\_by: String

The identifier of the actor that created the item.

class BetaResponseFunctionToolCallOutputItem { id, call\_id, output, 5 more }

id: String

The unique ID of the function call tool output.

call\_id: String

output: String | Array[[BetaResponseInputText](/api/reference/ruby/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_text%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  | [BetaResponseInputImage](/api/reference/ruby/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_image%20%3E%20(schema)) { detail, type, file\_id, 2 more }  | [BetaResponseInputFile](/api/reference/ruby/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_file%20%3E%20(schema)) { type, detail, file\_data, 4 more } ]

The output from the function call generated by your code.

String = String

A string of the output of the function call.

OutputContentList = Array[[BetaResponseInputText](/api/reference/ruby/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_text%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  | [BetaResponseInputImage](/api/reference/ruby/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_image%20%3E%20(schema)) { detail, type, file\_id, 2 more }  | [BetaResponseInputFile](/api/reference/ruby/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_file%20%3E%20(schema)) { type, detail, file\_data, 4 more } ]

Text, image, or file output of the function call.

class BetaResponseInputText { text, type, prompt\_cache\_breakpoint }

text: String

type: :input\_text

prompt\_cache\_breakpoint: PromptCacheBreakpoint{ mode}

mode: :explicit

class BetaResponseInputImage { detail, type, file\_id, 2 more }

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: :low | :high | :auto | :original

:low

:high

:auto

:original

type: :input\_image

file\_id: String

image\_url: String

prompt\_cache\_breakpoint: PromptCacheBreakpoint{ mode}

mode: :explicit

class BetaResponseInputFile { type, detail, file\_data, 4 more }

type: :input\_file

detail: :auto | :low | :high

:auto

:low

:high

file\_data: String

file\_id: String

file\_url: String

filename: String

prompt\_cache\_breakpoint: PromptCacheBreakpoint{ mode}

mode: :explicit

status: :in\_progress | :completed | :incomplete

:in\_progress

:completed

:incomplete

type: :function\_call\_output

agent: Agent{ agent\_name}

agent\_name: String

caller\_: Direct{ type} | Program{ caller\_id, type}

class Direct { type }

type: :direct

The caller type. Always `direct`.

class Program { caller\_id, type }

caller\_id: String

maxLength64

minLength1

type: :program

created\_by: String

The identifier of the actor that created the item.

class AgentMessage { id, author, content, 3 more }

id: String

The unique ID of the agent message.

author: String

content: Array[[BetaResponseInputText](/api/reference/ruby/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_text%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  | [BetaResponseOutputText](/api/reference/ruby/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_text%20%3E%20(schema)) { annotations, text, type, logprobs }  | Text{ text, type} | 7 more]

Encrypted content sent between agents.

class BetaResponseInputText { text, type, prompt\_cache\_breakpoint }

text: String

type: :input\_text

prompt\_cache\_breakpoint: PromptCacheBreakpoint{ mode}

mode: :explicit

class BetaResponseOutputText { annotations, text, type, logprobs }

annotations: Array[FileCitation{ file\_id, filename, index, type} | URLCitation{ end\_index, start\_index, title, 2 more} | ContainerFileCitation{ container\_id, end\_index, file\_id, 3 more} | FilePath{ file\_id, index, type}]

class FileCitation { file\_id, filename, index, type }

file\_id: String

filename: String

index: Integer

type: :file\_citation

class URLCitation { end\_index, start\_index, title, 2 more }

end\_index: Integer

start\_index: Integer

title: String

type: :url\_citation

url: String

class ContainerFileCitation { container\_id, end\_index, file\_id, 3 more }

container\_id: String

end\_index: Integer

file\_id: String

filename: String

start\_index: Integer

type: :container\_file\_citation

class FilePath { file\_id, index, type }

file\_id: String

index: Integer

type: :file\_path

text: String

type: :output\_text

logprobs: Array[Logprob{ token, bytes, logprob, top\_logprobs}]

token: String

bytes: Array[Integer]

logprob: Float

top\_logprobs: Array[TopLogprob{ token, bytes, logprob}]

token: String

bytes: Array[Integer]

logprob: Float

class Text { text, type }

A text content.

text: String

type: :text

class SummaryText { text, type }

A summary text from the model.

text: String

type: :summary\_text

class ReasoningText { text, type }

text: String

type: :reasoning\_text

class BetaResponseOutputRefusal { refusal, type }

refusal: String

type: :refusal

class BetaResponseInputImage { detail, type, file\_id, 2 more }

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: :low | :high | :auto | :original

:low

:high

:auto

:original

type: :input\_image

file\_id: String

image\_url: String

prompt\_cache\_breakpoint: PromptCacheBreakpoint{ mode}

mode: :explicit

class ComputerScreenshot { detail, file\_id, image\_url, 2 more }

A screenshot of a computer.

detail: :low | :high | :auto | :original

The detail level of the screenshot image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

:low

:high

:auto

:original

file\_id: String

image\_url: String

type: :computer\_screenshot

Specifies the event type. For a computer screenshot, this property is always set to `computer_screenshot`.

prompt\_cache\_breakpoint: PromptCacheBreakpoint{ mode}

mode: :explicit

class BetaResponseInputFile { type, detail, file\_data, 4 more }

type: :input\_file

detail: :auto | :low | :high

:auto

:low

:high

file\_data: String

file\_id: String

file\_url: String

filename: String

prompt\_cache\_breakpoint: PromptCacheBreakpoint{ mode}

mode: :explicit

class EncryptedContent { encrypted\_content, type }

encrypted\_content: String

type: :encrypted\_content

recipient: String

type: :agent\_message

The type of the item. Always `agent_message`.

agent: Agent{ agent\_name}

agent\_name: String

class MultiAgentCall { id, action, arguments, 3 more }

id: String

The unique ID of the multi-agent call item.

action: :spawn\_agent | :interrupt\_agent | :list\_agents | 3 more

The multi-agent action to execute.

:spawn\_agent

:interrupt\_agent

:list\_agents

:send\_message

:followup\_task

:wait\_agent

arguments: String

The JSON string of arguments generated for the action.

call\_id: String

type: :multi\_agent\_call

The type of the multi-agent call. Always `multi_agent_call`.

agent: Agent{ agent\_name}

agent\_name: String

class MultiAgentCallOutput { id, action, call\_id, 3 more }

id: String

The unique ID of the multi-agent call output item.

action: :spawn\_agent | :interrupt\_agent | :list\_agents | 3 more

:spawn\_agent

:interrupt\_agent

:list\_agents

:send\_message

:followup\_task

:wait\_agent

call\_id: String

output: Array[[BetaResponseOutputText](/api/reference/ruby/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_text%20%3E%20(schema)) { annotations, text, type, logprobs } ]

annotations: Array[FileCitation{ file\_id, filename, index, type} | URLCitation{ end\_index, start\_index, title, 2 more} | ContainerFileCitation{ container\_id, end\_index, file\_id, 3 more} | FilePath{ file\_id, index, type}]

class FileCitation { file\_id, filename, index, type }

file\_id: String

filename: String

index: Integer

type: :file\_citation

class URLCitation { end\_index, start\_index, title, 2 more }

end\_index: Integer

start\_index: Integer

title: String

type: :url\_citation

url: String

class ContainerFileCitation { container\_id, end\_index, file\_id, 3 more }

container\_id: String

end\_index: Integer

file\_id: String

filename: String

start\_index: Integer

type: :container\_file\_citation

class FilePath { file\_id, index, type }

file\_id: String

index: Integer

type: :file\_path

text: String

type: :output\_text

logprobs: Array[Logprob{ token, bytes, logprob, top\_logprobs}]

token: String

bytes: Array[Integer]

logprob: Float

top\_logprobs: Array[TopLogprob{ token, bytes, logprob}]

token: String

bytes: Array[Integer]

logprob: Float

type: :multi\_agent\_call\_output

The type of the multi-agent result. Always `multi_agent_call_output`.

agent: Agent{ agent\_name}

agent\_name: String

class BetaResponseToolSearchCall { id, arguments, call\_id, 5 more }

id: String

The unique ID of the tool search call item.

arguments: untyped

Arguments used for the tool search call.

call\_id: String

execution: :server | :client

:server

:client

status: :in\_progress | :completed | :incomplete

The status of the tool search call item that was recorded.

:in\_progress

:completed

:incomplete

type: :tool\_search\_call

The type of the item. Always `tool_search_call`.

agent: Agent{ agent\_name}

agent\_name: String

created\_by: String

The identifier of the actor that created the item.

class BetaResponseToolSearchOutputItem { id, call\_id, execution, 5 more }

id: String

The unique ID of the tool search output item.

call\_id: String

execution: :server | :client

:server

:client

status: :in\_progress | :completed | :incomplete

The status of the tool search output item that was recorded.

:in\_progress

:completed

:incomplete

tools: Array[[BetaTool](/api/reference/ruby/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))]

The loaded tool definitions returned by tool search.

class BetaFunctionTool { name, parameters, strict, 5 more }

name: String

parameters: Hash[Symbol, untyped]

strict: bool

type: :function

allowed\_callers: Array[:direct | :programmatic]

:direct

:programmatic

defer\_loading: bool

description: String

output\_schema: Hash[Symbol, untyped]

class BetaFileSearchTool { type, vector\_store\_ids, filters, 2 more }

type: :file\_search

vector\_store\_ids: Array[String]

filters: ComparisonFilter{ key, type, value} | CompoundFilter{ filters, type}

class ComparisonFilter { key, type, value }

key: String

type: :eq | :ne | :gt | 5 more

:eq

:ne

:gt

:gte

:lt

:lte

:in

:nin

value: String | Float | bool | Array[String | Float]

String = String

Float = Float

UnionMember2 = bool

UnionMember3 = Array[String | Float]

String = String

Float = Float

class CompoundFilter { filters, type }

filters: Array[ComparisonFilter{ key, type, value} | untyped]

class ComparisonFilter { key, type, value }

key: String

type: :eq | :ne | :gt | 5 more

:eq

:ne

:gt

:gte

:lt

:lte

:in

:nin

value: String | Float | bool | Array[String | Float]

String = String

Float = Float

UnionMember2 = bool

UnionMember3 = Array[String | Float]

String = String

Float = Float

UnionMember1 = untyped

type: :and | :or

:and

:or

max\_num\_results: Integer

ranking\_options: RankingOptions{ hybrid\_search, ranker, score\_threshold}

hybrid\_search: HybridSearch{ embedding\_weight, text\_weight}

embedding\_weight: Float

text\_weight: Float

ranker: :auto | :"default-2024-11-15"

:auto

:"default-2024-11-15"

score\_threshold: Float

class BetaComputerTool { type }

type: :computer

class BetaComputerUsePreviewTool { display\_height, display\_width, environment, type }

display\_height: Integer

display\_width: Integer

environment: :windows | :mac | :linux | 2 more

:windows

:mac

:linux

:ubuntu

:browser

type: :computer\_use\_preview

class BetaWebSearchTool { type, filters, search\_context\_size, user\_location }

[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: :web\_search | :web\_search\_2025\_08\_26

:web\_search

:web\_search\_2025\_08\_26

filters: Filters{ allowed\_domains}

allowed\_domains: Array[String]

search\_context\_size: :low | :medium | :high

:low

:medium

:high

user\_location: UserLocation{ city, country, region, 2 more}

city: String

country: String

region: String

timezone: String

type: :approximate

class Mcp { server\_label, type, allowed\_callers, 9 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: String

type: :mcp

allowed\_callers: Array[:direct | :programmatic]

:direct

:programmatic

allowed\_tools: Array[String] | McpToolFilter{ read\_only, tool\_names}

McpAllowedTools = Array[String]

A string array of allowed tool names

class McpToolFilter { read\_only, tool\_names }

read\_only: bool

tool\_names: Array[String]

authorization: String

connector\_id: :connector\_dropbox | :connector\_gmail | :connector\_googlecalendar | 5 more

about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

:connector\_dropbox

:connector\_gmail

:connector\_googlecalendar

:connector\_googledrive

:connector\_microsoftteams

:connector\_outlookcalendar

:connector\_outlookemail

:connector\_sharepoint

defer\_loading: bool

headers: Hash[Symbol, String]

require\_approval: McpToolApprovalFilter{ always, never} | :always | :never

class McpToolApprovalFilter { always, never }

always: Always{ read\_only, tool\_names}

read\_only: bool

tool\_names: Array[String]

never: Never{ read\_only, tool\_names}

read\_only: bool

tool\_names: Array[String]

McpToolApprovalSetting = :always | :never

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

:always

:never

server\_description: String

server\_url: String

tunnel\_id: String

class CodeInterpreter { container, type, allowed\_callers }

A tool that runs Python code to help generate a response to a prompt.

container: String | CodeInterpreterToolAuto{ type, file\_ids, memory\_limit, network\_policy}

String = String

The container ID.

class CodeInterpreterToolAuto { type, file\_ids, memory\_limit, network\_policy }

type: :auto

file\_ids: Array[String]

memory\_limit: :"1g" | :"4g" | :"16g" | :"64g"

:"1g"

:"4g"

:"16g"

:"64g"

network\_policy: [BetaContainerNetworkPolicyDisabled](/api/reference/ruby/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  | [BetaContainerNetworkPolicyAllowlist](/api/reference/ruby/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

class BetaContainerNetworkPolicyDisabled { type }

type: :disabled

class BetaContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array[String]

type: :allowlist

domain\_secrets: Array[[BetaContainerNetworkPolicyDomainSecret](/api/reference/ruby/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } ]

domain: String

minLength1

name: String

minLength1

value: String

maxLength10485760

minLength1

type: :code\_interpreter

allowed\_callers: Array[:direct | :programmatic]

:direct

:programmatic

class ProgrammaticToolCalling { type }

type: :programmatic\_tool\_calling

The type of the tool. Always `programmatic_tool_calling`.

class ImageGeneration { type, action, background, 9 more }

A tool that generates images using the GPT image models.

type: :image\_generation

action: :generate | :edit | :auto

:generate

:edit

:auto

background: :transparent | :opaque | :auto

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

:transparent

:opaque

:auto

input\_fidelity: :high | :low

:high

:low

input\_image\_mask: InputImageMask{ file\_id, image\_url}

file\_id: String

image\_url: String

model: String | :"gpt-image-1" | :"gpt-image-1-mini" | :"gpt-image-2" | 3 more

String = String

Model = :"gpt-image-1" | :"gpt-image-1-mini" | :"gpt-image-2" | 3 more

:"gpt-image-1"

:"gpt-image-1-mini"

:"gpt-image-2"

:"gpt-image-2-2026-04-21"

:"gpt-image-1.5"

:"chatgpt-image-latest"

moderation: :auto | :low

:auto

:low

output\_compression: Integer

minimum0

maximum100

output\_format: :png | :webp | :jpeg

:png

:webp

:jpeg

partial\_images: Integer

minimum0

maximum3

quality: :low | :medium | :high | :auto

:low

:medium

:high

:auto

size: String | :"1024x1024" | :"1024x1536" | :"1536x1024" | :auto

String = String

Size = :"1024x1024" | :"1024x1536" | :"1536x1024" | :auto

:"1024x1024"

:"1024x1536"

:"1536x1024"

:auto

class LocalShell { type }

A tool that allows the model to execute shell commands in a local environment.

type: :local\_shell

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool { type, allowed\_callers, environment }

type: :shell

allowed\_callers: Array[:direct | :programmatic]

:direct

:programmatic

environment: [BetaContainerAuto](/api/reference/ruby/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_auto%20%3E%20(schema)) { type, file\_ids, memory\_limit, 2 more }  | [BetaLocalEnvironment](/api/reference/ruby/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_environment%20%3E%20(schema)) { type, skills }  | [BetaContainerReference](/api/reference/ruby/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_reference%20%3E%20(schema)) { container\_id, type }

class BetaContainerAuto { type, file\_ids, memory\_limit, 2 more }

type: :container\_auto

file\_ids: Array[String]

memory\_limit: :"1g" | :"4g" | :"16g" | :"64g"

:"1g"

:"4g"

:"16g"

:"64g"

network\_policy: [BetaContainerNetworkPolicyDisabled](/api/reference/ruby/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  | [BetaContainerNetworkPolicyAllowlist](/api/reference/ruby/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

class BetaContainerNetworkPolicyDisabled { type }

type: :disabled

class BetaContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array[String]

type: :allowlist

domain\_secrets: Array[[BetaContainerNetworkPolicyDomainSecret](/api/reference/ruby/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } ]

domain: String

minLength1

name: String

minLength1

value: String

maxLength10485760

minLength1

skills: Array[[BetaSkillReference](/api/reference/ruby/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_skill_reference%20%3E%20(schema)) { skill\_id, type, version }  | [BetaInlineSkill](/api/reference/ruby/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill%20%3E%20(schema)) { description, name, source, type } ]

class BetaSkillReference { skill\_id, type, version }

skill\_id: String

maxLength64

minLength1

type: :skill\_reference

version: String

class BetaInlineSkill { description, name, source, type }

description: String

name: String

source: [BetaInlineSkillSource](/api/reference/ruby/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema)) { data, media\_type, type }

data: String

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

media\_type: :"application/zip"

The media type of the inline skill payload. Must be `application/zip`.

type: :base64

The type of the inline skill source. Must be `base64`.

type: :inline

class BetaLocalEnvironment { type, skills }

type: :local

skills: Array[[BetaLocalSkill](/api/reference/ruby/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema)) { description, name, path } ]

description: String

name: String

path: String

class BetaContainerReference { container\_id, type }

container\_id: String

type: :container\_reference

class BetaCustomTool { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: String

type: :custom

allowed\_callers: Array[:direct | :programmatic]

:direct

:programmatic

defer\_loading: bool

description: String

format\_: Text{ type} | Grammar{ definition, syntax, type}

class Text { type }

Unconstrained free-form text.

type: :text

Unconstrained text format. Always `text`.

class Grammar { definition, syntax, type }

definition: String

syntax: :lark | :regex

:lark

:regex

type: :grammar

class BetaNamespaceTool { description, name, tools, type }

description: String

minLength1

name: String

minLength1

tools: Array[Function{ name, type, allowed\_callers, 5 more} | [BetaCustomTool](/api/reference/ruby/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_custom_tool%20%3E%20(schema)) { name, type, allowed\_callers, 3 more } ]

class Function { name, type, allowed\_callers, 5 more }

name: String

maxLength128

minLength1

type: :function

allowed\_callers: Array[:direct | :programmatic]

:direct

:programmatic

defer\_loading: bool

description: String

output\_schema: Hash[Symbol, untyped]

parameters: untyped

strict: bool

class BetaCustomTool { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: String

type: :custom

allowed\_callers: Array[:direct | :programmatic]

:direct

:programmatic

defer\_loading: bool

description: String

format\_: Text{ type} | Grammar{ definition, syntax, type}

class Text { type }

Unconstrained free-form text.

type: :text

Unconstrained text format. Always `text`.

class Grammar { definition, syntax, type }

definition: String

syntax: :lark | :regex

:lark

:regex

type: :grammar

type: :namespace

class BetaToolSearchTool { type, description, execution, parameters }

type: :tool\_search

description: String

execution: :server | :client

:server

:client

parameters: untyped

class BetaWebSearchPreviewTool { type, search\_content\_types, search\_context\_size, user\_location }

type: :web\_search\_preview | :web\_search\_preview\_2025\_03\_11

:web\_search\_preview

:web\_search\_preview\_2025\_03\_11

search\_content\_types: Array[:text | :image]

:text

:image

search\_context\_size: :low | :medium | :high

:low

:medium

:high

user\_location: UserLocation{ type, city, country, 2 more}

type: :approximate

city: String

country: String

region: String

timezone: String

class BetaApplyPatchTool { type, allowed\_callers }

type: :apply\_patch

allowed\_callers: Array[:direct | :programmatic]

:direct

:programmatic

type: :tool\_search\_output

The type of the item. Always `tool_search_output`.

agent: Agent{ agent\_name}

agent\_name: String

created\_by: String

The identifier of the actor that created the item.

class AdditionalTools { id, role, tools, 2 more }

id: String

The unique ID of the additional tools item.

role: :unknown | :user | :assistant | 5 more

The role that provided the additional tools.

:unknown

:user

:assistant

:system

:critic

:discriminator

:developer

:tool

tools: Array[[BetaTool](/api/reference/ruby/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))]

The additional tool definitions made available at this item.

class BetaFunctionTool { name, parameters, strict, 5 more }

name: String

parameters: Hash[Symbol, untyped]

strict: bool

type: :function

allowed\_callers: Array[:direct | :programmatic]

:direct

:programmatic

defer\_loading: bool

description: String

output\_schema: Hash[Symbol, untyped]

class BetaFileSearchTool { type, vector\_store\_ids, filters, 2 more }

type: :file\_search

vector\_store\_ids: Array[String]

filters: ComparisonFilter{ key, type, value} | CompoundFilter{ filters, type}

class ComparisonFilter { key, type, value }

key: String

type: :eq | :ne | :gt | 5 more

:eq

:ne

:gt

:gte

:lt

:lte

:in

:nin

value: String | Float | bool | Array[String | Float]

String = String

Float = Float

UnionMember2 = bool

UnionMember3 = Array[String | Float]

String = String

Float = Float

class CompoundFilter { filters, type }

filters: Array[ComparisonFilter{ key, type, value} | untyped]

class ComparisonFilter { key, type, value }

key: String

type: :eq | :ne | :gt | 5 more

:eq

:ne

:gt

:gte

:lt

:lte

:in

:nin

value: String | Float | bool | Array[String | Float]

String = String

Float = Float

UnionMember2 = bool

UnionMember3 = Array[String | Float]

String = String

Float = Float

UnionMember1 = untyped

type: :and | :or

:and

:or

max\_num\_results: Integer

ranking\_options: RankingOptions{ hybrid\_search, ranker, score\_threshold}

hybrid\_search: HybridSearch{ embedding\_weight, text\_weight}

embedding\_weight: Float

text\_weight: Float

ranker: :auto | :"default-2024-11-15"

:auto

:"default-2024-11-15"

score\_threshold: Float

class BetaComputerTool { type }

type: :computer

class BetaComputerUsePreviewTool { display\_height, display\_width, environment, type }

display\_height: Integer

display\_width: Integer

environment: :windows | :mac | :linux | 2 more

:windows

:mac

:linux

:ubuntu

:browser

type: :computer\_use\_preview

class BetaWebSearchTool { type, filters, search\_context\_size, user\_location }

[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: :web\_search | :web\_search\_2025\_08\_26

:web\_search

:web\_search\_2025\_08\_26

filters: Filters{ allowed\_domains}

allowed\_domains: Array[String]

search\_context\_size: :low | :medium | :high

:low

:medium

:high

user\_location: UserLocation{ city, country, region, 2 more}

city: String

country: String

region: String

timezone: String

type: :approximate

class Mcp { server\_label, type, allowed\_callers, 9 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: String

type: :mcp

allowed\_callers: Array[:direct | :programmatic]

:direct

:programmatic

allowed\_tools: Array[String] | McpToolFilter{ read\_only, tool\_names}

McpAllowedTools = Array[String]

A string array of allowed tool names

class McpToolFilter { read\_only, tool\_names }

read\_only: bool

tool\_names: Array[String]

authorization: String

connector\_id: :connector\_dropbox | :connector\_gmail | :connector\_googlecalendar | 5 more

about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

:connector\_dropbox

:connector\_gmail

:connector\_googlecalendar

:connector\_googledrive

:connector\_microsoftteams

:connector\_outlookcalendar

:connector\_outlookemail

:connector\_sharepoint

defer\_loading: bool

headers: Hash[Symbol, String]

require\_approval: McpToolApprovalFilter{ always, never} | :always | :never

class McpToolApprovalFilter { always, never }

always: Always{ read\_only, tool\_names}

read\_only: bool

tool\_names: Array[String]

never: Never{ read\_only, tool\_names}

read\_only: bool

tool\_names: Array[String]

McpToolApprovalSetting = :always | :never

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

:always

:never

server\_description: String

server\_url: String

tunnel\_id: String

class CodeInterpreter { container, type, allowed\_callers }

A tool that runs Python code to help generate a response to a prompt.

container: String | CodeInterpreterToolAuto{ type, file\_ids, memory\_limit, network\_policy}

String = String

The container ID.

class CodeInterpreterToolAuto { type, file\_ids, memory\_limit, network\_policy }

type: :auto

file\_ids: Array[String]

memory\_limit: :"1g" | :"4g" | :"16g" | :"64g"

:"1g"

:"4g"

:"16g"

:"64g"

network\_policy: [BetaContainerNetworkPolicyDisabled](/api/reference/ruby/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  | [BetaContainerNetworkPolicyAllowlist](/api/reference/ruby/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

class BetaContainerNetworkPolicyDisabled { type }

type: :disabled

class BetaContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array[String]

type: :allowlist

domain\_secrets: Array[[BetaContainerNetworkPolicyDomainSecret](/api/reference/ruby/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } ]

domain: String

minLength1

name: String

minLength1

value: String

maxLength10485760

minLength1

type: :code\_interpreter

allowed\_callers: Array[:direct | :programmatic]

:direct

:programmatic

class ProgrammaticToolCalling { type }

type: :programmatic\_tool\_calling

The type of the tool. Always `programmatic_tool_calling`.

class ImageGeneration { type, action, background, 9 more }

A tool that generates images using the GPT image models.

type: :image\_generation

action: :generate | :edit | :auto

:generate

:edit

:auto

background: :transparent | :opaque | :auto

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

:transparent

:opaque

:auto

input\_fidelity: :high | :low

:high

:low

input\_image\_mask: InputImageMask{ file\_id, image\_url}

file\_id: String

image\_url: String

model: String | :"gpt-image-1" | :"gpt-image-1-mini" | :"gpt-image-2" | 3 more

String = String

Model = :"gpt-image-1" | :"gpt-image-1-mini" | :"gpt-image-2" | 3 more

:"gpt-image-1"

:"gpt-image-1-mini"

:"gpt-image-2"

:"gpt-image-2-2026-04-21"

:"gpt-image-1.5"

:"chatgpt-image-latest"

moderation: :auto | :low

:auto

:low

output\_compression: Integer

minimum0

maximum100

output\_format: :png | :webp | :jpeg

:png

:webp

:jpeg

partial\_images: Integer

minimum0

maximum3

quality: :low | :medium | :high | :auto

:low

:medium

:high

:auto

size: String | :"1024x1024" | :"1024x1536" | :"1536x1024" | :auto

String = String

Size = :"1024x1024" | :"1024x1536" | :"1536x1024" | :auto

:"1024x1024"

:"1024x1536"

:"1536x1024"

:auto

class LocalShell { type }

A tool that allows the model to execute shell commands in a local environment.

type: :local\_shell

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool { type, allowed\_callers, environment }

type: :shell

allowed\_callers: Array[:direct | :programmatic]

:direct

:programmatic

environment: [BetaContainerAuto](/api/reference/ruby/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_auto%20%3E%20(schema)) { type, file\_ids, memory\_limit, 2 more }  | [BetaLocalEnvironment](/api/reference/ruby/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_environment%20%3E%20(schema)) { type, skills }  | [BetaContainerReference](/api/reference/ruby/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_reference%20%3E%20(schema)) { container\_id, type }

class BetaContainerAuto { type, file\_ids, memory\_limit, 2 more }

type: :container\_auto

file\_ids: Array[String]

memory\_limit: :"1g" | :"4g" | :"16g" | :"64g"

:"1g"

:"4g"

:"16g"

:"64g"

network\_policy: [BetaContainerNetworkPolicyDisabled](/api/reference/ruby/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  | [BetaContainerNetworkPolicyAllowlist](/api/reference/ruby/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

class BetaContainerNetworkPolicyDisabled { type }

type: :disabled

class BetaContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array[String]

type: :allowlist

domain\_secrets: Array[[BetaContainerNetworkPolicyDomainSecret](/api/reference/ruby/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } ]

domain: String

minLength1

name: String

minLength1

value: String

maxLength10485760

minLength1

skills: Array[[BetaSkillReference](/api/reference/ruby/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_skill_reference%20%3E%20(schema)) { skill\_id, type, version }  | [BetaInlineSkill](/api/reference/ruby/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill%20%3E%20(schema)) { description, name, source, type } ]

class BetaSkillReference { skill\_id, type, version }

skill\_id: String

maxLength64

minLength1

type: :skill\_reference

version: String

class BetaInlineSkill { description, name, source, type }

description: String

name: String

source: [BetaInlineSkillSource](/api/reference/ruby/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema)) { data, media\_type, type }

data: String

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

media\_type: :"application/zip"

The media type of the inline skill payload. Must be `application/zip`.

type: :base64

The type of the inline skill source. Must be `base64`.

type: :inline

class BetaLocalEnvironment { type, skills }

type: :local

skills: Array[[BetaLocalSkill](/api/reference/ruby/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema)) { description, name, path } ]

description: String

name: String

path: String

class BetaContainerReference { container\_id, type }

container\_id: String

type: :container\_reference

class BetaCustomTool { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: String

type: :custom

allowed\_callers: Array[:direct | :programmatic]

:direct

:programmatic

defer\_loading: bool

description: String

format\_: Text{ type} | Grammar{ definition, syntax, type}

class Text { type }

Unconstrained free-form text.

type: :text

Unconstrained text format. Always `text`.

class Grammar { definition, syntax, type }

definition: String

syntax: :lark | :regex

:lark

:regex

type: :grammar

class BetaNamespaceTool { description, name, tools, type }

description: String

minLength1

name: String

minLength1

tools: Array[Function{ name, type, allowed\_callers, 5 more} | [BetaCustomTool](/api/reference/ruby/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_custom_tool%20%3E%20(schema)) { name, type, allowed\_callers, 3 more } ]

class Function { name, type, allowed\_callers, 5 more }

name: String

maxLength128

minLength1

type: :function

allowed\_callers: Array[:direct | :programmatic]

:direct

:programmatic

defer\_loading: bool

description: String

output\_schema: Hash[Symbol, untyped]

parameters: untyped

strict: bool

class BetaCustomTool { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: String

type: :custom

allowed\_callers: Array[:direct | :programmatic]

:direct

:programmatic

defer\_loading: bool

description: String

format\_: Text{ type} | Grammar{ definition, syntax, type}

class Text { type }

Unconstrained free-form text.

type: :text

Unconstrained text format. Always `text`.

class Grammar { definition, syntax, type }

definition: String

syntax: :lark | :regex

:lark

:regex

type: :grammar

type: :namespace

class BetaToolSearchTool { type, description, execution, parameters }

type: :tool\_search

description: String

execution: :server | :client

:server

:client

parameters: untyped

class BetaWebSearchPreviewTool { type, search\_content\_types, search\_context\_size, user\_location }

type: :web\_search\_preview | :web\_search\_preview\_2025\_03\_11

:web\_search\_preview

:web\_search\_preview\_2025\_03\_11

search\_content\_types: Array[:text | :image]

:text

:image

search\_context\_size: :low | :medium | :high

:low

:medium

:high

user\_location: UserLocation{ type, city, country, 2 more}

type: :approximate

city: String

country: String

region: String

timezone: String

class BetaApplyPatchTool { type, allowed\_callers }

type: :apply\_patch

allowed\_callers: Array[:direct | :programmatic]

:direct

:programmatic

type: :additional\_tools

The type of the item. Always `additional_tools`.

agent: Agent{ agent\_name}

agent\_name: String

class BetaResponseReasoningItem { id, summary, type, 4 more }

[managing context](https://platform.openai.com/docs/guides/conversation-state).

id: String

summary: Array[Summary{ text, type}]

text: String

type: :summary\_text

type: :reasoning

agent: Agent{ agent\_name}

agent\_name: String

content: Array[Content{ text, type}]

text: String

type: :reasoning\_text

encrypted\_content: String

status: :in\_progress | :completed | :incomplete

:in\_progress

:completed

:incomplete

class Program { id, call\_id, code, 3 more }

id: String

The unique ID of the program item.

call\_id: String

code: String

fingerprint: String

type: :program

The type of the item. Always `program`.

agent: Agent{ agent\_name}

agent\_name: String

class ProgramOutput { id, call\_id, result, 3 more }

id: String

The unique ID of the program output item.

call\_id: String

result: String

status: :completed | :incomplete

The terminal status of the program output item.

:completed

:incomplete

type: :program\_output

The type of the item. Always `program_output`.

agent: Agent{ agent\_name}

agent\_name: String

class BetaResponseCompactionItem { id, encrypted\_content, type, 2 more }

A compaction item generated by the [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).

id: String

The unique ID of the compaction item.

encrypted\_content: String

The encrypted content that was produced by compaction.

type: :compaction

agent: Agent{ agent\_name}

agent\_name: String

created\_by: String

The identifier of the actor that created the item.

class ImageGenerationCall { id, result, status, 2 more }

An image generation request made by the model.

id: String

result: String

status: :in\_progress | :completed | :generating | :failed

:in\_progress

:completed

:generating

:failed

type: :image\_generation\_call

agent: Agent{ agent\_name}

agent\_name: String

class BetaResponseCodeInterpreterToolCall { id, code, container\_id, 4 more }

id: String

code: String

container\_id: String

outputs: Array[Logs{ logs, type} | Image{ type, url}]

class Logs { logs, type }

logs: String

type: :logs

class Image { type, url }

type: :image

url: String

status: :in\_progress | :completed | :incomplete | 2 more

:in\_progress

:completed

:incomplete

:interpreting

:failed

type: :code\_interpreter\_call

agent: Agent{ agent\_name}

agent\_name: String

class LocalShellCall { id, action, call\_id, 3 more }

A tool call to run a command on the local shell.

id: String

action: Action{ command, env, type, 3 more}

command: Array[String]

env: Hash[Symbol, String]

type: :exec

timeout\_ms: Integer

user: String

working\_directory: String

call\_id: String

status: :in\_progress | :completed | :incomplete

:in\_progress

:completed

:incomplete

type: :local\_shell\_call

agent: Agent{ agent\_name}

agent\_name: String

class LocalShellCallOutput { id, output, type, 2 more }

The output of a local shell tool call.

id: String

output: String

type: :local\_shell\_call\_output

agent: Agent{ agent\_name}

agent\_name: String

status: :in\_progress | :completed | :incomplete

:in\_progress

:completed

:incomplete

class BetaResponseFunctionShellToolCall { id, action, call\_id, 6 more }

A tool call that executes one or more shell commands in a managed environment.

id: String

action: Action{ commands, max\_output\_length, timeout\_ms}

commands: Array[String]

max\_output\_length: Integer

Optional maximum number of characters to return from each command.

timeout\_ms: Integer

Optional timeout in milliseconds for the commands.

call\_id: String

environment: [BetaResponseLocalEnvironment](/api/reference/ruby/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_local_environment%20%3E%20(schema)) { type }  | [BetaResponseContainerReference](/api/reference/ruby/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_container_reference%20%3E%20(schema)) { container\_id, type }

Represents the use of a local environment to perform shell actions.

class BetaResponseLocalEnvironment { type }

Represents the use of a local environment to perform shell actions.

type: :local

The environment type. Always `local`.

class BetaResponseContainerReference { container\_id, type }

Represents a container created with /v1/containers.

container\_id: String

type: :container\_reference

The environment type. Always `container_reference`.

status: :in\_progress | :completed | :incomplete

:in\_progress

:completed

:incomplete

type: :shell\_call

agent: Agent{ agent\_name}

agent\_name: String

caller\_: Direct{ type} | Program{ caller\_id, type}

class Direct { type }

type: :direct

class Program { caller\_id, type }

caller\_id: String

type: :program

created\_by: String

The ID of the entity that created this tool call.

class BetaResponseFunctionShellToolCallOutput { id, call\_id, max\_output\_length, 6 more }

The output of a shell tool call that was emitted.

id: String

The unique ID of the shell call output. Populated when this item is returned via API.

call\_id: String

max\_output\_length: Integer

The maximum length of the shell command output. This is generated by the model and should be passed back with the raw output.

output: Array[Output{ outcome, stderr, stdout, created\_by}]

An array of shell call output contents

outcome: Timeout{ type} | Exit{ exit\_code, type}

Represents either an exit outcome (with an exit code) or a timeout outcome for a shell call output chunk.

class Timeout { type }

Indicates that the shell call exceeded its configured time limit.

type: :timeout

The outcome type. Always `timeout`.

class Exit { exit\_code, type }

exit\_code: Integer

Exit code from the shell process.

type: :exit

stderr: String

The standard error output that was captured.

stdout: String

The standard output that was captured.

created\_by: String

The identifier of the actor that created the item.

status: :in\_progress | :completed | :incomplete

The status of the shell call output. One of `in_progress`, `completed`, or `incomplete`.

:in\_progress

:completed

:incomplete

type: :shell\_call\_output

The type of the shell call output. Always `shell_call_output`.

agent: Agent{ agent\_name}

agent\_name: String

caller\_: Direct{ type} | Program{ caller\_id, type}

class Direct { type }

type: :direct

class Program { caller\_id, type }

caller\_id: String

type: :program

created\_by: String

The identifier of the actor that created the item.

class BetaResponseApplyPatchToolCall { id, call\_id, operation, 5 more }

A tool call that applies file diffs by creating, deleting, or updating files.

id: String

call\_id: String

operation: CreateFile{ diff, path, type} | DeleteFile{ path, type} | UpdateFile{ diff, path, type}

One of the create\_file, delete\_file, or update\_file operations applied via apply\_patch.

class CreateFile { diff, path, type }

Instruction describing how to create a file via the apply\_patch tool.

diff: String

Diff to apply.

path: String

Path of the file to create.

type: :create\_file

Create a new file with the provided diff.

class DeleteFile { path, type }

Instruction describing how to delete a file via the apply\_patch tool.

path: String

Path of the file to delete.

type: :delete\_file

Delete the specified file.

class UpdateFile { diff, path, type }

Instruction describing how to update a file via the apply\_patch tool.

diff: String

Diff to apply.

path: String

Path of the file to update.

type: :update\_file

Update an existing file with the provided diff.

status: :in\_progress | :completed

:in\_progress

:completed

type: :apply\_patch\_call

agent: Agent{ agent\_name}

agent\_name: String

caller\_: Direct{ type} | Program{ caller\_id, type}

class Direct { type }

type: :direct

class Program { caller\_id, type }

caller\_id: String

type: :program

created\_by: String

The ID of the entity that created this tool call.

class BetaResponseApplyPatchToolCallOutput { id, call\_id, status, 5 more }

The output emitted by an apply patch tool call.

id: String

call\_id: String

status: :completed | :failed

:completed

:failed

type: :apply\_patch\_call\_output

agent: Agent{ agent\_name}

agent\_name: String

caller\_: Direct{ type} | Program{ caller\_id, type}

class Direct { type }

type: :direct

class Program { caller\_id, type }

caller\_id: String

type: :program

created\_by: String

The ID of the entity that created this tool call output.

output: String

Optional textual output returned by the apply patch tool.

class McpListTools { id, server\_label, tools, 3 more }

A list of tools available on an MCP server.

id: String

server\_label: String

tools: Array[Tool{ input\_schema, name, annotations, description}]

input\_schema: untyped

name: String

annotations: untyped

description: String

type: :mcp\_list\_tools

agent: Agent{ agent\_name}

agent\_name: String

error: String

class McpApprovalRequest { id, arguments, name, 3 more }

A request for human approval of a tool invocation.

id: String

arguments: String

name: String

server\_label: String

type: :mcp\_approval\_request

agent: Agent{ agent\_name}

agent\_name: String

class McpApprovalResponse { id, approval\_request\_id, approve, 3 more }

A response to an MCP approval request.

id: String

approval\_request\_id: String

approve: bool

type: :mcp\_approval\_response

agent: Agent{ agent\_name}

agent\_name: String

reason: String

class McpCall { id, arguments, name, 7 more }

An invocation of a tool on an MCP server.

id: String

arguments: String

name: String

server\_label: String

type: :mcp\_call

agent: Agent{ agent\_name}

agent\_name: String

approval\_request\_id: String

error: String

output: String

status: :in\_progress | :completed | :incomplete | 2 more

:in\_progress

:completed

:incomplete

:calling

:failed

class BetaResponseCustomToolCallItem { id, status, created\_by }

id: String

The unique ID of the custom tool call item.

status: :in\_progress | :completed | :incomplete

:in\_progress

:completed

:incomplete

created\_by: String

The identifier of the actor that created the item.

class BetaResponseCustomToolCallOutputItem { id, status, created\_by }

id: String

The unique ID of the custom tool call output item.

status: :in\_progress | :completed | :incomplete

:in\_progress

:completed

:incomplete

created\_by: String

The identifier of the actor that created the item.

### List input items

Ruby

require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.beta.responses.input_items.list("response_id")

puts(page)

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
