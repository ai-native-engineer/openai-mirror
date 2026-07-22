<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/responses/methods/compact/ -->

[API Reference](/api/reference/java)

[Beta](/api/reference/java/resources/beta)

[Responses](/api/reference/java/resources/beta/subresources/responses)

# Compact a response

[BetaCompactedResponse](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_compacted_response%20%3E%20(schema)) beta().responses().compact(ResponseCompactParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/responses/compact

Compact a conversation. Returns a compacted response object.

Learn when and how to compact long-running conversations in the [conversation state guide](https://platform.openai.com/docs/guides/conversation-state#managing-the-context-window). For ZDR-compatible compaction details, see [Compaction (advanced)](https://platform.openai.com/docs/guides/conversation-state#compaction-advanced).

##### ParametersExpand Collapse

ResponseCompactParams params

Optional<List<Beta>> betas

RESPONSES\_MULTI\_AGENT\_V1("responses\_multi\_agent=v1")

Optional<Model> model

Model ID used to generate the response, like `gpt-5` or `o3`. OpenAI offers a wide range of models with different capabilities, performance characteristics, and price points. Refer to the [model guide](https://platform.openai.com/docs/models) to browse and compare available models.

GPT\_5\_6\_SOL("gpt-5.6-sol")

GPT\_5\_6\_TERRA("gpt-5.6-terra")

GPT\_5\_6\_LUNA("gpt-5.6-luna")

GPT\_5\_4("gpt-5.4")

GPT\_5\_4\_MINI("gpt-5.4-mini")

GPT\_5\_4\_NANO("gpt-5.4-nano")

GPT\_5\_4\_MINI\_2026\_03\_17("gpt-5.4-mini-2026-03-17")

GPT\_5\_4\_NANO\_2026\_03\_17("gpt-5.4-nano-2026-03-17")

GPT\_5\_3\_CHAT\_LATEST("gpt-5.3-chat-latest")

GPT\_5\_2("gpt-5.2")

GPT\_5\_2\_2025\_12\_11("gpt-5.2-2025-12-11")

GPT\_5\_2\_CHAT\_LATEST("gpt-5.2-chat-latest")

GPT\_5\_2\_PRO("gpt-5.2-pro")

GPT\_5\_2\_PRO\_2025\_12\_11("gpt-5.2-pro-2025-12-11")

GPT\_5\_1("gpt-5.1")

GPT\_5\_1\_2025\_11\_13("gpt-5.1-2025-11-13")

GPT\_5\_1\_CODEX("gpt-5.1-codex")

GPT\_5\_1\_MINI("gpt-5.1-mini")

GPT\_5\_1\_CHAT\_LATEST("gpt-5.1-chat-latest")

GPT\_5("gpt-5")

GPT\_5\_MINI("gpt-5-mini")

GPT\_5\_NANO("gpt-5-nano")

GPT\_5\_2025\_08\_07("gpt-5-2025-08-07")

GPT\_5\_MINI\_2025\_08\_07("gpt-5-mini-2025-08-07")

GPT\_5\_NANO\_2025\_08\_07("gpt-5-nano-2025-08-07")

GPT\_5\_CHAT\_LATEST("gpt-5-chat-latest")

GPT\_4\_1("gpt-4.1")

GPT\_4\_1\_MINI("gpt-4.1-mini")

GPT\_4\_1\_NANO("gpt-4.1-nano")

GPT\_4\_1\_2025\_04\_14("gpt-4.1-2025-04-14")

GPT\_4\_1\_MINI\_2025\_04\_14("gpt-4.1-mini-2025-04-14")

GPT\_4\_1\_NANO\_2025\_04\_14("gpt-4.1-nano-2025-04-14")

O4\_MINI("o4-mini")

O4\_MINI\_2025\_04\_16("o4-mini-2025-04-16")

O3("o3")

O3\_2025\_04\_16("o3-2025-04-16")

O3\_MINI("o3-mini")

O3\_MINI\_2025\_01\_31("o3-mini-2025-01-31")

O1("o1")

O1\_2024\_12\_17("o1-2024-12-17")

O1\_PREVIEW("o1-preview")

O1\_PREVIEW\_2024\_09\_12("o1-preview-2024-09-12")

O1\_MINI("o1-mini")

O1\_MINI\_2024\_09\_12("o1-mini-2024-09-12")

GPT\_4O("gpt-4o")

GPT\_4O\_2024\_11\_20("gpt-4o-2024-11-20")

GPT\_4O\_2024\_08\_06("gpt-4o-2024-08-06")

GPT\_4O\_2024\_05\_13("gpt-4o-2024-05-13")

GPT\_4O\_AUDIO\_PREVIEW("gpt-4o-audio-preview")

GPT\_4O\_AUDIO\_PREVIEW\_2024\_10\_01("gpt-4o-audio-preview-2024-10-01")

GPT\_4O\_AUDIO\_PREVIEW\_2024\_12\_17("gpt-4o-audio-preview-2024-12-17")

GPT\_4O\_AUDIO\_PREVIEW\_2025\_06\_03("gpt-4o-audio-preview-2025-06-03")

GPT\_4O\_MINI\_AUDIO\_PREVIEW("gpt-4o-mini-audio-preview")

GPT\_4O\_MINI\_AUDIO\_PREVIEW\_2024\_12\_17("gpt-4o-mini-audio-preview-2024-12-17")

GPT\_4O\_SEARCH\_PREVIEW("gpt-4o-search-preview")

GPT\_4O\_MINI\_SEARCH\_PREVIEW("gpt-4o-mini-search-preview")

GPT\_4O\_SEARCH\_PREVIEW\_2025\_03\_11("gpt-4o-search-preview-2025-03-11")

GPT\_4O\_MINI\_SEARCH\_PREVIEW\_2025\_03\_11("gpt-4o-mini-search-preview-2025-03-11")

CHATGPT\_4O\_LATEST("chatgpt-4o-latest")

CODEX\_MINI\_LATEST("codex-mini-latest")

GPT\_4O\_MINI("gpt-4o-mini")

GPT\_4O\_MINI\_2024\_07\_18("gpt-4o-mini-2024-07-18")

GPT\_4\_TURBO("gpt-4-turbo")

GPT\_4\_TURBO\_2024\_04\_09("gpt-4-turbo-2024-04-09")

GPT\_4\_0125\_PREVIEW("gpt-4-0125-preview")

GPT\_4\_TURBO\_PREVIEW("gpt-4-turbo-preview")

GPT\_4\_1106\_PREVIEW("gpt-4-1106-preview")

GPT\_4\_VISION\_PREVIEW("gpt-4-vision-preview")

GPT\_4("gpt-4")

GPT\_4\_0314("gpt-4-0314")

GPT\_4\_0613("gpt-4-0613")

GPT\_4\_32K("gpt-4-32k")

GPT\_4\_32K\_0314("gpt-4-32k-0314")

GPT\_4\_32K\_0613("gpt-4-32k-0613")

GPT\_3\_5\_TURBO("gpt-3.5-turbo")

GPT\_3\_5\_TURBO\_16K("gpt-3.5-turbo-16k")

GPT\_3\_5\_TURBO\_0301("gpt-3.5-turbo-0301")

GPT\_3\_5\_TURBO\_0613("gpt-3.5-turbo-0613")

GPT\_3\_5\_TURBO\_1106("gpt-3.5-turbo-1106")

GPT\_3\_5\_TURBO\_0125("gpt-3.5-turbo-0125")

GPT\_3\_5\_TURBO\_16K\_0613("gpt-3.5-turbo-16k-0613")

O1\_PRO("o1-pro")

O1\_PRO\_2025\_03\_19("o1-pro-2025-03-19")

O3\_PRO("o3-pro")

O3\_PRO\_2025\_06\_10("o3-pro-2025-06-10")

O3\_DEEP\_RESEARCH("o3-deep-research")

O3\_DEEP\_RESEARCH\_2025\_06\_26("o3-deep-research-2025-06-26")

O4\_MINI\_DEEP\_RESEARCH("o4-mini-deep-research")

O4\_MINI\_DEEP\_RESEARCH\_2025\_06\_26("o4-mini-deep-research-2025-06-26")

COMPUTER\_USE\_PREVIEW("computer-use-preview")

COMPUTER\_USE\_PREVIEW\_2025\_03\_11("computer-use-preview-2025-03-11")

GPT\_5\_CODEX("gpt-5-codex")

GPT\_5\_PRO("gpt-5-pro")

GPT\_5\_PRO\_2025\_10\_06("gpt-5-pro-2025-10-06")

GPT\_5\_1\_CODEX\_MAX("gpt-5.1-codex-max")

Optional<Input> input

Text, image, or file inputs to the model, used to generate a response

String

List<[BetaResponseInputItem](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_item%20%3E%20(schema))>

class BetaEasyInputMessage:

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

Content content

Text, image, or audio input to the model, used to generate a response.
Can also contain previous assistant responses.

String

List<[BetaResponseInputContent](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_content%20%3E%20(schema))>

class BetaResponseInputText:

String text

JsonValue; type "input\_text"constant"input\_text"constant

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

JsonValue; mode "explicit"constant"explicit"constant

class BetaResponseInputImage:

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

Detail detail

LOW("low")

HIGH("high")

AUTO("auto")

ORIGINAL("original")

JsonValue; type "input\_image"constant"input\_image"constant

Optional<String> fileId

Optional<String> imageUrl

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

JsonValue; mode "explicit"constant"explicit"constant

class BetaResponseInputFile:

JsonValue; type "input\_file"constant"input\_file"constant

Optional<Detail> detail

AUTO("auto")

LOW("low")

HIGH("high")

Optional<String> fileData

Optional<String> fileId

Optional<String> fileUrl

Optional<String> filename

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

JsonValue; mode "explicit"constant"explicit"constant

Role role

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

USER("user")

ASSISTANT("assistant")

SYSTEM("system")

DEVELOPER("developer")

Optional<Phase> phase

COMMENTARY("commentary")

FINAL\_ANSWER("final\_answer")

Optional<Type> type

The type of the message input. Always `message`.

Message

List<[BetaResponseInputContent](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_content%20%3E%20(schema))> content

class BetaResponseInputText:

String text

JsonValue; type "input\_text"constant"input\_text"constant

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

JsonValue; mode "explicit"constant"explicit"constant

class BetaResponseInputImage:

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

Detail detail

LOW("low")

HIGH("high")

AUTO("auto")

ORIGINAL("original")

JsonValue; type "input\_image"constant"input\_image"constant

Optional<String> fileId

Optional<String> imageUrl

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

JsonValue; mode "explicit"constant"explicit"constant

class BetaResponseInputFile:

JsonValue; type "input\_file"constant"input\_file"constant

Optional<Detail> detail

AUTO("auto")

LOW("low")

HIGH("high")

Optional<String> fileData

Optional<String> fileId

Optional<String> fileUrl

Optional<String> filename

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

JsonValue; mode "explicit"constant"explicit"constant

Role role

USER("user")

SYSTEM("system")

DEVELOPER("developer")

Optional<Agent> agent

String agentName

Optional<Status> status

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

Optional<Type> type

class BetaResponseOutputMessage:

String id

List<Content> content

class BetaResponseOutputText:

List<Annotation> annotations

class FileCitation:

String fileId

String filename

long index

JsonValue; type "file\_citation"constant"file\_citation"constant

class UrlCitation:

long endIndex

long startIndex

String title

JsonValue; type "url\_citation"constant"url\_citation"constant

String url

class ContainerFileCitation:

String containerId

long endIndex

String fileId

String filename

long startIndex

JsonValue; type "container\_file\_citation"constant"container\_file\_citation"constant

class FilePath:

String fileId

long index

JsonValue; type "file\_path"constant"file\_path"constant

String text

JsonValue; type "output\_text"constant"output\_text"constant

Optional<List<Logprob>> logprobs

String token

List<long> bytes

double logprob

List<TopLogprob> topLogprobs

String token

List<long> bytes

double logprob

class BetaResponseOutputRefusal:

String refusal

JsonValue; type "refusal"constant"refusal"constant

JsonValue; role "assistant"constant"assistant"constant

Status status

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

JsonValue; type "message"constant"message"constant

Optional<Agent> agent

String agentName

Optional<Phase> phase

COMMENTARY("commentary")

FINAL\_ANSWER("final\_answer")

class BetaResponseFileSearchToolCall:

[file search guide](https://platform.openai.com/docs/guides/tools-file-search) for more information.

String id

List<String> queries

Status status

IN\_PROGRESS("in\_progress")

SEARCHING("searching")

COMPLETED("completed")

INCOMPLETE("incomplete")

FAILED("failed")

JsonValue; type "file\_search\_call"constant"file\_search\_call"constant

Optional<Agent> agent

String agentName

Optional<List<Result>> results

Optional<Attributes> attributes

String

double

boolean

Optional<String> fileId

Optional<String> filename

Optional<Double> score

formatfloat

Optional<String> text

class BetaResponseComputerToolCall:

[computer use guide](https://platform.openai.com/docs/guides/tools-computer-use) for more information.

String id

String callId

List<PendingSafetyCheck> pendingSafetyChecks

String id

Optional<String> code

Optional<String> message

Status status

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

Type type

Optional<[BetaComputerAction](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_computer_action%20%3E%20(schema))> action

Click

Button button

Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

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

  { x: 100, y: 200 },
  { x: 200, y: 300 }

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

Optional<List<[BetaComputerAction](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_computer_action%20%3E%20(schema))>> actions

Click

Button button

Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

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

  { x: 100, y: 200 },
  { x: 200, y: 300 }

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

Optional<Agent> agent

String agentName

ComputerCallOutput

String callId

maxLength64

minLength1

[BetaResponseComputerToolCallOutputScreenshot](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_computer_tool_call_output_screenshot%20%3E%20(schema)) output

JsonValue; type "computer\_screenshot"constant"computer\_screenshot"constant

Specifies the event type. For a computer screenshot, this property is
always set to `computer_screenshot`.

Optional<String> fileId

Optional<String> imageUrl

JsonValue; type "computer\_call\_output"constant"computer\_call\_output"constant

Optional<String> id

The ID of the computer tool call output.

Optional<List<AcknowledgedSafetyCheck>> acknowledgedSafetyChecks

The safety checks reported by the API that have been acknowledged by the developer.

String id

Optional<String> code

Optional<String> message

Optional<Agent> agent

String agentName

Optional<Status> status

The status of the message input. One of `in_progress`, `completed`, or `incomplete`. Populated when input items are returned via API.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

class BetaResponseFunctionWebSearch:

[web search guide](https://platform.openai.com/docs/guides/tools-web-search) for more information.

String id

Action action

class Search:

JsonValue; type "search"constant"search"constant

Optional<List<String>> queries

DeprecatedOptional<String> query

Optional<List<Source>> sources

JsonValue; type "url"constant"url"constant

String url

class OpenPage:

JsonValue; type "open\_page"constant"open\_page"constant

Optional<String> url

class FindInPage:

String pattern

JsonValue; type "find\_in\_page"constant"find\_in\_page"constant

String url

Status status

IN\_PROGRESS("in\_progress")

SEARCHING("searching")

COMPLETED("completed")

FAILED("failed")

JsonValue; type "web\_search\_call"constant"web\_search\_call"constant

Optional<Agent> agent

String agentName

class BetaResponseFunctionToolCall:

[function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.

String arguments

A JSON string of the arguments to pass to the function.

String callId

String name

The name of the function to run.

JsonValue; type "function\_call"constant"function\_call"constant

The type of the function tool call. Always `function_call`.

Optional<String> id

Optional<Agent> agent

String agentName

Optional<Caller> caller

JsonValue;

JsonValue; type "direct"constant"direct"constant

class Program:

String callerId

JsonValue; type "program"constant"program"constant

Optional<String> namespace

The namespace of the function to run.

Optional<Status> status

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

FunctionCallOutput

String callId

maxLength64

minLength1

Output output

Text, image, or file output of the function tool call.

String

List<[BetaResponseFunctionCallOutputItem](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_call_output_item%20%3E%20(schema))>

class BetaResponseInputTextContent:

String text

maxLength10485760

JsonValue; type "input\_text"constant"input\_text"constant

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

JsonValue; mode "explicit"constant"explicit"constant

class BetaResponseInputImageContent:

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision)

JsonValue; type "input\_image"constant"input\_image"constant

Optional<Detail> detail

LOW("low")

HIGH("high")

AUTO("auto")

ORIGINAL("original")

Optional<String> fileId

Optional<String> imageUrl

maxLength20971520

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

JsonValue; mode "explicit"constant"explicit"constant

class BetaResponseInputFileContent:

JsonValue; type "input\_file"constant"input\_file"constant

Optional<Detail> detail

AUTO("auto")

LOW("low")

HIGH("high")

Optional<String> fileData

The base64-encoded data of the file to be sent to the model.

maxLength73400320

Optional<String> fileId

Optional<String> fileUrl

Optional<String> filename

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

JsonValue; mode "explicit"constant"explicit"constant

JsonValue; type "function\_call\_output"constant"function\_call\_output"constant

Optional<String> id

The unique ID of the function tool call output. Populated when this item is returned via API.

Optional<Agent> agent

String agentName

Optional<Caller> caller

JsonValue;

JsonValue; type "direct"constant"direct"constant

The caller type. Always `direct`.

class Program:

String callerId

maxLength64

minLength1

JsonValue; type "program"constant"program"constant

Optional<Status> status

The status of the item. One of `in_progress`, `completed`, or `incomplete`. Populated when items are returned via API.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

AgentMessage

String author

List<Content> content

Plaintext, image, or encrypted content sent between agents.

class BetaResponseInputTextContent:

String text

maxLength10485760

JsonValue; type "input\_text"constant"input\_text"constant

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

JsonValue; mode "explicit"constant"explicit"constant

class BetaResponseInputImageContent:

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision)

JsonValue; type "input\_image"constant"input\_image"constant

Optional<Detail> detail

LOW("low")

HIGH("high")

AUTO("auto")

ORIGINAL("original")

Optional<String> fileId

Optional<String> imageUrl

maxLength20971520

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

JsonValue; mode "explicit"constant"explicit"constant

class EncryptedContent:

String encryptedContent

maxLength10485760

JsonValue; type "encrypted\_content"constant"encrypted\_content"constant

String recipient

JsonValue; type "agent\_message"constant"agent\_message"constant

The item type. Always `agent_message`.

Optional<String> id

The unique ID of this agent message item.

Optional<Agent> agent

String agentName

MultiAgentCall

Action action

The multi-agent action that was executed.

SPAWN\_AGENT("spawn\_agent")

INTERRUPT\_AGENT("interrupt\_agent")

LIST\_AGENTS("list\_agents")

SEND\_MESSAGE("send\_message")

FOLLOWUP\_TASK("followup\_task")

WAIT\_AGENT("wait\_agent")

String arguments

The action arguments as a JSON string.

String callId

maxLength64

minLength1

JsonValue; type "multi\_agent\_call"constant"multi\_agent\_call"constant

The item type. Always `multi_agent_call`.

Optional<String> id

The unique ID of this multi-agent call.

Optional<Agent> agent

String agentName

MultiAgentCallOutput

Action action

SPAWN\_AGENT("spawn\_agent")

INTERRUPT\_AGENT("interrupt\_agent")

LIST\_AGENTS("list\_agents")

SEND\_MESSAGE("send\_message")

FOLLOWUP\_TASK("followup\_task")

WAIT\_AGENT("wait\_agent")

String callId

maxLength64

minLength1

List<Output> output

String text

The text content.

maxLength10485760

JsonValue; type "output\_text"constant"output\_text"constant

The content type. Always `output_text`.

Optional<List<Annotation>> annotations

Citations associated with the text content.

class FileCitation:

String fileId

String filename

long index

minimum0

JsonValue; type "file\_citation"constant"file\_citation"constant

The citation type. Always `file_citation`.

class UrlCitation:

long endIndex

The index of the last character of the citation in the message.

minimum0

long startIndex

The index of the first character of the citation in the message.

minimum0

String title

The title of the cited resource.

JsonValue; type "url\_citation"constant"url\_citation"constant

The citation type. Always `url_citation`.

String url

The URL of the cited resource.

class ContainerFileCitation:

String containerId

The ID of the container.

long endIndex

The index of the last character of the citation in the message.

minimum0

String fileId

String filename

long startIndex

The index of the first character of the citation in the message.

minimum0

JsonValue; type "container\_file\_citation"constant"container\_file\_citation"constant

The citation type. Always `container_file_citation`.

JsonValue; type "multi\_agent\_call\_output"constant"multi\_agent\_call\_output"constant

The item type. Always `multi_agent_call_output`.

Optional<String> id

The unique ID of this multi-agent call output.

Optional<Agent> agent

String agentName

ToolSearchCall

JsonValue arguments

The arguments supplied to the tool search call.

JsonValue; type "tool\_search\_call"constant"tool\_search\_call"constant

The item type. Always `tool_search_call`.

Optional<String> id

The unique ID of this tool search call.

Optional<Agent> agent

String agentName

Optional<String> callId

maxLength64

minLength1

Optional<Execution> execution

SERVER("server")

CLIENT("client")

Optional<Status> status

The status of the tool search call.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

class BetaResponseToolSearchOutputItemParam:

List<[BetaTool](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))> tools

The loaded tool definitions returned by the tool search output.

class BetaFunctionTool:

String name

Optional<Parameters> parameters

Optional<Boolean> strict

JsonValue; type "function"constant"function"constant

Optional<List<AllowedCaller>> allowedCallers

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Optional<String> description

Optional<OutputSchema> outputSchema

class BetaFileSearchTool:

JsonValue; type "file\_search"constant"file\_search"constant

List<String> vectorStoreIds

Optional<Filters> filters

class ComparisonFilter:

String key

Type type

EQ("eq")

NE("ne")

GT("gt")

GTE("gte")

LT("lt")

LTE("lte")

IN("in")

NIN("nin")

Value value

String

double

boolean

List<ComparisonFilterValueItem>

String

double

class CompoundFilter:

List<Filter> filters

class ComparisonFilter:

String key

Type type

EQ("eq")

NE("ne")

GT("gt")

GTE("gte")

LT("lt")

LTE("lte")

IN("in")

NIN("nin")

Value value

String

double

boolean

List<ComparisonFilterValueItem>

String

double

JsonValue

Type type

AND("and")

OR("or")

Optional<Long> maxNumResults

Optional<RankingOptions> rankingOptions

Optional<HybridSearch> hybridSearch

double embeddingWeight

double textWeight

Optional<Ranker> ranker

AUTO("auto")

DEFAULT\_2024\_11\_15("default-2024-11-15")

Optional<Double> scoreThreshold

class BetaComputerTool:

JsonValue; type "computer"constant"computer"constant

class BetaComputerUsePreviewTool:

long displayHeight

long displayWidth

Environment environment

WINDOWS("windows")

MAC("mac")

LINUX("linux")

UBUNTU("ubuntu")

BROWSER("browser")

JsonValue; type "computer\_use\_preview"constant"computer\_use\_preview"constant

class BetaWebSearchTool:

[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type type

WEB\_SEARCH("web\_search")

WEB\_SEARCH\_2025\_08\_26("web\_search\_2025\_08\_26")

Optional<Filters> filters

Optional<List<String>> allowedDomains

Optional<SearchContextSize> searchContextSize

LOW("low")

MEDIUM("medium")

HIGH("high")

Optional<UserLocation> userLocation

Optional<String> city

Optional<String> country

Optional<String> region

Optional<String> timezone

Optional<Type> type

Mcp

String serverLabel

JsonValue; type "mcp"constant"mcp"constant

Optional<List<AllowedCaller>> allowedCallers

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<AllowedTools> allowedTools

List<String>

class McpToolFilter:

Optional<Boolean> readOnly

Optional<List<String>> toolNames

Optional<String> authorization

Optional<ConnectorId> connectorId

about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

CONNECTOR\_DROPBOX("connector\_dropbox")

CONNECTOR\_GMAIL("connector\_gmail")

CONNECTOR\_GOOGLECALENDAR("connector\_googlecalendar")

CONNECTOR\_GOOGLEDRIVE("connector\_googledrive")

CONNECTOR\_MICROSOFTTEAMS("connector\_microsoftteams")

CONNECTOR\_OUTLOOKCALENDAR("connector\_outlookcalendar")

CONNECTOR\_OUTLOOKEMAIL("connector\_outlookemail")

CONNECTOR\_SHAREPOINT("connector\_sharepoint")

Optional<Boolean> deferLoading

Optional<Headers> headers

Optional<RequireApproval> requireApproval

class McpToolApprovalFilter:

Optional<Always> always

Optional<Boolean> readOnly

Optional<List<String>> toolNames

Optional<Never> never

Optional<Boolean> readOnly

Optional<List<String>> toolNames

enum McpToolApprovalSetting:

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

ALWAYS("always")

NEVER("never")

Optional<String> serverDescription

Optional<String> serverUrl

Optional<String> tunnelId

CodeInterpreter

Container container

String

class CodeInterpreterToolAuto:

JsonValue; type "auto"constant"auto"constant

Optional<List<String>> fileIds

Optional<MemoryLimit> memoryLimit

\_1G("1g")

\_4G("4g")

\_16G("16g")

\_64G("64g")

Optional<NetworkPolicy> networkPolicy

class BetaContainerNetworkPolicyDisabled:

JsonValue; type "disabled"constant"disabled"constant

class BetaContainerNetworkPolicyAllowlist:

List<String> allowedDomains

JsonValue; type "allowlist"constant"allowlist"constant

Optional<List<[BetaContainerNetworkPolicyDomainSecret](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))>> domainSecrets

String domain

minLength1

String name

minLength1

String value

maxLength10485760

minLength1

JsonValue; type "code\_interpreter"constant"code\_interpreter"constant

Optional<List<AllowedCaller>> allowedCallers

DIRECT("direct")

PROGRAMMATIC("programmatic")

JsonValue;

JsonValue; type "programmatic\_tool\_calling"constant"programmatic\_tool\_calling"constant

The type of the tool. Always `programmatic_tool_calling`.

ImageGeneration

JsonValue; type "image\_generation"constant"image\_generation"constant

Optional<Action> action

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

TRANSPARENT("transparent")

OPAQUE("opaque")

AUTO("auto")

Optional<InputFidelity> inputFidelity

HIGH("high")

LOW("low")

Optional<InputImageMask> inputImageMask

Optional<String> fileId

Optional<String> imageUrl

Optional<Model> model

GPT\_IMAGE\_1("gpt-image-1")

GPT\_IMAGE\_1\_MINI("gpt-image-1-mini")

GPT\_IMAGE\_2("gpt-image-2")

GPT\_IMAGE\_2\_2026\_04\_21("gpt-image-2-2026-04-21")

GPT\_IMAGE\_1\_5("gpt-image-1.5")

CHATGPT\_IMAGE\_LATEST("chatgpt-image-latest")

Optional<Moderation> moderation

AUTO("auto")

LOW("low")

Optional<Long> outputCompression

minimum0

maximum100

Optional<OutputFormat> outputFormat

PNG("png")

WEBP("webp")

JPEG("jpeg")

Optional<Long> partialImages

minimum0

maximum3

Optional<Quality> quality

LOW("low")

MEDIUM("medium")

HIGH("high")

AUTO("auto")

Optional<Size> size

\_1024X1024("1024x1024")

\_1024X1536("1024x1536")

\_1536X1024("1536x1024")

AUTO("auto")

JsonValue;

JsonValue; type "local\_shell"constant"local\_shell"constant

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool:

JsonValue; type "shell"constant"shell"constant

Optional<List<AllowedCaller>> allowedCallers

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Environment> environment

class BetaContainerAuto:

JsonValue; type "container\_auto"constant"container\_auto"constant

Optional<List<String>> fileIds

Optional<MemoryLimit> memoryLimit

\_1G("1g")

\_4G("4g")

\_16G("16g")

\_64G("64g")

Optional<NetworkPolicy> networkPolicy

class BetaContainerNetworkPolicyDisabled:

JsonValue; type "disabled"constant"disabled"constant

class BetaContainerNetworkPolicyAllowlist:

List<String> allowedDomains

JsonValue; type "allowlist"constant"allowlist"constant

Optional<List<[BetaContainerNetworkPolicyDomainSecret](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))>> domainSecrets

String domain

minLength1

String name

minLength1

String value

maxLength10485760

minLength1

Optional<List<Skill>> skills

class BetaSkillReference:

String skillId

maxLength64

minLength1

JsonValue; type "skill\_reference"constant"skill\_reference"constant

Optional<String> version

class BetaInlineSkill:

String description

String name

[BetaInlineSkillSource](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema)) source

String data

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

JsonValue; mediaType "application/zip"constant"application/zip"constant

The media type of the inline skill payload. Must be `application/zip`.

JsonValue; type "base64"constant"base64"constant

The type of the inline skill source. Must be `base64`.

JsonValue; type "inline"constant"inline"constant

class BetaLocalEnvironment:

JsonValue; type "local"constant"local"constant

Optional<List<[BetaLocalSkill](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))>> skills

String description

String name

String path

class BetaContainerReference:

String containerId

JsonValue; type "container\_reference"constant"container\_reference"constant

class BetaCustomTool:

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

String name

JsonValue; type "custom"constant"custom"constant

Optional<List<AllowedCaller>> allowedCallers

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Optional<String> description

Optional<Format> format

JsonValue;

JsonValue; type "text"constant"text"constant

Unconstrained text format. Always `text`.

class Grammar:

String definition

Syntax syntax

LARK("lark")

REGEX("regex")

JsonValue; type "grammar"constant"grammar"constant

class BetaNamespaceTool:

String description

minLength1

String name

minLength1

List<Tool> tools

class Function:

String name

maxLength128

minLength1

JsonValue; type "function"constant"function"constant

Optional<List<AllowedCaller>> allowedCallers

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Optional<String> description

Optional<OutputSchema> outputSchema

Optional<JsonValue> parameters

Optional<Boolean> strict

class BetaCustomTool:

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

String name

JsonValue; type "custom"constant"custom"constant

Optional<List<AllowedCaller>> allowedCallers

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Optional<String> description

Optional<Format> format

JsonValue;

JsonValue; type "text"constant"text"constant

Unconstrained text format. Always `text`.

class Grammar:

String definition

Syntax syntax

LARK("lark")

REGEX("regex")

JsonValue; type "grammar"constant"grammar"constant

JsonValue; type "namespace"constant"namespace"constant

class BetaToolSearchTool:

JsonValue; type "tool\_search"constant"tool\_search"constant

Optional<String> description

Optional<Execution> execution

SERVER("server")

CLIENT("client")

Optional<JsonValue> parameters

class BetaWebSearchPreviewTool:

Type type

WEB\_SEARCH\_PREVIEW("web\_search\_preview")

WEB\_SEARCH\_PREVIEW\_2025\_03\_11("web\_search\_preview\_2025\_03\_11")

Optional<List<SearchContentType>> searchContentTypes

TEXT("text")

IMAGE("image")

Optional<SearchContextSize> searchContextSize

LOW("low")

MEDIUM("medium")

HIGH("high")

Optional<UserLocation> userLocation

JsonValue; type "approximate"constant"approximate"constant

Optional<String> city

Optional<String> country

Optional<String> region

Optional<String> timezone

class BetaApplyPatchTool:

JsonValue; type "apply\_patch"constant"apply\_patch"constant

Optional<List<AllowedCaller>> allowedCallers

DIRECT("direct")

PROGRAMMATIC("programmatic")

JsonValue; type "tool\_search\_output"constant"tool\_search\_output"constant

The item type. Always `tool_search_output`.

Optional<String> id

The unique ID of this tool search output.

Optional<Agent> agent

String agentName

Optional<String> callId

maxLength64

minLength1

Optional<Execution> execution

SERVER("server")

CLIENT("client")

Optional<Status> status

The status of the tool search output.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

AdditionalTools

JsonValue; role "developer"constant"developer"constant

The role that provided the additional tools. Only `developer` is supported.

List<[BetaTool](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))> tools

A list of additional tools made available at this item.

class BetaFunctionTool:

String name

Optional<Parameters> parameters

Optional<Boolean> strict

JsonValue; type "function"constant"function"constant

Optional<List<AllowedCaller>> allowedCallers

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Optional<String> description

Optional<OutputSchema> outputSchema

class BetaFileSearchTool:

JsonValue; type "file\_search"constant"file\_search"constant

List<String> vectorStoreIds

Optional<Filters> filters

class ComparisonFilter:

String key

Type type

EQ("eq")

NE("ne")

GT("gt")

GTE("gte")

LT("lt")

LTE("lte")

IN("in")

NIN("nin")

Value value

String

double

boolean

List<ComparisonFilterValueItem>

String

double

class CompoundFilter:

List<Filter> filters

class ComparisonFilter:

String key

Type type

EQ("eq")

NE("ne")

GT("gt")

GTE("gte")

LT("lt")

LTE("lte")

IN("in")

NIN("nin")

Value value

String

double

boolean

List<ComparisonFilterValueItem>

String

double

JsonValue

Type type

AND("and")

OR("or")

Optional<Long> maxNumResults

Optional<RankingOptions> rankingOptions

Optional<HybridSearch> hybridSearch

double embeddingWeight

double textWeight

Optional<Ranker> ranker

AUTO("auto")

DEFAULT\_2024\_11\_15("default-2024-11-15")

Optional<Double> scoreThreshold

class BetaComputerTool:

JsonValue; type "computer"constant"computer"constant

class BetaComputerUsePreviewTool:

long displayHeight

long displayWidth

Environment environment

WINDOWS("windows")

MAC("mac")

LINUX("linux")

UBUNTU("ubuntu")

BROWSER("browser")

JsonValue; type "computer\_use\_preview"constant"computer\_use\_preview"constant

class BetaWebSearchTool:

[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type type

WEB\_SEARCH("web\_search")

WEB\_SEARCH\_2025\_08\_26("web\_search\_2025\_08\_26")

Optional<Filters> filters

Optional<List<String>> allowedDomains

Optional<SearchContextSize> searchContextSize

LOW("low")

MEDIUM("medium")

HIGH("high")

Optional<UserLocation> userLocation

Optional<String> city

Optional<String> country

Optional<String> region

Optional<String> timezone

Optional<Type> type

Mcp

String serverLabel

JsonValue; type "mcp"constant"mcp"constant

Optional<List<AllowedCaller>> allowedCallers

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<AllowedTools> allowedTools

List<String>

class McpToolFilter:

Optional<Boolean> readOnly

Optional<List<String>> toolNames

Optional<String> authorization

Optional<ConnectorId> connectorId

about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

CONNECTOR\_DROPBOX("connector\_dropbox")

CONNECTOR\_GMAIL("connector\_gmail")

CONNECTOR\_GOOGLECALENDAR("connector\_googlecalendar")

CONNECTOR\_GOOGLEDRIVE("connector\_googledrive")

CONNECTOR\_MICROSOFTTEAMS("connector\_microsoftteams")

CONNECTOR\_OUTLOOKCALENDAR("connector\_outlookcalendar")

CONNECTOR\_OUTLOOKEMAIL("connector\_outlookemail")

CONNECTOR\_SHAREPOINT("connector\_sharepoint")

Optional<Boolean> deferLoading

Optional<Headers> headers

Optional<RequireApproval> requireApproval

class McpToolApprovalFilter:

Optional<Always> always

Optional<Boolean> readOnly

Optional<List<String>> toolNames

Optional<Never> never

Optional<Boolean> readOnly

Optional<List<String>> toolNames

enum McpToolApprovalSetting:

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

ALWAYS("always")

NEVER("never")

Optional<String> serverDescription

Optional<String> serverUrl

Optional<String> tunnelId

CodeInterpreter

Container container

String

class CodeInterpreterToolAuto:

JsonValue; type "auto"constant"auto"constant

Optional<List<String>> fileIds

Optional<MemoryLimit> memoryLimit

\_1G("1g")

\_4G("4g")

\_16G("16g")

\_64G("64g")

Optional<NetworkPolicy> networkPolicy

class BetaContainerNetworkPolicyDisabled:

JsonValue; type "disabled"constant"disabled"constant

class BetaContainerNetworkPolicyAllowlist:

List<String> allowedDomains

JsonValue; type "allowlist"constant"allowlist"constant

Optional<List<[BetaContainerNetworkPolicyDomainSecret](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))>> domainSecrets

String domain

minLength1

String name

minLength1

String value

maxLength10485760

minLength1

JsonValue; type "code\_interpreter"constant"code\_interpreter"constant

Optional<List<AllowedCaller>> allowedCallers

DIRECT("direct")

PROGRAMMATIC("programmatic")

JsonValue;

JsonValue; type "programmatic\_tool\_calling"constant"programmatic\_tool\_calling"constant

The type of the tool. Always `programmatic_tool_calling`.

ImageGeneration

JsonValue; type "image\_generation"constant"image\_generation"constant

Optional<Action> action

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

TRANSPARENT("transparent")

OPAQUE("opaque")

AUTO("auto")

Optional<InputFidelity> inputFidelity

HIGH("high")

LOW("low")

Optional<InputImageMask> inputImageMask

Optional<String> fileId

Optional<String> imageUrl

Optional<Model> model

GPT\_IMAGE\_1("gpt-image-1")

GPT\_IMAGE\_1\_MINI("gpt-image-1-mini")

GPT\_IMAGE\_2("gpt-image-2")

GPT\_IMAGE\_2\_2026\_04\_21("gpt-image-2-2026-04-21")

GPT\_IMAGE\_1\_5("gpt-image-1.5")

CHATGPT\_IMAGE\_LATEST("chatgpt-image-latest")

Optional<Moderation> moderation

AUTO("auto")

LOW("low")

Optional<Long> outputCompression

minimum0

maximum100

Optional<OutputFormat> outputFormat

PNG("png")

WEBP("webp")

JPEG("jpeg")

Optional<Long> partialImages

minimum0

maximum3

Optional<Quality> quality

LOW("low")

MEDIUM("medium")

HIGH("high")

AUTO("auto")

Optional<Size> size

\_1024X1024("1024x1024")

\_1024X1536("1024x1536")

\_1536X1024("1536x1024")

AUTO("auto")

JsonValue;

JsonValue; type "local\_shell"constant"local\_shell"constant

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool:

JsonValue; type "shell"constant"shell"constant

Optional<List<AllowedCaller>> allowedCallers

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Environment> environment

class BetaContainerAuto:

JsonValue; type "container\_auto"constant"container\_auto"constant

Optional<List<String>> fileIds

Optional<MemoryLimit> memoryLimit

\_1G("1g")

\_4G("4g")

\_16G("16g")

\_64G("64g")

Optional<NetworkPolicy> networkPolicy

class BetaContainerNetworkPolicyDisabled:

JsonValue; type "disabled"constant"disabled"constant

class BetaContainerNetworkPolicyAllowlist:

List<String> allowedDomains

JsonValue; type "allowlist"constant"allowlist"constant

Optional<List<[BetaContainerNetworkPolicyDomainSecret](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))>> domainSecrets

String domain

minLength1

String name

minLength1

String value

maxLength10485760

minLength1

Optional<List<Skill>> skills

class BetaSkillReference:

String skillId

maxLength64

minLength1

JsonValue; type "skill\_reference"constant"skill\_reference"constant

Optional<String> version

class BetaInlineSkill:

String description

String name

[BetaInlineSkillSource](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema)) source

String data

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

JsonValue; mediaType "application/zip"constant"application/zip"constant

The media type of the inline skill payload. Must be `application/zip`.

JsonValue; type "base64"constant"base64"constant

The type of the inline skill source. Must be `base64`.

JsonValue; type "inline"constant"inline"constant

class BetaLocalEnvironment:

JsonValue; type "local"constant"local"constant

Optional<List<[BetaLocalSkill](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))>> skills

String description

String name

String path

class BetaContainerReference:

String containerId

JsonValue; type "container\_reference"constant"container\_reference"constant

class BetaCustomTool:

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

String name

JsonValue; type "custom"constant"custom"constant

Optional<List<AllowedCaller>> allowedCallers

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Optional<String> description

Optional<Format> format

JsonValue;

JsonValue; type "text"constant"text"constant

Unconstrained text format. Always `text`.

class Grammar:

String definition

Syntax syntax

LARK("lark")

REGEX("regex")

JsonValue; type "grammar"constant"grammar"constant

class BetaNamespaceTool:

String description

minLength1

String name

minLength1

List<Tool> tools

class Function:

String name

maxLength128

minLength1

JsonValue; type "function"constant"function"constant

Optional<List<AllowedCaller>> allowedCallers

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Optional<String> description

Optional<OutputSchema> outputSchema

Optional<JsonValue> parameters

Optional<Boolean> strict

class BetaCustomTool:

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

String name

JsonValue; type "custom"constant"custom"constant

Optional<List<AllowedCaller>> allowedCallers

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Optional<String> description

Optional<Format> format

JsonValue;

JsonValue; type "text"constant"text"constant

Unconstrained text format. Always `text`.

class Grammar:

String definition

Syntax syntax

LARK("lark")

REGEX("regex")

JsonValue; type "grammar"constant"grammar"constant

JsonValue; type "namespace"constant"namespace"constant

class BetaToolSearchTool:

JsonValue; type "tool\_search"constant"tool\_search"constant

Optional<String> description

Optional<Execution> execution

SERVER("server")

CLIENT("client")

Optional<JsonValue> parameters

class BetaWebSearchPreviewTool:

Type type

WEB\_SEARCH\_PREVIEW("web\_search\_preview")

WEB\_SEARCH\_PREVIEW\_2025\_03\_11("web\_search\_preview\_2025\_03\_11")

Optional<List<SearchContentType>> searchContentTypes

TEXT("text")

IMAGE("image")

Optional<SearchContextSize> searchContextSize

LOW("low")

MEDIUM("medium")

HIGH("high")

Optional<UserLocation> userLocation

JsonValue; type "approximate"constant"approximate"constant

Optional<String> city

Optional<String> country

Optional<String> region

Optional<String> timezone

class BetaApplyPatchTool:

JsonValue; type "apply\_patch"constant"apply\_patch"constant

Optional<List<AllowedCaller>> allowedCallers

DIRECT("direct")

PROGRAMMATIC("programmatic")

JsonValue; type "additional\_tools"constant"additional\_tools"constant

The item type. Always `additional_tools`.

Optional<String> id

The unique ID of this additional tools item.

Optional<Agent> agent

String agentName

class BetaResponseReasoningItem:

[managing context](https://platform.openai.com/docs/guides/conversation-state).

String id

List<Summary> summary

String text

JsonValue; type "summary\_text"constant"summary\_text"constant

JsonValue; type "reasoning"constant"reasoning"constant

Optional<Agent> agent

String agentName

Optional<List<Content>> content

String text

JsonValue; type "reasoning\_text"constant"reasoning\_text"constant

Optional<String> encryptedContent

Optional<Status> status

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

class BetaResponseCompactionItemParam:

A compaction item generated by the [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).

String encryptedContent

The encrypted content of the compaction summary.

maxLength10485760

JsonValue; type "compaction"constant"compaction"constant

Optional<String> id

The ID of the compaction item.

Optional<Agent> agent

String agentName

ImageGenerationCall

String id

Optional<String> result

Status status

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

GENERATING("generating")

FAILED("failed")

JsonValue; type "image\_generation\_call"constant"image\_generation\_call"constant

Optional<Agent> agent

String agentName

class BetaResponseCodeInterpreterToolCall:

String id

Optional<String> code

String containerId

Optional<List<Output>> outputs

class Logs:

String logs

JsonValue; type "logs"constant"logs"constant

class Image:

JsonValue; type "image"constant"image"constant

String url

Status status

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

INTERPRETING("interpreting")

FAILED("failed")

JsonValue; type "code\_interpreter\_call"constant"code\_interpreter\_call"constant

Optional<Agent> agent

String agentName

LocalShellCall

String id

Action action

List<String> command

Env env

JsonValue; type "exec"constant"exec"constant

Optional<Long> timeoutMs

Optional<String> user

Optional<String> workingDirectory

String callId

Status status

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

JsonValue; type "local\_shell\_call"constant"local\_shell\_call"constant

Optional<Agent> agent

String agentName

LocalShellCallOutput

String id

String output

JsonValue; type "local\_shell\_call\_output"constant"local\_shell\_call\_output"constant

Optional<Agent> agent

String agentName

Optional<Status> status

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

ShellCall

Action action

List<String> commands

Ordered shell commands for the execution environment to run.

Optional<Long> maxOutputLength

Maximum number of UTF-8 characters to capture from combined stdout and stderr output.

Optional<Long> timeoutMs

Maximum wall-clock time in milliseconds to allow the shell commands to run.

String callId

maxLength64

minLength1

JsonValue; type "shell\_call"constant"shell\_call"constant

Optional<String> id

Optional<Agent> agent

String agentName

Optional<Caller> caller

JsonValue;

JsonValue; type "direct"constant"direct"constant

The caller type. Always `direct`.

class Program:

String callerId

maxLength64

minLength1

JsonValue; type "program"constant"program"constant

Optional<Environment> environment

The environment to execute the shell commands in.

class BetaLocalEnvironment:

JsonValue; type "local"constant"local"constant

Optional<List<[BetaLocalSkill](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))>> skills

String description

String name

String path

class BetaContainerReference:

String containerId

JsonValue; type "container\_reference"constant"container\_reference"constant

Optional<Status> status

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

ShellCallOutput

String callId

maxLength64

minLength1

List<[BetaResponseFunctionShellCallOutputContent](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_shell_call_output_content%20%3E%20(schema))> output

Captured chunks of stdout and stderr output, along with their associated outcomes.

Outcome outcome

The exit or timeout outcome associated with this shell call.

JsonValue;

JsonValue; type "timeout"constant"timeout"constant

The outcome type. Always `timeout`.

class Exit:

long exitCode

The exit code returned by the shell process.

JsonValue; type "exit"constant"exit"constant

String stderr

Captured stderr output for the shell call.

maxLength10485760

String stdout

Captured stdout output for the shell call.

maxLength10485760

JsonValue; type "shell\_call\_output"constant"shell\_call\_output"constant

The type of the item. Always `shell_call_output`.

Optional<String> id

The unique ID of the shell tool call output. Populated when this item is returned via API.

Optional<Agent> agent

String agentName

Optional<Caller> caller

JsonValue;

JsonValue; type "direct"constant"direct"constant

The caller type. Always `direct`.

class Program:

String callerId

maxLength64

minLength1

JsonValue; type "program"constant"program"constant

Optional<Long> maxOutputLength

The maximum number of UTF-8 characters captured for this shell call’s combined output.

Optional<Status> status

The status of the shell call output.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

ApplyPatchCall

String callId

maxLength64

minLength1

Operation operation

The specific create, delete, or update instruction for the apply\_patch tool call.

class CreateFile:

Instruction for creating a new file via the apply\_patch tool.

String diff

Unified diff content to apply when creating the file.

maxLength10485760

String path

Path of the file to create relative to the workspace root.

minLength1

JsonValue; type "create\_file"constant"create\_file"constant

The operation type. Always `create_file`.

class DeleteFile:

Instruction for deleting an existing file via the apply\_patch tool.

String path

Path of the file to delete relative to the workspace root.

minLength1

JsonValue; type "delete\_file"constant"delete\_file"constant

The operation type. Always `delete_file`.

class UpdateFile:

Instruction for updating an existing file via the apply\_patch tool.

String diff

Unified diff content to apply to the existing file.

maxLength10485760

String path

Path of the file to update relative to the workspace root.

minLength1

JsonValue; type "update\_file"constant"update\_file"constant

The operation type. Always `update_file`.

Status status

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

JsonValue; type "apply\_patch\_call"constant"apply\_patch\_call"constant

Optional<String> id

Optional<Agent> agent

String agentName

Optional<Caller> caller

JsonValue;

JsonValue; type "direct"constant"direct"constant

The caller type. Always `direct`.

class Program:

String callerId

maxLength64

minLength1

JsonValue; type "program"constant"program"constant

ApplyPatchCallOutput

String callId

maxLength64

minLength1

Status status

COMPLETED("completed")

FAILED("failed")

JsonValue; type "apply\_patch\_call\_output"constant"apply\_patch\_call\_output"constant

Optional<String> id

Optional<Agent> agent

String agentName

Optional<Caller> caller

JsonValue;

JsonValue; type "direct"constant"direct"constant

The caller type. Always `direct`.

class Program:

String callerId

maxLength64

minLength1

JsonValue; type "program"constant"program"constant

Optional<String> output

Optional human-readable log text from the apply patch tool (e.g., patch results or errors).

maxLength10485760

McpListTools

String id

String serverLabel

List<Tool> tools

JsonValue inputSchema

String name

Optional<JsonValue> annotations

Optional<String> description

JsonValue; type "mcp\_list\_tools"constant"mcp\_list\_tools"constant

Optional<Agent> agent

String agentName

Optional<String> error

McpApprovalRequest

String id

String arguments

String name

String serverLabel

JsonValue; type "mcp\_approval\_request"constant"mcp\_approval\_request"constant

Optional<Agent> agent

String agentName

McpApprovalResponse

String approvalRequestId

boolean approve

JsonValue; type "mcp\_approval\_response"constant"mcp\_approval\_response"constant

Optional<String> id

Optional<Agent> agent

String agentName

Optional<String> reason

McpCall

String id

String arguments

String name

String serverLabel

JsonValue; type "mcp\_call"constant"mcp\_call"constant

Optional<Agent> agent

String agentName

Optional<String> approvalRequestId

Optional<String> error

Optional<String> output

Optional<Status> status

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

CALLING("calling")

FAILED("failed")

class BetaResponseCustomToolCallOutput:

String callId

The call ID, used to map this custom tool call output to a custom tool call.

Output output

The output from the custom tool call generated by your code.

String

List<BetaFunctionAndCustomToolCallOutput>

class BetaResponseInputText:

String text

JsonValue; type "input\_text"constant"input\_text"constant

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

JsonValue; mode "explicit"constant"explicit"constant

class BetaResponseInputImage:

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

Detail detail

LOW("low")

HIGH("high")

AUTO("auto")

ORIGINAL("original")

JsonValue; type "input\_image"constant"input\_image"constant

Optional<String> fileId

Optional<String> imageUrl

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

JsonValue; mode "explicit"constant"explicit"constant

class BetaResponseInputFile:

JsonValue; type "input\_file"constant"input\_file"constant

Optional<Detail> detail

AUTO("auto")

LOW("low")

HIGH("high")

Optional<String> fileData

Optional<String> fileId

Optional<String> fileUrl

Optional<String> filename

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

JsonValue; mode "explicit"constant"explicit"constant

JsonValue; type "custom\_tool\_call\_output"constant"custom\_tool\_call\_output"constant

The type of the custom tool call output. Always `custom_tool_call_output`.

Optional<String> id

The unique ID of the custom tool call output in the OpenAI platform.

Optional<Agent> agent

String agentName

Optional<Caller> caller

JsonValue;

JsonValue; type "direct"constant"direct"constant

The caller type. Always `direct`.

class Program:

String callerId

maxLength64

minLength1

JsonValue; type "program"constant"program"constant

class BetaResponseCustomToolCall:

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

Optional<Agent> agent

String agentName

Optional<Caller> caller

JsonValue;

JsonValue; type "direct"constant"direct"constant

class Program:

String callerId

JsonValue; type "program"constant"program"constant

Optional<String> namespace

The namespace of the custom tool being called.

CompactionTrigger

JsonValue; type "compaction\_trigger"constant"compaction\_trigger"constant

The type of the item. Always `compaction_trigger`.

Optional<Agent> agent

String agentName

ItemReference

String id

The ID of the item to reference.

Optional<Agent> agent

String agentName

Optional<Type> type

The type of item to reference. Always `item_reference`.

Program

String id

The unique ID of this program item.

String callId

maxLength64

minLength1

String code

maxLength10485760

String fingerprint

maxLength10485760

JsonValue; type "program"constant"program"constant

The item type. Always `program`.

Optional<Agent> agent

String agentName

ProgramOutput

String id

The unique ID of this program output item.

String callId

maxLength64

minLength1

String result

maxLength10485760

Status status

The terminal status of the program output.

COMPLETED("completed")

INCOMPLETE("incomplete")

JsonValue; type "program\_output"constant"program\_output"constant

The item type. Always `program_output`.

Optional<Agent> agent

String agentName

Optional<String> instructions

A system (or developer) message inserted into the model’s context.
When used along with `previous_response_id`, the instructions from a previous response will not be carried over to the next response. This makes it simple to swap out system (or developer) messages in new responses.

Optional<String> previousResponseId

The unique ID of the previous response to the model. Use this to create multi-turn conversations. Learn more about [conversation state](https://platform.openai.com/docs/guides/conversation-state). Cannot be used in conjunction with `conversation`.

Optional<String> promptCacheKey

A key to use when reading from or writing to the prompt cache.

maxLength64

Optional<PromptCacheOptions> promptCacheOptions

Options for prompt caching. Supported for `gpt-5.6` and later models. By default, OpenAI automatically chooses one implicit cache breakpoint. You can add explicit breakpoints to content blocks with `prompt_cache_breakpoint`. Each request can write up to four breakpoints. For cache matching, OpenAI considers up to the latest 80 breakpoints in the conversation, without a content-block lookback limit. Set `mode` to `explicit` to disable the implicit breakpoint. The `ttl` defaults to `30m`, which is currently the only supported value. See the [prompt caching guide](https://platform.openai.com/docs/guides/prompt-caching) for current details.

Optional<Mode> mode

Controls whether OpenAI automatically creates an implicit cache breakpoint. Defaults to `implicit`. With `implicit`, OpenAI creates one implicit breakpoint and writes up to the latest three explicit breakpoints in the request. With `explicit`, OpenAI does not create an implicit breakpoint and writes up to the latest four explicit breakpoints. If there are no explicit breakpoints, the request does not use prompt caching.

IMPLICIT("implicit")

EXPLICIT("explicit")

Optional<Ttl> ttl

The minimum lifetime applied to every implicit and explicit cache breakpoint written by the request. Defaults to `30m`, which is currently the only supported value. The backend may retain cache entries for longer.

DeprecatedOptional<PromptCacheRetention> promptCacheRetention

How long to retain a prompt cache entry created by this request.

IN\_MEMORY("in\_memory")

\_24H("24h")

Optional<ServiceTier> serviceTier

The service tier to use for this request.

AUTO("auto")

DEFAULT("default")

FLEX("flex")

PRIORITY("priority")

##### ReturnsExpand Collapse

class BetaCompactedResponse:

String id

The unique identifier for the compacted response.

long createdAt

Unix timestamp (in seconds) when the compacted conversation was created.

formatunixtime

JsonValue; object\_ "response.compaction"constant"response.compaction"constant

The object type. Always `response.compaction`.

List<[BetaResponseOutputItem](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_item%20%3E%20(schema))> output

The compacted list of output items. This is a list of all user messages, followed by a single compaction item.

class BetaResponseOutputMessage:

String id

List<Content> content

class BetaResponseOutputText:

List<Annotation> annotations

class FileCitation:

String fileId

String filename

long index

JsonValue; type "file\_citation"constant"file\_citation"constant

class UrlCitation:

long endIndex

long startIndex

String title

JsonValue; type "url\_citation"constant"url\_citation"constant

String url

class ContainerFileCitation:

String containerId

long endIndex

String fileId

String filename

long startIndex

JsonValue; type "container\_file\_citation"constant"container\_file\_citation"constant

class FilePath:

String fileId

long index

JsonValue; type "file\_path"constant"file\_path"constant

String text

JsonValue; type "output\_text"constant"output\_text"constant

Optional<List<Logprob>> logprobs

String token

List<long> bytes

double logprob

List<TopLogprob> topLogprobs

String token

List<long> bytes

double logprob

class BetaResponseOutputRefusal:

String refusal

JsonValue; type "refusal"constant"refusal"constant

JsonValue; role "assistant"constant"assistant"constant

Status status

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

JsonValue; type "message"constant"message"constant

Optional<Agent> agent

String agentName

Optional<Phase> phase

COMMENTARY("commentary")

FINAL\_ANSWER("final\_answer")

class BetaResponseFileSearchToolCall:

[file search guide](https://platform.openai.com/docs/guides/tools-file-search) for more information.

String id

List<String> queries

Status status

IN\_PROGRESS("in\_progress")

SEARCHING("searching")

COMPLETED("completed")

INCOMPLETE("incomplete")

FAILED("failed")

JsonValue; type "file\_search\_call"constant"file\_search\_call"constant

Optional<Agent> agent

String agentName

Optional<List<Result>> results

Optional<Attributes> attributes

String

double

boolean

Optional<String> fileId

Optional<String> filename

Optional<Double> score

formatfloat

Optional<String> text

class BetaResponseFunctionToolCall:

[function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.

String arguments

A JSON string of the arguments to pass to the function.

String callId

String name

The name of the function to run.

JsonValue; type "function\_call"constant"function\_call"constant

The type of the function tool call. Always `function_call`.

Optional<String> id

Optional<Agent> agent

String agentName

Optional<Caller> caller

JsonValue;

JsonValue; type "direct"constant"direct"constant

class Program:

String callerId

JsonValue; type "program"constant"program"constant

Optional<String> namespace

The namespace of the function to run.

Optional<Status> status

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

class BetaResponseFunctionToolCallOutputItem:

String id

The unique ID of the function call tool output.

String callId

Output output

The output from the function call generated by your code.

String

List<BetaFunctionAndCustomToolCallOutput>

class BetaResponseInputText:

String text

JsonValue; type "input\_text"constant"input\_text"constant

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

JsonValue; mode "explicit"constant"explicit"constant

class BetaResponseInputImage:

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

Detail detail

LOW("low")

HIGH("high")

AUTO("auto")

ORIGINAL("original")

JsonValue; type "input\_image"constant"input\_image"constant

Optional<String> fileId

Optional<String> imageUrl

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

JsonValue; mode "explicit"constant"explicit"constant

class BetaResponseInputFile:

JsonValue; type "input\_file"constant"input\_file"constant

Optional<Detail> detail

AUTO("auto")

LOW("low")

HIGH("high")

Optional<String> fileData

Optional<String> fileId

Optional<String> fileUrl

Optional<String> filename

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

JsonValue; mode "explicit"constant"explicit"constant

Status status

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

JsonValue; type "function\_call\_output"constant"function\_call\_output"constant

Optional<Agent> agent

String agentName

Optional<Caller> caller

JsonValue;

JsonValue; type "direct"constant"direct"constant

The caller type. Always `direct`.

class Program:

String callerId

maxLength64

minLength1

JsonValue; type "program"constant"program"constant

Optional<String> createdBy

The identifier of the actor that created the item.

AgentMessage

String id

The unique ID of the agent message.

String author

List<Content> content

Encrypted content sent between agents.

class BetaResponseInputText:

String text

JsonValue; type "input\_text"constant"input\_text"constant

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

JsonValue; mode "explicit"constant"explicit"constant

class BetaResponseOutputText:

List<Annotation> annotations

class FileCitation:

String fileId

String filename

long index

JsonValue; type "file\_citation"constant"file\_citation"constant

class UrlCitation:

long endIndex

long startIndex

String title

JsonValue; type "url\_citation"constant"url\_citation"constant

String url

class ContainerFileCitation:

String containerId

long endIndex

String fileId

String filename

long startIndex

JsonValue; type "container\_file\_citation"constant"container\_file\_citation"constant

class FilePath:

String fileId

long index

JsonValue; type "file\_path"constant"file\_path"constant

String text

JsonValue; type "output\_text"constant"output\_text"constant

Optional<List<Logprob>> logprobs

String token

List<long> bytes

double logprob

List<TopLogprob> topLogprobs

String token

List<long> bytes

double logprob

class Text:

A text content.

String text

JsonValue; type "text"constant"text"constant

class SummaryText:

A summary text from the model.

String text

JsonValue; type "summary\_text"constant"summary\_text"constant

class ReasoningText:

String text

JsonValue; type "reasoning\_text"constant"reasoning\_text"constant

class BetaResponseOutputRefusal:

String refusal

JsonValue; type "refusal"constant"refusal"constant

class BetaResponseInputImage:

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

Detail detail

LOW("low")

HIGH("high")

AUTO("auto")

ORIGINAL("original")

JsonValue; type "input\_image"constant"input\_image"constant

Optional<String> fileId

Optional<String> imageUrl

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

JsonValue; mode "explicit"constant"explicit"constant

class ComputerScreenshot:

A screenshot of a computer.

Detail detail

The detail level of the screenshot image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

LOW("low")

HIGH("high")

AUTO("auto")

ORIGINAL("original")

Optional<String> fileId

Optional<String> imageUrl

JsonValue; type "computer\_screenshot"constant"computer\_screenshot"constant

Specifies the event type. For a computer screenshot, this property is always set to `computer_screenshot`.

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

JsonValue; mode "explicit"constant"explicit"constant

class BetaResponseInputFile:

JsonValue; type "input\_file"constant"input\_file"constant

Optional<Detail> detail

AUTO("auto")

LOW("low")

HIGH("high")

Optional<String> fileData

Optional<String> fileId

Optional<String> fileUrl

Optional<String> filename

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

JsonValue; mode "explicit"constant"explicit"constant

class EncryptedContent:

String encryptedContent

JsonValue; type "encrypted\_content"constant"encrypted\_content"constant

String recipient

JsonValue; type "agent\_message"constant"agent\_message"constant

The type of the item. Always `agent_message`.

Optional<Agent> agent

String agentName

MultiAgentCall

String id

The unique ID of the multi-agent call item.

Action action

The multi-agent action to execute.

SPAWN\_AGENT("spawn\_agent")

INTERRUPT\_AGENT("interrupt\_agent")

LIST\_AGENTS("list\_agents")

SEND\_MESSAGE("send\_message")

FOLLOWUP\_TASK("followup\_task")

WAIT\_AGENT("wait\_agent")

String arguments

The JSON string of arguments generated for the action.

String callId

JsonValue; type "multi\_agent\_call"constant"multi\_agent\_call"constant

The type of the multi-agent call. Always `multi_agent_call`.

Optional<Agent> agent

String agentName

MultiAgentCallOutput

String id

The unique ID of the multi-agent call output item.

Action action

SPAWN\_AGENT("spawn\_agent")

INTERRUPT\_AGENT("interrupt\_agent")

LIST\_AGENTS("list\_agents")

SEND\_MESSAGE("send\_message")

FOLLOWUP\_TASK("followup\_task")

WAIT\_AGENT("wait\_agent")

String callId

List<[BetaResponseOutputText](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_text%20%3E%20(schema))> output

List<Annotation> annotations

class FileCitation:

String fileId

String filename

long index

JsonValue; type "file\_citation"constant"file\_citation"constant

class UrlCitation:

long endIndex

long startIndex

String title

JsonValue; type "url\_citation"constant"url\_citation"constant

String url

class ContainerFileCitation:

String containerId

long endIndex

String fileId

String filename

long startIndex

JsonValue; type "container\_file\_citation"constant"container\_file\_citation"constant

class FilePath:

String fileId

long index

JsonValue; type "file\_path"constant"file\_path"constant

String text

JsonValue; type "output\_text"constant"output\_text"constant

Optional<List<Logprob>> logprobs

String token

List<long> bytes

double logprob

List<TopLogprob> topLogprobs

String token

List<long> bytes

double logprob

JsonValue; type "multi\_agent\_call\_output"constant"multi\_agent\_call\_output"constant

The type of the multi-agent result. Always `multi_agent_call_output`.

Optional<Agent> agent

String agentName

class BetaResponseFunctionWebSearch:

[web search guide](https://platform.openai.com/docs/guides/tools-web-search) for more information.

String id

Action action

class Search:

JsonValue; type "search"constant"search"constant

Optional<List<String>> queries

DeprecatedOptional<String> query

Optional<List<Source>> sources

JsonValue; type "url"constant"url"constant

String url

class OpenPage:

JsonValue; type "open\_page"constant"open\_page"constant

Optional<String> url

class FindInPage:

String pattern

JsonValue; type "find\_in\_page"constant"find\_in\_page"constant

String url

Status status

IN\_PROGRESS("in\_progress")

SEARCHING("searching")

COMPLETED("completed")

FAILED("failed")

JsonValue; type "web\_search\_call"constant"web\_search\_call"constant

Optional<Agent> agent

String agentName

class BetaResponseComputerToolCall:

[computer use guide](https://platform.openai.com/docs/guides/tools-computer-use) for more information.

String id

String callId

List<PendingSafetyCheck> pendingSafetyChecks

String id

Optional<String> code

Optional<String> message

Status status

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

Type type

Optional<[BetaComputerAction](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_computer_action%20%3E%20(schema))> action

Click

Button button

Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

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

  { x: 100, y: 200 },
  { x: 200, y: 300 }

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

Optional<List<[BetaComputerAction](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_computer_action%20%3E%20(schema))>> actions

Click

Button button

Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

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

  { x: 100, y: 200 },
  { x: 200, y: 300 }

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

Optional<Agent> agent

String agentName

class BetaResponseComputerToolCallOutputItem:

String id

The unique ID of the computer call tool output.

String callId

[BetaResponseComputerToolCallOutputScreenshot](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_computer_tool_call_output_screenshot%20%3E%20(schema)) output

JsonValue; type "computer\_screenshot"constant"computer\_screenshot"constant

Specifies the event type. For a computer screenshot, this property is
always set to `computer_screenshot`.

Optional<String> fileId

Optional<String> imageUrl

Status status

COMPLETED("completed")

INCOMPLETE("incomplete")

FAILED("failed")

IN\_PROGRESS("in\_progress")

JsonValue; type "computer\_call\_output"constant"computer\_call\_output"constant

Optional<List<AcknowledgedSafetyCheck>> acknowledgedSafetyChecks

The safety checks reported by the API that have been acknowledged by the
developer.

String id

Optional<String> code

Optional<String> message

Optional<Agent> agent

String agentName

Optional<String> createdBy

The identifier of the actor that created the item.

class BetaResponseReasoningItem:

[managing context](https://platform.openai.com/docs/guides/conversation-state).

String id

List<Summary> summary

String text

JsonValue; type "summary\_text"constant"summary\_text"constant

JsonValue; type "reasoning"constant"reasoning"constant

Optional<Agent> agent

String agentName

Optional<List<Content>> content

String text

JsonValue; type "reasoning\_text"constant"reasoning\_text"constant

Optional<String> encryptedContent

Optional<Status> status

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

Program

String id

The unique ID of the program item.

String callId

String code

String fingerprint

JsonValue; type "program"constant"program"constant

The type of the item. Always `program`.

Optional<Agent> agent

String agentName

ProgramOutput

String id

The unique ID of the program output item.

String callId

String result

Status status

The terminal status of the program output item.

COMPLETED("completed")

INCOMPLETE("incomplete")

JsonValue; type "program\_output"constant"program\_output"constant

The type of the item. Always `program_output`.

Optional<Agent> agent

String agentName

class BetaResponseToolSearchCall:

String id

The unique ID of the tool search call item.

JsonValue arguments

Arguments used for the tool search call.

Optional<String> callId

Execution execution

SERVER("server")

CLIENT("client")

Status status

The status of the tool search call item that was recorded.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

JsonValue; type "tool\_search\_call"constant"tool\_search\_call"constant

The type of the item. Always `tool_search_call`.

Optional<Agent> agent

String agentName

Optional<String> createdBy

The identifier of the actor that created the item.

class BetaResponseToolSearchOutputItem:

String id

The unique ID of the tool search output item.

Optional<String> callId

Execution execution

SERVER("server")

CLIENT("client")

Status status

The status of the tool search output item that was recorded.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

List<[BetaTool](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))> tools

The loaded tool definitions returned by tool search.

class BetaFunctionTool:

String name

Optional<Parameters> parameters

Optional<Boolean> strict

JsonValue; type "function"constant"function"constant

Optional<List<AllowedCaller>> allowedCallers

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Optional<String> description

Optional<OutputSchema> outputSchema

class BetaFileSearchTool:

JsonValue; type "file\_search"constant"file\_search"constant

List<String> vectorStoreIds

Optional<Filters> filters

class ComparisonFilter:

String key

Type type

EQ("eq")

NE("ne")

GT("gt")

GTE("gte")

LT("lt")

LTE("lte")

IN("in")

NIN("nin")

Value value

String

double

boolean

List<ComparisonFilterValueItem>

String

double

class CompoundFilter:

List<Filter> filters

class ComparisonFilter:

String key

Type type

EQ("eq")

NE("ne")

GT("gt")

GTE("gte")

LT("lt")

LTE("lte")

IN("in")

NIN("nin")

Value value

String

double

boolean

List<ComparisonFilterValueItem>

String

double

JsonValue

Type type

AND("and")

OR("or")

Optional<Long> maxNumResults

Optional<RankingOptions> rankingOptions

Optional<HybridSearch> hybridSearch

double embeddingWeight

double textWeight

Optional<Ranker> ranker

AUTO("auto")

DEFAULT\_2024\_11\_15("default-2024-11-15")

Optional<Double> scoreThreshold

class BetaComputerTool:

JsonValue; type "computer"constant"computer"constant

class BetaComputerUsePreviewTool:

long displayHeight

long displayWidth

Environment environment

WINDOWS("windows")

MAC("mac")

LINUX("linux")

UBUNTU("ubuntu")

BROWSER("browser")

JsonValue; type "computer\_use\_preview"constant"computer\_use\_preview"constant

class BetaWebSearchTool:

[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type type

WEB\_SEARCH("web\_search")

WEB\_SEARCH\_2025\_08\_26("web\_search\_2025\_08\_26")

Optional<Filters> filters

Optional<List<String>> allowedDomains

Optional<SearchContextSize> searchContextSize

LOW("low")

MEDIUM("medium")

HIGH("high")

Optional<UserLocation> userLocation

Optional<String> city

Optional<String> country

Optional<String> region

Optional<String> timezone

Optional<Type> type

Mcp

String serverLabel

JsonValue; type "mcp"constant"mcp"constant

Optional<List<AllowedCaller>> allowedCallers

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<AllowedTools> allowedTools

List<String>

class McpToolFilter:

Optional<Boolean> readOnly

Optional<List<String>> toolNames

Optional<String> authorization

Optional<ConnectorId> connectorId

about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

CONNECTOR\_DROPBOX("connector\_dropbox")

CONNECTOR\_GMAIL("connector\_gmail")

CONNECTOR\_GOOGLECALENDAR("connector\_googlecalendar")

CONNECTOR\_GOOGLEDRIVE("connector\_googledrive")

CONNECTOR\_MICROSOFTTEAMS("connector\_microsoftteams")

CONNECTOR\_OUTLOOKCALENDAR("connector\_outlookcalendar")

CONNECTOR\_OUTLOOKEMAIL("connector\_outlookemail")

CONNECTOR\_SHAREPOINT("connector\_sharepoint")

Optional<Boolean> deferLoading

Optional<Headers> headers

Optional<RequireApproval> requireApproval

class McpToolApprovalFilter:

Optional<Always> always

Optional<Boolean> readOnly

Optional<List<String>> toolNames

Optional<Never> never

Optional<Boolean> readOnly

Optional<List<String>> toolNames

enum McpToolApprovalSetting:

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

ALWAYS("always")

NEVER("never")

Optional<String> serverDescription

Optional<String> serverUrl

Optional<String> tunnelId

CodeInterpreter

Container container

String

class CodeInterpreterToolAuto:

JsonValue; type "auto"constant"auto"constant

Optional<List<String>> fileIds

Optional<MemoryLimit> memoryLimit

\_1G("1g")

\_4G("4g")

\_16G("16g")

\_64G("64g")

Optional<NetworkPolicy> networkPolicy

class BetaContainerNetworkPolicyDisabled:

JsonValue; type "disabled"constant"disabled"constant

class BetaContainerNetworkPolicyAllowlist:

List<String> allowedDomains

JsonValue; type "allowlist"constant"allowlist"constant

Optional<List<[BetaContainerNetworkPolicyDomainSecret](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))>> domainSecrets

String domain

minLength1

String name

minLength1

String value

maxLength10485760

minLength1

JsonValue; type "code\_interpreter"constant"code\_interpreter"constant

Optional<List<AllowedCaller>> allowedCallers

DIRECT("direct")

PROGRAMMATIC("programmatic")

JsonValue;

JsonValue; type "programmatic\_tool\_calling"constant"programmatic\_tool\_calling"constant

The type of the tool. Always `programmatic_tool_calling`.

ImageGeneration

JsonValue; type "image\_generation"constant"image\_generation"constant

Optional<Action> action

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

TRANSPARENT("transparent")

OPAQUE("opaque")

AUTO("auto")

Optional<InputFidelity> inputFidelity

HIGH("high")

LOW("low")

Optional<InputImageMask> inputImageMask

Optional<String> fileId

Optional<String> imageUrl

Optional<Model> model

GPT\_IMAGE\_1("gpt-image-1")

GPT\_IMAGE\_1\_MINI("gpt-image-1-mini")

GPT\_IMAGE\_2("gpt-image-2")

GPT\_IMAGE\_2\_2026\_04\_21("gpt-image-2-2026-04-21")

GPT\_IMAGE\_1\_5("gpt-image-1.5")

CHATGPT\_IMAGE\_LATEST("chatgpt-image-latest")

Optional<Moderation> moderation

AUTO("auto")

LOW("low")

Optional<Long> outputCompression

minimum0

maximum100

Optional<OutputFormat> outputFormat

PNG("png")

WEBP("webp")

JPEG("jpeg")

Optional<Long> partialImages

minimum0

maximum3

Optional<Quality> quality

LOW("low")

MEDIUM("medium")

HIGH("high")

AUTO("auto")

Optional<Size> size

\_1024X1024("1024x1024")

\_1024X1536("1024x1536")

\_1536X1024("1536x1024")

AUTO("auto")

JsonValue;

JsonValue; type "local\_shell"constant"local\_shell"constant

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool:

JsonValue; type "shell"constant"shell"constant

Optional<List<AllowedCaller>> allowedCallers

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Environment> environment

class BetaContainerAuto:

JsonValue; type "container\_auto"constant"container\_auto"constant

Optional<List<String>> fileIds

Optional<MemoryLimit> memoryLimit

\_1G("1g")

\_4G("4g")

\_16G("16g")

\_64G("64g")

Optional<NetworkPolicy> networkPolicy

class BetaContainerNetworkPolicyDisabled:

JsonValue; type "disabled"constant"disabled"constant

class BetaContainerNetworkPolicyAllowlist:

List<String> allowedDomains

JsonValue; type "allowlist"constant"allowlist"constant

Optional<List<[BetaContainerNetworkPolicyDomainSecret](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))>> domainSecrets

String domain

minLength1

String name

minLength1

String value

maxLength10485760

minLength1

Optional<List<Skill>> skills

class BetaSkillReference:

String skillId

maxLength64

minLength1

JsonValue; type "skill\_reference"constant"skill\_reference"constant

Optional<String> version

class BetaInlineSkill:

String description

String name

[BetaInlineSkillSource](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema)) source

String data

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

JsonValue; mediaType "application/zip"constant"application/zip"constant

The media type of the inline skill payload. Must be `application/zip`.

JsonValue; type "base64"constant"base64"constant

The type of the inline skill source. Must be `base64`.

JsonValue; type "inline"constant"inline"constant

class BetaLocalEnvironment:

JsonValue; type "local"constant"local"constant

Optional<List<[BetaLocalSkill](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))>> skills

String description

String name

String path

class BetaContainerReference:

String containerId

JsonValue; type "container\_reference"constant"container\_reference"constant

class BetaCustomTool:

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

String name

JsonValue; type "custom"constant"custom"constant

Optional<List<AllowedCaller>> allowedCallers

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Optional<String> description

Optional<Format> format

JsonValue;

JsonValue; type "text"constant"text"constant

Unconstrained text format. Always `text`.

class Grammar:

String definition

Syntax syntax

LARK("lark")

REGEX("regex")

JsonValue; type "grammar"constant"grammar"constant

class BetaNamespaceTool:

String description

minLength1

String name

minLength1

List<Tool> tools

class Function:

String name

maxLength128

minLength1

JsonValue; type "function"constant"function"constant

Optional<List<AllowedCaller>> allowedCallers

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Optional<String> description

Optional<OutputSchema> outputSchema

Optional<JsonValue> parameters

Optional<Boolean> strict

class BetaCustomTool:

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

String name

JsonValue; type "custom"constant"custom"constant

Optional<List<AllowedCaller>> allowedCallers

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Optional<String> description

Optional<Format> format

JsonValue;

JsonValue; type "text"constant"text"constant

Unconstrained text format. Always `text`.

class Grammar:

String definition

Syntax syntax

LARK("lark")

REGEX("regex")

JsonValue; type "grammar"constant"grammar"constant

JsonValue; type "namespace"constant"namespace"constant

class BetaToolSearchTool:

JsonValue; type "tool\_search"constant"tool\_search"constant

Optional<String> description

Optional<Execution> execution

SERVER("server")

CLIENT("client")

Optional<JsonValue> parameters

class BetaWebSearchPreviewTool:

Type type

WEB\_SEARCH\_PREVIEW("web\_search\_preview")

WEB\_SEARCH\_PREVIEW\_2025\_03\_11("web\_search\_preview\_2025\_03\_11")

Optional<List<SearchContentType>> searchContentTypes

TEXT("text")

IMAGE("image")

Optional<SearchContextSize> searchContextSize

LOW("low")

MEDIUM("medium")

HIGH("high")

Optional<UserLocation> userLocation

JsonValue; type "approximate"constant"approximate"constant

Optional<String> city

Optional<String> country

Optional<String> region

Optional<String> timezone

class BetaApplyPatchTool:

JsonValue; type "apply\_patch"constant"apply\_patch"constant

Optional<List<AllowedCaller>> allowedCallers

DIRECT("direct")

PROGRAMMATIC("programmatic")

JsonValue; type "tool\_search\_output"constant"tool\_search\_output"constant

The type of the item. Always `tool_search_output`.

Optional<Agent> agent

String agentName

Optional<String> createdBy

The identifier of the actor that created the item.

AdditionalTools

String id

The unique ID of the additional tools item.

Role role

The role that provided the additional tools.

UNKNOWN("unknown")

USER("user")

ASSISTANT("assistant")

SYSTEM("system")

CRITIC("critic")

DISCRIMINATOR("discriminator")

DEVELOPER("developer")

TOOL("tool")

List<[BetaTool](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))> tools

The additional tool definitions made available at this item.

class BetaFunctionTool:

String name

Optional<Parameters> parameters

Optional<Boolean> strict

JsonValue; type "function"constant"function"constant

Optional<List<AllowedCaller>> allowedCallers

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Optional<String> description

Optional<OutputSchema> outputSchema

class BetaFileSearchTool:

JsonValue; type "file\_search"constant"file\_search"constant

List<String> vectorStoreIds

Optional<Filters> filters

class ComparisonFilter:

String key

Type type

EQ("eq")

NE("ne")

GT("gt")

GTE("gte")

LT("lt")

LTE("lte")

IN("in")

NIN("nin")

Value value

String

double

boolean

List<ComparisonFilterValueItem>

String

double

class CompoundFilter:

List<Filter> filters

class ComparisonFilter:

String key

Type type

EQ("eq")

NE("ne")

GT("gt")

GTE("gte")

LT("lt")

LTE("lte")

IN("in")

NIN("nin")

Value value

String

double

boolean

List<ComparisonFilterValueItem>

String

double

JsonValue

Type type

AND("and")

OR("or")

Optional<Long> maxNumResults

Optional<RankingOptions> rankingOptions

Optional<HybridSearch> hybridSearch

double embeddingWeight

double textWeight

Optional<Ranker> ranker

AUTO("auto")

DEFAULT\_2024\_11\_15("default-2024-11-15")

Optional<Double> scoreThreshold

class BetaComputerTool:

JsonValue; type "computer"constant"computer"constant

class BetaComputerUsePreviewTool:

long displayHeight

long displayWidth

Environment environment

WINDOWS("windows")

MAC("mac")

LINUX("linux")

UBUNTU("ubuntu")

BROWSER("browser")

JsonValue; type "computer\_use\_preview"constant"computer\_use\_preview"constant

class BetaWebSearchTool:

[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type type

WEB\_SEARCH("web\_search")

WEB\_SEARCH\_2025\_08\_26("web\_search\_2025\_08\_26")

Optional<Filters> filters

Optional<List<String>> allowedDomains

Optional<SearchContextSize> searchContextSize

LOW("low")

MEDIUM("medium")

HIGH("high")

Optional<UserLocation> userLocation

Optional<String> city

Optional<String> country

Optional<String> region

Optional<String> timezone

Optional<Type> type

Mcp

String serverLabel

JsonValue; type "mcp"constant"mcp"constant

Optional<List<AllowedCaller>> allowedCallers

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<AllowedTools> allowedTools

List<String>

class McpToolFilter:

Optional<Boolean> readOnly

Optional<List<String>> toolNames

Optional<String> authorization

Optional<ConnectorId> connectorId

about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

CONNECTOR\_DROPBOX("connector\_dropbox")

CONNECTOR\_GMAIL("connector\_gmail")

CONNECTOR\_GOOGLECALENDAR("connector\_googlecalendar")

CONNECTOR\_GOOGLEDRIVE("connector\_googledrive")

CONNECTOR\_MICROSOFTTEAMS("connector\_microsoftteams")

CONNECTOR\_OUTLOOKCALENDAR("connector\_outlookcalendar")

CONNECTOR\_OUTLOOKEMAIL("connector\_outlookemail")

CONNECTOR\_SHAREPOINT("connector\_sharepoint")

Optional<Boolean> deferLoading

Optional<Headers> headers

Optional<RequireApproval> requireApproval

class McpToolApprovalFilter:

Optional<Always> always

Optional<Boolean> readOnly

Optional<List<String>> toolNames

Optional<Never> never

Optional<Boolean> readOnly

Optional<List<String>> toolNames

enum McpToolApprovalSetting:

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

ALWAYS("always")

NEVER("never")

Optional<String> serverDescription

Optional<String> serverUrl

Optional<String> tunnelId

CodeInterpreter

Container container

String

class CodeInterpreterToolAuto:

JsonValue; type "auto"constant"auto"constant

Optional<List<String>> fileIds

Optional<MemoryLimit> memoryLimit

\_1G("1g")

\_4G("4g")

\_16G("16g")

\_64G("64g")

Optional<NetworkPolicy> networkPolicy

class BetaContainerNetworkPolicyDisabled:

JsonValue; type "disabled"constant"disabled"constant

class BetaContainerNetworkPolicyAllowlist:

List<String> allowedDomains

JsonValue; type "allowlist"constant"allowlist"constant

Optional<List<[BetaContainerNetworkPolicyDomainSecret](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))>> domainSecrets

String domain

minLength1

String name

minLength1

String value

maxLength10485760

minLength1

JsonValue; type "code\_interpreter"constant"code\_interpreter"constant

Optional<List<AllowedCaller>> allowedCallers

DIRECT("direct")

PROGRAMMATIC("programmatic")

JsonValue;

JsonValue; type "programmatic\_tool\_calling"constant"programmatic\_tool\_calling"constant

The type of the tool. Always `programmatic_tool_calling`.

ImageGeneration

JsonValue; type "image\_generation"constant"image\_generation"constant

Optional<Action> action

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

TRANSPARENT("transparent")

OPAQUE("opaque")

AUTO("auto")

Optional<InputFidelity> inputFidelity

HIGH("high")

LOW("low")

Optional<InputImageMask> inputImageMask

Optional<String> fileId

Optional<String> imageUrl

Optional<Model> model

GPT\_IMAGE\_1("gpt-image-1")

GPT\_IMAGE\_1\_MINI("gpt-image-1-mini")

GPT\_IMAGE\_2("gpt-image-2")

GPT\_IMAGE\_2\_2026\_04\_21("gpt-image-2-2026-04-21")

GPT\_IMAGE\_1\_5("gpt-image-1.5")

CHATGPT\_IMAGE\_LATEST("chatgpt-image-latest")

Optional<Moderation> moderation

AUTO("auto")

LOW("low")

Optional<Long> outputCompression

minimum0

maximum100

Optional<OutputFormat> outputFormat

PNG("png")

WEBP("webp")

JPEG("jpeg")

Optional<Long> partialImages

minimum0

maximum3

Optional<Quality> quality

LOW("low")

MEDIUM("medium")

HIGH("high")

AUTO("auto")

Optional<Size> size

\_1024X1024("1024x1024")

\_1024X1536("1024x1536")

\_1536X1024("1536x1024")

AUTO("auto")

JsonValue;

JsonValue; type "local\_shell"constant"local\_shell"constant

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool:

JsonValue; type "shell"constant"shell"constant

Optional<List<AllowedCaller>> allowedCallers

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Environment> environment

class BetaContainerAuto:

JsonValue; type "container\_auto"constant"container\_auto"constant

Optional<List<String>> fileIds

Optional<MemoryLimit> memoryLimit

\_1G("1g")

\_4G("4g")

\_16G("16g")

\_64G("64g")

Optional<NetworkPolicy> networkPolicy

class BetaContainerNetworkPolicyDisabled:

JsonValue; type "disabled"constant"disabled"constant

class BetaContainerNetworkPolicyAllowlist:

List<String> allowedDomains

JsonValue; type "allowlist"constant"allowlist"constant

Optional<List<[BetaContainerNetworkPolicyDomainSecret](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))>> domainSecrets

String domain

minLength1

String name

minLength1

String value

maxLength10485760

minLength1

Optional<List<Skill>> skills

class BetaSkillReference:

String skillId

maxLength64

minLength1

JsonValue; type "skill\_reference"constant"skill\_reference"constant

Optional<String> version

class BetaInlineSkill:

String description

String name

[BetaInlineSkillSource](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema)) source

String data

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

JsonValue; mediaType "application/zip"constant"application/zip"constant

The media type of the inline skill payload. Must be `application/zip`.

JsonValue; type "base64"constant"base64"constant

The type of the inline skill source. Must be `base64`.

JsonValue; type "inline"constant"inline"constant

class BetaLocalEnvironment:

JsonValue; type "local"constant"local"constant

Optional<List<[BetaLocalSkill](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))>> skills

String description

String name

String path

class BetaContainerReference:

String containerId

JsonValue; type "container\_reference"constant"container\_reference"constant

class BetaCustomTool:

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

String name

JsonValue; type "custom"constant"custom"constant

Optional<List<AllowedCaller>> allowedCallers

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Optional<String> description

Optional<Format> format

JsonValue;

JsonValue; type "text"constant"text"constant

Unconstrained text format. Always `text`.

class Grammar:

String definition

Syntax syntax

LARK("lark")

REGEX("regex")

JsonValue; type "grammar"constant"grammar"constant

class BetaNamespaceTool:

String description

minLength1

String name

minLength1

List<Tool> tools

class Function:

String name

maxLength128

minLength1

JsonValue; type "function"constant"function"constant

Optional<List<AllowedCaller>> allowedCallers

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Optional<String> description

Optional<OutputSchema> outputSchema

Optional<JsonValue> parameters

Optional<Boolean> strict

class BetaCustomTool:

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

String name

JsonValue; type "custom"constant"custom"constant

Optional<List<AllowedCaller>> allowedCallers

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Optional<String> description

Optional<Format> format

JsonValue;

JsonValue; type "text"constant"text"constant

Unconstrained text format. Always `text`.

class Grammar:

String definition

Syntax syntax

LARK("lark")

REGEX("regex")

JsonValue; type "grammar"constant"grammar"constant

JsonValue; type "namespace"constant"namespace"constant

class BetaToolSearchTool:

JsonValue; type "tool\_search"constant"tool\_search"constant

Optional<String> description

Optional<Execution> execution

SERVER("server")

CLIENT("client")

Optional<JsonValue> parameters

class BetaWebSearchPreviewTool:

Type type

WEB\_SEARCH\_PREVIEW("web\_search\_preview")

WEB\_SEARCH\_PREVIEW\_2025\_03\_11("web\_search\_preview\_2025\_03\_11")

Optional<List<SearchContentType>> searchContentTypes

TEXT("text")

IMAGE("image")

Optional<SearchContextSize> searchContextSize

LOW("low")

MEDIUM("medium")

HIGH("high")

Optional<UserLocation> userLocation

JsonValue; type "approximate"constant"approximate"constant

Optional<String> city

Optional<String> country

Optional<String> region

Optional<String> timezone

class BetaApplyPatchTool:

JsonValue; type "apply\_patch"constant"apply\_patch"constant

Optional<List<AllowedCaller>> allowedCallers

DIRECT("direct")

PROGRAMMATIC("programmatic")

JsonValue; type "additional\_tools"constant"additional\_tools"constant

The type of the item. Always `additional_tools`.

Optional<Agent> agent

String agentName

class BetaResponseCompactionItem:

A compaction item generated by the [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).

String id

The unique ID of the compaction item.

String encryptedContent

The encrypted content that was produced by compaction.

JsonValue; type "compaction"constant"compaction"constant

Optional<Agent> agent

String agentName

Optional<String> createdBy

The identifier of the actor that created the item.

ImageGenerationCall

String id

Optional<String> result

Status status

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

GENERATING("generating")

FAILED("failed")

JsonValue; type "image\_generation\_call"constant"image\_generation\_call"constant

Optional<Agent> agent

String agentName

class BetaResponseCodeInterpreterToolCall:

String id

Optional<String> code

String containerId

Optional<List<Output>> outputs

class Logs:

String logs

JsonValue; type "logs"constant"logs"constant

class Image:

JsonValue; type "image"constant"image"constant

String url

Status status

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

INTERPRETING("interpreting")

FAILED("failed")

JsonValue; type "code\_interpreter\_call"constant"code\_interpreter\_call"constant

Optional<Agent> agent

String agentName

LocalShellCall

String id

Action action

List<String> command

Env env

JsonValue; type "exec"constant"exec"constant

Optional<Long> timeoutMs

Optional<String> user

Optional<String> workingDirectory

String callId

Status status

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

JsonValue; type "local\_shell\_call"constant"local\_shell\_call"constant

Optional<Agent> agent

String agentName

LocalShellCallOutput

String id

String output

JsonValue; type "local\_shell\_call\_output"constant"local\_shell\_call\_output"constant

Optional<Agent> agent

String agentName

Optional<Status> status

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

class BetaResponseFunctionShellToolCall:

A tool call that executes one or more shell commands in a managed environment.

String id

Action action

List<String> commands

Optional<Long> maxOutputLength

Optional maximum number of characters to return from each command.

Optional<Long> timeoutMs

Optional timeout in milliseconds for the commands.

String callId

Optional<Environment> environment

Represents the use of a local environment to perform shell actions.

class BetaResponseLocalEnvironment:

Represents the use of a local environment to perform shell actions.

JsonValue; type "local"constant"local"constant

The environment type. Always `local`.

class BetaResponseContainerReference:

Represents a container created with /v1/containers.

String containerId

JsonValue; type "container\_reference"constant"container\_reference"constant

The environment type. Always `container_reference`.

Status status

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

JsonValue; type "shell\_call"constant"shell\_call"constant

Optional<Agent> agent

String agentName

Optional<Caller> caller

JsonValue;

JsonValue; type "direct"constant"direct"constant

class Program:

String callerId

JsonValue; type "program"constant"program"constant

Optional<String> createdBy

The ID of the entity that created this tool call.

class BetaResponseFunctionShellToolCallOutput:

The output of a shell tool call that was emitted.

String id

The unique ID of the shell call output. Populated when this item is returned via API.

String callId

Optional<Long> maxOutputLength

The maximum length of the shell command output. This is generated by the model and should be passed back with the raw output.

List<Output> output

An array of shell call output contents

Outcome outcome

Represents either an exit outcome (with an exit code) or a timeout outcome for a shell call output chunk.

JsonValue;

JsonValue; type "timeout"constant"timeout"constant

The outcome type. Always `timeout`.

class Exit:

long exitCode

Exit code from the shell process.

JsonValue; type "exit"constant"exit"constant

String stderr

The standard error output that was captured.

String stdout

The standard output that was captured.

Optional<String> createdBy

The identifier of the actor that created the item.

Status status

The status of the shell call output. One of `in_progress`, `completed`, or `incomplete`.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

JsonValue; type "shell\_call\_output"constant"shell\_call\_output"constant

The type of the shell call output. Always `shell_call_output`.

Optional<Agent> agent

String agentName

Optional<Caller> caller

JsonValue;

JsonValue; type "direct"constant"direct"constant

class Program:

String callerId

JsonValue; type "program"constant"program"constant

Optional<String> createdBy

The identifier of the actor that created the item.

class BetaResponseApplyPatchToolCall:

A tool call that applies file diffs by creating, deleting, or updating files.

String id

String callId

Operation operation

One of the create\_file, delete\_file, or update\_file operations applied via apply\_patch.

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

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

JsonValue; type "apply\_patch\_call"constant"apply\_patch\_call"constant

Optional<Agent> agent

String agentName

Optional<Caller> caller

JsonValue;

JsonValue; type "direct"constant"direct"constant

class Program:

String callerId

JsonValue; type "program"constant"program"constant

Optional<String> createdBy

The ID of the entity that created this tool call.

class BetaResponseApplyPatchToolCallOutput:

The output emitted by an apply patch tool call.

String id

String callId

Status status

COMPLETED("completed")

FAILED("failed")

JsonValue; type "apply\_patch\_call\_output"constant"apply\_patch\_call\_output"constant

Optional<Agent> agent

String agentName

Optional<Caller> caller

JsonValue;

JsonValue; type "direct"constant"direct"constant

class Program:

String callerId

JsonValue; type "program"constant"program"constant

Optional<String> createdBy

The ID of the entity that created this tool call output.

Optional<String> output

Optional textual output returned by the apply patch tool.

McpCall

String id

String arguments

String name

String serverLabel

JsonValue; type "mcp\_call"constant"mcp\_call"constant

Optional<Agent> agent

String agentName

Optional<String> approvalRequestId

Optional<String> error

Optional<String> output

Optional<Status> status

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

CALLING("calling")

FAILED("failed")

McpListTools

String id

String serverLabel

List<Tool> tools

JsonValue inputSchema

String name

Optional<JsonValue> annotations

Optional<String> description

JsonValue; type "mcp\_list\_tools"constant"mcp\_list\_tools"constant

Optional<Agent> agent

String agentName

Optional<String> error

McpApprovalRequest

String id

String arguments

String name

String serverLabel

JsonValue; type "mcp\_approval\_request"constant"mcp\_approval\_request"constant

Optional<Agent> agent

String agentName

McpApprovalResponse

String id

String approvalRequestId

boolean approve

JsonValue; type "mcp\_approval\_response"constant"mcp\_approval\_response"constant

Optional<Agent> agent

String agentName

Optional<String> reason

class BetaResponseCustomToolCall:

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

Optional<Agent> agent

String agentName

Optional<Caller> caller

JsonValue;

JsonValue; type "direct"constant"direct"constant

class Program:

String callerId

JsonValue; type "program"constant"program"constant

Optional<String> namespace

The namespace of the custom tool being called.

class BetaResponseCustomToolCallOutputItem:

String id

The unique ID of the custom tool call output item.

Status status

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

Optional<String> createdBy

The identifier of the actor that created the item.

[BetaResponseUsage](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_usage%20%3E%20(schema)) usage

Token accounting for the compaction pass, including cached, reasoning, and total tokens.

long inputTokens

The number of input tokens.

InputTokensDetails inputTokensDetails

A detailed breakdown of the input tokens.

long cacheWriteTokens

The number of input tokens that were written to the cache.

long cachedTokens

The number of tokens that were retrieved from the cache.
[More on prompt caching](https://platform.openai.com/docs/guides/prompt-caching).

long outputTokens

The number of output tokens.

OutputTokensDetails outputTokensDetails

A detailed breakdown of the output tokens.

long reasoningTokens

The number of reasoning tokens.

long totalTokens

The total number of tokens used.

### Compact a response

Java

package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.responses.BetaCompactedResponse;
import com.openai.models.beta.responses.ResponseCompactParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ResponseCompactParams params = ResponseCompactParams.builder()
            .model(ResponseCompactParams.Model.GPT_5_6_SOL)
            .build();
        BetaCompactedResponse betaCompactedResponse = client.beta().responses().compact(params);

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
