<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/responses/subresources/input_items/methods/list/ -->

[API Reference](/api/reference/go)

[Beta](/api/reference/go/resources/beta)

[Responses](/api/reference/go/resources/beta/subresources/responses)

[Input Items](/api/reference/go/resources/beta/subresources/responses/subresources/input_items)

# List input items

client.Beta.Responses.InputItems.List(ctx, responseID, params) (\*CursorPage[[BetaResponseItemUnion](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_item%20%3E%20(schema))], error)

GET/responses/{response\_id}/input\_items

Returns a list of input items for a given response.

##### ParametersExpand Collapse

responseID string

params BetaResponseInputItemListParams

After param.Field[string]Optional

Query param: An item ID to list items after, used in pagination.

Include param.Field[[][BetaResponseIncludable](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_includable%20%3E%20(schema))]Optional

Query param: Additional fields to include in the response. See the `include`
parameter for Response creation above for more information.

const BetaResponseIncludableFileSearchCallResults [BetaResponseIncludable](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_includable%20%3E%20(schema)) = "file\_search\_call.results"

const BetaResponseIncludableWebSearchCallResults [BetaResponseIncludable](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_includable%20%3E%20(schema)) = "web\_search\_call.results"

const BetaResponseIncludableWebSearchCallActionSources [BetaResponseIncludable](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_includable%20%3E%20(schema)) = "web\_search\_call.action.sources"

const BetaResponseIncludableMessageInputImageImageURL [BetaResponseIncludable](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_includable%20%3E%20(schema)) = "message.input\_image.image\_url"

const BetaResponseIncludableComputerCallOutputOutputImageURL [BetaResponseIncludable](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_includable%20%3E%20(schema)) = "computer\_call\_output.output.image\_url"

const BetaResponseIncludableCodeInterpreterCallOutputs [BetaResponseIncludable](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_includable%20%3E%20(schema)) = "code\_interpreter\_call.outputs"

const BetaResponseIncludableReasoningEncryptedContent [BetaResponseIncludable](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_includable%20%3E%20(schema)) = "reasoning.encrypted\_content"

const BetaResponseIncludableMessageOutputTextLogprobs [BetaResponseIncludable](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_includable%20%3E%20(schema)) = "message.output\_text.logprobs"

Limit param.Field[int64]Optional

Query param: A limit on the number of objects to be returned. Limit can range between
1 and 100, and the default is 20.

Order param.Field[[BetaResponseInputItemListParamsOrder](/api/reference/go/resources/beta/subresources/responses/subresources/input_items/methods/list#(resource)%20beta.responses.input_items%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))]Optional

Query param: The order to return the input items in. Default is `desc`.

* `asc`: Return the input items in ascending order.
* `desc`: Return the input items in descending order.

const BetaResponseInputItemListParamsOrderAsc [BetaResponseInputItemListParamsOrder](/api/reference/go/resources/beta/subresources/responses/subresources/input_items/methods/list#(resource)%20beta.responses.input_items%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)) = "asc"

const BetaResponseInputItemListParamsOrderDesc [BetaResponseInputItemListParamsOrder](/api/reference/go/resources/beta/subresources/responses/subresources/input_items/methods/list#(resource)%20beta.responses.input_items%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)) = "desc"

Betas param.Field[[]string]Optional

Header param: Optional beta features to enable for this request.

const BetaResponseInputItemListParamsOpenAIBetaResponsesMultiAgentV1 BetaResponseInputItemListParamsOpenAIBeta = "responses\_multi\_agent=v1"

##### ReturnsExpand Collapse

type BetaResponseItemUnion interface{…}

Content item used to generate a response.

type BetaResponseInputMessageItem struct{…}

ID string

The unique ID of the message input.

Content [BetaResponseInputMessageContentList](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_message_content_list%20%3E%20(schema))

type BetaResponseInputText struct{…}

Text string

Type InputText

PromptCacheBreakpoint BetaResponseInputTextPromptCacheBreakpointOptional

Mode Explicit

type BetaResponseInputImage struct{…}

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

Detail BetaResponseInputImageDetail

const BetaResponseInputImageDetailLow BetaResponseInputImageDetail = "low"

const BetaResponseInputImageDetailHigh BetaResponseInputImageDetail = "high"

const BetaResponseInputImageDetailAuto BetaResponseInputImageDetail = "auto"

const BetaResponseInputImageDetailOriginal BetaResponseInputImageDetail = "original"

Type InputImage

FileID stringOptional

ImageURL stringOptional

PromptCacheBreakpoint BetaResponseInputImagePromptCacheBreakpointOptional

Mode Explicit

type BetaResponseInputFile struct{…}

Type InputFile

Detail BetaResponseInputFileDetailOptional

const BetaResponseInputFileDetailAuto BetaResponseInputFileDetail = "auto"

const BetaResponseInputFileDetailLow BetaResponseInputFileDetail = "low"

const BetaResponseInputFileDetailHigh BetaResponseInputFileDetail = "high"

FileData stringOptional

FileID stringOptional

FileURL stringOptional

Filename stringOptional

PromptCacheBreakpoint BetaResponseInputFilePromptCacheBreakpointOptional

Mode Explicit

Role BetaResponseInputMessageItemRole

const BetaResponseInputMessageItemRoleUser BetaResponseInputMessageItemRole = "user"

const BetaResponseInputMessageItemRoleSystem BetaResponseInputMessageItemRole = "system"

const BetaResponseInputMessageItemRoleDeveloper BetaResponseInputMessageItemRole = "developer"

Type Message

Agent BetaResponseInputMessageItemAgentOptional

AgentName string

Status BetaResponseInputMessageItemStatusOptional

const BetaResponseInputMessageItemStatusInProgress BetaResponseInputMessageItemStatus = "in\_progress"

const BetaResponseInputMessageItemStatusCompleted BetaResponseInputMessageItemStatus = "completed"

const BetaResponseInputMessageItemStatusIncomplete BetaResponseInputMessageItemStatus = "incomplete"

type BetaResponseOutputMessage struct{…}

ID string

Content []BetaResponseOutputMessageContentUnion

type BetaResponseOutputText struct{…}

Annotations []BetaResponseOutputTextAnnotationUnion

type BetaResponseOutputTextAnnotationFileCitation struct{…}

FileID string

Filename string

Index int64

Type FileCitation

type BetaResponseOutputTextAnnotationURLCitation struct{…}

EndIndex int64

StartIndex int64

Title string

Type URLCitation

URL string

type BetaResponseOutputTextAnnotationContainerFileCitation struct{…}

ContainerID string

EndIndex int64

FileID string

Filename string

StartIndex int64

Type ContainerFileCitation

type BetaResponseOutputTextAnnotationFilePath struct{…}

FileID string

Index int64

Type FilePath

Text string

Type OutputText

Logprobs []BetaResponseOutputTextLogprobOptional

Token string

Bytes []int64

Logprob float64

TopLogprobs []BetaResponseOutputTextLogprobTopLogprob

Token string

Bytes []int64

Logprob float64

type BetaResponseOutputRefusal struct{…}

Refusal string

Type Refusal

Role Assistant

Status BetaResponseOutputMessageStatus

const BetaResponseOutputMessageStatusInProgress BetaResponseOutputMessageStatus = "in\_progress"

const BetaResponseOutputMessageStatusCompleted BetaResponseOutputMessageStatus = "completed"

const BetaResponseOutputMessageStatusIncomplete BetaResponseOutputMessageStatus = "incomplete"

Type Message

Agent BetaResponseOutputMessageAgentOptional

AgentName string

Phase BetaResponseOutputMessagePhaseOptional

const BetaResponseOutputMessagePhaseCommentary BetaResponseOutputMessagePhase = "commentary"

const BetaResponseOutputMessagePhaseFinalAnswer BetaResponseOutputMessagePhase = "final\_answer"

type BetaResponseFileSearchToolCall struct{…}

[file search guide](https://platform.openai.com/docs/guides/tools-file-search) for more information.

ID string

Queries []string

Status BetaResponseFileSearchToolCallStatus

const BetaResponseFileSearchToolCallStatusInProgress BetaResponseFileSearchToolCallStatus = "in\_progress"

const BetaResponseFileSearchToolCallStatusSearching BetaResponseFileSearchToolCallStatus = "searching"

const BetaResponseFileSearchToolCallStatusCompleted BetaResponseFileSearchToolCallStatus = "completed"

const BetaResponseFileSearchToolCallStatusIncomplete BetaResponseFileSearchToolCallStatus = "incomplete"

const BetaResponseFileSearchToolCallStatusFailed BetaResponseFileSearchToolCallStatus = "failed"

Type FileSearchCall

Agent BetaResponseFileSearchToolCallAgentOptional

AgentName string

Results []BetaResponseFileSearchToolCallResultOptional

Attributes map[string, BetaResponseFileSearchToolCallResultAttributeUnion]Optional

string

float64

bool

FileID stringOptional

Filename stringOptional

Score float64Optional

formatfloat

Text stringOptional

type BetaResponseComputerToolCall struct{…}

[computer use guide](https://platform.openai.com/docs/guides/tools-computer-use) for more information.

ID string

CallID string

PendingSafetyChecks []BetaResponseComputerToolCallPendingSafetyCheck

ID string

Code stringOptional

Message stringOptional

Status BetaResponseComputerToolCallStatus

const BetaResponseComputerToolCallStatusInProgress BetaResponseComputerToolCallStatus = "in\_progress"

const BetaResponseComputerToolCallStatusCompleted BetaResponseComputerToolCallStatus = "completed"

const BetaResponseComputerToolCallStatusIncomplete BetaResponseComputerToolCallStatus = "incomplete"

Type BetaResponseComputerToolCallType

Action [BetaComputerActionUnion](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_computer_action%20%3E%20(schema))Optional

type BetaComputerActionClick struct{…}

Button string

Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

const BetaComputerActionClickButtonLeft BetaComputerActionClickButton = "left"

const BetaComputerActionClickButtonRight BetaComputerActionClickButton = "right"

const BetaComputerActionClickButtonWheel BetaComputerActionClickButton = "wheel"

const BetaComputerActionClickButtonBack BetaComputerActionClickButton = "back"

const BetaComputerActionClickButtonForward BetaComputerActionClickButton = "forward"

Type Click

Specifies the event type. For a click action, this property is always `click`.

X int64

The x-coordinate where the click occurred.

Y int64

The y-coordinate where the click occurred.

Keys []stringOptional

The keys being held while clicking.

type BetaComputerActionDoubleClick struct{…}

A double click action.

Keys []string

The keys being held while double-clicking.

Type DoubleClick

Specifies the event type. For a double click action, this property is always set to `double_click`.

X int64

The x-coordinate where the double click occurred.

Y int64

The y-coordinate where the double click occurred.

type BetaComputerActionDrag struct{…}

A drag action.

Path []BetaComputerActionDragPath

An array of coordinates representing the path of the drag action. Coordinates will appear as an array of objects, eg

  { x: 100, y: 200 },
  { x: 200, y: 300 }

X int64

The x-coordinate.

Y int64

The y-coordinate.

Type Drag

Specifies the event type. For a drag action, this property is always set to `drag`.

Keys []stringOptional

The keys being held while dragging the mouse.

type BetaComputerActionKeypress struct{…}

A collection of keypresses the model would like to perform.

Keys []string

The combination of keys the model is requesting to be pressed. This is an array of strings, each representing a key.

Type Keypress

Specifies the event type. For a keypress action, this property is always set to `keypress`.

type BetaComputerActionMove struct{…}

A mouse move action.

Type Move

Specifies the event type. For a move action, this property is always set to `move`.

X int64

The x-coordinate to move to.

Y int64

The y-coordinate to move to.

Keys []stringOptional

The keys being held while moving the mouse.

type BetaComputerActionScreenshot struct{…}

A screenshot action.

Type Screenshot

Specifies the event type. For a screenshot action, this property is always set to `screenshot`.

type BetaComputerActionScroll struct{…}

A scroll action.

ScrollX int64

The horizontal scroll distance.

ScrollY int64

The vertical scroll distance.

Type Scroll

Specifies the event type. For a scroll action, this property is always set to `scroll`.

X int64

The x-coordinate where the scroll occurred.

Y int64

The y-coordinate where the scroll occurred.

Keys []stringOptional

The keys being held while scrolling.

type BetaComputerActionType struct{…}

An action to type in text.

Text string

The text to type.

Type Type

Specifies the event type. For a type action, this property is always set to `type`.

type BetaComputerActionWait struct{…}

A wait action.

Type Wait

Specifies the event type. For a wait action, this property is always set to `wait`.

Actions [BetaComputerActionList](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_computer_action_list%20%3E%20(schema))Optional

type BetaComputerActionClick struct{…}

Button string

Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

const BetaComputerActionClickButtonLeft BetaComputerActionClickButton = "left"

const BetaComputerActionClickButtonRight BetaComputerActionClickButton = "right"

const BetaComputerActionClickButtonWheel BetaComputerActionClickButton = "wheel"

const BetaComputerActionClickButtonBack BetaComputerActionClickButton = "back"

const BetaComputerActionClickButtonForward BetaComputerActionClickButton = "forward"

Type Click

Specifies the event type. For a click action, this property is always `click`.

X int64

The x-coordinate where the click occurred.

Y int64

The y-coordinate where the click occurred.

Keys []stringOptional

The keys being held while clicking.

type BetaComputerActionDoubleClick struct{…}

A double click action.

Keys []string

The keys being held while double-clicking.

Type DoubleClick

Specifies the event type. For a double click action, this property is always set to `double_click`.

X int64

The x-coordinate where the double click occurred.

Y int64

The y-coordinate where the double click occurred.

type BetaComputerActionDrag struct{…}

A drag action.

Path []BetaComputerActionDragPath

An array of coordinates representing the path of the drag action. Coordinates will appear as an array of objects, eg

  { x: 100, y: 200 },
  { x: 200, y: 300 }

X int64

The x-coordinate.

Y int64

The y-coordinate.

Type Drag

Specifies the event type. For a drag action, this property is always set to `drag`.

Keys []stringOptional

The keys being held while dragging the mouse.

type BetaComputerActionKeypress struct{…}

A collection of keypresses the model would like to perform.

Keys []string

The combination of keys the model is requesting to be pressed. This is an array of strings, each representing a key.

Type Keypress

Specifies the event type. For a keypress action, this property is always set to `keypress`.

type BetaComputerActionMove struct{…}

A mouse move action.

Type Move

Specifies the event type. For a move action, this property is always set to `move`.

X int64

The x-coordinate to move to.

Y int64

The y-coordinate to move to.

Keys []stringOptional

The keys being held while moving the mouse.

type BetaComputerActionScreenshot struct{…}

A screenshot action.

Type Screenshot

Specifies the event type. For a screenshot action, this property is always set to `screenshot`.

type BetaComputerActionScroll struct{…}

A scroll action.

ScrollX int64

The horizontal scroll distance.

ScrollY int64

The vertical scroll distance.

Type Scroll

Specifies the event type. For a scroll action, this property is always set to `scroll`.

X int64

The x-coordinate where the scroll occurred.

Y int64

The y-coordinate where the scroll occurred.

Keys []stringOptional

The keys being held while scrolling.

type BetaComputerActionType struct{…}

An action to type in text.

Text string

The text to type.

Type Type

Specifies the event type. For a type action, this property is always set to `type`.

type BetaComputerActionWait struct{…}

A wait action.

Type Wait

Specifies the event type. For a wait action, this property is always set to `wait`.

Agent BetaResponseComputerToolCallAgentOptional

AgentName string

type BetaResponseComputerToolCallOutputItem struct{…}

ID string

The unique ID of the computer call tool output.

CallID string

Output [BetaResponseComputerToolCallOutputScreenshot](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_computer_tool_call_output_screenshot%20%3E%20(schema))

Type ComputerScreenshot

Specifies the event type. For a computer screenshot, this property is
always set to `computer_screenshot`.

FileID stringOptional

ImageURL stringOptional

Status BetaResponseComputerToolCallOutputItemStatus

const BetaResponseComputerToolCallOutputItemStatusCompleted BetaResponseComputerToolCallOutputItemStatus = "completed"

const BetaResponseComputerToolCallOutputItemStatusIncomplete BetaResponseComputerToolCallOutputItemStatus = "incomplete"

const BetaResponseComputerToolCallOutputItemStatusFailed BetaResponseComputerToolCallOutputItemStatus = "failed"

const BetaResponseComputerToolCallOutputItemStatusInProgress BetaResponseComputerToolCallOutputItemStatus = "in\_progress"

Type ComputerCallOutput

AcknowledgedSafetyChecks []BetaResponseComputerToolCallOutputItemAcknowledgedSafetyCheckOptional

The safety checks reported by the API that have been acknowledged by the
developer.

ID string

Code stringOptional

Message stringOptional

Agent BetaResponseComputerToolCallOutputItemAgentOptional

AgentName string

CreatedBy stringOptional

The identifier of the actor that created the item.

type BetaResponseFunctionWebSearch struct{…}

[web search guide](https://platform.openai.com/docs/guides/tools-web-search) for more information.

ID string

Action BetaResponseFunctionWebSearchActionUnion

type BetaResponseFunctionWebSearchActionSearch struct{…}

Type Search

Queries []stringOptional

DeprecatedQuery stringOptional

Sources []BetaResponseFunctionWebSearchActionSearchSourceOptional

Type URL

URL string

type BetaResponseFunctionWebSearchActionOpenPage struct{…}

Type OpenPage

URL stringOptional

type BetaResponseFunctionWebSearchActionFindInPage struct{…}

Pattern string

Type FindInPage

URL string

Status BetaResponseFunctionWebSearchStatus

const BetaResponseFunctionWebSearchStatusInProgress BetaResponseFunctionWebSearchStatus = "in\_progress"

const BetaResponseFunctionWebSearchStatusSearching BetaResponseFunctionWebSearchStatus = "searching"

const BetaResponseFunctionWebSearchStatusCompleted BetaResponseFunctionWebSearchStatus = "completed"

const BetaResponseFunctionWebSearchStatusFailed BetaResponseFunctionWebSearchStatus = "failed"

Type WebSearchCall

Agent BetaResponseFunctionWebSearchAgentOptional

AgentName string

type BetaResponseFunctionToolCallItem struct{…}

[function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.

ID string

Status string

const BetaResponseFunctionToolCallItemStatusInProgress BetaResponseFunctionToolCallItemStatus = "in\_progress"

const BetaResponseFunctionToolCallItemStatusCompleted BetaResponseFunctionToolCallItemStatus = "completed"

const BetaResponseFunctionToolCallItemStatusIncomplete BetaResponseFunctionToolCallItemStatus = "incomplete"

CreatedBy stringOptional

The identifier of the actor that created the item.

type BetaResponseFunctionToolCallOutputItem struct{…}

ID string

The unique ID of the function call tool output.

CallID string

Output BetaResponseFunctionToolCallOutputItemOutputUnion

The output from the function call generated by your code.

string

type BetaResponseFunctionToolCallOutputItemOutputOutputContentList []BetaResponseFunctionToolCallOutputItemOutputOutputContentListItemUnion

Text, image, or file output of the function call.

type BetaResponseInputText struct{…}

Text string

Type InputText

PromptCacheBreakpoint BetaResponseInputTextPromptCacheBreakpointOptional

Mode Explicit

type BetaResponseInputImage struct{…}

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

Detail BetaResponseInputImageDetail

const BetaResponseInputImageDetailLow BetaResponseInputImageDetail = "low"

const BetaResponseInputImageDetailHigh BetaResponseInputImageDetail = "high"

const BetaResponseInputImageDetailAuto BetaResponseInputImageDetail = "auto"

const BetaResponseInputImageDetailOriginal BetaResponseInputImageDetail = "original"

Type InputImage

FileID stringOptional

ImageURL stringOptional

PromptCacheBreakpoint BetaResponseInputImagePromptCacheBreakpointOptional

Mode Explicit

type BetaResponseInputFile struct{…}

Type InputFile

Detail BetaResponseInputFileDetailOptional

const BetaResponseInputFileDetailAuto BetaResponseInputFileDetail = "auto"

const BetaResponseInputFileDetailLow BetaResponseInputFileDetail = "low"

const BetaResponseInputFileDetailHigh BetaResponseInputFileDetail = "high"

FileData stringOptional

FileID stringOptional

FileURL stringOptional

Filename stringOptional

PromptCacheBreakpoint BetaResponseInputFilePromptCacheBreakpointOptional

Mode Explicit

Status BetaResponseFunctionToolCallOutputItemStatus

const BetaResponseFunctionToolCallOutputItemStatusInProgress BetaResponseFunctionToolCallOutputItemStatus = "in\_progress"

const BetaResponseFunctionToolCallOutputItemStatusCompleted BetaResponseFunctionToolCallOutputItemStatus = "completed"

const BetaResponseFunctionToolCallOutputItemStatusIncomplete BetaResponseFunctionToolCallOutputItemStatus = "incomplete"

Type FunctionCallOutput

Agent BetaResponseFunctionToolCallOutputItemAgentOptional

AgentName string

Caller BetaResponseFunctionToolCallOutputItemCallerUnionOptional

type BetaResponseFunctionToolCallOutputItemCallerDirect struct{…}

Type Direct

The caller type. Always `direct`.

type BetaResponseFunctionToolCallOutputItemCallerProgram struct{…}

CallerID string

maxLength64

minLength1

Type Program

CreatedBy stringOptional

The identifier of the actor that created the item.

type BetaResponseItemAgentMessage struct{…}

ID string

The unique ID of the agent message.

Author string

Content []BetaResponseItemAgentMessageContentUnion

Encrypted content sent between agents.

type BetaResponseInputText struct{…}

Text string

Type InputText

PromptCacheBreakpoint BetaResponseInputTextPromptCacheBreakpointOptional

Mode Explicit

type BetaResponseOutputText struct{…}

Annotations []BetaResponseOutputTextAnnotationUnion

type BetaResponseOutputTextAnnotationFileCitation struct{…}

FileID string

Filename string

Index int64

Type FileCitation

type BetaResponseOutputTextAnnotationURLCitation struct{…}

EndIndex int64

StartIndex int64

Title string

Type URLCitation

URL string

type BetaResponseOutputTextAnnotationContainerFileCitation struct{…}

ContainerID string

EndIndex int64

FileID string

Filename string

StartIndex int64

Type ContainerFileCitation

type BetaResponseOutputTextAnnotationFilePath struct{…}

FileID string

Index int64

Type FilePath

Text string

Type OutputText

Logprobs []BetaResponseOutputTextLogprobOptional

Token string

Bytes []int64

Logprob float64

TopLogprobs []BetaResponseOutputTextLogprobTopLogprob

Token string

Bytes []int64

Logprob float64

type BetaResponseItemAgentMessageContentText struct{…}

A text content.

Text string

Type Text

type BetaResponseItemAgentMessageContentSummaryText struct{…}

A summary text from the model.

Text string

Type SummaryText

type BetaResponseItemAgentMessageContentReasoningText struct{…}

Text string

Type ReasoningText

type BetaResponseOutputRefusal struct{…}

Refusal string

Type Refusal

type BetaResponseInputImage struct{…}

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

Detail BetaResponseInputImageDetail

const BetaResponseInputImageDetailLow BetaResponseInputImageDetail = "low"

const BetaResponseInputImageDetailHigh BetaResponseInputImageDetail = "high"

const BetaResponseInputImageDetailAuto BetaResponseInputImageDetail = "auto"

const BetaResponseInputImageDetailOriginal BetaResponseInputImageDetail = "original"

Type InputImage

FileID stringOptional

ImageURL stringOptional

PromptCacheBreakpoint BetaResponseInputImagePromptCacheBreakpointOptional

Mode Explicit

type BetaResponseItemAgentMessageContentComputerScreenshot struct{…}

A screenshot of a computer.

Detail string

The detail level of the screenshot image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

const BetaResponseItemAgentMessageContentComputerScreenshotDetailLow BetaResponseItemAgentMessageContentComputerScreenshotDetail = "low"

const BetaResponseItemAgentMessageContentComputerScreenshotDetailHigh BetaResponseItemAgentMessageContentComputerScreenshotDetail = "high"

const BetaResponseItemAgentMessageContentComputerScreenshotDetailAuto BetaResponseItemAgentMessageContentComputerScreenshotDetail = "auto"

const BetaResponseItemAgentMessageContentComputerScreenshotDetailOriginal BetaResponseItemAgentMessageContentComputerScreenshotDetail = "original"

FileID string

ImageURL string

Type ComputerScreenshot

Specifies the event type. For a computer screenshot, this property is always set to `computer_screenshot`.

PromptCacheBreakpoint BetaResponseItemAgentMessageContentComputerScreenshotPromptCacheBreakpointOptional

Mode Explicit

type BetaResponseInputFile struct{…}

Type InputFile

Detail BetaResponseInputFileDetailOptional

const BetaResponseInputFileDetailAuto BetaResponseInputFileDetail = "auto"

const BetaResponseInputFileDetailLow BetaResponseInputFileDetail = "low"

const BetaResponseInputFileDetailHigh BetaResponseInputFileDetail = "high"

FileData stringOptional

FileID stringOptional

FileURL stringOptional

Filename stringOptional

PromptCacheBreakpoint BetaResponseInputFilePromptCacheBreakpointOptional

Mode Explicit

type BetaResponseItemAgentMessageContentEncryptedContent struct{…}

EncryptedContent string

Type EncryptedContent

Recipient string

Type AgentMessage

The type of the item. Always `agent_message`.

Agent BetaResponseItemAgentMessageAgentOptional

AgentName string

type BetaResponseItemMultiAgentCall struct{…}

ID string

The unique ID of the multi-agent call item.

Action string

The multi-agent action to execute.

const BetaResponseItemMultiAgentCallActionSpawnAgent BetaResponseItemMultiAgentCallAction = "spawn\_agent"

const BetaResponseItemMultiAgentCallActionInterruptAgent BetaResponseItemMultiAgentCallAction = "interrupt\_agent"

const BetaResponseItemMultiAgentCallActionListAgents BetaResponseItemMultiAgentCallAction = "list\_agents"

const BetaResponseItemMultiAgentCallActionSendMessage BetaResponseItemMultiAgentCallAction = "send\_message"

const BetaResponseItemMultiAgentCallActionFollowupTask BetaResponseItemMultiAgentCallAction = "followup\_task"

const BetaResponseItemMultiAgentCallActionWaitAgent BetaResponseItemMultiAgentCallAction = "wait\_agent"

Arguments string

The JSON string of arguments generated for the action.

CallID string

Type MultiAgentCall

The type of the multi-agent call. Always `multi_agent_call`.

Agent BetaResponseItemMultiAgentCallAgentOptional

AgentName string

type BetaResponseItemMultiAgentCallOutput struct{…}

ID string

The unique ID of the multi-agent call output item.

Action string

const BetaResponseItemMultiAgentCallOutputActionSpawnAgent BetaResponseItemMultiAgentCallOutputAction = "spawn\_agent"

const BetaResponseItemMultiAgentCallOutputActionInterruptAgent BetaResponseItemMultiAgentCallOutputAction = "interrupt\_agent"

const BetaResponseItemMultiAgentCallOutputActionListAgents BetaResponseItemMultiAgentCallOutputAction = "list\_agents"

const BetaResponseItemMultiAgentCallOutputActionSendMessage BetaResponseItemMultiAgentCallOutputAction = "send\_message"

const BetaResponseItemMultiAgentCallOutputActionFollowupTask BetaResponseItemMultiAgentCallOutputAction = "followup\_task"

const BetaResponseItemMultiAgentCallOutputActionWaitAgent BetaResponseItemMultiAgentCallOutputAction = "wait\_agent"

CallID string

Output [][BetaResponseOutputText](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_text%20%3E%20(schema))

Annotations []BetaResponseOutputTextAnnotationUnion

type BetaResponseOutputTextAnnotationFileCitation struct{…}

FileID string

Filename string

Index int64

Type FileCitation

type BetaResponseOutputTextAnnotationURLCitation struct{…}

EndIndex int64

StartIndex int64

Title string

Type URLCitation

URL string

type BetaResponseOutputTextAnnotationContainerFileCitation struct{…}

ContainerID string

EndIndex int64

FileID string

Filename string

StartIndex int64

Type ContainerFileCitation

type BetaResponseOutputTextAnnotationFilePath struct{…}

FileID string

Index int64

Type FilePath

Text string

Type OutputText

Logprobs []BetaResponseOutputTextLogprobOptional

Token string

Bytes []int64

Logprob float64

TopLogprobs []BetaResponseOutputTextLogprobTopLogprob

Token string

Bytes []int64

Logprob float64

Type MultiAgentCallOutput

The type of the multi-agent result. Always `multi_agent_call_output`.

Agent BetaResponseItemMultiAgentCallOutputAgentOptional

AgentName string

type BetaResponseToolSearchCall struct{…}

ID string

The unique ID of the tool search call item.

Arguments any

Arguments used for the tool search call.

CallID string

Execution BetaResponseToolSearchCallExecution

const BetaResponseToolSearchCallExecutionServer BetaResponseToolSearchCallExecution = "server"

const BetaResponseToolSearchCallExecutionClient BetaResponseToolSearchCallExecution = "client"

Status BetaResponseToolSearchCallStatus

The status of the tool search call item that was recorded.

const BetaResponseToolSearchCallStatusInProgress BetaResponseToolSearchCallStatus = "in\_progress"

const BetaResponseToolSearchCallStatusCompleted BetaResponseToolSearchCallStatus = "completed"

const BetaResponseToolSearchCallStatusIncomplete BetaResponseToolSearchCallStatus = "incomplete"

Type ToolSearchCall

The type of the item. Always `tool_search_call`.

Agent BetaResponseToolSearchCallAgentOptional

AgentName string

CreatedBy stringOptional

The identifier of the actor that created the item.

type BetaResponseToolSearchOutputItem struct{…}

ID string

The unique ID of the tool search output item.

CallID string

Execution BetaResponseToolSearchOutputItemExecution

const BetaResponseToolSearchOutputItemExecutionServer BetaResponseToolSearchOutputItemExecution = "server"

const BetaResponseToolSearchOutputItemExecutionClient BetaResponseToolSearchOutputItemExecution = "client"

Status BetaResponseToolSearchOutputItemStatus

The status of the tool search output item that was recorded.

const BetaResponseToolSearchOutputItemStatusInProgress BetaResponseToolSearchOutputItemStatus = "in\_progress"

const BetaResponseToolSearchOutputItemStatusCompleted BetaResponseToolSearchOutputItemStatus = "completed"

const BetaResponseToolSearchOutputItemStatusIncomplete BetaResponseToolSearchOutputItemStatus = "incomplete"

Tools [][BetaToolUnion](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))

The loaded tool definitions returned by tool search.

type BetaFunctionTool struct{…}

Name string

Parameters map[string, any]

Strict bool

Type Function

AllowedCallers []stringOptional

const BetaFunctionToolAllowedCallerDirect BetaFunctionToolAllowedCaller = "direct"

const BetaFunctionToolAllowedCallerProgrammatic BetaFunctionToolAllowedCaller = "programmatic"

DeferLoading boolOptional

Description stringOptional

OutputSchema map[string, any]Optional

type BetaFileSearchTool struct{…}

Type FileSearch

VectorStoreIDs []string

Filters BetaFileSearchToolFiltersUnionOptional

type BetaFileSearchToolFiltersComparisonFilter struct{…}

Key string

Type string

const BetaFileSearchToolFiltersComparisonFilterTypeEq BetaFileSearchToolFiltersComparisonFilterType = "eq"

const BetaFileSearchToolFiltersComparisonFilterTypeNe BetaFileSearchToolFiltersComparisonFilterType = "ne"

const BetaFileSearchToolFiltersComparisonFilterTypeGt BetaFileSearchToolFiltersComparisonFilterType = "gt"

const BetaFileSearchToolFiltersComparisonFilterTypeGte BetaFileSearchToolFiltersComparisonFilterType = "gte"

const BetaFileSearchToolFiltersComparisonFilterTypeLt BetaFileSearchToolFiltersComparisonFilterType = "lt"

const BetaFileSearchToolFiltersComparisonFilterTypeLte BetaFileSearchToolFiltersComparisonFilterType = "lte"

const BetaFileSearchToolFiltersComparisonFilterTypeIn BetaFileSearchToolFiltersComparisonFilterType = "in"

const BetaFileSearchToolFiltersComparisonFilterTypeNin BetaFileSearchToolFiltersComparisonFilterType = "nin"

Value BetaFileSearchToolFiltersComparisonFilterValueUnion

string

float64

bool

type BetaFileSearchToolFiltersComparisonFilterValueArray []BetaFileSearchToolFiltersComparisonFilterValueArrayItemUnion

string

float64

type BetaFileSearchToolFiltersCompoundFilter struct{…}

Filters []BetaFileSearchToolFiltersCompoundFilterFilter

type BetaFileSearchToolFiltersCompoundFilterFilter struct{…}

Key string

Type string

const BetaFileSearchToolFiltersCompoundFilterFilterTypeEq BetaFileSearchToolFiltersCompoundFilterFilterType = "eq"

const BetaFileSearchToolFiltersCompoundFilterFilterTypeNe BetaFileSearchToolFiltersCompoundFilterFilterType = "ne"

const BetaFileSearchToolFiltersCompoundFilterFilterTypeGt BetaFileSearchToolFiltersCompoundFilterFilterType = "gt"

const BetaFileSearchToolFiltersCompoundFilterFilterTypeGte BetaFileSearchToolFiltersCompoundFilterFilterType = "gte"

const BetaFileSearchToolFiltersCompoundFilterFilterTypeLt BetaFileSearchToolFiltersCompoundFilterFilterType = "lt"

const BetaFileSearchToolFiltersCompoundFilterFilterTypeLte BetaFileSearchToolFiltersCompoundFilterFilterType = "lte"

const BetaFileSearchToolFiltersCompoundFilterFilterTypeIn BetaFileSearchToolFiltersCompoundFilterFilterType = "in"

const BetaFileSearchToolFiltersCompoundFilterFilterTypeNin BetaFileSearchToolFiltersCompoundFilterFilterType = "nin"

Value BetaFileSearchToolFiltersCompoundFilterFilterValueUnion

string

float64

bool

type BetaFileSearchToolFiltersCompoundFilterFilterValueArray []BetaFileSearchToolFiltersCompoundFilterFilterValueArrayItemUnion

string

float64

Type string

const BetaFileSearchToolFiltersCompoundFilterTypeAnd BetaFileSearchToolFiltersCompoundFilterType = "and"

const BetaFileSearchToolFiltersCompoundFilterTypeOr BetaFileSearchToolFiltersCompoundFilterType = "or"

MaxNumResults int64Optional

RankingOptions BetaFileSearchToolRankingOptionsOptional

HybridSearch BetaFileSearchToolRankingOptionsHybridSearchOptional

EmbeddingWeight float64

TextWeight float64

Ranker stringOptional

const BetaFileSearchToolRankingOptionsRankerAuto BetaFileSearchToolRankingOptionsRanker = "auto"

const BetaFileSearchToolRankingOptionsRankerDefault2024\_11\_15 BetaFileSearchToolRankingOptionsRanker = "default-2024-11-15"

ScoreThreshold float64Optional

type BetaComputerTool struct{…}

Type Computer

type BetaComputerUsePreviewTool struct{…}

DisplayHeight int64

DisplayWidth int64

Environment BetaComputerUsePreviewToolEnvironment

const BetaComputerUsePreviewToolEnvironmentWindows BetaComputerUsePreviewToolEnvironment = "windows"

const BetaComputerUsePreviewToolEnvironmentMac BetaComputerUsePreviewToolEnvironment = "mac"

const BetaComputerUsePreviewToolEnvironmentLinux BetaComputerUsePreviewToolEnvironment = "linux"

const BetaComputerUsePreviewToolEnvironmentUbuntu BetaComputerUsePreviewToolEnvironment = "ubuntu"

const BetaComputerUsePreviewToolEnvironmentBrowser BetaComputerUsePreviewToolEnvironment = "browser"

Type ComputerUsePreview

type BetaWebSearchTool struct{…}

[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type BetaWebSearchToolType

const BetaWebSearchToolTypeWebSearch BetaWebSearchToolType = "web\_search"

const BetaWebSearchToolTypeWebSearch2025\_08\_26 BetaWebSearchToolType = "web\_search\_2025\_08\_26"

Filters BetaWebSearchToolFiltersOptional

AllowedDomains []stringOptional

SearchContextSize BetaWebSearchToolSearchContextSizeOptional

const BetaWebSearchToolSearchContextSizeLow BetaWebSearchToolSearchContextSize = "low"

const BetaWebSearchToolSearchContextSizeMedium BetaWebSearchToolSearchContextSize = "medium"

const BetaWebSearchToolSearchContextSizeHigh BetaWebSearchToolSearchContextSize = "high"

UserLocation BetaWebSearchToolUserLocationOptional

City stringOptional

Country stringOptional

Region stringOptional

Timezone stringOptional

Type stringOptional

type BetaToolMcp struct{…}

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

ServerLabel string

Type Mcp

AllowedCallers []stringOptional

const BetaToolMcpAllowedCallerDirect BetaToolMcpAllowedCaller = "direct"

const BetaToolMcpAllowedCallerProgrammatic BetaToolMcpAllowedCaller = "programmatic"

AllowedTools BetaToolMcpAllowedToolsUnionOptional

type BetaToolMcpAllowedToolsMcpAllowedTools []string

A string array of allowed tool names

type BetaToolMcpAllowedToolsMcpToolFilter struct{…}

ReadOnly boolOptional

ToolNames []stringOptional

Authorization stringOptional

ConnectorID stringOptional

about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

const BetaToolMcpConnectorIDConnectorDropbox BetaToolMcpConnectorID = "connector\_dropbox"

const BetaToolMcpConnectorIDConnectorGmail BetaToolMcpConnectorID = "connector\_gmail"

const BetaToolMcpConnectorIDConnectorGooglecalendar BetaToolMcpConnectorID = "connector\_googlecalendar"

const BetaToolMcpConnectorIDConnectorGoogledrive BetaToolMcpConnectorID = "connector\_googledrive"

const BetaToolMcpConnectorIDConnectorMicrosoftteams BetaToolMcpConnectorID = "connector\_microsoftteams"

const BetaToolMcpConnectorIDConnectorOutlookcalendar BetaToolMcpConnectorID = "connector\_outlookcalendar"

const BetaToolMcpConnectorIDConnectorOutlookemail BetaToolMcpConnectorID = "connector\_outlookemail"

const BetaToolMcpConnectorIDConnectorSharepoint BetaToolMcpConnectorID = "connector\_sharepoint"

DeferLoading boolOptional

Headers map[string, string]Optional

RequireApproval BetaToolMcpRequireApprovalUnionOptional

type BetaToolMcpRequireApprovalMcpToolApprovalFilter struct{…}

Always BetaToolMcpRequireApprovalMcpToolApprovalFilterAlwaysOptional

ReadOnly boolOptional

ToolNames []stringOptional

Never BetaToolMcpRequireApprovalMcpToolApprovalFilterNeverOptional

ReadOnly boolOptional

ToolNames []stringOptional

type BetaToolMcpRequireApprovalMcpToolApprovalSetting string

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

const BetaToolMcpRequireApprovalMcpToolApprovalSettingAlways BetaToolMcpRequireApprovalMcpToolApprovalSetting = "always"

const BetaToolMcpRequireApprovalMcpToolApprovalSettingNever BetaToolMcpRequireApprovalMcpToolApprovalSetting = "never"

ServerDescription stringOptional

ServerURL stringOptional

TunnelID stringOptional

type BetaToolCodeInterpreter struct{…}

A tool that runs Python code to help generate a response to a prompt.

Container BetaToolCodeInterpreterContainerUnion

string

type BetaToolCodeInterpreterContainerCodeInterpreterToolAuto struct{…}

Type Auto

FileIDs []stringOptional

MemoryLimit stringOptional

const BetaToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit1g BetaToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit = "1g"

const BetaToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit4g BetaToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit = "4g"

const BetaToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit16g BetaToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit = "16g"

const BetaToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit64g BetaToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit = "64g"

NetworkPolicy BetaToolCodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicyUnionOptional

type BetaContainerNetworkPolicyDisabled struct{…}

Type Disabled

type BetaContainerNetworkPolicyAllowlist struct{…}

AllowedDomains []string

Type Allowlist

DomainSecrets [][BetaContainerNetworkPolicyDomainSecret](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))Optional

Domain string

minLength1

Name string

minLength1

Value string

maxLength10485760

minLength1

Type CodeInterpreter

AllowedCallers []stringOptional

const BetaToolCodeInterpreterAllowedCallerDirect BetaToolCodeInterpreterAllowedCaller = "direct"

const BetaToolCodeInterpreterAllowedCallerProgrammatic BetaToolCodeInterpreterAllowedCaller = "programmatic"

type BetaToolProgrammaticToolCalling struct{…}

Type ProgrammaticToolCalling

The type of the tool. Always `programmatic_tool_calling`.

type BetaToolImageGeneration struct{…}

A tool that generates images using the GPT image models.

Type ImageGeneration

Action stringOptional

const BetaToolImageGenerationActionGenerate BetaToolImageGenerationAction = "generate"

const BetaToolImageGenerationActionEdit BetaToolImageGenerationAction = "edit"

const BetaToolImageGenerationActionAuto BetaToolImageGenerationAction = "auto"

Background stringOptional

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

const BetaToolImageGenerationBackgroundTransparent BetaToolImageGenerationBackground = "transparent"

const BetaToolImageGenerationBackgroundOpaque BetaToolImageGenerationBackground = "opaque"

const BetaToolImageGenerationBackgroundAuto BetaToolImageGenerationBackground = "auto"

InputFidelity stringOptional

const BetaToolImageGenerationInputFidelityHigh BetaToolImageGenerationInputFidelity = "high"

const BetaToolImageGenerationInputFidelityLow BetaToolImageGenerationInputFidelity = "low"

InputImageMask BetaToolImageGenerationInputImageMaskOptional

FileID stringOptional

ImageURL stringOptional

Model stringOptional

string

string

const BetaToolImageGenerationModelGPTImage1 BetaToolImageGenerationModel = "gpt-image-1"

const BetaToolImageGenerationModelGPTImage1Mini BetaToolImageGenerationModel = "gpt-image-1-mini"

const BetaToolImageGenerationModelGPTImage2 BetaToolImageGenerationModel = "gpt-image-2"

const BetaToolImageGenerationModelGPTImage2\_2026\_04\_21 BetaToolImageGenerationModel = "gpt-image-2-2026-04-21"

const BetaToolImageGenerationModelGPTImage1\_5 BetaToolImageGenerationModel = "gpt-image-1.5"

const BetaToolImageGenerationModelChatgptImageLatest BetaToolImageGenerationModel = "chatgpt-image-latest"

Moderation stringOptional

const BetaToolImageGenerationModerationAuto BetaToolImageGenerationModeration = "auto"

const BetaToolImageGenerationModerationLow BetaToolImageGenerationModeration = "low"

OutputCompression int64Optional

minimum0

maximum100

OutputFormat stringOptional

const BetaToolImageGenerationOutputFormatPNG BetaToolImageGenerationOutputFormat = "png"

const BetaToolImageGenerationOutputFormatWebP BetaToolImageGenerationOutputFormat = "webp"

const BetaToolImageGenerationOutputFormatJPEG BetaToolImageGenerationOutputFormat = "jpeg"

PartialImages int64Optional

minimum0

maximum3

Quality stringOptional

const BetaToolImageGenerationQualityLow BetaToolImageGenerationQuality = "low"

const BetaToolImageGenerationQualityMedium BetaToolImageGenerationQuality = "medium"

const BetaToolImageGenerationQualityHigh BetaToolImageGenerationQuality = "high"

const BetaToolImageGenerationQualityAuto BetaToolImageGenerationQuality = "auto"

Size stringOptional

string

string

const BetaToolImageGenerationSize1024x1024 BetaToolImageGenerationSize = "1024x1024"

const BetaToolImageGenerationSize1024x1536 BetaToolImageGenerationSize = "1024x1536"

const BetaToolImageGenerationSize1536x1024 BetaToolImageGenerationSize = "1536x1024"

const BetaToolImageGenerationSizeAuto BetaToolImageGenerationSize = "auto"

type BetaToolLocalShell struct{…}

A tool that allows the model to execute shell commands in a local environment.

Type LocalShell

The type of the local shell tool. Always `local_shell`.

type BetaFunctionShellTool struct{…}

Type Shell

AllowedCallers []stringOptional

const BetaFunctionShellToolAllowedCallerDirect BetaFunctionShellToolAllowedCaller = "direct"

const BetaFunctionShellToolAllowedCallerProgrammatic BetaFunctionShellToolAllowedCaller = "programmatic"

Environment BetaFunctionShellToolEnvironmentUnionOptional

type BetaContainerAuto struct{…}

Type ContainerAuto

FileIDs []stringOptional

MemoryLimit BetaContainerAutoMemoryLimitOptional

const BetaContainerAutoMemoryLimit1g BetaContainerAutoMemoryLimit = "1g"

const BetaContainerAutoMemoryLimit4g BetaContainerAutoMemoryLimit = "4g"

const BetaContainerAutoMemoryLimit16g BetaContainerAutoMemoryLimit = "16g"

const BetaContainerAutoMemoryLimit64g BetaContainerAutoMemoryLimit = "64g"

NetworkPolicy BetaContainerAutoNetworkPolicyUnionOptional

type BetaContainerNetworkPolicyDisabled struct{…}

Type Disabled

type BetaContainerNetworkPolicyAllowlist struct{…}

AllowedDomains []string

Type Allowlist

DomainSecrets [][BetaContainerNetworkPolicyDomainSecret](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))Optional

Domain string

minLength1

Name string

minLength1

Value string

maxLength10485760

minLength1

Skills []BetaContainerAutoSkillUnionOptional

type BetaSkillReference struct{…}

SkillID string

maxLength64

minLength1

Type SkillReference

Version stringOptional

type BetaInlineSkill struct{…}

Description string

Name string

Source [BetaInlineSkillSource](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

Data string

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

MediaType ApplicationZip

The media type of the inline skill payload. Must be `application/zip`.

Type Base64

The type of the inline skill source. Must be `base64`.

Type Inline

type BetaLocalEnvironment struct{…}

Type Local

Skills [][BetaLocalSkill](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))Optional

Description string

Name string

Path string

type BetaContainerReference struct{…}

ContainerID string

Type ContainerReference

type BetaCustomTool struct{…}

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

Name string

Type Custom

AllowedCallers []stringOptional

const BetaCustomToolAllowedCallerDirect BetaCustomToolAllowedCaller = "direct"

const BetaCustomToolAllowedCallerProgrammatic BetaCustomToolAllowedCaller = "programmatic"

DeferLoading boolOptional

Description stringOptional

Format BetaCustomToolFormatUnionOptional

type BetaCustomToolFormatText struct{…}

Unconstrained free-form text.

Type Text

Unconstrained text format. Always `text`.

type BetaCustomToolFormatGrammar struct{…}

Definition string

Syntax string

const BetaCustomToolFormatGrammarSyntaxLark BetaCustomToolFormatGrammarSyntax = "lark"

const BetaCustomToolFormatGrammarSyntaxRegex BetaCustomToolFormatGrammarSyntax = "regex"

Type Grammar

type BetaNamespaceTool struct{…}

Description string

minLength1

Name string

minLength1

Tools []BetaNamespaceToolToolUnion

type BetaNamespaceToolToolFunction struct{…}

Name string

maxLength128

minLength1

Type Function

AllowedCallers []stringOptional

const BetaNamespaceToolToolFunctionAllowedCallerDirect BetaNamespaceToolToolFunctionAllowedCaller = "direct"

const BetaNamespaceToolToolFunctionAllowedCallerProgrammatic BetaNamespaceToolToolFunctionAllowedCaller = "programmatic"

DeferLoading boolOptional

Description stringOptional

OutputSchema map[string, any]Optional

Parameters anyOptional

Strict boolOptional

type BetaCustomTool struct{…}

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

Name string

Type Custom

AllowedCallers []stringOptional

const BetaCustomToolAllowedCallerDirect BetaCustomToolAllowedCaller = "direct"

const BetaCustomToolAllowedCallerProgrammatic BetaCustomToolAllowedCaller = "programmatic"

DeferLoading boolOptional

Description stringOptional

Format BetaCustomToolFormatUnionOptional

type BetaCustomToolFormatText struct{…}

Unconstrained free-form text.

Type Text

Unconstrained text format. Always `text`.

type BetaCustomToolFormatGrammar struct{…}

Definition string

Syntax string

const BetaCustomToolFormatGrammarSyntaxLark BetaCustomToolFormatGrammarSyntax = "lark"

const BetaCustomToolFormatGrammarSyntaxRegex BetaCustomToolFormatGrammarSyntax = "regex"

Type Grammar

Type Namespace

type BetaToolSearchTool struct{…}

Type ToolSearch

Description stringOptional

Execution BetaToolSearchToolExecutionOptional

const BetaToolSearchToolExecutionServer BetaToolSearchToolExecution = "server"

const BetaToolSearchToolExecutionClient BetaToolSearchToolExecution = "client"

Parameters anyOptional

type BetaWebSearchPreviewTool struct{…}

Type BetaWebSearchPreviewToolType

const BetaWebSearchPreviewToolTypeWebSearchPreview BetaWebSearchPreviewToolType = "web\_search\_preview"

const BetaWebSearchPreviewToolTypeWebSearchPreview2025\_03\_11 BetaWebSearchPreviewToolType = "web\_search\_preview\_2025\_03\_11"

SearchContentTypes []stringOptional

const BetaWebSearchPreviewToolSearchContentTypeText BetaWebSearchPreviewToolSearchContentType = "text"

const BetaWebSearchPreviewToolSearchContentTypeImage BetaWebSearchPreviewToolSearchContentType = "image"

SearchContextSize BetaWebSearchPreviewToolSearchContextSizeOptional

const BetaWebSearchPreviewToolSearchContextSizeLow BetaWebSearchPreviewToolSearchContextSize = "low"

const BetaWebSearchPreviewToolSearchContextSizeMedium BetaWebSearchPreviewToolSearchContextSize = "medium"

const BetaWebSearchPreviewToolSearchContextSizeHigh BetaWebSearchPreviewToolSearchContextSize = "high"

UserLocation BetaWebSearchPreviewToolUserLocationOptional

Type Approximate

City stringOptional

Country stringOptional

Region stringOptional

Timezone stringOptional

type BetaApplyPatchTool struct{…}

Type ApplyPatch

AllowedCallers []stringOptional

const BetaApplyPatchToolAllowedCallerDirect BetaApplyPatchToolAllowedCaller = "direct"

const BetaApplyPatchToolAllowedCallerProgrammatic BetaApplyPatchToolAllowedCaller = "programmatic"

Type ToolSearchOutput

The type of the item. Always `tool_search_output`.

Agent BetaResponseToolSearchOutputItemAgentOptional

AgentName string

CreatedBy stringOptional

The identifier of the actor that created the item.

type BetaResponseItemAdditionalTools struct{…}

ID string

The unique ID of the additional tools item.

Role string

The role that provided the additional tools.

const BetaResponseItemAdditionalToolsRoleUnknown BetaResponseItemAdditionalToolsRole = "unknown"

const BetaResponseItemAdditionalToolsRoleUser BetaResponseItemAdditionalToolsRole = "user"

const BetaResponseItemAdditionalToolsRoleAssistant BetaResponseItemAdditionalToolsRole = "assistant"

const BetaResponseItemAdditionalToolsRoleSystem BetaResponseItemAdditionalToolsRole = "system"

const BetaResponseItemAdditionalToolsRoleCritic BetaResponseItemAdditionalToolsRole = "critic"

const BetaResponseItemAdditionalToolsRoleDiscriminator BetaResponseItemAdditionalToolsRole = "discriminator"

const BetaResponseItemAdditionalToolsRoleDeveloper BetaResponseItemAdditionalToolsRole = "developer"

const BetaResponseItemAdditionalToolsRoleTool BetaResponseItemAdditionalToolsRole = "tool"

Tools [][BetaToolUnion](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))

The additional tool definitions made available at this item.

type BetaFunctionTool struct{…}

Name string

Parameters map[string, any]

Strict bool

Type Function

AllowedCallers []stringOptional

const BetaFunctionToolAllowedCallerDirect BetaFunctionToolAllowedCaller = "direct"

const BetaFunctionToolAllowedCallerProgrammatic BetaFunctionToolAllowedCaller = "programmatic"

DeferLoading boolOptional

Description stringOptional

OutputSchema map[string, any]Optional

type BetaFileSearchTool struct{…}

Type FileSearch

VectorStoreIDs []string

Filters BetaFileSearchToolFiltersUnionOptional

type BetaFileSearchToolFiltersComparisonFilter struct{…}

Key string

Type string

const BetaFileSearchToolFiltersComparisonFilterTypeEq BetaFileSearchToolFiltersComparisonFilterType = "eq"

const BetaFileSearchToolFiltersComparisonFilterTypeNe BetaFileSearchToolFiltersComparisonFilterType = "ne"

const BetaFileSearchToolFiltersComparisonFilterTypeGt BetaFileSearchToolFiltersComparisonFilterType = "gt"

const BetaFileSearchToolFiltersComparisonFilterTypeGte BetaFileSearchToolFiltersComparisonFilterType = "gte"

const BetaFileSearchToolFiltersComparisonFilterTypeLt BetaFileSearchToolFiltersComparisonFilterType = "lt"

const BetaFileSearchToolFiltersComparisonFilterTypeLte BetaFileSearchToolFiltersComparisonFilterType = "lte"

const BetaFileSearchToolFiltersComparisonFilterTypeIn BetaFileSearchToolFiltersComparisonFilterType = "in"

const BetaFileSearchToolFiltersComparisonFilterTypeNin BetaFileSearchToolFiltersComparisonFilterType = "nin"

Value BetaFileSearchToolFiltersComparisonFilterValueUnion

string

float64

bool

type BetaFileSearchToolFiltersComparisonFilterValueArray []BetaFileSearchToolFiltersComparisonFilterValueArrayItemUnion

string

float64

type BetaFileSearchToolFiltersCompoundFilter struct{…}

Filters []BetaFileSearchToolFiltersCompoundFilterFilter

type BetaFileSearchToolFiltersCompoundFilterFilter struct{…}

Key string

Type string

const BetaFileSearchToolFiltersCompoundFilterFilterTypeEq BetaFileSearchToolFiltersCompoundFilterFilterType = "eq"

const BetaFileSearchToolFiltersCompoundFilterFilterTypeNe BetaFileSearchToolFiltersCompoundFilterFilterType = "ne"

const BetaFileSearchToolFiltersCompoundFilterFilterTypeGt BetaFileSearchToolFiltersCompoundFilterFilterType = "gt"

const BetaFileSearchToolFiltersCompoundFilterFilterTypeGte BetaFileSearchToolFiltersCompoundFilterFilterType = "gte"

const BetaFileSearchToolFiltersCompoundFilterFilterTypeLt BetaFileSearchToolFiltersCompoundFilterFilterType = "lt"

const BetaFileSearchToolFiltersCompoundFilterFilterTypeLte BetaFileSearchToolFiltersCompoundFilterFilterType = "lte"

const BetaFileSearchToolFiltersCompoundFilterFilterTypeIn BetaFileSearchToolFiltersCompoundFilterFilterType = "in"

const BetaFileSearchToolFiltersCompoundFilterFilterTypeNin BetaFileSearchToolFiltersCompoundFilterFilterType = "nin"

Value BetaFileSearchToolFiltersCompoundFilterFilterValueUnion

string

float64

bool

type BetaFileSearchToolFiltersCompoundFilterFilterValueArray []BetaFileSearchToolFiltersCompoundFilterFilterValueArrayItemUnion

string

float64

Type string

const BetaFileSearchToolFiltersCompoundFilterTypeAnd BetaFileSearchToolFiltersCompoundFilterType = "and"

const BetaFileSearchToolFiltersCompoundFilterTypeOr BetaFileSearchToolFiltersCompoundFilterType = "or"

MaxNumResults int64Optional

RankingOptions BetaFileSearchToolRankingOptionsOptional

HybridSearch BetaFileSearchToolRankingOptionsHybridSearchOptional

EmbeddingWeight float64

TextWeight float64

Ranker stringOptional

const BetaFileSearchToolRankingOptionsRankerAuto BetaFileSearchToolRankingOptionsRanker = "auto"

const BetaFileSearchToolRankingOptionsRankerDefault2024\_11\_15 BetaFileSearchToolRankingOptionsRanker = "default-2024-11-15"

ScoreThreshold float64Optional

type BetaComputerTool struct{…}

Type Computer

type BetaComputerUsePreviewTool struct{…}

DisplayHeight int64

DisplayWidth int64

Environment BetaComputerUsePreviewToolEnvironment

const BetaComputerUsePreviewToolEnvironmentWindows BetaComputerUsePreviewToolEnvironment = "windows"

const BetaComputerUsePreviewToolEnvironmentMac BetaComputerUsePreviewToolEnvironment = "mac"

const BetaComputerUsePreviewToolEnvironmentLinux BetaComputerUsePreviewToolEnvironment = "linux"

const BetaComputerUsePreviewToolEnvironmentUbuntu BetaComputerUsePreviewToolEnvironment = "ubuntu"

const BetaComputerUsePreviewToolEnvironmentBrowser BetaComputerUsePreviewToolEnvironment = "browser"

Type ComputerUsePreview

type BetaWebSearchTool struct{…}

[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type BetaWebSearchToolType

const BetaWebSearchToolTypeWebSearch BetaWebSearchToolType = "web\_search"

const BetaWebSearchToolTypeWebSearch2025\_08\_26 BetaWebSearchToolType = "web\_search\_2025\_08\_26"

Filters BetaWebSearchToolFiltersOptional

AllowedDomains []stringOptional

SearchContextSize BetaWebSearchToolSearchContextSizeOptional

const BetaWebSearchToolSearchContextSizeLow BetaWebSearchToolSearchContextSize = "low"

const BetaWebSearchToolSearchContextSizeMedium BetaWebSearchToolSearchContextSize = "medium"

const BetaWebSearchToolSearchContextSizeHigh BetaWebSearchToolSearchContextSize = "high"

UserLocation BetaWebSearchToolUserLocationOptional

City stringOptional

Country stringOptional

Region stringOptional

Timezone stringOptional

Type stringOptional

type BetaToolMcp struct{…}

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

ServerLabel string

Type Mcp

AllowedCallers []stringOptional

const BetaToolMcpAllowedCallerDirect BetaToolMcpAllowedCaller = "direct"

const BetaToolMcpAllowedCallerProgrammatic BetaToolMcpAllowedCaller = "programmatic"

AllowedTools BetaToolMcpAllowedToolsUnionOptional

type BetaToolMcpAllowedToolsMcpAllowedTools []string

A string array of allowed tool names

type BetaToolMcpAllowedToolsMcpToolFilter struct{…}

ReadOnly boolOptional

ToolNames []stringOptional

Authorization stringOptional

ConnectorID stringOptional

about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

const BetaToolMcpConnectorIDConnectorDropbox BetaToolMcpConnectorID = "connector\_dropbox"

const BetaToolMcpConnectorIDConnectorGmail BetaToolMcpConnectorID = "connector\_gmail"

const BetaToolMcpConnectorIDConnectorGooglecalendar BetaToolMcpConnectorID = "connector\_googlecalendar"

const BetaToolMcpConnectorIDConnectorGoogledrive BetaToolMcpConnectorID = "connector\_googledrive"

const BetaToolMcpConnectorIDConnectorMicrosoftteams BetaToolMcpConnectorID = "connector\_microsoftteams"

const BetaToolMcpConnectorIDConnectorOutlookcalendar BetaToolMcpConnectorID = "connector\_outlookcalendar"

const BetaToolMcpConnectorIDConnectorOutlookemail BetaToolMcpConnectorID = "connector\_outlookemail"

const BetaToolMcpConnectorIDConnectorSharepoint BetaToolMcpConnectorID = "connector\_sharepoint"

DeferLoading boolOptional

Headers map[string, string]Optional

RequireApproval BetaToolMcpRequireApprovalUnionOptional

type BetaToolMcpRequireApprovalMcpToolApprovalFilter struct{…}

Always BetaToolMcpRequireApprovalMcpToolApprovalFilterAlwaysOptional

ReadOnly boolOptional

ToolNames []stringOptional

Never BetaToolMcpRequireApprovalMcpToolApprovalFilterNeverOptional

ReadOnly boolOptional

ToolNames []stringOptional

type BetaToolMcpRequireApprovalMcpToolApprovalSetting string

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

const BetaToolMcpRequireApprovalMcpToolApprovalSettingAlways BetaToolMcpRequireApprovalMcpToolApprovalSetting = "always"

const BetaToolMcpRequireApprovalMcpToolApprovalSettingNever BetaToolMcpRequireApprovalMcpToolApprovalSetting = "never"

ServerDescription stringOptional

ServerURL stringOptional

TunnelID stringOptional

type BetaToolCodeInterpreter struct{…}

A tool that runs Python code to help generate a response to a prompt.

Container BetaToolCodeInterpreterContainerUnion

string

type BetaToolCodeInterpreterContainerCodeInterpreterToolAuto struct{…}

Type Auto

FileIDs []stringOptional

MemoryLimit stringOptional

const BetaToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit1g BetaToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit = "1g"

const BetaToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit4g BetaToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit = "4g"

const BetaToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit16g BetaToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit = "16g"

const BetaToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit64g BetaToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit = "64g"

NetworkPolicy BetaToolCodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicyUnionOptional

type BetaContainerNetworkPolicyDisabled struct{…}

Type Disabled

type BetaContainerNetworkPolicyAllowlist struct{…}

AllowedDomains []string

Type Allowlist

DomainSecrets [][BetaContainerNetworkPolicyDomainSecret](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))Optional

Domain string

minLength1

Name string

minLength1

Value string

maxLength10485760

minLength1

Type CodeInterpreter

AllowedCallers []stringOptional

const BetaToolCodeInterpreterAllowedCallerDirect BetaToolCodeInterpreterAllowedCaller = "direct"

const BetaToolCodeInterpreterAllowedCallerProgrammatic BetaToolCodeInterpreterAllowedCaller = "programmatic"

type BetaToolProgrammaticToolCalling struct{…}

Type ProgrammaticToolCalling

The type of the tool. Always `programmatic_tool_calling`.

type BetaToolImageGeneration struct{…}

A tool that generates images using the GPT image models.

Type ImageGeneration

Action stringOptional

const BetaToolImageGenerationActionGenerate BetaToolImageGenerationAction = "generate"

const BetaToolImageGenerationActionEdit BetaToolImageGenerationAction = "edit"

const BetaToolImageGenerationActionAuto BetaToolImageGenerationAction = "auto"

Background stringOptional

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

const BetaToolImageGenerationBackgroundTransparent BetaToolImageGenerationBackground = "transparent"

const BetaToolImageGenerationBackgroundOpaque BetaToolImageGenerationBackground = "opaque"

const BetaToolImageGenerationBackgroundAuto BetaToolImageGenerationBackground = "auto"

InputFidelity stringOptional

const BetaToolImageGenerationInputFidelityHigh BetaToolImageGenerationInputFidelity = "high"

const BetaToolImageGenerationInputFidelityLow BetaToolImageGenerationInputFidelity = "low"

InputImageMask BetaToolImageGenerationInputImageMaskOptional

FileID stringOptional

ImageURL stringOptional

Model stringOptional

string

string

const BetaToolImageGenerationModelGPTImage1 BetaToolImageGenerationModel = "gpt-image-1"

const BetaToolImageGenerationModelGPTImage1Mini BetaToolImageGenerationModel = "gpt-image-1-mini"

const BetaToolImageGenerationModelGPTImage2 BetaToolImageGenerationModel = "gpt-image-2"

const BetaToolImageGenerationModelGPTImage2\_2026\_04\_21 BetaToolImageGenerationModel = "gpt-image-2-2026-04-21"

const BetaToolImageGenerationModelGPTImage1\_5 BetaToolImageGenerationModel = "gpt-image-1.5"

const BetaToolImageGenerationModelChatgptImageLatest BetaToolImageGenerationModel = "chatgpt-image-latest"

Moderation stringOptional

const BetaToolImageGenerationModerationAuto BetaToolImageGenerationModeration = "auto"

const BetaToolImageGenerationModerationLow BetaToolImageGenerationModeration = "low"

OutputCompression int64Optional

minimum0

maximum100

OutputFormat stringOptional

const BetaToolImageGenerationOutputFormatPNG BetaToolImageGenerationOutputFormat = "png"

const BetaToolImageGenerationOutputFormatWebP BetaToolImageGenerationOutputFormat = "webp"

const BetaToolImageGenerationOutputFormatJPEG BetaToolImageGenerationOutputFormat = "jpeg"

PartialImages int64Optional

minimum0

maximum3

Quality stringOptional

const BetaToolImageGenerationQualityLow BetaToolImageGenerationQuality = "low"

const BetaToolImageGenerationQualityMedium BetaToolImageGenerationQuality = "medium"

const BetaToolImageGenerationQualityHigh BetaToolImageGenerationQuality = "high"

const BetaToolImageGenerationQualityAuto BetaToolImageGenerationQuality = "auto"

Size stringOptional

string

string

const BetaToolImageGenerationSize1024x1024 BetaToolImageGenerationSize = "1024x1024"

const BetaToolImageGenerationSize1024x1536 BetaToolImageGenerationSize = "1024x1536"

const BetaToolImageGenerationSize1536x1024 BetaToolImageGenerationSize = "1536x1024"

const BetaToolImageGenerationSizeAuto BetaToolImageGenerationSize = "auto"

type BetaToolLocalShell struct{…}

A tool that allows the model to execute shell commands in a local environment.

Type LocalShell

The type of the local shell tool. Always `local_shell`.

type BetaFunctionShellTool struct{…}

Type Shell

AllowedCallers []stringOptional

const BetaFunctionShellToolAllowedCallerDirect BetaFunctionShellToolAllowedCaller = "direct"

const BetaFunctionShellToolAllowedCallerProgrammatic BetaFunctionShellToolAllowedCaller = "programmatic"

Environment BetaFunctionShellToolEnvironmentUnionOptional

type BetaContainerAuto struct{…}

Type ContainerAuto

FileIDs []stringOptional

MemoryLimit BetaContainerAutoMemoryLimitOptional

const BetaContainerAutoMemoryLimit1g BetaContainerAutoMemoryLimit = "1g"

const BetaContainerAutoMemoryLimit4g BetaContainerAutoMemoryLimit = "4g"

const BetaContainerAutoMemoryLimit16g BetaContainerAutoMemoryLimit = "16g"

const BetaContainerAutoMemoryLimit64g BetaContainerAutoMemoryLimit = "64g"

NetworkPolicy BetaContainerAutoNetworkPolicyUnionOptional

type BetaContainerNetworkPolicyDisabled struct{…}

Type Disabled

type BetaContainerNetworkPolicyAllowlist struct{…}

AllowedDomains []string

Type Allowlist

DomainSecrets [][BetaContainerNetworkPolicyDomainSecret](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))Optional

Domain string

minLength1

Name string

minLength1

Value string

maxLength10485760

minLength1

Skills []BetaContainerAutoSkillUnionOptional

type BetaSkillReference struct{…}

SkillID string

maxLength64

minLength1

Type SkillReference

Version stringOptional

type BetaInlineSkill struct{…}

Description string

Name string

Source [BetaInlineSkillSource](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

Data string

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

MediaType ApplicationZip

The media type of the inline skill payload. Must be `application/zip`.

Type Base64

The type of the inline skill source. Must be `base64`.

Type Inline

type BetaLocalEnvironment struct{…}

Type Local

Skills [][BetaLocalSkill](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))Optional

Description string

Name string

Path string

type BetaContainerReference struct{…}

ContainerID string

Type ContainerReference

type BetaCustomTool struct{…}

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

Name string

Type Custom

AllowedCallers []stringOptional

const BetaCustomToolAllowedCallerDirect BetaCustomToolAllowedCaller = "direct"

const BetaCustomToolAllowedCallerProgrammatic BetaCustomToolAllowedCaller = "programmatic"

DeferLoading boolOptional

Description stringOptional

Format BetaCustomToolFormatUnionOptional

type BetaCustomToolFormatText struct{…}

Unconstrained free-form text.

Type Text

Unconstrained text format. Always `text`.

type BetaCustomToolFormatGrammar struct{…}

Definition string

Syntax string

const BetaCustomToolFormatGrammarSyntaxLark BetaCustomToolFormatGrammarSyntax = "lark"

const BetaCustomToolFormatGrammarSyntaxRegex BetaCustomToolFormatGrammarSyntax = "regex"

Type Grammar

type BetaNamespaceTool struct{…}

Description string

minLength1

Name string

minLength1

Tools []BetaNamespaceToolToolUnion

type BetaNamespaceToolToolFunction struct{…}

Name string

maxLength128

minLength1

Type Function

AllowedCallers []stringOptional

const BetaNamespaceToolToolFunctionAllowedCallerDirect BetaNamespaceToolToolFunctionAllowedCaller = "direct"

const BetaNamespaceToolToolFunctionAllowedCallerProgrammatic BetaNamespaceToolToolFunctionAllowedCaller = "programmatic"

DeferLoading boolOptional

Description stringOptional

OutputSchema map[string, any]Optional

Parameters anyOptional

Strict boolOptional

type BetaCustomTool struct{…}

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

Name string

Type Custom

AllowedCallers []stringOptional

const BetaCustomToolAllowedCallerDirect BetaCustomToolAllowedCaller = "direct"

const BetaCustomToolAllowedCallerProgrammatic BetaCustomToolAllowedCaller = "programmatic"

DeferLoading boolOptional

Description stringOptional

Format BetaCustomToolFormatUnionOptional

type BetaCustomToolFormatText struct{…}

Unconstrained free-form text.

Type Text

Unconstrained text format. Always `text`.

type BetaCustomToolFormatGrammar struct{…}

Definition string

Syntax string

const BetaCustomToolFormatGrammarSyntaxLark BetaCustomToolFormatGrammarSyntax = "lark"

const BetaCustomToolFormatGrammarSyntaxRegex BetaCustomToolFormatGrammarSyntax = "regex"

Type Grammar

Type Namespace

type BetaToolSearchTool struct{…}

Type ToolSearch

Description stringOptional

Execution BetaToolSearchToolExecutionOptional

const BetaToolSearchToolExecutionServer BetaToolSearchToolExecution = "server"

const BetaToolSearchToolExecutionClient BetaToolSearchToolExecution = "client"

Parameters anyOptional

type BetaWebSearchPreviewTool struct{…}

Type BetaWebSearchPreviewToolType

const BetaWebSearchPreviewToolTypeWebSearchPreview BetaWebSearchPreviewToolType = "web\_search\_preview"

const BetaWebSearchPreviewToolTypeWebSearchPreview2025\_03\_11 BetaWebSearchPreviewToolType = "web\_search\_preview\_2025\_03\_11"

SearchContentTypes []stringOptional

const BetaWebSearchPreviewToolSearchContentTypeText BetaWebSearchPreviewToolSearchContentType = "text"

const BetaWebSearchPreviewToolSearchContentTypeImage BetaWebSearchPreviewToolSearchContentType = "image"

SearchContextSize BetaWebSearchPreviewToolSearchContextSizeOptional

const BetaWebSearchPreviewToolSearchContextSizeLow BetaWebSearchPreviewToolSearchContextSize = "low"

const BetaWebSearchPreviewToolSearchContextSizeMedium BetaWebSearchPreviewToolSearchContextSize = "medium"

const BetaWebSearchPreviewToolSearchContextSizeHigh BetaWebSearchPreviewToolSearchContextSize = "high"

UserLocation BetaWebSearchPreviewToolUserLocationOptional

Type Approximate

City stringOptional

Country stringOptional

Region stringOptional

Timezone stringOptional

type BetaApplyPatchTool struct{…}

Type ApplyPatch

AllowedCallers []stringOptional

const BetaApplyPatchToolAllowedCallerDirect BetaApplyPatchToolAllowedCaller = "direct"

const BetaApplyPatchToolAllowedCallerProgrammatic BetaApplyPatchToolAllowedCaller = "programmatic"

Type AdditionalTools

The type of the item. Always `additional_tools`.

Agent BetaResponseItemAdditionalToolsAgentOptional

AgentName string

type BetaResponseReasoningItem struct{…}

[managing context](https://platform.openai.com/docs/guides/conversation-state).

ID string

Summary []BetaResponseReasoningItemSummary

Text string

Type SummaryText

Type Reasoning

Agent BetaResponseReasoningItemAgentOptional

AgentName string

Content []BetaResponseReasoningItemContentOptional

Text string

Type ReasoningText

EncryptedContent stringOptional

Status BetaResponseReasoningItemStatusOptional

const BetaResponseReasoningItemStatusInProgress BetaResponseReasoningItemStatus = "in\_progress"

const BetaResponseReasoningItemStatusCompleted BetaResponseReasoningItemStatus = "completed"

const BetaResponseReasoningItemStatusIncomplete BetaResponseReasoningItemStatus = "incomplete"

type BetaResponseItemProgram struct{…}

ID string

The unique ID of the program item.

CallID string

Code string

Fingerprint string

Type Program

The type of the item. Always `program`.

Agent BetaResponseItemProgramAgentOptional

AgentName string

type BetaResponseItemProgramOutput struct{…}

ID string

The unique ID of the program output item.

CallID string

Result string

Status string

The terminal status of the program output item.

const BetaResponseItemProgramOutputStatusCompleted BetaResponseItemProgramOutputStatus = "completed"

const BetaResponseItemProgramOutputStatusIncomplete BetaResponseItemProgramOutputStatus = "incomplete"

Type ProgramOutput

The type of the item. Always `program_output`.

Agent BetaResponseItemProgramOutputAgentOptional

AgentName string

type BetaResponseCompactionItem struct{…}

A compaction item generated by the [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).

ID string

The unique ID of the compaction item.

EncryptedContent string

The encrypted content that was produced by compaction.

Type Compaction

Agent BetaResponseCompactionItemAgentOptional

AgentName string

CreatedBy stringOptional

The identifier of the actor that created the item.

type BetaResponseItemImageGenerationCall struct{…}

An image generation request made by the model.

ID string

Result string

Status string

const BetaResponseItemImageGenerationCallStatusInProgress BetaResponseItemImageGenerationCallStatus = "in\_progress"

const BetaResponseItemImageGenerationCallStatusCompleted BetaResponseItemImageGenerationCallStatus = "completed"

const BetaResponseItemImageGenerationCallStatusGenerating BetaResponseItemImageGenerationCallStatus = "generating"

const BetaResponseItemImageGenerationCallStatusFailed BetaResponseItemImageGenerationCallStatus = "failed"

Type ImageGenerationCall

Agent BetaResponseItemImageGenerationCallAgentOptional

AgentName string

type BetaResponseCodeInterpreterToolCall struct{…}

ID string

Code string

ContainerID string

Outputs []BetaResponseCodeInterpreterToolCallOutputUnion

type BetaResponseCodeInterpreterToolCallOutputLogs struct{…}

Logs string

Type Logs

type BetaResponseCodeInterpreterToolCallOutputImage struct{…}

Type Image

URL string

Status BetaResponseCodeInterpreterToolCallStatus

const BetaResponseCodeInterpreterToolCallStatusInProgress BetaResponseCodeInterpreterToolCallStatus = "in\_progress"

const BetaResponseCodeInterpreterToolCallStatusCompleted BetaResponseCodeInterpreterToolCallStatus = "completed"

const BetaResponseCodeInterpreterToolCallStatusIncomplete BetaResponseCodeInterpreterToolCallStatus = "incomplete"

const BetaResponseCodeInterpreterToolCallStatusInterpreting BetaResponseCodeInterpreterToolCallStatus = "interpreting"

const BetaResponseCodeInterpreterToolCallStatusFailed BetaResponseCodeInterpreterToolCallStatus = "failed"

Type CodeInterpreterCall

Agent BetaResponseCodeInterpreterToolCallAgentOptional

AgentName string

type BetaResponseItemLocalShellCall struct{…}

A tool call to run a command on the local shell.

ID string

Action BetaResponseItemLocalShellCallAction

Command []string

Env map[string, string]

Type Exec

TimeoutMs int64Optional

User stringOptional

WorkingDirectory stringOptional

CallID string

Status string

const BetaResponseItemLocalShellCallStatusInProgress BetaResponseItemLocalShellCallStatus = "in\_progress"

const BetaResponseItemLocalShellCallStatusCompleted BetaResponseItemLocalShellCallStatus = "completed"

const BetaResponseItemLocalShellCallStatusIncomplete BetaResponseItemLocalShellCallStatus = "incomplete"

Type LocalShellCall

Agent BetaResponseItemLocalShellCallAgentOptional

AgentName string

type BetaResponseItemLocalShellCallOutput struct{…}

The output of a local shell tool call.

ID string

Output string

Type LocalShellCallOutput

Agent BetaResponseItemLocalShellCallOutputAgentOptional

AgentName string

Status stringOptional

const BetaResponseItemLocalShellCallOutputStatusInProgress BetaResponseItemLocalShellCallOutputStatus = "in\_progress"

const BetaResponseItemLocalShellCallOutputStatusCompleted BetaResponseItemLocalShellCallOutputStatus = "completed"

const BetaResponseItemLocalShellCallOutputStatusIncomplete BetaResponseItemLocalShellCallOutputStatus = "incomplete"

type BetaResponseFunctionShellToolCall struct{…}

A tool call that executes one or more shell commands in a managed environment.

ID string

Action BetaResponseFunctionShellToolCallAction

Commands []string

MaxOutputLength int64

Optional maximum number of characters to return from each command.

TimeoutMs int64

Optional timeout in milliseconds for the commands.

CallID string

Environment BetaResponseFunctionShellToolCallEnvironmentUnion

Represents the use of a local environment to perform shell actions.

type BetaResponseLocalEnvironment struct{…}

Represents the use of a local environment to perform shell actions.

Type Local

The environment type. Always `local`.

type BetaResponseContainerReference struct{…}

Represents a container created with /v1/containers.

ContainerID string

Type ContainerReference

The environment type. Always `container_reference`.

Status BetaResponseFunctionShellToolCallStatus

const BetaResponseFunctionShellToolCallStatusInProgress BetaResponseFunctionShellToolCallStatus = "in\_progress"

const BetaResponseFunctionShellToolCallStatusCompleted BetaResponseFunctionShellToolCallStatus = "completed"

const BetaResponseFunctionShellToolCallStatusIncomplete BetaResponseFunctionShellToolCallStatus = "incomplete"

Type ShellCall

Agent BetaResponseFunctionShellToolCallAgentOptional

AgentName string

Caller BetaResponseFunctionShellToolCallCallerUnionOptional

type BetaResponseFunctionShellToolCallCallerDirect struct{…}

Type Direct

type BetaResponseFunctionShellToolCallCallerProgram struct{…}

CallerID string

Type Program

CreatedBy stringOptional

The ID of the entity that created this tool call.

type BetaResponseFunctionShellToolCallOutput struct{…}

The output of a shell tool call that was emitted.

ID string

The unique ID of the shell call output. Populated when this item is returned via API.

CallID string

MaxOutputLength int64

The maximum length of the shell command output. This is generated by the model and should be passed back with the raw output.

Output []BetaResponseFunctionShellToolCallOutputOutput

An array of shell call output contents

Outcome BetaResponseFunctionShellToolCallOutputOutputOutcomeUnion

Represents either an exit outcome (with an exit code) or a timeout outcome for a shell call output chunk.

type BetaResponseFunctionShellToolCallOutputOutputOutcomeTimeout struct{…}

Indicates that the shell call exceeded its configured time limit.

Type Timeout

The outcome type. Always `timeout`.

type BetaResponseFunctionShellToolCallOutputOutputOutcomeExit struct{…}

ExitCode int64

Exit code from the shell process.

Type Exit

Stderr string

The standard error output that was captured.

Stdout string

The standard output that was captured.

CreatedBy stringOptional

The identifier of the actor that created the item.

Status BetaResponseFunctionShellToolCallOutputStatus

The status of the shell call output. One of `in_progress`, `completed`, or `incomplete`.

const BetaResponseFunctionShellToolCallOutputStatusInProgress BetaResponseFunctionShellToolCallOutputStatus = "in\_progress"

const BetaResponseFunctionShellToolCallOutputStatusCompleted BetaResponseFunctionShellToolCallOutputStatus = "completed"

const BetaResponseFunctionShellToolCallOutputStatusIncomplete BetaResponseFunctionShellToolCallOutputStatus = "incomplete"

Type ShellCallOutput

The type of the shell call output. Always `shell_call_output`.

Agent BetaResponseFunctionShellToolCallOutputAgentOptional

AgentName string

Caller BetaResponseFunctionShellToolCallOutputCallerUnionOptional

type BetaResponseFunctionShellToolCallOutputCallerDirect struct{…}

Type Direct

type BetaResponseFunctionShellToolCallOutputCallerProgram struct{…}

CallerID string

Type Program

CreatedBy stringOptional

The identifier of the actor that created the item.

type BetaResponseApplyPatchToolCall struct{…}

A tool call that applies file diffs by creating, deleting, or updating files.

ID string

CallID string

Operation BetaResponseApplyPatchToolCallOperationUnion

One of the create\_file, delete\_file, or update\_file operations applied via apply\_patch.

type BetaResponseApplyPatchToolCallOperationCreateFile struct{…}

Instruction describing how to create a file via the apply\_patch tool.

Diff string

Diff to apply.

Path string

Path of the file to create.

Type CreateFile

Create a new file with the provided diff.

type BetaResponseApplyPatchToolCallOperationDeleteFile struct{…}

Instruction describing how to delete a file via the apply\_patch tool.

Path string

Path of the file to delete.

Type DeleteFile

Delete the specified file.

type BetaResponseApplyPatchToolCallOperationUpdateFile struct{…}

Instruction describing how to update a file via the apply\_patch tool.

Diff string

Diff to apply.

Path string

Path of the file to update.

Type UpdateFile

Update an existing file with the provided diff.

Status BetaResponseApplyPatchToolCallStatus

const BetaResponseApplyPatchToolCallStatusInProgress BetaResponseApplyPatchToolCallStatus = "in\_progress"

const BetaResponseApplyPatchToolCallStatusCompleted BetaResponseApplyPatchToolCallStatus = "completed"

Type ApplyPatchCall

Agent BetaResponseApplyPatchToolCallAgentOptional

AgentName string

Caller BetaResponseApplyPatchToolCallCallerUnionOptional

type BetaResponseApplyPatchToolCallCallerDirect struct{…}

Type Direct

type BetaResponseApplyPatchToolCallCallerProgram struct{…}

CallerID string

Type Program

CreatedBy stringOptional

The ID of the entity that created this tool call.

type BetaResponseApplyPatchToolCallOutput struct{…}

The output emitted by an apply patch tool call.

ID string

CallID string

Status BetaResponseApplyPatchToolCallOutputStatus

const BetaResponseApplyPatchToolCallOutputStatusCompleted BetaResponseApplyPatchToolCallOutputStatus = "completed"

const BetaResponseApplyPatchToolCallOutputStatusFailed BetaResponseApplyPatchToolCallOutputStatus = "failed"

Type ApplyPatchCallOutput

Agent BetaResponseApplyPatchToolCallOutputAgentOptional

AgentName string

Caller BetaResponseApplyPatchToolCallOutputCallerUnionOptional

type BetaResponseApplyPatchToolCallOutputCallerDirect struct{…}

Type Direct

type BetaResponseApplyPatchToolCallOutputCallerProgram struct{…}

CallerID string

Type Program

CreatedBy stringOptional

The ID of the entity that created this tool call output.

Output stringOptional

Optional textual output returned by the apply patch tool.

type BetaResponseItemMcpListTools struct{…}

A list of tools available on an MCP server.

ID string

ServerLabel string

Tools []BetaResponseItemMcpListToolsTool

InputSchema any

Name string

Annotations anyOptional

Description stringOptional

Type McpListTools

Agent BetaResponseItemMcpListToolsAgentOptional

AgentName string

Error stringOptional

type BetaResponseItemMcpApprovalRequest struct{…}

A request for human approval of a tool invocation.

ID string

Arguments string

Name string

ServerLabel string

Type McpApprovalRequest

Agent BetaResponseItemMcpApprovalRequestAgentOptional

AgentName string

type BetaResponseItemMcpApprovalResponse struct{…}

A response to an MCP approval request.

ID string

ApprovalRequestID string

Approve bool

Type McpApprovalResponse

Agent BetaResponseItemMcpApprovalResponseAgentOptional

AgentName string

Reason stringOptional

type BetaResponseItemMcpCall struct{…}

An invocation of a tool on an MCP server.

ID string

Arguments string

Name string

ServerLabel string

Type McpCall

Agent BetaResponseItemMcpCallAgentOptional

AgentName string

ApprovalRequestID stringOptional

Error stringOptional

Output stringOptional

Status stringOptional

const BetaResponseItemMcpCallStatusInProgress BetaResponseItemMcpCallStatus = "in\_progress"

const BetaResponseItemMcpCallStatusCompleted BetaResponseItemMcpCallStatus = "completed"

const BetaResponseItemMcpCallStatusIncomplete BetaResponseItemMcpCallStatus = "incomplete"

const BetaResponseItemMcpCallStatusCalling BetaResponseItemMcpCallStatus = "calling"

const BetaResponseItemMcpCallStatusFailed BetaResponseItemMcpCallStatus = "failed"

type BetaResponseCustomToolCallItem struct{…}

ID string

The unique ID of the custom tool call item.

Status string

const BetaResponseCustomToolCallItemStatusInProgress BetaResponseCustomToolCallItemStatus = "in\_progress"

const BetaResponseCustomToolCallItemStatusCompleted BetaResponseCustomToolCallItemStatus = "completed"

const BetaResponseCustomToolCallItemStatusIncomplete BetaResponseCustomToolCallItemStatus = "incomplete"

CreatedBy stringOptional

The identifier of the actor that created the item.

type BetaResponseCustomToolCallOutputItem struct{…}

ID string

The unique ID of the custom tool call output item.

Status string

const BetaResponseCustomToolCallOutputItemStatusInProgress BetaResponseCustomToolCallOutputItemStatus = "in\_progress"

const BetaResponseCustomToolCallOutputItemStatusCompleted BetaResponseCustomToolCallOutputItemStatus = "completed"

const BetaResponseCustomToolCallOutputItemStatusIncomplete BetaResponseCustomToolCallOutputItemStatus = "incomplete"

CreatedBy stringOptional

The identifier of the actor that created the item.

### List input items

Go

package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  page, err := client.Beta.Responses.InputItems.List(
    context.TODO(),
    "response_id",
    openai.BetaResponseInputItemListParams{

    },
  )
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", page)

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
