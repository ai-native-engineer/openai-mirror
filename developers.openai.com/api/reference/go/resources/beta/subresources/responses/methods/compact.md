<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/responses/methods/compact/ -->

[API Reference](/api/reference/go)

[Beta](/api/reference/go/resources/beta)

[Responses](/api/reference/go/resources/beta/subresources/responses)

# Compact a response

client.Beta.Responses.Compact(ctx, params) (\*[BetaCompactedResponse](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_compacted_response%20%3E%20(schema)), error)

POST/responses/compact

Compact a conversation. Returns a compacted response object.

Learn when and how to compact long-running conversations in the [conversation state guide](https://platform.openai.com/docs/guides/conversation-state#managing-the-context-window). For ZDR-compatible compaction details, see [Compaction (advanced)](https://platform.openai.com/docs/guides/conversation-state#compaction-advanced).

##### ParametersExpand Collapse

params BetaResponseCompactParams

Model param.Field[BetaResponseCompactParamsModel]

Body param: Model ID used to generate the response, like `gpt-5` or `o3`. OpenAI offers a wide range of models with different capabilities, performance characteristics, and price points. Refer to the [model guide](https://platform.openai.com/docs/models) to browse and compare available models.

type BetaResponseCompactParamsModel string

Model ID used to generate the response, like `gpt-5` or `o3`. OpenAI offers a wide range of models with different capabilities, performance characteristics, and price points. Refer to the [model guide](https://platform.openai.com/docs/models) to browse and compare available models.

const BetaResponseCompactParamsModelGPT5\_6Sol BetaResponseCompactParamsModel = "gpt-5.6-sol"

const BetaResponseCompactParamsModelGPT5\_6Terra BetaResponseCompactParamsModel = "gpt-5.6-terra"

const BetaResponseCompactParamsModelGPT5\_6Luna BetaResponseCompactParamsModel = "gpt-5.6-luna"

const BetaResponseCompactParamsModelGPT5\_4 BetaResponseCompactParamsModel = "gpt-5.4"

const BetaResponseCompactParamsModelGPT5\_4Mini BetaResponseCompactParamsModel = "gpt-5.4-mini"

const BetaResponseCompactParamsModelGPT5\_4Nano BetaResponseCompactParamsModel = "gpt-5.4-nano"

const BetaResponseCompactParamsModelGPT5\_4Mini2026\_03\_17 BetaResponseCompactParamsModel = "gpt-5.4-mini-2026-03-17"

const BetaResponseCompactParamsModelGPT5\_4Nano2026\_03\_17 BetaResponseCompactParamsModel = "gpt-5.4-nano-2026-03-17"

const BetaResponseCompactParamsModelGPT5\_3ChatLatest BetaResponseCompactParamsModel = "gpt-5.3-chat-latest"

const BetaResponseCompactParamsModelGPT5\_2 BetaResponseCompactParamsModel = "gpt-5.2"

const BetaResponseCompactParamsModelGPT5\_2\_2025\_12\_11 BetaResponseCompactParamsModel = "gpt-5.2-2025-12-11"

const BetaResponseCompactParamsModelGPT5\_2ChatLatest BetaResponseCompactParamsModel = "gpt-5.2-chat-latest"

const BetaResponseCompactParamsModelGPT5\_2Pro BetaResponseCompactParamsModel = "gpt-5.2-pro"

const BetaResponseCompactParamsModelGPT5\_2Pro2025\_12\_11 BetaResponseCompactParamsModel = "gpt-5.2-pro-2025-12-11"

const BetaResponseCompactParamsModelGPT5\_1 BetaResponseCompactParamsModel = "gpt-5.1"

const BetaResponseCompactParamsModelGPT5\_1\_2025\_11\_13 BetaResponseCompactParamsModel = "gpt-5.1-2025-11-13"

const BetaResponseCompactParamsModelGPT5\_1Codex BetaResponseCompactParamsModel = "gpt-5.1-codex"

const BetaResponseCompactParamsModelGPT5\_1Mini BetaResponseCompactParamsModel = "gpt-5.1-mini"

const BetaResponseCompactParamsModelGPT5\_1ChatLatest BetaResponseCompactParamsModel = "gpt-5.1-chat-latest"

const BetaResponseCompactParamsModelGPT5 BetaResponseCompactParamsModel = "gpt-5"

const BetaResponseCompactParamsModelGPT5Mini BetaResponseCompactParamsModel = "gpt-5-mini"

const BetaResponseCompactParamsModelGPT5Nano BetaResponseCompactParamsModel = "gpt-5-nano"

const BetaResponseCompactParamsModelGPT5\_2025\_08\_07 BetaResponseCompactParamsModel = "gpt-5-2025-08-07"

const BetaResponseCompactParamsModelGPT5Mini2025\_08\_07 BetaResponseCompactParamsModel = "gpt-5-mini-2025-08-07"

const BetaResponseCompactParamsModelGPT5Nano2025\_08\_07 BetaResponseCompactParamsModel = "gpt-5-nano-2025-08-07"

const BetaResponseCompactParamsModelGPT5ChatLatest BetaResponseCompactParamsModel = "gpt-5-chat-latest"

const BetaResponseCompactParamsModelGPT4\_1 BetaResponseCompactParamsModel = "gpt-4.1"

const BetaResponseCompactParamsModelGPT4\_1Mini BetaResponseCompactParamsModel = "gpt-4.1-mini"

const BetaResponseCompactParamsModelGPT4\_1Nano BetaResponseCompactParamsModel = "gpt-4.1-nano"

const BetaResponseCompactParamsModelGPT4\_1\_2025\_04\_14 BetaResponseCompactParamsModel = "gpt-4.1-2025-04-14"

const BetaResponseCompactParamsModelGPT4\_1Mini2025\_04\_14 BetaResponseCompactParamsModel = "gpt-4.1-mini-2025-04-14"

const BetaResponseCompactParamsModelGPT4\_1Nano2025\_04\_14 BetaResponseCompactParamsModel = "gpt-4.1-nano-2025-04-14"

const BetaResponseCompactParamsModelO4Mini BetaResponseCompactParamsModel = "o4-mini"

const BetaResponseCompactParamsModelO4Mini2025\_04\_16 BetaResponseCompactParamsModel = "o4-mini-2025-04-16"

const BetaResponseCompactParamsModelO3 BetaResponseCompactParamsModel = "o3"

const BetaResponseCompactParamsModelO3\_2025\_04\_16 BetaResponseCompactParamsModel = "o3-2025-04-16"

const BetaResponseCompactParamsModelO3Mini BetaResponseCompactParamsModel = "o3-mini"

const BetaResponseCompactParamsModelO3Mini2025\_01\_31 BetaResponseCompactParamsModel = "o3-mini-2025-01-31"

const BetaResponseCompactParamsModelO1 BetaResponseCompactParamsModel = "o1"

const BetaResponseCompactParamsModelO1\_2024\_12\_17 BetaResponseCompactParamsModel = "o1-2024-12-17"

const BetaResponseCompactParamsModelO1Preview BetaResponseCompactParamsModel = "o1-preview"

const BetaResponseCompactParamsModelO1Preview2024\_09\_12 BetaResponseCompactParamsModel = "o1-preview-2024-09-12"

const BetaResponseCompactParamsModelO1Mini BetaResponseCompactParamsModel = "o1-mini"

const BetaResponseCompactParamsModelO1Mini2024\_09\_12 BetaResponseCompactParamsModel = "o1-mini-2024-09-12"

const BetaResponseCompactParamsModelGPT4o BetaResponseCompactParamsModel = "gpt-4o"

const BetaResponseCompactParamsModelGPT4o2024\_11\_20 BetaResponseCompactParamsModel = "gpt-4o-2024-11-20"

const BetaResponseCompactParamsModelGPT4o2024\_08\_06 BetaResponseCompactParamsModel = "gpt-4o-2024-08-06"

const BetaResponseCompactParamsModelGPT4o2024\_05\_13 BetaResponseCompactParamsModel = "gpt-4o-2024-05-13"

const BetaResponseCompactParamsModelGPT4oAudioPreview BetaResponseCompactParamsModel = "gpt-4o-audio-preview"

const BetaResponseCompactParamsModelGPT4oAudioPreview2024\_10\_01 BetaResponseCompactParamsModel = "gpt-4o-audio-preview-2024-10-01"

const BetaResponseCompactParamsModelGPT4oAudioPreview2024\_12\_17 BetaResponseCompactParamsModel = "gpt-4o-audio-preview-2024-12-17"

const BetaResponseCompactParamsModelGPT4oAudioPreview2025\_06\_03 BetaResponseCompactParamsModel = "gpt-4o-audio-preview-2025-06-03"

const BetaResponseCompactParamsModelGPT4oMiniAudioPreview BetaResponseCompactParamsModel = "gpt-4o-mini-audio-preview"

const BetaResponseCompactParamsModelGPT4oMiniAudioPreview2024\_12\_17 BetaResponseCompactParamsModel = "gpt-4o-mini-audio-preview-2024-12-17"

const BetaResponseCompactParamsModelGPT4oSearchPreview BetaResponseCompactParamsModel = "gpt-4o-search-preview"

const BetaResponseCompactParamsModelGPT4oMiniSearchPreview BetaResponseCompactParamsModel = "gpt-4o-mini-search-preview"

const BetaResponseCompactParamsModelGPT4oSearchPreview2025\_03\_11 BetaResponseCompactParamsModel = "gpt-4o-search-preview-2025-03-11"

const BetaResponseCompactParamsModelGPT4oMiniSearchPreview2025\_03\_11 BetaResponseCompactParamsModel = "gpt-4o-mini-search-preview-2025-03-11"

const BetaResponseCompactParamsModelChatgpt4oLatest BetaResponseCompactParamsModel = "chatgpt-4o-latest"

const BetaResponseCompactParamsModelCodexMiniLatest BetaResponseCompactParamsModel = "codex-mini-latest"

const BetaResponseCompactParamsModelGPT4oMini BetaResponseCompactParamsModel = "gpt-4o-mini"

const BetaResponseCompactParamsModelGPT4oMini2024\_07\_18 BetaResponseCompactParamsModel = "gpt-4o-mini-2024-07-18"

const BetaResponseCompactParamsModelGPT4Turbo BetaResponseCompactParamsModel = "gpt-4-turbo"

const BetaResponseCompactParamsModelGPT4Turbo2024\_04\_09 BetaResponseCompactParamsModel = "gpt-4-turbo-2024-04-09"

const BetaResponseCompactParamsModelGPT4\_0125Preview BetaResponseCompactParamsModel = "gpt-4-0125-preview"

const BetaResponseCompactParamsModelGPT4TurboPreview BetaResponseCompactParamsModel = "gpt-4-turbo-preview"

const BetaResponseCompactParamsModelGPT4\_1106Preview BetaResponseCompactParamsModel = "gpt-4-1106-preview"

const BetaResponseCompactParamsModelGPT4VisionPreview BetaResponseCompactParamsModel = "gpt-4-vision-preview"

const BetaResponseCompactParamsModelGPT4 BetaResponseCompactParamsModel = "gpt-4"

const BetaResponseCompactParamsModelGPT4\_0314 BetaResponseCompactParamsModel = "gpt-4-0314"

const BetaResponseCompactParamsModelGPT4\_0613 BetaResponseCompactParamsModel = "gpt-4-0613"

const BetaResponseCompactParamsModelGPT4\_32k BetaResponseCompactParamsModel = "gpt-4-32k"

const BetaResponseCompactParamsModelGPT4\_32k0314 BetaResponseCompactParamsModel = "gpt-4-32k-0314"

const BetaResponseCompactParamsModelGPT4\_32k0613 BetaResponseCompactParamsModel = "gpt-4-32k-0613"

const BetaResponseCompactParamsModelGPT3\_5Turbo BetaResponseCompactParamsModel = "gpt-3.5-turbo"

const BetaResponseCompactParamsModelGPT3\_5Turbo16k BetaResponseCompactParamsModel = "gpt-3.5-turbo-16k"

const BetaResponseCompactParamsModelGPT3\_5Turbo0301 BetaResponseCompactParamsModel = "gpt-3.5-turbo-0301"

const BetaResponseCompactParamsModelGPT3\_5Turbo0613 BetaResponseCompactParamsModel = "gpt-3.5-turbo-0613"

const BetaResponseCompactParamsModelGPT3\_5Turbo1106 BetaResponseCompactParamsModel = "gpt-3.5-turbo-1106"

const BetaResponseCompactParamsModelGPT3\_5Turbo0125 BetaResponseCompactParamsModel = "gpt-3.5-turbo-0125"

const BetaResponseCompactParamsModelGPT3\_5Turbo16k0613 BetaResponseCompactParamsModel = "gpt-3.5-turbo-16k-0613"

const BetaResponseCompactParamsModelO1Pro BetaResponseCompactParamsModel = "o1-pro"

const BetaResponseCompactParamsModelO1Pro2025\_03\_19 BetaResponseCompactParamsModel = "o1-pro-2025-03-19"

const BetaResponseCompactParamsModelO3Pro BetaResponseCompactParamsModel = "o3-pro"

const BetaResponseCompactParamsModelO3Pro2025\_06\_10 BetaResponseCompactParamsModel = "o3-pro-2025-06-10"

const BetaResponseCompactParamsModelO3DeepResearch BetaResponseCompactParamsModel = "o3-deep-research"

const BetaResponseCompactParamsModelO3DeepResearch2025\_06\_26 BetaResponseCompactParamsModel = "o3-deep-research-2025-06-26"

const BetaResponseCompactParamsModelO4MiniDeepResearch BetaResponseCompactParamsModel = "o4-mini-deep-research"

const BetaResponseCompactParamsModelO4MiniDeepResearch2025\_06\_26 BetaResponseCompactParamsModel = "o4-mini-deep-research-2025-06-26"

const BetaResponseCompactParamsModelComputerUsePreview BetaResponseCompactParamsModel = "computer-use-preview"

const BetaResponseCompactParamsModelComputerUsePreview2025\_03\_11 BetaResponseCompactParamsModel = "computer-use-preview-2025-03-11"

const BetaResponseCompactParamsModelGPT5Codex BetaResponseCompactParamsModel = "gpt-5-codex"

const BetaResponseCompactParamsModelGPT5Pro BetaResponseCompactParamsModel = "gpt-5-pro"

const BetaResponseCompactParamsModelGPT5Pro2025\_10\_06 BetaResponseCompactParamsModel = "gpt-5-pro-2025-10-06"

const BetaResponseCompactParamsModelGPT5\_1CodexMax BetaResponseCompactParamsModel = "gpt-5.1-codex-max"

string

Input param.Field[[BetaResponseCompactParamsInputUnion](/api/reference/go/resources/beta/subresources/responses/methods/compact#(resource)%20beta.responses%20%3E%20(method)%20compact%20%3E%20(params)%20default%20%3E%20(param)%20input%20%3E%20(schema))]Optional

Body param: Text, image, or file inputs to the model, used to generate a response

string

type BetaResponseCompactParamsInputArray [][BetaResponseInputItemUnion](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_item%20%3E%20(schema))

A list of one or many input items to the model, containing different content types.

type BetaEasyInputMessage struct{…}

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

Content BetaEasyInputMessageContentUnion

Text, image, or audio input to the model, used to generate a response.
Can also contain previous assistant responses.

string

type BetaResponseInputMessageContentList [][BetaResponseInputContentUnion](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_content%20%3E%20(schema))

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

Role BetaEasyInputMessageRole

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

const BetaEasyInputMessageRoleUser BetaEasyInputMessageRole = "user"

const BetaEasyInputMessageRoleAssistant BetaEasyInputMessageRole = "assistant"

const BetaEasyInputMessageRoleSystem BetaEasyInputMessageRole = "system"

const BetaEasyInputMessageRoleDeveloper BetaEasyInputMessageRole = "developer"

Phase BetaEasyInputMessagePhaseOptional

const BetaEasyInputMessagePhaseCommentary BetaEasyInputMessagePhase = "commentary"

const BetaEasyInputMessagePhaseFinalAnswer BetaEasyInputMessagePhase = "final\_answer"

Type BetaEasyInputMessageTypeOptional

The type of the message input. Always `message`.

type BetaResponseInputItemMessage struct{…}

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role.

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

Role string

const BetaResponseInputItemMessageRoleUser BetaResponseInputItemMessageRole = "user"

const BetaResponseInputItemMessageRoleSystem BetaResponseInputItemMessageRole = "system"

const BetaResponseInputItemMessageRoleDeveloper BetaResponseInputItemMessageRole = "developer"

Agent BetaResponseInputItemMessageAgentOptional

AgentName string

Status stringOptional

const BetaResponseInputItemMessageStatusInProgress BetaResponseInputItemMessageStatus = "in\_progress"

const BetaResponseInputItemMessageStatusCompleted BetaResponseInputItemMessageStatus = "completed"

const BetaResponseInputItemMessageStatusIncomplete BetaResponseInputItemMessageStatus = "incomplete"

Type stringOptional

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

type BetaResponseInputItemComputerCallOutput struct{…}

The output of a computer tool call.

CallID string

maxLength64

minLength1

Output [BetaResponseComputerToolCallOutputScreenshot](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_computer_tool_call_output_screenshot%20%3E%20(schema))

Type ComputerScreenshot

Specifies the event type. For a computer screenshot, this property is
always set to `computer_screenshot`.

FileID stringOptional

ImageURL stringOptional

Type ComputerCallOutput

ID stringOptional

The ID of the computer tool call output.

AcknowledgedSafetyChecks []BetaResponseInputItemComputerCallOutputAcknowledgedSafetyCheckOptional

The safety checks reported by the API that have been acknowledged by the developer.

ID string

Code stringOptional

Message stringOptional

Agent BetaResponseInputItemComputerCallOutputAgentOptional

AgentName string

Status stringOptional

The status of the message input. One of `in_progress`, `completed`, or `incomplete`. Populated when input items are returned via API.

const BetaResponseInputItemComputerCallOutputStatusInProgress BetaResponseInputItemComputerCallOutputStatus = "in\_progress"

const BetaResponseInputItemComputerCallOutputStatusCompleted BetaResponseInputItemComputerCallOutputStatus = "completed"

const BetaResponseInputItemComputerCallOutputStatusIncomplete BetaResponseInputItemComputerCallOutputStatus = "incomplete"

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

type BetaResponseFunctionToolCall struct{…}

[function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.

Arguments string

A JSON string of the arguments to pass to the function.

CallID string

Name string

The name of the function to run.

Type FunctionCall

The type of the function tool call. Always `function_call`.

ID stringOptional

Agent BetaResponseFunctionToolCallAgentOptional

AgentName string

Caller BetaResponseFunctionToolCallCallerUnionOptional

type BetaResponseFunctionToolCallCallerDirect struct{…}

Type Direct

type BetaResponseFunctionToolCallCallerProgram struct{…}

CallerID string

Type Program

Namespace stringOptional

The namespace of the function to run.

Status BetaResponseFunctionToolCallStatusOptional

const BetaResponseFunctionToolCallStatusInProgress BetaResponseFunctionToolCallStatus = "in\_progress"

const BetaResponseFunctionToolCallStatusCompleted BetaResponseFunctionToolCallStatus = "completed"

const BetaResponseFunctionToolCallStatusIncomplete BetaResponseFunctionToolCallStatus = "incomplete"

type BetaResponseInputItemFunctionCallOutput struct{…}

The output of a function tool call.

CallID string

maxLength64

minLength1

Output BetaResponseInputItemFunctionCallOutputOutputUnion

Text, image, or file output of the function tool call.

string

type BetaResponseFunctionCallOutputItemList [][BetaResponseFunctionCallOutputItemUnion](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_call_output_item%20%3E%20(schema))

An array of content outputs (text, image, file) for the function tool call.

type BetaResponseInputTextContent struct{…}

Text string

maxLength10485760

Type InputText

PromptCacheBreakpoint BetaResponseInputTextContentPromptCacheBreakpointOptional

Mode Explicit

type BetaResponseInputImageContent struct{…}

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision)

Type InputImage

Detail BetaResponseInputImageContentDetailOptional

const BetaResponseInputImageContentDetailLow BetaResponseInputImageContentDetail = "low"

const BetaResponseInputImageContentDetailHigh BetaResponseInputImageContentDetail = "high"

const BetaResponseInputImageContentDetailAuto BetaResponseInputImageContentDetail = "auto"

const BetaResponseInputImageContentDetailOriginal BetaResponseInputImageContentDetail = "original"

FileID stringOptional

ImageURL stringOptional

maxLength20971520

PromptCacheBreakpoint BetaResponseInputImageContentPromptCacheBreakpointOptional

Mode Explicit

type BetaResponseInputFileContent struct{…}

Type InputFile

Detail BetaResponseInputFileContentDetailOptional

const BetaResponseInputFileContentDetailAuto BetaResponseInputFileContentDetail = "auto"

const BetaResponseInputFileContentDetailLow BetaResponseInputFileContentDetail = "low"

const BetaResponseInputFileContentDetailHigh BetaResponseInputFileContentDetail = "high"

FileData stringOptional

The base64-encoded data of the file to be sent to the model.

maxLength73400320

FileID stringOptional

FileURL stringOptional

Filename stringOptional

PromptCacheBreakpoint BetaResponseInputFileContentPromptCacheBreakpointOptional

Mode Explicit

Type FunctionCallOutput

ID stringOptional

The unique ID of the function tool call output. Populated when this item is returned via API.

Agent BetaResponseInputItemFunctionCallOutputAgentOptional

AgentName string

Caller BetaResponseInputItemFunctionCallOutputCallerUnionOptional

type BetaResponseInputItemFunctionCallOutputCallerDirect struct{…}

Type Direct

The caller type. Always `direct`.

type BetaResponseInputItemFunctionCallOutputCallerProgram struct{…}

CallerID string

maxLength64

minLength1

Type Program

Status stringOptional

The status of the item. One of `in_progress`, `completed`, or `incomplete`. Populated when items are returned via API.

const BetaResponseInputItemFunctionCallOutputStatusInProgress BetaResponseInputItemFunctionCallOutputStatus = "in\_progress"

const BetaResponseInputItemFunctionCallOutputStatusCompleted BetaResponseInputItemFunctionCallOutputStatus = "completed"

const BetaResponseInputItemFunctionCallOutputStatusIncomplete BetaResponseInputItemFunctionCallOutputStatus = "incomplete"

type BetaResponseInputItemAgentMessage struct{…}

A message routed between agents.

Author string

Content []BetaResponseInputItemAgentMessageContentUnion

Plaintext, image, or encrypted content sent between agents.

type BetaResponseInputTextContent struct{…}

Text string

maxLength10485760

Type InputText

PromptCacheBreakpoint BetaResponseInputTextContentPromptCacheBreakpointOptional

Mode Explicit

type BetaResponseInputImageContent struct{…}

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision)

Type InputImage

Detail BetaResponseInputImageContentDetailOptional

const BetaResponseInputImageContentDetailLow BetaResponseInputImageContentDetail = "low"

const BetaResponseInputImageContentDetailHigh BetaResponseInputImageContentDetail = "high"

const BetaResponseInputImageContentDetailAuto BetaResponseInputImageContentDetail = "auto"

const BetaResponseInputImageContentDetailOriginal BetaResponseInputImageContentDetail = "original"

FileID stringOptional

ImageURL stringOptional

maxLength20971520

PromptCacheBreakpoint BetaResponseInputImageContentPromptCacheBreakpointOptional

Mode Explicit

type BetaResponseInputItemAgentMessageContentEncryptedContent struct{…}

EncryptedContent string

maxLength10485760

Type EncryptedContent

Recipient string

Type AgentMessage

The item type. Always `agent_message`.

ID stringOptional

The unique ID of this agent message item.

Agent BetaResponseInputItemAgentMessageAgentOptional

AgentName string

type BetaResponseInputItemMultiAgentCall struct{…}

Action string

The multi-agent action that was executed.

const BetaResponseInputItemMultiAgentCallActionSpawnAgent BetaResponseInputItemMultiAgentCallAction = "spawn\_agent"

const BetaResponseInputItemMultiAgentCallActionInterruptAgent BetaResponseInputItemMultiAgentCallAction = "interrupt\_agent"

const BetaResponseInputItemMultiAgentCallActionListAgents BetaResponseInputItemMultiAgentCallAction = "list\_agents"

const BetaResponseInputItemMultiAgentCallActionSendMessage BetaResponseInputItemMultiAgentCallAction = "send\_message"

const BetaResponseInputItemMultiAgentCallActionFollowupTask BetaResponseInputItemMultiAgentCallAction = "followup\_task"

const BetaResponseInputItemMultiAgentCallActionWaitAgent BetaResponseInputItemMultiAgentCallAction = "wait\_agent"

Arguments string

The action arguments as a JSON string.

CallID string

maxLength64

minLength1

Type MultiAgentCall

The item type. Always `multi_agent_call`.

ID stringOptional

The unique ID of this multi-agent call.

Agent BetaResponseInputItemMultiAgentCallAgentOptional

AgentName string

type BetaResponseInputItemMultiAgentCallOutput struct{…}

Action string

const BetaResponseInputItemMultiAgentCallOutputActionSpawnAgent BetaResponseInputItemMultiAgentCallOutputAction = "spawn\_agent"

const BetaResponseInputItemMultiAgentCallOutputActionInterruptAgent BetaResponseInputItemMultiAgentCallOutputAction = "interrupt\_agent"

const BetaResponseInputItemMultiAgentCallOutputActionListAgents BetaResponseInputItemMultiAgentCallOutputAction = "list\_agents"

const BetaResponseInputItemMultiAgentCallOutputActionSendMessage BetaResponseInputItemMultiAgentCallOutputAction = "send\_message"

const BetaResponseInputItemMultiAgentCallOutputActionFollowupTask BetaResponseInputItemMultiAgentCallOutputAction = "followup\_task"

const BetaResponseInputItemMultiAgentCallOutputActionWaitAgent BetaResponseInputItemMultiAgentCallOutputAction = "wait\_agent"

CallID string

maxLength64

minLength1

Output []BetaResponseInputItemMultiAgentCallOutputOutput

Text string

The text content.

maxLength10485760

Type OutputText

The content type. Always `output_text`.

Annotations []BetaResponseInputItemMultiAgentCallOutputOutputAnnotationUnionOptional

Citations associated with the text content.

type BetaResponseInputItemMultiAgentCallOutputOutputAnnotationFileCitation struct{…}

FileID string

Filename string

Index int64

minimum0

Type FileCitation

The citation type. Always `file_citation`.

type BetaResponseInputItemMultiAgentCallOutputOutputAnnotationURLCitation struct{…}

EndIndex int64

The index of the last character of the citation in the message.

minimum0

StartIndex int64

The index of the first character of the citation in the message.

minimum0

Title string

The title of the cited resource.

Type URLCitation

The citation type. Always `url_citation`.

URL string

The URL of the cited resource.

type BetaResponseInputItemMultiAgentCallOutputOutputAnnotationContainerFileCitation struct{…}

ContainerID string

The ID of the container.

EndIndex int64

The index of the last character of the citation in the message.

minimum0

FileID string

Filename string

StartIndex int64

The index of the first character of the citation in the message.

minimum0

Type ContainerFileCitation

The citation type. Always `container_file_citation`.

Type MultiAgentCallOutput

The item type. Always `multi_agent_call_output`.

ID stringOptional

The unique ID of this multi-agent call output.

Agent BetaResponseInputItemMultiAgentCallOutputAgentOptional

AgentName string

type BetaResponseInputItemToolSearchCall struct{…}

Arguments any

The arguments supplied to the tool search call.

Type ToolSearchCall

The item type. Always `tool_search_call`.

ID stringOptional

The unique ID of this tool search call.

Agent BetaResponseInputItemToolSearchCallAgentOptional

AgentName string

CallID stringOptional

maxLength64

minLength1

Execution stringOptional

const BetaResponseInputItemToolSearchCallExecutionServer BetaResponseInputItemToolSearchCallExecution = "server"

const BetaResponseInputItemToolSearchCallExecutionClient BetaResponseInputItemToolSearchCallExecution = "client"

Status stringOptional

The status of the tool search call.

const BetaResponseInputItemToolSearchCallStatusInProgress BetaResponseInputItemToolSearchCallStatus = "in\_progress"

const BetaResponseInputItemToolSearchCallStatusCompleted BetaResponseInputItemToolSearchCallStatus = "completed"

const BetaResponseInputItemToolSearchCallStatusIncomplete BetaResponseInputItemToolSearchCallStatus = "incomplete"

type BetaResponseToolSearchOutputItemParamResp struct{…}

Tools [][BetaToolUnion](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))

The loaded tool definitions returned by the tool search output.

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

The item type. Always `tool_search_output`.

ID stringOptional

The unique ID of this tool search output.

Agent BetaResponseToolSearchOutputItemParamAgentRespOptional

AgentName string

CallID stringOptional

maxLength64

minLength1

Execution BetaResponseToolSearchOutputItemParamExecutionOptional

const BetaResponseToolSearchOutputItemParamExecutionServer BetaResponseToolSearchOutputItemParamExecution = "server"

const BetaResponseToolSearchOutputItemParamExecutionClient BetaResponseToolSearchOutputItemParamExecution = "client"

Status BetaResponseToolSearchOutputItemParamStatusOptional

The status of the tool search output.

const BetaResponseToolSearchOutputItemParamStatusInProgress BetaResponseToolSearchOutputItemParamStatus = "in\_progress"

const BetaResponseToolSearchOutputItemParamStatusCompleted BetaResponseToolSearchOutputItemParamStatus = "completed"

const BetaResponseToolSearchOutputItemParamStatusIncomplete BetaResponseToolSearchOutputItemParamStatus = "incomplete"

type BetaResponseInputItemAdditionalTools struct{…}

Role Developer

The role that provided the additional tools. Only `developer` is supported.

Tools [][BetaToolUnion](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))

A list of additional tools made available at this item.

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

The item type. Always `additional_tools`.

ID stringOptional

The unique ID of this additional tools item.

Agent BetaResponseInputItemAdditionalToolsAgentOptional

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

type BetaResponseCompactionItemParamResp struct{…}

A compaction item generated by the [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).

EncryptedContent string

The encrypted content of the compaction summary.

maxLength10485760

Type Compaction

ID stringOptional

The ID of the compaction item.

Agent BetaResponseCompactionItemParamAgentRespOptional

AgentName string

type BetaResponseInputItemImageGenerationCall struct{…}

An image generation request made by the model.

ID string

Result string

Status string

const BetaResponseInputItemImageGenerationCallStatusInProgress BetaResponseInputItemImageGenerationCallStatus = "in\_progress"

const BetaResponseInputItemImageGenerationCallStatusCompleted BetaResponseInputItemImageGenerationCallStatus = "completed"

const BetaResponseInputItemImageGenerationCallStatusGenerating BetaResponseInputItemImageGenerationCallStatus = "generating"

const BetaResponseInputItemImageGenerationCallStatusFailed BetaResponseInputItemImageGenerationCallStatus = "failed"

Type ImageGenerationCall

Agent BetaResponseInputItemImageGenerationCallAgentOptional

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

type BetaResponseInputItemLocalShellCall struct{…}

A tool call to run a command on the local shell.

ID string

Action BetaResponseInputItemLocalShellCallAction

Command []string

Env map[string, string]

Type Exec

TimeoutMs int64Optional

User stringOptional

WorkingDirectory stringOptional

CallID string

Status string

const BetaResponseInputItemLocalShellCallStatusInProgress BetaResponseInputItemLocalShellCallStatus = "in\_progress"

const BetaResponseInputItemLocalShellCallStatusCompleted BetaResponseInputItemLocalShellCallStatus = "completed"

const BetaResponseInputItemLocalShellCallStatusIncomplete BetaResponseInputItemLocalShellCallStatus = "incomplete"

Type LocalShellCall

Agent BetaResponseInputItemLocalShellCallAgentOptional

AgentName string

type BetaResponseInputItemLocalShellCallOutput struct{…}

The output of a local shell tool call.

ID string

Output string

Type LocalShellCallOutput

Agent BetaResponseInputItemLocalShellCallOutputAgentOptional

AgentName string

Status stringOptional

const BetaResponseInputItemLocalShellCallOutputStatusInProgress BetaResponseInputItemLocalShellCallOutputStatus = "in\_progress"

const BetaResponseInputItemLocalShellCallOutputStatusCompleted BetaResponseInputItemLocalShellCallOutputStatus = "completed"

const BetaResponseInputItemLocalShellCallOutputStatusIncomplete BetaResponseInputItemLocalShellCallOutputStatus = "incomplete"

type BetaResponseInputItemShellCall struct{…}

A tool representing a request to execute one or more shell commands.

Action BetaResponseInputItemShellCallAction

Commands []string

Ordered shell commands for the execution environment to run.

MaxOutputLength int64Optional

Maximum number of UTF-8 characters to capture from combined stdout and stderr output.

TimeoutMs int64Optional

Maximum wall-clock time in milliseconds to allow the shell commands to run.

CallID string

maxLength64

minLength1

Type ShellCall

ID stringOptional

Agent BetaResponseInputItemShellCallAgentOptional

AgentName string

Caller BetaResponseInputItemShellCallCallerUnionOptional

type BetaResponseInputItemShellCallCallerDirect struct{…}

Type Direct

The caller type. Always `direct`.

type BetaResponseInputItemShellCallCallerProgram struct{…}

CallerID string

maxLength64

minLength1

Type Program

Environment BetaResponseInputItemShellCallEnvironmentUnionOptional

The environment to execute the shell commands in.

type BetaLocalEnvironment struct{…}

Type Local

Skills [][BetaLocalSkill](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))Optional

Description string

Name string

Path string

type BetaContainerReference struct{…}

ContainerID string

Type ContainerReference

Status stringOptional

const BetaResponseInputItemShellCallStatusInProgress BetaResponseInputItemShellCallStatus = "in\_progress"

const BetaResponseInputItemShellCallStatusCompleted BetaResponseInputItemShellCallStatus = "completed"

const BetaResponseInputItemShellCallStatusIncomplete BetaResponseInputItemShellCallStatus = "incomplete"

type BetaResponseInputItemShellCallOutput struct{…}

The streamed output items emitted by a shell tool call.

CallID string

maxLength64

minLength1

Output [][BetaResponseFunctionShellCallOutputContent](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_shell_call_output_content%20%3E%20(schema))

Captured chunks of stdout and stderr output, along with their associated outcomes.

Outcome BetaResponseFunctionShellCallOutputContentOutcomeUnion

The exit or timeout outcome associated with this shell call.

type BetaResponseFunctionShellCallOutputContentOutcomeTimeout struct{…}

Indicates that the shell call exceeded its configured time limit.

Type Timeout

The outcome type. Always `timeout`.

type BetaResponseFunctionShellCallOutputContentOutcomeExit struct{…}

ExitCode int64

The exit code returned by the shell process.

Type Exit

Stderr string

Captured stderr output for the shell call.

maxLength10485760

Stdout string

Captured stdout output for the shell call.

maxLength10485760

Type ShellCallOutput

The type of the item. Always `shell_call_output`.

ID stringOptional

The unique ID of the shell tool call output. Populated when this item is returned via API.

Agent BetaResponseInputItemShellCallOutputAgentOptional

AgentName string

Caller BetaResponseInputItemShellCallOutputCallerUnionOptional

type BetaResponseInputItemShellCallOutputCallerDirect struct{…}

Type Direct

The caller type. Always `direct`.

type BetaResponseInputItemShellCallOutputCallerProgram struct{…}

CallerID string

maxLength64

minLength1

Type Program

MaxOutputLength int64Optional

The maximum number of UTF-8 characters captured for this shell call’s combined output.

Status stringOptional

The status of the shell call output.

const BetaResponseInputItemShellCallOutputStatusInProgress BetaResponseInputItemShellCallOutputStatus = "in\_progress"

const BetaResponseInputItemShellCallOutputStatusCompleted BetaResponseInputItemShellCallOutputStatus = "completed"

const BetaResponseInputItemShellCallOutputStatusIncomplete BetaResponseInputItemShellCallOutputStatus = "incomplete"

type BetaResponseInputItemApplyPatchCall struct{…}

A tool call representing a request to create, delete, or update files using diff patches.

CallID string

maxLength64

minLength1

Operation BetaResponseInputItemApplyPatchCallOperationUnion

The specific create, delete, or update instruction for the apply\_patch tool call.

type BetaResponseInputItemApplyPatchCallOperationCreateFile struct{…}

Instruction for creating a new file via the apply\_patch tool.

Diff string

Unified diff content to apply when creating the file.

maxLength10485760

Path string

Path of the file to create relative to the workspace root.

minLength1

Type CreateFile

The operation type. Always `create_file`.

type BetaResponseInputItemApplyPatchCallOperationDeleteFile struct{…}

Instruction for deleting an existing file via the apply\_patch tool.

Path string

Path of the file to delete relative to the workspace root.

minLength1

Type DeleteFile

The operation type. Always `delete_file`.

type BetaResponseInputItemApplyPatchCallOperationUpdateFile struct{…}

Instruction for updating an existing file via the apply\_patch tool.

Diff string

Unified diff content to apply to the existing file.

maxLength10485760

Path string

Path of the file to update relative to the workspace root.

minLength1

Type UpdateFile

The operation type. Always `update_file`.

Status string

const BetaResponseInputItemApplyPatchCallStatusInProgress BetaResponseInputItemApplyPatchCallStatus = "in\_progress"

const BetaResponseInputItemApplyPatchCallStatusCompleted BetaResponseInputItemApplyPatchCallStatus = "completed"

Type ApplyPatchCall

ID stringOptional

Agent BetaResponseInputItemApplyPatchCallAgentOptional

AgentName string

Caller BetaResponseInputItemApplyPatchCallCallerUnionOptional

type BetaResponseInputItemApplyPatchCallCallerDirect struct{…}

Type Direct

The caller type. Always `direct`.

type BetaResponseInputItemApplyPatchCallCallerProgram struct{…}

CallerID string

maxLength64

minLength1

Type Program

type BetaResponseInputItemApplyPatchCallOutput struct{…}

The streamed output emitted by an apply patch tool call.

CallID string

maxLength64

minLength1

Status string

const BetaResponseInputItemApplyPatchCallOutputStatusCompleted BetaResponseInputItemApplyPatchCallOutputStatus = "completed"

const BetaResponseInputItemApplyPatchCallOutputStatusFailed BetaResponseInputItemApplyPatchCallOutputStatus = "failed"

Type ApplyPatchCallOutput

ID stringOptional

Agent BetaResponseInputItemApplyPatchCallOutputAgentOptional

AgentName string

Caller BetaResponseInputItemApplyPatchCallOutputCallerUnionOptional

type BetaResponseInputItemApplyPatchCallOutputCallerDirect struct{…}

Type Direct

The caller type. Always `direct`.

type BetaResponseInputItemApplyPatchCallOutputCallerProgram struct{…}

CallerID string

maxLength64

minLength1

Type Program

Output stringOptional

Optional human-readable log text from the apply patch tool (e.g., patch results or errors).

maxLength10485760

type BetaResponseInputItemMcpListTools struct{…}

A list of tools available on an MCP server.

ID string

ServerLabel string

Tools []BetaResponseInputItemMcpListToolsTool

InputSchema any

Name string

Annotations anyOptional

Description stringOptional

Type McpListTools

Agent BetaResponseInputItemMcpListToolsAgentOptional

AgentName string

Error stringOptional

type BetaResponseInputItemMcpApprovalRequest struct{…}

A request for human approval of a tool invocation.

ID string

Arguments string

Name string

ServerLabel string

Type McpApprovalRequest

Agent BetaResponseInputItemMcpApprovalRequestAgentOptional

AgentName string

type BetaResponseInputItemMcpApprovalResponse struct{…}

A response to an MCP approval request.

ApprovalRequestID string

Approve bool

Type McpApprovalResponse

ID stringOptional

Agent BetaResponseInputItemMcpApprovalResponseAgentOptional

AgentName string

Reason stringOptional

type BetaResponseInputItemMcpCall struct{…}

An invocation of a tool on an MCP server.

ID string

Arguments string

Name string

ServerLabel string

Type McpCall

Agent BetaResponseInputItemMcpCallAgentOptional

AgentName string

ApprovalRequestID stringOptional

Error stringOptional

Output stringOptional

Status stringOptional

const BetaResponseInputItemMcpCallStatusInProgress BetaResponseInputItemMcpCallStatus = "in\_progress"

const BetaResponseInputItemMcpCallStatusCompleted BetaResponseInputItemMcpCallStatus = "completed"

const BetaResponseInputItemMcpCallStatusIncomplete BetaResponseInputItemMcpCallStatus = "incomplete"

const BetaResponseInputItemMcpCallStatusCalling BetaResponseInputItemMcpCallStatus = "calling"

const BetaResponseInputItemMcpCallStatusFailed BetaResponseInputItemMcpCallStatus = "failed"

type BetaResponseCustomToolCallOutput struct{…}

CallID string

The call ID, used to map this custom tool call output to a custom tool call.

Output BetaResponseCustomToolCallOutputOutputUnion

The output from the custom tool call generated by your code.

string

type BetaResponseCustomToolCallOutputOutputOutputContentList []BetaResponseCustomToolCallOutputOutputOutputContentListItemUnion

Text, image, or file output of the custom tool call.

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

Type CustomToolCallOutput

The type of the custom tool call output. Always `custom_tool_call_output`.

ID stringOptional

The unique ID of the custom tool call output in the OpenAI platform.

Agent BetaResponseCustomToolCallOutputAgentOptional

AgentName string

Caller BetaResponseCustomToolCallOutputCallerUnionOptional

type BetaResponseCustomToolCallOutputCallerDirect struct{…}

Type Direct

The caller type. Always `direct`.

type BetaResponseCustomToolCallOutputCallerProgram struct{…}

CallerID string

maxLength64

minLength1

Type Program

type BetaResponseCustomToolCall struct{…}

CallID string

An identifier used to map this custom tool call to a tool call output.

Input string

The input for the custom tool call generated by the model.

Name string

The name of the custom tool being called.

Type CustomToolCall

The type of the custom tool call. Always `custom_tool_call`.

ID stringOptional

The unique ID of the custom tool call in the OpenAI platform.

Agent BetaResponseCustomToolCallAgentOptional

AgentName string

Caller BetaResponseCustomToolCallCallerUnionOptional

type BetaResponseCustomToolCallCallerDirect struct{…}

Type Direct

type BetaResponseCustomToolCallCallerProgram struct{…}

CallerID string

Type Program

Namespace stringOptional

The namespace of the custom tool being called.

type BetaResponseInputItemCompactionTrigger struct{…}

Compacts the current context. Must be the final input item.

Type CompactionTrigger

The type of the item. Always `compaction_trigger`.

Agent BetaResponseInputItemCompactionTriggerAgentOptional

AgentName string

type BetaResponseInputItemItemReference struct{…}

An internal identifier for an item to reference.

ID string

The ID of the item to reference.

Agent BetaResponseInputItemItemReferenceAgentOptional

AgentName string

Type stringOptional

The type of item to reference. Always `item_reference`.

type BetaResponseInputItemProgram struct{…}

ID string

The unique ID of this program item.

CallID string

maxLength64

minLength1

Code string

maxLength10485760

Fingerprint string

maxLength10485760

Type Program

The item type. Always `program`.

Agent BetaResponseInputItemProgramAgentOptional

AgentName string

type BetaResponseInputItemProgramOutput struct{…}

ID string

The unique ID of this program output item.

CallID string

maxLength64

minLength1

Result string

maxLength10485760

Status string

The terminal status of the program output.

const BetaResponseInputItemProgramOutputStatusCompleted BetaResponseInputItemProgramOutputStatus = "completed"

const BetaResponseInputItemProgramOutputStatusIncomplete BetaResponseInputItemProgramOutputStatus = "incomplete"

Type ProgramOutput

The item type. Always `program_output`.

Agent BetaResponseInputItemProgramOutputAgentOptional

AgentName string

Instructions param.Field[string]Optional

Body param: A system (or developer) message inserted into the model’s context.
When used along with `previous_response_id`, the instructions from a previous response will not be carried over to the next response. This makes it simple to swap out system (or developer) messages in new responses.

PreviousResponseID param.Field[string]Optional

Body param: The unique ID of the previous response to the model. Use this to create multi-turn conversations. Learn more about [conversation state](https://platform.openai.com/docs/guides/conversation-state). Cannot be used in conjunction with `conversation`.

PromptCacheKey param.Field[string]Optional

Body param: A key to use when reading from or writing to the prompt cache.

maxLength64

PromptCacheOptions param.Field[[BetaResponseCompactParamsPromptCacheOptions](/api/reference/go/resources/beta/subresources/responses/methods/compact#(resource)%20beta.responses%20%3E%20(method)%20compact%20%3E%20(params)%20default%20%3E%20(param)%20prompt_cache_options%20%3E%20(schema))]Optional

Body param: Options for prompt caching. Supported for `gpt-5.6` and later models. By default, OpenAI automatically chooses one implicit cache breakpoint. You can add explicit breakpoints to content blocks with `prompt_cache_breakpoint`. Each request can write up to four breakpoints. For cache matching, OpenAI considers up to the latest 80 breakpoints in the conversation, without a content-block lookback limit. Set `mode` to `explicit` to disable the implicit breakpoint. The `ttl` defaults to `30m`, which is currently the only supported value. See the [prompt caching guide](https://platform.openai.com/docs/guides/prompt-caching) for current details.

Mode stringOptional

Controls whether OpenAI automatically creates an implicit cache breakpoint. Defaults to `implicit`. With `implicit`, OpenAI creates one implicit breakpoint and writes up to the latest three explicit breakpoints in the request. With `explicit`, OpenAI does not create an implicit breakpoint and writes up to the latest four explicit breakpoints. If there are no explicit breakpoints, the request does not use prompt caching.

const BetaResponseCompactParamsPromptCacheOptionsModeImplicit BetaResponseCompactParamsPromptCacheOptionsMode = "implicit"

const BetaResponseCompactParamsPromptCacheOptionsModeExplicit BetaResponseCompactParamsPromptCacheOptionsMode = "explicit"

Ttl stringOptional

The minimum lifetime applied to every implicit and explicit cache breakpoint written by the request. Defaults to `30m`, which is currently the only supported value. The backend may retain cache entries for longer.

DeprecatedPromptCacheRetention param.Field[[BetaResponseCompactParamsPromptCacheRetention](/api/reference/go/resources/beta/subresources/responses/methods/compact#(resource)%20beta.responses%20%3E%20(method)%20compact%20%3E%20(params)%20default%20%3E%20(param)%20prompt_cache_retention%20%3E%20(schema))]Optional

Body param: How long to retain a prompt cache entry created by this request.

const BetaResponseCompactParamsPromptCacheRetentionInMemory [BetaResponseCompactParamsPromptCacheRetention](/api/reference/go/resources/beta/subresources/responses/methods/compact#(resource)%20beta.responses%20%3E%20(method)%20compact%20%3E%20(params)%20default%20%3E%20(param)%20prompt_cache_retention%20%3E%20(schema)) = "in\_memory"

const BetaResponseCompactParamsPromptCacheRetention24h [BetaResponseCompactParamsPromptCacheRetention](/api/reference/go/resources/beta/subresources/responses/methods/compact#(resource)%20beta.responses%20%3E%20(method)%20compact%20%3E%20(params)%20default%20%3E%20(param)%20prompt_cache_retention%20%3E%20(schema)) = "24h"

ServiceTier param.Field[[BetaResponseCompactParamsServiceTier](/api/reference/go/resources/beta/subresources/responses/methods/compact#(resource)%20beta.responses%20%3E%20(method)%20compact%20%3E%20(params)%20default%20%3E%20(param)%20service_tier%20%3E%20(schema))]Optional

Body param: The service tier to use for this request.

const BetaResponseCompactParamsServiceTierAuto [BetaResponseCompactParamsServiceTier](/api/reference/go/resources/beta/subresources/responses/methods/compact#(resource)%20beta.responses%20%3E%20(method)%20compact%20%3E%20(params)%20default%20%3E%20(param)%20service_tier%20%3E%20(schema)) = "auto"

const BetaResponseCompactParamsServiceTierDefault [BetaResponseCompactParamsServiceTier](/api/reference/go/resources/beta/subresources/responses/methods/compact#(resource)%20beta.responses%20%3E%20(method)%20compact%20%3E%20(params)%20default%20%3E%20(param)%20service_tier%20%3E%20(schema)) = "default"

const BetaResponseCompactParamsServiceTierFlex [BetaResponseCompactParamsServiceTier](/api/reference/go/resources/beta/subresources/responses/methods/compact#(resource)%20beta.responses%20%3E%20(method)%20compact%20%3E%20(params)%20default%20%3E%20(param)%20service_tier%20%3E%20(schema)) = "flex"

const BetaResponseCompactParamsServiceTierPriority [BetaResponseCompactParamsServiceTier](/api/reference/go/resources/beta/subresources/responses/methods/compact#(resource)%20beta.responses%20%3E%20(method)%20compact%20%3E%20(params)%20default%20%3E%20(param)%20service_tier%20%3E%20(schema)) = "priority"

Betas param.Field[[]string]Optional

Header param: Optional beta features to enable for this request.

const BetaResponseCompactParamsOpenAIBetaResponsesMultiAgentV1 BetaResponseCompactParamsOpenAIBeta = "responses\_multi\_agent=v1"

##### ReturnsExpand Collapse

type BetaCompactedResponse struct{…}

ID string

The unique identifier for the compacted response.

CreatedAt int64

Unix timestamp (in seconds) when the compacted conversation was created.

formatunixtime

Object ResponseCompaction

The object type. Always `response.compaction`.

Output [][BetaResponseOutputItemUnion](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_item%20%3E%20(schema))

The compacted list of output items. This is a list of all user messages, followed by a single compaction item.

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

type BetaResponseFunctionToolCall struct{…}

[function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.

Arguments string

A JSON string of the arguments to pass to the function.

CallID string

Name string

The name of the function to run.

Type FunctionCall

The type of the function tool call. Always `function_call`.

ID stringOptional

Agent BetaResponseFunctionToolCallAgentOptional

AgentName string

Caller BetaResponseFunctionToolCallCallerUnionOptional

type BetaResponseFunctionToolCallCallerDirect struct{…}

Type Direct

type BetaResponseFunctionToolCallCallerProgram struct{…}

CallerID string

Type Program

Namespace stringOptional

The namespace of the function to run.

Status BetaResponseFunctionToolCallStatusOptional

const BetaResponseFunctionToolCallStatusInProgress BetaResponseFunctionToolCallStatus = "in\_progress"

const BetaResponseFunctionToolCallStatusCompleted BetaResponseFunctionToolCallStatus = "completed"

const BetaResponseFunctionToolCallStatusIncomplete BetaResponseFunctionToolCallStatus = "incomplete"

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

type BetaResponseOutputItemAgentMessage struct{…}

ID string

The unique ID of the agent message.

Author string

Content []BetaResponseOutputItemAgentMessageContentUnion

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

type BetaResponseOutputItemAgentMessageContentText struct{…}

A text content.

Text string

Type Text

type BetaResponseOutputItemAgentMessageContentSummaryText struct{…}

A summary text from the model.

Text string

Type SummaryText

type BetaResponseOutputItemAgentMessageContentReasoningText struct{…}

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

type BetaResponseOutputItemAgentMessageContentComputerScreenshot struct{…}

A screenshot of a computer.

Detail string

The detail level of the screenshot image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

const BetaResponseOutputItemAgentMessageContentComputerScreenshotDetailLow BetaResponseOutputItemAgentMessageContentComputerScreenshotDetail = "low"

const BetaResponseOutputItemAgentMessageContentComputerScreenshotDetailHigh BetaResponseOutputItemAgentMessageContentComputerScreenshotDetail = "high"

const BetaResponseOutputItemAgentMessageContentComputerScreenshotDetailAuto BetaResponseOutputItemAgentMessageContentComputerScreenshotDetail = "auto"

const BetaResponseOutputItemAgentMessageContentComputerScreenshotDetailOriginal BetaResponseOutputItemAgentMessageContentComputerScreenshotDetail = "original"

FileID string

ImageURL string

Type ComputerScreenshot

Specifies the event type. For a computer screenshot, this property is always set to `computer_screenshot`.

PromptCacheBreakpoint BetaResponseOutputItemAgentMessageContentComputerScreenshotPromptCacheBreakpointOptional

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

type BetaResponseOutputItemAgentMessageContentEncryptedContent struct{…}

EncryptedContent string

Type EncryptedContent

Recipient string

Type AgentMessage

The type of the item. Always `agent_message`.

Agent BetaResponseOutputItemAgentMessageAgentOptional

AgentName string

type BetaResponseOutputItemMultiAgentCall struct{…}

ID string

The unique ID of the multi-agent call item.

Action string

The multi-agent action to execute.

const BetaResponseOutputItemMultiAgentCallActionSpawnAgent BetaResponseOutputItemMultiAgentCallAction = "spawn\_agent"

const BetaResponseOutputItemMultiAgentCallActionInterruptAgent BetaResponseOutputItemMultiAgentCallAction = "interrupt\_agent"

const BetaResponseOutputItemMultiAgentCallActionListAgents BetaResponseOutputItemMultiAgentCallAction = "list\_agents"

const BetaResponseOutputItemMultiAgentCallActionSendMessage BetaResponseOutputItemMultiAgentCallAction = "send\_message"

const BetaResponseOutputItemMultiAgentCallActionFollowupTask BetaResponseOutputItemMultiAgentCallAction = "followup\_task"

const BetaResponseOutputItemMultiAgentCallActionWaitAgent BetaResponseOutputItemMultiAgentCallAction = "wait\_agent"

Arguments string

The JSON string of arguments generated for the action.

CallID string

Type MultiAgentCall

The type of the multi-agent call. Always `multi_agent_call`.

Agent BetaResponseOutputItemMultiAgentCallAgentOptional

AgentName string

type BetaResponseOutputItemMultiAgentCallOutput struct{…}

ID string

The unique ID of the multi-agent call output item.

Action string

const BetaResponseOutputItemMultiAgentCallOutputActionSpawnAgent BetaResponseOutputItemMultiAgentCallOutputAction = "spawn\_agent"

const BetaResponseOutputItemMultiAgentCallOutputActionInterruptAgent BetaResponseOutputItemMultiAgentCallOutputAction = "interrupt\_agent"

const BetaResponseOutputItemMultiAgentCallOutputActionListAgents BetaResponseOutputItemMultiAgentCallOutputAction = "list\_agents"

const BetaResponseOutputItemMultiAgentCallOutputActionSendMessage BetaResponseOutputItemMultiAgentCallOutputAction = "send\_message"

const BetaResponseOutputItemMultiAgentCallOutputActionFollowupTask BetaResponseOutputItemMultiAgentCallOutputAction = "followup\_task"

const BetaResponseOutputItemMultiAgentCallOutputActionWaitAgent BetaResponseOutputItemMultiAgentCallOutputAction = "wait\_agent"

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

Agent BetaResponseOutputItemMultiAgentCallOutputAgentOptional

AgentName string

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

type BetaResponseOutputItemProgram struct{…}

ID string

The unique ID of the program item.

CallID string

Code string

Fingerprint string

Type Program

The type of the item. Always `program`.

Agent BetaResponseOutputItemProgramAgentOptional

AgentName string

type BetaResponseOutputItemProgramOutput struct{…}

ID string

The unique ID of the program output item.

CallID string

Result string

Status string

The terminal status of the program output item.

const BetaResponseOutputItemProgramOutputStatusCompleted BetaResponseOutputItemProgramOutputStatus = "completed"

const BetaResponseOutputItemProgramOutputStatusIncomplete BetaResponseOutputItemProgramOutputStatus = "incomplete"

Type ProgramOutput

The type of the item. Always `program_output`.

Agent BetaResponseOutputItemProgramOutputAgentOptional

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

type BetaResponseOutputItemAdditionalTools struct{…}

ID string

The unique ID of the additional tools item.

Role string

The role that provided the additional tools.

const BetaResponseOutputItemAdditionalToolsRoleUnknown BetaResponseOutputItemAdditionalToolsRole = "unknown"

const BetaResponseOutputItemAdditionalToolsRoleUser BetaResponseOutputItemAdditionalToolsRole = "user"

const BetaResponseOutputItemAdditionalToolsRoleAssistant BetaResponseOutputItemAdditionalToolsRole = "assistant"

const BetaResponseOutputItemAdditionalToolsRoleSystem BetaResponseOutputItemAdditionalToolsRole = "system"

const BetaResponseOutputItemAdditionalToolsRoleCritic BetaResponseOutputItemAdditionalToolsRole = "critic"

const BetaResponseOutputItemAdditionalToolsRoleDiscriminator BetaResponseOutputItemAdditionalToolsRole = "discriminator"

const BetaResponseOutputItemAdditionalToolsRoleDeveloper BetaResponseOutputItemAdditionalToolsRole = "developer"

const BetaResponseOutputItemAdditionalToolsRoleTool BetaResponseOutputItemAdditionalToolsRole = "tool"

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

Agent BetaResponseOutputItemAdditionalToolsAgentOptional

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

type BetaResponseOutputItemImageGenerationCall struct{…}

An image generation request made by the model.

ID string

Result string

Status string

const BetaResponseOutputItemImageGenerationCallStatusInProgress BetaResponseOutputItemImageGenerationCallStatus = "in\_progress"

const BetaResponseOutputItemImageGenerationCallStatusCompleted BetaResponseOutputItemImageGenerationCallStatus = "completed"

const BetaResponseOutputItemImageGenerationCallStatusGenerating BetaResponseOutputItemImageGenerationCallStatus = "generating"

const BetaResponseOutputItemImageGenerationCallStatusFailed BetaResponseOutputItemImageGenerationCallStatus = "failed"

Type ImageGenerationCall

Agent BetaResponseOutputItemImageGenerationCallAgentOptional

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

type BetaResponseOutputItemLocalShellCall struct{…}

A tool call to run a command on the local shell.

ID string

Action BetaResponseOutputItemLocalShellCallAction

Command []string

Env map[string, string]

Type Exec

TimeoutMs int64Optional

User stringOptional

WorkingDirectory stringOptional

CallID string

Status string

const BetaResponseOutputItemLocalShellCallStatusInProgress BetaResponseOutputItemLocalShellCallStatus = "in\_progress"

const BetaResponseOutputItemLocalShellCallStatusCompleted BetaResponseOutputItemLocalShellCallStatus = "completed"

const BetaResponseOutputItemLocalShellCallStatusIncomplete BetaResponseOutputItemLocalShellCallStatus = "incomplete"

Type LocalShellCall

Agent BetaResponseOutputItemLocalShellCallAgentOptional

AgentName string

type BetaResponseOutputItemLocalShellCallOutput struct{…}

The output of a local shell tool call.

ID string

Output string

Type LocalShellCallOutput

Agent BetaResponseOutputItemLocalShellCallOutputAgentOptional

AgentName string

Status stringOptional

const BetaResponseOutputItemLocalShellCallOutputStatusInProgress BetaResponseOutputItemLocalShellCallOutputStatus = "in\_progress"

const BetaResponseOutputItemLocalShellCallOutputStatusCompleted BetaResponseOutputItemLocalShellCallOutputStatus = "completed"

const BetaResponseOutputItemLocalShellCallOutputStatusIncomplete BetaResponseOutputItemLocalShellCallOutputStatus = "incomplete"

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

type BetaResponseOutputItemMcpCall struct{…}

An invocation of a tool on an MCP server.

ID string

Arguments string

Name string

ServerLabel string

Type McpCall

Agent BetaResponseOutputItemMcpCallAgentOptional

AgentName string

ApprovalRequestID stringOptional

Error stringOptional

Output stringOptional

Status stringOptional

const BetaResponseOutputItemMcpCallStatusInProgress BetaResponseOutputItemMcpCallStatus = "in\_progress"

const BetaResponseOutputItemMcpCallStatusCompleted BetaResponseOutputItemMcpCallStatus = "completed"

const BetaResponseOutputItemMcpCallStatusIncomplete BetaResponseOutputItemMcpCallStatus = "incomplete"

const BetaResponseOutputItemMcpCallStatusCalling BetaResponseOutputItemMcpCallStatus = "calling"

const BetaResponseOutputItemMcpCallStatusFailed BetaResponseOutputItemMcpCallStatus = "failed"

type BetaResponseOutputItemMcpListTools struct{…}

A list of tools available on an MCP server.

ID string

ServerLabel string

Tools []BetaResponseOutputItemMcpListToolsTool

InputSchema any

Name string

Annotations anyOptional

Description stringOptional

Type McpListTools

Agent BetaResponseOutputItemMcpListToolsAgentOptional

AgentName string

Error stringOptional

type BetaResponseOutputItemMcpApprovalRequest struct{…}

A request for human approval of a tool invocation.

ID string

Arguments string

Name string

ServerLabel string

Type McpApprovalRequest

Agent BetaResponseOutputItemMcpApprovalRequestAgentOptional

AgentName string

type BetaResponseOutputItemMcpApprovalResponse struct{…}

A response to an MCP approval request.

ID string

ApprovalRequestID string

Approve bool

Type McpApprovalResponse

Agent BetaResponseOutputItemMcpApprovalResponseAgentOptional

AgentName string

Reason stringOptional

type BetaResponseCustomToolCall struct{…}

CallID string

An identifier used to map this custom tool call to a tool call output.

Input string

The input for the custom tool call generated by the model.

Name string

The name of the custom tool being called.

Type CustomToolCall

The type of the custom tool call. Always `custom_tool_call`.

ID stringOptional

The unique ID of the custom tool call in the OpenAI platform.

Agent BetaResponseCustomToolCallAgentOptional

AgentName string

Caller BetaResponseCustomToolCallCallerUnionOptional

type BetaResponseCustomToolCallCallerDirect struct{…}

Type Direct

type BetaResponseCustomToolCallCallerProgram struct{…}

CallerID string

Type Program

Namespace stringOptional

The namespace of the custom tool being called.

type BetaResponseCustomToolCallOutputItem struct{…}

ID string

The unique ID of the custom tool call output item.

Status string

const BetaResponseCustomToolCallOutputItemStatusInProgress BetaResponseCustomToolCallOutputItemStatus = "in\_progress"

const BetaResponseCustomToolCallOutputItemStatusCompleted BetaResponseCustomToolCallOutputItemStatus = "completed"

const BetaResponseCustomToolCallOutputItemStatusIncomplete BetaResponseCustomToolCallOutputItemStatus = "incomplete"

CreatedBy stringOptional

The identifier of the actor that created the item.

Usage [BetaResponseUsage](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_usage%20%3E%20(schema))

Token accounting for the compaction pass, including cached, reasoning, and total tokens.

InputTokens int64

The number of input tokens.

InputTokensDetails BetaResponseUsageInputTokensDetails

A detailed breakdown of the input tokens.

CacheWriteTokens int64

The number of input tokens that were written to the cache.

CachedTokens int64

The number of tokens that were retrieved from the cache.
[More on prompt caching](https://platform.openai.com/docs/guides/prompt-caching).

OutputTokens int64

The number of output tokens.

OutputTokensDetails BetaResponseUsageOutputTokensDetails

A detailed breakdown of the output tokens.

ReasoningTokens int64

The number of reasoning tokens.

TotalTokens int64

The total number of tokens used.

### Compact a response

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
  betaCompactedResponse, err := client.Beta.Responses.Compact(context.TODO(), openai.BetaResponseCompactParams{
    Model: openai.BetaResponseCompactParamsModelGPT5_6Sol,
  })
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", betaCompactedResponse.ID)

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
