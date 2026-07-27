<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/responses/ -->
<!-- part of: https://developers.openai.com/api/reference/python/resources/beta/subresources/responses/ -->

<!-- chunk-start -->

The index of the output item this summary part is associated with.

part: Part

The summary part that was added.

text: str

The text of the summary part.

type: Literal["summary\_text"]

The type of the summary part. Always `summary_text`.

sequence\_number: int

The sequence number of this event.

summary\_index: int

The index of the summary part within the reasoning summary.

type: Literal["response.reasoning\_summary\_part.added"]

The type of the event. Always `response.reasoning_summary_part.added`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseReasoningSummaryPartDoneEvent: …

Emitted when a reasoning summary part is completed.

item\_id: str

The ID of the item this summary part is associated with.

output\_index: int

The index of the output item this summary part is associated with.

part: Part

The completed summary part.

text: str

The text of the summary part.

type: Literal["summary\_text"]

The type of the summary part. Always `summary_text`.

sequence\_number: int

The sequence number of this event.

summary\_index: int

The index of the summary part within the reasoning summary.

type: Literal["response.reasoning\_summary\_part.done"]

The type of the event. Always `response.reasoning_summary_part.done`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

status: Optional[Literal["incomplete"]]

The completion status of the summary part. Omitted when the part completed
normally and set to `incomplete` when generation was interrupted.

class BetaResponseReasoningSummaryTextDeltaEvent: …

Emitted when a delta is added to a reasoning summary text.

delta: str

The text delta that was added to the summary.

item\_id: str

The ID of the item this summary text delta is associated with.

output\_index: int

The index of the output item this summary text delta is associated with.

sequence\_number: int

The sequence number of this event.

summary\_index: int

The index of the summary part within the reasoning summary.

type: Literal["response.reasoning\_summary\_text.delta"]

The type of the event. Always `response.reasoning_summary_text.delta`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseReasoningSummaryTextDoneEvent: …

Emitted when a reasoning summary text is completed.

item\_id: str

The ID of the item this summary text is associated with.

output\_index: int

The index of the output item this summary text is associated with.

sequence\_number: int

The sequence number of this event.

summary\_index: int

The index of the summary part within the reasoning summary.

text: str

The full text of the completed reasoning summary.

type: Literal["response.reasoning\_summary\_text.done"]

The type of the event. Always `response.reasoning_summary_text.done`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseReasoningTextDeltaEvent: …

Emitted when a delta is added to a reasoning text.

content\_index: int

The index of the reasoning content part this delta is associated with.

delta: str

The text delta that was added to the reasoning content.

item\_id: str

The ID of the item this reasoning text delta is associated with.

output\_index: int

The index of the output item this reasoning text delta is associated with.

sequence\_number: int

The sequence number of this event.

type: Literal["response.reasoning\_text.delta"]

The type of the event. Always `response.reasoning_text.delta`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseReasoningTextDoneEvent: …

Emitted when a reasoning text is completed.

content\_index: int

The index of the reasoning content part.

item\_id: str

The ID of the item this reasoning text is associated with.

output\_index: int

The index of the output item this reasoning text is associated with.

sequence\_number: int

The sequence number of this event.

text: str

The full text of the completed reasoning content.

type: Literal["response.reasoning\_text.done"]

The type of the event. Always `response.reasoning_text.done`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseRefusalDeltaEvent: …

Emitted when there is a partial refusal text.

content\_index: int

The index of the content part that the refusal text is added to.

delta: str

The refusal text that is added.

item\_id: str

The ID of the output item that the refusal text is added to.

output\_index: int

The index of the output item that the refusal text is added to.

sequence\_number: int

The sequence number of this event.

type: Literal["response.refusal.delta"]

The type of the event. Always `response.refusal.delta`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseRefusalDoneEvent: …

Emitted when refusal text is finalized.

content\_index: int

The index of the content part that the refusal text is finalized.

item\_id: str

The ID of the output item that the refusal text is finalized.

output\_index: int

The index of the output item that the refusal text is finalized.

refusal: str

The refusal text that is finalized.

sequence\_number: int

The sequence number of this event.

type: Literal["response.refusal.done"]

The type of the event. Always `response.refusal.done`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseTextDeltaEvent: …

Emitted when there is an additional text delta.

content\_index: int

The index of the content part that the text delta was added to.

delta: str

The text delta that was added.

item\_id: str

The ID of the output item that the text delta was added to.

logprobs: List[Logprob]

The log probabilities of the tokens in the delta.

token: str

A possible text token.

logprob: float

The log probability of this token.

top\_logprobs: Optional[List[LogprobTopLogprob]]

The log probabilities of up to 20 of the most likely tokens.

token: Optional[str]

A possible text token.

logprob: Optional[float]

The log probability of this token.

output\_index: int

The index of the output item that the text delta was added to.

sequence\_number: int

The sequence number for this event.

type: Literal["response.output\_text.delta"]

The type of the event. Always `response.output_text.delta`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseTextDoneEvent: …

Emitted when text content is finalized.

content\_index: int

The index of the content part that the text content is finalized.

item\_id: str

The ID of the output item that the text content is finalized.

logprobs: List[Logprob]

The log probabilities of the tokens in the delta.

token: str

A possible text token.

logprob: float

The log probability of this token.

top\_logprobs: Optional[List[LogprobTopLogprob]]

The log probabilities of up to 20 of the most likely tokens.

token: Optional[str]

A possible text token.

logprob: Optional[float]

The log probability of this token.

output\_index: int

The index of the output item that the text content is finalized.

sequence\_number: int

The sequence number for this event.

text: str

The text content that is finalized.

type: Literal["response.output\_text.done"]

The type of the event. Always `response.output_text.done`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseWebSearchCallCompletedEvent: …

Emitted when a web search call is completed.

item\_id: str

Unique ID for the output item associated with the web search call.

output\_index: int

The index of the output item that the web search call is associated with.

sequence\_number: int

The sequence number of the web search call being processed.

type: Literal["response.web\_search\_call.completed"]

The type of the event. Always `response.web_search_call.completed`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseWebSearchCallInProgressEvent: …

Emitted when a web search call is initiated.

item\_id: str

Unique ID for the output item associated with the web search call.

output\_index: int

The index of the output item that the web search call is associated with.

sequence\_number: int

The sequence number of the web search call being processed.

type: Literal["response.web\_search\_call.in\_progress"]

The type of the event. Always `response.web_search_call.in_progress`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseWebSearchCallSearchingEvent: …

Emitted when a web search call is executing.

item\_id: str

Unique ID for the output item associated with the web search call.

output\_index: int

The index of the output item that the web search call is associated with.

sequence\_number: int

The sequence number of the web search call being processed.

type: Literal["response.web\_search\_call.searching"]

The type of the event. Always `response.web_search_call.searching`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseImageGenCallCompletedEvent: …

Emitted when an image generation tool call has completed and the final image is available.

item\_id: str

The unique identifier of the image generation item being processed.

output\_index: int

The index of the output item in the response’s output array.

sequence\_number: int

The sequence number of this event.

type: Literal["response.image\_generation\_call.completed"]

The type of the event. Always ‘response.image\_generation\_call.completed’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseImageGenCallGeneratingEvent: …

Emitted when an image generation tool call is actively generating an image (intermediate state).

item\_id: str

The unique identifier of the image generation item being processed.

output\_index: int

The index of the output item in the response’s output array.

sequence\_number: int

The sequence number of the image generation item being processed.

type: Literal["response.image\_generation\_call.generating"]

The type of the event. Always ‘response.image\_generation\_call.generating’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseImageGenCallInProgressEvent: …

Emitted when an image generation tool call is in progress.

item\_id: str

The unique identifier of the image generation item being processed.

output\_index: int

The index of the output item in the response’s output array.

sequence\_number: int

The sequence number of the image generation item being processed.

type: Literal["response.image\_generation\_call.in\_progress"]

The type of the event. Always ‘response.image\_generation\_call.in\_progress’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseImageGenCallPartialImageEvent: …

Emitted when a partial image is available during image generation streaming.

item\_id: str

The unique identifier of the image generation item being processed.

output\_index: int

The index of the output item in the response’s output array.

partial\_image\_b64: str

Base64-encoded partial image data, suitable for rendering as an image.

partial\_image\_index: int

0-based index for the partial image (backend is 1-based, but this is 0-based for the user).

sequence\_number: int

The sequence number of the image generation item being processed.

type: Literal["response.image\_generation\_call.partial\_image"]

The type of the event. Always ‘response.image\_generation\_call.partial\_image’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseMcpCallArgumentsDeltaEvent: …

Emitted when there is a delta (partial update) to the arguments of an MCP tool call.

delta: str

A JSON string containing the partial update to the arguments for the MCP tool call.

item\_id: str

The unique identifier of the MCP tool call item being processed.

output\_index: int

The index of the output item in the response’s output array.

sequence\_number: int

The sequence number of this event.

type: Literal["response.mcp\_call\_arguments.delta"]

The type of the event. Always ‘response.mcp\_call\_arguments.delta’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseMcpCallArgumentsDoneEvent: …

Emitted when the arguments for an MCP tool call are finalized.

arguments: str

A JSON string containing the finalized arguments for the MCP tool call.

item\_id: str

The unique identifier of the MCP tool call item being processed.

output\_index: int

The index of the output item in the response’s output array.

sequence\_number: int

The sequence number of this event.

type: Literal["response.mcp\_call\_arguments.done"]

The type of the event. Always ‘response.mcp\_call\_arguments.done’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseMcpCallCompletedEvent: …

Emitted when an MCP tool call has completed successfully.

item\_id: str

The ID of the MCP tool call item that completed.

output\_index: int

The index of the output item that completed.

sequence\_number: int

The sequence number of this event.

type: Literal["response.mcp\_call.completed"]

The type of the event. Always ‘response.mcp\_call.completed’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseMcpCallFailedEvent: …

Emitted when an MCP tool call has failed.

item\_id: str

The ID of the MCP tool call item that failed.

output\_index: int

The index of the output item that failed.

sequence\_number: int

The sequence number of this event.

type: Literal["response.mcp\_call.failed"]

The type of the event. Always ‘response.mcp\_call.failed’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseMcpCallInProgressEvent: …

Emitted when an MCP tool call is in progress.

item\_id: str

The unique identifier of the MCP tool call item being processed.

output\_index: int

The index of the output item in the response’s output array.

sequence\_number: int

The sequence number of this event.

type: Literal["response.mcp\_call.in\_progress"]

The type of the event. Always ‘response.mcp\_call.in\_progress’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseMcpListToolsCompletedEvent: …

Emitted when the list of available MCP tools has been successfully retrieved.

item\_id: str

The ID of the MCP tool call item that produced this output.

output\_index: int

The index of the output item that was processed.

sequence\_number: int

The sequence number of this event.

type: Literal["response.mcp\_list\_tools.completed"]

The type of the event. Always ‘response.mcp\_list\_tools.completed’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseMcpListToolsFailedEvent: …

Emitted when the attempt to list available MCP tools has failed.

item\_id: str

The ID of the MCP tool call item that failed.

output\_index: int

The index of the output item that failed.

sequence\_number: int

The sequence number of this event.

type: Literal["response.mcp\_list\_tools.failed"]

The type of the event. Always ‘response.mcp\_list\_tools.failed’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseMcpListToolsInProgressEvent: …

Emitted when the system is in the process of retrieving the list of available MCP tools.

item\_id: str

The ID of the MCP tool call item that is being processed.

output\_index: int

The index of the output item that is being processed.

sequence\_number: int

The sequence number of this event.

type: Literal["response.mcp\_list\_tools.in\_progress"]

The type of the event. Always ‘response.mcp\_list\_tools.in\_progress’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseOutputTextAnnotationAddedEvent: …

Emitted when an annotation is added to output text content.

annotation: object

The annotation object being added. (See annotation schema for details.)

annotation\_index: int

The index of the annotation within the content part.

content\_index: int

The index of the content part within the output item.

item\_id: str

The unique identifier of the item to which the annotation is being added.

output\_index: int

The index of the output item in the response’s output array.

sequence\_number: int

The sequence number of this event.

type: Literal["response.output\_text.annotation.added"]

The type of the event. Always ‘response.output\_text.annotation.added’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseQueuedEvent: …

Emitted when a response is queued and waiting to be processed.

response: [BetaResponse](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema))

The full response object that is queued.

sequence\_number: int

The sequence number for this event.

type: Literal["response.queued"]

The type of the event. Always ‘response.queued’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseCustomToolCallInputDeltaEvent: …

Event representing a delta (partial update) to the input of a custom tool call.

delta: str

The incremental input data (delta) for the custom tool call.

item\_id: str

Unique identifier for the API item associated with this event.

output\_index: int

The index of the output this delta applies to.

sequence\_number: int

The sequence number of this event.

type: Literal["response.custom\_tool\_call\_input.delta"]

The event type identifier.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseCustomToolCallInputDoneEvent: …

Event indicating that input for a custom tool call is complete.

input: str

The complete input data for the custom tool call.

item\_id: str

Unique identifier for the API item associated with this event.

output\_index: int

The index of the output this event applies to.

sequence\_number: int

The sequence number of this event.

type: Literal["response.custom\_tool\_call\_input.done"]

The event type identifier.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseInjectCreatedEvent: …

Emitted when all injected input items were validated and committed to the
active response.

response\_id: str

The ID of the response that accepted the input.

sequence\_number: int

The sequence number for this event.

type: Literal["response.inject.created"]

The event discriminator. Always `response.inject.created`.

stream\_id: Optional[str]

The multiplexed WebSocket stream that emitted the event. This field is
present only when WebSocket multiplexing is enabled separately.

class BetaResponseInjectFailedEvent: …

Emitted when injected input could not be committed to a response. The event
returns the uncommitted raw input so the client can retry it in another
response when appropriate.

error: Error

Information about why the input was not committed.

code: Literal["response\_already\_completed", "response\_not\_found"]

A machine-readable error code.

"response\_already\_completed"

"response\_not\_found"

message: str

A human-readable description of the error.

input: List[[BetaResponseInputItem](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_item%20%3E%20(schema))]

The raw input items that were not committed.

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

List[[BetaResponseInputContent](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_content%20%3E%20(schema))]

class BetaResponseInputText: …

text: str

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

"low"

"high"

"auto"

"original"

type: Literal["input\_image"]

file\_id: Optional[str]

image\_url: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputFile: …

type: Literal["input\_file"]

detail: Optional[Literal["auto", "low", "high"]]

"auto"

"low"

"high"

file\_data: Optional[str]

file\_id: Optional[str]

file\_url: Optional[str]

filename: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

role: Literal["user", "assistant", "system", "developer"]

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

"user"

"assistant"

"system"

"developer"

phase: Optional[Literal["commentary", "final\_answer"]]

"commentary"

"final\_answer"

type: Optional[Literal["message"]]

The type of the message input. Always `message`.

class Message: …

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role.

content: [BetaResponseInputMessageContentList](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_message_content_list%20%3E%20(schema))

role: Literal["user", "system", "developer"]

"user"

"system"

"developer"

agent: Optional[MessageAgent]

agent\_name: str

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

type: Optional[Literal["message"]]

class BetaResponseOutputMessage: …

id: str

content: List[Content]

class BetaResponseOutputText: …

annotations: List[Annotation]

class AnnotationFileCitation: …

file\_id: str

filename: str

index: int

type: Literal["file\_citation"]

class AnnotationURLCitation: …

end\_index: int

start\_index: int

title: str

type: Literal["url\_citation"]

url: str

class AnnotationContainerFileCitation: …

container\_id: str

end\_index: int

file\_id: str

filename: str

start\_index: int

type: Literal["container\_file\_citation"]

class AnnotationFilePath: …

file\_id: str

index: int

type: Literal["file\_path"]

text: str

type: Literal["output\_text"]

logprobs: Optional[List[Logprob]]

token: str

bytes: List[int]

logprob: float

top\_logprobs: List[LogprobTopLogprob]

token: str

bytes: List[int]

logprob: float

class BetaResponseOutputRefusal: …

refusal: str

type: Literal["refusal"]

role: Literal["assistant"]

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["message"]

agent: Optional[Agent]

agent\_name: str

phase: Optional[Literal["commentary", "final\_answer"]]

"commentary"

"final\_answer"

class BetaResponseFileSearchToolCall: …

[file search guide](https://platform.openai.com/docs/guides/tools-file-search) for more information.

id: str

queries: List[str]

status: Literal["in\_progress", "searching", "completed", 2 more]

"in\_progress"

"searching"

"completed"

"incomplete"

"failed"

type: Literal["file\_search\_call"]

agent: Optional[Agent]

agent\_name: str

results: Optional[List[Result]]

attributes: Optional[Dict[str, Union[str, float, bool]]]

str

float

bool

file\_id: Optional[str]

filename: Optional[str]

score: Optional[float]

formatfloat

text: Optional[str]

class BetaResponseComputerToolCall: …

[computer use guide](https://platform.openai.com/docs/guides/tools-computer-use) for more information.

id: str

call\_id: str

pending\_safety\_checks: List[PendingSafetyCheck]

id: str

code: Optional[str]

message: Optional[str]

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["computer\_call"]

action: Optional[BetaComputerAction]

actions: Optional[BetaComputerActionList]

agent: Optional[Agent]

agent\_name: str

class ComputerCallOutput: …

The output of a computer tool call.

call\_id: str

maxLength64

minLength1

output: [BetaResponseComputerToolCallOutputScreenshot](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_computer_tool_call_output_screenshot%20%3E%20(schema))

type: Literal["computer\_call\_output"]

id: Optional[str]

The ID of the computer tool call output.

acknowledged\_safety\_checks: Optional[List[ComputerCallOutputAcknowledgedSafetyCheck]]

The safety checks reported by the API that have been acknowledged by the developer.

id: str

code: Optional[str]

message: Optional[str]

agent: Optional[ComputerCallOutputAgent]

agent\_name: str

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the message input. One of `in_progress`, `completed`, or `incomplete`. Populated when input items are returned via API.

"in\_progress"

"completed"

"incomplete"

class BetaResponseFunctionWebSearch: …

[web search guide](https://platform.openai.com/docs/guides/tools-web-search) for more information.

id: str

action: Action

class ActionSearch: …

type: Literal["search"]

queries: Optional[List[str]]

Deprecatedquery: Optional[str]

sources: Optional[List[ActionSearchSource]]

type: Literal["url"]

url: str

class ActionOpenPage: …

type: Literal["open\_page"]

url: Optional[str]

class ActionFindInPage: …

pattern: str

type: Literal["find\_in\_page"]

url: str

status: Literal["in\_progress", "searching", "completed", "failed"]

"in\_progress"

"searching"

"completed"

"failed"

type: Literal["web\_search\_call"]

agent: Optional[Agent]

agent\_name: str

class BetaResponseFunctionToolCall: …

[function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.

arguments: str

A JSON string of the arguments to pass to the function.

call\_id: str

name: str

The name of the function to run.

type: Literal["function\_call"]

The type of the function tool call. Always `function_call`.

id: Optional[str]

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

namespace: Optional[str]

The namespace of the function to run.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class FunctionCallOutput: …

The output of a function tool call.

call\_id: str

maxLength64

minLength1

output: Union[str, [BetaResponseFunctionCallOutputItemList](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_call_output_item_list%20%3E%20(schema))]

Text, image, or file output of the function tool call.

str

A JSON string of the output of the function tool call.

List[[BetaResponseFunctionCallOutputItem](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_call_output_item%20%3E%20(schema))]

class BetaResponseInputTextContent: …

text: str

maxLength10485760

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputImageContent: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision)

type: Literal["input\_image"]

detail: Optional[Literal["low", "high", "auto", "original"]]

"low"

"high"

"auto"

"original"

file\_id: Optional[str]

image\_url: Optional[str]

maxLength20971520

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputFileContent: …

type: Literal["input\_file"]

detail: Optional[Literal["auto", "low", "high"]]

"auto"

"low"

"high"

file\_data: Optional[str]

The base64-encoded data of the file to be sent to the model.

maxLength73400320

file\_id: Optional[str]

file\_url: Optional[str]

filename: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

type: Literal["function\_call\_output"]

id: Optional[str]

The unique ID of the function tool call output. Populated when this item is returned via API.

agent: Optional[FunctionCallOutputAgent]

agent\_name: str

caller: Optional[FunctionCallOutputCaller]

class FunctionCallOutputCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class FunctionCallOutputCallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the item. One of `in_progress`, `completed`, or `incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

class AgentMessage: …

A message routed between agents.

author: str

content: List[AgentMessageContent]

Plaintext, image, or encrypted content sent between agents.

class BetaResponseInputTextContent: …

text: str

maxLength10485760

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputImageContent: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision)

type: Literal["input\_image"]

detail: Optional[Literal["low", "high", "auto", "original"]]

"low"

"high"

"auto"

"original"

file\_id: Optional[str]

image\_url: Optional[str]

maxLength20971520

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class AgentMessageContentEncryptedContent: …

encrypted\_content: str

maxLength10485760

type: Literal["encrypted\_content"]

recipient: str

type: Literal["agent\_message"]

The item type. Always `agent_message`.

id: Optional[str]

The unique ID of this agent message item.

agent: Optional[AgentMessageAgent]

agent\_name: str

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

maxLength64

minLength1

type: Literal["multi\_agent\_call"]

The item type. Always `multi_agent_call`.

id: Optional[str]

The unique ID of this multi-agent call.

agent: Optional[MultiAgentCallAgent]

agent\_name: str

class MultiAgentCallOutput: …

action: Literal["spawn\_agent", "interrupt\_agent", "list\_agents", 3 more]

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

call\_id: str

maxLength64

minLength1

output: List[MultiAgentCallOutputOutput]

text: str

The text content.

maxLength10485760

type: Literal["output\_text"]

The content type. Always `output_text`.

annotations: Optional[List[MultiAgentCallOutputOutputAnnotation]]

Citations associated with the text content.

class MultiAgentCallOutputOutputAnnotationFileCitation: …

file\_id: str

filename: str

index: int

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

class MultiAgentCallOutputOutputAnnotationContainerFileCitation: …

container\_id: str

The ID of the container.

end\_index: int

The index of the last character of the citation in the message.

minimum0

file\_id: str

filename: str

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

agent\_name: str

class ToolSearchCall: …

arguments: object

The arguments supplied to the tool search call.

type: Literal["tool\_search\_call"]

The item type. Always `tool_search_call`.

id: Optional[str]

The unique ID of this tool search call.

agent: Optional[ToolSearchCallAgent]

agent\_name: str

call\_id: Optional[str]

maxLength64

minLength1

execution: Optional[Literal["server", "client"]]

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

name: str

parameters: Optional[Dict[str, object]]

strict: Optional[bool]

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

class BetaFileSearchTool: …

type: Literal["file\_search"]

vector\_store\_ids: List[str]

filters: Optional[Filters]

class FiltersComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

class FiltersCompoundFilter: …

filters: List[FiltersCompoundFilterFilter]

class FiltersCompoundFilterFilterComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

object

type: Literal["and", "or"]

"and"

"or"

max\_num\_results: Optional[int]

ranking\_options: Optional[RankingOptions]

hybrid\_search: Optional[RankingOptionsHybridSearch]

embedding\_weight: float

text\_weight: float

ranker: Optional[Literal["auto", "default-2024-11-15"]]

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

class BetaComputerTool: …

type: Literal["computer"]

class BetaComputerUsePreviewTool: …

display\_height: int

display\_width: int

environment: Literal["windows", "mac", "linux", 2 more]

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

class BetaWebSearchTool: …

[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

"web\_search"

"web\_search\_2025\_08\_26"

filters: Optional[Filters]

allowed\_domains: Optional[List[str]]

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

type: Optional[Literal["approximate"]]

class Mcp: …

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: str

type: Literal["mcp"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

allowed\_tools: Optional[McpAllowedTools]

List[str]

A string array of allowed tool names

class McpAllowedToolsMcpToolFilter: …

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

authorization: Optional[str]

connector\_id: Optional[Literal["connector\_dropbox", "connector\_gmail", "connector\_googlecalendar", 5 more]]

about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading: Optional[bool]

headers: Optional[Dict[str, str]]

require\_approval: Optional[McpRequireApproval]

class McpRequireApprovalMcpToolApprovalFilter: …

always: Optional[McpRequireApprovalMcpToolApprovalFilterAlways]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

never: Optional[McpRequireApprovalMcpToolApprovalFilterNever]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

Literal["always", "never"]

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

"always"

"never"

server\_description: Optional[str]

server\_url: Optional[str]

tunnel\_id: Optional[str]

class CodeInterpreter: …

A tool that runs Python code to help generate a response to a prompt.

container: CodeInterpreterContainer

str

The container ID.

class CodeInterpreterContainerCodeInterpreterToolAuto: …

type: Literal["auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

type: Literal["code\_interpreter"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

class ProgrammaticToolCalling: …

type: Literal["programmatic\_tool\_calling"]

The type of the tool. Always `programmatic_tool_calling`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

action: Optional[Literal["generate", "edit", "auto"]]

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

"high"

"low"

input\_image\_mask: Optional[ImageGenerationInputImageMask]

file\_id: Optional[str]

image\_url: Optional[str]

model: Optional[Union[str, Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more], null]]

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

"auto"

"low"

output\_compression: Optional[int]

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

"png"

"webp"

"jpeg"

partial\_images: Optional[int]

minimum0

maximum3

quality: Optional[Literal["low", "medium", "high", "auto"]]

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool: …

type: Literal["shell"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

environment: Optional[Environment]

class BetaContainerAuto: …

type: Literal["container\_auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

skills: Optional[List[Skill]]

class BetaSkillReference: …

skill\_id: str

maxLength64

minLength1

type: Literal["skill\_reference"]

version: Optional[str]

class BetaInlineSkill: …

description: str

name: str

source: [BetaInlineSkillSource](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

type: Literal["inline"]

class BetaLocalEnvironment: …

type: Literal["local"]

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

description: str

name: str

path: str

class BetaContainerReference: …

container\_id: str

type: Literal["container\_reference"]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

class BetaNamespaceTool: …

description: str

minLength1

name: str

minLength1

tools: List[Tool]

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

parameters: Optional[object]

strict: Optional[bool]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

type: Literal["namespace"]

class BetaToolSearchTool: …

type: Literal["tool\_search"]

description: Optional[str]

execution: Optional[Literal["server", "client"]]

"server"

"client"

parameters: Optional[object]

class BetaWebSearchPreviewTool: …

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

type: Literal["approximate"]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

class BetaApplyPatchTool: …

type: Literal["apply\_patch"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

type: Literal["tool\_search\_output"]

The item type. Always `tool_search_output`.

id: Optional[str]

The unique ID of this tool search output.

agent: Optional[Agent]

agent\_name: str

call\_id: Optional[str]

maxLength64

minLength1

execution: Optional[Literal["server", "client"]]

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

name: str

parameters: Optional[Dict[str, object]]

strict: Optional[bool]

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

class BetaFileSearchTool: …

type: Literal["file\_search"]

vector\_store\_ids: List[str]

filters: Optional[Filters]

class FiltersComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

class FiltersCompoundFilter: …

filters: List[FiltersCompoundFilterFilter]

class FiltersCompoundFilterFilterComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

object

type: Literal["and", "or"]

"and"

"or"

max\_num\_results: Optional[int]

ranking\_options: Optional[RankingOptions]

hybrid\_search: Optional[RankingOptionsHybridSearch]

embedding\_weight: float

text\_weight: float

ranker: Optional[Literal["auto", "default-2024-11-15"]]

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

class BetaComputerTool: …

type: Literal["computer"]

class BetaComputerUsePreviewTool: …

display\_height: int

display\_width: int

environment: Literal["windows", "mac", "linux", 2 more]

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

class BetaWebSearchTool: …

[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

"web\_search"

"web\_search\_2025\_08\_26"

filters: Optional[Filters]

allowed\_domains: Optional[List[str]]

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

type: Optional[Literal["approximate"]]

class Mcp: …

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: str

type: Literal["mcp"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

allowed\_tools: Optional[McpAllowedTools]

List[str]

A string array of allowed tool names

class McpAllowedToolsMcpToolFilter: …

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

authorization: Optional[str]

connector\_id: Optional[Literal["connector\_dropbox", "connector\_gmail", "connector\_googlecalendar", 5 more]]

about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading: Optional[bool]

headers: Optional[Dict[str, str]]

require\_approval: Optional[McpRequireApproval]

class McpRequireApprovalMcpToolApprovalFilter: …

always: Optional[McpRequireApprovalMcpToolApprovalFilterAlways]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

never: Optional[McpRequireApprovalMcpToolApprovalFilterNever]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

Literal["always", "never"]

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

"always"

"never"

server\_description: Optional[str]

server\_url: Optional[str]

tunnel\_id: Optional[str]

class CodeInterpreter: …

A tool that runs Python code to help generate a response to a prompt.

container: CodeInterpreterContainer

str

The container ID.

class CodeInterpreterContainerCodeInterpreterToolAuto: …

type: Literal["auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

type: Literal["code\_interpreter"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

class ProgrammaticToolCalling: …

type: Literal["programmatic\_tool\_calling"]

The type of the tool. Always `programmatic_tool_calling`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

action: Optional[Literal["generate", "edit", "auto"]]

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

"high"

"low"

input\_image\_mask: Optional[ImageGenerationInputImageMask]

file\_id: Optional[str]

image\_url: Optional[str]

model: Optional[Union[str, Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more], null]]

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

"auto"

"low"

output\_compression: Optional[int]

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

"png"

"webp"

"jpeg"

partial\_images: Optional[int]

minimum0

maximum3

quality: Optional[Literal["low", "medium", "high", "auto"]]

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool: …

type: Literal["shell"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

environment: Optional[Environment]

class BetaContainerAuto: …

type: Literal["container\_auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

skills: Optional[List[Skill]]

class BetaSkillReference: …

skill\_id: str

maxLength64

minLength1

type: Literal["skill\_reference"]

version: Optional[str]

class BetaInlineSkill: …

description: str

name: str

source: [BetaInlineSkillSource](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

type: Literal["inline"]

class BetaLocalEnvironment: …

type: Literal["local"]

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

description: str

name: str

path: str

class BetaContainerReference: …

container\_id: str

type: Literal["container\_reference"]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

class BetaNamespaceTool: …

description: str

minLength1

name: str

minLength1

tools: List[Tool]

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

parameters: Optional[object]

strict: Optional[bool]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

type: Literal["namespace"]

class BetaToolSearchTool: …

type: Literal["tool\_search"]

description: Optional[str]

execution: Optional[Literal["server", "client"]]

"server"

"client"

parameters: Optional[object]

class BetaWebSearchPreviewTool: …

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

type: Literal["approximate"]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

class BetaApplyPatchTool: …

type: Literal["apply\_patch"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

type: Literal["additional\_tools"]

The item type. Always `additional_tools`.

id: Optional[str]

The unique ID of this additional tools item.

agent: Optional[AdditionalToolsAgent]

agent\_name: str

class BetaResponseReasoningItem: …

[managing context](https://platform.openai.com/docs/guides/conversation-state).

id: str

summary: List[Summary]

text: str

type: Literal["summary\_text"]

type: Literal["reasoning"]

agent: Optional[Agent]

agent\_name: str

content: Optional[List[Content]]

text: str

type: Literal["reasoning\_text"]

encrypted\_content: Optional[str]

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class BetaResponseCompactionItemParam: …

A compaction item generated by the [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).

encrypted\_content: str

The encrypted content of the compaction summary.

maxLength10485760

type: Literal["compaction"]

id: Optional[str]

The ID of the compaction item.

agent: Optional[Agent]

agent\_name: str

class ImageGenerationCall: …

An image generation request made by the model.

id: str

result: Optional[str]

status: Literal["in\_progress", "completed", "generating", "failed"]

"in\_progress"

"completed"

"generating"

"failed"

type: Literal["image\_generation\_call"]

agent: Optional[ImageGenerationCallAgent]

agent\_name: str

class BetaResponseCodeInterpreterToolCall: …

id: str

code: Optional[str]

container\_id: str

outputs: Optional[List[Output]]

class OutputLogs: …

logs: str

type: Literal["logs"]

class OutputImage: …

type: Literal["image"]

url: str

status: Literal["in\_progress", "completed", "incomplete", 2 more]

"in\_progress"

"completed"

"incomplete"

"interpreting"

"failed"

type: Literal["code\_interpreter\_call"]

agent: Optional[Agent]

agent\_name: str

class LocalShellCall: …

A tool call to run a command on the local shell.

id: str

action: LocalShellCallAction

command: List[str]

env: Dict[str, str]

type: Literal["exec"]

timeout\_ms: Optional[int]

user: Optional[str]

working\_directory: Optional[str]

call\_id: str

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["local\_shell\_call"]

agent: Optional[LocalShellCallAgent]

agent\_name: str

class LocalShellCallOutput: …

The output of a local shell tool call.

id: str

output: str

type: Literal["local\_shell\_call\_output"]

agent: Optional[LocalShellCallOutputAgent]

agent\_name: str

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class ShellCall: …

A tool representing a request to execute one or more shell commands.

action: ShellCallAction

commands: List[str]

Ordered shell commands for the execution environment to run.

max\_output\_length: Optional[int]

Maximum number of UTF-8 characters to capture from combined stdout and stderr output.

timeout\_ms: Optional[int]

Maximum wall-clock time in milliseconds to allow the shell commands to run.

call\_id: str

maxLength64

minLength1

type: Literal["shell\_call"]

id: Optional[str]

agent: Optional[ShellCallAgent]

agent\_name: str

caller: Optional[ShellCallCaller]

class ShellCallCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class ShellCallCallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

environment: Optional[ShellCallEnvironment]

The environment to execute the shell commands in.

class BetaLocalEnvironment: …

type: Literal["local"]

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

description: str

name: str

path: str

class BetaContainerReference: …

container\_id: str

type: Literal["container\_reference"]

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class ShellCallOutput: …

The streamed output items emitted by a shell tool call.

call\_id: str

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

exit\_code: int

The exit code returned by the shell process.

type: Literal["exit"]

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

agent\_name: str

caller: Optional[ShellCallOutputCaller]

class ShellCallOutputCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class ShellCallOutputCallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

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

"in\_progress"

"completed"

type: Literal["apply\_patch\_call"]

id: Optional[str]

agent: Optional[ApplyPatchCallAgent]

agent\_name: str

caller: Optional[ApplyPatchCallCaller]

class ApplyPatchCallCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class ApplyPatchCallCallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

class ApplyPatchCallOutput: …

The streamed output emitted by an apply patch tool call.

call\_id: str

maxLength64

minLength1

status: Literal["completed", "failed"]

"completed"

"failed"

type: Literal["apply\_patch\_call\_output"]

id: Optional[str]

agent: Optional[ApplyPatchCallOutputAgent]

agent\_name: str

caller: Optional[ApplyPatchCallOutputCaller]

class ApplyPatchCallOutputCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class ApplyPatchCallOutputCallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

output: Optional[str]

Optional human-readable log text from the apply patch tool (e.g., patch results or errors).

maxLength10485760

class McpListTools: …

A list of tools available on an MCP server.

id: str

server\_label: str

tools: List[McpListToolsTool]

input\_schema: object

name: str

annotations: Optional[object]

description: Optional[str]

type: Literal["mcp\_list\_tools"]

agent: Optional[McpListToolsAgent]

agent\_name: str

error: Optional[str]

class McpApprovalRequest: …

A request for human approval of a tool invocation.

id: str

arguments: str

name: str

server\_label: str

type: Literal["mcp\_approval\_request"]

agent: Optional[McpApprovalRequestAgent]

agent\_name: str

class McpApprovalResponse: …

A response to an MCP approval request.

approval\_request\_id: str

approve: bool

type: Literal["mcp\_approval\_response"]

id: Optional[str]

agent: Optional[McpApprovalResponseAgent]

agent\_name: str

reason: Optional[str]

class McpCall: …

An invocation of a tool on an MCP server.

id: str

arguments: str

name: str

server\_label: str

type: Literal["mcp\_call"]

agent: Optional[McpCallAgent]

agent\_name: str

approval\_request\_id: Optional[str]

error: Optional[str]

output: Optional[str]

status: Optional[Literal["in\_progress", "completed", "incomplete", 2 more]]

"in\_progress"

"completed"

"incomplete"

"calling"

"failed"

class BetaResponseCustomToolCallOutput: …

call\_id: str

The call ID, used to map this custom tool call output to a custom tool call.

output: Union[str, List[OutputOutputContentList]]

The output from the custom tool call generated by your code.

str

A string of the output of the custom tool call.

List[OutputOutputContentList]

Text, image, or file output of the custom tool call.

class BetaResponseInputText: …

text: str

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

"low"

"high"

"auto"

"original"

type: Literal["input\_image"]

file\_id: Optional[str]

image\_url: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputFile: …

type: Literal["input\_file"]

detail: Optional[Literal["auto", "low", "high"]]

"auto"

"low"

"high"

file\_data: Optional[str]

file\_id: Optional[str]

file\_url: Optional[str]

filename: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

type: Literal["custom\_tool\_call\_output"]

The type of the custom tool call output. Always `custom_tool_call_output`.

id: Optional[str]

The unique ID of the custom tool call output in the OpenAI platform.

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class CallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

class BetaResponseCustomToolCall: …

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

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

namespace: Optional[str]

The namespace of the custom tool being called.

class CompactionTrigger: …

Compacts the current context. Must be the final input item.

type: Literal["compaction\_trigger"]

The type of the item. Always `compaction_trigger`.

agent: Optional[CompactionTriggerAgent]

agent\_name: str

class ItemReference: …

An internal identifier for an item to reference.

id: str

The ID of the item to reference.

agent: Optional[ItemReferenceAgent]

agent\_name: str

type: Optional[Literal["item\_reference"]]

The type of item to reference. Always `item_reference`.

class Program: …

id: str

The unique ID of this program item.

call\_id: str

maxLength64

minLength1

code: str

maxLength10485760

fingerprint: str

maxLength10485760

type: Literal["program"]

The item type. Always `program`.

agent: Optional[ProgramAgent]

agent\_name: str

class ProgramOutput: …

id: str

The unique ID of this program output item.

call\_id: str

maxLength64

minLength1

result: str

maxLength10485760

status: Literal["completed", "incomplete"]

The terminal status of the program output.

"completed"

"incomplete"

type: Literal["program\_output"]

The item type. Always `program_output`.

agent: Optional[ProgramOutputAgent]

agent\_name: str

response\_id: str

The ID of the response that rejected the input.

sequence\_number: int

The sequence number for this event.

type: Literal["response.inject.failed"]

The event discriminator. Always `response.inject.failed`.

stream\_id: Optional[str]

The multiplexed WebSocket stream that emitted the event. This field is
present only when WebSocket multiplexing is enabled separately.

class BetaSkillReference: …

skill\_id: str

maxLength64

minLength1

type: Literal["skill\_reference"]

version: Optional[str]

[BetaTool](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))

A tool that can be used to generate a response.

class BetaFunctionTool: …

name: str

parameters: Optional[Dict[str, object]]

strict: Optional[bool]

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

class BetaFileSearchTool: …

type: Literal["file\_search"]

vector\_store\_ids: List[str]

filters: Optional[Filters]

class FiltersComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

class FiltersCompoundFilter: …

filters: List[FiltersCompoundFilterFilter]

class FiltersCompoundFilterFilterComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

object

type: Literal["and", "or"]

"and"

"or"

max\_num\_results: Optional[int]

ranking\_options: Optional[RankingOptions]

hybrid\_search: Optional[RankingOptionsHybridSearch]

embedding\_weight: float

text\_weight: float

ranker: Optional[Literal["auto", "default-2024-11-15"]]

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

class BetaComputerTool: …

type: Literal["computer"]

class BetaComputerUsePreviewTool: …

display\_height: int

display\_width: int

environment: Literal["windows", "mac", "linux", 2 more]

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

class BetaWebSearchTool: …

[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

"web\_search"

"web\_search\_2025\_08\_26"

filters: Optional[Filters]

allowed\_domains: Optional[List[str]]

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

type: Optional[Literal["approximate"]]

class Mcp: …

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: str

type: Literal["mcp"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

allowed\_tools: Optional[McpAllowedTools]

List[str]

A string array of allowed tool names

class McpAllowedToolsMcpToolFilter: …

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

authorization: Optional[str]

connector\_id: Optional[Literal["connector\_dropbox", "connector\_gmail", "connector\_googlecalendar", 5 more]]

about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading: Optional[bool]

headers: Optional[Dict[str, str]]

require\_approval: Optional[McpRequireApproval]

class McpRequireApprovalMcpToolApprovalFilter: …

always: Optional[McpRequireApprovalMcpToolApprovalFilterAlways]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

never: Optional[McpRequireApprovalMcpToolApprovalFilterNever]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

Literal["always", "never"]

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

"always"

"never"

server\_description: Optional[str]

server\_url: Optional[str]

tunnel\_id: Optional[str]

class CodeInterpreter: …

A tool that runs Python code to help generate a response to a prompt.

container: CodeInterpreterContainer

str

The container ID.

class CodeInterpreterContainerCodeInterpreterToolAuto: …

type: Literal["auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

type: Literal["code\_interpreter"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

class ProgrammaticToolCalling: …

type: Literal["programmatic\_tool\_calling"]

The type of the tool. Always `programmatic_tool_calling`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

action: Optional[Literal["generate", "edit", "auto"]]

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

"high"

"low"

input\_image\_mask: Optional[ImageGenerationInputImageMask]

file\_id: Optional[str]

image\_url: Optional[str]

model: Optional[Union[str, Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more], null]]

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

"auto"

"low"

output\_compression: Optional[int]

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

"png"

"webp"

"jpeg"

partial\_images: Optional[int]

minimum0

maximum3

quality: Optional[Literal["low", "medium", "high", "auto"]]

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool: …

type: Literal["shell"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

environment: Optional[Environment]

class BetaContainerAuto: …

type: Literal["container\_auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

skills: Optional[List[Skill]]

class BetaSkillReference: …

skill\_id: str

maxLength64

minLength1

type: Literal["skill\_reference"]

version: Optional[str]

class BetaInlineSkill: …

description: str

name: str

source: [BetaInlineSkillSource](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

type: Literal["inline"]

class BetaLocalEnvironment: …

type: Literal["local"]

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

description: str

name: str

path: str

class BetaContainerReference: …

container\_id: str

type: Literal["container\_reference"]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

class BetaNamespaceTool: …

description: str

minLength1

name: str

minLength1

tools: List[Tool]

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

parameters: Optional[object]

strict: Optional[bool]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

type: Literal["namespace"]

class BetaToolSearchTool: …

type: Literal["tool\_search"]

description: Optional[str]

execution: Optional[Literal["server", "client"]]

"server"

"client"

parameters: Optional[object]

class BetaWebSearchPreviewTool: …

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

type: Literal["approximate"]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

class BetaApplyPatchTool: …

type: Literal["apply\_patch"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

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

  { "type": "function", "name": "get_weather" },
  { "type": "mcp", "server_label": "deepwiki" },
  { "type": "image_generation" }

type: Literal["allowed\_tools"]

Allowed tool configuration type. Always `allowed_tools`.

class BetaToolChoiceApplyPatch: …

Forces the model to call the apply\_patch tool when executing a tool call.

type: Literal["apply\_patch"]

The tool to call. Always `apply_patch`.

class BetaToolChoiceCustom: …

Use this option to force the model to call a specific custom tool.

name: str

The name of the custom tool to call.

type: Literal["custom"]

For custom tool calling, the type is always `custom`.

class BetaToolChoiceFunction: …

Use this option to force the model to call a specific function.

name: str

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

Literal["none", "auto", "required"]

Controls which (if any) tool is called by the model.

`none` means the model will not call any tool and instead generates a message.

`auto` means the model can pick between generating a message or calling one or
more tools.

`required` means the model must call one or more tools.

"none"

"auto"

"required"

class BetaToolChoiceShell: …

Forces the model to call the shell tool when a tool call is required.

type: Literal["shell"]

The tool to call. Always `shell`.

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

class BetaToolSearchTool: …

type: Literal["tool\_search"]

description: Optional[str]

execution: Optional[Literal["server", "client"]]

"server"

"client"

parameters: Optional[object]

class BetaWebSearchPreviewTool: …

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

type: Literal["approximate"]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

class BetaWebSearchTool: …

[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

"web\_search"

"web\_search\_2025\_08\_26"

filters: Optional[Filters]

allowed\_domains: Optional[List[str]]

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

type: Optional[Literal["approximate"]]

#### ResponsesInput Items

##### [List input items](/api/reference/python/resources/beta/subresources/responses/subresources/input_items/methods/list)

beta.responses.input\_items.list(strresponse\_id, InputItemListParams\*\*kwargs)  -> SyncCursorPage[[BetaResponseItem](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_item%20%3E%20(schema))]

GET/responses/{response\_id}/input\_items

##### ModelsExpand Collapse

class BetaResponseItemList: …

A list of Response items.

data: List[[BetaResponseItem](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_item%20%3E%20(schema))]

A list of items used to generate this response.

class BetaResponseInputMessageItem: …

id: str

The unique ID of the message input.

content: [BetaResponseInputMessageContentList](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_message_content_list%20%3E%20(schema))

role: Literal["user", "system", "developer"]

"user"

"system"

"developer"

type: Literal["message"]

agent: Optional[Agent]

agent\_name: str

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class BetaResponseOutputMessage: …

id: str

content: List[Content]

class BetaResponseOutputText: …

annotations: List[Annotation]

class AnnotationFileCitation: …

file\_id: str

filename: str

index: int

type: Literal["file\_citation"]

class AnnotationURLCitation: …

end\_index: int

start\_index: int

title: str

type: Literal["url\_citation"]

url: str

class AnnotationContainerFileCitation: …

container\_id: str

end\_index: int

file\_id: str

filename: str

start\_index: int

type: Literal["container\_file\_citation"]

class AnnotationFilePath: …

file\_id: str

index: int

type: Literal["file\_path"]

text: str

type: Literal["output\_text"]

logprobs: Optional[List[Logprob]]

token: str

bytes: List[int]

logprob: float

top\_logprobs: List[LogprobTopLogprob]

token: str

bytes: List[int]

logprob: float

class BetaResponseOutputRefusal: …

refusal: str

type: Literal["refusal"]

role: Literal["assistant"]

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["message"]

agent: Optional[Agent]

agent\_name: str

phase: Optional[Literal["commentary", "final\_answer"]]

"commentary"

"final\_answer"

class BetaResponseFileSearchToolCall: …

[file search guide](https://platform.openai.com/docs/guides/tools-file-search) for more information.

id: str

queries: List[str]

status: Literal["in\_progress", "searching", "completed", 2 more]

"in\_progress"

"searching"

"completed"

"incomplete"

"failed"

type: Literal["file\_search\_call"]

agent: Optional[Agent]

agent\_name: str

results: Optional[List[Result]]

attributes: Optional[Dict[str, Union[str, float, bool]]]

str

float

bool

file\_id: Optional[str]

filename: Optional[str]

score: Optional[float]

formatfloat

text: Optional[str]

class BetaResponseComputerToolCall: …

[computer use guide](https://platform.openai.com/docs/guides/tools-computer-use) for more information.

id: str

call\_id: str

pending\_safety\_checks: List[PendingSafetyCheck]

id: str

code: Optional[str]

message: Optional[str]

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["computer\_call"]

action: Optional[BetaComputerAction]

actions: Optional[BetaComputerActionList]

agent: Optional[Agent]

agent\_name: str

class BetaResponseComputerToolCallOutputItem: …

id: str

The unique ID of the computer call tool output.

call\_id: str

output: [BetaResponseComputerToolCallOutputScreenshot](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_computer_tool_call_output_screenshot%20%3E%20(schema))

status: Literal["completed", "incomplete", "failed", "in\_progress"]

"completed"

"incomplete"

"failed"

"in\_progress"

type: Literal["computer\_call\_output"]

acknowledged\_safety\_checks: Optional[List[AcknowledgedSafetyCheck]]

The safety checks reported by the API that have been acknowledged by the
developer.

id: str

code: Optional[str]

message: Optional[str]

agent: Optional[Agent]

agent\_name: str

created\_by: Optional[str]

The identifier of the actor that created the item.

class BetaResponseFunctionWebSearch: …

[web search guide](https://platform.openai.com/docs/guides/tools-web-search) for more information.

id: str

action: Action

class ActionSearch: …

type: Literal["search"]

queries: Optional[List[str]]

Deprecatedquery: Optional[str]

sources: Optional[List[ActionSearchSource]]

type: Literal["url"]

url: str

class ActionOpenPage: …

type: Literal["open\_page"]

url: Optional[str]

class ActionFindInPage: …

pattern: str

type: Literal["find\_in\_page"]

url: str

status: Literal["in\_progress", "searching", "completed", "failed"]

"in\_progress"

"searching"

"completed"

"failed"

type: Literal["web\_search\_call"]

agent: Optional[Agent]

agent\_name: str

class BetaResponseFunctionToolCallItem: …

[function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.

id: str

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

created\_by: Optional[str]

The identifier of the actor that created the item.

class BetaResponseFunctionToolCallOutputItem: …

id: str

The unique ID of the function call tool output.

call\_id: str

output: Union[str, List[OutputOutputContentList]]

The output from the function call generated by your code.

str

A string of the output of the function call.

List[OutputOutputContentList]

Text, image, or file output of the function call.

class BetaResponseInputText: …

text: str

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

"low"

"high"

"auto"

"original"

type: Literal["input\_image"]

file\_id: Optional[str]

image\_url: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputFile: …

type: Literal["input\_file"]

detail: Optional[Literal["auto", "low", "high"]]

"auto"

"low"

"high"

file\_data: Optional[str]

file\_id: Optional[str]

file\_url: Optional[str]

filename: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["function\_call\_output"]

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class CallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

created\_by: Optional[str]

The identifier of the actor that created the item.

class AgentMessage: …

id: str

The unique ID of the agent message.

author: str

content: List[AgentMessageContent]

Encrypted content sent between agents.

class BetaResponseInputText: …

text: str

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseOutputText: …

annotations: List[Annotation]

class AnnotationFileCitation: …

file\_id: str

filename: str

index: int

type: Literal["file\_citation"]

class AnnotationURLCitation: …

end\_index: int

start\_index: int

title: str

type: Literal["url\_citation"]

url: str

class AnnotationContainerFileCitation: …

container\_id: str

end\_index: int

file\_id: str

filename: str

start\_index: int

type: Literal["container\_file\_citation"]

class AnnotationFilePath: …

file\_id: str

index: int

type: Literal["file\_path"]

text: str

type: Literal["output\_text"]

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

type: Literal["summary\_text"]

class AgentMessageContentReasoningText: …

text: str

type: Literal["reasoning\_text"]

class BetaResponseOutputRefusal: …

refusal: str

type: Literal["refusal"]

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

"low"

"high"

"auto"

"original"

type: Literal["input\_image"]

file\_id: Optional[str]

image\_url: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class AgentMessageContentComputerScreenshot: …

A screenshot of a computer.

detail: Literal["low", "high", "auto", "original"]

The detail level of the screenshot image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

"low"

"high"

"auto"

"original"

file\_id: Optional[str]

image\_url: Optional[str]

type: Literal["computer\_screenshot"]

Specifies the event type. For a computer screenshot, this property is always set to `computer_screenshot`.

prompt\_cache\_breakpoint: Optional[AgentMessageContentComputerScreenshotPromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputFile: …

type: Literal["input\_file"]

detail: Optional[Literal["auto", "low", "high"]]

"auto"

"low"

"high"

file\_data: Optional[str]

file\_id: Optional[str]

file\_url: Optional[str]

filename: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class AgentMessageContentEncryptedContent: …

encrypted\_content: str

type: Literal["encrypted\_content"]

recipient: str

type: Literal["agent\_message"]

The type of the item. Always `agent_message`.

agent: Optional[AgentMessageAgent]

agent\_name: str

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

type: Literal["multi\_agent\_call"]

The type of the multi-agent call. Always `multi_agent_call`.

agent: Optional[MultiAgentCallAgent]

agent\_name: str

class MultiAgentCallOutput: …

id: str

The unique ID of the multi-agent call output item.

action: Literal["spawn\_agent", "interrupt\_agent", "list\_agents", 3 more]

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

call\_id: str

output: List[[BetaResponseOutputText](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_text%20%3E%20(schema))]

annotations: List[Annotation]

class AnnotationFileCitation: …

file\_id: str

filename: str

index: int

type: Literal["file\_citation"]

class AnnotationURLCitation: …

end\_index: int

start\_index: int

title: str

type: Literal["url\_citation"]

url: str

class AnnotationContainerFileCitation: …

container\_id: str

end\_index: int

file\_id: str

filename: str

start\_index: int

type: Literal["container\_file\_citation"]

class AnnotationFilePath: …

file\_id: str

index: int

type: Literal["file\_path"]

text: str

type: Literal["output\_text"]

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

agent\_name: str

class BetaResponseToolSearchCall: …

id: str

The unique ID of the tool search call item.

arguments: object

Arguments used for the tool search call.

call\_id: Optional[str]

execution: Literal["server", "client"]

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

agent\_name: str

created\_by: Optional[str]

The identifier of the actor that created the item.

class BetaResponseToolSearchOutputItem: …

id: str

The unique ID of the tool search output item.

call\_id: Optional[str]

execution: Literal["server", "client"]

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

name: str

parameters: Optional[Dict[str, object]]

strict: Optional[bool]

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

class BetaFileSearchTool: …

type: Literal["file\_search"]

vector\_store\_ids: List[str]

filters: Optional[Filters]

class FiltersComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

class FiltersCompoundFilter: …

filters: List[FiltersCompoundFilterFilter]

class FiltersCompoundFilterFilterComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

object

type: Literal["and", "or"]

"and"

"or"

max\_num\_results: Optional[int]

ranking\_options: Optional[RankingOptions]

hybrid\_search: Optional[RankingOptionsHybridSearch]

embedding\_weight: float

text\_weight: float

ranker: Optional[Literal["auto", "default-2024-11-15"]]

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

class BetaComputerTool: …

type: Literal["computer"]

class BetaComputerUsePreviewTool: …

display\_height: int

display\_width: int

environment: Literal["windows", "mac", "linux", 2 more]

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

class BetaWebSearchTool: …

[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

"web\_search"

"web\_search\_2025\_08\_26"

filters: Optional[Filters]

allowed\_domains: Optional[List[str]]

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

type: Optional[Literal["approximate"]]

class Mcp: …

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: str

type: Literal["mcp"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

allowed\_tools: Optional[McpAllowedTools]

List[str]

A string array of allowed tool names

class McpAllowedToolsMcpToolFilter: …

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

authorization: Optional[str]

connector\_id: Optional[Literal["connector\_dropbox", "connector\_gmail", "connector\_googlecalendar", 5 more]]

about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading: Optional[bool]

headers: Optional[Dict[str, str]]

require\_approval: Optional[McpRequireApproval]

class McpRequireApprovalMcpToolApprovalFilter: …

always: Optional[McpRequireApprovalMcpToolApprovalFilterAlways]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

never: Optional[McpRequireApprovalMcpToolApprovalFilterNever]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

Literal["always", "never"]

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

"always"

"never"

server\_description: Optional[str]

server\_url: Optional[str]

tunnel\_id: Optional[str]

class CodeInterpreter: …

A tool that runs Python code to help generate a response to a prompt.

container: CodeInterpreterContainer

str

The container ID.

class CodeInterpreterContainerCodeInterpreterToolAuto: …

type: Literal["auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

type: Literal["code\_interpreter"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

class ProgrammaticToolCalling: …

type: Literal["programmatic\_tool\_calling"]

The type of the tool. Always `programmatic_tool_calling`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

action: Optional[Literal["generate", "edit", "auto"]]

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

"high"

"low"

input\_image\_mask: Optional[ImageGenerationInputImageMask]

file\_id: Optional[str]

image\_url: Optional[str]

model: Optional[Union[str, Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more], null]]

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

"auto"

"low"

output\_compression: Optional[int]

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

"png"

"webp"

"jpeg"

partial\_images: Optional[int]

minimum0

maximum3

quality: Optional[Literal["low", "medium", "high", "auto"]]

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool: …

type: Literal["shell"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

environment: Optional[Environment]

class BetaContainerAuto: …

type: Literal["container\_auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

skills: Optional[List[Skill]]

class BetaSkillReference: …

skill\_id: str

maxLength64

minLength1

type: Literal["skill\_reference"]

version: Optional[str]

class BetaInlineSkill: …

description: str

name: str

source: [BetaInlineSkillSource](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

type: Literal["inline"]

class BetaLocalEnvironment: …

type: Literal["local"]

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

description: str

name: str

path: str

class BetaContainerReference: …

container\_id: str

type: Literal["container\_reference"]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

class BetaNamespaceTool: …

description: str

minLength1

name: str

minLength1

tools: List[Tool]

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

parameters: Optional[object]

strict: Optional[bool]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

type: Literal["namespace"]

class BetaToolSearchTool: …

type: Literal["tool\_search"]

description: Optional[str]

execution: Optional[Literal["server", "client"]]

"server"

"client"

parameters: Optional[object]

class BetaWebSearchPreviewTool: …

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

type: Literal["approximate"]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

class BetaApplyPatchTool: …

type: Literal["apply\_patch"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

type: Literal["tool\_search\_output"]

The type of the item. Always `tool_search_output`.

agent: Optional[Agent]

agent\_name: str

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

name: str

parameters: Optional[Dict[str, object]]

strict: Optional[bool]

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

class BetaFileSearchTool: …

type: Literal["file\_search"]

vector\_store\_ids: List[str]

filters: Optional[Filters]

class FiltersComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

class FiltersCompoundFilter: …

filters: List[FiltersCompoundFilterFilter]

class FiltersCompoundFilterFilterComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

object

type: Literal["and", "or"]

"and"

"or"

max\_num\_results: Optional[int]

ranking\_options: Optional[RankingOptions]

hybrid\_search: Optional[RankingOptionsHybridSearch]

embedding\_weight: float

text\_weight: float

ranker: Optional[Literal["auto", "default-2024-11-15"]]

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

class BetaComputerTool: …

type: Literal["computer"]

class BetaComputerUsePreviewTool: …

display\_height: int

display\_width: int

environment: Literal["windows", "mac", "linux", 2 more]

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

class BetaWebSearchTool: …

[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

"web\_search"

"web\_search\_2025\_08\_26"

filters: Optional[Filters]

allowed\_domains: Optional[List[str]]

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

type: Optional[Literal["approximate"]]

class Mcp: …

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: str

type: Literal["mcp"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

allowed\_tools: Optional[McpAllowedTools]

List[str]

A string array of allowed tool names

class McpAllowedToolsMcpToolFilter: …

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

authorization: Optional[str]

connector\_id: Optional[Literal["connector\_dropbox", "connector\_gmail", "connector\_googlecalendar", 5 more]]

about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading: Optional[bool]

headers: Optional[Dict[str, str]]

require\_approval: Optional[McpRequireApproval]

class McpRequireApprovalMcpToolApprovalFilter: …

always: Optional[McpRequireApprovalMcpToolApprovalFilterAlways]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

never: Optional[McpRequireApprovalMcpToolApprovalFilterNever]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

Literal["always", "never"]

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

"always"

"never"

server\_description: Optional[str]

server\_url: Optional[str]

tunnel\_id: Optional[str]

class CodeInterpreter: …

A tool that runs Python code to help generate a response to a prompt.

container: CodeInterpreterContainer

str

The container ID.

class CodeInterpreterContainerCodeInterpreterToolAuto: …

type: Literal["auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

type: Literal["code\_interpreter"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

class ProgrammaticToolCalling: …

type: Literal["programmatic\_tool\_calling"]

The type of the tool. Always `programmatic_tool_calling`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

action: Optional[Literal["generate", "edit", "auto"]]

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

"high"

"low"

input\_image\_mask: Optional[ImageGenerationInputImageMask]

file\_id: Optional[str]

image\_url: Optional[str]

model: Optional[Union[str, Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more], null]]

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

"auto"

"low"

output\_compression: Optional[int]

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

"png"

"webp"

"jpeg"

partial\_images: Optional[int]

minimum0

maximum3

quality: Optional[Literal["low", "medium", "high", "auto"]]

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool: …

type: Literal["shell"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

environment: Optional[Environment]

class BetaContainerAuto: …

type: Literal["container\_auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

skills: Optional[List[Skill]]

class BetaSkillReference: …

skill\_id: str

maxLength64

minLength1

type: Literal["skill\_reference"]

version: Optional[str]

class BetaInlineSkill: …

description: str

name: str

source: [BetaInlineSkillSource](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

type: Literal["inline"]

class BetaLocalEnvironment: …

type: Literal["local"]

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

description: str

name: str

path: str

class BetaContainerReference: …

container\_id: str

type: Literal["container\_reference"]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

class BetaNamespaceTool: …

description: str

minLength1

name: str

minLength1

tools: List[Tool]

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

parameters: Optional[object]

strict: Optional[bool]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

type: Literal["namespace"]

class BetaToolSearchTool: …

type: Literal["tool\_search"]

description: Optional[str]

execution: Optional[Literal["server", "client"]]

"server"

"client"

parameters: Optional[object]

class BetaWebSearchPreviewTool: …

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

type: Literal["approximate"]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

class BetaApplyPatchTool: …

type: Literal["apply\_patch"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

type: Literal["additional\_tools"]

The type of the item. Always `additional_tools`.

agent: Optional[AdditionalToolsAgent]

agent\_name: str

class BetaResponseReasoningItem: …

[managing context](https://platform.openai.com/docs/guides/conversation-state).

id: str

summary: List[Summary]

text: str

type: Literal["summary\_text"]

type: Literal["reasoning"]

agent: Optional[Agent]

agent\_name: str

content: Optional[List[Content]]

text: str

type: Literal["reasoning\_text"]

encrypted\_content: Optional[str]

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class Program: …

id: str

The unique ID of the program item.

call\_id: str

code: str

fingerprint: str

type: Literal["program"]

The type of the item. Always `program`.

agent: Optional[ProgramAgent]

agent\_name: str

class ProgramOutput: …

id: str

The unique ID of the program output item.

call\_id: str

result: str

status: Literal["completed", "incomplete"]

The terminal status of the program output item.

"completed"

"incomplete"

type: Literal["program\_output"]

The type of the item. Always `program_output`.

agent: Optional[ProgramOutputAgent]

agent\_name: str

class BetaResponseCompactionItem: …

A compaction item generated by the [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).

id: str

The unique ID of the compaction item.

encrypted\_content: str

The encrypted content that was produced by compaction.

type: Literal["compaction"]

agent: Optional[Agent]

agent\_name: str

created\_by: Optional[str]

The identifier of the actor that created the item.

class ImageGenerationCall: …

An image generation request made by the model.

id: str

result: Optional[str]

status: Literal["in\_progress", "completed", "generating", "failed"]

"in\_progress"

"completed"

"generating"

"failed"

type: Literal["image\_generation\_call"]

agent: Optional[ImageGenerationCallAgent]

agent\_name: str

class BetaResponseCodeInterpreterToolCall: …

id: str

code: Optional[str]

container\_id: str

outputs: Optional[List[Output]]

class OutputLogs: …

logs: str

type: Literal["logs"]

class OutputImage: …

type: Literal["image"]

url: str

status: Literal["in\_progress", "completed", "incomplete", 2 more]

"in\_progress"

"completed"

"incomplete"

"interpreting"

"failed"

type: Literal["code\_interpreter\_call"]

agent: Optional[Agent]

agent\_name: str

class LocalShellCall: …

A tool call to run a command on the local shell.

id: str

action: LocalShellCallAction

command: List[str]

env: Dict[str, str]

type: Literal["exec"]

timeout\_ms: Optional[int]

user: Optional[str]

working\_directory: Optional[str]

call\_id: str

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["local\_shell\_call"]

agent: Optional[LocalShellCallAgent]

agent\_name: str

class LocalShellCallOutput: …

The output of a local shell tool call.

id: str

output: str

type: Literal["local\_shell\_call\_output"]

agent: Optional[LocalShellCallOutputAgent]

agent\_name: str

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class BetaResponseFunctionShellToolCall: …

A tool call that executes one or more shell commands in a managed environment.

id: str

action: Action

commands: List[str]

max\_output\_length: Optional[int]

Optional maximum number of characters to return from each command.

timeout\_ms: Optional[int]

Optional timeout in milliseconds for the commands.

call\_id: str

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

"in\_progress"

"completed"

"incomplete"

type: Literal["shell\_call"]

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

created\_by: Optional[str]

The ID of the entity that created this tool call.

class BetaResponseFunctionShellToolCallOutput: …

The output of a shell tool call that was emitted.

id: str

The unique ID of the shell call output. Populated when this item is returned via API.

call\_id: str

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

exit\_code: int

Exit code from the shell process.

type: Literal["exit"]

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

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

created\_by: Optional[str]

The identifier of the actor that created the item.

class BetaResponseApplyPatchToolCall: …

A tool call that applies file diffs by creating, deleting, or updating files.

id: str

call\_id: str

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

"in\_progress"

"completed"

type: Literal["apply\_patch\_call"]

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

created\_by: Optional[str]

The ID of the entity that created this tool call.

class BetaResponseApplyPatchToolCallOutput: …

The output emitted by an apply patch tool call.

id: str

call\_id: str

status: Literal["completed", "failed"]

"completed"

"failed"

type: Literal["apply\_patch\_call\_output"]

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

created\_by: Optional[str]

The ID of the entity that created this tool call output.

output: Optional[str]

Optional textual output returned by the apply patch tool.

class McpListTools: …

A list of tools available on an MCP server.

id: str

server\_label: str

tools: List[McpListToolsTool]

input\_schema: object

name: str

annotations: Optional[object]

description: Optional[str]

type: Literal["mcp\_list\_tools"]

agent: Optional[McpListToolsAgent]

agent\_name: str

error: Optional[str]

class McpApprovalRequest: …

A request for human approval of a tool invocation.

id: str

arguments: str

name: str

server\_label: str

type: Literal["mcp\_approval\_request"]

agent: Optional[McpApprovalRequestAgent]

agent\_name: str

class McpApprovalResponse: …

A response to an MCP approval request.

id: str

approval\_request\_id: str

approve: bool

type: Literal["mcp\_approval\_response"]

agent: Optional[McpApprovalResponseAgent]

agent\_name: str

reason: Optional[str]

class McpCall: …

An invocation of a tool on an MCP server.

id: str

arguments: str

name: str

server\_label: str

type: Literal["mcp\_call"]

agent: Optional[McpCallAgent]

agent\_name: str

approval\_request\_id: Optional[str]

error: Optional[str]

output: Optional[str]

status: Optional[Literal["in\_progress", "completed", "incomplete", 2 more]]

"in\_progress"

"completed"

"incomplete"

"calling"

"failed"

class BetaResponseCustomToolCallItem: …

id: str

The unique ID of the custom tool call item.

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

created\_by: Optional[str]

The identifier of the actor that created the item.

class BetaResponseCustomToolCallOutputItem: …

id: str

The unique ID of the custom tool call output item.

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

created\_by: Optional[str]

The identifier of the actor that created the item.

first\_id: str

The ID of the first item in the list.

has\_more: bool

Whether there are more items available.

last\_id: str

The ID of the last item in the list.

object: Literal["list"]

The type of object returned, must be `list`.

#### ResponsesInput Tokens

##### [Get input token counts](/api/reference/python/resources/beta/subresources/responses/subresources/input_tokens/methods/count)

beta.responses.input\_tokens.count(InputTokenCountParams\*\*kwargs)  -> [InputTokenCountResponse](/api/reference/python/resources/beta#(resource)%20beta.responses.input_tokens%20%3E%20(model)%20input_token_count_response%20%3E%20(schema))

POST/responses/input\_tokens

##### ModelsExpand Collapse

class InputTokenCountResponse: …

input\_tokens: int

object: Literal["response.input\_tokens"]
