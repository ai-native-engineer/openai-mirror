<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/responses/ -->

[API Reference](/api/reference/java)

[Beta](/api/reference/java/resources/beta)

# Responses

##### [Create a model response](/api/reference/java/resources/beta/subresources/responses/methods/create)

[BetaResponse](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema)) beta().responses().create(ResponseCreateParamsparams = ResponseCreateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/responses

##### [Get a model response](/api/reference/java/resources/beta/subresources/responses/methods/retrieve)

[BetaResponse](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema)) beta().responses().retrieve(ResponseRetrieveParamsparams = ResponseRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/responses/{response\_id}

##### [Delete a model response](/api/reference/java/resources/beta/subresources/responses/methods/delete)

beta().responses().delete(ResponseDeleteParamsparams = ResponseDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/responses/{response\_id}

##### [Cancel a response](/api/reference/java/resources/beta/subresources/responses/methods/cancel)

[BetaResponse](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema)) beta().responses().cancel(ResponseCancelParamsparams = ResponseCancelParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/responses/{response\_id}/cancel

##### [Compact a response](/api/reference/java/resources/beta/subresources/responses/methods/compact)

[BetaCompactedResponse](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_compacted_response%20%3E%20(schema)) beta().responses().compact(ResponseCompactParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/responses/compact

##### ModelsExpand Collapse

class BetaApplyPatchTool:

JsonValue; type "apply\_patch"constant"apply\_patch"constant

Optional<List<AllowedCaller>> allowedCallers

DIRECT("direct")

PROGRAMMATIC("programmatic")

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

class BetaComputerAction: A class that can be one of several variants.union

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

class BetaContainerNetworkPolicyDisabled:

JsonValue; type "disabled"constant"disabled"constant

class BetaContainerNetworkPolicyDomainSecret:

String domain

minLength1

String name

minLength1

String value

maxLength10485760

minLength1

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

class BetaInlineSkill:

String description

String name

[BetaInlineSkillSource](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema)) source

JsonValue; type "inline"constant"inline"constant

class BetaInlineSkillSource:

String data

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

JsonValue; mediaType "application/zip"constant"application/zip"constant

The media type of the inline skill payload. Must be `application/zip`.

JsonValue; type "base64"constant"base64"constant

The type of the inline skill source. Must be `base64`.

class BetaLocalEnvironment:

JsonValue; type "local"constant"local"constant

Optional<List<[BetaLocalSkill](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))>> skills

String description

String name

String path

class BetaLocalSkill:

String description

String name

String path

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

class BetaResponse:

String id

Unique identifier for this Response.

double createdAt

Unix timestamp (in seconds) of when this Response was created.

formatunixtime

Optional<[BetaResponseError](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_error%20%3E%20(schema))> error

An error object returned when the model fails to generate a Response.

Optional<IncompleteDetails> incompleteDetails

Details about why the response is incomplete.

Optional<Reason> reason

The reason why the response is incomplete.

MAX\_OUTPUT\_TOKENS("max\_output\_tokens")

CONTENT\_FILTER("content\_filter")

Optional<Instructions> instructions

A system (or developer) message inserted into the model’s context.

When using along with `previous_response_id`, the instructions from a previous
response will not be carried over to the next response. This makes it simple
to swap out system (or developer) messages in new responses.

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

Optional<Metadata> metadata

format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

Model model

Model ID used to generate the response, like `gpt-4o` or `o3`. OpenAI
offers a wide range of models with different capabilities, performance
characteristics, and price points. Refer to the [model guide](https://platform.openai.com/docs/models)
to browse and compare available models.

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

JsonValue; object\_ "response"constant"response"constant

The object type of this resource - always set to `response`.

List<[BetaResponseOutputItem](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_item%20%3E%20(schema))> output

An array of content items generated by the model.

* The length and order of items in the `output` array is dependent
  on the model’s response.
* Rather than accessing the first item in the `output` array and
  assuming it’s an `assistant` message with the content generated by
  the model, you might consider using the `output_text` property where
  supported in SDKs.

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

boolean parallelToolCalls

Whether to allow the model to run tool calls in parallel.

Optional<Double> temperature

What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.
We generally recommend altering this or `top_p` but not both.

minimum0

maximum2

ToolChoice toolChoice

How the model should select which tool (or tools) to use when generating
a response. See the `tools` parameter to see how to specify which tools
the model can call.

enum BetaToolChoiceOptions:

Controls which (if any) tool is called by the model.

`none` means the model will not call any tool and instead generates a message.

`auto` means the model can pick between generating a message or calling one or
more tools.

`required` means the model must call one or more tools.

NONE("none")

AUTO("auto")

REQUIRED("required")

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

class BetaToolChoiceCustom:

Use this option to force the model to call a specific custom tool.

String name

The name of the custom tool to call.

JsonValue; type "custom"constant"custom"constant

For custom tool calling, the type is always `custom`.

JsonValue;

JsonValue; type "programmatic\_tool\_calling"constant"programmatic\_tool\_calling"constant

The tool to call. Always `programmatic_tool_calling`.

class BetaToolChoiceApplyPatch:

Forces the model to call the apply\_patch tool when executing a tool call.

JsonValue; type "apply\_patch"constant"apply\_patch"constant

The tool to call. Always `apply_patch`.

class BetaToolChoiceShell:

Forces the model to call the shell tool when a tool call is required.

JsonValue; type "shell"constant"shell"constant

The tool to call. Always `shell`.

List<[BetaTool](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))> tools

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

Optional<Double> topP

An alternative to sampling with temperature, called nucleus sampling,
where the model considers the results of the tokens with top\_p probability
mass. So 0.1 means only the tokens comprising the top 10% probability mass
are considered.

We generally recommend altering this or `temperature` but not both.

minimum0

maximum1

Optional<Boolean> background

Whether to run the model response in the background.
[Learn more](https://platform.openai.com/docs/guides/background).

Optional<Double> completedAt

Unix timestamp (in seconds) of when this Response was completed.
Only present when the status is `completed`.

formatunixtime

Optional<Conversation> conversation

The conversation that this response belonged to. Input items and output items from this response were automatically added to this conversation.

String id

The unique ID of the conversation that this response was associated with.

Optional<Long> maxOutputTokens

An upper bound for the number of tokens that can be generated for a response, including visible output tokens and [reasoning tokens](https://platform.openai.com/docs/guides/reasoning).

Optional<Long> maxToolCalls

The maximum number of total calls to built-in tools that can be processed in a response. This maximum number applies across all built-in tool calls, not per individual tool. Any further attempts to call a tool by the model will be ignored.

Optional<Moderation> moderation

Moderation results for the response input and output, if moderated completions were requested.

Input input

Moderation for the response input.

class ModerationResult:

A moderation result produced for the response input or output.

Categories categories

A dictionary of moderation categories to booleans, True if the input is flagged under this category.

CategoryAppliedInputTypes categoryAppliedInputTypes

Which modalities of input are reflected by the score for each category.

TEXT("text")

IMAGE("image")

CategoryScores categoryScores

A dictionary of moderation categories to scores.

boolean flagged

A boolean indicating whether the content was flagged by any category.

String model

The moderation model that produced this result.

JsonValue; type "moderation\_result"constant"moderation\_result"constant

The object type, which was always `moderation_result` for successful moderation results.

class Error:

An error produced while attempting moderation for the response input or output.

String code

The error code.

String message

The error message.

JsonValue; type "error"constant"error"constant

The object type, which was always `error` for moderation failures.

Output output

Moderation for the response output.

class ModerationResult:

A moderation result produced for the response input or output.

Categories categories

A dictionary of moderation categories to booleans, True if the input is flagged under this category.

CategoryAppliedInputTypes categoryAppliedInputTypes

Which modalities of input are reflected by the score for each category.

TEXT("text")

IMAGE("image")

CategoryScores categoryScores

A dictionary of moderation categories to scores.

boolean flagged

A boolean indicating whether the content was flagged by any category.

String model

The moderation model that produced this result.

JsonValue; type "moderation\_result"constant"moderation\_result"constant

The object type, which was always `moderation_result` for successful moderation results.

class Error:

An error produced while attempting moderation for the response input or output.

String code

The error code.

String message

The error message.

JsonValue; type "error"constant"error"constant

The object type, which was always `error` for moderation failures.

Optional<String> previousResponseId

The unique ID of the previous response to the model. Use this to
create multi-turn conversations. Learn more about
[conversation state](https://platform.openai.com/docs/guides/conversation-state). Cannot be used in conjunction with `conversation`.

Optional<[BetaResponsePrompt](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_prompt%20%3E%20(schema))> prompt

Reference to a prompt template and its variables.
[Learn more](https://platform.openai.com/docs/guides/text?api-mode=responses#reusable-prompts).

Optional<String> promptCacheKey

Used by OpenAI to cache responses for similar requests to optimize your cache hit rates. Replaces the `user` field. [Learn more](https://platform.openai.com/docs/guides/prompt-caching).

Optional<PromptCacheOptions> promptCacheOptions

The prompt-caching options that were applied to the response. Supported for `gpt-5.6` and later models.

Mode mode

Whether implicit prompt-cache breakpoints were enabled.

IMPLICIT("implicit")

EXPLICIT("explicit")

Ttl ttl

The minimum lifetime applied to each cache breakpoint.

DeprecatedOptional<PromptCacheRetention> promptCacheRetention

Deprecated. Use `prompt_cache_options.ttl` instead.

The retention policy for the prompt cache. Set to `24h` to enable extended prompt caching, which keeps cached prefixes active for longer, up to a maximum of 24 hours. [Learn more](https://platform.openai.com/docs/guides/prompt-caching#prompt-cache-retention).
This field expresses a maximum retention policy, while
`prompt_cache_options.ttl` expresses a minimum cache lifetime. The two
fields are independent and do not interact.
For `gpt-5.5`, `gpt-5.5-pro`, and future models, only `24h` is supported.

For older models that support both `in_memory` and `24h`, the default depends on your organization’s data retention policy:

* Organizations without ZDR enabled default to `24h`.
* Organizations with ZDR enabled default to `in_memory` when `prompt_cache_retention` is not specified.

IN\_MEMORY("in\_memory")

\_24H("24h")

Optional<Reasoning> reasoning

**gpt-5 and o-series models only**

Configuration options for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).

Optional<Context> context

Controls which reasoning items are rendered back to the model on later turns.
When returned on a response, this is the effective reasoning context mode
used for the response.

AUTO("auto")

CURRENT\_TURN("current\_turn")

ALL\_TURNS("all\_turns")

Optional<Effort> effort

Constrains effort on reasoning for reasoning models. Currently supported
values are `none`, `minimal`, `low`, `medium`, `high`, `xhigh`, and `max`.
Reducing reasoning effort can result in faster responses and fewer tokens
used on reasoning in a response. Not all reasoning models support every
value. See the
[reasoning guide](https://platform.openai.com/docs/guides/reasoning)
for model-specific support.

NONE("none")

MINIMAL("minimal")

LOW("low")

MEDIUM("medium")

HIGH("high")

XHIGH("xhigh")

MAX("max")

DeprecatedOptional<GenerateSummary> generateSummary

**Deprecated:** use `summary` instead.

A summary of the reasoning performed by the model. This can be
useful for debugging and understanding the model’s reasoning process.
One of `auto`, `concise`, or `detailed`.

AUTO("auto")

CONCISE("concise")

DETAILED("detailed")

Optional<Mode> mode

Controls the reasoning execution mode for the request.

When returned on a response, this is the effective execution mode.

STANDARD("standard")

PRO("pro")

Optional<Summary> summary

A summary of the reasoning performed by the model. This can be
useful for debugging and understanding the model’s reasoning process.
One of `auto`, `concise`, or `detailed`.

`concise` is supported for `computer-use-preview` models and all reasoning models after `gpt-5`.

AUTO("auto")

CONCISE("concise")

DETAILED("detailed")

Optional<String> safetyIdentifier

A stable identifier used to help detect users of your application that may be violating OpenAI’s usage policies.
The IDs should be a string that uniquely identifies each user, with a maximum length of 64 characters. We recommend hashing their username or email address, in order to avoid sending us any identifying information. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).

maxLength64

Optional<ServiceTier> serviceTier

Specifies the processing type used for serving the request.

* If set to ‘auto’, then the request will be processed with the service tier configured in the Project settings. Unless otherwise configured, the Project will use ‘default’.
* If set to ‘default’, then the request will be processed with the standard pricing and performance for the selected model.
* If set to ‘[flex](https://platform.openai.com/docs/guides/flex-processing)’ or ‘[priority](https://openai.com/api-priority-processing/)’, then the request will be processed with the corresponding service tier.
* When not set, the default behavior is ‘auto’.

When the `service_tier` parameter is set, the response body will include the `service_tier` value based on the processing mode actually used to serve the request. This response value may be different from the value set in the parameter.

AUTO("auto")

DEFAULT("default")

FLEX("flex")

SCALE("scale")

PRIORITY("priority")

Optional<[BetaResponseStatus](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_status%20%3E%20(schema))> status

The status of the response generation. One of `completed`, `failed`,
`in_progress`, `cancelled`, `queued`, or `incomplete`.

Optional<[BetaResponseTextConfig](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_text_config%20%3E%20(schema))> text

Configuration options for a text response from the model. Can be plain
text or structured JSON data. Learn more:

* [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
* [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

Optional<Long> topLogprobs

An integer between 0 and 20 specifying the maximum number of most likely
tokens to return at each token position, each with an associated log
probability. In some cases, the number of returned tokens may be fewer than
requested.

minimum0

maximum20

Optional<Truncation> truncation

The truncation strategy to use for the model response.

* `auto`: If the input to this Response exceeds
  the model’s context window size, the model will truncate the
  response to fit the context window by dropping items from the beginning of the conversation.
* `disabled` (default): If the input size will exceed the context window
  size for a model, the request will fail with a 400 error.

AUTO("auto")

DISABLED("disabled")

Optional<[BetaResponseUsage](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_usage%20%3E%20(schema))> usage

Represents token usage details including input tokens, output tokens,
a breakdown of output tokens, and the total tokens used.

DeprecatedOptional<String> user

This field is being replaced by `safety_identifier` and `prompt_cache_key`. Use `prompt_cache_key` instead to maintain caching optimizations.
A stable identifier for your end-users.
Used to boost cache hit rates by better bucketing similar requests and to help OpenAI detect and prevent abuse. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).

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

class BetaResponseAudioDeltaEvent:

Emitted when there is a partial audio response.

String delta

A chunk of Base64 encoded response audio bytes.

long sequenceNumber

A sequence number for this chunk of the stream response.

JsonValue; type "response.audio.delta"constant"response.audio.delta"constant

The type of the event. Always `response.audio.delta`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseAudioDoneEvent:

Emitted when the audio response is complete.

long sequenceNumber

The sequence number of the delta.

JsonValue; type "response.audio.done"constant"response.audio.done"constant

The type of the event. Always `response.audio.done`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseAudioTranscriptDeltaEvent:

Emitted when there is a partial transcript of audio.

String delta

The partial transcript of the audio response.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.audio.transcript.delta"constant"response.audio.transcript.delta"constant

The type of the event. Always `response.audio.transcript.delta`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseAudioTranscriptDoneEvent:

Emitted when the full audio transcript is completed.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.audio.transcript.done"constant"response.audio.transcript.done"constant

The type of the event. Always `response.audio.transcript.done`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseCodeInterpreterCallCodeDeltaEvent:

Emitted when a partial code snippet is streamed by the code interpreter.

String delta

The partial code snippet being streamed by the code interpreter.

String itemId

The unique identifier of the code interpreter tool call item.

long outputIndex

The index of the output item in the response for which the code is being streamed.

long sequenceNumber

The sequence number of this event, used to order streaming events.

JsonValue; type "response.code\_interpreter\_call\_code.delta"constant"response.code\_interpreter\_call\_code.delta"constant

The type of the event. Always `response.code_interpreter_call_code.delta`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseCodeInterpreterCallCodeDoneEvent:

Emitted when the code snippet is finalized by the code interpreter.

String code

The final code snippet output by the code interpreter.

String itemId

The unique identifier of the code interpreter tool call item.

long outputIndex

The index of the output item in the response for which the code is finalized.

long sequenceNumber

The sequence number of this event, used to order streaming events.

JsonValue; type "response.code\_interpreter\_call\_code.done"constant"response.code\_interpreter\_call\_code.done"constant

The type of the event. Always `response.code_interpreter_call_code.done`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseCodeInterpreterCallCompletedEvent:

Emitted when the code interpreter call is completed.

String itemId

The unique identifier of the code interpreter tool call item.

long outputIndex

The index of the output item in the response for which the code interpreter call is completed.

long sequenceNumber

The sequence number of this event, used to order streaming events.

JsonValue; type "response.code\_interpreter\_call.completed"constant"response.code\_interpreter\_call.completed"constant

The type of the event. Always `response.code_interpreter_call.completed`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseCodeInterpreterCallInProgressEvent:

Emitted when a code interpreter call is in progress.

String itemId

The unique identifier of the code interpreter tool call item.

long outputIndex

The index of the output item in the response for which the code interpreter call is in progress.

long sequenceNumber

The sequence number of this event, used to order streaming events.

JsonValue; type "response.code\_interpreter\_call.in\_progress"constant"response.code\_interpreter\_call.in\_progress"constant

The type of the event. Always `response.code_interpreter_call.in_progress`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseCodeInterpreterCallInterpretingEvent:

Emitted when the code interpreter is actively interpreting the code snippet.

String itemId

The unique identifier of the code interpreter tool call item.

long outputIndex

The index of the output item in the response for which the code interpreter is interpreting code.

long sequenceNumber

The sequence number of this event, used to order streaming events.

JsonValue; type "response.code\_interpreter\_call.interpreting"constant"response.code\_interpreter\_call.interpreting"constant

The type of the event. Always `response.code_interpreter_call.interpreting`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

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

class BetaResponseCompletedEvent:

Emitted when the model response is complete.

[BetaResponse](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema)) response

Properties of the completed response.

long sequenceNumber

The sequence number for this event.

JsonValue; type "response.completed"constant"response.completed"constant

The type of the event. Always `response.completed`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

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

class BetaResponseComputerToolCallOutputScreenshot:

JsonValue; type "computer\_screenshot"constant"computer\_screenshot"constant

Specifies the event type. For a computer screenshot, this property is
always set to `computer_screenshot`.

Optional<String> fileId

Optional<String> imageUrl

class BetaResponseContainerReference:

Represents a container created with /v1/containers.

String containerId

JsonValue; type "container\_reference"constant"container\_reference"constant

The environment type. Always `container_reference`.

class BetaResponseContent: A class that can be one of several variants.union

Multi-modal input and output contents.

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

ReasoningText

String text

JsonValue; type "reasoning\_text"constant"reasoning\_text"constant

class BetaResponseContentPartAddedEvent:

Emitted when a new content part is added.

long contentIndex

The index of the content part that was added.

String itemId

The ID of the output item that the content part was added to.

long outputIndex

The index of the output item that the content part was added to.

Part part

The content part that was added.

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

class ReasoningText:

String text

JsonValue; type "reasoning\_text"constant"reasoning\_text"constant

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.content\_part.added"constant"response.content\_part.added"constant

The type of the event. Always `response.content_part.added`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseContentPartDoneEvent:

Emitted when a content part is done.

long contentIndex

The index of the content part that is done.

String itemId

The ID of the output item that the content part was added to.

long outputIndex

The index of the output item that the content part was added to.

Part part

The content part that is done.

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

class ReasoningText:

String text

JsonValue; type "reasoning\_text"constant"reasoning\_text"constant

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.content\_part.done"constant"response.content\_part.done"constant

The type of the event. Always `response.content_part.done`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseConversationParam:

The conversation that this response belongs to.

String id

The unique ID of the conversation.

class BetaResponseCreatedEvent:

An event that is emitted when a response is created.

[BetaResponse](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema)) response

The response that was created.

long sequenceNumber

The sequence number for this event.

JsonValue; type "response.created"constant"response.created"constant

The type of the event. Always `response.created`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

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

class BetaResponseCustomToolCallItem:

String id

The unique ID of the custom tool call item.

Status status

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

Optional<String> createdBy

The identifier of the actor that created the item.

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

class BetaResponseCustomToolCallOutputItem:

String id

The unique ID of the custom tool call output item.

Status status

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

Optional<String> createdBy

The identifier of the actor that created the item.

class BetaResponseError:

An error object returned when the model fails to generate a Response.

Code code

The error code for the response.

SERVER\_ERROR("server\_error")

RATE\_LIMIT\_EXCEEDED("rate\_limit\_exceeded")

INVALID\_PROMPT("invalid\_prompt")

BIO\_POLICY("bio\_policy")

VECTOR\_STORE\_TIMEOUT("vector\_store\_timeout")

INVALID\_IMAGE("invalid\_image")

INVALID\_IMAGE\_FORMAT("invalid\_image\_format")

INVALID\_BASE64\_IMAGE("invalid\_base64\_image")

INVALID\_IMAGE\_URL("invalid\_image\_url")

IMAGE\_TOO\_LARGE("image\_too\_large")

IMAGE\_TOO\_SMALL("image\_too\_small")

IMAGE\_PARSE\_ERROR("image\_parse\_error")

IMAGE\_CONTENT\_POLICY\_VIOLATION("image\_content\_policy\_violation")

INVALID\_IMAGE\_MODE("invalid\_image\_mode")

IMAGE\_FILE\_TOO\_LARGE("image\_file\_too\_large")

UNSUPPORTED\_IMAGE\_MEDIA\_TYPE("unsupported\_image\_media\_type")

EMPTY\_IMAGE\_FILE("empty\_image\_file")

FAILED\_TO\_DOWNLOAD\_IMAGE("failed\_to\_download\_image")

IMAGE\_FILE\_NOT\_FOUND("image\_file\_not\_found")

String message

A human-readable description of the error.

class BetaResponseErrorEvent:

Emitted when an error occurs.

Optional<String> code

The error code.

String message

The error message.

Optional<String> param

The error parameter.

long sequenceNumber

The sequence number of this event.

JsonValue; type "error"constant"error"constant

The type of the event. Always `error`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseFailedEvent:

An event that is emitted when a response fails.

[BetaResponse](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema)) response

The response that failed.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.failed"constant"response.failed"constant

The type of the event. Always `response.failed`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseFileSearchCallCompletedEvent:

Emitted when a file search call is completed (results found).

String itemId

The ID of the output item that the file search call is initiated.

long outputIndex

The index of the output item that the file search call is initiated.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.file\_search\_call.completed"constant"response.file\_search\_call.completed"constant

The type of the event. Always `response.file_search_call.completed`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseFileSearchCallInProgressEvent:

Emitted when a file search call is initiated.

String itemId

The ID of the output item that the file search call is initiated.

long outputIndex

The index of the output item that the file search call is initiated.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.file\_search\_call.in\_progress"constant"response.file\_search\_call.in\_progress"constant

The type of the event. Always `response.file_search_call.in_progress`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseFileSearchCallSearchingEvent:

Emitted when a file search is currently searching.

String itemId

The ID of the output item that the file search call is initiated.

long outputIndex

The index of the output item that the file search call is searching.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.file\_search\_call.searching"constant"response.file\_search\_call.searching"constant

The type of the event. Always `response.file_search_call.searching`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

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

class BetaResponseFormatTextConfig: A class that can be one of several variants.union

An object specifying the format that the model must output.

Configuring `{ "type": "json_schema" }` enables Structured Outputs,
which ensures the model will match your supplied JSON schema. Learn more in the
[Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

The default format is `{ "type": "text" }` with no additional options.

**Not recommended for gpt-4o and newer models:**

Setting to `{ "type": "json_object" }` enables the older JSON mode, which
ensures the message the model generates is valid JSON. Using `json_schema`
is preferred for models that support it.

JsonValue;

JsonValue; type "text"constant"text"constant

The type of response format being defined. Always `text`.

class BetaResponseFormatTextJsonSchemaConfig:

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

String name

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

Schema schema

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

JsonValue; type "json\_schema"constant"json\_schema"constant

The type of response format being defined. Always `json_schema`.

Optional<String> description

A description of what the response format is for, used by the model to
determine how to respond in the format.

Optional<Boolean> strict

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

JsonValue;

JsonValue; type "json\_object"constant"json\_object"constant

The type of response format being defined. Always `json_object`.

class BetaResponseFormatTextJsonSchemaConfig:

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

String name

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

Schema schema

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

JsonValue; type "json\_schema"constant"json\_schema"constant

The type of response format being defined. Always `json_schema`.

Optional<String> description

A description of what the response format is for, used by the model to
determine how to respond in the format.

Optional<Boolean> strict

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

class BetaResponseFunctionCallArgumentsDeltaEvent:

Emitted when there is a partial function-call arguments delta.

String delta

The function-call arguments delta that is added.

String itemId

The ID of the output item that the function-call arguments delta is added to.

long outputIndex

The index of the output item that the function-call arguments delta is added to.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.function\_call\_arguments.delta"constant"response.function\_call\_arguments.delta"constant

The type of the event. Always `response.function_call_arguments.delta`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseFunctionCallArgumentsDoneEvent:

Emitted when function-call arguments are finalized.

String arguments

The function-call arguments.

String itemId

The ID of the item.

String name

The name of the function that was called.

long outputIndex

The index of the output item.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.function\_call\_arguments.done"constant"response.function\_call\_arguments.done"constant

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseFunctionCallOutputItem: A class that can be one of several variants.union

A piece of message content, such as text, an image, or a file.

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

class BetaResponseFunctionShellCallOutputContent:

Captured stdout and stderr for a portion of a shell tool call output.

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

class BetaResponseInProgressEvent:

Emitted when the response is in progress.

[BetaResponse](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema)) response

The response that is in progress.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.in\_progress"constant"response.in\_progress"constant

The type of the event. Always `response.in_progress`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

enum BetaResponseIncludable:

Specify additional output data to include in the model response. Currently supported values are:

* `web_search_call.results`: Include the search results of the web search tool call.
* `web_search_call.action.sources`: Include the sources of the web search tool call.
* `code_interpreter_call.outputs`: Includes the outputs of python code execution in code interpreter tool call items.
* `computer_call_output.output.image_url`: Include image urls from the computer call output.
* `file_search_call.results`: Include the search results of the file search tool call.
* `message.input_image.image_url`: Include image urls from the input message.
* `message.output_text.logprobs`: Include logprobs with assistant messages.
* `reasoning.encrypted_content`: Includes an encrypted version of reasoning tokens in reasoning item outputs. This enables reasoning items to be used in multi-turn conversations when using the Responses API statelessly (like when the `store` parameter is set to `false`, or when an organization is enrolled in the zero data retention program).

FILE\_SEARCH\_CALL\_RESULTS("file\_search\_call.results")

WEB\_SEARCH\_CALL\_RESULTS("web\_search\_call.results")

WEB\_SEARCH\_CALL\_ACTION\_SOURCES("web\_search\_call.action.sources")

MESSAGE\_INPUT\_IMAGE\_IMAGE\_URL("message.input\_image.image\_url")

COMPUTER\_CALL\_OUTPUT\_OUTPUT\_IMAGE\_URL("computer\_call\_output.output.image\_url")

CODE\_INTERPRETER\_CALL\_OUTPUTS("code\_interpreter\_call.outputs")

REASONING\_ENCRYPTED\_CONTENT("reasoning.encrypted\_content")

MESSAGE\_OUTPUT\_TEXT\_LOGPROBS("message.output\_text.logprobs")

class BetaResponseIncompleteEvent:

An event that is emitted when a response finishes as incomplete.

[BetaResponse](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema)) response

The response that was incomplete.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.incomplete"constant"response.incomplete"constant

The type of the event. Always `response.incomplete`.

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

class BetaResponseInjectEvent:

Injects input items into an active response over a WebSocket connection.
The items are validated and committed atomically. Currently, the server
accepts client-owned tool outputs that resume a waiting agent.

List<[BetaResponseInputItem](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_item%20%3E%20(schema))> input

Input items to inject into the active response.

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

The ID of the active response that should receive the input.

JsonValue; type "response.inject"constant"response.inject"constant

The event discriminator. Always `response.inject`.

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

class BetaResponseInputAudio:

An audio input to the model.

InputAudio inputAudio

String data

Base64-encoded audio data.

Format format

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

MP3("mp3")

WAV("wav")

JsonValue; type "input\_audio"constant"input\_audio"constant

The type of the input item. Always `input_audio`.

class BetaResponseInputContent: A class that can be one of several variants.union

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

class BetaResponseInputItem: A class that can be one of several variants.union

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

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

class BetaResponseInputText:

String text

JsonValue; type "input\_text"constant"input\_text"constant

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

JsonValue; mode "explicit"constant"explicit"constant

class BetaResponseInputTextContent:

String text

maxLength10485760

JsonValue; type "input\_text"constant"input\_text"constant

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

JsonValue; mode "explicit"constant"explicit"constant

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

class BetaResponseLocalEnvironment:

Represents the use of a local environment to perform shell actions.

JsonValue; type "local"constant"local"constant

The environment type. Always `local`.

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

class BetaResponseOutputAudio:

An audio output from the model.

String data

Base64-encoded audio data from the model.

String transcript

The transcript of the audio data from the model.

JsonValue; type "output\_audio"constant"output\_audio"constant

The type of the output audio. Always `output_audio`.

class BetaResponseOutputItem: A class that can be one of several variants.union

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

class BetaResponseOutputItemAddedEvent:

Emitted when a new output item is added.

[BetaResponseOutputItem](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_item%20%3E%20(schema)) item

The output item that was added.

long outputIndex

The index of the output item that was added.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.output\_item.added"constant"response.output\_item.added"constant

The type of the event. Always `response.output_item.added`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseOutputItemDoneEvent:

Emitted when an output item is marked done.

[BetaResponseOutputItem](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_item%20%3E%20(schema)) item

The output item that was marked done.

long outputIndex

The index of the output item that was marked done.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.output\_item.done"constant"response.output\_item.done"constant

The type of the event. Always `response.output_item.done`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

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

class BetaResponseOutputRefusal:

String refusal

JsonValue; type "refusal"constant"refusal"constant

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

class BetaResponsePrompt:

Reference to a prompt template and its variables.
[Learn more](https://platform.openai.com/docs/guides/text?api-mode=responses#reusable-prompts).

String id

The unique identifier of the prompt template to use.

Optional<Variables> variables

Optional map of values to substitute in for variables in your
prompt. The substitution values can either be strings, or other
Response input types like images or files.

String

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

Optional<String> version

Optional version of the prompt template.

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

class BetaResponseReasoningSummaryPartAddedEvent:

Emitted when a new reasoning summary part is added.

String itemId

The ID of the item this summary part is associated with.

long outputIndex

The index of the output item this summary part is associated with.

Part part

The summary part that was added.

String text

The text of the summary part.

JsonValue; type "summary\_text"constant"summary\_text"constant

The type of the summary part. Always `summary_text`.

long sequenceNumber

The sequence number of this event.

long summaryIndex

The index of the summary part within the reasoning summary.

JsonValue; type "response.reasoning\_summary\_part.added"constant"response.reasoning\_summary\_part.added"constant

The type of the event. Always `response.reasoning_summary_part.added`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseReasoningSummaryPartDoneEvent:

Emitted when a reasoning summary part is completed.

String itemId

The ID of the item this summary part is associated with.

long outputIndex

The index of the output item this summary part is associated with.

Part part

The completed summary part.

String text

The text of the summary part.

JsonValue; type "summary\_text"constant"summary\_text"constant

The type of the summary part. Always `summary_text`.

long sequenceNumber

The sequence number of this event.

long summaryIndex

The index of the summary part within the reasoning summary.

JsonValue; type "response.reasoning\_summary\_part.done"constant"response.reasoning\_summary\_part.done"constant

The type of the event. Always `response.reasoning_summary_part.done`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

Optional<Status> status

The completion status of the summary part. Omitted when the part completed
normally and set to `incomplete` when generation was interrupted.

class BetaResponseReasoningSummaryTextDeltaEvent:

Emitted when a delta is added to a reasoning summary text.

String delta

The text delta that was added to the summary.

String itemId

The ID of the item this summary text delta is associated with.

long outputIndex

The index of the output item this summary text delta is associated with.

long sequenceNumber

The sequence number of this event.

long summaryIndex

The index of the summary part within the reasoning summary.

JsonValue; type "response.reasoning\_summary\_text.delta"constant"response.reasoning\_summary\_text.delta"constant

The type of the event. Always `response.reasoning_summary_text.delta`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseReasoningSummaryTextDoneEvent:

Emitted when a reasoning summary text is completed.

String itemId

The ID of the item this summary text is associated with.

long outputIndex

The index of the output item this summary text is associated with.

long sequenceNumber

The sequence number of this event.

long summaryIndex

The index of the summary part within the reasoning summary.

String text

The full text of the completed reasoning summary.

JsonValue; type "response.reasoning\_summary\_text.done"constant"response.reasoning\_summary\_text.done"constant

The type of the event. Always `response.reasoning_summary_text.done`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseReasoningTextDeltaEvent:

Emitted when a delta is added to a reasoning text.

long contentIndex

The index of the reasoning content part this delta is associated with.

String delta

The text delta that was added to the reasoning content.

String itemId

The ID of the item this reasoning text delta is associated with.

long outputIndex

The index of the output item this reasoning text delta is associated with.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.reasoning\_text.delta"constant"response.reasoning\_text.delta"constant

The type of the event. Always `response.reasoning_text.delta`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseReasoningTextDoneEvent:

Emitted when a reasoning text is completed.

long contentIndex

The index of the reasoning content part.

String itemId

The ID of the item this reasoning text is associated with.

long outputIndex

The index of the output item this reasoning text is associated with.

long sequenceNumber

The sequence number of this event.

String text

The full text of the completed reasoning content.

JsonValue; type "response.reasoning\_text.done"constant"response.reasoning\_text.done"constant

The type of the event. Always `response.reasoning_text.done`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseRefusalDeltaEvent:

Emitted when there is a partial refusal text.

long contentIndex

The index of the content part that the refusal text is added to.

String delta

The refusal text that is added.

String itemId

The ID of the output item that the refusal text is added to.

long outputIndex

The index of the output item that the refusal text is added to.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.refusal.delta"constant"response.refusal.delta"constant

The type of the event. Always `response.refusal.delta`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseRefusalDoneEvent:

Emitted when refusal text is finalized.

long contentIndex

The index of the content part that the refusal text is finalized.

String itemId

The ID of the output item that the refusal text is finalized.

long outputIndex

The index of the output item that the refusal text is finalized.

String refusal

The refusal text that is finalized.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.refusal.done"constant"response.refusal.done"constant

The type of the event. Always `response.refusal.done`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

enum BetaResponseStatus:

The status of the response generation. One of `completed`, `failed`,
`in_progress`, `cancelled`, `queued`, or `incomplete`.

COMPLETED("completed")

FAILED("failed")

IN\_PROGRESS("in\_progress")

CANCELLED("cancelled")

QUEUED("queued")

INCOMPLETE("incomplete")

class BetaResponseStreamEvent: A class that can be one of several variants.union

Emitted when there is a partial audio response.

class BetaResponseAudioDeltaEvent:

Emitted when there is a partial audio response.

String delta

A chunk of Base64 encoded response audio bytes.

long sequenceNumber

A sequence number for this chunk of the stream response.

JsonValue; type "response.audio.delta"constant"response.audio.delta"constant

The type of the event. Always `response.audio.delta`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseAudioDoneEvent:

Emitted when the audio response is complete.

long sequenceNumber

The sequence number of the delta.

JsonValue; type "response.audio.done"constant"response.audio.done"constant

The type of the event. Always `response.audio.done`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseAudioTranscriptDeltaEvent:

Emitted when there is a partial transcript of audio.

String delta

The partial transcript of the audio response.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.audio.transcript.delta"constant"response.audio.transcript.delta"constant

The type of the event. Always `response.audio.transcript.delta`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseAudioTranscriptDoneEvent:

Emitted when the full audio transcript is completed.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.audio.transcript.done"constant"response.audio.transcript.done"constant

The type of the event. Always `response.audio.transcript.done`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseCodeInterpreterCallCodeDeltaEvent:

Emitted when a partial code snippet is streamed by the code interpreter.

String delta

The partial code snippet being streamed by the code interpreter.

String itemId

The unique identifier of the code interpreter tool call item.

long outputIndex

The index of the output item in the response for which the code is being streamed.

long sequenceNumber

The sequence number of this event, used to order streaming events.

JsonValue; type "response.code\_interpreter\_call\_code.delta"constant"response.code\_interpreter\_call\_code.delta"constant

The type of the event. Always `response.code_interpreter_call_code.delta`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseCodeInterpreterCallCodeDoneEvent:

Emitted when the code snippet is finalized by the code interpreter.

String code

The final code snippet output by the code interpreter.

String itemId

The unique identifier of the code interpreter tool call item.

long outputIndex

The index of the output item in the response for which the code is finalized.

long sequenceNumber

The sequence number of this event, used to order streaming events.

JsonValue; type "response.code\_interpreter\_call\_code.done"constant"response.code\_interpreter\_call\_code.done"constant

The type of the event. Always `response.code_interpreter_call_code.done`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseCodeInterpreterCallCompletedEvent:

Emitted when the code interpreter call is completed.

String itemId

The unique identifier of the code interpreter tool call item.

long outputIndex

The index of the output item in the response for which the code interpreter call is completed.

long sequenceNumber

The sequence number of this event, used to order streaming events.

JsonValue; type "response.code\_interpreter\_call.completed"constant"response.code\_interpreter\_call.completed"constant

The type of the event. Always `response.code_interpreter_call.completed`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseCodeInterpreterCallInProgressEvent:

Emitted when a code interpreter call is in progress.

String itemId

The unique identifier of the code interpreter tool call item.

long outputIndex

The index of the output item in the response for which the code interpreter call is in progress.

long sequenceNumber

The sequence number of this event, used to order streaming events.

JsonValue; type "response.code\_interpreter\_call.in\_progress"constant"response.code\_interpreter\_call.in\_progress"constant

The type of the event. Always `response.code_interpreter_call.in_progress`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseCodeInterpreterCallInterpretingEvent:

Emitted when the code interpreter is actively interpreting the code snippet.

String itemId

The unique identifier of the code interpreter tool call item.

long outputIndex

The index of the output item in the response for which the code interpreter is interpreting code.

long sequenceNumber

The sequence number of this event, used to order streaming events.

JsonValue; type "response.code\_interpreter\_call.interpreting"constant"response.code\_interpreter\_call.interpreting"constant

The type of the event. Always `response.code_interpreter_call.interpreting`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseCompletedEvent:

Emitted when the model response is complete.

[BetaResponse](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema)) response

Properties of the completed response.

long sequenceNumber

The sequence number for this event.

JsonValue; type "response.completed"constant"response.completed"constant

The type of the event. Always `response.completed`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseContentPartAddedEvent:

Emitted when a new content part is added.

long contentIndex

The index of the content part that was added.

String itemId

The ID of the output item that the content part was added to.

long outputIndex

The index of the output item that the content part was added to.

Part part

The content part that was added.

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

class ReasoningText:

String text

JsonValue; type "reasoning\_text"constant"reasoning\_text"constant

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.content\_part.added"constant"response.content\_part.added"constant

The type of the event. Always `response.content_part.added`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseContentPartDoneEvent:

Emitted when a content part is done.

long contentIndex

The index of the content part that is done.

String itemId

The ID of the output item that the content part was added to.

long outputIndex

The index of the output item that the content part was added to.

Part part

The content part that is done.

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

class ReasoningText:

String text

JsonValue; type "reasoning\_text"constant"reasoning\_text"constant

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.content\_part.done"constant"response.content\_part.done"constant

The type of the event. Always `response.content_part.done`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseCreatedEvent:

An event that is emitted when a response is created.

[BetaResponse](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema)) response

The response that was created.

long sequenceNumber

The sequence number for this event.

JsonValue; type "response.created"constant"response.created"constant

The type of the event. Always `response.created`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseErrorEvent:

Emitted when an error occurs.

Optional<String> code

The error code.

String message

The error message.

Optional<String> param

The error parameter.

long sequenceNumber

The sequence number of this event.

JsonValue; type "error"constant"error"constant

The type of the event. Always `error`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseFileSearchCallCompletedEvent:

Emitted when a file search call is completed (results found).

String itemId

The ID of the output item that the file search call is initiated.

long outputIndex

The index of the output item that the file search call is initiated.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.file\_search\_call.completed"constant"response.file\_search\_call.completed"constant

The type of the event. Always `response.file_search_call.completed`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseFileSearchCallInProgressEvent:

Emitted when a file search call is initiated.

String itemId

The ID of the output item that the file search call is initiated.

long outputIndex

The index of the output item that the file search call is initiated.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.file\_search\_call.in\_progress"constant"response.file\_search\_call.in\_progress"constant

The type of the event. Always `response.file_search_call.in_progress`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseFileSearchCallSearchingEvent:

Emitted when a file search is currently searching.

String itemId

The ID of the output item that the file search call is initiated.

long outputIndex

The index of the output item that the file search call is searching.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.file\_search\_call.searching"constant"response.file\_search\_call.searching"constant

The type of the event. Always `response.file_search_call.searching`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseFunctionCallArgumentsDeltaEvent:

Emitted when there is a partial function-call arguments delta.

String delta

The function-call arguments delta that is added.

String itemId

The ID of the output item that the function-call arguments delta is added to.

long outputIndex

The index of the output item that the function-call arguments delta is added to.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.function\_call\_arguments.delta"constant"response.function\_call\_arguments.delta"constant

The type of the event. Always `response.function_call_arguments.delta`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseFunctionCallArgumentsDoneEvent:

Emitted when function-call arguments are finalized.

String arguments

The function-call arguments.

String itemId

The ID of the item.

String name

The name of the function that was called.

long outputIndex

The index of the output item.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.function\_call\_arguments.done"constant"response.function\_call\_arguments.done"constant

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseInProgressEvent:

Emitted when the response is in progress.

[BetaResponse](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema)) response

The response that is in progress.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.in\_progress"constant"response.in\_progress"constant

The type of the event. Always `response.in_progress`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseFailedEvent:

An event that is emitted when a response fails.

[BetaResponse](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema)) response

The response that failed.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.failed"constant"response.failed"constant

The type of the event. Always `response.failed`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseIncompleteEvent:

An event that is emitted when a response finishes as incomplete.

[BetaResponse](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema)) response

The response that was incomplete.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.incomplete"constant"response.incomplete"constant

The type of the event. Always `response.incomplete`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseOutputItemAddedEvent:

Emitted when a new output item is added.

[BetaResponseOutputItem](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_item%20%3E%20(schema)) item

The output item that was added.

long outputIndex

The index of the output item that was added.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.output\_item.added"constant"response.output\_item.added"constant

The type of the event. Always `response.output_item.added`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseOutputItemDoneEvent:

Emitted when an output item is marked done.

[BetaResponseOutputItem](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_item%20%3E%20(schema)) item

The output item that was marked done.

long outputIndex

The index of the output item that was marked done.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.output\_item.done"constant"response.output\_item.done"constant

The type of the event. Always `response.output_item.done`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseReasoningSummaryPartAddedEvent:

Emitted when a new reasoning summary part is added.

String itemId

The ID of the item this summary part is associated with.

long outputIndex

The index of the output item this summary part is associated with.

Part part

The summary part that was added.

String text

The text of the summary part.

JsonValue; type "summary\_text"constant"summary\_text"constant

The type of the summary part. Always `summary_text`.

long sequenceNumber

The sequence number of this event.

long summaryIndex

The index of the summary part within the reasoning summary.

JsonValue; type "response.reasoning\_summary\_part.added"constant"response.reasoning\_summary\_part.added"constant

The type of the event. Always `response.reasoning_summary_part.added`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseReasoningSummaryPartDoneEvent:

Emitted when a reasoning summary part is completed.

String itemId

The ID of the item this summary part is associated with.

long outputIndex

The index of the output item this summary part is associated with.

Part part

The completed summary part.

String text

The text of the summary part.

JsonValue; type "summary\_text"constant"summary\_text"constant

The type of the summary part. Always `summary_text`.

long sequenceNumber

The sequence number of this event.

long summaryIndex

The index of the summary part within the reasoning summary.

JsonValue; type "response.reasoning\_summary\_part.done"constant"response.reasoning\_summary\_part.done"constant

The type of the event. Always `response.reasoning_summary_part.done`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

Optional<Status> status

The completion status of the summary part. Omitted when the part completed
normally and set to `incomplete` when generation was interrupted.

class BetaResponseReasoningSummaryTextDeltaEvent:

Emitted when a delta is added to a reasoning summary text.

String delta

The text delta that was added to the summary.

String itemId

The ID of the item this summary text delta is associated with.

long outputIndex

The index of the output item this summary text delta is associated with.

long sequenceNumber

The sequence number of this event.

long summaryIndex

The index of the summary part within the reasoning summary.

JsonValue; type "response.reasoning\_summary\_text.delta"constant"response.reasoning\_summary\_text.delta"constant

The type of the event. Always `response.reasoning_summary_text.delta`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseReasoningSummaryTextDoneEvent:

Emitted when a reasoning summary text is completed.

String itemId

The ID of the item this summary text is associated with.

long outputIndex

The index of the output item this summary text is associated with.

long sequenceNumber

The sequence number of this event.

long summaryIndex

The index of the summary part within the reasoning summary.

String text

The full text of the completed reasoning summary.

JsonValue; type "response.reasoning\_summary\_text.done"constant"response.reasoning\_summary\_text.done"constant

The type of the event. Always `response.reasoning_summary_text.done`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseReasoningTextDeltaEvent:

Emitted when a delta is added to a reasoning text.

long contentIndex

The index of the reasoning content part this delta is associated with.

String delta

The text delta that was added to the reasoning content.

String itemId

The ID of the item this reasoning text delta is associated with.

long outputIndex

The index of the output item this reasoning text delta is associated with.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.reasoning\_text.delta"constant"response.reasoning\_text.delta"constant

The type of the event. Always `response.reasoning_text.delta`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseReasoningTextDoneEvent:

Emitted when a reasoning text is completed.

long contentIndex

The index of the reasoning content part.

String itemId

The ID of the item this reasoning text is associated with.

long outputIndex

The index of the output item this reasoning text is associated with.

long sequenceNumber

The sequence number of this event.

String text

The full text of the completed reasoning content.

JsonValue; type "response.reasoning\_text.done"constant"response.reasoning\_text.done"constant

The type of the event. Always `response.reasoning_text.done`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseRefusalDeltaEvent:

Emitted when there is a partial refusal text.

long contentIndex

The index of the content part that the refusal text is added to.

String delta

The refusal text that is added.

String itemId

The ID of the output item that the refusal text is added to.

long outputIndex

The index of the output item that the refusal text is added to.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.refusal.delta"constant"response.refusal.delta"constant

The type of the event. Always `response.refusal.delta`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseRefusalDoneEvent:

Emitted when refusal text is finalized.

long contentIndex

The index of the content part that the refusal text is finalized.

String itemId

The ID of the output item that the refusal text is finalized.

long outputIndex

The index of the output item that the refusal text is finalized.

String refusal

The refusal text that is finalized.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.refusal.done"constant"response.refusal.done"constant

The type of the event. Always `response.refusal.done`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseTextDeltaEvent:

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

class BetaResponseTextConfig:

Configuration options for a text response from the model. Can be plain
text or structured JSON data. Learn more:

* [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
* [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

Optional<[BetaResponseFormatTextConfig](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_format_text_config%20%3E%20(schema))> format

An object specifying the format that the model must output.

Configuring `{ "type": "json_schema" }` enables Structured Outputs,
which ensures the model will match your supplied JSON schema. Learn more in the
[Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

The default format is `{ "type": "text" }` with no additional options.

**Not recommended for gpt-4o and newer models:**

Setting to `{ "type": "json_object" }` enables the older JSON mode, which
ensures the message the model generates is valid JSON. Using `json_schema`
is preferred for models that support it.

Optional<Verbosity> verbosity

Constrains the verbosity of the model’s response. Lower values will result in
more concise responses, while higher values will result in more verbose responses.
Currently supported values are `low`, `medium`, and `high`.

LOW("low")

MEDIUM("medium")

HIGH("high")

class BetaResponseTextDeltaEvent:

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

class BetaResponseUsage:

Represents token usage details including input tokens, output tokens,
a breakdown of output tokens, and the total tokens used.

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

class BetaResponsesClientEvent: A class that can be one of several variants.union

Client events accepted by the Responses WebSocket server.

ResponseCreate

JsonValue; type "response.create"constant"response.create"constant

The type of the client event. Always `response.create`.

Optional<Boolean> background

Whether to run the model response in the background.
[Learn more](https://platform.openai.com/docs/guides/background).

Optional<List<ContextManagement>> contextManagement

Context management configuration for this request.

String type

The context management entry type. Currently only ‘compaction’ is supported.

Optional<Long> compactThreshold

Token threshold at which compaction should be triggered for this entry.

minimum1000

Optional<Conversation> conversation

The conversation that this response belongs to. Items from this conversation are prepended to `input_items` for this response request.
Input items and output items from this response are automatically added to this conversation after this response completes.

String

class BetaResponseConversationParam:

The conversation that this response belongs to.

String id

The unique ID of the conversation.

Optional<List<[BetaResponseIncludable](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_includable%20%3E%20(schema))>> include

Specify additional output data to include in the model response. Currently supported values are:

* `web_search_call.action.sources`: Include the sources of the web search tool call.
* `code_interpreter_call.outputs`: Includes the outputs of python code execution in code interpreter tool call items.
* `computer_call_output.output.image_url`: Include image urls from the computer call output.
* `file_search_call.results`: Include the search results of the file search tool call.
* `message.input_image.image_url`: Include image urls from the input message.
* `message.output_text.logprobs`: Include logprobs with assistant messages.
* `reasoning.encrypted_content`: Includes an encrypted version of reasoning tokens in reasoning item outputs. This enables reasoning items to be used in multi-turn conversations when using the Responses API statelessly (like when the `store` parameter is set to `false`, or when an organization is enrolled in the zero data retention program).

FILE\_SEARCH\_CALL\_RESULTS("file\_search\_call.results")

WEB\_SEARCH\_CALL\_RESULTS("web\_search\_call.results")

WEB\_SEARCH\_CALL\_ACTION\_SOURCES("web\_search\_call.action.sources")

MESSAGE\_INPUT\_IMAGE\_IMAGE\_URL("message.input\_image.image\_url")

COMPUTER\_CALL\_OUTPUT\_OUTPUT\_IMAGE\_URL("computer\_call\_output.output.image\_url")

CODE\_INTERPRETER\_CALL\_OUTPUTS("code\_interpreter\_call.outputs")

REASONING\_ENCRYPTED\_CONTENT("reasoning.encrypted\_content")

MESSAGE\_OUTPUT\_TEXT\_LOGPROBS("message.output\_text.logprobs")

Optional<Input> input

Text, image, or file inputs to the model, used to generate a response.

Learn more:

* [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
* [Image inputs](https://platform.openai.com/docs/guides/images)
* [File inputs](https://platform.openai.com/docs/guides/pdf-files)
* [Conversation state](https://platform.openai.com/docs/guides/conversation-state)
* [Function calling](https://platform.openai.com/docs/guides/function-calling)

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

Optional<String> instructions

A system (or developer) message inserted into the model’s context.

When using along with `previous_response_id`, the instructions from a previous
response will not be carried over to the next response. This makes it simple
to swap out system (or developer) messages in new responses.

Optional<Long> maxOutputTokens

An upper bound for the number of tokens that can be generated for a response, including visible output tokens and [reasoning tokens](https://platform.openai.com/docs/guides/reasoning).

minimum16

Optional<Long> maxToolCalls

The maximum number of total calls to built-in tools that can be processed in a response. This maximum number applies across all built-in tool calls, not per individual tool. Any further attempts to call a tool by the model will be ignored.

Optional<Metadata> metadata

format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

Optional<Model> model

Model ID used to generate the response, like `gpt-4o` or `o3`. OpenAI
offers a wide range of models with different capabilities, performance
characteristics, and price points. Refer to the [model guide](https://platform.openai.com/docs/models)
to browse and compare available models.

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

Optional<Moderation> moderation

Configuration for running moderation on the input and output of this response.

String model

The moderation model to use for moderated completions, e.g. ‘omni-moderation-latest’.

Optional<Policy> policy

The policy to apply to moderated response input and output.

Optional<Input> input

The moderation policy for the response input.

Mode mode

SCORE("score")

BLOCK("block")

Optional<Output> output

The moderation policy for the response output.

Mode mode

SCORE("score")

BLOCK("block")

Optional<MultiAgent> multiAgent

Configuration for server-hosted multi-agent execution.

boolean enabled

Whether to enable server-hosted multi-agent execution for this response.

Optional<Long> maxConcurrentSubagents

`max_concurrent_subagents` sets the maximum number of subagents that can be active simultaneously across the entire agent tree. It includes all descendants—children, grandchildren, and deeper subagents—but excludes the root agent.
The API does not impose a fixed upper bound on this setting. The default is `3`, which is recommended for most workloads. Multi-agent runs also have no fixed limit on tree depth or the total number of subagents created during a run.

minimum1

Optional<Boolean> parallelToolCalls

Whether to allow the model to run tool calls in parallel.

Optional<String> previousResponseId

The unique ID of the previous response to the model. Use this to
create multi-turn conversations. Learn more about
[conversation state](https://platform.openai.com/docs/guides/conversation-state). Cannot be used in conjunction with `conversation`.

Optional<[BetaResponsePrompt](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_prompt%20%3E%20(schema))> prompt

Reference to a prompt template and its variables.
[Learn more](https://platform.openai.com/docs/guides/text?api-mode=responses#reusable-prompts).

Optional<String> promptCacheKey

Used by OpenAI to cache responses for similar requests to optimize your cache hit rates. Replaces the `user` field. [Learn more](https://platform.openai.com/docs/guides/prompt-caching).

Optional<PromptCacheOptions> promptCacheOptions

Options for prompt caching. Supported for `gpt-5.6` and later models. By default, OpenAI automatically chooses one implicit cache breakpoint. You can add explicit breakpoints to content blocks with `prompt_cache_breakpoint`. Each request can write up to four breakpoints. For cache matching, OpenAI considers up to the latest 80 breakpoints in the conversation, without a content-block lookback limit. Set `mode` to `explicit` to disable the implicit breakpoint. The `ttl` defaults to `30m`, which is currently the only supported value. See the [prompt caching guide](https://platform.openai.com/docs/guides/prompt-caching) for current details.

Optional<Mode> mode

Controls whether OpenAI automatically creates an implicit cache breakpoint. Defaults to `implicit`. With `implicit`, OpenAI creates one implicit breakpoint and writes up to the latest three explicit breakpoints in the request. With `explicit`, OpenAI does not create an implicit breakpoint and writes up to the latest four explicit breakpoints. If there are no explicit breakpoints, the request does not use prompt caching.

IMPLICIT("implicit")

EXPLICIT("explicit")

Optional<Ttl> ttl

The minimum lifetime applied to every implicit and explicit cache breakpoint written by the request. Defaults to `30m`, which is currently the only supported value. The backend may retain cache entries for longer.

DeprecatedOptional<PromptCacheRetention> promptCacheRetention

Deprecated. Use `prompt_cache_options.ttl` instead.

The retention policy for the prompt cache. Set to `24h` to enable extended prompt caching, which keeps cached prefixes active for longer, up to a maximum of 24 hours. [Learn more](https://platform.openai.com/docs/guides/prompt-caching#prompt-cache-retention).
This field expresses a maximum retention policy, while
`prompt_cache_options.ttl` expresses a minimum cache lifetime. The two
fields are independent and do not interact.
For `gpt-5.5`, `gpt-5.5-pro`, and future models, only `24h` is supported.

For older models that support both `in_memory` and `24h`, the default depends on your organization’s data retention policy:

* Organizations without ZDR enabled default to `24h`.
* Organizations with ZDR enabled default to `in_memory` when `prompt_cache_retention` is not specified.

IN\_MEMORY("in\_memory")

\_24H("24h")

Optional<Reasoning> reasoning

**gpt-5 and o-series models only**

Configuration options for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).

Optional<Context> context

Controls which reasoning items are rendered back to the model on later turns.
When returned on a response, this is the effective reasoning context mode
used for the response.

AUTO("auto")

CURRENT\_TURN("current\_turn")

ALL\_TURNS("all\_turns")

Optional<Effort> effort

Constrains effort on reasoning for reasoning models. Currently supported
values are `none`, `minimal`, `low`, `medium`, `high`, `xhigh`, and `max`.
Reducing reasoning effort can result in faster responses and fewer tokens
used on reasoning in a response. Not all reasoning models support every
value. See the
[reasoning guide](https://platform.openai.com/docs/guides/reasoning)
for model-specific support.

NONE("none")

MINIMAL("minimal")

LOW("low")

MEDIUM("medium")

HIGH("high")

XHIGH("xhigh")

MAX("max")

DeprecatedOptional<GenerateSummary> generateSummary

**Deprecated:** use `summary` instead.

A summary of the reasoning performed by the model. This can be
useful for debugging and understanding the model’s reasoning process.
One of `auto`, `concise`, or `detailed`.

AUTO("auto")

CONCISE("concise")

DETAILED("detailed")

Optional<Mode> mode

Controls the reasoning execution mode for the request.

When returned on a response, this is the effective execution mode.

STANDARD("standard")

PRO("pro")

Optional<Summary> summary

A summary of the reasoning performed by the model. This can be
useful for debugging and understanding the model’s reasoning process.
One of `auto`, `concise`, or `detailed`.

`concise` is supported for `computer-use-preview` models and all reasoning models after `gpt-5`.

AUTO("auto")

CONCISE("concise")

DETAILED("detailed")

Optional<String> safetyIdentifier

A stable identifier used to help detect users of your application that may be violating OpenAI’s usage policies.
The IDs should be a string that uniquely identifies each user, with a maximum length of 64 characters. We recommend hashing their username or email address, in order to avoid sending us any identifying information. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).

maxLength64

Optional<ServiceTier> serviceTier

Specifies the processing type used for serving the request.

* If set to ‘auto’, then the request will be processed with the service tier configured in the Project settings. Unless otherwise configured, the Project will use ‘default’.
* If set to ‘default’, then the request will be processed with the standard pricing and performance for the selected model.
* If set to ‘[flex](https://platform.openai.com/docs/guides/flex-processing)’ or ‘[priority](https://openai.com/api-priority-processing/)’, then the request will be processed with the corresponding service tier.
* When not set, the default behavior is ‘auto’.

When the `service_tier` parameter is set, the response body will include the `service_tier` value based on the processing mode actually used to serve the request. This response value may be different from the value set in the parameter.

AUTO("auto")

DEFAULT("default")

FLEX("flex")

SCALE("scale")

PRIORITY("priority")

Optional<Boolean> store

Whether to store the generated model response for later retrieval via
API.

Optional<Boolean> stream

If set to true, the model response data will be streamed to the client
as it is generated using [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format).
See the [Streaming section below](https://platform.openai.com/docs/api-reference/responses-streaming)
for more information.

Optional<StreamOptions> streamOptions

Options for streaming responses. Only set this when you set `stream: true`.

Optional<Boolean> includeObfuscation

When true, stream obfuscation will be enabled. Stream obfuscation adds
random characters to an `obfuscation` field on streaming delta events to
normalize payload sizes as a mitigation to certain side-channel attacks.
These obfuscation fields are included by default, but add a small amount
of overhead to the data stream. You can set `include_obfuscation` to
false to optimize for bandwidth if you trust the network links between
your application and the OpenAI API.

Optional<Double> temperature

What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.
We generally recommend altering this or `top_p` but not both.

minimum0

maximum2

Optional<[BetaResponseTextConfig](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_text_config%20%3E%20(schema))> text

Configuration options for a text response from the model. Can be plain
text or structured JSON data. Learn more:

* [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
* [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

Optional<ToolChoice> toolChoice

How the model should select which tool (or tools) to use when generating
a response. See the `tools` parameter to see how to specify which tools
the model can call.

enum BetaToolChoiceOptions:

Controls which (if any) tool is called by the model.

`none` means the model will not call any tool and instead generates a message.

`auto` means the model can pick between generating a message or calling one or
more tools.

`required` means the model must call one or more tools.

NONE("none")

AUTO("auto")

REQUIRED("required")

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

class BetaToolChoiceCustom:

Use this option to force the model to call a specific custom tool.

String name

The name of the custom tool to call.

JsonValue; type "custom"constant"custom"constant

For custom tool calling, the type is always `custom`.

JsonValue;

JsonValue; type "programmatic\_tool\_calling"constant"programmatic\_tool\_calling"constant

The tool to call. Always `programmatic_tool_calling`.

class BetaToolChoiceApplyPatch:

Forces the model to call the apply\_patch tool when executing a tool call.

JsonValue; type "apply\_patch"constant"apply\_patch"constant

The tool to call. Always `apply_patch`.

class BetaToolChoiceShell:

Forces the model to call the shell tool when a tool call is required.

JsonValue; type "shell"constant"shell"constant

The tool to call. Always `shell`.

Optional<List<[BetaTool](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))>> tools

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

Optional<Long> topLogprobs

An integer between 0 and 20 specifying the maximum number of most likely
tokens to return at each token position, each with an associated log
probability. In some cases, the number of returned tokens may be fewer than
requested.

minimum0

maximum20

Optional<Double> topP

An alternative to sampling with temperature, called nucleus sampling,
where the model considers the results of the tokens with top\_p probability
mass. So 0.1 means only the tokens comprising the top 10% probability mass
are considered.

We generally recommend altering this or `temperature` but not both.

minimum0

maximum1

DeprecatedOptional<Truncation> truncation

The truncation strategy to use for the model response.

* `auto`: If the input to this Response exceeds
  the model’s context window size, the model will truncate the
  response to fit the context window by dropping items from the beginning of the conversation.
* `disabled` (default): If the input size will exceed the context window
  size for a model, the request will fail with a 400 error.

AUTO("auto")

DISABLED("disabled")

DeprecatedOptional<String> user

This field is being replaced by `safety_identifier` and `prompt_cache_key`. Use `prompt_cache_key` instead to maintain caching optimizations.
A stable identifier for your end-users.
Used to boost cache hit rates by better bucketing similar requests and to help OpenAI detect and prevent abuse. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).

class BetaResponseInjectEvent:

Injects input items into an active response over a WebSocket connection.
The items are validated and committed atomically. Currently, the server
accepts client-owned tool outputs that resume a waiting agent.

List<[BetaResponseInputItem](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_item%20%3E%20(schema))> input

Input items to inject into the active response.

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

The ID of the active response that should receive the input.

JsonValue; type "response.inject"constant"response.inject"constant

The event discriminator. Always `response.inject`.

class BetaResponsesServerEvent: A class that can be one of several variants.union

Server events emitted by the Responses WebSocket server.

class BetaResponseAudioDeltaEvent:

Emitted when there is a partial audio response.

String delta

A chunk of Base64 encoded response audio bytes.

long sequenceNumber

A sequence number for this chunk of the stream response.

JsonValue; type "response.audio.delta"constant"response.audio.delta"constant

The type of the event. Always `response.audio.delta`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseAudioDoneEvent:

Emitted when the audio response is complete.

long sequenceNumber

The sequence number of the delta.

JsonValue; type "response.audio.done"constant"response.audio.done"constant

The type of the event. Always `response.audio.done`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseAudioTranscriptDeltaEvent:

Emitted when there is a partial transcript of audio.

String delta

The partial transcript of the audio response.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.audio.transcript.delta"constant"response.audio.transcript.delta"constant

The type of the event. Always `response.audio.transcript.delta`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseAudioTranscriptDoneEvent:

Emitted when the full audio transcript is completed.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.audio.transcript.done"constant"response.audio.transcript.done"constant

The type of the event. Always `response.audio.transcript.done`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseCodeInterpreterCallCodeDeltaEvent:

Emitted when a partial code snippet is streamed by the code interpreter.

String delta

The partial code snippet being streamed by the code interpreter.

String itemId

The unique identifier of the code interpreter tool call item.

long outputIndex

The index of the output item in the response for which the code is being streamed.

long sequenceNumber

The sequence number of this event, used to order streaming events.

JsonValue; type "response.code\_interpreter\_call\_code.delta"constant"response.code\_interpreter\_call\_code.delta"constant

The type of the event. Always `response.code_interpreter_call_code.delta`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseCodeInterpreterCallCodeDoneEvent:

Emitted when the code snippet is finalized by the code interpreter.

String code

The final code snippet output by the code interpreter.

String itemId

The unique identifier of the code interpreter tool call item.

long outputIndex

The index of the output item in the response for which the code is finalized.

long sequenceNumber

The sequence number of this event, used to order streaming events.

JsonValue; type "response.code\_interpreter\_call\_code.done"constant"response.code\_interpreter\_call\_code.done"constant

The type of the event. Always `response.code_interpreter_call_code.done`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseCodeInterpreterCallCompletedEvent:

Emitted when the code interpreter call is completed.

String itemId

The unique identifier of the code interpreter tool call item.

long outputIndex

The index of the output item in the response for which the code interpreter call is completed.

long sequenceNumber

The sequence number of this event, used to order streaming events.

JsonValue; type "response.code\_interpreter\_call.completed"constant"response.code\_interpreter\_call.completed"constant

The type of the event. Always `response.code_interpreter_call.completed`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseCodeInterpreterCallInProgressEvent:

Emitted when a code interpreter call is in progress.

String itemId

The unique identifier of the code interpreter tool call item.

long outputIndex

The index of the output item in the response for which the code interpreter call is in progress.

long sequenceNumber

The sequence number of this event, used to order streaming events.

JsonValue; type "response.code\_interpreter\_call.in\_progress"constant"response.code\_interpreter\_call.in\_progress"constant

The type of the event. Always `response.code_interpreter_call.in_progress`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseCodeInterpreterCallInterpretingEvent:

Emitted when the code interpreter is actively interpreting the code snippet.

String itemId

The unique identifier of the code interpreter tool call item.

long outputIndex

The index of the output item in the response for which the code interpreter is interpreting code.

long sequenceNumber

The sequence number of this event, used to order streaming events.

JsonValue; type "response.code\_interpreter\_call.interpreting"constant"response.code\_interpreter\_call.interpreting"constant

The type of the event. Always `response.code_interpreter_call.interpreting`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseCompletedEvent:

Emitted when the model response is complete.

[BetaResponse](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema)) response

Properties of the completed response.

long sequenceNumber

The sequence number for this event.

JsonValue; type "response.completed"constant"response.completed"constant

The type of the event. Always `response.completed`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseContentPartAddedEvent:

Emitted when a new content part is added.

long contentIndex

The index of the content part that was added.

String itemId

The ID of the output item that the content part was added to.

long outputIndex

The index of the output item that the content part was added to.

Part part

The content part that was added.

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

class ReasoningText:

String text

JsonValue; type "reasoning\_text"constant"reasoning\_text"constant

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.content\_part.added"constant"response.content\_part.added"constant

The type of the event. Always `response.content_part.added`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseContentPartDoneEvent:

Emitted when a content part is done.

long contentIndex

The index of the content part that is done.

String itemId

The ID of the output item that the content part was added to.

long outputIndex

The index of the output item that the content part was added to.

Part part

The content part that is done.

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

class ReasoningText:

String text

JsonValue; type "reasoning\_text"constant"reasoning\_text"constant

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.content\_part.done"constant"response.content\_part.done"constant

The type of the event. Always `response.content_part.done`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseCreatedEvent:

An event that is emitted when a response is created.

[BetaResponse](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema)) response

The response that was created.

long sequenceNumber

The sequence number for this event.

JsonValue; type "response.created"constant"response.created"constant

The type of the event. Always `response.created`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseErrorEvent:

Emitted when an error occurs.

Optional<String> code

The error code.

String message

The error message.

Optional<String> param

The error parameter.

long sequenceNumber

The sequence number of this event.

JsonValue; type "error"constant"error"constant

The type of the event. Always `error`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseFileSearchCallCompletedEvent:

Emitted when a file search call is completed (results found).

String itemId

The ID of the output item that the file search call is initiated.

long outputIndex

The index of the output item that the file search call is initiated.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.file\_search\_call.completed"constant"response.file\_search\_call.completed"constant

The type of the event. Always `response.file_search_call.completed`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseFileSearchCallInProgressEvent:

Emitted when a file search call is initiated.

String itemId

The ID of the output item that the file search call is initiated.

long outputIndex

The index of the output item that the file search call is initiated.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.file\_search\_call.in\_progress"constant"response.file\_search\_call.in\_progress"constant

The type of the event. Always `response.file_search_call.in_progress`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseFileSearchCallSearchingEvent:

Emitted when a file search is currently searching.

String itemId

The ID of the output item that the file search call is initiated.

long outputIndex

The index of the output item that the file search call is searching.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.file\_search\_call.searching"constant"response.file\_search\_call.searching"constant

The type of the event. Always `response.file_search_call.searching`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseFunctionCallArgumentsDeltaEvent:

Emitted when there is a partial function-call arguments delta.

String delta

The function-call arguments delta that is added.

String itemId

The ID of the output item that the function-call arguments delta is added to.

long outputIndex

The index of the output item that the function-call arguments delta is added to.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.function\_call\_arguments.delta"constant"response.function\_call\_arguments.delta"constant

The type of the event. Always `response.function_call_arguments.delta`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseFunctionCallArgumentsDoneEvent:

Emitted when function-call arguments are finalized.

String arguments

The function-call arguments.

String itemId

The ID of the item.

String name

The name of the function that was called.

long outputIndex

The index of the output item.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.function\_call\_arguments.done"constant"response.function\_call\_arguments.done"constant

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseInProgressEvent:

Emitted when the response is in progress.

[BetaResponse](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema)) response

The response that is in progress.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.in\_progress"constant"response.in\_progress"constant

The type of the event. Always `response.in_progress`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseFailedEvent:

An event that is emitted when a response fails.

[BetaResponse](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema)) response

The response that failed.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.failed"constant"response.failed"constant

The type of the event. Always `response.failed`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseIncompleteEvent:

An event that is emitted when a response finishes as incomplete.

[BetaResponse](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema)) response

The response that was incomplete.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.incomplete"constant"response.incomplete"constant

The type of the event. Always `response.incomplete`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseOutputItemAddedEvent:

Emitted when a new output item is added.

[BetaResponseOutputItem](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_item%20%3E%20(schema)) item

The output item that was added.

long outputIndex

The index of the output item that was added.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.output\_item.added"constant"response.output\_item.added"constant

The type of the event. Always `response.output_item.added`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseOutputItemDoneEvent:

Emitted when an output item is marked done.

[BetaResponseOutputItem](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_item%20%3E%20(schema)) item

The output item that was marked done.

long outputIndex

The index of the output item that was marked done.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.output\_item.done"constant"response.output\_item.done"constant

The type of the event. Always `response.output_item.done`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseReasoningSummaryPartAddedEvent:

Emitted when a new reasoning summary part is added.

String itemId

The ID of the item this summary part is associated with.

long outputIndex

The index of the output item this summary part is associated with.

Part part

The summary part that was added.

String text

The text of the summary part.

JsonValue; type "summary\_text"constant"summary\_text"constant

The type of the summary part. Always `summary_text`.

long sequenceNumber

The sequence number of this event.

long summaryIndex

The index of the summary part within the reasoning summary.

JsonValue; type "response.reasoning\_summary\_part.added"constant"response.reasoning\_summary\_part.added"constant

The type of the event. Always `response.reasoning_summary_part.added`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseReasoningSummaryPartDoneEvent:

Emitted when a reasoning summary part is completed.

String itemId

The ID of the item this summary part is associated with.

long outputIndex

The index of the output item this summary part is associated with.

Part part

The completed summary part.

String text

The text of the summary part.

JsonValue; type "summary\_text"constant"summary\_text"constant

The type of the summary part. Always `summary_text`.

long sequenceNumber

The sequence number of this event.

long summaryIndex

The index of the summary part within the reasoning summary.

JsonValue; type "response.reasoning\_summary\_part.done"constant"response.reasoning\_summary\_part.done"constant

The type of the event. Always `response.reasoning_summary_part.done`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

Optional<Status> status

The completion status of the summary part. Omitted when the part completed
normally and set to `incomplete` when generation was interrupted.

class BetaResponseReasoningSummaryTextDeltaEvent:

Emitted when a delta is added to a reasoning summary text.

String delta

The text delta that was added to the summary.

String itemId

The ID of the item this summary text delta is associated with.

long outputIndex

The index of the output item this summary text delta is associated with.

long sequenceNumber

The sequence number of this event.

long summaryIndex

The index of the summary part within the reasoning summary.

JsonValue; type "response.reasoning\_summary\_text.delta"constant"response.reasoning\_summary\_text.delta"constant

The type of the event. Always `response.reasoning_summary_text.delta`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseReasoningSummaryTextDoneEvent:

Emitted when a reasoning summary text is completed.

String itemId

The ID of the item this summary text is associated with.

long outputIndex

The index of the output item this summary text is associated with.

long sequenceNumber

The sequence number of this event.

long summaryIndex

The index of the summary part within the reasoning summary.

String text

The full text of the completed reasoning summary.

JsonValue; type "response.reasoning\_summary\_text.done"constant"response.reasoning\_summary\_text.done"constant

The type of the event. Always `response.reasoning_summary_text.done`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseReasoningTextDeltaEvent:

Emitted when a delta is added to a reasoning text.

long contentIndex

The index of the reasoning content part this delta is associated with.

String delta

The text delta that was added to the reasoning content.

String itemId

The ID of the item this reasoning text delta is associated with.

long outputIndex

The index of the output item this reasoning text delta is associated with.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.reasoning\_text.delta"constant"response.reasoning\_text.delta"constant

The type of the event. Always `response.reasoning_text.delta`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseReasoningTextDoneEvent:

Emitted when a reasoning text is completed.

long contentIndex

The index of the reasoning content part.

String itemId

The ID of the item this reasoning text is associated with.

long outputIndex

The index of the output item this reasoning text is associated with.

long sequenceNumber

The sequence number of this event.

String text

The full text of the completed reasoning content.

JsonValue; type "response.reasoning\_text.done"constant"response.reasoning\_text.done"constant

The type of the event. Always `response.reasoning_text.done`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseRefusalDeltaEvent:

Emitted when there is a partial refusal text.

long contentIndex

The index of the content part that the refusal text is added to.

String delta

The refusal text that is added.

String itemId

The ID of the output item that the refusal text is added to.

long outputIndex

The index of the output item that the refusal text is added to.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.refusal.delta"constant"response.refusal.delta"constant

The type of the event. Always `response.refusal.delta`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseRefusalDoneEvent:

Emitted when refusal text is finalized.

long contentIndex

The index of the content part that the refusal text is finalized.

String itemId

The ID of the output item that the refusal text is finalized.

long outputIndex

The index of the output item that the refusal text is finalized.

String refusal

The refusal text that is finalized.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.refusal.done"constant"response.refusal.done"constant

The type of the event. Always `response.refusal.done`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

class BetaResponseTextDeltaEvent:

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
