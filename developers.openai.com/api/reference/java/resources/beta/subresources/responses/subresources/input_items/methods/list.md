<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/responses/subresources/input_items/methods/list/ -->

[API Reference](/api/reference/java)

[Beta](/api/reference/java/resources/beta)

[Responses](/api/reference/java/resources/beta/subresources/responses)

[Input Items](/api/reference/java/resources/beta/subresources/responses/subresources/input_items)

# List input items

InputItemListPage beta().responses().inputItems().list(InputItemListParamsparams = InputItemListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/responses/{response\_id}/input\_items

Returns a list of input items for a given response.

##### ParametersExpand Collapse

InputItemListParams params

Optional<String> responseId

Optional<String> after

An item ID to list items after, used in pagination.

Optional<List<[BetaResponseIncludable](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_includable%20%3E%20(schema))>> include

Additional fields to include in the response. See the `include`
parameter for Response creation above for more information.

FILE\_SEARCH\_CALL\_RESULTS("file\_search\_call.results")

WEB\_SEARCH\_CALL\_RESULTS("web\_search\_call.results")

WEB\_SEARCH\_CALL\_ACTION\_SOURCES("web\_search\_call.action.sources")

MESSAGE\_INPUT\_IMAGE\_IMAGE\_URL("message.input\_image.image\_url")

COMPUTER\_CALL\_OUTPUT\_OUTPUT\_IMAGE\_URL("computer\_call\_output.output.image\_url")

CODE\_INTERPRETER\_CALL\_OUTPUTS("code\_interpreter\_call.outputs")

REASONING\_ENCRYPTED\_CONTENT("reasoning.encrypted\_content")

MESSAGE\_OUTPUT\_TEXT\_LOGPROBS("message.output\_text.logprobs")

Optional<Long> limit

A limit on the number of objects to be returned. Limit can range between
1 and 100, and the default is 20.

Optional<[Order](/api/reference/java/resources/beta/subresources/responses/subresources/input_items/methods/list#(resource)%20beta.responses.input_items%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))> order

The order to return the input items in. Default is `desc`.

* `asc`: Return the input items in ascending order.
* `desc`: Return the input items in descending order.

ASC("asc")

DESC("desc")

Optional<List<Beta>> betas

RESPONSES\_MULTI\_AGENT\_V1("responses\_multi\_agent=v1")

##### ReturnsExpand Collapse

class BetaResponseItem: A class that can be one of several variants.union

Content item used to generate a response.

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

### List input items

Java

package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.responses.inputitems.InputItemListPage;
import com.openai.models.beta.responses.inputitems.InputItemListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        InputItemListPage page = client.beta().responses().inputItems().list("response_id");

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
