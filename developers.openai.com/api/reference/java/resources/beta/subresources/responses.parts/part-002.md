<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/responses/ -->
<!-- part of: https://developers.openai.com/api/reference/java/resources/beta/subresources/responses/ -->

<!-- chunk-start -->

Emitted when there is an additional text delta.

long contentIndex

The index of the content part that the text delta was added to.

String delta

The text delta that was added.

String itemId

The ID of the output item that the text delta was added to.

List<Logprob> logprobs

The log probabilities of the tokens in the delta.

String token

A possible text token.

double logprob

The log probability of this token.

Optional<List<TopLogprob>> topLogprobs

The log probabilities of up to 20 of the most likely tokens.

Optional<String> token

A possible text token.

Optional<Double> logprob

The log probability of this token.

long outputIndex

The index of the output item that the text delta was added to.

long sequenceNumber

The sequence number for this event.

JsonValue; type "response.output\_text.delta"constant"response.output\_text.delta"constant

The type of the event. Always `response.output_text.delta`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseTextDoneEvent:

Emitted when text content is finalized.

long contentIndex

The index of the content part that the text content is finalized.

String itemId

The ID of the output item that the text content is finalized.

List<Logprob> logprobs

The log probabilities of the tokens in the delta.

String token

A possible text token.

double logprob

The log probability of this token.

Optional<List<TopLogprob>> topLogprobs

The log probabilities of up to 20 of the most likely tokens.

Optional<String> token

A possible text token.

Optional<Double> logprob

The log probability of this token.

long outputIndex

The index of the output item that the text content is finalized.

long sequenceNumber

The sequence number for this event.

String text

The text content that is finalized.

JsonValue; type "response.output\_text.done"constant"response.output\_text.done"constant

The type of the event. Always `response.output_text.done`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseWebSearchCallCompletedEvent:

Emitted when a web search call is completed.

String itemId

Unique ID for the output item associated with the web search call.

long outputIndex

The index of the output item that the web search call is associated with.

long sequenceNumber

The sequence number of the web search call being processed.

JsonValue; type "response.web\_search\_call.completed"constant"response.web\_search\_call.completed"constant

The type of the event. Always `response.web_search_call.completed`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseWebSearchCallInProgressEvent:

Emitted when a web search call is initiated.

String itemId

Unique ID for the output item associated with the web search call.

long outputIndex

The index of the output item that the web search call is associated with.

long sequenceNumber

The sequence number of the web search call being processed.

JsonValue; type "response.web\_search\_call.in\_progress"constant"response.web\_search\_call.in\_progress"constant

The type of the event. Always `response.web_search_call.in_progress`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseWebSearchCallSearchingEvent:

Emitted when a web search call is executing.

String itemId

Unique ID for the output item associated with the web search call.

long outputIndex

The index of the output item that the web search call is associated with.

long sequenceNumber

The sequence number of the web search call being processed.

JsonValue; type "response.web\_search\_call.searching"constant"response.web\_search\_call.searching"constant

The type of the event. Always `response.web_search_call.searching`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseImageGenCallCompletedEvent:

Emitted when an image generation tool call has completed and the final image is available.

String itemId

The unique identifier of the image generation item being processed.

long outputIndex

The index of the output item in the response’s output array.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.image\_generation\_call.completed"constant"response.image\_generation\_call.completed"constant

The type of the event. Always ‘response.image\_generation\_call.completed’.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseImageGenCallGeneratingEvent:

Emitted when an image generation tool call is actively generating an image (intermediate state).

String itemId

The unique identifier of the image generation item being processed.

long outputIndex

The index of the output item in the response’s output array.

long sequenceNumber

The sequence number of the image generation item being processed.

JsonValue; type "response.image\_generation\_call.generating"constant"response.image\_generation\_call.generating"constant

The type of the event. Always ‘response.image\_generation\_call.generating’.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseImageGenCallInProgressEvent:

Emitted when an image generation tool call is in progress.

String itemId

The unique identifier of the image generation item being processed.

long outputIndex

The index of the output item in the response’s output array.

long sequenceNumber

The sequence number of the image generation item being processed.

JsonValue; type "response.image\_generation\_call.in\_progress"constant"response.image\_generation\_call.in\_progress"constant

The type of the event. Always ‘response.image\_generation\_call.in\_progress’.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseImageGenCallPartialImageEvent:

Emitted when a partial image is available during image generation streaming.

String itemId

The unique identifier of the image generation item being processed.

long outputIndex

The index of the output item in the response’s output array.

String partialImageB64

Base64-encoded partial image data, suitable for rendering as an image.

long partialImageIndex

0-based index for the partial image (backend is 1-based, but this is 0-based for the user).

long sequenceNumber

The sequence number of the image generation item being processed.

JsonValue; type "response.image\_generation\_call.partial\_image"constant"response.image\_generation\_call.partial\_image"constant

The type of the event. Always ‘response.image\_generation\_call.partial\_image’.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseMcpCallArgumentsDeltaEvent:

Emitted when there is a delta (partial update) to the arguments of an MCP tool call.

String delta

A JSON string containing the partial update to the arguments for the MCP tool call.

String itemId

The unique identifier of the MCP tool call item being processed.

long outputIndex

The index of the output item in the response’s output array.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.mcp\_call\_arguments.delta"constant"response.mcp\_call\_arguments.delta"constant

The type of the event. Always ‘response.mcp\_call\_arguments.delta’.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseMcpCallArgumentsDoneEvent:

Emitted when the arguments for an MCP tool call are finalized.

String arguments

A JSON string containing the finalized arguments for the MCP tool call.

String itemId

The unique identifier of the MCP tool call item being processed.

long outputIndex

The index of the output item in the response’s output array.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.mcp\_call\_arguments.done"constant"response.mcp\_call\_arguments.done"constant

The type of the event. Always ‘response.mcp\_call\_arguments.done’.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseMcpCallCompletedEvent:

Emitted when an MCP tool call has completed successfully.

String itemId

The ID of the MCP tool call item that completed.

long outputIndex

The index of the output item that completed.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.mcp\_call.completed"constant"response.mcp\_call.completed"constant

The type of the event. Always ‘response.mcp\_call.completed’.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseMcpCallFailedEvent:

Emitted when an MCP tool call has failed.

String itemId

The ID of the MCP tool call item that failed.

long outputIndex

The index of the output item that failed.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.mcp\_call.failed"constant"response.mcp\_call.failed"constant

The type of the event. Always ‘response.mcp\_call.failed’.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseMcpCallInProgressEvent:

Emitted when an MCP tool call is in progress.

String itemId

The unique identifier of the MCP tool call item being processed.

long outputIndex

The index of the output item in the response’s output array.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.mcp\_call.in\_progress"constant"response.mcp\_call.in\_progress"constant

The type of the event. Always ‘response.mcp\_call.in\_progress’.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseMcpListToolsCompletedEvent:

Emitted when the list of available MCP tools has been successfully retrieved.

String itemId

The ID of the MCP tool call item that produced this output.

long outputIndex

The index of the output item that was processed.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.mcp\_list\_tools.completed"constant"response.mcp\_list\_tools.completed"constant

The type of the event. Always ‘response.mcp\_list\_tools.completed’.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseMcpListToolsFailedEvent:

Emitted when the attempt to list available MCP tools has failed.

String itemId

The ID of the MCP tool call item that failed.

long outputIndex

The index of the output item that failed.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.mcp\_list\_tools.failed"constant"response.mcp\_list\_tools.failed"constant

The type of the event. Always ‘response.mcp\_list\_tools.failed’.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseMcpListToolsInProgressEvent:

Emitted when the system is in the process of retrieving the list of available MCP tools.

String itemId

The ID of the MCP tool call item that is being processed.

long outputIndex

The index of the output item that is being processed.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.mcp\_list\_tools.in\_progress"constant"response.mcp\_list\_tools.in\_progress"constant

The type of the event. Always ‘response.mcp\_list\_tools.in\_progress’.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseOutputTextAnnotationAddedEvent:

Emitted when an annotation is added to output text content.

JsonValue annotation

The annotation object being added. (See annotation schema for details.)

long annotationIndex

The index of the annotation within the content part.

long contentIndex

The index of the content part within the output item.

String itemId

The unique identifier of the item to which the annotation is being added.

long outputIndex

The index of the output item in the response’s output array.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.output\_text.annotation.added"constant"response.output\_text.annotation.added"constant

The type of the event. Always ‘response.output\_text.annotation.added’.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseQueuedEvent:

Emitted when a response is queued and waiting to be processed.

[BetaResponse](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema)) response

The full response object that is queued.

long sequenceNumber

The sequence number for this event.

JsonValue; type "response.queued"constant"response.queued"constant

The type of the event. Always ‘response.queued’.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseCustomToolCallInputDeltaEvent:

Event representing a delta (partial update) to the input of a custom tool call.

String delta

The incremental input data (delta) for the custom tool call.

String itemId

Unique identifier for the API item associated with this event.

long outputIndex

The index of the output this delta applies to.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.custom\_tool\_call\_input.delta"constant"response.custom\_tool\_call\_input.delta"constant

The event type identifier.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseCustomToolCallInputDoneEvent:

Event indicating that input for a custom tool call is complete.

String input

The complete input data for the custom tool call.

String itemId

Unique identifier for the API item associated with this event.

long outputIndex

The index of the output this event applies to.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.custom\_tool\_call\_input.done"constant"response.custom\_tool\_call\_input.done"constant

The event type identifier.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseInjectCreatedEvent:

Emitted when all injected input items were validated and committed to the
active response.

String responseId

The ID of the response that accepted the input.

long sequenceNumber

The sequence number for this event.

JsonValue; type "response.inject.created"constant"response.inject.created"constant

The event discriminator. Always `response.inject.created`.

Optional<String> streamId

The multiplexed WebSocket stream that emitted the event. This field is
present only when WebSocket multiplexing is enabled separately.

class BetaResponseInjectFailedEvent:

Emitted when injected input could not be committed to a response. The event
returns the uncommitted raw input so the client can retry it in another
response when appropriate.

Error error

Information about why the input was not committed.

Code code

A machine-readable error code.

RESPONSE\_ALREADY\_COMPLETED("response\_already\_completed")

RESPONSE\_NOT\_FOUND("response\_not\_found")

String message

A human-readable description of the error.

List<[BetaResponseInputItem](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_item%20%3E%20(schema))> input

The raw input items that were not committed.

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

String responseId

The ID of the response that rejected the input.

long sequenceNumber

The sequence number for this event.

JsonValue; type "response.inject.failed"constant"response.inject.failed"constant

The event discriminator. Always `response.inject.failed`.

Optional<String> streamId

The multiplexed WebSocket stream that emitted the event. This field is
present only when WebSocket multiplexing is enabled separately.

class BetaSkillReference:

String skillId

maxLength64

minLength1

JsonValue; type "skill\_reference"constant"skill\_reference"constant

Optional<String> version

class BetaTool: A class that can be one of several variants.union

A tool that can be used to generate a response.

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

class BetaToolChoiceAllowed:

Constrains the tools available to the model to a pre-defined set.

Mode mode

Constrains the tools available to the model to a pre-defined set.

`auto` allows the model to pick from among the allowed tools and generate a
message.

`required` requires the model to call one or more of the allowed tools.

AUTO("auto")

REQUIRED("required")

List<Tool> tools

A list of tool definitions that the model should be allowed to call.

For the Responses API, the list of tool definitions might look like:

  { "type": "function", "name": "get_weather" },
  { "type": "mcp", "server_label": "deepwiki" },
  { "type": "image_generation" }

JsonValue; type "allowed\_tools"constant"allowed\_tools"constant

Allowed tool configuration type. Always `allowed_tools`.

class BetaToolChoiceApplyPatch:

Forces the model to call the apply\_patch tool when executing a tool call.

JsonValue; type "apply\_patch"constant"apply\_patch"constant

The tool to call. Always `apply_patch`.

class BetaToolChoiceCustom:

Use this option to force the model to call a specific custom tool.

String name

The name of the custom tool to call.

JsonValue; type "custom"constant"custom"constant

For custom tool calling, the type is always `custom`.

class BetaToolChoiceFunction:

Use this option to force the model to call a specific function.

String name

JsonValue; type "function"constant"function"constant

For function calling, the type is always `function`.

class BetaToolChoiceMcp:

Use this option to force the model to call a specific tool on a remote MCP server.

String serverLabel

The label of the MCP server to use.

JsonValue; type "mcp"constant"mcp"constant

For MCP tools, the type is always `mcp`.

Optional<String> name

The name of the tool to call on the server.

enum BetaToolChoiceOptions:

Controls which (if any) tool is called by the model.

`none` means the model will not call any tool and instead generates a message.

`auto` means the model can pick between generating a message or calling one or
more tools.

`required` means the model must call one or more tools.

NONE("none")

AUTO("auto")

REQUIRED("required")

class BetaToolChoiceShell:

Forces the model to call the shell tool when a tool call is required.

JsonValue; type "shell"constant"shell"constant

The tool to call. Always `shell`.

class BetaToolChoiceTypes:

Indicates that the model should use a built-in tool to generate a response.
[Learn more about built-in tools](https://platform.openai.com/docs/guides/tools).

Type type

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

FILE\_SEARCH("file\_search")

WEB\_SEARCH\_PREVIEW("web\_search\_preview")

COMPUTER("computer")

COMPUTER\_USE\_PREVIEW("computer\_use\_preview")

COMPUTER\_USE("computer\_use")

WEB\_SEARCH\_PREVIEW\_2025\_03\_11("web\_search\_preview\_2025\_03\_11")

IMAGE\_GENERATION("image\_generation")

CODE\_INTERPRETER("code\_interpreter")

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

#### ResponsesInput Items

##### [List input items](/api/reference/java/resources/beta/subresources/responses/subresources/input_items/methods/list)

InputItemListPage beta().responses().inputItems().list(InputItemListParamsparams = InputItemListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/responses/{response\_id}/input\_items

##### ModelsExpand Collapse

class BetaResponseItemList:

A list of Response items.

List<[BetaResponseItem](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_item%20%3E%20(schema))> data

A list of items used to generate this response.

class BetaResponseInputMessageItem:

String id

The unique ID of the message input.

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

JsonValue; type "message"constant"message"constant

Optional<Agent> agent

String agentName

Optional<Status> status

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

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

class BetaResponseFunctionToolCallItem:

[function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.

String id

Status status

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

Optional<String> createdBy

The identifier of the actor that created the item.

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

class BetaResponseCustomToolCallItem:

String id

The unique ID of the custom tool call item.

Status status

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

Optional<String> createdBy

The identifier of the actor that created the item.

class BetaResponseCustomToolCallOutputItem:

String id

The unique ID of the custom tool call output item.

Status status

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

Optional<String> createdBy

The identifier of the actor that created the item.

String firstId

The ID of the first item in the list.

boolean hasMore

Whether there are more items available.

String lastId

The ID of the last item in the list.

JsonValue; object\_ "list"constant"list"constant

The type of object returned, must be `list`.

#### ResponsesInput Tokens

##### [Get input token counts](/api/reference/java/resources/beta/subresources/responses/subresources/input_tokens/methods/count)

[InputTokenCountResponse](/api/reference/java/resources/beta#(resource)%20beta.responses.input_tokens%20%3E%20(model)%20InputTokenCountResponse%20%3E%20(schema)) beta().responses().inputTokens().count(InputTokenCountParamsparams = InputTokenCountParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/responses/input\_tokens
