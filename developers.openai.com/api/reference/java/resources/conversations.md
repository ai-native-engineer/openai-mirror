<!-- source: https://developers.openai.com/api/reference/java/resources/conversations/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Conversations

Manage conversations and conversation items.

##### [Create a conversation](/api/reference/java/resources/conversations/methods/create)

[Conversation](/api/reference/java/resources/conversations#(resource)%20conversations%20%3E%20(model)%20conversation%20%3E%20(schema)) conversations().create(ConversationCreateParamsparams = ConversationCreateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/conversations

##### [Retrieve a conversation](/api/reference/java/resources/conversations/methods/retrieve)

[Conversation](/api/reference/java/resources/conversations#(resource)%20conversations%20%3E%20(model)%20conversation%20%3E%20(schema)) conversations().retrieve(ConversationRetrieveParamsparams = ConversationRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/conversations/{conversation\_id}

##### [Update a conversation](/api/reference/java/resources/conversations/methods/update)

[Conversation](/api/reference/java/resources/conversations#(resource)%20conversations%20%3E%20(model)%20conversation%20%3E%20(schema)) conversations().update(ConversationUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/conversations/{conversation\_id}

##### [Delete a conversation](/api/reference/java/resources/conversations/methods/delete)

[ConversationDeletedResource](/api/reference/java/resources/conversations#(resource)%20conversations%20%3E%20(model)%20conversation_deleted_resource%20%3E%20(schema)) conversations().delete(ConversationDeleteParamsparams = ConversationDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/conversations/{conversation\_id}

##### ModelsExpand Collapse

class ComputerScreenshotContent:

A screenshot of a computer.

Detail detail

The detail level of the screenshot image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

One of the following:

LOW("low")

HIGH("high")

AUTO("auto")

ORIGINAL("original")

Optional<String> fileId

The identifier of an uploaded file that contains the screenshot.

Optional<String> imageUrl

The URL of the screenshot image.

formaturi

JsonValue; type "computer\_screenshot"constant"computer\_screenshot"constant

Specifies the event type. For a computer screenshot, this property is always set to `computer_screenshot`.

class Conversation:

String id

The unique ID of the conversation.

long createdAt

The time at which the conversation was created, measured in seconds since the Unix epoch.

formatunixtime

JsonValue metadata

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format, and querying for objects via API or the dashboard.
Keys are strings with a maximum length of 64 characters. Values are strings with a maximum length of 512 characters.

JsonValue; object\_ "conversation"constant"conversation"constant

The object type, which is always `conversation`.

class ConversationDeleted:

String id

boolean deleted

JsonValue; object\_ "conversation.deleted"constant"conversation.deleted"constant

class ConversationDeletedResource:

String id

boolean deleted

JsonValue; object\_ "conversation.deleted"constant"conversation.deleted"constant

class Message:

A message to or from the model.

String id

The unique ID of the message.

List<Content> content

The content of the message

One of the following:

class ResponseInputText:

A text input to the model.

String text

The text input to the model.

JsonValue; type "input\_text"constant"input\_text"constant

The type of the input item. Always `input_text`.

class ResponseOutputText:

A text output from the model.

List<Annotation> annotations

The annotations of the text output.

One of the following:

class FileCitation:

A citation to a file.

String fileId

The ID of the file.

String filename

The filename of the file cited.

long index

The index of the file in the list of files.

JsonValue; type "file\_citation"constant"file\_citation"constant

The type of the file citation. Always `file_citation`.

class UrlCitation:

A citation for a web resource used to generate a model response.

long endIndex

The index of the last character of the URL citation in the message.

long startIndex

The index of the first character of the URL citation in the message.

String title

The title of the web resource.

JsonValue; type "url\_citation"constant"url\_citation"constant

The type of the URL citation. Always `url_citation`.

String url

The URL of the web resource.

formaturi

class ContainerFileCitation:

A citation for a container file used to generate a model response.

String containerId

The ID of the container file.

long endIndex

The index of the last character of the container file citation in the message.

String fileId

The ID of the file.

String filename

The filename of the container file cited.

long startIndex

The index of the first character of the container file citation in the message.

JsonValue; type "container\_file\_citation"constant"container\_file\_citation"constant

The type of the container file citation. Always `container_file_citation`.

class FilePath:

A path to a file.

String fileId

The ID of the file.

long index

The index of the file in the list of files.

JsonValue; type "file\_path"constant"file\_path"constant

The type of the file path. Always `file_path`.

String text

The text output from the model.

JsonValue; type "output\_text"constant"output\_text"constant

The type of the output text. Always `output_text`.

Optional<List<Logprob>> logprobs

String token

List<long> bytes

double logprob

List<TopLogprob> topLogprobs

String token

List<long> bytes

double logprob

class TextContent:

A text content.

String text

JsonValue; type "text"constant"text"constant

class SummaryTextContent:

A summary text from the model.

String text

A summary of the reasoning output from the model so far.

JsonValue; type "summary\_text"constant"summary\_text"constant

The type of the object. Always `summary_text`.

class ReasoningText:

Reasoning text from the model.

String text

The reasoning text from the model.

JsonValue; type "reasoning\_text"constant"reasoning\_text"constant

The type of the reasoning text. Always `reasoning_text`.

class ResponseOutputRefusal:

A refusal from the model.

String refusal

The refusal explanation from the model.

JsonValue; type "refusal"constant"refusal"constant

The type of the refusal. Always `refusal`.

class ResponseInputImage:

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

Detail detail

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

One of the following:

LOW("low")

HIGH("high")

AUTO("auto")

ORIGINAL("original")

JsonValue; type "input\_image"constant"input\_image"constant

The type of the input item. Always `input_image`.

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> imageUrl

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

class ComputerScreenshotContent:

A screenshot of a computer.

Detail detail

The detail level of the screenshot image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

One of the following:

LOW("low")

HIGH("high")

AUTO("auto")

ORIGINAL("original")

Optional<String> fileId

The identifier of an uploaded file that contains the screenshot.

Optional<String> imageUrl

The URL of the screenshot image.

formaturi

JsonValue; type "computer\_screenshot"constant"computer\_screenshot"constant

Specifies the event type. For a computer screenshot, this property is always set to `computer_screenshot`.

class ResponseInputFile:

A file input to the model.

JsonValue; type "input\_file"constant"input\_file"constant

The type of the input item. Always `input_file`.

Optional<Detail> detail

The detail level of the file to be sent to the model. Use `low` for the default rendering behavior, or `high` to render the file at higher quality. Defaults to `low`.

One of the following:

LOW("low")

HIGH("high")

Optional<String> fileData

The content of the file to be sent to the model.

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> fileUrl

The URL of the file to be sent to the model.

formaturi

Optional<String> filename

The name of the file to be sent to the model.

Role role

The role of the message. One of `unknown`, `user`, `assistant`, `system`, `critic`, `discriminator`, `developer`, or `tool`.

One of the following:

UNKNOWN("unknown")

USER("user")

ASSISTANT("assistant")

SYSTEM("system")

CRITIC("critic")

DISCRIMINATOR("discriminator")

DEVELOPER("developer")

TOOL("tool")

Status status

The status of item. One of `in_progress`, `completed`, or `incomplete`. Populated when items are returned via API.

One of the following:

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

JsonValue; type "message"constant"message"constant

The type of the message. Always set to `message`.

Optional<Phase> phase

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`). For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

One of the following:

COMMENTARY("commentary")

FINAL\_ANSWER("final\_answer")

class SummaryTextContent:

A summary text from the model.

String text

A summary of the reasoning output from the model so far.

JsonValue; type "summary\_text"constant"summary\_text"constant

The type of the object. Always `summary_text`.

class TextContent:

A text content.

String text

JsonValue; type "text"constant"text"constant

#### ConversationsItems

Manage conversations and conversation items.

##### [Create items](/api/reference/java/resources/conversations/subresources/items/methods/create)

[ConversationItemList](/api/reference/java/resources/conversations#(resource)%20conversations.items%20%3E%20(model)%20conversation_item_list%20%3E%20(schema)) conversations().items().create(ItemCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/conversations/{conversation\_id}/items

##### [List items](/api/reference/java/resources/conversations/subresources/items/methods/list)

ItemListPage conversations().items().list(ItemListParamsparams = ItemListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/conversations/{conversation\_id}/items

##### [Retrieve an item](/api/reference/java/resources/conversations/subresources/items/methods/retrieve)

[ConversationItem](/api/reference/java/resources/conversations#(resource)%20conversations.items%20%3E%20(model)%20conversation_item%20%3E%20(schema)) conversations().items().retrieve(ItemRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/conversations/{conversation\_id}/items/{item\_id}

##### [Delete an item](/api/reference/java/resources/conversations/subresources/items/methods/delete)

[Conversation](/api/reference/java/resources/conversations#(resource)%20conversations%20%3E%20(model)%20conversation%20%3E%20(schema)) conversations().items().delete(ItemDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

DELETE/conversations/{conversation\_id}/items/{item\_id}

##### ModelsExpand Collapse

class ConversationItem: A class that can be one of several variants.union

A single item within a conversation. The set of possible types are the same as the `output` type of a [Response object](https://platform.openai.com/docs/api-reference/responses/object#responses/object-output).

class Message:

A message to or from the model.

String id

The unique ID of the message.

List<Content> content

The content of the message

One of the following:

class ResponseInputText:

A text input to the model.

String text

The text input to the model.

JsonValue; type "input\_text"constant"input\_text"constant

The type of the input item. Always `input_text`.

class ResponseOutputText:

A text output from the model.

List<Annotation> annotations

The annotations of the text output.

One of the following:

class FileCitation:

A citation to a file.

String fileId

The ID of the file.

String filename

The filename of the file cited.

long index

The index of the file in the list of files.

JsonValue; type "file\_citation"constant"file\_citation"constant

The type of the file citation. Always `file_citation`.

class UrlCitation:

A citation for a web resource used to generate a model response.

long endIndex

The index of the last character of the URL citation in the message.

long startIndex

The index of the first character of the URL citation in the message.

String title

The title of the web resource.

JsonValue; type "url\_citation"constant"url\_citation"constant

The type of the URL citation. Always `url_citation`.

String url

The URL of the web resource.

formaturi

class ContainerFileCitation:

A citation for a container file used to generate a model response.

String containerId

The ID of the container file.

long endIndex

The index of the last character of the container file citation in the message.

String fileId

The ID of the file.

String filename

The filename of the container file cited.

long startIndex

The index of the first character of the container file citation in the message.

JsonValue; type "container\_file\_citation"constant"container\_file\_citation"constant

The type of the container file citation. Always `container_file_citation`.

class FilePath:

A path to a file.

String fileId

The ID of the file.

long index

The index of the file in the list of files.

JsonValue; type "file\_path"constant"file\_path"constant

The type of the file path. Always `file_path`.

String text

The text output from the model.

JsonValue; type "output\_text"constant"output\_text"constant

The type of the output text. Always `output_text`.

Optional<List<Logprob>> logprobs

String token

List<long> bytes

double logprob

List<TopLogprob> topLogprobs

String token

List<long> bytes

double logprob

class TextContent:

A text content.

String text

JsonValue; type "text"constant"text"constant

class SummaryTextContent:

A summary text from the model.

String text

A summary of the reasoning output from the model so far.

JsonValue; type "summary\_text"constant"summary\_text"constant

The type of the object. Always `summary_text`.

class ReasoningText:

Reasoning text from the model.

String text

The reasoning text from the model.

JsonValue; type "reasoning\_text"constant"reasoning\_text"constant

The type of the reasoning text. Always `reasoning_text`.

class ResponseOutputRefusal:

A refusal from the model.

String refusal

The refusal explanation from the model.

JsonValue; type "refusal"constant"refusal"constant

The type of the refusal. Always `refusal`.

class ResponseInputImage:

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

Detail detail

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

One of the following:

LOW("low")

HIGH("high")

AUTO("auto")

ORIGINAL("original")

JsonValue; type "input\_image"constant"input\_image"constant

The type of the input item. Always `input_image`.

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> imageUrl

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

class ComputerScreenshotContent:

A screenshot of a computer.

Detail detail

The detail level of the screenshot image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

One of the following:

LOW("low")

HIGH("high")

AUTO("auto")

ORIGINAL("original")

Optional<String> fileId

The identifier of an uploaded file that contains the screenshot.

Optional<String> imageUrl

The URL of the screenshot image.

formaturi

JsonValue; type "computer\_screenshot"constant"computer\_screenshot"constant

Specifies the event type. For a computer screenshot, this property is always set to `computer_screenshot`.

class ResponseInputFile:

A file input to the model.

JsonValue; type "input\_file"constant"input\_file"constant

The type of the input item. Always `input_file`.

Optional<Detail> detail

The detail level of the file to be sent to the model. Use `low` for the default rendering behavior, or `high` to render the file at higher quality. Defaults to `low`.

One of the following:

LOW("low")

HIGH("high")

Optional<String> fileData

The content of the file to be sent to the model.

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> fileUrl

The URL of the file to be sent to the model.

formaturi

Optional<String> filename

The name of the file to be sent to the model.

Role role

The role of the message. One of `unknown`, `user`, `assistant`, `system`, `critic`, `discriminator`, `developer`, or `tool`.

One of the following:

UNKNOWN("unknown")

USER("user")

ASSISTANT("assistant")

SYSTEM("system")

CRITIC("critic")

DISCRIMINATOR("discriminator")

DEVELOPER("developer")

TOOL("tool")

Status status

The status of item. One of `in_progress`, `completed`, or `incomplete`. Populated when items are returned via API.

One of the following:

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

JsonValue; type "message"constant"message"constant

The type of the message. Always set to `message`.

Optional<Phase> phase

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`). For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

One of the following:

COMMENTARY("commentary")

FINAL\_ANSWER("final\_answer")

class ResponseFunctionToolCallItem:

A tool call to run a function. See the
[function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.

String id

The unique ID of the function tool call.

Status status

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

One of the following:

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

Optional<String> createdBy

The identifier of the actor that created the item.

class ResponseFunctionToolCallOutputItem:

String id

The unique ID of the function call tool output.

String callId

The unique ID of the function tool call generated by the model.

Output output

The output from the function call generated by your code.
Can be a string or an list of output content.

One of the following:

String

List<FunctionAndCustomToolCallOutput>

One of the following:

class ResponseInputText:

A text input to the model.

String text

The text input to the model.

JsonValue; type "input\_text"constant"input\_text"constant

The type of the input item. Always `input_text`.

class ResponseInputImage:

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

Detail detail

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

One of the following:

LOW("low")

HIGH("high")

AUTO("auto")

ORIGINAL("original")

JsonValue; type "input\_image"constant"input\_image"constant

The type of the input item. Always `input_image`.

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> imageUrl

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

class ResponseInputFile:

A file input to the model.

JsonValue; type "input\_file"constant"input\_file"constant

The type of the input item. Always `input_file`.

Optional<Detail> detail

The detail level of the file to be sent to the model. Use `low` for the default rendering behavior, or `high` to render the file at higher quality. Defaults to `low`.

One of the following:

LOW("low")

HIGH("high")

Optional<String> fileData

The content of the file to be sent to the model.

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> fileUrl

The URL of the file to be sent to the model.

formaturi

Optional<String> filename

The name of the file to be sent to the model.

Status status

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

One of the following:

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

JsonValue; type "function\_call\_output"constant"function\_call\_output"constant

The type of the function tool call output. Always `function_call_output`.

Optional<String> createdBy

The identifier of the actor that created the item.

class ResponseFileSearchToolCall:

The results of a file search tool call. See the
[file search guide](https://platform.openai.com/docs/guides/tools-file-search) for more information.

String id

The unique ID of the file search tool call.

List<String> queries

The queries used to search for files.

Status status

The status of the file search tool call. One of `in_progress`,
`searching`, `incomplete` or `failed`,

One of the following:

IN\_PROGRESS("in\_progress")

SEARCHING("searching")

COMPLETED("completed")

INCOMPLETE("incomplete")

FAILED("failed")

JsonValue; type "file\_search\_call"constant"file\_search\_call"constant

The type of the file search tool call. Always `file_search_call`.

Optional<List<Result>> results

The results of the file search tool call.

Optional<Attributes> attributes

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.

One of the following:

String

double

boolean

Optional<String> fileId

The unique ID of the file.

Optional<String> filename

The name of the file.

Optional<Double> score

The relevance score of the file - a value between 0 and 1.

formatfloat

Optional<String> text

The text that was retrieved from the file.

class ResponseFunctionWebSearch:

The results of a web search tool call. See the
[web search guide](https://platform.openai.com/docs/guides/tools-web-search) for more information.

String id

The unique ID of the web search tool call.

Action action

An object describing the specific action taken in this web search call.
Includes details on how the model used the web (search, open\_page, find\_in\_page).

One of the following:

class Search:

Action type “search” - Performs a web search query.

JsonValue; type "search"constant"search"constant

The action type.

Optional<List<String>> queries

The search queries.

DeprecatedOptional<String> query

The search query.

Optional<List<Source>> sources

The sources used in the search.

JsonValue; type "url"constant"url"constant

The type of source. Always `url`.

String url

The URL of the source.

formaturi

class OpenPage:

Action type “open\_page” - Opens a specific URL from search results.

JsonValue; type "open\_page"constant"open\_page"constant

The action type.

Optional<String> url

The URL opened by the model.

formaturi

class FindInPage:

Action type “find\_in\_page”: Searches for a pattern within a loaded page.

String pattern

The pattern or text to search for within the page.

JsonValue; type "find\_in\_page"constant"find\_in\_page"constant

The action type.

String url

The URL of the page searched for the pattern.

formaturi

Status status

The status of the web search tool call.

One of the following:

IN\_PROGRESS("in\_progress")

SEARCHING("searching")

COMPLETED("completed")

FAILED("failed")

JsonValue; type "web\_search\_call"constant"web\_search\_call"constant

The type of the web search tool call. Always `web_search_call`.

ImageGenerationCall

String id

The unique ID of the image generation call.

Optional<String> result

The generated image encoded in base64.

Status status

The status of the image generation call.

One of the following:

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

GENERATING("generating")

FAILED("failed")

JsonValue; type "image\_generation\_call"constant"image\_generation\_call"constant

The type of the image generation call. Always `image_generation_call`.

class ResponseComputerToolCall:

A tool call to a computer use tool. See the
[computer use guide](https://platform.openai.com/docs/guides/tools-computer-use) for more information.

String id

The unique ID of the computer call.

String callId

An identifier used when responding to the tool call with output.

List<PendingSafetyCheck> pendingSafetyChecks

The pending safety checks for the computer call.

String id

The ID of the pending safety check.

Optional<String> code

The type of the pending safety check.

Optional<String> message

Details about the pending safety check.

Status status

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

One of the following:

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

Type type

The type of the computer call. Always `computer_call`.

Optional<Action> action

A click action.

One of the following:

class Click:

A click action.

Button button

Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

One of the following:

LEFT("left")

RIGHT("right")

WHEEL("wheel")

BACK("back")

FORWARD("forward")

JsonValue; type "click"constant"click"constant

Specifies the event type. For a click action, this property is always `click`.

long x

The x-coordinate where the click occurred.

long y

The y-coordinate where the click occurred.

Optional<List<String>> keys

The keys being held while clicking.

class DoubleClick:

A double click action.

Optional<List<String>> keys

The keys being held while double-clicking.

JsonValue; type "double\_click"constant"double\_click"constant

Specifies the event type. For a double click action, this property is always set to `double_click`.

long x

The x-coordinate where the double click occurred.

long y

The y-coordinate where the double click occurred.

class Drag:

A drag action.

List<Path> path

An array of coordinates representing the path of the drag action. Coordinates will appear as an array of objects, eg

[
  { x: 100, y: 200 },
  { x: 200, y: 300 }
]

long x

The x-coordinate.

long y

The y-coordinate.

JsonValue; type "drag"constant"drag"constant

Specifies the event type. For a drag action, this property is always set to `drag`.

Optional<List<String>> keys

The keys being held while dragging the mouse.

class Keypress:

A collection of keypresses the model would like to perform.

List<String> keys

The combination of keys the model is requesting to be pressed. This is an array of strings, each representing a key.

JsonValue; type "keypress"constant"keypress"constant

Specifies the event type. For a keypress action, this property is always set to `keypress`.

class Move:

A mouse move action.

JsonValue; type "move"constant"move"constant

Specifies the event type. For a move action, this property is always set to `move`.

long x

The x-coordinate to move to.

long y

The y-coordinate to move to.

Optional<List<String>> keys

The keys being held while moving the mouse.

JsonValue;

JsonValue; type "screenshot"constant"screenshot"constant

Specifies the event type. For a screenshot action, this property is always set to `screenshot`.

class Scroll:

A scroll action.

long scrollX

The horizontal scroll distance.

long scrollY

The vertical scroll distance.

JsonValue; type "scroll"constant"scroll"constant

Specifies the event type. For a scroll action, this property is always set to `scroll`.

long x

The x-coordinate where the scroll occurred.

long y

The y-coordinate where the scroll occurred.

Optional<List<String>> keys

The keys being held while scrolling.

class Type:

An action to type in text.

String text

The text to type.

JsonValue; type "type"constant"type"constant

Specifies the event type. For a type action, this property is always set to `type`.

JsonValue;

JsonValue; type "wait"constant"wait"constant

Specifies the event type. For a wait action, this property is always set to `wait`.

Optional<List<[ComputerAction](/api/reference/java/resources/responses#(resource)%20responses%20%3E%20(model)%20computer_action%20%3E%20(schema))>> actions

Flattened batched actions for `computer_use`. Each action includes an
`type` discriminator and action-specific fields.

One of the following:

Click

Button button

Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

One of the following:

LEFT("left")

RIGHT("right")

WHEEL("wheel")

BACK("back")

FORWARD("forward")

JsonValue; type "click"constant"click"constant

Specifies the event type. For a click action, this property is always `click`.

long x

The x-coordinate where the click occurred.

long y

The y-coordinate where the click occurred.

Optional<List<String>> keys

The keys being held while clicking.

DoubleClick

Optional<List<String>> keys

The keys being held while double-clicking.

JsonValue; type "double\_click"constant"double\_click"constant

Specifies the event type. For a double click action, this property is always set to `double_click`.

long x

The x-coordinate where the double click occurred.

long y

The y-coordinate where the double click occurred.

Drag

List<Path> path

An array of coordinates representing the path of the drag action. Coordinates will appear as an array of objects, eg

[
  { x: 100, y: 200 },
  { x: 200, y: 300 }
]

long x

The x-coordinate.

long y

The y-coordinate.

JsonValue; type "drag"constant"drag"constant

Specifies the event type. For a drag action, this property is always set to `drag`.

Optional<List<String>> keys

The keys being held while dragging the mouse.

Keypress

List<String> keys

The combination of keys the model is requesting to be pressed. This is an array of strings, each representing a key.

JsonValue; type "keypress"constant"keypress"constant

Specifies the event type. For a keypress action, this property is always set to `keypress`.

Move

JsonValue; type "move"constant"move"constant

Specifies the event type. For a move action, this property is always set to `move`.

long x

The x-coordinate to move to.

long y

The y-coordinate to move to.

Optional<List<String>> keys

The keys being held while moving the mouse.

JsonValue;

JsonValue; type "screenshot"constant"screenshot"constant

Specifies the event type. For a screenshot action, this property is always set to `screenshot`.

Scroll

long scrollX

The horizontal scroll distance.

long scrollY

The vertical scroll distance.

JsonValue; type "scroll"constant"scroll"constant

Specifies the event type. For a scroll action, this property is always set to `scroll`.

long x

The x-coordinate where the scroll occurred.

long y

The y-coordinate where the scroll occurred.

Optional<List<String>> keys

The keys being held while scrolling.

Type

String text

The text to type.

JsonValue; type "type"constant"type"constant

Specifies the event type. For a type action, this property is always set to `type`.

JsonValue;

JsonValue; type "wait"constant"wait"constant

Specifies the event type. For a wait action, this property is always set to `wait`.

class ResponseComputerToolCallOutputItem:

String id

The unique ID of the computer call tool output.

String callId

The ID of the computer tool call that produced the output.

[ResponseComputerToolCallOutputScreenshot](/api/reference/java/resources/responses#(resource)%20responses%20%3E%20(model)%20response_computer_tool_call_output_screenshot%20%3E%20(schema)) output

A computer screenshot image used with the computer use tool.

Status status

The status of the message input. One of `in_progress`, `completed`, or
`incomplete`. Populated when input items are returned via API.

One of the following:

COMPLETED("completed")

INCOMPLETE("incomplete")

FAILED("failed")

IN\_PROGRESS("in\_progress")

JsonValue; type "computer\_call\_output"constant"computer\_call\_output"constant

The type of the computer tool call output. Always `computer_call_output`.

Optional<List<AcknowledgedSafetyCheck>> acknowledgedSafetyChecks

The safety checks reported by the API that have been acknowledged by the
developer.

String id

The ID of the pending safety check.

Optional<String> code

The type of the pending safety check.

Optional<String> message

Details about the pending safety check.

Optional<String> createdBy

The identifier of the actor that created the item.

class ResponseToolSearchCall:

String id

The unique ID of the tool search call item.

JsonValue arguments

Arguments used for the tool search call.

Optional<String> callId

The unique ID of the tool search call generated by the model.

Execution execution

Whether tool search was executed by the server or by the client.

One of the following:

SERVER("server")

CLIENT("client")

Status status

The status of the tool search call item that was recorded.

One of the following:

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

JsonValue; type "tool\_search\_call"constant"tool\_search\_call"constant

The type of the item. Always `tool_search_call`.

Optional<String> createdBy

The identifier of the actor that created the item.

class ResponseToolSearchOutputItem:

String id

The unique ID of the tool search output item.

Optional<String> callId

The unique ID of the tool search call generated by the model.

Execution execution

Whether tool search was executed by the server or by the client.

One of the following:

SERVER("server")

CLIENT("client")

Status status

The status of the tool search output item that was recorded.

One of the following:

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

List<[Tool](/api/reference/java/resources/responses#(resource)%20responses%20%3E%20(model)%20tool%20%3E%20(schema))> tools

The loaded tool definitions returned by tool search.

One of the following:

class FunctionTool:

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

String name

The name of the function to call.

Optional<Parameters> parameters

A JSON schema object describing the parameters of the function.

Optional<Boolean> strict

Whether to enforce strict parameter validation. Default `true`.

JsonValue; type "function"constant"function"constant

The type of the function tool. Always `function`.

Optional<Boolean> deferLoading

Whether this function is deferred and loaded via tool search.

Optional<String> description

A description of the function. Used by the model to determine whether or not to call the function.

class FileSearchTool:

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

JsonValue; type "file\_search"constant"file\_search"constant

The type of the file search tool. Always `file_search`.

List<String> vectorStoreIds

The IDs of the vector stores to search.

Optional<Filters> filters

A filter to apply.

One of the following:

class ComparisonFilter:

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

String key

The key to compare against the value.

Type type

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

EQ("eq")

NE("ne")

GT("gt")

GTE("gte")

LT("lt")

LTE("lte")

IN("in")

NIN("nin")

Value value

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

String

double

boolean

List<ComparisonFilterValueItem>

One of the following:

String

double

class CompoundFilter:

Combine multiple filters using `and` or `or`.

List<Filter> filters

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

One of the following:

class ComparisonFilter:

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

String key

The key to compare against the value.

Type type

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

EQ("eq")

NE("ne")

GT("gt")

GTE("gte")

LT("lt")

LTE("lte")

IN("in")

NIN("nin")

Value value

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

String

double

boolean

List<ComparisonFilterValueItem>

One of the following:

String

double

JsonValue

Type type

Type of operation: `and` or `or`.

One of the following:

AND("and")

OR("or")

Optional<Long> maxNumResults

The maximum number of results to return. This number should be between 1 and 50 inclusive.

Optional<RankingOptions> rankingOptions

Ranking options for search.

Optional<HybridSearch> hybridSearch

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

double embeddingWeight

The weight of the embedding in the reciprocal ranking fusion.

double textWeight

The weight of the text in the reciprocal ranking fusion.

Optional<Ranker> ranker

The ranker to use for the file search.

One of the following:

AUTO("auto")

DEFAULT\_2024\_11\_15("default-2024-11-15")

Optional<Double> scoreThreshold

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

class ComputerTool:

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

JsonValue; type "computer"constant"computer"constant

The type of the computer tool. Always `computer`.

class ComputerUsePreviewTool:

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

long displayHeight

The height of the computer display.

long displayWidth

The width of the computer display.

Environment environment

The type of computer environment to control.

One of the following:

WINDOWS("windows")

MAC("mac")

LINUX("linux")

UBUNTU("ubuntu")

BROWSER("browser")

JsonValue; type "computer\_use\_preview"constant"computer\_use\_preview"constant

The type of the computer use tool. Always `computer_use_preview`.

class WebSearchTool:

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type type

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

One of the following:

WEB\_SEARCH("web\_search")

WEB\_SEARCH\_2025\_08\_26("web\_search\_2025\_08\_26")

Optional<Filters> filters

Filters for the search.

Optional<List<String>> allowedDomains

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

Optional<SearchContextSize> searchContextSize

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

LOW("low")

MEDIUM("medium")

HIGH("high")

Optional<UserLocation> userLocation

The approximate location of the user.

Optional<String> city

Free text input for the city of the user, e.g. `San Francisco`.

Optional<String> country

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

Optional<String> region

Free text input for the region of the user, e.g. `California`.

Optional<String> timezone

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

Optional<Type> type

The type of location approximation. Always `approximate`.

Mcp

String serverLabel

A label for this MCP server, used to identify it in tool calls.

JsonValue; type "mcp"constant"mcp"constant

The type of the MCP tool. Always `mcp`.

Optional<AllowedTools> allowedTools

List of allowed tool names or a filter object.

One of the following:

List<String>

class McpToolFilter:

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

Optional<String> authorization

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

Optional<ConnectorId> connectorId

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

CONNECTOR\_DROPBOX("connector\_dropbox")

CONNECTOR\_GMAIL("connector\_gmail")

CONNECTOR\_GOOGLECALENDAR("connector\_googlecalendar")

CONNECTOR\_GOOGLEDRIVE("connector\_googledrive")

CONNECTOR\_MICROSOFTTEAMS("connector\_microsoftteams")

CONNECTOR\_OUTLOOKCALENDAR("connector\_outlookcalendar")

CONNECTOR\_OUTLOOKEMAIL("connector\_outlookemail")

CONNECTOR\_SHAREPOINT("connector\_sharepoint")

Optional<Boolean> deferLoading

Whether this MCP tool is deferred and discovered via tool search.

Optional<Headers> headers

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

Optional<RequireApproval> requireApproval

Specify which of the MCP server’s tools require approval.

One of the following:

class McpToolApprovalFilter:

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

Optional<Always> always

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

Optional<Never> never

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

enum McpToolApprovalSetting:

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

ALWAYS("always")

NEVER("never")

Optional<String> serverDescription

Optional description of the MCP server, used to provide more context.

Optional<String> serverUrl

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

Optional<String> tunnelId

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

CodeInterpreter

Container container

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

One of the following:

String

class CodeInterpreterToolAuto:

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

JsonValue; type "auto"constant"auto"constant

Always `auto`.

Optional<List<String>> fileIds

An optional list of uploaded files to make available to your code.

Optional<MemoryLimit> memoryLimit

The memory limit for the code interpreter container.

One of the following:

\_1G("1g")

\_4G("4g")

\_16G("16g")

\_64G("64g")

Optional<NetworkPolicy> networkPolicy

Network access policy for the container.

One of the following:

class ContainerNetworkPolicyDisabled:

JsonValue; type "disabled"constant"disabled"constant

Disable outbound network access. Always `disabled`.

class ContainerNetworkPolicyAllowlist:

List<String> allowedDomains

A list of allowed domains when type is `allowlist`.

JsonValue; type "allowlist"constant"allowlist"constant

Allow outbound network access only to specified domains. Always `allowlist`.

Optional<List<[ContainerNetworkPolicyDomainSecret](/api/reference/java/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema))>> domainSecrets

Optional domain-scoped secrets for allowlisted domains.

String domain

The domain associated with the secret.

minLength1

String name

The name of the secret to inject for the domain.

minLength1

String value

The secret value to inject for the domain.

maxLength10485760

minLength1

JsonValue; type "code\_interpreter"constant"code\_interpreter"constant

The type of the code interpreter tool. Always `code_interpreter`.

ImageGeneration

JsonValue; type "image\_generation"constant"image\_generation"constant

The type of the image generation tool. Always `image_generation`.

Optional<Action> action

Whether to generate a new image or edit an existing image. Default: `auto`.

One of the following:

GENERATE("generate")

EDIT("edit")

AUTO("auto")

Optional<Background> background

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

TRANSPARENT("transparent")

OPAQUE("opaque")

AUTO("auto")

Optional<InputFidelity> inputFidelity

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

One of the following:

HIGH("high")

LOW("low")

Optional<InputImageMask> inputImageMask

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

Optional<String> fileId

File ID for the mask image.

Optional<String> imageUrl

Base64-encoded mask image.

Optional<Model> model

The image generation model to use. Default: `gpt-image-1`.

One of the following:

GPT\_IMAGE\_1("gpt-image-1")

GPT\_IMAGE\_1\_MINI("gpt-image-1-mini")

GPT\_IMAGE\_2("gpt-image-2")

GPT\_IMAGE\_2\_2026\_04\_21("gpt-image-2-2026-04-21")

GPT\_IMAGE\_1\_5("gpt-image-1.5")

CHATGPT\_IMAGE\_LATEST("chatgpt-image-latest")

Optional<Moderation> moderation

Moderation level for the generated image. Default: `auto`.

One of the following:

AUTO("auto")

LOW("low")

Optional<Long> outputCompression

Compression level for the output image. Default: 100.

minimum0

maximum100

Optional<OutputFormat> outputFormat

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

One of the following:

PNG("png")

WEBP("webp")

JPEG("jpeg")

Optional<Long> partialImages

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

Optional<Quality> quality

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

One of the following:

LOW("low")

MEDIUM("medium")

HIGH("high")

AUTO("auto")

Optional<Size> size

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

One of the following:

\_1024X1024("1024x1024")

\_1024X1536("1024x1536")

\_1536X1024("1536x1024")

AUTO("auto")

JsonValue;

JsonValue; type "local\_shell"constant"local\_shell"constant

The type of the local shell tool. Always `local_shell`.

class FunctionShellTool:

A tool that allows the model to execute shell commands.

JsonValue; type "shell"constant"shell"constant

The type of the shell tool. Always `shell`.

Optional<Environment> environment

One of the following:

class ContainerAuto:

JsonValue; type "container\_auto"constant"container\_auto"constant

Automatically creates a container for this request

Optional<List<String>> fileIds

An optional list of uploaded files to make available to your code.

Optional<MemoryLimit> memoryLimit

The memory limit for the container.

One of the following:

\_1G("1g")

\_4G("4g")

\_16G("16g")

\_64G("64g")

Optional<NetworkPolicy> networkPolicy

Network access policy for the container.

One of the following:

class ContainerNetworkPolicyDisabled:

JsonValue; type "disabled"constant"disabled"constant

Disable outbound network access. Always `disabled`.

class ContainerNetworkPolicyAllowlist:

List<String> allowedDomains

A list of allowed domains when type is `allowlist`.

JsonValue; type "allowlist"constant"allowlist"constant

Allow outbound network access only to specified domains. Always `allowlist`.

Optional<List<[ContainerNetworkPolicyDomainSecret](/api/reference/java/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema))>> domainSecrets

Optional domain-scoped secrets for allowlisted domains.

String domain

The domain associated with the secret.

minLength1

String name

The name of the secret to inject for the domain.

minLength1

String value

The secret value to inject for the domain.

maxLength10485760

minLength1

Optional<List<Skill>> skills

An optional list of skills referenced by id or inline data.

One of the following:

class SkillReference:

String skillId

The ID of the referenced skill.

maxLength64

minLength1

JsonValue; type "skill\_reference"constant"skill\_reference"constant

References a skill created with the /v1/skills endpoint.

Optional<String> version

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

class InlineSkill:

String description

The description of the skill.

String name

The name of the skill.

[InlineSkillSource](/api/reference/java/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill_source%20%3E%20(schema)) source

Inline skill payload

JsonValue; type "inline"constant"inline"constant

Defines an inline skill for this request.

class LocalEnvironment:

JsonValue; type "local"constant"local"constant

Use a local computer environment.

Optional<List<[LocalSkill](/api/reference/java/resources/responses#(resource)%20responses%20%3E%20(model)%20local_skill%20%3E%20(schema))>> skills

An optional list of skills.

String description

The description of the skill.

String name

The name of the skill.

String path

The path to the directory containing the skill.

class ContainerReference:

String containerId

The ID of the referenced container.

JsonValue; type "container\_reference"constant"container\_reference"constant

References a container created with the /v1/containers endpoint

class CustomTool:

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

String name

The name of the custom tool, used to identify it in tool calls.

JsonValue; type "custom"constant"custom"constant

The type of the custom tool. Always `custom`.

Optional<Boolean> deferLoading

Whether this tool should be deferred and discovered via tool search.

Optional<String> description

Optional description of the custom tool, used to provide more context.

Optional<[CustomToolInputFormat](/api/reference/java/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))> format

The input format for the custom tool. Default is unconstrained text.

class NamespaceTool:

Groups function/custom tools under a shared namespace.

String description

A description of the namespace shown to the model.

minLength1

String name

The namespace name used in tool calls (for example, `crm`).

minLength1

List<Tool> tools

The function/custom tools available inside this namespace.

One of the following:

class Function:

String name

maxLength128

minLength1

JsonValue; type "function"constant"function"constant

Optional<Boolean> deferLoading

Whether this function should be deferred and discovered via tool search.

Optional<String> description

Optional<JsonValue> parameters

Optional<Boolean> strict

class CustomTool:

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

String name

The name of the custom tool, used to identify it in tool calls.

JsonValue; type "custom"constant"custom"constant

The type of the custom tool. Always `custom`.

Optional<Boolean> deferLoading

Whether this tool should be deferred and discovered via tool search.

Optional<String> description

Optional description of the custom tool, used to provide more context.

Optional<[CustomToolInputFormat](/api/reference/java/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))> format

The input format for the custom tool. Default is unconstrained text.

JsonValue; type "namespace"constant"namespace"constant

The type of the tool. Always `namespace`.

class ToolSearchTool:

Hosted or BYOT tool search configuration for deferred tools.

JsonValue; type "tool\_search"constant"tool\_search"constant

The type of the tool. Always `tool_search`.

Optional<String> description

Description shown to the model for a client-executed tool search tool.

Optional<Execution> execution

Whether tool search is executed by the server or by the client.

One of the following:

SERVER("server")

CLIENT("client")

Optional<JsonValue> parameters

Parameter schema for a client-executed tool search tool.

class WebSearchPreviewTool:

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type type

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

One of the following:

WEB\_SEARCH\_PREVIEW("web\_search\_preview")

WEB\_SEARCH\_PREVIEW\_2025\_03\_11("web\_search\_preview\_2025\_03\_11")

Optional<List<SearchContentType>> searchContentTypes

One of the following:

TEXT("text")

IMAGE("image")

Optional<SearchContextSize> searchContextSize

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

LOW("low")

MEDIUM("medium")

HIGH("high")

Optional<UserLocation> userLocation

The user’s location.

JsonValue; type "approximate"constant"approximate"constant

The type of location approximation. Always `approximate`.

Optional<String> city

Free text input for the city of the user, e.g. `San Francisco`.

Optional<String> country

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

Optional<String> region

Free text input for the region of the user, e.g. `California`.

Optional<String> timezone

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

class ApplyPatchTool:

Allows the assistant to create, delete, or update files using unified diffs.

JsonValue; type "apply\_patch"constant"apply\_patch"constant

The type of the tool. Always `apply_patch`.

JsonValue; type "tool\_search\_output"constant"tool\_search\_output"constant

The type of the item. Always `tool_search_output`.

Optional<String> createdBy

The identifier of the actor that created the item.

AdditionalTools

String id

The unique ID of the additional tools item.

Role role

The role that provided the additional tools.

One of the following:

UNKNOWN("unknown")

USER("user")

ASSISTANT("assistant")

SYSTEM("system")

CRITIC("critic")

DISCRIMINATOR("discriminator")

DEVELOPER("developer")

TOOL("tool")

List<[Tool](/api/reference/java/resources/responses#(resource)%20responses%20%3E%20(model)%20tool%20%3E%20(schema))> tools

The additional tool definitions made available at this item.

One of the following:

class FunctionTool:

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

String name

The name of the function to call.

Optional<Parameters> parameters

A JSON schema object describing the parameters of the function.

Optional<Boolean> strict

Whether to enforce strict parameter validation. Default `true`.

JsonValue; type "function"constant"function"constant

The type of the function tool. Always `function`.

Optional<Boolean> deferLoading

Whether this function is deferred and loaded via tool search.

Optional<String> description

A description of the function. Used by the model to determine whether or not to call the function.

class FileSearchTool:

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

JsonValue; type "file\_search"constant"file\_search"constant

The type of the file search tool. Always `file_search`.

List<String> vectorStoreIds

The IDs of the vector stores to search.

Optional<Filters> filters

A filter to apply.

One of the following:

class ComparisonFilter:

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

String key

The key to compare against the value.

Type type

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

EQ("eq")

NE("ne")

GT("gt")

GTE("gte")

LT("lt")

LTE("lte")

IN("in")

NIN("nin")

Value value

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

String

double

boolean

List<ComparisonFilterValueItem>

One of the following:

String

double

class CompoundFilter:

Combine multiple filters using `and` or `or`.

List<Filter> filters

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

One of the following:

class ComparisonFilter:

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

String key

The key to compare against the value.

Type type

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

EQ("eq")

NE("ne")

GT("gt")

GTE("gte")

LT("lt")

LTE("lte")

IN("in")

NIN("nin")

Value value

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

String

double

boolean

List<ComparisonFilterValueItem>

One of the following:

String

double

JsonValue

Type type

Type of operation: `and` or `or`.

One of the following:

AND("and")

OR("or")

Optional<Long> maxNumResults

The maximum number of results to return. This number should be between 1 and 50 inclusive.

Optional<RankingOptions> rankingOptions

Ranking options for search.

Optional<HybridSearch> hybridSearch

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

double embeddingWeight

The weight of the embedding in the reciprocal ranking fusion.

double textWeight

The weight of the text in the reciprocal ranking fusion.

Optional<Ranker> ranker

The ranker to use for the file search.

One of the following:

AUTO("auto")

DEFAULT\_2024\_11\_15("default-2024-11-15")

Optional<Double> scoreThreshold

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

class ComputerTool:

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

JsonValue; type "computer"constant"computer"constant

The type of the computer tool. Always `computer`.

class ComputerUsePreviewTool:

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

long displayHeight

The height of the computer display.

long displayWidth

The width of the computer display.

Environment environment

The type of computer environment to control.

One of the following:

WINDOWS("windows")

MAC("mac")

LINUX("linux")

UBUNTU("ubuntu")

BROWSER("browser")

JsonValue; type "computer\_use\_preview"constant"computer\_use\_preview"constant

The type of the computer use tool. Always `computer_use_preview`.

class WebSearchTool:

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type type

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

One of the following:

WEB\_SEARCH("web\_search")

WEB\_SEARCH\_2025\_08\_26("web\_search\_2025\_08\_26")

Optional<Filters> filters

Filters for the search.

Optional<List<String>> allowedDomains

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

Optional<SearchContextSize> searchContextSize

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

LOW("low")

MEDIUM("medium")

HIGH("high")

Optional<UserLocation> userLocation

The approximate location of the user.

Optional<String> city

Free text input for the city of the user, e.g. `San Francisco`.

Optional<String> country

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

Optional<String> region

Free text input for the region of the user, e.g. `California`.

Optional<String> timezone

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

Optional<Type> type

The type of location approximation. Always `approximate`.

Mcp

String serverLabel

A label for this MCP server, used to identify it in tool calls.

JsonValue; type "mcp"constant"mcp"constant

The type of the MCP tool. Always `mcp`.

Optional<AllowedTools> allowedTools

List of allowed tool names or a filter object.

One of the following:

List<String>

class McpToolFilter:

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

Optional<String> authorization

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

Optional<ConnectorId> connectorId

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

CONNECTOR\_DROPBOX("connector\_dropbox")

CONNECTOR\_GMAIL("connector\_gmail")

CONNECTOR\_GOOGLECALENDAR("connector\_googlecalendar")

CONNECTOR\_GOOGLEDRIVE("connector\_googledrive")

CONNECTOR\_MICROSOFTTEAMS("connector\_microsoftteams")

CONNECTOR\_OUTLOOKCALENDAR("connector\_outlookcalendar")

CONNECTOR\_OUTLOOKEMAIL("connector\_outlookemail")

CONNECTOR\_SHAREPOINT("connector\_sharepoint")

Optional<Boolean> deferLoading

Whether this MCP tool is deferred and discovered via tool search.

Optional<Headers> headers

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

Optional<RequireApproval> requireApproval

Specify which of the MCP server’s tools require approval.

One of the following:

class McpToolApprovalFilter:

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

Optional<Always> always

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

Optional<Never> never

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

enum McpToolApprovalSetting:

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

ALWAYS("always")

NEVER("never")

Optional<String> serverDescription

Optional description of the MCP server, used to provide more context.

Optional<String> serverUrl

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

Optional<String> tunnelId

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

CodeInterpreter

Container container

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

One of the following:

String

class CodeInterpreterToolAuto:

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

JsonValue; type "auto"constant"auto"constant

Always `auto`.

Optional<List<String>> fileIds

An optional list of uploaded files to make available to your code.

Optional<MemoryLimit> memoryLimit

The memory limit for the code interpreter container.

One of the following:

\_1G("1g")

\_4G("4g")

\_16G("16g")

\_64G("64g")

Optional<NetworkPolicy> networkPolicy

Network access policy for the container.

One of the following:

class ContainerNetworkPolicyDisabled:

JsonValue; type "disabled"constant"disabled"constant

Disable outbound network access. Always `disabled`.

class ContainerNetworkPolicyAllowlist:

List<String> allowedDomains

A list of allowed domains when type is `allowlist`.

JsonValue; type "allowlist"constant"allowlist"constant

Allow outbound network access only to specified domains. Always `allowlist`.

Optional<List<[ContainerNetworkPolicyDomainSecret](/api/reference/java/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema))>> domainSecrets

Optional domain-scoped secrets for allowlisted domains.

String domain

The domain associated with the secret.

minLength1

String name

The name of the secret to inject for the domain.

minLength1

String value

The secret value to inject for the domain.

maxLength10485760

minLength1

JsonValue; type "code\_interpreter"constant"code\_interpreter"constant

The type of the code interpreter tool. Always `code_interpreter`.

ImageGeneration

JsonValue; type "image\_generation"constant"image\_generation"constant

The type of the image generation tool. Always `image_generation`.

Optional<Action> action

Whether to generate a new image or edit an existing image. Default: `auto`.

One of the following:

GENERATE("generate")

EDIT("edit")

AUTO("auto")

Optional<Background> background

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

TRANSPARENT("transparent")

OPAQUE("opaque")

AUTO("auto")

Optional<InputFidelity> inputFidelity

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

One of the following:

HIGH("high")

LOW("low")

Optional<InputImageMask> inputImageMask

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

Optional<String> fileId

File ID for the mask image.

Optional<String> imageUrl

Base64-encoded mask image.

Optional<Model> model

The image generation model to use. Default: `gpt-image-1`.

One of the following:

GPT\_IMAGE\_1("gpt-image-1")

GPT\_IMAGE\_1\_MINI("gpt-image-1-mini")

GPT\_IMAGE\_2("gpt-image-2")

GPT\_IMAGE\_2\_2026\_04\_21("gpt-image-2-2026-04-21")

GPT\_IMAGE\_1\_5("gpt-image-1.5")

CHATGPT\_IMAGE\_LATEST("chatgpt-image-latest")

Optional<Moderation> moderation

Moderation level for the generated image. Default: `auto`.

One of the following:

AUTO("auto")

LOW("low")

Optional<Long> outputCompression

Compression level for the output image. Default: 100.

minimum0

maximum100

Optional<OutputFormat> outputFormat

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

One of the following:

PNG("png")

WEBP("webp")

JPEG("jpeg")

Optional<Long> partialImages

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

Optional<Quality> quality

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

One of the following:

LOW("low")

MEDIUM("medium")

HIGH("high")

AUTO("auto")

Optional<Size> size

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

One of the following:

\_1024X1024("1024x1024")

\_1024X1536("1024x1536")

\_1536X1024("1536x1024")

AUTO("auto")

JsonValue;

JsonValue; type "local\_shell"constant"local\_shell"constant

The type of the local shell tool. Always `local_shell`.

class FunctionShellTool:

A tool that allows the model to execute shell commands.

JsonValue; type "shell"constant"shell"constant

The type of the shell tool. Always `shell`.

Optional<Environment> environment

One of the following:

class ContainerAuto:

JsonValue; type "container\_auto"constant"container\_auto"constant

Automatically creates a container for this request

Optional<List<String>> fileIds

An optional list of uploaded files to make available to your code.

Optional<MemoryLimit> memoryLimit

The memory limit for the container.

One of the following:

\_1G("1g")

\_4G("4g")

\_16G("16g")

\_64G("64g")

Optional<NetworkPolicy> networkPolicy

Network access policy for the container.

One of the following:

class ContainerNetworkPolicyDisabled:

JsonValue; type "disabled"constant"disabled"constant

Disable outbound network access. Always `disabled`.

class ContainerNetworkPolicyAllowlist:

List<String> allowedDomains

A list of allowed domains when type is `allowlist`.

JsonValue; type "allowlist"constant"allowlist"constant

Allow outbound network access only to specified domains. Always `allowlist`.

Optional<List<[ContainerNetworkPolicyDomainSecret](/api/reference/java/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema))>> domainSecrets

Optional domain-scoped secrets for allowlisted domains.

String domain

The domain associated with the secret.

minLength1

String name

The name of the secret to inject for the domain.

minLength1

String value

The secret value to inject for the domain.

maxLength10485760

minLength1

Optional<List<Skill>> skills

An optional list of skills referenced by id or inline data.

One of the following:

class SkillReference:

String skillId

The ID of the referenced skill.

maxLength64

minLength1

JsonValue; type "skill\_reference"constant"skill\_reference"constant

References a skill created with the /v1/skills endpoint.

Optional<String> version

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

class InlineSkill:

String description

The description of the skill.

String name

The name of the skill.

[InlineSkillSource](/api/reference/java/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill_source%20%3E%20(schema)) source

Inline skill payload

JsonValue; type "inline"constant"inline"constant

Defines an inline skill for this request.

class LocalEnvironment:

JsonValue; type "local"constant"local"constant

Use a local computer environment.

Optional<List<[LocalSkill](/api/reference/java/resources/responses#(resource)%20responses%20%3E%20(model)%20local_skill%20%3E%20(schema))>> skills

An optional list of skills.

String description

The description of the skill.

String name

The name of the skill.

String path

The path to the directory containing the skill.

class ContainerReference:

String containerId

The ID of the referenced container.

JsonValue; type "container\_reference"constant"container\_reference"constant

References a container created with the /v1/containers endpoint

class CustomTool:

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

String name

The name of the custom tool, used to identify it in tool calls.

JsonValue; type "custom"constant"custom"constant

The type of the custom tool. Always `custom`.

Optional<Boolean> deferLoading

Whether this tool should be deferred and discovered via tool search.

Optional<String> description

Optional description of the custom tool, used to provide more context.

Optional<[CustomToolInputFormat](/api/reference/java/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))> format

The input format for the custom tool. Default is unconstrained text.

class NamespaceTool:

Groups function/custom tools under a shared namespace.

String description

A description of the namespace shown to the model.

minLength1

String name

The namespace name used in tool calls (for example, `crm`).

minLength1

List<Tool> tools

The function/custom tools available inside this namespace.

One of the following:

class Function:

String name

maxLength128

minLength1

JsonValue; type "function"constant"function"constant

Optional<Boolean> deferLoading

Whether this function should be deferred and discovered via tool search.

Optional<String> description

Optional<JsonValue> parameters

Optional<Boolean> strict

class CustomTool:

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

String name

The name of the custom tool, used to identify it in tool calls.

JsonValue; type "custom"constant"custom"constant

The type of the custom tool. Always `custom`.

Optional<Boolean> deferLoading

Whether this tool should be deferred and discovered via tool search.

Optional<String> description

Optional description of the custom tool, used to provide more context.

Optional<[CustomToolInputFormat](/api/reference/java/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))> format

The input format for the custom tool. Default is unconstrained text.

JsonValue; type "namespace"constant"namespace"constant

The type of the tool. Always `namespace`.

class ToolSearchTool:

Hosted or BYOT tool search configuration for deferred tools.

JsonValue; type "tool\_search"constant"tool\_search"constant

The type of the tool. Always `tool_search`.

Optional<String> description

Description shown to the model for a client-executed tool search tool.

Optional<Execution> execution

Whether tool search is executed by the server or by the client.

One of the following:

SERVER("server")

CLIENT("client")

Optional<JsonValue> parameters

Parameter schema for a client-executed tool search tool.

class WebSearchPreviewTool:

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type type

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

One of the following:

WEB\_SEARCH\_PREVIEW("web\_search\_preview")

WEB\_SEARCH\_PREVIEW\_2025\_03\_11("web\_search\_preview\_2025\_03\_11")

Optional<List<SearchContentType>> searchContentTypes

One of the following:

TEXT("text")

IMAGE("image")

Optional<SearchContextSize> searchContextSize

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

LOW("low")

MEDIUM("medium")

HIGH("high")

Optional<UserLocation> userLocation

The user’s location.

JsonValue; type "approximate"constant"approximate"constant

The type of location approximation. Always `approximate`.

Optional<String> city

Free text input for the city of the user, e.g. `San Francisco`.

Optional<String> country

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

Optional<String> region

Free text input for the region of the user, e.g. `California`.

Optional<String> timezone

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

class ApplyPatchTool:

Allows the assistant to create, delete, or update files using unified diffs.

JsonValue; type "apply\_patch"constant"apply\_patch"constant

The type of the tool. Always `apply_patch`.

JsonValue; type "additional\_tools"constant"additional\_tools"constant

The type of the item. Always `additional_tools`.

class ResponseReasoningItem:

A description of the chain of thought used by a reasoning model while generating
a response. Be sure to include these items in your `input` to the Responses API
for subsequent turns of a conversation if you are manually
[managing context](https://platform.openai.com/docs/guides/conversation-state).

String id

The unique identifier of the reasoning content.

List<Summary> summary

Reasoning summary content.

String text

A summary of the reasoning output from the model so far.

JsonValue; type "summary\_text"constant"summary\_text"constant

The type of the object. Always `summary_text`.

JsonValue; type "reasoning"constant"reasoning"constant

The type of the object. Always `reasoning`.

Optional<List<Content>> content

Reasoning text content.

String text

The reasoning text from the model.

JsonValue; type "reasoning\_text"constant"reasoning\_text"constant

The type of the reasoning text. Always `reasoning_text`.

Optional<String> encryptedContent

The encrypted content of the reasoning item - populated when a response is
generated with `reasoning.encrypted_content` in the `include` parameter.

Optional<Status> status

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

One of the following:

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

class ResponseCompactionItem:

A compaction item generated by the [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).

String id

The unique ID of the compaction item.

String encryptedContent

The encrypted content that was produced by compaction.

JsonValue; type "compaction"constant"compaction"constant

The type of the item. Always `compaction`.

Optional<String> createdBy

The identifier of the actor that created the item.

class ResponseCodeInterpreterToolCall:

A tool call to run code.

String id

The unique ID of the code interpreter tool call.

Optional<String> code

The code to run, or null if not available.

String containerId

The ID of the container used to run the code.

Optional<List<Output>> outputs

The outputs generated by the code interpreter, such as logs or images.
Can be null if no outputs are available.

One of the following:

class Logs:

The logs output from the code interpreter.

String logs

The logs output from the code interpreter.

JsonValue; type "logs"constant"logs"constant

The type of the output. Always `logs`.

class Image:

The image output from the code interpreter.

JsonValue; type "image"constant"image"constant

The type of the output. Always `image`.

String url

The URL of the image output from the code interpreter.

formaturi

Status status

The status of the code interpreter tool call. Valid values are `in_progress`, `completed`, `incomplete`, `interpreting`, and `failed`.

One of the following:

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

INTERPRETING("interpreting")

FAILED("failed")

JsonValue; type "code\_interpreter\_call"constant"code\_interpreter\_call"constant

The type of the code interpreter tool call. Always `code_interpreter_call`.

LocalShellCall

String id

The unique ID of the local shell call.

Action action

Execute a shell command on the server.

List<String> command

The command to run.

Env env

Environment variables to set for the command.

JsonValue; type "exec"constant"exec"constant

The type of the local shell action. Always `exec`.

Optional<Long> timeoutMs

Optional timeout in milliseconds for the command.

Optional<String> user

Optional user to run the command as.

Optional<String> workingDirectory

Optional working directory to run the command in.

String callId

The unique ID of the local shell tool call generated by the model.

Status status

The status of the local shell call.

One of the following:

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

JsonValue; type "local\_shell\_call"constant"local\_shell\_call"constant

The type of the local shell call. Always `local_shell_call`.

LocalShellCallOutput

String id

The unique ID of the local shell tool call generated by the model.

String output

A JSON string of the output of the local shell tool call.

JsonValue; type "local\_shell\_call\_output"constant"local\_shell\_call\_output"constant

The type of the local shell tool call output. Always `local_shell_call_output`.

Optional<Status> status

The status of the item. One of `in_progress`, `completed`, or `incomplete`.

One of the following:

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

class ResponseFunctionShellToolCall:

A tool call that executes one or more shell commands in a managed environment.

String id

The unique ID of the shell tool call. Populated when this item is returned via API.

Action action

The shell commands and limits that describe how to run the tool call.

List<String> commands

Optional<Long> maxOutputLength

Optional maximum number of characters to return from each command.

Optional<Long> timeoutMs

Optional timeout in milliseconds for the commands.

String callId

The unique ID of the shell tool call generated by the model.

Optional<Environment> environment

Represents the use of a local environment to perform shell actions.

One of the following:

class ResponseLocalEnvironment:

Represents the use of a local environment to perform shell actions.

JsonValue; type "local"constant"local"constant

The environment type. Always `local`.

class ResponseContainerReference:

Represents a container created with /v1/containers.

String containerId

JsonValue; type "container\_reference"constant"container\_reference"constant

The environment type. Always `container_reference`.

Status status

The status of the shell call. One of `in_progress`, `completed`, or `incomplete`.

One of the following:

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

JsonValue; type "shell\_call"constant"shell\_call"constant

The type of the item. Always `shell_call`.

Optional<String> createdBy

The ID of the entity that created this tool call.

class ResponseFunctionShellToolCallOutput:

The output of a shell tool call that was emitted.

String id

The unique ID of the shell call output. Populated when this item is returned via API.

String callId

The unique ID of the shell tool call generated by the model.

Optional<Long> maxOutputLength

The maximum length of the shell command output. This is generated by the model and should be passed back with the raw output.

List<Output> output

An array of shell call output contents

Outcome outcome

Represents either an exit outcome (with an exit code) or a timeout outcome for a shell call output chunk.

One of the following:

JsonValue;

JsonValue; type "timeout"constant"timeout"constant

The outcome type. Always `timeout`.

class Exit:

Indicates that the shell commands finished and returned an exit code.

long exitCode

Exit code from the shell process.

JsonValue; type "exit"constant"exit"constant

The outcome type. Always `exit`.

String stderr

The standard error output that was captured.

String stdout

The standard output that was captured.

Optional<String> createdBy

The identifier of the actor that created the item.

Status status

The status of the shell call output. One of `in_progress`, `completed`, or `incomplete`.

One of the following:

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

JsonValue; type "shell\_call\_output"constant"shell\_call\_output"constant

The type of the shell call output. Always `shell_call_output`.

Optional<String> createdBy

The identifier of the actor that created the item.

class ResponseApplyPatchToolCall:

A tool call that applies file diffs by creating, deleting, or updating files.

String id

The unique ID of the apply patch tool call. Populated when this item is returned via API.

String callId

The unique ID of the apply patch tool call generated by the model.

Operation operation

One of the create\_file, delete\_file, or update\_file operations applied via apply\_patch.

One of the following:

class CreateFile:

Instruction describing how to create a file via the apply\_patch tool.

String diff

Diff to apply.

String path

Path of the file to create.

JsonValue; type "create\_file"constant"create\_file"constant

Create a new file with the provided diff.

class DeleteFile:

Instruction describing how to delete a file via the apply\_patch tool.

String path

Path of the file to delete.

JsonValue; type "delete\_file"constant"delete\_file"constant

Delete the specified file.

class UpdateFile:

Instruction describing how to update a file via the apply\_patch tool.

String diff

Diff to apply.

String path

Path of the file to update.

JsonValue; type "update\_file"constant"update\_file"constant

Update an existing file with the provided diff.

Status status

The status of the apply patch tool call. One of `in_progress` or `completed`.

One of the following:

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

JsonValue; type "apply\_patch\_call"constant"apply\_patch\_call"constant

The type of the item. Always `apply_patch_call`.

Optional<String> createdBy

The ID of the entity that created this tool call.

class ResponseApplyPatchToolCallOutput:

The output emitted by an apply patch tool call.

String id

The unique ID of the apply patch tool call output. Populated when this item is returned via API.

String callId

The unique ID of the apply patch tool call generated by the model.

Status status

The status of the apply patch tool call output. One of `completed` or `failed`.

One of the following:

COMPLETED("completed")

FAILED("failed")

JsonValue; type "apply\_patch\_call\_output"constant"apply\_patch\_call\_output"constant

The type of the item. Always `apply_patch_call_output`.

Optional<String> createdBy

The ID of the entity that created this tool call output.

Optional<String> output

Optional textual output returned by the apply patch tool.

McpListTools

String id

The unique ID of the list.

String serverLabel

The label of the MCP server.

List<Tool> tools

The tools available on the server.

JsonValue inputSchema

The JSON schema describing the tool’s input.

String name

The name of the tool.

Optional<JsonValue> annotations

Additional annotations about the tool.

Optional<String> description

The description of the tool.

JsonValue; type "mcp\_list\_tools"constant"mcp\_list\_tools"constant

The type of the item. Always `mcp_list_tools`.

Optional<String> error

Error message if the server could not list tools.

McpApprovalRequest

String id

The unique ID of the approval request.

String arguments

A JSON string of arguments for the tool.

String name

The name of the tool to run.

String serverLabel

The label of the MCP server making the request.

JsonValue; type "mcp\_approval\_request"constant"mcp\_approval\_request"constant

The type of the item. Always `mcp_approval_request`.

McpApprovalResponse

String id

The unique ID of the approval response

String approvalRequestId

The ID of the approval request being answered.

boolean approve

Whether the request was approved.

JsonValue; type "mcp\_approval\_response"constant"mcp\_approval\_response"constant

The type of the item. Always `mcp_approval_response`.

Optional<String> reason

Optional reason for the decision.

McpCall

String id

The unique ID of the tool call.

String arguments

A JSON string of the arguments passed to the tool.

String name

The name of the tool that was run.

String serverLabel

The label of the MCP server running the tool.

JsonValue; type "mcp\_call"constant"mcp\_call"constant

The type of the item. Always `mcp_call`.

Optional<String> approvalRequestId

Unique identifier for the MCP tool call approval request.
Include this value in a subsequent `mcp_approval_response` input to approve or reject the corresponding tool call.

Optional<String> error

The error from the tool call, if any.

Optional<String> output

The output from the tool call.

Optional<Status> status

The status of the tool call. One of `in_progress`, `completed`, `incomplete`, `calling`, or `failed`.

One of the following:

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

CALLING("calling")

FAILED("failed")

class ResponseCustomToolCall:

A call to a custom tool created by the model.

String callId

An identifier used to map this custom tool call to a tool call output.

String input

The input for the custom tool call generated by the model.

String name

The name of the custom tool being called.

JsonValue; type "custom\_tool\_call"constant"custom\_tool\_call"constant

The type of the custom tool call. Always `custom_tool_call`.

Optional<String> id

The unique ID of the custom tool call in the OpenAI platform.

Optional<String> namespace

The namespace of the custom tool being called.

class ResponseCustomToolCallOutput:

The output of a custom tool call from your code, being sent back to the model.

String callId

The call ID, used to map this custom tool call output to a custom tool call.

Output output

The output from the custom tool call generated by your code.
Can be a string or an list of output content.

One of the following:

String

List<FunctionAndCustomToolCallOutput>

One of the following:

class ResponseInputText:

A text input to the model.

String text

The text input to the model.

JsonValue; type "input\_text"constant"input\_text"constant

The type of the input item. Always `input_text`.

class ResponseInputImage:

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

Detail detail

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

One of the following:

LOW("low")

HIGH("high")

AUTO("auto")

ORIGINAL("original")

JsonValue; type "input\_image"constant"input\_image"constant

The type of the input item. Always `input_image`.

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> imageUrl

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

class ResponseInputFile:

A file input to the model.

JsonValue; type "input\_file"constant"input\_file"constant

The type of the input item. Always `input_file`.

Optional<Detail> detail

The detail level of the file to be sent to the model. Use `low` for the default rendering behavior, or `high` to render the file at higher quality. Defaults to `low`.

One of the following:

LOW("low")

HIGH("high")

Optional<String> fileData

The content of the file to be sent to the model.

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> fileUrl

The URL of the file to be sent to the model.

formaturi

Optional<String> filename

The name of the file to be sent to the model.

JsonValue; type "custom\_tool\_call\_output"constant"custom\_tool\_call\_output"constant

The type of the custom tool call output. Always `custom_tool_call_output`.

Optional<String> id

The unique ID of the custom tool call output in the OpenAI platform.

class ConversationItemList:

A list of Conversation items.

List<[ConversationItem](/api/reference/java/resources/conversations#(resource)%20conversations.items%20%3E%20(model)%20conversation_item%20%3E%20(schema))> data

A list of conversation items.

One of the following:

class Message:

A message to or from the model.

String id

The unique ID of the message.

List<Content> content

The content of the message

One of the following:

class ResponseInputText:

A text input to the model.

String text

The text input to the model.

JsonValue; type "input\_text"constant"input\_text"constant

The type of the input item. Always `input_text`.

class ResponseOutputText:

A text output from the model.

List<Annotation> annotations

The annotations of the text output.

One of the following:

class FileCitation:

A citation to a file.

String fileId

The ID of the file.

String filename

The filename of the file cited.

long index

The index of the file in the list of files.

JsonValue; type "file\_citation"constant"file\_citation"constant

The type of the file citation. Always `file_citation`.

class UrlCitation:

A citation for a web resource used to generate a model response.

long endIndex

The index of the last character of the URL citation in the message.

long startIndex

The index of the first character of the URL citation in the message.

String title

The title of the web resource.

JsonValue; type "url\_citation"constant"url\_citation"constant

The type of the URL citation. Always `url_citation`.

String url

The URL of the web resource.

formaturi

class ContainerFileCitation:

A citation for a container file used to generate a model response.

String containerId

The ID of the container file.

long endIndex

The index of the last character of the container file citation in the message.

String fileId

The ID of the file.

String filename

The filename of the container file cited.

long startIndex

The index of the first character of the container file citation in the message.

JsonValue; type "container\_file\_citation"constant"container\_file\_citation"constant

The type of the container file citation. Always `container_file_citation`.

class FilePath:

A path to a file.

String fileId

The ID of the file.

long index

The index of the file in the list of files.

JsonValue; type "file\_path"constant"file\_path"constant

The type of the file path. Always `file_path`.

String text

The text output from the model.

JsonValue; type "output\_text"constant"output\_text"constant

The type of the output text. Always `output_text`.

Optional<List<Logprob>> logprobs

String token

List<long> bytes

double logprob

List<TopLogprob> topLogprobs

String token

List<long> bytes

double logprob

class TextContent:

A text content.

String text

JsonValue; type "text"constant"text"constant

class SummaryTextContent:

A summary text from the model.

String text

A summary of the reasoning output from the model so far.

JsonValue; type "summary\_text"constant"summary\_text"constant

The type of the object. Always `summary_text`.

class ReasoningText:

Reasoning text from the model.

String text

The reasoning text from the model.

JsonValue; type "reasoning\_text"constant"reasoning\_text"constant

The type of the reasoning text. Always `reasoning_text`.

class ResponseOutputRefusal:

A refusal from the model.

String refusal

The refusal explanation from the model.

JsonValue; type "refusal"constant"refusal"constant

The type of the refusal. Always `refusal`.

class ResponseInputImage:

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

Detail detail

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

One of the following:

LOW("low")

HIGH("high")

AUTO("auto")

ORIGINAL("original")

JsonValue; type "input\_image"constant"input\_image"constant

The type of the input item. Always `input_image`.

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> imageUrl

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

class ComputerScreenshotContent:

A screenshot of a computer.

Detail detail

The detail level of the screenshot image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

One of the following:

LOW("low")

HIGH("high")

AUTO("auto")

ORIGINAL("original")

Optional<String> fileId

The identifier of an uploaded file that contains the screenshot.

Optional<String> imageUrl

The URL of the screenshot image.

formaturi

JsonValue; type "computer\_screenshot"constant"computer\_screenshot"constant

Specifies the event type. For a computer screenshot, this property is always set to `computer_screenshot`.

class ResponseInputFile:

A file input to the model.

JsonValue; type "input\_file"constant"input\_file"constant

The type of the input item. Always `input_file`.

Optional<Detail> detail

The detail level of the file to be sent to the model. Use `low` for the default rendering behavior, or `high` to render the file at higher quality. Defaults to `low`.

One of the following:

LOW("low")

HIGH("high")

Optional<String> fileData

The content of the file to be sent to the model.

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> fileUrl

The URL of the file to be sent to the model.

formaturi

Optional<String> filename

The name of the file to be sent to the model.

Role role

The role of the message. One of `unknown`, `user`, `assistant`, `system`, `critic`, `discriminator`, `developer`, or `tool`.

One of the following:

UNKNOWN("unknown")

USER("user")

ASSISTANT("assistant")

SYSTEM("system")

CRITIC("critic")

DISCRIMINATOR("discriminator")

DEVELOPER("developer")

TOOL("tool")

Status status

The status of item. One of `in_progress`, `completed`, or `incomplete`. Populated when items are returned via API.

One of the following:

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

JsonValue; type "message"constant"message"constant

The type of the message. Always set to `message`.

Optional<Phase> phase

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`). For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

One of the following:

COMMENTARY("commentary")

FINAL\_ANSWER("final\_answer")

class ResponseFunctionToolCallItem:

A tool call to run a function. See the
[function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.

String id

The unique ID of the function tool call.

Status status

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

One of the following:

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

Optional<String> createdBy

The identifier of the actor that created the item.

class ResponseFunctionToolCallOutputItem:

String id

The unique ID of the function call tool output.

String callId

The unique ID of the function tool call generated by the model.

Output output

The output from the function call generated by your code.
Can be a string or an list of output content.

One of the following:

String

List<FunctionAndCustomToolCallOutput>

One of the following:

class ResponseInputText:

A text input to the model.

String text

The text input to the model.

JsonValue; type "input\_text"constant"input\_text"constant

The type of the input item. Always `input_text`.

class ResponseInputImage:

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

Detail detail

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

One of the following:

LOW("low")

HIGH("high")

AUTO("auto")

ORIGINAL("original")

JsonValue; type "input\_image"constant"input\_image"constant

The type of the input item. Always `input_image`.

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> imageUrl

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

class ResponseInputFile:

A file input to the model.

JsonValue; type "input\_file"constant"input\_file"constant

The type of the input item. Always `input_file`.

Optional<Detail> detail

The detail level of the file to be sent to the model. Use `low` for the default rendering behavior, or `high` to render the file at higher quality. Defaults to `low`.

One of the following:

LOW("low")

HIGH("high")

Optional<String> fileData

The content of the file to be sent to the model.

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> fileUrl

The URL of the file to be sent to the model.

formaturi

Optional<String> filename

The name of the file to be sent to the model.

Status status

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

One of the following:

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

JsonValue; type "function\_call\_output"constant"function\_call\_output"constant

The type of the function tool call output. Always `function_call_output`.

Optional<String> createdBy

The identifier of the actor that created the item.

class ResponseFileSearchToolCall:

The results of a file search tool call. See the
[file search guide](https://platform.openai.com/docs/guides/tools-file-search) for more information.

String id

The unique ID of the file search tool call.

List<String> queries

The queries used to search for files.

Status status

The status of the file search tool call. One of `in_progress`,
`searching`, `incomplete` or `failed`,

One of the following:

IN\_PROGRESS("in\_progress")

SEARCHING("searching")

COMPLETED("completed")

INCOMPLETE("incomplete")

FAILED("failed")

JsonValue; type "file\_search\_call"constant"file\_search\_call"constant

The type of the file search tool call. Always `file_search_call`.

Optional<List<Result>> results

The results of the file search tool call.

Optional<Attributes> attributes

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.

One of the following:

String

double

boolean

Optional<String> fileId

The unique ID of the file.

Optional<String> filename

The name of the file.

Optional<Double> score

The relevance score of the file - a value between 0 and 1.

formatfloat

Optional<String> text

The text that was retrieved from the file.

class ResponseFunctionWebSearch:

The results of a web search tool call. See the
[web search guide](https://platform.openai.com/docs/guides/tools-web-search) for more information.

String id

The unique ID of the web search tool call.

Action action

An object describing the specific action taken in this web search call.
Includes details on how the model used the web (search, open\_page, find\_in\_page).

One of the following:

class Search:

Action type “search” - Performs a web search query.

JsonValue; type "search"constant"search"constant

The action type.

Optional<List<String>> queries

The search queries.

DeprecatedOptional<String> query

The search query.

Optional<List<Source>> sources

The sources used in the search.

JsonValue; type "url"constant"url"constant

The type of source. Always `url`.

String url

The URL of the source.

formaturi

class OpenPage:

Action type “open\_page” - Opens a specific URL from search results.

JsonValue; type "open\_page"constant"open\_page"constant

The action type.

Optional<String> url

The URL opened by the model.

formaturi

class FindInPage:

Action type “find\_in\_page”: Searches for a pattern within a loaded page.

String pattern

The pattern or text to search for within the page.

JsonValue; type "find\_in\_page"constant"find\_in\_page"constant

The action type.

String url

The URL of the page searched for the pattern.

formaturi

Status status

The status of the web search tool call.

One of the following:

IN\_PROGRESS("in\_progress")

SEARCHING("searching")

COMPLETED("completed")

FAILED("failed")

JsonValue; type "web\_search\_call"constant"web\_search\_call"constant

The type of the web search tool call. Always `web_search_call`.

ImageGenerationCall

String id

The unique ID of the image generation call.

Optional<String> result

The generated image encoded in base64.

Status status

The status of the image generation call.

One of the following:

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

GENERATING("generating")

FAILED("failed")

JsonValue; type "image\_generation\_call"constant"image\_generation\_call"constant

The type of the image generation call. Always `image_generation_call`.

class ResponseComputerToolCall:

A tool call to a computer use tool. See the
[computer use guide](https://platform.openai.com/docs/guides/tools-computer-use) for more information.

String id

The unique ID of the computer call.

String callId

An identifier used when responding to the tool call with output.

List<PendingSafetyCheck> pendingSafetyChecks

The pending safety checks for the computer call.

String id

The ID of the pending safety check.

Optional<String> code

The type of the pending safety check.

Optional<String> message

Details about the pending safety check.

Status status

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

One of the following:

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

Type type

The type of the computer call. Always `computer_call`.

Optional<Action> action

A click action.

One of the following:

class Click:

A click action.

Button button

Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

One of the following:

LEFT("left")

RIGHT("right")

WHEEL("wheel")

BACK("back")

FORWARD("forward")

JsonValue; type "click"constant"click"constant

Specifies the event type. For a click action, this property is always `click`.

long x

The x-coordinate where the click occurred.

long y

The y-coordinate where the click occurred.

Optional<List<String>> keys

The keys being held while clicking.

class DoubleClick:

A double click action.

Optional<List<String>> keys

The keys being held while double-clicking.

JsonValue; type "double\_click"constant"double\_click"constant

Specifies the event type. For a double click action, this property is always set to `double_click`.

long x

The x-coordinate where the double click occurred.

long y

The y-coordinate where the double click occurred.

class Drag:

A drag action.

List<Path> path

An array of coordinates representing the path of the drag action. Coordinates will appear as an array of objects, eg

[
  { x: 100, y: 200 },
  { x: 200, y: 300 }
]

long x

The x-coordinate.

long y

The y-coordinate.

JsonValue; type "drag"constant"drag"constant

Specifies the event type. For a drag action, this property is always set to `drag`.

Optional<List<String>> keys

The keys being held while dragging the mouse.

class Keypress:

A collection of keypresses the model would like to perform.

List<String> keys

The combination of keys the model is requesting to be pressed. This is an array of strings, each representing a key.

JsonValue; type "keypress"constant"keypress"constant

Specifies the event type. For a keypress action, this property is always set to `keypress`.

class Move:

A mouse move action.

JsonValue; type "move"constant"move"constant

Specifies the event type. For a move action, this property is always set to `move`.

long x

The x-coordinate to move to.

long y

The y-coordinate to move to.

Optional<List<String>> keys

The keys being held while moving the mouse.

JsonValue;

JsonValue; type "screenshot"constant"screenshot"constant

Specifies the event type. For a screenshot action, this property is always set to `screenshot`.

class Scroll:

A scroll action.

long scrollX

The horizontal scroll distance.

long scrollY

The vertical scroll distance.

JsonValue; type "scroll"constant"scroll"constant

Specifies the event type. For a scroll action, this property is always set to `scroll`.

long x

The x-coordinate where the scroll occurred.

long y

The y-coordinate where the scroll occurred.

Optional<List<String>> keys

The keys being held while scrolling.

class Type:

An action to type in text.

String text

The text to type.

JsonValue; type "type"constant"type"constant

Specifies the event type. For a type action, this property is always set to `type`.

JsonValue;

JsonValue; type "wait"constant"wait"constant

Specifies the event type. For a wait action, this property is always set to `wait`.

Optional<List<[ComputerAction](/api/reference/java/resources/responses#(resource)%20responses%20%3E%20(model)%20computer_action%20%3E%20(schema))>> actions

Flattened batched actions for `computer_use`. Each action includes an
`type` discriminator and action-specific fields.

One of the following:

Click

Button button

Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

One of the following:

LEFT("left")

RIGHT("right")

WHEEL("wheel")

BACK("back")

FORWARD("forward")

JsonValue; type "click"constant"click"constant

Specifies the event type. For a click action, this property is always `click`.

long x

The x-coordinate where the click occurred.

long y

The y-coordinate where the click occurred.

Optional<List<String>> keys

The keys being held while clicking.

DoubleClick

Optional<List<String>> keys

The keys being held while double-clicking.

JsonValue; type "double\_click"constant"double\_click"constant

Specifies the event type. For a double click action, this property is always set to `double_click`.

long x

The x-coordinate where the double click occurred.

long y

The y-coordinate where the double click occurred.

Drag

List<Path> path

An array of coordinates representing the path of the drag action. Coordinates will appear as an array of objects, eg

[
  { x: 100, y: 200 },
  { x: 200, y: 300 }
]

long x

The x-coordinate.

long y

The y-coordinate.

JsonValue; type "drag"constant"drag"constant

Specifies the event type. For a drag action, this property is always set to `drag`.

Optional<List<String>> keys

The keys being held while dragging the mouse.

Keypress

List<String> keys

The combination of keys the model is requesting to be pressed. This is an array of strings, each representing a key.

JsonValue; type "keypress"constant"keypress"constant

Specifies the event type. For a keypress action, this property is always set to `keypress`.

Move

JsonValue; type "move"constant"move"constant

Specifies the event type. For a move action, this property is always set to `move`.

long x

The x-coordinate to move to.

long y

The y-coordinate to move to.

Optional<List<String>> keys

The keys being held while moving the mouse.

JsonValue;

JsonValue; type "screenshot"constant"screenshot"constant

Specifies the event type. For a screenshot action, this property is always set to `screenshot`.

Scroll

long scrollX

The horizontal scroll distance.

long scrollY

The vertical scroll distance.

JsonValue; type "scroll"constant"scroll"constant

Specifies the event type. For a scroll action, this property is always set to `scroll`.

long x

The x-coordinate where the scroll occurred.

long y

The y-coordinate where the scroll occurred.

Optional<List<String>> keys

The keys being held while scrolling.

Type

String text

The text to type.

JsonValue; type "type"constant"type"constant

Specifies the event type. For a type action, this property is always set to `type`.

JsonValue;

JsonValue; type "wait"constant"wait"constant

Specifies the event type. For a wait action, this property is always set to `wait`.

class ResponseComputerToolCallOutputItem:

String id

The unique ID of the computer call tool output.

String callId

The ID of the computer tool call that produced the output.

[ResponseComputerToolCallOutputScreenshot](/api/reference/java/resources/responses#(resource)%20responses%20%3E%20(model)%20response_computer_tool_call_output_screenshot%20%3E%20(schema)) output

A computer screenshot image used with the computer use tool.

Status status

The status of the message input. One of `in_progress`, `completed`, or
`incomplete`. Populated when input items are returned via API.

One of the following:

COMPLETED("completed")

INCOMPLETE("incomplete")

FAILED("failed")

IN\_PROGRESS("in\_progress")

JsonValue; type "computer\_call\_output"constant"computer\_call\_output"constant

The type of the computer tool call output. Always `computer_call_output`.

Optional<List<AcknowledgedSafetyCheck>> acknowledgedSafetyChecks

The safety checks reported by the API that have been acknowledged by the
developer.

String id

The ID of the pending safety check.

Optional<String> code

The type of the pending safety check.

Optional<String> message

Details about the pending safety check.

Optional<String> createdBy

The identifier of the actor that created the item.

class ResponseToolSearchCall:

String id

The unique ID of the tool search call item.

JsonValue arguments

Arguments used for the tool search call.

Optional<String> callId

The unique ID of the tool search call generated by the model.

Execution execution

Whether tool search was executed by the server or by the client.

One of the following:

SERVER("server")

CLIENT("client")

Status status

The status of the tool search call item that was recorded.

One of the following:

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

JsonValue; type "tool\_search\_call"constant"tool\_search\_call"constant

The type of the item. Always `tool_search_call`.

Optional<String> createdBy

The identifier of the actor that created the item.

class ResponseToolSearchOutputItem:

String id

The unique ID of the tool search output item.

Optional<String> callId

The unique ID of the tool search call generated by the model.

Execution execution

Whether tool search was executed by the server or by the client.

One of the following:

SERVER("server")

CLIENT("client")

Status status

The status of the tool search output item that was recorded.

One of the following:

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

List<[Tool](/api/reference/java/resources/responses#(resource)%20responses%20%3E%20(model)%20tool%20%3E%20(schema))> tools

The loaded tool definitions returned by tool search.

One of the following:

class FunctionTool:

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

String name

The name of the function to call.

Optional<Parameters> parameters

A JSON schema object describing the parameters of the function.

Optional<Boolean> strict

Whether to enforce strict parameter validation. Default `true`.

JsonValue; type "function"constant"function"constant

The type of the function tool. Always `function`.

Optional<Boolean> deferLoading

Whether this function is deferred and loaded via tool search.

Optional<String> description

A description of the function. Used by the model to determine whether or not to call the function.

class FileSearchTool:

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

JsonValue; type "file\_search"constant"file\_search"constant

The type of the file search tool. Always `file_search`.

List<String> vectorStoreIds

The IDs of the vector stores to search.

Optional<Filters> filters

A filter to apply.

One of the following:

class ComparisonFilter:

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

String key

The key to compare against the value.

Type type

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

EQ("eq")

NE("ne")

GT("gt")

GTE("gte")

LT("lt")

LTE("lte")

IN("in")

NIN("nin")

Value value

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

String

double

boolean

List<ComparisonFilterValueItem>

One of the following:

String

double

class CompoundFilter:

Combine multiple filters using `and` or `or`.

List<Filter> filters

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

One of the following:

class ComparisonFilter:

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

String key

The key to compare against the value.

Type type

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

EQ("eq")

NE("ne")

GT("gt")

GTE("gte")

LT("lt")

LTE("lte")

IN("in")

NIN("nin")

Value value

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

String

double

boolean

List<ComparisonFilterValueItem>

One of the following:

String

double

JsonValue

Type type

Type of operation: `and` or `or`.

One of the following:

AND("and")

OR("or")

Optional<Long> maxNumResults

The maximum number of results to return. This number should be between 1 and 50 inclusive.

Optional<RankingOptions> rankingOptions

Ranking options for search.

Optional<HybridSearch> hybridSearch

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

double embeddingWeight

The weight of the embedding in the reciprocal ranking fusion.

double textWeight

The weight of the text in the reciprocal ranking fusion.

Optional<Ranker> ranker

The ranker to use for the file search.

One of the following:

AUTO("auto")

DEFAULT\_2024\_11\_15("default-2024-11-15")

Optional<Double> scoreThreshold

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

class ComputerTool:

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

JsonValue; type "computer"constant"computer"constant

The type of the computer tool. Always `computer`.

class ComputerUsePreviewTool:

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

long displayHeight

The height of the computer display.

long displayWidth

The width of the computer display.

Environment environment

The type of computer environment to control.

One of the following:

WINDOWS("windows")

MAC("mac")

LINUX("linux")

UBUNTU("ubuntu")

BROWSER("browser")

JsonValue; type "computer\_use\_preview"constant"computer\_use\_preview"constant

The type of the computer use tool. Always `computer_use_preview`.

class WebSearchTool:

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type type

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

One of the following:

WEB\_SEARCH("web\_search")

WEB\_SEARCH\_2025\_08\_26("web\_search\_2025\_08\_26")

Optional<Filters> filters

Filters for the search.

Optional<List<String>> allowedDomains

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

Optional<SearchContextSize> searchContextSize

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

LOW("low")

MEDIUM("medium")

HIGH("high")

Optional<UserLocation> userLocation

The approximate location of the user.

Optional<String> city

Free text input for the city of the user, e.g. `San Francisco`.

Optional<String> country

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

Optional<String> region

Free text input for the region of the user, e.g. `California`.

Optional<String> timezone

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

Optional<Type> type

The type of location approximation. Always `approximate`.

Mcp

String serverLabel

A label for this MCP server, used to identify it in tool calls.

JsonValue; type "mcp"constant"mcp"constant

The type of the MCP tool. Always `mcp`.

Optional<AllowedTools> allowedTools

List of allowed tool names or a filter object.

One of the following:

List<String>

class McpToolFilter:

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

Optional<String> authorization

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

Optional<ConnectorId> connectorId

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

CONNECTOR\_DROPBOX("connector\_dropbox")

CONNECTOR\_GMAIL("connector\_gmail")

CONNECTOR\_GOOGLECALENDAR("connector\_googlecalendar")

CONNECTOR\_GOOGLEDRIVE("connector\_googledrive")

CONNECTOR\_MICROSOFTTEAMS("connector\_microsoftteams")

CONNECTOR\_OUTLOOKCALENDAR("connector\_outlookcalendar")

CONNECTOR\_OUTLOOKEMAIL("connector\_outlookemail")

CONNECTOR\_SHAREPOINT("connector\_sharepoint")

Optional<Boolean> deferLoading

Whether this MCP tool is deferred and discovered via tool search.

Optional<Headers> headers

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

Optional<RequireApproval> requireApproval

Specify which of the MCP server’s tools require approval.

One of the following:

class McpToolApprovalFilter:

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

Optional<Always> always

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

Optional<Never> never

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

enum McpToolApprovalSetting:

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

ALWAYS("always")

NEVER("never")

Optional<String> serverDescription

Optional description of the MCP server, used to provide more context.

Optional<String> serverUrl

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

Optional<String> tunnelId

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

CodeInterpreter

Container container

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

One of the following:

String

class CodeInterpreterToolAuto:

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

JsonValue; type "auto"constant"auto"constant

Always `auto`.

Optional<List<String>> fileIds

An optional list of uploaded files to make available to your code.

Optional<MemoryLimit> memoryLimit

The memory limit for the code interpreter container.

One of the following:

\_1G("1g")

\_4G("4g")

\_16G("16g")

\_64G("64g")

Optional<NetworkPolicy> networkPolicy

Network access policy for the container.

One of the following:

class ContainerNetworkPolicyDisabled:

JsonValue; type "disabled"constant"disabled"constant

Disable outbound network access. Always `disabled`.

class ContainerNetworkPolicyAllowlist:

List<String> allowedDomains

A list of allowed domains when type is `allowlist`.

JsonValue; type "allowlist"constant"allowlist"constant

Allow outbound network access only to specified domains. Always `allowlist`.

Optional<List<[ContainerNetworkPolicyDomainSecret](/api/reference/java/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema))>> domainSecrets

Optional domain-scoped secrets for allowlisted domains.

String domain

The domain associated with the secret.

minLength1

String name

The name of the secret to inject for the domain.

minLength1

String value

The secret value to inject for the domain.

maxLength10485760

minLength1

JsonValue; type "code\_interpreter"constant"code\_interpreter"constant

The type of the code interpreter tool. Always `code_interpreter`.

ImageGeneration

JsonValue; type "image\_generation"constant"image\_generation"constant

The type of the image generation tool. Always `image_generation`.

Optional<Action> action

Whether to generate a new image or edit an existing image. Default: `auto`.

One of the following:

GENERATE("generate")

EDIT("edit")

AUTO("auto")

Optional<Background> background

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

TRANSPARENT("transparent")

OPAQUE("opaque")

AUTO("auto")

Optional<InputFidelity> inputFidelity

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

One of the following:

HIGH("high")

LOW("low")

Optional<InputImageMask> inputImageMask

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

Optional<String> fileId

File ID for the mask image.

Optional<String> imageUrl

Base64-encoded mask image.

Optional<Model> model

The image generation model to use. Default: `gpt-image-1`.

One of the following:

GPT\_IMAGE\_1("gpt-image-1")

GPT\_IMAGE\_1\_MINI("gpt-image-1-mini")

GPT\_IMAGE\_2("gpt-image-2")

GPT\_IMAGE\_2\_2026\_04\_21("gpt-image-2-2026-04-21")

GPT\_IMAGE\_1\_5("gpt-image-1.5")

CHATGPT\_IMAGE\_LATEST("chatgpt-image-latest")

Optional<Moderation> moderation

Moderation level for the generated image. Default: `auto`.

One of the following:

AUTO("auto")

LOW("low")

Optional<Long> outputCompression

Compression level for the output image. Default: 100.

minimum0

maximum100

Optional<OutputFormat> outputFormat

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

One of the following:

PNG("png")

WEBP("webp")

JPEG("jpeg")

Optional<Long> partialImages

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

Optional<Quality> quality

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

One of the following:

LOW("low")

MEDIUM("medium")

HIGH("high")

AUTO("auto")

Optional<Size> size

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

One of the following:

\_1024X1024("1024x1024")

\_1024X1536("1024x1536")

\_1536X1024("1536x1024")

AUTO("auto")

JsonValue;

JsonValue; type "local\_shell"constant"local\_shell"constant

The type of the local shell tool. Always `local_shell`.

class FunctionShellTool:

A tool that allows the model to execute shell commands.

JsonValue; type "shell"constant"shell"constant

The type of the shell tool. Always `shell`.

Optional<Environment> environment

One of the following:

class ContainerAuto:

JsonValue; type "container\_auto"constant"container\_auto"constant

Automatically creates a container for this request

Optional<List<String>> fileIds

An optional list of uploaded files to make available to your code.

Optional<MemoryLimit> memoryLimit

The memory limit for the container.

One of the following:

\_1G("1g")

\_4G("4g")

\_16G("16g")

\_64G("64g")

Optional<NetworkPolicy> networkPolicy

Network access policy for the container.

One of the following:

class ContainerNetworkPolicyDisabled:

JsonValue; type "disabled"constant"disabled"constant

Disable outbound network access. Always `disabled`.

class ContainerNetworkPolicyAllowlist:

List<String> allowedDomains

A list of allowed domains when type is `allowlist`.

JsonValue; type "allowlist"constant"allowlist"constant

Allow outbound network access only to specified domains. Always `allowlist`.

Optional<List<[ContainerNetworkPolicyDomainSecret](/api/reference/java/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema))>> domainSecrets

Optional domain-scoped secrets for allowlisted domains.

String domain

The domain associated with the secret.

minLength1

String name

The name of the secret to inject for the domain.

minLength1

String value

The secret value to inject for the domain.

maxLength10485760

minLength1

Optional<List<Skill>> skills

An optional list of skills referenced by id or inline data.

One of the following:

class SkillReference:

String skillId

The ID of the referenced skill.

maxLength64

minLength1

JsonValue; type "skill\_reference"constant"skill\_reference"constant

References a skill created with the /v1/skills endpoint.

Optional<String> version

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

class InlineSkill:

String description

The description of the skill.

String name

The name of the skill.

[InlineSkillSource](/api/reference/java/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill_source%20%3E%20(schema)) source

Inline skill payload

JsonValue; type "inline"constant"inline"constant

Defines an inline skill for this request.

class LocalEnvironment:

JsonValue; type "local"constant"local"constant

Use a local computer environment.

Optional<List<[LocalSkill](/api/reference/java/resources/responses#(resource)%20responses%20%3E%20(model)%20local_skill%20%3E%20(schema))>> skills

An optional list of skills.

String description

The description of the skill.

String name

The name of the skill.

String path

The path to the directory containing the skill.

class ContainerReference:

String containerId

The ID of the referenced container.

JsonValue; type "container\_reference"constant"container\_reference"constant

References a container created with the /v1/containers endpoint

class CustomTool:

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

String name

The name of the custom tool, used to identify it in tool calls.

JsonValue; type "custom"constant"custom"constant

The type of the custom tool. Always `custom`.

Optional<Boolean> deferLoading

Whether this tool should be deferred and discovered via tool search.

Optional<String> description

Optional description of the custom tool, used to provide more context.

Optional<[CustomToolInputFormat](/api/reference/java/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))> format

The input format for the custom tool. Default is unconstrained text.

class NamespaceTool:

Groups function/custom tools under a shared namespace.

String description

A description of the namespace shown to the model.

minLength1

String name

The namespace name used in tool calls (for example, `crm`).

minLength1

List<Tool> tools

The function/custom tools available inside this namespace.

One of the following:

class Function:

String name

maxLength128

minLength1

JsonValue; type "function"constant"function"constant

Optional<Boolean> deferLoading

Whether this function should be deferred and discovered via tool search.

Optional<String> description

Optional<JsonValue> parameters

Optional<Boolean> strict

class CustomTool:

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

String name

The name of the custom tool, used to identify it in tool calls.

JsonValue; type "custom"constant"custom"constant

The type of the custom tool. Always `custom`.

Optional<Boolean> deferLoading

Whether this tool should be deferred and discovered via tool search.

Optional<String> description

Optional description of the custom tool, used to provide more context.

Optional<[CustomToolInputFormat](/api/reference/java/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))> format

The input format for the custom tool. Default is unconstrained text.

JsonValue; type "namespace"constant"namespace"constant

The type of the tool. Always `namespace`.

class ToolSearchTool:

Hosted or BYOT tool search configuration for deferred tools.

JsonValue; type "tool\_search"constant"tool\_search"constant

The type of the tool. Always `tool_search`.

Optional<String> description

Description shown to the model for a client-executed tool search tool.

Optional<Execution> execution

Whether tool search is executed by the server or by the client.

One of the following:

SERVER("server")

CLIENT("client")

Optional<JsonValue> parameters

Parameter schema for a client-executed tool search tool.

class WebSearchPreviewTool:

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type type

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

One of the following:

WEB\_SEARCH\_PREVIEW("web\_search\_preview")

WEB\_SEARCH\_PREVIEW\_2025\_03\_11("web\_search\_preview\_2025\_03\_11")

Optional<List<SearchContentType>> searchContentTypes

One of the following:

TEXT("text")

IMAGE("image")

Optional<SearchContextSize> searchContextSize

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

LOW("low")

MEDIUM("medium")

HIGH("high")

Optional<UserLocation> userLocation

The user’s location.

JsonValue; type "approximate"constant"approximate"constant

The type of location approximation. Always `approximate`.

Optional<String> city

Free text input for the city of the user, e.g. `San Francisco`.

Optional<String> country

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

Optional<String> region

Free text input for the region of the user, e.g. `California`.

Optional<String> timezone

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

class ApplyPatchTool:

Allows the assistant to create, delete, or update files using unified diffs.

JsonValue; type "apply\_patch"constant"apply\_patch"constant

The type of the tool. Always `apply_patch`.

JsonValue; type "tool\_search\_output"constant"tool\_search\_output"constant

The type of the item. Always `tool_search_output`.

Optional<String> createdBy

The identifier of the actor that created the item.

AdditionalTools

String id

The unique ID of the additional tools item.

Role role

The role that provided the additional tools.

One of the following:

UNKNOWN("unknown")

USER("user")

ASSISTANT("assistant")

SYSTEM("system")

CRITIC("critic")

DISCRIMINATOR("discriminator")

DEVELOPER("developer")

TOOL("tool")

List<[Tool](/api/reference/java/resources/responses#(resource)%20responses%20%3E%20(model)%20tool%20%3E%20(schema))> tools

The additional tool definitions made available at this item.

One of the following:

class FunctionTool:

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

String name

The name of the function to call.

Optional<Parameters> parameters

A JSON schema object describing the parameters of the function.

Optional<Boolean> strict

Whether to enforce strict parameter validation. Default `true`.

JsonValue; type "function"constant"function"constant

The type of the function tool. Always `function`.

Optional<Boolean> deferLoading

Whether this function is deferred and loaded via tool search.

Optional<String> description

A description of the function. Used by the model to determine whether or not to call the function.

class FileSearchTool:

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

JsonValue; type "file\_search"constant"file\_search"constant

The type of the file search tool. Always `file_search`.

List<String> vectorStoreIds

The IDs of the vector stores to search.

Optional<Filters> filters

A filter to apply.

One of the following:

class ComparisonFilter:

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

String key

The key to compare against the value.

Type type

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

EQ("eq")

NE("ne")

GT("gt")

GTE("gte")

LT("lt")

LTE("lte")

IN("in")

NIN("nin")

Value value

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

String

double

boolean

List<ComparisonFilterValueItem>

One of the following:

String

double

class CompoundFilter:

Combine multiple filters using `and` or `or`.

List<Filter> filters

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

One of the following:

class ComparisonFilter:

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

String key

The key to compare against the value.

Type type

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

EQ("eq")

NE("ne")

GT("gt")

GTE("gte")

LT("lt")

LTE("lte")

IN("in")

NIN("nin")

Value value

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

String

double

boolean

List<ComparisonFilterValueItem>

One of the following:

String

double

JsonValue

Type type

Type of operation: `and` or `or`.

One of the following:

AND("and")

OR("or")

Optional<Long> maxNumResults

The maximum number of results to return. This number should be between 1 and 50 inclusive.

Optional<RankingOptions> rankingOptions

Ranking options for search.

Optional<HybridSearch> hybridSearch

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

double embeddingWeight

The weight of the embedding in the reciprocal ranking fusion.

double textWeight

The weight of the text in the reciprocal ranking fusion.

Optional<Ranker> ranker

The ranker to use for the file search.

One of the following:

AUTO("auto")

DEFAULT\_2024\_11\_15("default-2024-11-15")

Optional<Double> scoreThreshold

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

class ComputerTool:

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

JsonValue; type "computer"constant"computer"constant

The type of the computer tool. Always `computer`.

class ComputerUsePreviewTool:

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

long displayHeight

The height of the computer display.

long displayWidth

The width of the computer display.

Environment environment

The type of computer environment to control.

One of the following:

WINDOWS("windows")

MAC("mac")

LINUX("linux")

UBUNTU("ubuntu")

BROWSER("browser")

JsonValue; type "computer\_use\_preview"constant"computer\_use\_preview"constant

The type of the computer use tool. Always `computer_use_preview`.

class WebSearchTool:

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type type

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

One of the following:

WEB\_SEARCH("web\_search")

WEB\_SEARCH\_2025\_08\_26("web\_search\_2025\_08\_26")

Optional<Filters> filters

Filters for the search.

Optional<List<String>> allowedDomains

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

Optional<SearchContextSize> searchContextSize

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

LOW("low")

MEDIUM("medium")

HIGH("high")

Optional<UserLocation> userLocation

The approximate location of the user.

Optional<String> city

Free text input for the city of the user, e.g. `San Francisco`.

Optional<String> country

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

Optional<String> region

Free text input for the region of the user, e.g. `California`.

Optional<String> timezone

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

Optional<Type> type

The type of location approximation. Always `approximate`.

Mcp

String serverLabel

A label for this MCP server, used to identify it in tool calls.

JsonValue; type "mcp"constant"mcp"constant

The type of the MCP tool. Always `mcp`.

Optional<AllowedTools> allowedTools

List of allowed tool names or a filter object.

One of the following:

List<String>

class McpToolFilter:

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

Optional<String> authorization

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

Optional<ConnectorId> connectorId

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

CONNECTOR\_DROPBOX("connector\_dropbox")

CONNECTOR\_GMAIL("connector\_gmail")

CONNECTOR\_GOOGLECALENDAR("connector\_googlecalendar")

CONNECTOR\_GOOGLEDRIVE("connector\_googledrive")

CONNECTOR\_MICROSOFTTEAMS("connector\_microsoftteams")

CONNECTOR\_OUTLOOKCALENDAR("connector\_outlookcalendar")

CONNECTOR\_OUTLOOKEMAIL("connector\_outlookemail")

CONNECTOR\_SHAREPOINT("connector\_sharepoint")

Optional<Boolean> deferLoading

Whether this MCP tool is deferred and discovered via tool search.

Optional<Headers> headers

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

Optional<RequireApproval> requireApproval

Specify which of the MCP server’s tools require approval.

One of the following:

class McpToolApprovalFilter:

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

Optional<Always> always

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

Optional<Never> never

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

enum McpToolApprovalSetting:

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

ALWAYS("always")

NEVER("never")

Optional<String> serverDescription

Optional description of the MCP server, used to provide more context.

Optional<String> serverUrl

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

Optional<String> tunnelId

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

CodeInterpreter

Container container

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

One of the following:

String

class CodeInterpreterToolAuto:

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

JsonValue; type "auto"constant"auto"constant

Always `auto`.

Optional<List<String>> fileIds

An optional list of uploaded files to make available to your code.

Optional<MemoryLimit> memoryLimit

The memory limit for the code interpreter container.

One of the following:

\_1G("1g")

\_4G("4g")

\_16G("16g")

\_64G("64g")

Optional<NetworkPolicy> networkPolicy

Network access policy for the container.

One of the following:

class ContainerNetworkPolicyDisabled:

JsonValue; type "disabled"constant"disabled"constant

Disable outbound network access. Always `disabled`.

class ContainerNetworkPolicyAllowlist:

List<String> allowedDomains

A list of allowed domains when type is `allowlist`.

JsonValue; type "allowlist"constant"allowlist"constant

Allow outbound network access only to specified domains. Always `allowlist`.

Optional<List<[ContainerNetworkPolicyDomainSecret](/api/reference/java/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema))>> domainSecrets

Optional domain-scoped secrets for allowlisted domains.

String domain

The domain associated with the secret.

minLength1

String name

The name of the secret to inject for the domain.

minLength1

String value

The secret value to inject for the domain.

maxLength10485760

minLength1

JsonValue; type "code\_interpreter"constant"code\_interpreter"constant

The type of the code interpreter tool. Always `code_interpreter`.

ImageGeneration

JsonValue; type "image\_generation"constant"image\_generation"constant

The type of the image generation tool. Always `image_generation`.

Optional<Action> action

Whether to generate a new image or edit an existing image. Default: `auto`.

One of the following:

GENERATE("generate")

EDIT("edit")

AUTO("auto")

Optional<Background> background

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

TRANSPARENT("transparent")

OPAQUE("opaque")

AUTO("auto")

Optional<InputFidelity> inputFidelity

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

One of the following:

HIGH("high")

LOW("low")

Optional<InputImageMask> inputImageMask

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

Optional<String> fileId

File ID for the mask image.

Optional<String> imageUrl

Base64-encoded mask image.

Optional<Model> model

The image generation model to use. Default: `gpt-image-1`.

One of the following:

GPT\_IMAGE\_1("gpt-image-1")

GPT\_IMAGE\_1\_MINI("gpt-image-1-mini")

GPT\_IMAGE\_2("gpt-image-2")

GPT\_IMAGE\_2\_2026\_04\_21("gpt-image-2-2026-04-21")

GPT\_IMAGE\_1\_5("gpt-image-1.5")

CHATGPT\_IMAGE\_LATEST("chatgpt-image-latest")

Optional<Moderation> moderation

Moderation level for the generated image. Default: `auto`.

One of the following:

AUTO("auto")

LOW("low")

Optional<Long> outputCompression

Compression level for the output image. Default: 100.

minimum0

maximum100

Optional<OutputFormat> outputFormat

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

One of the following:

PNG("png")

WEBP("webp")

JPEG("jpeg")

Optional<Long> partialImages

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

Optional<Quality> quality

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

One of the following:

LOW("low")

MEDIUM("medium")

HIGH("high")

AUTO("auto")

Optional<Size> size

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

One of the following:

\_1024X1024("1024x1024")

\_1024X1536("1024x1536")

\_1536X1024("1536x1024")

AUTO("auto")

JsonValue;

JsonValue; type "local\_shell"constant"local\_shell"constant

The type of the local shell tool. Always `local_shell`.

class FunctionShellTool:

A tool that allows the model to execute shell commands.

JsonValue; type "shell"constant"shell"constant

The type of the shell tool. Always `shell`.

Optional<Environment> environment

One of the following:

class ContainerAuto:

JsonValue; type "container\_auto"constant"container\_auto"constant

Automatically creates a container for this request

Optional<List<String>> fileIds

An optional list of uploaded files to make available to your code.

Optional<MemoryLimit> memoryLimit

The memory limit for the container.

One of the following:

\_1G("1g")

\_4G("4g")

\_16G("16g")

\_64G("64g")

Optional<NetworkPolicy> networkPolicy

Network access policy for the container.

One of the following:

class ContainerNetworkPolicyDisabled:

JsonValue; type "disabled"constant"disabled"constant

Disable outbound network access. Always `disabled`.

class ContainerNetworkPolicyAllowlist:

List<String> allowedDomains

A list of allowed domains when type is `allowlist`.

JsonValue; type "allowlist"constant"allowlist"constant

Allow outbound network access only to specified domains. Always `allowlist`.

Optional<List<[ContainerNetworkPolicyDomainSecret](/api/reference/java/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema))>> domainSecrets

Optional domain-scoped secrets for allowlisted domains.

String domain

The domain associated with the secret.

minLength1

String name

The name of the secret to inject for the domain.

minLength1

String value

The secret value to inject for the domain.

maxLength10485760

minLength1

Optional<List<Skill>> skills

An optional list of skills referenced by id or inline data.

One of the following:

class SkillReference:

String skillId

The ID of the referenced skill.

maxLength64

minLength1

JsonValue; type "skill\_reference"constant"skill\_reference"constant

References a skill created with the /v1/skills endpoint.

Optional<String> version

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

class InlineSkill:

String description

The description of the skill.

String name

The name of the skill.

[InlineSkillSource](/api/reference/java/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill_source%20%3E%20(schema)) source

Inline skill payload

JsonValue; type "inline"constant"inline"constant

Defines an inline skill for this request.

class LocalEnvironment:

JsonValue; type "local"constant"local"constant

Use a local computer environment.

Optional<List<[LocalSkill](/api/reference/java/resources/responses#(resource)%20responses%20%3E%20(model)%20local_skill%20%3E%20(schema))>> skills

An optional list of skills.

String description

The description of the skill.

String name

The name of the skill.

String path

The path to the directory containing the skill.

class ContainerReference:

String containerId

The ID of the referenced container.

JsonValue; type "container\_reference"constant"container\_reference"constant

References a container created with the /v1/containers endpoint

class CustomTool:

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

String name

The name of the custom tool, used to identify it in tool calls.

JsonValue; type "custom"constant"custom"constant

The type of the custom tool. Always `custom`.

Optional<Boolean> deferLoading

Whether this tool should be deferred and discovered via tool search.

Optional<String> description

Optional description of the custom tool, used to provide more context.

Optional<[CustomToolInputFormat](/api/reference/java/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))> format

The input format for the custom tool. Default is unconstrained text.

class NamespaceTool:

Groups function/custom tools under a shared namespace.

String description

A description of the namespace shown to the model.

minLength1

String name

The namespace name used in tool calls (for example, `crm`).

minLength1

List<Tool> tools

The function/custom tools available inside this namespace.

One of the following:

class Function:

String name

maxLength128

minLength1

JsonValue; type "function"constant"function"constant

Optional<Boolean> deferLoading

Whether this function should be deferred and discovered via tool search.

Optional<String> description

Optional<JsonValue> parameters

Optional<Boolean> strict

class CustomTool:

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

String name

The name of the custom tool, used to identify it in tool calls.

JsonValue; type "custom"constant"custom"constant

The type of the custom tool. Always `custom`.

Optional<Boolean> deferLoading

Whether this tool should be deferred and discovered via tool search.

Optional<String> description

Optional description of the custom tool, used to provide more context.

Optional<[CustomToolInputFormat](/api/reference/java/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))> format

The input format for the custom tool. Default is unconstrained text.

JsonValue; type "namespace"constant"namespace"constant

The type of the tool. Always `namespace`.

class ToolSearchTool:

Hosted or BYOT tool search configuration for deferred tools.

JsonValue; type "tool\_search"constant"tool\_search"constant

The type of the tool. Always `tool_search`.

Optional<String> description

Description shown to the model for a client-executed tool search tool.

Optional<Execution> execution

Whether tool search is executed by the server or by the client.

One of the following:

SERVER("server")

CLIENT("client")

Optional<JsonValue> parameters

Parameter schema for a client-executed tool search tool.

class WebSearchPreviewTool:

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type type

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

One of the following:

WEB\_SEARCH\_PREVIEW("web\_search\_preview")

WEB\_SEARCH\_PREVIEW\_2025\_03\_11("web\_search\_preview\_2025\_03\_11")

Optional<List<SearchContentType>> searchContentTypes

One of the following:

TEXT("text")

IMAGE("image")

Optional<SearchContextSize> searchContextSize

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

LOW("low")

MEDIUM("medium")

HIGH("high")

Optional<UserLocation> userLocation

The user’s location.

JsonValue; type "approximate"constant"approximate"constant

The type of location approximation. Always `approximate`.

Optional<String> city

Free text input for the city of the user, e.g. `San Francisco`.

Optional<String> country

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

Optional<String> region

Free text input for the region of the user, e.g. `California`.

Optional<String> timezone

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

class ApplyPatchTool:

Allows the assistant to create, delete, or update files using unified diffs.

JsonValue; type "apply\_patch"constant"apply\_patch"constant

The type of the tool. Always `apply_patch`.

JsonValue; type "additional\_tools"constant"additional\_tools"constant

The type of the item. Always `additional_tools`.

class ResponseReasoningItem:

A description of the chain of thought used by a reasoning model while generating
a response. Be sure to include these items in your `input` to the Responses API
for subsequent turns of a conversation if you are manually
[managing context](https://platform.openai.com/docs/guides/conversation-state).

String id

The unique identifier of the reasoning content.

List<Summary> summary

Reasoning summary content.

String text

A summary of the reasoning output from the model so far.

JsonValue; type "summary\_text"constant"summary\_text"constant

The type of the object. Always `summary_text`.

JsonValue; type "reasoning"constant"reasoning"constant

The type of the object. Always `reasoning`.

Optional<List<Content>> content

Reasoning text content.

String text

The reasoning text from the model.

JsonValue; type "reasoning\_text"constant"reasoning\_text"constant

The type of the reasoning text. Always `reasoning_text`.

Optional<String> encryptedContent

The encrypted content of the reasoning item - populated when a response is
generated with `reasoning.encrypted_content` in the `include` parameter.

Optional<Status> status

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

One of the following:

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

class ResponseCompactionItem:

A compaction item generated by the [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).

String id

The unique ID of the compaction item.

String encryptedContent

The encrypted content that was produced by compaction.

JsonValue; type "compaction"constant"compaction"constant

The type of the item. Always `compaction`.

Optional<String> createdBy

The identifier of the actor that created the item.

class ResponseCodeInterpreterToolCall:

A tool call to run code.

String id

The unique ID of the code interpreter tool call.

Optional<String> code

The code to run, or null if not available.

String containerId

The ID of the container used to run the code.

Optional<List<Output>> outputs

The outputs generated by the code interpreter, such as logs or images.
Can be null if no outputs are available.

One of the following:

class Logs:

The logs output from the code interpreter.

String logs

The logs output from the code interpreter.

JsonValue; type "logs"constant"logs"constant

The type of the output. Always `logs`.

class Image:

The image output from the code interpreter.

JsonValue; type "image"constant"image"constant

The type of the output. Always `image`.

String url

The URL of the image output from the code interpreter.

formaturi

Status status

The status of the code interpreter tool call. Valid values are `in_progress`, `completed`, `incomplete`, `interpreting`, and `failed`.

One of the following:

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

INTERPRETING("interpreting")

FAILED("failed")

JsonValue; type "code\_interpreter\_call"constant"code\_interpreter\_call"constant

The type of the code interpreter tool call. Always `code_interpreter_call`.

LocalShellCall

String id

The unique ID of the local shell call.

Action action

Execute a shell command on the server.

List<String> command

The command to run.

Env env

Environment variables to set for the command.

JsonValue; type "exec"constant"exec"constant

The type of the local shell action. Always `exec`.

Optional<Long> timeoutMs

Optional timeout in milliseconds for the command.

Optional<String> user

Optional user to run the command as.

Optional<String> workingDirectory

Optional working directory to run the command in.

String callId

The unique ID of the local shell tool call generated by the model.

Status status

The status of the local shell call.

One of the following:

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

JsonValue; type "local\_shell\_call"constant"local\_shell\_call"constant

The type of the local shell call. Always `local_shell_call`.

LocalShellCallOutput

String id

The unique ID of the local shell tool call generated by the model.

String output

A JSON string of the output of the local shell tool call.

JsonValue; type "local\_shell\_call\_output"constant"local\_shell\_call\_output"constant

The type of the local shell tool call output. Always `local_shell_call_output`.

Optional<Status> status

The status of the item. One of `in_progress`, `completed`, or `incomplete`.

One of the following:

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

class ResponseFunctionShellToolCall:

A tool call that executes one or more shell commands in a managed environment.

String id

The unique ID of the shell tool call. Populated when this item is returned via API.

Action action

The shell commands and limits that describe how to run the tool call.

List<String> commands

Optional<Long> maxOutputLength

Optional maximum number of characters to return from each command.

Optional<Long> timeoutMs

Optional timeout in milliseconds for the commands.

String callId

The unique ID of the shell tool call generated by the model.

Optional<Environment> environment

Represents the use of a local environment to perform shell actions.

One of the following:

class ResponseLocalEnvironment:

Represents the use of a local environment to perform shell actions.

JsonValue; type "local"constant"local"constant

The environment type. Always `local`.

class ResponseContainerReference:

Represents a container created with /v1/containers.

String containerId

JsonValue; type "container\_reference"constant"container\_reference"constant

The environment type. Always `container_reference`.

Status status

The status of the shell call. One of `in_progress`, `completed`, or `incomplete`.

One of the following:

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

JsonValue; type "shell\_call"constant"shell\_call"constant

The type of the item. Always `shell_call`.

Optional<String> createdBy

The ID of the entity that created this tool call.

class ResponseFunctionShellToolCallOutput:

The output of a shell tool call that was emitted.

String id

The unique ID of the shell call output. Populated when this item is returned via API.

String callId

The unique ID of the shell tool call generated by the model.

Optional<Long> maxOutputLength

The maximum length of the shell command output. This is generated by the model and should be passed back with the raw output.

List<Output> output

An array of shell call output contents

Outcome outcome

Represents either an exit outcome (with an exit code) or a timeout outcome for a shell call output chunk.

One of the following:

JsonValue;

JsonValue; type "timeout"constant"timeout"constant

The outcome type. Always `timeout`.

class Exit:

Indicates that the shell commands finished and returned an exit code.

long exitCode

Exit code from the shell process.

JsonValue; type "exit"constant"exit"constant

The outcome type. Always `exit`.

String stderr

The standard error output that was captured.

String stdout

The standard output that was captured.

Optional<String> createdBy

The identifier of the actor that created the item.

Status status

The status of the shell call output. One of `in_progress`, `completed`, or `incomplete`.

One of the following:

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

JsonValue; type "shell\_call\_output"constant"shell\_call\_output"constant

The type of the shell call output. Always `shell_call_output`.

Optional<String> createdBy

The identifier of the actor that created the item.

class ResponseApplyPatchToolCall:

A tool call that applies file diffs by creating, deleting, or updating files.

String id

The unique ID of the apply patch tool call. Populated when this item is returned via API.

String callId

The unique ID of the apply patch tool call generated by the model.

Operation operation

One of the create\_file, delete\_file, or update\_file operations applied via apply\_patch.

One of the following:

class CreateFile:

Instruction describing how to create a file via the apply\_patch tool.

String diff

Diff to apply.

String path

Path of the file to create.

JsonValue; type "create\_file"constant"create\_file"constant

Create a new file with the provided diff.

class DeleteFile:

Instruction describing how to delete a file via the apply\_patch tool.

String path

Path of the file to delete.

JsonValue; type "delete\_file"constant"delete\_file"constant

Delete the specified file.

class UpdateFile:

Instruction describing how to update a file via the apply\_patch tool.

String diff

Diff to apply.

String path

Path of the file to update.

JsonValue; type "update\_file"constant"update\_file"constant

Update an existing file with the provided diff.

Status status

The status of the apply patch tool call. One of `in_progress` or `completed`.

One of the following:

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

JsonValue; type "apply\_patch\_call"constant"apply\_patch\_call"constant

The type of the item. Always `apply_patch_call`.

Optional<String> createdBy

The ID of the entity that created this tool call.

class ResponseApplyPatchToolCallOutput:

The output emitted by an apply patch tool call.

String id

The unique ID of the apply patch tool call output. Populated when this item is returned via API.

String callId

The unique ID of the apply patch tool call generated by the model.

Status status

The status of the apply patch tool call output. One of `completed` or `failed`.

One of the following:

COMPLETED("completed")

FAILED("failed")

JsonValue; type "apply\_patch\_call\_output"constant"apply\_patch\_call\_output"constant

The type of the item. Always `apply_patch_call_output`.

Optional<String> createdBy

The ID of the entity that created this tool call output.

Optional<String> output

Optional textual output returned by the apply patch tool.

McpListTools

String id

The unique ID of the list.

String serverLabel

The label of the MCP server.

List<Tool> tools

The tools available on the server.

JsonValue inputSchema

The JSON schema describing the tool’s input.

String name

The name of the tool.

Optional<JsonValue> annotations

Additional annotations about the tool.

Optional<String> description

The description of the tool.

JsonValue; type "mcp\_list\_tools"constant"mcp\_list\_tools"constant

The type of the item. Always `mcp_list_tools`.

Optional<String> error

Error message if the server could not list tools.

McpApprovalRequest

String id

The unique ID of the approval request.

String arguments

A JSON string of arguments for the tool.

String name

The name of the tool to run.

String serverLabel

The label of the MCP server making the request.

JsonValue; type "mcp\_approval\_request"constant"mcp\_approval\_request"constant

The type of the item. Always `mcp_approval_request`.

McpApprovalResponse

String id

The unique ID of the approval response

String approvalRequestId

The ID of the approval request being answered.

boolean approve

Whether the request was approved.

JsonValue; type "mcp\_approval\_response"constant"mcp\_approval\_response"constant

The type of the item. Always `mcp_approval_response`.

Optional<String> reason

Optional reason for the decision.

McpCall

String id

The unique ID of the tool call.

String arguments

A JSON string of the arguments passed to the tool.

String name

The name of the tool that was run.

String serverLabel

The label of the MCP server running the tool.

JsonValue; type "mcp\_call"constant"mcp\_call"constant

The type of the item. Always `mcp_call`.

Optional<String> approvalRequestId

Unique identifier for the MCP tool call approval request.
Include this value in a subsequent `mcp_approval_response` input to approve or reject the corresponding tool call.

Optional<String> error

The error from the tool call, if any.

Optional<String> output

The output from the tool call.

Optional<Status> status

The status of the tool call. One of `in_progress`, `completed`, `incomplete`, `calling`, or `failed`.

One of the following:

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

CALLING("calling")

FAILED("failed")

class ResponseCustomToolCall:

A call to a custom tool created by the model.

String callId

An identifier used to map this custom tool call to a tool call output.

String input

The input for the custom tool call generated by the model.

String name

The name of the custom tool being called.

JsonValue; type "custom\_tool\_call"constant"custom\_tool\_call"constant

The type of the custom tool call. Always `custom_tool_call`.

Optional<String> id

The unique ID of the custom tool call in the OpenAI platform.

Optional<String> namespace

The namespace of the custom tool being called.

class ResponseCustomToolCallOutput:

The output of a custom tool call from your code, being sent back to the model.

String callId

The call ID, used to map this custom tool call output to a custom tool call.

Output output

The output from the custom tool call generated by your code.
Can be a string or an list of output content.

One of the following:

String

List<FunctionAndCustomToolCallOutput>

One of the following:

class ResponseInputText:

A text input to the model.

String text

The text input to the model.

JsonValue; type "input\_text"constant"input\_text"constant

The type of the input item. Always `input_text`.

class ResponseInputImage:

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

Detail detail

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

One of the following:

LOW("low")

HIGH("high")

AUTO("auto")

ORIGINAL("original")

JsonValue; type "input\_image"constant"input\_image"constant

The type of the input item. Always `input_image`.

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> imageUrl

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

class ResponseInputFile:

A file input to the model.

JsonValue; type "input\_file"constant"input\_file"constant

The type of the input item. Always `input_file`.

Optional<Detail> detail

The detail level of the file to be sent to the model. Use `low` for the default rendering behavior, or `high` to render the file at higher quality. Defaults to `low`.

One of the following:

LOW("low")

HIGH("high")

Optional<String> fileData

The content of the file to be sent to the model.

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> fileUrl

The URL of the file to be sent to the model.

formaturi

Optional<String> filename

The name of the file to be sent to the model.

JsonValue; type "custom\_tool\_call\_output"constant"custom\_tool\_call\_output"constant

The type of the custom tool call output. Always `custom_tool_call_output`.

Optional<String> id

The unique ID of the custom tool call output in the OpenAI platform.

String firstId

The ID of the first item in the list.

boolean hasMore

Whether there are more items available.

String lastId

The ID of the last item in the list.

JsonValue; object\_ "list"constant"list"constant

The type of object returned, must be `list`.
