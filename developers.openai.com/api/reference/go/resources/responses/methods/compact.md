<!-- source: https://developers.openai.com/api/reference/go/resources/responses/methods/compact/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Responses](/api/reference/go/resources/responses)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Compact a response

client.Responses.Compact(ctx, body) (\*[CompactedResponse](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20compacted_response%20%3E%20(schema)), error)

POST/responses/compact

Compact a conversation. Returns a compacted response object.

Learn when and how to compact long-running conversations in the [conversation state guide](https://platform.openai.com/docs/guides/conversation-state#managing-the-context-window). For ZDR-compatible compaction details, see [Compaction (advanced)](https://platform.openai.com/docs/guides/conversation-state#compaction-advanced).

##### ParametersExpand Collapse

body ResponseCompactParams

Model param.Field[ResponseCompactParamsModel]

Model ID used to generate the response, like `gpt-5` or `o3`. OpenAI offers a wide range of models with different capabilities, performance characteristics, and price points. Refer to the [model guide](https://platform.openai.com/docs/models) to browse and compare available models.

type ResponseCompactParamsModel string

Model ID used to generate the response, like `gpt-5` or `o3`. OpenAI offers a wide range of models with different capabilities, performance characteristics, and price points. Refer to the [model guide](https://platform.openai.com/docs/models) to browse and compare available models.

One of the following:

const ResponseCompactParamsModelGPT5\_4 ResponseCompactParamsModel = "gpt-5.4"

const ResponseCompactParamsModelGPT5\_4Mini ResponseCompactParamsModel = "gpt-5.4-mini"

const ResponseCompactParamsModelGPT5\_4Nano ResponseCompactParamsModel = "gpt-5.4-nano"

const ResponseCompactParamsModelGPT5\_4Mini2026\_03\_17 ResponseCompactParamsModel = "gpt-5.4-mini-2026-03-17"

const ResponseCompactParamsModelGPT5\_4Nano2026\_03\_17 ResponseCompactParamsModel = "gpt-5.4-nano-2026-03-17"

const ResponseCompactParamsModelGPT5\_3ChatLatest ResponseCompactParamsModel = "gpt-5.3-chat-latest"

const ResponseCompactParamsModelGPT5\_2 ResponseCompactParamsModel = "gpt-5.2"

const ResponseCompactParamsModelGPT5\_2\_2025\_12\_11 ResponseCompactParamsModel = "gpt-5.2-2025-12-11"

const ResponseCompactParamsModelGPT5\_2ChatLatest ResponseCompactParamsModel = "gpt-5.2-chat-latest"

const ResponseCompactParamsModelGPT5\_2Pro ResponseCompactParamsModel = "gpt-5.2-pro"

const ResponseCompactParamsModelGPT5\_2Pro2025\_12\_11 ResponseCompactParamsModel = "gpt-5.2-pro-2025-12-11"

const ResponseCompactParamsModelGPT5\_1 ResponseCompactParamsModel = "gpt-5.1"

const ResponseCompactParamsModelGPT5\_1\_2025\_11\_13 ResponseCompactParamsModel = "gpt-5.1-2025-11-13"

const ResponseCompactParamsModelGPT5\_1Codex ResponseCompactParamsModel = "gpt-5.1-codex"

const ResponseCompactParamsModelGPT5\_1Mini ResponseCompactParamsModel = "gpt-5.1-mini"

const ResponseCompactParamsModelGPT5\_1ChatLatest ResponseCompactParamsModel = "gpt-5.1-chat-latest"

const ResponseCompactParamsModelGPT5 ResponseCompactParamsModel = "gpt-5"

const ResponseCompactParamsModelGPT5Mini ResponseCompactParamsModel = "gpt-5-mini"

const ResponseCompactParamsModelGPT5Nano ResponseCompactParamsModel = "gpt-5-nano"

const ResponseCompactParamsModelGPT5\_2025\_08\_07 ResponseCompactParamsModel = "gpt-5-2025-08-07"

const ResponseCompactParamsModelGPT5Mini2025\_08\_07 ResponseCompactParamsModel = "gpt-5-mini-2025-08-07"

const ResponseCompactParamsModelGPT5Nano2025\_08\_07 ResponseCompactParamsModel = "gpt-5-nano-2025-08-07"

const ResponseCompactParamsModelGPT5ChatLatest ResponseCompactParamsModel = "gpt-5-chat-latest"

const ResponseCompactParamsModelGPT4\_1 ResponseCompactParamsModel = "gpt-4.1"

const ResponseCompactParamsModelGPT4\_1Mini ResponseCompactParamsModel = "gpt-4.1-mini"

const ResponseCompactParamsModelGPT4\_1Nano ResponseCompactParamsModel = "gpt-4.1-nano"

const ResponseCompactParamsModelGPT4\_1\_2025\_04\_14 ResponseCompactParamsModel = "gpt-4.1-2025-04-14"

const ResponseCompactParamsModelGPT4\_1Mini2025\_04\_14 ResponseCompactParamsModel = "gpt-4.1-mini-2025-04-14"

const ResponseCompactParamsModelGPT4\_1Nano2025\_04\_14 ResponseCompactParamsModel = "gpt-4.1-nano-2025-04-14"

const ResponseCompactParamsModelO4Mini ResponseCompactParamsModel = "o4-mini"

const ResponseCompactParamsModelO4Mini2025\_04\_16 ResponseCompactParamsModel = "o4-mini-2025-04-16"

const ResponseCompactParamsModelO3 ResponseCompactParamsModel = "o3"

const ResponseCompactParamsModelO3\_2025\_04\_16 ResponseCompactParamsModel = "o3-2025-04-16"

const ResponseCompactParamsModelO3Mini ResponseCompactParamsModel = "o3-mini"

const ResponseCompactParamsModelO3Mini2025\_01\_31 ResponseCompactParamsModel = "o3-mini-2025-01-31"

const ResponseCompactParamsModelO1 ResponseCompactParamsModel = "o1"

const ResponseCompactParamsModelO1\_2024\_12\_17 ResponseCompactParamsModel = "o1-2024-12-17"

const ResponseCompactParamsModelO1Preview ResponseCompactParamsModel = "o1-preview"

const ResponseCompactParamsModelO1Preview2024\_09\_12 ResponseCompactParamsModel = "o1-preview-2024-09-12"

const ResponseCompactParamsModelO1Mini ResponseCompactParamsModel = "o1-mini"

const ResponseCompactParamsModelO1Mini2024\_09\_12 ResponseCompactParamsModel = "o1-mini-2024-09-12"

const ResponseCompactParamsModelGPT4o ResponseCompactParamsModel = "gpt-4o"

const ResponseCompactParamsModelGPT4o2024\_11\_20 ResponseCompactParamsModel = "gpt-4o-2024-11-20"

const ResponseCompactParamsModelGPT4o2024\_08\_06 ResponseCompactParamsModel = "gpt-4o-2024-08-06"

const ResponseCompactParamsModelGPT4o2024\_05\_13 ResponseCompactParamsModel = "gpt-4o-2024-05-13"

const ResponseCompactParamsModelGPT4oAudioPreview ResponseCompactParamsModel = "gpt-4o-audio-preview"

const ResponseCompactParamsModelGPT4oAudioPreview2024\_10\_01 ResponseCompactParamsModel = "gpt-4o-audio-preview-2024-10-01"

const ResponseCompactParamsModelGPT4oAudioPreview2024\_12\_17 ResponseCompactParamsModel = "gpt-4o-audio-preview-2024-12-17"

const ResponseCompactParamsModelGPT4oAudioPreview2025\_06\_03 ResponseCompactParamsModel = "gpt-4o-audio-preview-2025-06-03"

const ResponseCompactParamsModelGPT4oMiniAudioPreview ResponseCompactParamsModel = "gpt-4o-mini-audio-preview"

const ResponseCompactParamsModelGPT4oMiniAudioPreview2024\_12\_17 ResponseCompactParamsModel = "gpt-4o-mini-audio-preview-2024-12-17"

const ResponseCompactParamsModelGPT4oSearchPreview ResponseCompactParamsModel = "gpt-4o-search-preview"

const ResponseCompactParamsModelGPT4oMiniSearchPreview ResponseCompactParamsModel = "gpt-4o-mini-search-preview"

const ResponseCompactParamsModelGPT4oSearchPreview2025\_03\_11 ResponseCompactParamsModel = "gpt-4o-search-preview-2025-03-11"

const ResponseCompactParamsModelGPT4oMiniSearchPreview2025\_03\_11 ResponseCompactParamsModel = "gpt-4o-mini-search-preview-2025-03-11"

const ResponseCompactParamsModelChatgpt4oLatest ResponseCompactParamsModel = "chatgpt-4o-latest"

const ResponseCompactParamsModelCodexMiniLatest ResponseCompactParamsModel = "codex-mini-latest"

const ResponseCompactParamsModelGPT4oMini ResponseCompactParamsModel = "gpt-4o-mini"

const ResponseCompactParamsModelGPT4oMini2024\_07\_18 ResponseCompactParamsModel = "gpt-4o-mini-2024-07-18"

const ResponseCompactParamsModelGPT4Turbo ResponseCompactParamsModel = "gpt-4-turbo"

const ResponseCompactParamsModelGPT4Turbo2024\_04\_09 ResponseCompactParamsModel = "gpt-4-turbo-2024-04-09"

const ResponseCompactParamsModelGPT4\_0125Preview ResponseCompactParamsModel = "gpt-4-0125-preview"

const ResponseCompactParamsModelGPT4TurboPreview ResponseCompactParamsModel = "gpt-4-turbo-preview"

const ResponseCompactParamsModelGPT4\_1106Preview ResponseCompactParamsModel = "gpt-4-1106-preview"

const ResponseCompactParamsModelGPT4VisionPreview ResponseCompactParamsModel = "gpt-4-vision-preview"

const ResponseCompactParamsModelGPT4 ResponseCompactParamsModel = "gpt-4"

const ResponseCompactParamsModelGPT4\_0314 ResponseCompactParamsModel = "gpt-4-0314"

const ResponseCompactParamsModelGPT4\_0613 ResponseCompactParamsModel = "gpt-4-0613"

const ResponseCompactParamsModelGPT4\_32k ResponseCompactParamsModel = "gpt-4-32k"

const ResponseCompactParamsModelGPT4\_32k0314 ResponseCompactParamsModel = "gpt-4-32k-0314"

const ResponseCompactParamsModelGPT4\_32k0613 ResponseCompactParamsModel = "gpt-4-32k-0613"

const ResponseCompactParamsModelGPT3\_5Turbo ResponseCompactParamsModel = "gpt-3.5-turbo"

const ResponseCompactParamsModelGPT3\_5Turbo16k ResponseCompactParamsModel = "gpt-3.5-turbo-16k"

const ResponseCompactParamsModelGPT3\_5Turbo0301 ResponseCompactParamsModel = "gpt-3.5-turbo-0301"

const ResponseCompactParamsModelGPT3\_5Turbo0613 ResponseCompactParamsModel = "gpt-3.5-turbo-0613"

const ResponseCompactParamsModelGPT3\_5Turbo1106 ResponseCompactParamsModel = "gpt-3.5-turbo-1106"

const ResponseCompactParamsModelGPT3\_5Turbo0125 ResponseCompactParamsModel = "gpt-3.5-turbo-0125"

const ResponseCompactParamsModelGPT3\_5Turbo16k0613 ResponseCompactParamsModel = "gpt-3.5-turbo-16k-0613"

const ResponseCompactParamsModelO1Pro ResponseCompactParamsModel = "o1-pro"

const ResponseCompactParamsModelO1Pro2025\_03\_19 ResponseCompactParamsModel = "o1-pro-2025-03-19"

const ResponseCompactParamsModelO3Pro ResponseCompactParamsModel = "o3-pro"

const ResponseCompactParamsModelO3Pro2025\_06\_10 ResponseCompactParamsModel = "o3-pro-2025-06-10"

const ResponseCompactParamsModelO3DeepResearch ResponseCompactParamsModel = "o3-deep-research"

const ResponseCompactParamsModelO3DeepResearch2025\_06\_26 ResponseCompactParamsModel = "o3-deep-research-2025-06-26"

const ResponseCompactParamsModelO4MiniDeepResearch ResponseCompactParamsModel = "o4-mini-deep-research"

const ResponseCompactParamsModelO4MiniDeepResearch2025\_06\_26 ResponseCompactParamsModel = "o4-mini-deep-research-2025-06-26"

const ResponseCompactParamsModelComputerUsePreview ResponseCompactParamsModel = "computer-use-preview"

const ResponseCompactParamsModelComputerUsePreview2025\_03\_11 ResponseCompactParamsModel = "computer-use-preview-2025-03-11"

const ResponseCompactParamsModelGPT5Codex ResponseCompactParamsModel = "gpt-5-codex"

const ResponseCompactParamsModelGPT5Pro ResponseCompactParamsModel = "gpt-5-pro"

const ResponseCompactParamsModelGPT5Pro2025\_10\_06 ResponseCompactParamsModel = "gpt-5-pro-2025-10-06"

const ResponseCompactParamsModelGPT5\_1CodexMax ResponseCompactParamsModel = "gpt-5.1-codex-max"

string

Input param.Field[[ResponseCompactParamsInputUnion](/api/reference/go/resources/responses/methods/compact#(resource)%20responses%20%3E%20(method)%20compact%20%3E%20(params)%20default%20%3E%20(param)%20input%20%3E%20(schema))]Optional

Text, image, or file inputs to the model, used to generate a response

string

type ResponseCompactParamsInputArray [][ResponseInputItemUnion](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_item%20%3E%20(schema))

A list of one or many input items to the model, containing different content types.

One of the following:

type EasyInputMessage struct{…}

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

Content EasyInputMessageContentUnion

Text, image, or audio input to the model, used to generate a response.
Can also contain previous assistant responses.

One of the following:

string

type ResponseInputMessageContentList [][ResponseInputContentUnion](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_content%20%3E%20(schema))

A list of one or many input items to the model, containing different content
types.

One of the following:

type ResponseInputText struct{…}

A text input to the model.

Text string

The text input to the model.

Type InputText

The type of the input item. Always `input_text`.

type ResponseInputImage struct{…}

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

Detail ResponseInputImageDetail

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

One of the following:

const ResponseInputImageDetailLow ResponseInputImageDetail = "low"

const ResponseInputImageDetailHigh ResponseInputImageDetail = "high"

const ResponseInputImageDetailAuto ResponseInputImageDetail = "auto"

const ResponseInputImageDetailOriginal ResponseInputImageDetail = "original"

Type InputImage

The type of the input item. Always `input_image`.

FileID stringOptional

The ID of the file to be sent to the model.

ImageURL stringOptional

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

type ResponseInputFile struct{…}

A file input to the model.

Type InputFile

The type of the input item. Always `input_file`.

Detail ResponseInputFileDetailOptional

The detail level of the file to be sent to the model. Use `low` for the default rendering behavior, or `high` to render the file at higher quality. Defaults to `low`.

One of the following:

const ResponseInputFileDetailLow ResponseInputFileDetail = "low"

const ResponseInputFileDetailHigh ResponseInputFileDetail = "high"

FileData stringOptional

The content of the file to be sent to the model.

FileID stringOptional

The ID of the file to be sent to the model.

FileURL stringOptional

The URL of the file to be sent to the model.

formaturi

Filename stringOptional

The name of the file to be sent to the model.

Role EasyInputMessageRole

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

const EasyInputMessageRoleUser EasyInputMessageRole = "user"

const EasyInputMessageRoleAssistant EasyInputMessageRole = "assistant"

const EasyInputMessageRoleSystem EasyInputMessageRole = "system"

const EasyInputMessageRoleDeveloper EasyInputMessageRole = "developer"

Phase EasyInputMessagePhaseOptional

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

One of the following:

const EasyInputMessagePhaseCommentary EasyInputMessagePhase = "commentary"

const EasyInputMessagePhaseFinalAnswer EasyInputMessagePhase = "final\_answer"

Type EasyInputMessageTypeOptional

The type of the message input. Always `message`.

type ResponseInputItemMessage struct{…}

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role.

Content [ResponseInputMessageContentList](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_message_content_list%20%3E%20(schema))

A list of one or many input items to the model, containing different content
types.

One of the following:

type ResponseInputText struct{…}

A text input to the model.

Text string

The text input to the model.

Type InputText

The type of the input item. Always `input_text`.

type ResponseInputImage struct{…}

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

Detail ResponseInputImageDetail

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

One of the following:

const ResponseInputImageDetailLow ResponseInputImageDetail = "low"

const ResponseInputImageDetailHigh ResponseInputImageDetail = "high"

const ResponseInputImageDetailAuto ResponseInputImageDetail = "auto"

const ResponseInputImageDetailOriginal ResponseInputImageDetail = "original"

Type InputImage

The type of the input item. Always `input_image`.

FileID stringOptional

The ID of the file to be sent to the model.

ImageURL stringOptional

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

type ResponseInputFile struct{…}

A file input to the model.

Type InputFile

The type of the input item. Always `input_file`.

Detail ResponseInputFileDetailOptional

The detail level of the file to be sent to the model. Use `low` for the default rendering behavior, or `high` to render the file at higher quality. Defaults to `low`.

One of the following:

const ResponseInputFileDetailLow ResponseInputFileDetail = "low"

const ResponseInputFileDetailHigh ResponseInputFileDetail = "high"

FileData stringOptional

The content of the file to be sent to the model.

FileID stringOptional

The ID of the file to be sent to the model.

FileURL stringOptional

The URL of the file to be sent to the model.

formaturi

Filename stringOptional

The name of the file to be sent to the model.

Role string

The role of the message input. One of `user`, `system`, or `developer`.

One of the following:

const ResponseInputItemMessageRoleUser ResponseInputItemMessageRole = "user"

const ResponseInputItemMessageRoleSystem ResponseInputItemMessageRole = "system"

const ResponseInputItemMessageRoleDeveloper ResponseInputItemMessageRole = "developer"

Status stringOptional

The status of item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

One of the following:

const ResponseInputItemMessageStatusInProgress ResponseInputItemMessageStatus = "in\_progress"

const ResponseInputItemMessageStatusCompleted ResponseInputItemMessageStatus = "completed"

const ResponseInputItemMessageStatusIncomplete ResponseInputItemMessageStatus = "incomplete"

Type stringOptional

The type of the message input. Always set to `message`.

type ResponseOutputMessage struct{…}

An output message from the model.

ID string

The unique ID of the output message.

Content []ResponseOutputMessageContentUnion

The content of the output message.

One of the following:

type ResponseOutputText struct{…}

A text output from the model.

Annotations []ResponseOutputTextAnnotationUnion

The annotations of the text output.

One of the following:

type ResponseOutputTextAnnotationFileCitation struct{…}

A citation to a file.

FileID string

The ID of the file.

Filename string

The filename of the file cited.

Index int64

The index of the file in the list of files.

Type FileCitation

The type of the file citation. Always `file_citation`.

type ResponseOutputTextAnnotationURLCitation struct{…}

A citation for a web resource used to generate a model response.

EndIndex int64

The index of the last character of the URL citation in the message.

StartIndex int64

The index of the first character of the URL citation in the message.

Title string

The title of the web resource.

Type URLCitation

The type of the URL citation. Always `url_citation`.

URL string

The URL of the web resource.

formaturi

type ResponseOutputTextAnnotationContainerFileCitation struct{…}

A citation for a container file used to generate a model response.

ContainerID string

The ID of the container file.

EndIndex int64

The index of the last character of the container file citation in the message.

FileID string

The ID of the file.

Filename string

The filename of the container file cited.

StartIndex int64

The index of the first character of the container file citation in the message.

Type ContainerFileCitation

The type of the container file citation. Always `container_file_citation`.

type ResponseOutputTextAnnotationFilePath struct{…}

A path to a file.

FileID string

The ID of the file.

Index int64

The index of the file in the list of files.

Type FilePath

The type of the file path. Always `file_path`.

Text string

The text output from the model.

Type OutputText

The type of the output text. Always `output_text`.

Logprobs []ResponseOutputTextLogprobOptional

Token string

Bytes []int64

Logprob float64

TopLogprobs []ResponseOutputTextLogprobTopLogprob

Token string

Bytes []int64

Logprob float64

type ResponseOutputRefusal struct{…}

A refusal from the model.

Refusal string

The refusal explanation from the model.

Type Refusal

The type of the refusal. Always `refusal`.

Role Assistant

The role of the output message. Always `assistant`.

Status ResponseOutputMessageStatus

The status of the message input. One of `in_progress`, `completed`, or
`incomplete`. Populated when input items are returned via API.

One of the following:

const ResponseOutputMessageStatusInProgress ResponseOutputMessageStatus = "in\_progress"

const ResponseOutputMessageStatusCompleted ResponseOutputMessageStatus = "completed"

const ResponseOutputMessageStatusIncomplete ResponseOutputMessageStatus = "incomplete"

Type Message

The type of the output message. Always `message`.

Phase ResponseOutputMessagePhaseOptional

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

One of the following:

const ResponseOutputMessagePhaseCommentary ResponseOutputMessagePhase = "commentary"

const ResponseOutputMessagePhaseFinalAnswer ResponseOutputMessagePhase = "final\_answer"

type ResponseFileSearchToolCall struct{…}

The results of a file search tool call. See the
[file search guide](https://platform.openai.com/docs/guides/tools-file-search) for more information.

ID string

The unique ID of the file search tool call.

Queries []string

The queries used to search for files.

Status ResponseFileSearchToolCallStatus

The status of the file search tool call. One of `in_progress`,
`searching`, `incomplete` or `failed`,

One of the following:

const ResponseFileSearchToolCallStatusInProgress ResponseFileSearchToolCallStatus = "in\_progress"

const ResponseFileSearchToolCallStatusSearching ResponseFileSearchToolCallStatus = "searching"

const ResponseFileSearchToolCallStatusCompleted ResponseFileSearchToolCallStatus = "completed"

const ResponseFileSearchToolCallStatusIncomplete ResponseFileSearchToolCallStatus = "incomplete"

const ResponseFileSearchToolCallStatusFailed ResponseFileSearchToolCallStatus = "failed"

Type FileSearchCall

The type of the file search tool call. Always `file_search_call`.

Results []ResponseFileSearchToolCallResultOptional

The results of the file search tool call.

Attributes map[string, ResponseFileSearchToolCallResultAttributeUnion]Optional

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.

One of the following:

string

float64

bool

FileID stringOptional

The unique ID of the file.

Filename stringOptional

The name of the file.

Score float64Optional

The relevance score of the file - a value between 0 and 1.

formatfloat

Text stringOptional

The text that was retrieved from the file.

type ResponseComputerToolCall struct{…}

A tool call to a computer use tool. See the
[computer use guide](https://platform.openai.com/docs/guides/tools-computer-use) for more information.

ID string

The unique ID of the computer call.

CallID string

An identifier used when responding to the tool call with output.

PendingSafetyChecks []ResponseComputerToolCallPendingSafetyCheck

The pending safety checks for the computer call.

ID string

The ID of the pending safety check.

Code stringOptional

The type of the pending safety check.

Message stringOptional

Details about the pending safety check.

Status ResponseComputerToolCallStatus

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

One of the following:

const ResponseComputerToolCallStatusInProgress ResponseComputerToolCallStatus = "in\_progress"

const ResponseComputerToolCallStatusCompleted ResponseComputerToolCallStatus = "completed"

const ResponseComputerToolCallStatusIncomplete ResponseComputerToolCallStatus = "incomplete"

Type ResponseComputerToolCallType

The type of the computer call. Always `computer_call`.

Action ResponseComputerToolCallActionUnionOptional

A click action.

One of the following:

type ResponseComputerToolCallActionClick struct{…}

A click action.

Button string

Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

One of the following:

const ResponseComputerToolCallActionClickButtonLeft ResponseComputerToolCallActionClickButton = "left"

const ResponseComputerToolCallActionClickButtonRight ResponseComputerToolCallActionClickButton = "right"

const ResponseComputerToolCallActionClickButtonWheel ResponseComputerToolCallActionClickButton = "wheel"

const ResponseComputerToolCallActionClickButtonBack ResponseComputerToolCallActionClickButton = "back"

const ResponseComputerToolCallActionClickButtonForward ResponseComputerToolCallActionClickButton = "forward"

Type Click

Specifies the event type. For a click action, this property is always `click`.

X int64

The x-coordinate where the click occurred.

Y int64

The y-coordinate where the click occurred.

Keys []stringOptional

The keys being held while clicking.

type ResponseComputerToolCallActionDoubleClick struct{…}

A double click action.

Keys []string

The keys being held while double-clicking.

Type DoubleClick

Specifies the event type. For a double click action, this property is always set to `double_click`.

X int64

The x-coordinate where the double click occurred.

Y int64

The y-coordinate where the double click occurred.

type ResponseComputerToolCallActionDrag struct{…}

A drag action.

Path []ResponseComputerToolCallActionDragPath

An array of coordinates representing the path of the drag action. Coordinates will appear as an array of objects, eg

[
  { x: 100, y: 200 },
  { x: 200, y: 300 }
]

X int64

The x-coordinate.

Y int64

The y-coordinate.

Type Drag

Specifies the event type. For a drag action, this property is always set to `drag`.

Keys []stringOptional

The keys being held while dragging the mouse.

type ResponseComputerToolCallActionKeypress struct{…}

A collection of keypresses the model would like to perform.

Keys []string

The combination of keys the model is requesting to be pressed. This is an array of strings, each representing a key.

Type Keypress

Specifies the event type. For a keypress action, this property is always set to `keypress`.

type ResponseComputerToolCallActionMove struct{…}

A mouse move action.

Type Move

Specifies the event type. For a move action, this property is always set to `move`.

X int64

The x-coordinate to move to.

Y int64

The y-coordinate to move to.

Keys []stringOptional

The keys being held while moving the mouse.

type ResponseComputerToolCallActionScreenshot struct{…}

A screenshot action.

Type Screenshot

Specifies the event type. For a screenshot action, this property is always set to `screenshot`.

type ResponseComputerToolCallActionScroll struct{…}

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

type ResponseComputerToolCallActionType struct{…}

An action to type in text.

Text string

The text to type.

Type Type

Specifies the event type. For a type action, this property is always set to `type`.

type ResponseComputerToolCallActionWait struct{…}

A wait action.

Type Wait

Specifies the event type. For a wait action, this property is always set to `wait`.

Actions [ComputerActionList](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20computer_action_list%20%3E%20(schema))Optional

Flattened batched actions for `computer_use`. Each action includes an
`type` discriminator and action-specific fields.

One of the following:

type ComputerActionClick struct{…}

A click action.

Button string

Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

One of the following:

const ComputerActionClickButtonLeft ComputerActionClickButton = "left"

const ComputerActionClickButtonRight ComputerActionClickButton = "right"

const ComputerActionClickButtonWheel ComputerActionClickButton = "wheel"

const ComputerActionClickButtonBack ComputerActionClickButton = "back"

const ComputerActionClickButtonForward ComputerActionClickButton = "forward"

Type Click

Specifies the event type. For a click action, this property is always `click`.

X int64

The x-coordinate where the click occurred.

Y int64

The y-coordinate where the click occurred.

Keys []stringOptional

The keys being held while clicking.

type ComputerActionDoubleClick struct{…}

A double click action.

Keys []string

The keys being held while double-clicking.

Type DoubleClick

Specifies the event type. For a double click action, this property is always set to `double_click`.

X int64

The x-coordinate where the double click occurred.

Y int64

The y-coordinate where the double click occurred.

type ComputerActionDrag struct{…}

A drag action.

Path []ComputerActionDragPath

An array of coordinates representing the path of the drag action. Coordinates will appear as an array of objects, eg

[
  { x: 100, y: 200 },
  { x: 200, y: 300 }
]

X int64

The x-coordinate.

Y int64

The y-coordinate.

Type Drag

Specifies the event type. For a drag action, this property is always set to `drag`.

Keys []stringOptional

The keys being held while dragging the mouse.

type ComputerActionKeypress struct{…}

A collection of keypresses the model would like to perform.

Keys []string

The combination of keys the model is requesting to be pressed. This is an array of strings, each representing a key.

Type Keypress

Specifies the event type. For a keypress action, this property is always set to `keypress`.

type ComputerActionMove struct{…}

A mouse move action.

Type Move

Specifies the event type. For a move action, this property is always set to `move`.

X int64

The x-coordinate to move to.

Y int64

The y-coordinate to move to.

Keys []stringOptional

The keys being held while moving the mouse.

type ComputerActionScreenshot struct{…}

A screenshot action.

Type Screenshot

Specifies the event type. For a screenshot action, this property is always set to `screenshot`.

type ComputerActionScroll struct{…}

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

type ComputerActionType struct{…}

An action to type in text.

Text string

The text to type.

Type Type

Specifies the event type. For a type action, this property is always set to `type`.

type ComputerActionWait struct{…}

A wait action.

Type Wait

Specifies the event type. For a wait action, this property is always set to `wait`.

type ResponseInputItemComputerCallOutput struct{…}

The output of a computer tool call.

CallID string

The ID of the computer tool call that produced the output.

maxLength64

minLength1

Output [ResponseComputerToolCallOutputScreenshot](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20response_computer_tool_call_output_screenshot%20%3E%20(schema))

A computer screenshot image used with the computer use tool.

Type ComputerScreenshot

Specifies the event type. For a computer screenshot, this property is
always set to `computer_screenshot`.

FileID stringOptional

The identifier of an uploaded file that contains the screenshot.

ImageURL stringOptional

The URL of the screenshot image.

formaturi

Type ComputerCallOutput

The type of the computer tool call output. Always `computer_call_output`.

ID stringOptional

The ID of the computer tool call output.

AcknowledgedSafetyChecks []ResponseInputItemComputerCallOutputAcknowledgedSafetyCheckOptional

The safety checks reported by the API that have been acknowledged by the developer.

ID string

The ID of the pending safety check.

Code stringOptional

The type of the pending safety check.

Message stringOptional

Details about the pending safety check.

Status stringOptional

The status of the message input. One of `in_progress`, `completed`, or `incomplete`. Populated when input items are returned via API.

One of the following:

const ResponseInputItemComputerCallOutputStatusInProgress ResponseInputItemComputerCallOutputStatus = "in\_progress"

const ResponseInputItemComputerCallOutputStatusCompleted ResponseInputItemComputerCallOutputStatus = "completed"

const ResponseInputItemComputerCallOutputStatusIncomplete ResponseInputItemComputerCallOutputStatus = "incomplete"

type ResponseFunctionWebSearch struct{…}

The results of a web search tool call. See the
[web search guide](https://platform.openai.com/docs/guides/tools-web-search) for more information.

ID string

The unique ID of the web search tool call.

Action ResponseFunctionWebSearchActionUnion

An object describing the specific action taken in this web search call.
Includes details on how the model used the web (search, open\_page, find\_in\_page).

One of the following:

type ResponseFunctionWebSearchActionSearch struct{…}

Action type “search” - Performs a web search query.

Type Search

The action type.

Queries []stringOptional

The search queries.

DeprecatedQuery stringOptional

The search query.

Sources []ResponseFunctionWebSearchActionSearchSourceOptional

The sources used in the search.

Type URL

The type of source. Always `url`.

URL string

The URL of the source.

formaturi

type ResponseFunctionWebSearchActionOpenPage struct{…}

Action type “open\_page” - Opens a specific URL from search results.

Type OpenPage

The action type.

URL stringOptional

The URL opened by the model.

formaturi

type ResponseFunctionWebSearchActionFindInPage struct{…}

Action type “find\_in\_page”: Searches for a pattern within a loaded page.

Pattern string

The pattern or text to search for within the page.

Type FindInPage

The action type.

URL string

The URL of the page searched for the pattern.

formaturi

Status ResponseFunctionWebSearchStatus

The status of the web search tool call.

One of the following:

const ResponseFunctionWebSearchStatusInProgress ResponseFunctionWebSearchStatus = "in\_progress"

const ResponseFunctionWebSearchStatusSearching ResponseFunctionWebSearchStatus = "searching"

const ResponseFunctionWebSearchStatusCompleted ResponseFunctionWebSearchStatus = "completed"

const ResponseFunctionWebSearchStatusFailed ResponseFunctionWebSearchStatus = "failed"

Type WebSearchCall

The type of the web search tool call. Always `web_search_call`.

type ResponseFunctionToolCall struct{…}

A tool call to run a function. See the
[function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.

Arguments string

A JSON string of the arguments to pass to the function.

CallID string

The unique ID of the function tool call generated by the model.

Name string

The name of the function to run.

Type FunctionCall

The type of the function tool call. Always `function_call`.

ID stringOptional

The unique ID of the function tool call.

Namespace stringOptional

The namespace of the function to run.

Status ResponseFunctionToolCallStatusOptional

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

One of the following:

const ResponseFunctionToolCallStatusInProgress ResponseFunctionToolCallStatus = "in\_progress"

const ResponseFunctionToolCallStatusCompleted ResponseFunctionToolCallStatus = "completed"

const ResponseFunctionToolCallStatusIncomplete ResponseFunctionToolCallStatus = "incomplete"

type ResponseInputItemFunctionCallOutput struct{…}

The output of a function tool call.

CallID string

The unique ID of the function tool call generated by the model.

maxLength64

minLength1

Output ResponseInputItemFunctionCallOutputOutputUnion

Text, image, or file output of the function tool call.

One of the following:

string

type ResponseFunctionCallOutputItemList [][ResponseFunctionCallOutputItemUnion](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20response_function_call_output_item%20%3E%20(schema))

An array of content outputs (text, image, file) for the function tool call.

One of the following:

type ResponseInputTextContent struct{…}

A text input to the model.

Text string

The text input to the model.

maxLength10485760

Type InputText

The type of the input item. Always `input_text`.

type ResponseInputImageContent struct{…}

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision)

Type InputImage

The type of the input item. Always `input_image`.

Detail ResponseInputImageContentDetailOptional

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

One of the following:

const ResponseInputImageContentDetailLow ResponseInputImageContentDetail = "low"

const ResponseInputImageContentDetailHigh ResponseInputImageContentDetail = "high"

const ResponseInputImageContentDetailAuto ResponseInputImageContentDetail = "auto"

const ResponseInputImageContentDetailOriginal ResponseInputImageContentDetail = "original"

FileID stringOptional

The ID of the file to be sent to the model.

ImageURL stringOptional

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

maxLength20971520

formaturi

type ResponseInputFileContent struct{…}

A file input to the model.

Type InputFile

The type of the input item. Always `input_file`.

Detail ResponseInputFileContentDetailOptional

The detail level of the file to be sent to the model. Use `low` for the default rendering behavior, or `high` to render the file at higher quality. Defaults to `low`.

One of the following:

const ResponseInputFileContentDetailLow ResponseInputFileContentDetail = "low"

const ResponseInputFileContentDetailHigh ResponseInputFileContentDetail = "high"

FileData stringOptional

The base64-encoded data of the file to be sent to the model.

maxLength73400320

FileID stringOptional

The ID of the file to be sent to the model.

FileURL stringOptional

The URL of the file to be sent to the model.

formaturi

Filename stringOptional

The name of the file to be sent to the model.

Type FunctionCallOutput

The type of the function tool call output. Always `function_call_output`.

ID stringOptional

The unique ID of the function tool call output. Populated when this item is returned via API.

Status stringOptional

The status of the item. One of `in_progress`, `completed`, or `incomplete`. Populated when items are returned via API.

One of the following:

const ResponseInputItemFunctionCallOutputStatusInProgress ResponseInputItemFunctionCallOutputStatus = "in\_progress"

const ResponseInputItemFunctionCallOutputStatusCompleted ResponseInputItemFunctionCallOutputStatus = "completed"

const ResponseInputItemFunctionCallOutputStatusIncomplete ResponseInputItemFunctionCallOutputStatus = "incomplete"

type ResponseInputItemToolSearchCall struct{…}

Arguments any

The arguments supplied to the tool search call.

Type ToolSearchCall

The item type. Always `tool_search_call`.

ID stringOptional

The unique ID of this tool search call.

CallID stringOptional

The unique ID of the tool search call generated by the model.

maxLength64

minLength1

Execution stringOptional

Whether tool search was executed by the server or by the client.

One of the following:

const ResponseInputItemToolSearchCallExecutionServer ResponseInputItemToolSearchCallExecution = "server"

const ResponseInputItemToolSearchCallExecutionClient ResponseInputItemToolSearchCallExecution = "client"

Status stringOptional

The status of the tool search call.

One of the following:

const ResponseInputItemToolSearchCallStatusInProgress ResponseInputItemToolSearchCallStatus = "in\_progress"

const ResponseInputItemToolSearchCallStatusCompleted ResponseInputItemToolSearchCallStatus = "completed"

const ResponseInputItemToolSearchCallStatusIncomplete ResponseInputItemToolSearchCallStatus = "incomplete"

type ResponseToolSearchOutputItemParamResp struct{…}

Tools [][ToolUnion](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20tool%20%3E%20(schema))

The loaded tool definitions returned by the tool search output.

One of the following:

type FunctionTool struct{…}

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

Name string

The name of the function to call.

Parameters map[string, any]

A JSON schema object describing the parameters of the function.

Strict bool

Whether to enforce strict parameter validation. Default `true`.

Type Function

The type of the function tool. Always `function`.

DeferLoading boolOptional

Whether this function is deferred and loaded via tool search.

Description stringOptional

A description of the function. Used by the model to determine whether or not to call the function.

type FileSearchTool struct{…}

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

Type FileSearch

The type of the file search tool. Always `file_search`.

VectorStoreIDs []string

The IDs of the vector stores to search.

Filters FileSearchToolFiltersUnionOptional

A filter to apply.

One of the following:

type ComparisonFilter struct{…}

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

Key string

The key to compare against the value.

Type ComparisonFilterType

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

const ComparisonFilterTypeEq ComparisonFilterType = "eq"

const ComparisonFilterTypeNe ComparisonFilterType = "ne"

const ComparisonFilterTypeGt ComparisonFilterType = "gt"

const ComparisonFilterTypeGte ComparisonFilterType = "gte"

const ComparisonFilterTypeLt ComparisonFilterType = "lt"

const ComparisonFilterTypeLte ComparisonFilterType = "lte"

const ComparisonFilterTypeIn ComparisonFilterType = "in"

const ComparisonFilterTypeNin ComparisonFilterType = "nin"

Value ComparisonFilterValueUnion

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

string

float64

bool

type ComparisonFilterValueArray []ComparisonFilterValueArrayItemUnion

One of the following:

string

float64

type CompoundFilter struct{…}

Combine multiple filters using `and` or `or`.

Filters [][ComparisonFilter](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema))

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

One of the following:

type ComparisonFilter struct{…}

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

Key string

The key to compare against the value.

Type ComparisonFilterType

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

const ComparisonFilterTypeEq ComparisonFilterType = "eq"

const ComparisonFilterTypeNe ComparisonFilterType = "ne"

const ComparisonFilterTypeGt ComparisonFilterType = "gt"

const ComparisonFilterTypeGte ComparisonFilterType = "gte"

const ComparisonFilterTypeLt ComparisonFilterType = "lt"

const ComparisonFilterTypeLte ComparisonFilterType = "lte"

const ComparisonFilterTypeIn ComparisonFilterType = "in"

const ComparisonFilterTypeNin ComparisonFilterType = "nin"

Value ComparisonFilterValueUnion

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

string

float64

bool

type ComparisonFilterValueArray []ComparisonFilterValueArrayItemUnion

One of the following:

string

float64

Type CompoundFilterType

Type of operation: `and` or `or`.

One of the following:

const CompoundFilterTypeAnd CompoundFilterType = "and"

const CompoundFilterTypeOr CompoundFilterType = "or"

MaxNumResults int64Optional

The maximum number of results to return. This number should be between 1 and 50 inclusive.

RankingOptions FileSearchToolRankingOptionsOptional

Ranking options for search.

HybridSearch FileSearchToolRankingOptionsHybridSearchOptional

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

EmbeddingWeight float64

The weight of the embedding in the reciprocal ranking fusion.

TextWeight float64

The weight of the text in the reciprocal ranking fusion.

Ranker stringOptional

The ranker to use for the file search.

One of the following:

const FileSearchToolRankingOptionsRankerAuto FileSearchToolRankingOptionsRanker = "auto"

const FileSearchToolRankingOptionsRankerDefault2024\_11\_15 FileSearchToolRankingOptionsRanker = "default-2024-11-15"

ScoreThreshold float64Optional

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

type ComputerTool struct{…}

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

Type Computer

The type of the computer tool. Always `computer`.

type ComputerUsePreviewTool struct{…}

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

DisplayHeight int64

The height of the computer display.

DisplayWidth int64

The width of the computer display.

Environment ComputerUsePreviewToolEnvironment

The type of computer environment to control.

One of the following:

const ComputerUsePreviewToolEnvironmentWindows ComputerUsePreviewToolEnvironment = "windows"

const ComputerUsePreviewToolEnvironmentMac ComputerUsePreviewToolEnvironment = "mac"

const ComputerUsePreviewToolEnvironmentLinux ComputerUsePreviewToolEnvironment = "linux"

const ComputerUsePreviewToolEnvironmentUbuntu ComputerUsePreviewToolEnvironment = "ubuntu"

const ComputerUsePreviewToolEnvironmentBrowser ComputerUsePreviewToolEnvironment = "browser"

Type ComputerUsePreview

The type of the computer use tool. Always `computer_use_preview`.

type WebSearchTool struct{…}

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type WebSearchToolType

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

One of the following:

const WebSearchToolTypeWebSearch WebSearchToolType = "web\_search"

const WebSearchToolTypeWebSearch2025\_08\_26 WebSearchToolType = "web\_search\_2025\_08\_26"

Filters WebSearchToolFiltersOptional

Filters for the search.

AllowedDomains []stringOptional

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

SearchContextSize WebSearchToolSearchContextSizeOptional

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

const WebSearchToolSearchContextSizeLow WebSearchToolSearchContextSize = "low"

const WebSearchToolSearchContextSizeMedium WebSearchToolSearchContextSize = "medium"

const WebSearchToolSearchContextSizeHigh WebSearchToolSearchContextSize = "high"

UserLocation WebSearchToolUserLocationOptional

The approximate location of the user.

City stringOptional

Free text input for the city of the user, e.g. `San Francisco`.

Country stringOptional

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

Region stringOptional

Free text input for the region of the user, e.g. `California`.

Timezone stringOptional

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

Type stringOptional

The type of location approximation. Always `approximate`.

type ToolMcp struct{…}

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

ServerLabel string

A label for this MCP server, used to identify it in tool calls.

Type Mcp

The type of the MCP tool. Always `mcp`.

AllowedTools ToolMcpAllowedToolsUnionOptional

List of allowed tool names or a filter object.

One of the following:

type ToolMcpAllowedToolsMcpAllowedTools []string

A string array of allowed tool names

type ToolMcpAllowedToolsMcpToolFilter struct{…}

A filter object to specify which tools are allowed.

ReadOnly boolOptional

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

ToolNames []stringOptional

List of allowed tool names.

Authorization stringOptional

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

ConnectorID stringOptional

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

const ToolMcpConnectorIDConnectorDropbox ToolMcpConnectorID = "connector\_dropbox"

const ToolMcpConnectorIDConnectorGmail ToolMcpConnectorID = "connector\_gmail"

const ToolMcpConnectorIDConnectorGooglecalendar ToolMcpConnectorID = "connector\_googlecalendar"

const ToolMcpConnectorIDConnectorGoogledrive ToolMcpConnectorID = "connector\_googledrive"

const ToolMcpConnectorIDConnectorMicrosoftteams ToolMcpConnectorID = "connector\_microsoftteams"

const ToolMcpConnectorIDConnectorOutlookcalendar ToolMcpConnectorID = "connector\_outlookcalendar"

const ToolMcpConnectorIDConnectorOutlookemail ToolMcpConnectorID = "connector\_outlookemail"

const ToolMcpConnectorIDConnectorSharepoint ToolMcpConnectorID = "connector\_sharepoint"

DeferLoading boolOptional

Whether this MCP tool is deferred and discovered via tool search.

Headers map[string, string]Optional

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

RequireApproval ToolMcpRequireApprovalUnionOptional

Specify which of the MCP server’s tools require approval.

One of the following:

type ToolMcpRequireApprovalMcpToolApprovalFilter struct{…}

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

Always ToolMcpRequireApprovalMcpToolApprovalFilterAlwaysOptional

A filter object to specify which tools are allowed.

ReadOnly boolOptional

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

ToolNames []stringOptional

List of allowed tool names.

Never ToolMcpRequireApprovalMcpToolApprovalFilterNeverOptional

A filter object to specify which tools are allowed.

ReadOnly boolOptional

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

ToolNames []stringOptional

List of allowed tool names.

type ToolMcpRequireApprovalMcpToolApprovalSetting string

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

One of the following:

const ToolMcpRequireApprovalMcpToolApprovalSettingAlways ToolMcpRequireApprovalMcpToolApprovalSetting = "always"

const ToolMcpRequireApprovalMcpToolApprovalSettingNever ToolMcpRequireApprovalMcpToolApprovalSetting = "never"

ServerDescription stringOptional

Optional description of the MCP server, used to provide more context.

ServerURL stringOptional

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

TunnelID stringOptional

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

type ToolCodeInterpreter struct{…}

A tool that runs Python code to help generate a response to a prompt.

Container ToolCodeInterpreterContainerUnion

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

One of the following:

string

type ToolCodeInterpreterContainerCodeInterpreterContainerAuto struct{…}

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

Type Auto

Always `auto`.

FileIDs []stringOptional

An optional list of uploaded files to make available to your code.

MemoryLimit stringOptional

The memory limit for the code interpreter container.

One of the following:

const ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit1g ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit = "1g"

const ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit4g ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit = "4g"

const ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit16g ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit = "16g"

const ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit64g ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit = "64g"

NetworkPolicy ToolCodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicyUnionOptional

Network access policy for the container.

One of the following:

type ContainerNetworkPolicyDisabled struct{…}

Type Disabled

Disable outbound network access. Always `disabled`.

type ContainerNetworkPolicyAllowlist struct{…}

AllowedDomains []string

A list of allowed domains when type is `allowlist`.

Type Allowlist

Allow outbound network access only to specified domains. Always `allowlist`.

DomainSecrets [][ContainerNetworkPolicyDomainSecret](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema))Optional

Optional domain-scoped secrets for allowlisted domains.

Domain string

The domain associated with the secret.

minLength1

Name string

The name of the secret to inject for the domain.

minLength1

Value string

The secret value to inject for the domain.

maxLength10485760

minLength1

Type CodeInterpreter

The type of the code interpreter tool. Always `code_interpreter`.

type ToolImageGeneration struct{…}

A tool that generates images using the GPT image models.

Type ImageGeneration

The type of the image generation tool. Always `image_generation`.

Action stringOptional

Whether to generate a new image or edit an existing image. Default: `auto`.

One of the following:

const ToolImageGenerationActionGenerate ToolImageGenerationAction = "generate"

const ToolImageGenerationActionEdit ToolImageGenerationAction = "edit"

const ToolImageGenerationActionAuto ToolImageGenerationAction = "auto"

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

One of the following:

const ToolImageGenerationBackgroundTransparent ToolImageGenerationBackground = "transparent"

const ToolImageGenerationBackgroundOpaque ToolImageGenerationBackground = "opaque"

const ToolImageGenerationBackgroundAuto ToolImageGenerationBackground = "auto"

InputFidelity stringOptional

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

One of the following:

const ToolImageGenerationInputFidelityHigh ToolImageGenerationInputFidelity = "high"

const ToolImageGenerationInputFidelityLow ToolImageGenerationInputFidelity = "low"

InputImageMask ToolImageGenerationInputImageMaskOptional

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

FileID stringOptional

File ID for the mask image.

ImageURL stringOptional

Base64-encoded mask image.

Model stringOptional

The image generation model to use. Default: `gpt-image-1`.

One of the following:

string

string

One of the following:

const ToolImageGenerationModelGPTImage1 ToolImageGenerationModel = "gpt-image-1"

const ToolImageGenerationModelGPTImage1Mini ToolImageGenerationModel = "gpt-image-1-mini"

const ToolImageGenerationModelGPTImage2 ToolImageGenerationModel = "gpt-image-2"

const ToolImageGenerationModelGPTImage2\_2026\_04\_21 ToolImageGenerationModel = "gpt-image-2-2026-04-21"

const ToolImageGenerationModelGPTImage1\_5 ToolImageGenerationModel = "gpt-image-1.5"

const ToolImageGenerationModelChatgptImageLatest ToolImageGenerationModel = "chatgpt-image-latest"

Moderation stringOptional

Moderation level for the generated image. Default: `auto`.

One of the following:

const ToolImageGenerationModerationAuto ToolImageGenerationModeration = "auto"

const ToolImageGenerationModerationLow ToolImageGenerationModeration = "low"

OutputCompression int64Optional

Compression level for the output image. Default: 100.

minimum0

maximum100

OutputFormat stringOptional

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

One of the following:

const ToolImageGenerationOutputFormatPNG ToolImageGenerationOutputFormat = "png"

const ToolImageGenerationOutputFormatWebP ToolImageGenerationOutputFormat = "webp"

const ToolImageGenerationOutputFormatJPEG ToolImageGenerationOutputFormat = "jpeg"

PartialImages int64Optional

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

Quality stringOptional

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

One of the following:

const ToolImageGenerationQualityLow ToolImageGenerationQuality = "low"

const ToolImageGenerationQualityMedium ToolImageGenerationQuality = "medium"

const ToolImageGenerationQualityHigh ToolImageGenerationQuality = "high"

const ToolImageGenerationQualityAuto ToolImageGenerationQuality = "auto"

Size stringOptional

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

One of the following:

string

string

One of the following:

const ToolImageGenerationSize1024x1024 ToolImageGenerationSize = "1024x1024"

const ToolImageGenerationSize1024x1536 ToolImageGenerationSize = "1024x1536"

const ToolImageGenerationSize1536x1024 ToolImageGenerationSize = "1536x1024"

const ToolImageGenerationSizeAuto ToolImageGenerationSize = "auto"

type ToolLocalShell struct{…}

A tool that allows the model to execute shell commands in a local environment.

Type LocalShell

The type of the local shell tool. Always `local_shell`.

type FunctionShellTool struct{…}

A tool that allows the model to execute shell commands.

Type Shell

The type of the shell tool. Always `shell`.

Environment FunctionShellToolEnvironmentUnionOptional

One of the following:

type ContainerAuto struct{…}

Type ContainerAuto

Automatically creates a container for this request

FileIDs []stringOptional

An optional list of uploaded files to make available to your code.

MemoryLimit ContainerAutoMemoryLimitOptional

The memory limit for the container.

One of the following:

const ContainerAutoMemoryLimit1g ContainerAutoMemoryLimit = "1g"

const ContainerAutoMemoryLimit4g ContainerAutoMemoryLimit = "4g"

const ContainerAutoMemoryLimit16g ContainerAutoMemoryLimit = "16g"

const ContainerAutoMemoryLimit64g ContainerAutoMemoryLimit = "64g"

NetworkPolicy ContainerAutoNetworkPolicyUnionOptional

Network access policy for the container.

One of the following:

type ContainerNetworkPolicyDisabled struct{…}

Type Disabled

Disable outbound network access. Always `disabled`.

type ContainerNetworkPolicyAllowlist struct{…}

AllowedDomains []string

A list of allowed domains when type is `allowlist`.

Type Allowlist

Allow outbound network access only to specified domains. Always `allowlist`.

DomainSecrets [][ContainerNetworkPolicyDomainSecret](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema))Optional

Optional domain-scoped secrets for allowlisted domains.

Domain string

The domain associated with the secret.

minLength1

Name string

The name of the secret to inject for the domain.

minLength1

Value string

The secret value to inject for the domain.

maxLength10485760

minLength1

Skills []ContainerAutoSkillUnionOptional

An optional list of skills referenced by id or inline data.

One of the following:

type SkillReference struct{…}

SkillID string

The ID of the referenced skill.

maxLength64

minLength1

Type SkillReference

References a skill created with the /v1/skills endpoint.

Version stringOptional

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

type InlineSkill struct{…}

Description string

The description of the skill.

Name string

The name of the skill.

Source [InlineSkillSource](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill_source%20%3E%20(schema))

Inline skill payload

Data string

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

MediaType ApplicationZip

The media type of the inline skill payload. Must be `application/zip`.

Type Base64

The type of the inline skill source. Must be `base64`.

Type Inline

Defines an inline skill for this request.

type LocalEnvironment struct{…}

Type Local

Use a local computer environment.

Skills [][LocalSkill](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20local_skill%20%3E%20(schema))Optional

An optional list of skills.

Description string

The description of the skill.

Name string

The name of the skill.

Path string

The path to the directory containing the skill.

type ContainerReference struct{…}

ContainerID string

The ID of the referenced container.

Type ContainerReference

References a container created with the /v1/containers endpoint

type CustomTool struct{…}

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

Name string

The name of the custom tool, used to identify it in tool calls.

Type Custom

The type of the custom tool. Always `custom`.

DeferLoading boolOptional

Whether this tool should be deferred and discovered via tool search.

Description stringOptional

Optional description of the custom tool, used to provide more context.

Format [CustomToolInputFormatUnion](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))Optional

The input format for the custom tool. Default is unconstrained text.

One of the following:

type CustomToolInputFormatText struct{…}

Unconstrained free-form text.

Type Text

Unconstrained text format. Always `text`.

type CustomToolInputFormatGrammar struct{…}

A grammar defined by the user.

Definition string

The grammar definition.

Syntax string

The syntax of the grammar definition. One of `lark` or `regex`.

One of the following:

const CustomToolInputFormatGrammarSyntaxLark CustomToolInputFormatGrammarSyntax = "lark"

const CustomToolInputFormatGrammarSyntaxRegex CustomToolInputFormatGrammarSyntax = "regex"

Type Grammar

Grammar format. Always `grammar`.

type NamespaceTool struct{…}

Groups function/custom tools under a shared namespace.

Description string

A description of the namespace shown to the model.

minLength1

Name string

The namespace name used in tool calls (for example, `crm`).

minLength1

Tools []NamespaceToolToolUnion

The function/custom tools available inside this namespace.

One of the following:

type NamespaceToolToolFunction struct{…}

Name string

maxLength128

minLength1

Type Function

DeferLoading boolOptional

Whether this function should be deferred and discovered via tool search.

Description stringOptional

Parameters anyOptional

Strict boolOptional

type CustomTool struct{…}

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

Name string

The name of the custom tool, used to identify it in tool calls.

Type Custom

The type of the custom tool. Always `custom`.

DeferLoading boolOptional

Whether this tool should be deferred and discovered via tool search.

Description stringOptional

Optional description of the custom tool, used to provide more context.

Format [CustomToolInputFormatUnion](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))Optional

The input format for the custom tool. Default is unconstrained text.

One of the following:

type CustomToolInputFormatText struct{…}

Unconstrained free-form text.

Type Text

Unconstrained text format. Always `text`.

type CustomToolInputFormatGrammar struct{…}

A grammar defined by the user.

Definition string

The grammar definition.

Syntax string

The syntax of the grammar definition. One of `lark` or `regex`.

One of the following:

const CustomToolInputFormatGrammarSyntaxLark CustomToolInputFormatGrammarSyntax = "lark"

const CustomToolInputFormatGrammarSyntaxRegex CustomToolInputFormatGrammarSyntax = "regex"

Type Grammar

Grammar format. Always `grammar`.

Type Namespace

The type of the tool. Always `namespace`.

type ToolSearchTool struct{…}

Hosted or BYOT tool search configuration for deferred tools.

Type ToolSearch

The type of the tool. Always `tool_search`.

Description stringOptional

Description shown to the model for a client-executed tool search tool.

Execution ToolSearchToolExecutionOptional

Whether tool search is executed by the server or by the client.

One of the following:

const ToolSearchToolExecutionServer ToolSearchToolExecution = "server"

const ToolSearchToolExecutionClient ToolSearchToolExecution = "client"

Parameters anyOptional

Parameter schema for a client-executed tool search tool.

type WebSearchPreviewTool struct{…}

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type WebSearchPreviewToolType

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

One of the following:

const WebSearchPreviewToolTypeWebSearchPreview WebSearchPreviewToolType = "web\_search\_preview"

const WebSearchPreviewToolTypeWebSearchPreview2025\_03\_11 WebSearchPreviewToolType = "web\_search\_preview\_2025\_03\_11"

SearchContentTypes []stringOptional

One of the following:

const WebSearchPreviewToolSearchContentTypeText WebSearchPreviewToolSearchContentType = "text"

const WebSearchPreviewToolSearchContentTypeImage WebSearchPreviewToolSearchContentType = "image"

SearchContextSize WebSearchPreviewToolSearchContextSizeOptional

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

const WebSearchPreviewToolSearchContextSizeLow WebSearchPreviewToolSearchContextSize = "low"

const WebSearchPreviewToolSearchContextSizeMedium WebSearchPreviewToolSearchContextSize = "medium"

const WebSearchPreviewToolSearchContextSizeHigh WebSearchPreviewToolSearchContextSize = "high"

UserLocation WebSearchPreviewToolUserLocationOptional

The user’s location.

Type Approximate

The type of location approximation. Always `approximate`.

City stringOptional

Free text input for the city of the user, e.g. `San Francisco`.

Country stringOptional

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

Region stringOptional

Free text input for the region of the user, e.g. `California`.

Timezone stringOptional

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

type ApplyPatchTool struct{…}

Allows the assistant to create, delete, or update files using unified diffs.

Type ApplyPatch

The type of the tool. Always `apply_patch`.

Type ToolSearchOutput

The item type. Always `tool_search_output`.

ID stringOptional

The unique ID of this tool search output.

CallID stringOptional

The unique ID of the tool search call generated by the model.

maxLength64

minLength1

Execution ResponseToolSearchOutputItemParamExecutionOptional

Whether tool search was executed by the server or by the client.

One of the following:

const ResponseToolSearchOutputItemParamExecutionServer ResponseToolSearchOutputItemParamExecution = "server"

const ResponseToolSearchOutputItemParamExecutionClient ResponseToolSearchOutputItemParamExecution = "client"

Status ResponseToolSearchOutputItemParamStatusOptional

The status of the tool search output.

One of the following:

const ResponseToolSearchOutputItemParamStatusInProgress ResponseToolSearchOutputItemParamStatus = "in\_progress"

const ResponseToolSearchOutputItemParamStatusCompleted ResponseToolSearchOutputItemParamStatus = "completed"

const ResponseToolSearchOutputItemParamStatusIncomplete ResponseToolSearchOutputItemParamStatus = "incomplete"

type ResponseInputItemAdditionalTools struct{…}

Role Developer

The role that provided the additional tools. Only `developer` is supported.

Tools [][ToolUnion](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20tool%20%3E%20(schema))

A list of additional tools made available at this item.

One of the following:

type FunctionTool struct{…}

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

Name string

The name of the function to call.

Parameters map[string, any]

A JSON schema object describing the parameters of the function.

Strict bool

Whether to enforce strict parameter validation. Default `true`.

Type Function

The type of the function tool. Always `function`.

DeferLoading boolOptional

Whether this function is deferred and loaded via tool search.

Description stringOptional

A description of the function. Used by the model to determine whether or not to call the function.

type FileSearchTool struct{…}

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

Type FileSearch

The type of the file search tool. Always `file_search`.

VectorStoreIDs []string

The IDs of the vector stores to search.

Filters FileSearchToolFiltersUnionOptional

A filter to apply.

One of the following:

type ComparisonFilter struct{…}

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

Key string

The key to compare against the value.

Type ComparisonFilterType

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

const ComparisonFilterTypeEq ComparisonFilterType = "eq"

const ComparisonFilterTypeNe ComparisonFilterType = "ne"

const ComparisonFilterTypeGt ComparisonFilterType = "gt"

const ComparisonFilterTypeGte ComparisonFilterType = "gte"

const ComparisonFilterTypeLt ComparisonFilterType = "lt"

const ComparisonFilterTypeLte ComparisonFilterType = "lte"

const ComparisonFilterTypeIn ComparisonFilterType = "in"

const ComparisonFilterTypeNin ComparisonFilterType = "nin"

Value ComparisonFilterValueUnion

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

string

float64

bool

type ComparisonFilterValueArray []ComparisonFilterValueArrayItemUnion

One of the following:

string

float64

type CompoundFilter struct{…}

Combine multiple filters using `and` or `or`.

Filters [][ComparisonFilter](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema))

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

One of the following:

type ComparisonFilter struct{…}

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

Key string

The key to compare against the value.

Type ComparisonFilterType

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

const ComparisonFilterTypeEq ComparisonFilterType = "eq"

const ComparisonFilterTypeNe ComparisonFilterType = "ne"

const ComparisonFilterTypeGt ComparisonFilterType = "gt"

const ComparisonFilterTypeGte ComparisonFilterType = "gte"

const ComparisonFilterTypeLt ComparisonFilterType = "lt"

const ComparisonFilterTypeLte ComparisonFilterType = "lte"

const ComparisonFilterTypeIn ComparisonFilterType = "in"

const ComparisonFilterTypeNin ComparisonFilterType = "nin"

Value ComparisonFilterValueUnion

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

string

float64

bool

type ComparisonFilterValueArray []ComparisonFilterValueArrayItemUnion

One of the following:

string

float64

Type CompoundFilterType

Type of operation: `and` or `or`.

One of the following:

const CompoundFilterTypeAnd CompoundFilterType = "and"

const CompoundFilterTypeOr CompoundFilterType = "or"

MaxNumResults int64Optional

The maximum number of results to return. This number should be between 1 and 50 inclusive.

RankingOptions FileSearchToolRankingOptionsOptional

Ranking options for search.

HybridSearch FileSearchToolRankingOptionsHybridSearchOptional

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

EmbeddingWeight float64

The weight of the embedding in the reciprocal ranking fusion.

TextWeight float64

The weight of the text in the reciprocal ranking fusion.

Ranker stringOptional

The ranker to use for the file search.

One of the following:

const FileSearchToolRankingOptionsRankerAuto FileSearchToolRankingOptionsRanker = "auto"

const FileSearchToolRankingOptionsRankerDefault2024\_11\_15 FileSearchToolRankingOptionsRanker = "default-2024-11-15"

ScoreThreshold float64Optional

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

type ComputerTool struct{…}

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

Type Computer

The type of the computer tool. Always `computer`.

type ComputerUsePreviewTool struct{…}

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

DisplayHeight int64

The height of the computer display.

DisplayWidth int64

The width of the computer display.

Environment ComputerUsePreviewToolEnvironment

The type of computer environment to control.

One of the following:

const ComputerUsePreviewToolEnvironmentWindows ComputerUsePreviewToolEnvironment = "windows"

const ComputerUsePreviewToolEnvironmentMac ComputerUsePreviewToolEnvironment = "mac"

const ComputerUsePreviewToolEnvironmentLinux ComputerUsePreviewToolEnvironment = "linux"

const ComputerUsePreviewToolEnvironmentUbuntu ComputerUsePreviewToolEnvironment = "ubuntu"

const ComputerUsePreviewToolEnvironmentBrowser ComputerUsePreviewToolEnvironment = "browser"

Type ComputerUsePreview

The type of the computer use tool. Always `computer_use_preview`.

type WebSearchTool struct{…}

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type WebSearchToolType

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

One of the following:

const WebSearchToolTypeWebSearch WebSearchToolType = "web\_search"

const WebSearchToolTypeWebSearch2025\_08\_26 WebSearchToolType = "web\_search\_2025\_08\_26"

Filters WebSearchToolFiltersOptional

Filters for the search.

AllowedDomains []stringOptional

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

SearchContextSize WebSearchToolSearchContextSizeOptional

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

const WebSearchToolSearchContextSizeLow WebSearchToolSearchContextSize = "low"

const WebSearchToolSearchContextSizeMedium WebSearchToolSearchContextSize = "medium"

const WebSearchToolSearchContextSizeHigh WebSearchToolSearchContextSize = "high"

UserLocation WebSearchToolUserLocationOptional

The approximate location of the user.

City stringOptional

Free text input for the city of the user, e.g. `San Francisco`.

Country stringOptional

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

Region stringOptional

Free text input for the region of the user, e.g. `California`.

Timezone stringOptional

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

Type stringOptional

The type of location approximation. Always `approximate`.

type ToolMcp struct{…}

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

ServerLabel string

A label for this MCP server, used to identify it in tool calls.

Type Mcp

The type of the MCP tool. Always `mcp`.

AllowedTools ToolMcpAllowedToolsUnionOptional

List of allowed tool names or a filter object.

One of the following:

type ToolMcpAllowedToolsMcpAllowedTools []string

A string array of allowed tool names

type ToolMcpAllowedToolsMcpToolFilter struct{…}

A filter object to specify which tools are allowed.

ReadOnly boolOptional

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

ToolNames []stringOptional

List of allowed tool names.

Authorization stringOptional

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

ConnectorID stringOptional

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

const ToolMcpConnectorIDConnectorDropbox ToolMcpConnectorID = "connector\_dropbox"

const ToolMcpConnectorIDConnectorGmail ToolMcpConnectorID = "connector\_gmail"

const ToolMcpConnectorIDConnectorGooglecalendar ToolMcpConnectorID = "connector\_googlecalendar"

const ToolMcpConnectorIDConnectorGoogledrive ToolMcpConnectorID = "connector\_googledrive"

const ToolMcpConnectorIDConnectorMicrosoftteams ToolMcpConnectorID = "connector\_microsoftteams"

const ToolMcpConnectorIDConnectorOutlookcalendar ToolMcpConnectorID = "connector\_outlookcalendar"

const ToolMcpConnectorIDConnectorOutlookemail ToolMcpConnectorID = "connector\_outlookemail"

const ToolMcpConnectorIDConnectorSharepoint ToolMcpConnectorID = "connector\_sharepoint"

DeferLoading boolOptional

Whether this MCP tool is deferred and discovered via tool search.

Headers map[string, string]Optional

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

RequireApproval ToolMcpRequireApprovalUnionOptional

Specify which of the MCP server’s tools require approval.

One of the following:

type ToolMcpRequireApprovalMcpToolApprovalFilter struct{…}

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

Always ToolMcpRequireApprovalMcpToolApprovalFilterAlwaysOptional

A filter object to specify which tools are allowed.

ReadOnly boolOptional

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

ToolNames []stringOptional

List of allowed tool names.

Never ToolMcpRequireApprovalMcpToolApprovalFilterNeverOptional

A filter object to specify which tools are allowed.

ReadOnly boolOptional

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

ToolNames []stringOptional

List of allowed tool names.

type ToolMcpRequireApprovalMcpToolApprovalSetting string

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

One of the following:

const ToolMcpRequireApprovalMcpToolApprovalSettingAlways ToolMcpRequireApprovalMcpToolApprovalSetting = "always"

const ToolMcpRequireApprovalMcpToolApprovalSettingNever ToolMcpRequireApprovalMcpToolApprovalSetting = "never"

ServerDescription stringOptional

Optional description of the MCP server, used to provide more context.

ServerURL stringOptional

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

TunnelID stringOptional

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

type ToolCodeInterpreter struct{…}

A tool that runs Python code to help generate a response to a prompt.

Container ToolCodeInterpreterContainerUnion

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

One of the following:

string

type ToolCodeInterpreterContainerCodeInterpreterContainerAuto struct{…}

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

Type Auto

Always `auto`.

FileIDs []stringOptional

An optional list of uploaded files to make available to your code.

MemoryLimit stringOptional

The memory limit for the code interpreter container.

One of the following:

const ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit1g ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit = "1g"

const ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit4g ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit = "4g"

const ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit16g ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit = "16g"

const ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit64g ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit = "64g"

NetworkPolicy ToolCodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicyUnionOptional

Network access policy for the container.

One of the following:

type ContainerNetworkPolicyDisabled struct{…}

Type Disabled

Disable outbound network access. Always `disabled`.

type ContainerNetworkPolicyAllowlist struct{…}

AllowedDomains []string

A list of allowed domains when type is `allowlist`.

Type Allowlist

Allow outbound network access only to specified domains. Always `allowlist`.

DomainSecrets [][ContainerNetworkPolicyDomainSecret](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema))Optional

Optional domain-scoped secrets for allowlisted domains.

Domain string

The domain associated with the secret.

minLength1

Name string

The name of the secret to inject for the domain.

minLength1

Value string

The secret value to inject for the domain.

maxLength10485760

minLength1

Type CodeInterpreter

The type of the code interpreter tool. Always `code_interpreter`.

type ToolImageGeneration struct{…}

A tool that generates images using the GPT image models.

Type ImageGeneration

The type of the image generation tool. Always `image_generation`.

Action stringOptional

Whether to generate a new image or edit an existing image. Default: `auto`.

One of the following:

const ToolImageGenerationActionGenerate ToolImageGenerationAction = "generate"

const ToolImageGenerationActionEdit ToolImageGenerationAction = "edit"

const ToolImageGenerationActionAuto ToolImageGenerationAction = "auto"

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

One of the following:

const ToolImageGenerationBackgroundTransparent ToolImageGenerationBackground = "transparent"

const ToolImageGenerationBackgroundOpaque ToolImageGenerationBackground = "opaque"

const ToolImageGenerationBackgroundAuto ToolImageGenerationBackground = "auto"

InputFidelity stringOptional

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

One of the following:

const ToolImageGenerationInputFidelityHigh ToolImageGenerationInputFidelity = "high"

const ToolImageGenerationInputFidelityLow ToolImageGenerationInputFidelity = "low"

InputImageMask ToolImageGenerationInputImageMaskOptional

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

FileID stringOptional

File ID for the mask image.

ImageURL stringOptional

Base64-encoded mask image.

Model stringOptional

The image generation model to use. Default: `gpt-image-1`.

One of the following:

string

string

One of the following:

const ToolImageGenerationModelGPTImage1 ToolImageGenerationModel = "gpt-image-1"

const ToolImageGenerationModelGPTImage1Mini ToolImageGenerationModel = "gpt-image-1-mini"

const ToolImageGenerationModelGPTImage2 ToolImageGenerationModel = "gpt-image-2"

const ToolImageGenerationModelGPTImage2\_2026\_04\_21 ToolImageGenerationModel = "gpt-image-2-2026-04-21"

const ToolImageGenerationModelGPTImage1\_5 ToolImageGenerationModel = "gpt-image-1.5"

const ToolImageGenerationModelChatgptImageLatest ToolImageGenerationModel = "chatgpt-image-latest"

Moderation stringOptional

Moderation level for the generated image. Default: `auto`.

One of the following:

const ToolImageGenerationModerationAuto ToolImageGenerationModeration = "auto"

const ToolImageGenerationModerationLow ToolImageGenerationModeration = "low"

OutputCompression int64Optional

Compression level for the output image. Default: 100.

minimum0

maximum100

OutputFormat stringOptional

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

One of the following:

const ToolImageGenerationOutputFormatPNG ToolImageGenerationOutputFormat = "png"

const ToolImageGenerationOutputFormatWebP ToolImageGenerationOutputFormat = "webp"

const ToolImageGenerationOutputFormatJPEG ToolImageGenerationOutputFormat = "jpeg"

PartialImages int64Optional

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

Quality stringOptional

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

One of the following:

const ToolImageGenerationQualityLow ToolImageGenerationQuality = "low"

const ToolImageGenerationQualityMedium ToolImageGenerationQuality = "medium"

const ToolImageGenerationQualityHigh ToolImageGenerationQuality = "high"

const ToolImageGenerationQualityAuto ToolImageGenerationQuality = "auto"

Size stringOptional

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

One of the following:

string

string

One of the following:

const ToolImageGenerationSize1024x1024 ToolImageGenerationSize = "1024x1024"

const ToolImageGenerationSize1024x1536 ToolImageGenerationSize = "1024x1536"

const ToolImageGenerationSize1536x1024 ToolImageGenerationSize = "1536x1024"

const ToolImageGenerationSizeAuto ToolImageGenerationSize = "auto"

type ToolLocalShell struct{…}

A tool that allows the model to execute shell commands in a local environment.

Type LocalShell

The type of the local shell tool. Always `local_shell`.

type FunctionShellTool struct{…}

A tool that allows the model to execute shell commands.

Type Shell

The type of the shell tool. Always `shell`.

Environment FunctionShellToolEnvironmentUnionOptional

One of the following:

type ContainerAuto struct{…}

Type ContainerAuto

Automatically creates a container for this request

FileIDs []stringOptional

An optional list of uploaded files to make available to your code.

MemoryLimit ContainerAutoMemoryLimitOptional

The memory limit for the container.

One of the following:

const ContainerAutoMemoryLimit1g ContainerAutoMemoryLimit = "1g"

const ContainerAutoMemoryLimit4g ContainerAutoMemoryLimit = "4g"

const ContainerAutoMemoryLimit16g ContainerAutoMemoryLimit = "16g"

const ContainerAutoMemoryLimit64g ContainerAutoMemoryLimit = "64g"

NetworkPolicy ContainerAutoNetworkPolicyUnionOptional

Network access policy for the container.

One of the following:

type ContainerNetworkPolicyDisabled struct{…}

Type Disabled

Disable outbound network access. Always `disabled`.

type ContainerNetworkPolicyAllowlist struct{…}

AllowedDomains []string

A list of allowed domains when type is `allowlist`.

Type Allowlist

Allow outbound network access only to specified domains. Always `allowlist`.

DomainSecrets [][ContainerNetworkPolicyDomainSecret](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema))Optional

Optional domain-scoped secrets for allowlisted domains.

Domain string

The domain associated with the secret.

minLength1

Name string

The name of the secret to inject for the domain.

minLength1

Value string

The secret value to inject for the domain.

maxLength10485760

minLength1

Skills []ContainerAutoSkillUnionOptional

An optional list of skills referenced by id or inline data.

One of the following:

type SkillReference struct{…}

SkillID string

The ID of the referenced skill.

maxLength64

minLength1

Type SkillReference

References a skill created with the /v1/skills endpoint.

Version stringOptional

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

type InlineSkill struct{…}

Description string

The description of the skill.

Name string

The name of the skill.

Source [InlineSkillSource](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill_source%20%3E%20(schema))

Inline skill payload

Data string

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

MediaType ApplicationZip

The media type of the inline skill payload. Must be `application/zip`.

Type Base64

The type of the inline skill source. Must be `base64`.

Type Inline

Defines an inline skill for this request.

type LocalEnvironment struct{…}

Type Local

Use a local computer environment.

Skills [][LocalSkill](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20local_skill%20%3E%20(schema))Optional

An optional list of skills.

Description string

The description of the skill.

Name string

The name of the skill.

Path string

The path to the directory containing the skill.

type ContainerReference struct{…}

ContainerID string

The ID of the referenced container.

Type ContainerReference

References a container created with the /v1/containers endpoint

type CustomTool struct{…}

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

Name string

The name of the custom tool, used to identify it in tool calls.

Type Custom

The type of the custom tool. Always `custom`.

DeferLoading boolOptional

Whether this tool should be deferred and discovered via tool search.

Description stringOptional

Optional description of the custom tool, used to provide more context.

Format [CustomToolInputFormatUnion](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))Optional

The input format for the custom tool. Default is unconstrained text.

One of the following:

type CustomToolInputFormatText struct{…}

Unconstrained free-form text.

Type Text

Unconstrained text format. Always `text`.

type CustomToolInputFormatGrammar struct{…}

A grammar defined by the user.

Definition string

The grammar definition.

Syntax string

The syntax of the grammar definition. One of `lark` or `regex`.

One of the following:

const CustomToolInputFormatGrammarSyntaxLark CustomToolInputFormatGrammarSyntax = "lark"

const CustomToolInputFormatGrammarSyntaxRegex CustomToolInputFormatGrammarSyntax = "regex"

Type Grammar

Grammar format. Always `grammar`.

type NamespaceTool struct{…}

Groups function/custom tools under a shared namespace.

Description string

A description of the namespace shown to the model.

minLength1

Name string

The namespace name used in tool calls (for example, `crm`).

minLength1

Tools []NamespaceToolToolUnion

The function/custom tools available inside this namespace.

One of the following:

type NamespaceToolToolFunction struct{…}

Name string

maxLength128

minLength1

Type Function

DeferLoading boolOptional

Whether this function should be deferred and discovered via tool search.

Description stringOptional

Parameters anyOptional

Strict boolOptional

type CustomTool struct{…}

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

Name string

The name of the custom tool, used to identify it in tool calls.

Type Custom

The type of the custom tool. Always `custom`.

DeferLoading boolOptional

Whether this tool should be deferred and discovered via tool search.

Description stringOptional

Optional description of the custom tool, used to provide more context.

Format [CustomToolInputFormatUnion](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))Optional

The input format for the custom tool. Default is unconstrained text.

One of the following:

type CustomToolInputFormatText struct{…}

Unconstrained free-form text.

Type Text

Unconstrained text format. Always `text`.

type CustomToolInputFormatGrammar struct{…}

A grammar defined by the user.

Definition string

The grammar definition.

Syntax string

The syntax of the grammar definition. One of `lark` or `regex`.

One of the following:

const CustomToolInputFormatGrammarSyntaxLark CustomToolInputFormatGrammarSyntax = "lark"

const CustomToolInputFormatGrammarSyntaxRegex CustomToolInputFormatGrammarSyntax = "regex"

Type Grammar

Grammar format. Always `grammar`.

Type Namespace

The type of the tool. Always `namespace`.

type ToolSearchTool struct{…}

Hosted or BYOT tool search configuration for deferred tools.

Type ToolSearch

The type of the tool. Always `tool_search`.

Description stringOptional

Description shown to the model for a client-executed tool search tool.

Execution ToolSearchToolExecutionOptional

Whether tool search is executed by the server or by the client.

One of the following:

const ToolSearchToolExecutionServer ToolSearchToolExecution = "server"

const ToolSearchToolExecutionClient ToolSearchToolExecution = "client"

Parameters anyOptional

Parameter schema for a client-executed tool search tool.

type WebSearchPreviewTool struct{…}

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type WebSearchPreviewToolType

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

One of the following:

const WebSearchPreviewToolTypeWebSearchPreview WebSearchPreviewToolType = "web\_search\_preview"

const WebSearchPreviewToolTypeWebSearchPreview2025\_03\_11 WebSearchPreviewToolType = "web\_search\_preview\_2025\_03\_11"

SearchContentTypes []stringOptional

One of the following:

const WebSearchPreviewToolSearchContentTypeText WebSearchPreviewToolSearchContentType = "text"

const WebSearchPreviewToolSearchContentTypeImage WebSearchPreviewToolSearchContentType = "image"

SearchContextSize WebSearchPreviewToolSearchContextSizeOptional

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

const WebSearchPreviewToolSearchContextSizeLow WebSearchPreviewToolSearchContextSize = "low"

const WebSearchPreviewToolSearchContextSizeMedium WebSearchPreviewToolSearchContextSize = "medium"

const WebSearchPreviewToolSearchContextSizeHigh WebSearchPreviewToolSearchContextSize = "high"

UserLocation WebSearchPreviewToolUserLocationOptional

The user’s location.

Type Approximate

The type of location approximation. Always `approximate`.

City stringOptional

Free text input for the city of the user, e.g. `San Francisco`.

Country stringOptional

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

Region stringOptional

Free text input for the region of the user, e.g. `California`.

Timezone stringOptional

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

type ApplyPatchTool struct{…}

Allows the assistant to create, delete, or update files using unified diffs.

Type ApplyPatch

The type of the tool. Always `apply_patch`.

Type AdditionalTools

The item type. Always `additional_tools`.

ID stringOptional

The unique ID of this additional tools item.

type ResponseReasoningItem struct{…}

A description of the chain of thought used by a reasoning model while generating
a response. Be sure to include these items in your `input` to the Responses API
for subsequent turns of a conversation if you are manually
[managing context](https://platform.openai.com/docs/guides/conversation-state).

ID string

The unique identifier of the reasoning content.

Summary []ResponseReasoningItemSummary

Reasoning summary content.

Text string

A summary of the reasoning output from the model so far.

Type SummaryText

The type of the object. Always `summary_text`.

Type Reasoning

The type of the object. Always `reasoning`.

Content []ResponseReasoningItemContentOptional

Reasoning text content.

Text string

The reasoning text from the model.

Type ReasoningText

The type of the reasoning text. Always `reasoning_text`.

EncryptedContent stringOptional

The encrypted content of the reasoning item - populated when a response is
generated with `reasoning.encrypted_content` in the `include` parameter.

Status ResponseReasoningItemStatusOptional

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

One of the following:

const ResponseReasoningItemStatusInProgress ResponseReasoningItemStatus = "in\_progress"

const ResponseReasoningItemStatusCompleted ResponseReasoningItemStatus = "completed"

const ResponseReasoningItemStatusIncomplete ResponseReasoningItemStatus = "incomplete"

type ResponseCompactionItemParamResp struct{…}

A compaction item generated by the [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).

EncryptedContent string

The encrypted content of the compaction summary.

maxLength10485760

Type Compaction

The type of the item. Always `compaction`.

ID stringOptional

The ID of the compaction item.

type ResponseInputItemImageGenerationCall struct{…}

An image generation request made by the model.

ID string

The unique ID of the image generation call.

Result string

The generated image encoded in base64.

Status string

The status of the image generation call.

One of the following:

const ResponseInputItemImageGenerationCallStatusInProgress ResponseInputItemImageGenerationCallStatus = "in\_progress"

const ResponseInputItemImageGenerationCallStatusCompleted ResponseInputItemImageGenerationCallStatus = "completed"

const ResponseInputItemImageGenerationCallStatusGenerating ResponseInputItemImageGenerationCallStatus = "generating"

const ResponseInputItemImageGenerationCallStatusFailed ResponseInputItemImageGenerationCallStatus = "failed"

Type ImageGenerationCall

The type of the image generation call. Always `image_generation_call`.

type ResponseCodeInterpreterToolCall struct{…}

A tool call to run code.

ID string

The unique ID of the code interpreter tool call.

Code string

The code to run, or null if not available.

ContainerID string

The ID of the container used to run the code.

Outputs []ResponseCodeInterpreterToolCallOutputUnion

The outputs generated by the code interpreter, such as logs or images.
Can be null if no outputs are available.

One of the following:

type ResponseCodeInterpreterToolCallOutputLogs struct{…}

The logs output from the code interpreter.

Logs string

The logs output from the code interpreter.

Type Logs

The type of the output. Always `logs`.

type ResponseCodeInterpreterToolCallOutputImage struct{…}

The image output from the code interpreter.

Type Image

The type of the output. Always `image`.

URL string

The URL of the image output from the code interpreter.

formaturi

Status ResponseCodeInterpreterToolCallStatus

The status of the code interpreter tool call. Valid values are `in_progress`, `completed`, `incomplete`, `interpreting`, and `failed`.

One of the following:

const ResponseCodeInterpreterToolCallStatusInProgress ResponseCodeInterpreterToolCallStatus = "in\_progress"

const ResponseCodeInterpreterToolCallStatusCompleted ResponseCodeInterpreterToolCallStatus = "completed"

const ResponseCodeInterpreterToolCallStatusIncomplete ResponseCodeInterpreterToolCallStatus = "incomplete"

const ResponseCodeInterpreterToolCallStatusInterpreting ResponseCodeInterpreterToolCallStatus = "interpreting"

const ResponseCodeInterpreterToolCallStatusFailed ResponseCodeInterpreterToolCallStatus = "failed"

Type CodeInterpreterCall

The type of the code interpreter tool call. Always `code_interpreter_call`.

type ResponseInputItemLocalShellCall struct{…}

A tool call to run a command on the local shell.

ID string

The unique ID of the local shell call.

Action ResponseInputItemLocalShellCallAction

Execute a shell command on the server.

Command []string

The command to run.

Env map[string, string]

Environment variables to set for the command.

Type Exec

The type of the local shell action. Always `exec`.

TimeoutMs int64Optional

Optional timeout in milliseconds for the command.

User stringOptional

Optional user to run the command as.

WorkingDirectory stringOptional

Optional working directory to run the command in.

CallID string

The unique ID of the local shell tool call generated by the model.

Status string

The status of the local shell call.

One of the following:

const ResponseInputItemLocalShellCallStatusInProgress ResponseInputItemLocalShellCallStatus = "in\_progress"

const ResponseInputItemLocalShellCallStatusCompleted ResponseInputItemLocalShellCallStatus = "completed"

const ResponseInputItemLocalShellCallStatusIncomplete ResponseInputItemLocalShellCallStatus = "incomplete"

Type LocalShellCall

The type of the local shell call. Always `local_shell_call`.

type ResponseInputItemLocalShellCallOutput struct{…}

The output of a local shell tool call.

ID string

The unique ID of the local shell tool call generated by the model.

Output string

A JSON string of the output of the local shell tool call.

Type LocalShellCallOutput

The type of the local shell tool call output. Always `local_shell_call_output`.

Status stringOptional

The status of the item. One of `in_progress`, `completed`, or `incomplete`.

One of the following:

const ResponseInputItemLocalShellCallOutputStatusInProgress ResponseInputItemLocalShellCallOutputStatus = "in\_progress"

const ResponseInputItemLocalShellCallOutputStatusCompleted ResponseInputItemLocalShellCallOutputStatus = "completed"

const ResponseInputItemLocalShellCallOutputStatusIncomplete ResponseInputItemLocalShellCallOutputStatus = "incomplete"

type ResponseInputItemShellCall struct{…}

A tool representing a request to execute one or more shell commands.

Action ResponseInputItemShellCallAction

The shell commands and limits that describe how to run the tool call.

Commands []string

Ordered shell commands for the execution environment to run.

MaxOutputLength int64Optional

Maximum number of UTF-8 characters to capture from combined stdout and stderr output.

TimeoutMs int64Optional

Maximum wall-clock time in milliseconds to allow the shell commands to run.

CallID string

The unique ID of the shell tool call generated by the model.

maxLength64

minLength1

Type ShellCall

The type of the item. Always `shell_call`.

ID stringOptional

The unique ID of the shell tool call. Populated when this item is returned via API.

Environment ResponseInputItemShellCallEnvironmentUnionOptional

The environment to execute the shell commands in.

One of the following:

type LocalEnvironment struct{…}

Type Local

Use a local computer environment.

Skills [][LocalSkill](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20local_skill%20%3E%20(schema))Optional

An optional list of skills.

Description string

The description of the skill.

Name string

The name of the skill.

Path string

The path to the directory containing the skill.

type ContainerReference struct{…}

ContainerID string

The ID of the referenced container.

Type ContainerReference

References a container created with the /v1/containers endpoint

Status stringOptional

The status of the shell call. One of `in_progress`, `completed`, or `incomplete`.

One of the following:

const ResponseInputItemShellCallStatusInProgress ResponseInputItemShellCallStatus = "in\_progress"

const ResponseInputItemShellCallStatusCompleted ResponseInputItemShellCallStatus = "completed"

const ResponseInputItemShellCallStatusIncomplete ResponseInputItemShellCallStatus = "incomplete"

type ResponseInputItemShellCallOutput struct{…}

The streamed output items emitted by a shell tool call.

CallID string

The unique ID of the shell tool call generated by the model.

maxLength64

minLength1

Output [][ResponseFunctionShellCallOutputContent](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20response_function_shell_call_output_content%20%3E%20(schema))

Captured chunks of stdout and stderr output, along with their associated outcomes.

Outcome ResponseFunctionShellCallOutputContentOutcomeUnion

The exit or timeout outcome associated with this shell call.

One of the following:

type ResponseFunctionShellCallOutputContentOutcomeTimeout struct{…}

Indicates that the shell call exceeded its configured time limit.

Type Timeout

The outcome type. Always `timeout`.

type ResponseFunctionShellCallOutputContentOutcomeExit struct{…}

Indicates that the shell commands finished and returned an exit code.

ExitCode int64

The exit code returned by the shell process.

Type Exit

The outcome type. Always `exit`.

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

MaxOutputLength int64Optional

The maximum number of UTF-8 characters captured for this shell call’s combined output.

Status stringOptional

The status of the shell call output.

One of the following:

const ResponseInputItemShellCallOutputStatusInProgress ResponseInputItemShellCallOutputStatus = "in\_progress"

const ResponseInputItemShellCallOutputStatusCompleted ResponseInputItemShellCallOutputStatus = "completed"

const ResponseInputItemShellCallOutputStatusIncomplete ResponseInputItemShellCallOutputStatus = "incomplete"

type ResponseInputItemApplyPatchCall struct{…}

A tool call representing a request to create, delete, or update files using diff patches.

CallID string

The unique ID of the apply patch tool call generated by the model.

maxLength64

minLength1

Operation ResponseInputItemApplyPatchCallOperationUnion

The specific create, delete, or update instruction for the apply\_patch tool call.

One of the following:

type ResponseInputItemApplyPatchCallOperationCreateFile struct{…}

Instruction for creating a new file via the apply\_patch tool.

Diff string

Unified diff content to apply when creating the file.

maxLength10485760

Path string

Path of the file to create relative to the workspace root.

minLength1

Type CreateFile

The operation type. Always `create_file`.

type ResponseInputItemApplyPatchCallOperationDeleteFile struct{…}

Instruction for deleting an existing file via the apply\_patch tool.

Path string

Path of the file to delete relative to the workspace root.

minLength1

Type DeleteFile

The operation type. Always `delete_file`.

type ResponseInputItemApplyPatchCallOperationUpdateFile struct{…}

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

The status of the apply patch tool call. One of `in_progress` or `completed`.

One of the following:

const ResponseInputItemApplyPatchCallStatusInProgress ResponseInputItemApplyPatchCallStatus = "in\_progress"

const ResponseInputItemApplyPatchCallStatusCompleted ResponseInputItemApplyPatchCallStatus = "completed"

Type ApplyPatchCall

The type of the item. Always `apply_patch_call`.

ID stringOptional

The unique ID of the apply patch tool call. Populated when this item is returned via API.

type ResponseInputItemApplyPatchCallOutput struct{…}

The streamed output emitted by an apply patch tool call.

CallID string

The unique ID of the apply patch tool call generated by the model.

maxLength64

minLength1

Status string

The status of the apply patch tool call output. One of `completed` or `failed`.

One of the following:

const ResponseInputItemApplyPatchCallOutputStatusCompleted ResponseInputItemApplyPatchCallOutputStatus = "completed"

const ResponseInputItemApplyPatchCallOutputStatusFailed ResponseInputItemApplyPatchCallOutputStatus = "failed"

Type ApplyPatchCallOutput

The type of the item. Always `apply_patch_call_output`.

ID stringOptional

The unique ID of the apply patch tool call output. Populated when this item is returned via API.

Output stringOptional

Optional human-readable log text from the apply patch tool (e.g., patch results or errors).

maxLength10485760

type ResponseInputItemMcpListTools struct{…}

A list of tools available on an MCP server.

ID string

The unique ID of the list.

ServerLabel string

The label of the MCP server.

Tools []ResponseInputItemMcpListToolsTool

The tools available on the server.

InputSchema any

The JSON schema describing the tool’s input.

Name string

The name of the tool.

Annotations anyOptional

Additional annotations about the tool.

Description stringOptional

The description of the tool.

Type McpListTools

The type of the item. Always `mcp_list_tools`.

Error stringOptional

Error message if the server could not list tools.

type ResponseInputItemMcpApprovalRequest struct{…}

A request for human approval of a tool invocation.

ID string

The unique ID of the approval request.

Arguments string

A JSON string of arguments for the tool.

Name string

The name of the tool to run.

ServerLabel string

The label of the MCP server making the request.

Type McpApprovalRequest

The type of the item. Always `mcp_approval_request`.

type ResponseInputItemMcpApprovalResponse struct{…}

A response to an MCP approval request.

ApprovalRequestID string

The ID of the approval request being answered.

Approve bool

Whether the request was approved.

Type McpApprovalResponse

The type of the item. Always `mcp_approval_response`.

ID stringOptional

The unique ID of the approval response

Reason stringOptional

Optional reason for the decision.

type ResponseInputItemMcpCall struct{…}

An invocation of a tool on an MCP server.

ID string

The unique ID of the tool call.

Arguments string

A JSON string of the arguments passed to the tool.

Name string

The name of the tool that was run.

ServerLabel string

The label of the MCP server running the tool.

Type McpCall

The type of the item. Always `mcp_call`.

ApprovalRequestID stringOptional

Unique identifier for the MCP tool call approval request.
Include this value in a subsequent `mcp_approval_response` input to approve or reject the corresponding tool call.

Error stringOptional

The error from the tool call, if any.

Output stringOptional

The output from the tool call.

Status stringOptional

The status of the tool call. One of `in_progress`, `completed`, `incomplete`, `calling`, or `failed`.

One of the following:

const ResponseInputItemMcpCallStatusInProgress ResponseInputItemMcpCallStatus = "in\_progress"

const ResponseInputItemMcpCallStatusCompleted ResponseInputItemMcpCallStatus = "completed"

const ResponseInputItemMcpCallStatusIncomplete ResponseInputItemMcpCallStatus = "incomplete"

const ResponseInputItemMcpCallStatusCalling ResponseInputItemMcpCallStatus = "calling"

const ResponseInputItemMcpCallStatusFailed ResponseInputItemMcpCallStatus = "failed"

type ResponseCustomToolCallOutput struct{…}

The output of a custom tool call from your code, being sent back to the model.

CallID string

The call ID, used to map this custom tool call output to a custom tool call.

Output ResponseCustomToolCallOutputOutputUnion

The output from the custom tool call generated by your code.
Can be a string or an list of output content.

One of the following:

string

type ResponseCustomToolCallOutputOutputOutputContentList []ResponseCustomToolCallOutputOutputOutputContentListItemUnion

Text, image, or file output of the custom tool call.

One of the following:

type ResponseInputText struct{…}

A text input to the model.

Text string

The text input to the model.

Type InputText

The type of the input item. Always `input_text`.

type ResponseInputImage struct{…}

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

Detail ResponseInputImageDetail

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

One of the following:

const ResponseInputImageDetailLow ResponseInputImageDetail = "low"

const ResponseInputImageDetailHigh ResponseInputImageDetail = "high"

const ResponseInputImageDetailAuto ResponseInputImageDetail = "auto"

const ResponseInputImageDetailOriginal ResponseInputImageDetail = "original"

Type InputImage

The type of the input item. Always `input_image`.

FileID stringOptional

The ID of the file to be sent to the model.

ImageURL stringOptional

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

type ResponseInputFile struct{…}

A file input to the model.

Type InputFile

The type of the input item. Always `input_file`.

Detail ResponseInputFileDetailOptional

The detail level of the file to be sent to the model. Use `low` for the default rendering behavior, or `high` to render the file at higher quality. Defaults to `low`.

One of the following:

const ResponseInputFileDetailLow ResponseInputFileDetail = "low"

const ResponseInputFileDetailHigh ResponseInputFileDetail = "high"

FileData stringOptional

The content of the file to be sent to the model.

FileID stringOptional

The ID of the file to be sent to the model.

FileURL stringOptional

The URL of the file to be sent to the model.

formaturi

Filename stringOptional

The name of the file to be sent to the model.

Type CustomToolCallOutput

The type of the custom tool call output. Always `custom_tool_call_output`.

ID stringOptional

The unique ID of the custom tool call output in the OpenAI platform.

type ResponseCustomToolCall struct{…}

A call to a custom tool created by the model.

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

Namespace stringOptional

The namespace of the custom tool being called.

type ResponseInputItemCompactionTrigger struct{…}

Compacts the current context. Must be the final input item.

Type CompactionTrigger

The type of the item. Always `compaction_trigger`.

type ResponseInputItemItemReference struct{…}

An internal identifier for an item to reference.

ID string

The ID of the item to reference.

Type stringOptional

The type of item to reference. Always `item_reference`.

Instructions param.Field[string]Optional

A system (or developer) message inserted into the model’s context.
When used along with `previous_response_id`, the instructions from a previous response will not be carried over to the next response. This makes it simple to swap out system (or developer) messages in new responses.

PreviousResponseID param.Field[string]Optional

The unique ID of the previous response to the model. Use this to create multi-turn conversations. Learn more about [conversation state](https://platform.openai.com/docs/guides/conversation-state). Cannot be used in conjunction with `conversation`.

PromptCacheKey param.Field[string]Optional

A key to use when reading from or writing to the prompt cache.

maxLength64

PromptCacheRetention param.Field[[ResponseCompactParamsPromptCacheRetention](/api/reference/go/resources/responses/methods/compact#(resource)%20responses%20%3E%20(method)%20compact%20%3E%20(params)%20default%20%3E%20(param)%20prompt_cache_retention%20%3E%20(schema))]Optional

How long to retain a prompt cache entry created by this request.

const ResponseCompactParamsPromptCacheRetentionInMemory [ResponseCompactParamsPromptCacheRetention](/api/reference/go/resources/responses/methods/compact#(resource)%20responses%20%3E%20(method)%20compact%20%3E%20(params)%20default%20%3E%20(param)%20prompt_cache_retention%20%3E%20(schema)) = "in\_memory"

const ResponseCompactParamsPromptCacheRetention24h [ResponseCompactParamsPromptCacheRetention](/api/reference/go/resources/responses/methods/compact#(resource)%20responses%20%3E%20(method)%20compact%20%3E%20(params)%20default%20%3E%20(param)%20prompt_cache_retention%20%3E%20(schema)) = "24h"

ServiceTier param.Field[[ResponseCompactParamsServiceTier](/api/reference/go/resources/responses/methods/compact#(resource)%20responses%20%3E%20(method)%20compact%20%3E%20(params)%20default%20%3E%20(param)%20service_tier%20%3E%20(schema))]Optional

The service tier to use for this request.

const ResponseCompactParamsServiceTierAuto [ResponseCompactParamsServiceTier](/api/reference/go/resources/responses/methods/compact#(resource)%20responses%20%3E%20(method)%20compact%20%3E%20(params)%20default%20%3E%20(param)%20service_tier%20%3E%20(schema)) = "auto"

const ResponseCompactParamsServiceTierDefault [ResponseCompactParamsServiceTier](/api/reference/go/resources/responses/methods/compact#(resource)%20responses%20%3E%20(method)%20compact%20%3E%20(params)%20default%20%3E%20(param)%20service_tier%20%3E%20(schema)) = "default"

const ResponseCompactParamsServiceTierFlex [ResponseCompactParamsServiceTier](/api/reference/go/resources/responses/methods/compact#(resource)%20responses%20%3E%20(method)%20compact%20%3E%20(params)%20default%20%3E%20(param)%20service_tier%20%3E%20(schema)) = "flex"

const ResponseCompactParamsServiceTierPriority [ResponseCompactParamsServiceTier](/api/reference/go/resources/responses/methods/compact#(resource)%20responses%20%3E%20(method)%20compact%20%3E%20(params)%20default%20%3E%20(param)%20service_tier%20%3E%20(schema)) = "priority"

##### ReturnsExpand Collapse

type CompactedResponse struct{…}

ID string

The unique identifier for the compacted response.

CreatedAt int64

Unix timestamp (in seconds) when the compacted conversation was created.

formatunixtime

Object ResponseCompaction

The object type. Always `response.compaction`.

Output [][ResponseOutputItemUnion](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20response_output_item%20%3E%20(schema))

The compacted list of output items. This is a list of all user messages, followed by a single compaction item.

One of the following:

type ResponseOutputMessage struct{…}

An output message from the model.

ID string

The unique ID of the output message.

Content []ResponseOutputMessageContentUnion

The content of the output message.

One of the following:

type ResponseOutputText struct{…}

A text output from the model.

Annotations []ResponseOutputTextAnnotationUnion

The annotations of the text output.

One of the following:

type ResponseOutputTextAnnotationFileCitation struct{…}

A citation to a file.

FileID string

The ID of the file.

Filename string

The filename of the file cited.

Index int64

The index of the file in the list of files.

Type FileCitation

The type of the file citation. Always `file_citation`.

type ResponseOutputTextAnnotationURLCitation struct{…}

A citation for a web resource used to generate a model response.

EndIndex int64

The index of the last character of the URL citation in the message.

StartIndex int64

The index of the first character of the URL citation in the message.

Title string

The title of the web resource.

Type URLCitation

The type of the URL citation. Always `url_citation`.

URL string

The URL of the web resource.

formaturi

type ResponseOutputTextAnnotationContainerFileCitation struct{…}

A citation for a container file used to generate a model response.

ContainerID string

The ID of the container file.

EndIndex int64

The index of the last character of the container file citation in the message.

FileID string

The ID of the file.

Filename string

The filename of the container file cited.

StartIndex int64

The index of the first character of the container file citation in the message.

Type ContainerFileCitation

The type of the container file citation. Always `container_file_citation`.

type ResponseOutputTextAnnotationFilePath struct{…}

A path to a file.

FileID string

The ID of the file.

Index int64

The index of the file in the list of files.

Type FilePath

The type of the file path. Always `file_path`.

Text string

The text output from the model.

Type OutputText

The type of the output text. Always `output_text`.

Logprobs []ResponseOutputTextLogprobOptional

Token string

Bytes []int64

Logprob float64

TopLogprobs []ResponseOutputTextLogprobTopLogprob

Token string

Bytes []int64

Logprob float64

type ResponseOutputRefusal struct{…}

A refusal from the model.

Refusal string

The refusal explanation from the model.

Type Refusal

The type of the refusal. Always `refusal`.

Role Assistant

The role of the output message. Always `assistant`.

Status ResponseOutputMessageStatus

The status of the message input. One of `in_progress`, `completed`, or
`incomplete`. Populated when input items are returned via API.

One of the following:

const ResponseOutputMessageStatusInProgress ResponseOutputMessageStatus = "in\_progress"

const ResponseOutputMessageStatusCompleted ResponseOutputMessageStatus = "completed"

const ResponseOutputMessageStatusIncomplete ResponseOutputMessageStatus = "incomplete"

Type Message

The type of the output message. Always `message`.

Phase ResponseOutputMessagePhaseOptional

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

One of the following:

const ResponseOutputMessagePhaseCommentary ResponseOutputMessagePhase = "commentary"

const ResponseOutputMessagePhaseFinalAnswer ResponseOutputMessagePhase = "final\_answer"

type ResponseFileSearchToolCall struct{…}

The results of a file search tool call. See the
[file search guide](https://platform.openai.com/docs/guides/tools-file-search) for more information.

ID string

The unique ID of the file search tool call.

Queries []string

The queries used to search for files.

Status ResponseFileSearchToolCallStatus

The status of the file search tool call. One of `in_progress`,
`searching`, `incomplete` or `failed`,

One of the following:

const ResponseFileSearchToolCallStatusInProgress ResponseFileSearchToolCallStatus = "in\_progress"

const ResponseFileSearchToolCallStatusSearching ResponseFileSearchToolCallStatus = "searching"

const ResponseFileSearchToolCallStatusCompleted ResponseFileSearchToolCallStatus = "completed"

const ResponseFileSearchToolCallStatusIncomplete ResponseFileSearchToolCallStatus = "incomplete"

const ResponseFileSearchToolCallStatusFailed ResponseFileSearchToolCallStatus = "failed"

Type FileSearchCall

The type of the file search tool call. Always `file_search_call`.

Results []ResponseFileSearchToolCallResultOptional

The results of the file search tool call.

Attributes map[string, ResponseFileSearchToolCallResultAttributeUnion]Optional

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.

One of the following:

string

float64

bool

FileID stringOptional

The unique ID of the file.

Filename stringOptional

The name of the file.

Score float64Optional

The relevance score of the file - a value between 0 and 1.

formatfloat

Text stringOptional

The text that was retrieved from the file.

type ResponseFunctionToolCall struct{…}

A tool call to run a function. See the
[function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.

Arguments string

A JSON string of the arguments to pass to the function.

CallID string

The unique ID of the function tool call generated by the model.

Name string

The name of the function to run.

Type FunctionCall

The type of the function tool call. Always `function_call`.

ID stringOptional

The unique ID of the function tool call.

Namespace stringOptional

The namespace of the function to run.

Status ResponseFunctionToolCallStatusOptional

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

One of the following:

const ResponseFunctionToolCallStatusInProgress ResponseFunctionToolCallStatus = "in\_progress"

const ResponseFunctionToolCallStatusCompleted ResponseFunctionToolCallStatus = "completed"

const ResponseFunctionToolCallStatusIncomplete ResponseFunctionToolCallStatus = "incomplete"

type ResponseFunctionToolCallOutputItem struct{…}

ID string

The unique ID of the function call tool output.

CallID string

The unique ID of the function tool call generated by the model.

Output ResponseFunctionToolCallOutputItemOutputUnion

The output from the function call generated by your code.
Can be a string or an list of output content.

One of the following:

string

type ResponseFunctionToolCallOutputItemOutputOutputContentList []ResponseFunctionToolCallOutputItemOutputOutputContentListItemUnion

Text, image, or file output of the function call.

One of the following:

type ResponseInputText struct{…}

A text input to the model.

Text string

The text input to the model.

Type InputText

The type of the input item. Always `input_text`.

type ResponseInputImage struct{…}

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

Detail ResponseInputImageDetail

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

One of the following:

const ResponseInputImageDetailLow ResponseInputImageDetail = "low"

const ResponseInputImageDetailHigh ResponseInputImageDetail = "high"

const ResponseInputImageDetailAuto ResponseInputImageDetail = "auto"

const ResponseInputImageDetailOriginal ResponseInputImageDetail = "original"

Type InputImage

The type of the input item. Always `input_image`.

FileID stringOptional

The ID of the file to be sent to the model.

ImageURL stringOptional

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

type ResponseInputFile struct{…}

A file input to the model.

Type InputFile

The type of the input item. Always `input_file`.

Detail ResponseInputFileDetailOptional

The detail level of the file to be sent to the model. Use `low` for the default rendering behavior, or `high` to render the file at higher quality. Defaults to `low`.

One of the following:

const ResponseInputFileDetailLow ResponseInputFileDetail = "low"

const ResponseInputFileDetailHigh ResponseInputFileDetail = "high"

FileData stringOptional

The content of the file to be sent to the model.

FileID stringOptional

The ID of the file to be sent to the model.

FileURL stringOptional

The URL of the file to be sent to the model.

formaturi

Filename stringOptional

The name of the file to be sent to the model.

Status ResponseFunctionToolCallOutputItemStatus

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

One of the following:

const ResponseFunctionToolCallOutputItemStatusInProgress ResponseFunctionToolCallOutputItemStatus = "in\_progress"

const ResponseFunctionToolCallOutputItemStatusCompleted ResponseFunctionToolCallOutputItemStatus = "completed"

const ResponseFunctionToolCallOutputItemStatusIncomplete ResponseFunctionToolCallOutputItemStatus = "incomplete"

Type FunctionCallOutput

The type of the function tool call output. Always `function_call_output`.

CreatedBy stringOptional

The identifier of the actor that created the item.

type ResponseFunctionWebSearch struct{…}

The results of a web search tool call. See the
[web search guide](https://platform.openai.com/docs/guides/tools-web-search) for more information.

ID string

The unique ID of the web search tool call.

Action ResponseFunctionWebSearchActionUnion

An object describing the specific action taken in this web search call.
Includes details on how the model used the web (search, open\_page, find\_in\_page).

One of the following:

type ResponseFunctionWebSearchActionSearch struct{…}

Action type “search” - Performs a web search query.

Type Search

The action type.

Queries []stringOptional

The search queries.

DeprecatedQuery stringOptional

The search query.

Sources []ResponseFunctionWebSearchActionSearchSourceOptional

The sources used in the search.

Type URL

The type of source. Always `url`.

URL string

The URL of the source.

formaturi

type ResponseFunctionWebSearchActionOpenPage struct{…}

Action type “open\_page” - Opens a specific URL from search results.

Type OpenPage

The action type.

URL stringOptional

The URL opened by the model.

formaturi

type ResponseFunctionWebSearchActionFindInPage struct{…}

Action type “find\_in\_page”: Searches for a pattern within a loaded page.

Pattern string

The pattern or text to search for within the page.

Type FindInPage

The action type.

URL string

The URL of the page searched for the pattern.

formaturi

Status ResponseFunctionWebSearchStatus

The status of the web search tool call.

One of the following:

const ResponseFunctionWebSearchStatusInProgress ResponseFunctionWebSearchStatus = "in\_progress"

const ResponseFunctionWebSearchStatusSearching ResponseFunctionWebSearchStatus = "searching"

const ResponseFunctionWebSearchStatusCompleted ResponseFunctionWebSearchStatus = "completed"

const ResponseFunctionWebSearchStatusFailed ResponseFunctionWebSearchStatus = "failed"

Type WebSearchCall

The type of the web search tool call. Always `web_search_call`.

type ResponseComputerToolCall struct{…}

A tool call to a computer use tool. See the
[computer use guide](https://platform.openai.com/docs/guides/tools-computer-use) for more information.

ID string

The unique ID of the computer call.

CallID string

An identifier used when responding to the tool call with output.

PendingSafetyChecks []ResponseComputerToolCallPendingSafetyCheck

The pending safety checks for the computer call.

ID string

The ID of the pending safety check.

Code stringOptional

The type of the pending safety check.

Message stringOptional

Details about the pending safety check.

Status ResponseComputerToolCallStatus

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

One of the following:

const ResponseComputerToolCallStatusInProgress ResponseComputerToolCallStatus = "in\_progress"

const ResponseComputerToolCallStatusCompleted ResponseComputerToolCallStatus = "completed"

const ResponseComputerToolCallStatusIncomplete ResponseComputerToolCallStatus = "incomplete"

Type ResponseComputerToolCallType

The type of the computer call. Always `computer_call`.

Action ResponseComputerToolCallActionUnionOptional

A click action.

One of the following:

type ResponseComputerToolCallActionClick struct{…}

A click action.

Button string

Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

One of the following:

const ResponseComputerToolCallActionClickButtonLeft ResponseComputerToolCallActionClickButton = "left"

const ResponseComputerToolCallActionClickButtonRight ResponseComputerToolCallActionClickButton = "right"

const ResponseComputerToolCallActionClickButtonWheel ResponseComputerToolCallActionClickButton = "wheel"

const ResponseComputerToolCallActionClickButtonBack ResponseComputerToolCallActionClickButton = "back"

const ResponseComputerToolCallActionClickButtonForward ResponseComputerToolCallActionClickButton = "forward"

Type Click

Specifies the event type. For a click action, this property is always `click`.

X int64

The x-coordinate where the click occurred.

Y int64

The y-coordinate where the click occurred.

Keys []stringOptional

The keys being held while clicking.

type ResponseComputerToolCallActionDoubleClick struct{…}

A double click action.

Keys []string

The keys being held while double-clicking.

Type DoubleClick

Specifies the event type. For a double click action, this property is always set to `double_click`.

X int64

The x-coordinate where the double click occurred.

Y int64

The y-coordinate where the double click occurred.

type ResponseComputerToolCallActionDrag struct{…}

A drag action.

Path []ResponseComputerToolCallActionDragPath

An array of coordinates representing the path of the drag action. Coordinates will appear as an array of objects, eg

[
  { x: 100, y: 200 },
  { x: 200, y: 300 }
]

X int64

The x-coordinate.

Y int64

The y-coordinate.

Type Drag

Specifies the event type. For a drag action, this property is always set to `drag`.

Keys []stringOptional

The keys being held while dragging the mouse.

type ResponseComputerToolCallActionKeypress struct{…}

A collection of keypresses the model would like to perform.

Keys []string

The combination of keys the model is requesting to be pressed. This is an array of strings, each representing a key.

Type Keypress

Specifies the event type. For a keypress action, this property is always set to `keypress`.

type ResponseComputerToolCallActionMove struct{…}

A mouse move action.

Type Move

Specifies the event type. For a move action, this property is always set to `move`.

X int64

The x-coordinate to move to.

Y int64

The y-coordinate to move to.

Keys []stringOptional

The keys being held while moving the mouse.

type ResponseComputerToolCallActionScreenshot struct{…}

A screenshot action.

Type Screenshot

Specifies the event type. For a screenshot action, this property is always set to `screenshot`.

type ResponseComputerToolCallActionScroll struct{…}

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

type ResponseComputerToolCallActionType struct{…}

An action to type in text.

Text string

The text to type.

Type Type

Specifies the event type. For a type action, this property is always set to `type`.

type ResponseComputerToolCallActionWait struct{…}

A wait action.

Type Wait

Specifies the event type. For a wait action, this property is always set to `wait`.

Actions [ComputerActionList](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20computer_action_list%20%3E%20(schema))Optional

Flattened batched actions for `computer_use`. Each action includes an
`type` discriminator and action-specific fields.

One of the following:

type ComputerActionClick struct{…}

A click action.

Button string

Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

One of the following:

const ComputerActionClickButtonLeft ComputerActionClickButton = "left"

const ComputerActionClickButtonRight ComputerActionClickButton = "right"

const ComputerActionClickButtonWheel ComputerActionClickButton = "wheel"

const ComputerActionClickButtonBack ComputerActionClickButton = "back"

const ComputerActionClickButtonForward ComputerActionClickButton = "forward"

Type Click

Specifies the event type. For a click action, this property is always `click`.

X int64

The x-coordinate where the click occurred.

Y int64

The y-coordinate where the click occurred.

Keys []stringOptional

The keys being held while clicking.

type ComputerActionDoubleClick struct{…}

A double click action.

Keys []string

The keys being held while double-clicking.

Type DoubleClick

Specifies the event type. For a double click action, this property is always set to `double_click`.

X int64

The x-coordinate where the double click occurred.

Y int64

The y-coordinate where the double click occurred.

type ComputerActionDrag struct{…}

A drag action.

Path []ComputerActionDragPath

An array of coordinates representing the path of the drag action. Coordinates will appear as an array of objects, eg

[
  { x: 100, y: 200 },
  { x: 200, y: 300 }
]

X int64

The x-coordinate.

Y int64

The y-coordinate.

Type Drag

Specifies the event type. For a drag action, this property is always set to `drag`.

Keys []stringOptional

The keys being held while dragging the mouse.

type ComputerActionKeypress struct{…}

A collection of keypresses the model would like to perform.

Keys []string

The combination of keys the model is requesting to be pressed. This is an array of strings, each representing a key.

Type Keypress

Specifies the event type. For a keypress action, this property is always set to `keypress`.

type ComputerActionMove struct{…}

A mouse move action.

Type Move

Specifies the event type. For a move action, this property is always set to `move`.

X int64

The x-coordinate to move to.

Y int64

The y-coordinate to move to.

Keys []stringOptional

The keys being held while moving the mouse.

type ComputerActionScreenshot struct{…}

A screenshot action.

Type Screenshot

Specifies the event type. For a screenshot action, this property is always set to `screenshot`.

type ComputerActionScroll struct{…}

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

type ComputerActionType struct{…}

An action to type in text.

Text string

The text to type.

Type Type

Specifies the event type. For a type action, this property is always set to `type`.

type ComputerActionWait struct{…}

A wait action.

Type Wait

Specifies the event type. For a wait action, this property is always set to `wait`.

type ResponseComputerToolCallOutputItem struct{…}

ID string

The unique ID of the computer call tool output.

CallID string

The ID of the computer tool call that produced the output.

Output [ResponseComputerToolCallOutputScreenshot](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20response_computer_tool_call_output_screenshot%20%3E%20(schema))

A computer screenshot image used with the computer use tool.

Type ComputerScreenshot

Specifies the event type. For a computer screenshot, this property is
always set to `computer_screenshot`.

FileID stringOptional

The identifier of an uploaded file that contains the screenshot.

ImageURL stringOptional

The URL of the screenshot image.

formaturi

Status ResponseComputerToolCallOutputItemStatus

The status of the message input. One of `in_progress`, `completed`, or
`incomplete`. Populated when input items are returned via API.

One of the following:

const ResponseComputerToolCallOutputItemStatusCompleted ResponseComputerToolCallOutputItemStatus = "completed"

const ResponseComputerToolCallOutputItemStatusIncomplete ResponseComputerToolCallOutputItemStatus = "incomplete"

const ResponseComputerToolCallOutputItemStatusFailed ResponseComputerToolCallOutputItemStatus = "failed"

const ResponseComputerToolCallOutputItemStatusInProgress ResponseComputerToolCallOutputItemStatus = "in\_progress"

Type ComputerCallOutput

The type of the computer tool call output. Always `computer_call_output`.

AcknowledgedSafetyChecks []ResponseComputerToolCallOutputItemAcknowledgedSafetyCheckOptional

The safety checks reported by the API that have been acknowledged by the
developer.

ID string

The ID of the pending safety check.

Code stringOptional

The type of the pending safety check.

Message stringOptional

Details about the pending safety check.

CreatedBy stringOptional

The identifier of the actor that created the item.

type ResponseReasoningItem struct{…}

A description of the chain of thought used by a reasoning model while generating
a response. Be sure to include these items in your `input` to the Responses API
for subsequent turns of a conversation if you are manually
[managing context](https://platform.openai.com/docs/guides/conversation-state).

ID string

The unique identifier of the reasoning content.

Summary []ResponseReasoningItemSummary

Reasoning summary content.

Text string

A summary of the reasoning output from the model so far.

Type SummaryText

The type of the object. Always `summary_text`.

Type Reasoning

The type of the object. Always `reasoning`.

Content []ResponseReasoningItemContentOptional

Reasoning text content.

Text string

The reasoning text from the model.

Type ReasoningText

The type of the reasoning text. Always `reasoning_text`.

EncryptedContent stringOptional

The encrypted content of the reasoning item - populated when a response is
generated with `reasoning.encrypted_content` in the `include` parameter.

Status ResponseReasoningItemStatusOptional

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

One of the following:

const ResponseReasoningItemStatusInProgress ResponseReasoningItemStatus = "in\_progress"

const ResponseReasoningItemStatusCompleted ResponseReasoningItemStatus = "completed"

const ResponseReasoningItemStatusIncomplete ResponseReasoningItemStatus = "incomplete"

type ResponseToolSearchCall struct{…}

ID string

The unique ID of the tool search call item.

Arguments any

Arguments used for the tool search call.

CallID string

The unique ID of the tool search call generated by the model.

Execution ResponseToolSearchCallExecution

Whether tool search was executed by the server or by the client.

One of the following:

const ResponseToolSearchCallExecutionServer ResponseToolSearchCallExecution = "server"

const ResponseToolSearchCallExecutionClient ResponseToolSearchCallExecution = "client"

Status ResponseToolSearchCallStatus

The status of the tool search call item that was recorded.

One of the following:

const ResponseToolSearchCallStatusInProgress ResponseToolSearchCallStatus = "in\_progress"

const ResponseToolSearchCallStatusCompleted ResponseToolSearchCallStatus = "completed"

const ResponseToolSearchCallStatusIncomplete ResponseToolSearchCallStatus = "incomplete"

Type ToolSearchCall

The type of the item. Always `tool_search_call`.

CreatedBy stringOptional

The identifier of the actor that created the item.

type ResponseToolSearchOutputItem struct{…}

ID string

The unique ID of the tool search output item.

CallID string

The unique ID of the tool search call generated by the model.

Execution ResponseToolSearchOutputItemExecution

Whether tool search was executed by the server or by the client.

One of the following:

const ResponseToolSearchOutputItemExecutionServer ResponseToolSearchOutputItemExecution = "server"

const ResponseToolSearchOutputItemExecutionClient ResponseToolSearchOutputItemExecution = "client"

Status ResponseToolSearchOutputItemStatus

The status of the tool search output item that was recorded.

One of the following:

const ResponseToolSearchOutputItemStatusInProgress ResponseToolSearchOutputItemStatus = "in\_progress"

const ResponseToolSearchOutputItemStatusCompleted ResponseToolSearchOutputItemStatus = "completed"

const ResponseToolSearchOutputItemStatusIncomplete ResponseToolSearchOutputItemStatus = "incomplete"

Tools [][ToolUnion](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20tool%20%3E%20(schema))

The loaded tool definitions returned by tool search.

One of the following:

type FunctionTool struct{…}

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

Name string

The name of the function to call.

Parameters map[string, any]

A JSON schema object describing the parameters of the function.

Strict bool

Whether to enforce strict parameter validation. Default `true`.

Type Function

The type of the function tool. Always `function`.

DeferLoading boolOptional

Whether this function is deferred and loaded via tool search.

Description stringOptional

A description of the function. Used by the model to determine whether or not to call the function.

type FileSearchTool struct{…}

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

Type FileSearch

The type of the file search tool. Always `file_search`.

VectorStoreIDs []string

The IDs of the vector stores to search.

Filters FileSearchToolFiltersUnionOptional

A filter to apply.

One of the following:

type ComparisonFilter struct{…}

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

Key string

The key to compare against the value.

Type ComparisonFilterType

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

const ComparisonFilterTypeEq ComparisonFilterType = "eq"

const ComparisonFilterTypeNe ComparisonFilterType = "ne"

const ComparisonFilterTypeGt ComparisonFilterType = "gt"

const ComparisonFilterTypeGte ComparisonFilterType = "gte"

const ComparisonFilterTypeLt ComparisonFilterType = "lt"

const ComparisonFilterTypeLte ComparisonFilterType = "lte"

const ComparisonFilterTypeIn ComparisonFilterType = "in"

const ComparisonFilterTypeNin ComparisonFilterType = "nin"

Value ComparisonFilterValueUnion

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

string

float64

bool

type ComparisonFilterValueArray []ComparisonFilterValueArrayItemUnion

One of the following:

string

float64

type CompoundFilter struct{…}

Combine multiple filters using `and` or `or`.

Filters [][ComparisonFilter](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema))

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

One of the following:

type ComparisonFilter struct{…}

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

Key string

The key to compare against the value.

Type ComparisonFilterType

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

const ComparisonFilterTypeEq ComparisonFilterType = "eq"

const ComparisonFilterTypeNe ComparisonFilterType = "ne"

const ComparisonFilterTypeGt ComparisonFilterType = "gt"

const ComparisonFilterTypeGte ComparisonFilterType = "gte"

const ComparisonFilterTypeLt ComparisonFilterType = "lt"

const ComparisonFilterTypeLte ComparisonFilterType = "lte"

const ComparisonFilterTypeIn ComparisonFilterType = "in"

const ComparisonFilterTypeNin ComparisonFilterType = "nin"

Value ComparisonFilterValueUnion

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

string

float64

bool

type ComparisonFilterValueArray []ComparisonFilterValueArrayItemUnion

One of the following:

string

float64

Type CompoundFilterType

Type of operation: `and` or `or`.

One of the following:

const CompoundFilterTypeAnd CompoundFilterType = "and"

const CompoundFilterTypeOr CompoundFilterType = "or"

MaxNumResults int64Optional

The maximum number of results to return. This number should be between 1 and 50 inclusive.

RankingOptions FileSearchToolRankingOptionsOptional

Ranking options for search.

HybridSearch FileSearchToolRankingOptionsHybridSearchOptional

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

EmbeddingWeight float64

The weight of the embedding in the reciprocal ranking fusion.

TextWeight float64

The weight of the text in the reciprocal ranking fusion.

Ranker stringOptional

The ranker to use for the file search.

One of the following:

const FileSearchToolRankingOptionsRankerAuto FileSearchToolRankingOptionsRanker = "auto"

const FileSearchToolRankingOptionsRankerDefault2024\_11\_15 FileSearchToolRankingOptionsRanker = "default-2024-11-15"

ScoreThreshold float64Optional

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

type ComputerTool struct{…}

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

Type Computer

The type of the computer tool. Always `computer`.

type ComputerUsePreviewTool struct{…}

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

DisplayHeight int64

The height of the computer display.

DisplayWidth int64

The width of the computer display.

Environment ComputerUsePreviewToolEnvironment

The type of computer environment to control.

One of the following:

const ComputerUsePreviewToolEnvironmentWindows ComputerUsePreviewToolEnvironment = "windows"

const ComputerUsePreviewToolEnvironmentMac ComputerUsePreviewToolEnvironment = "mac"

const ComputerUsePreviewToolEnvironmentLinux ComputerUsePreviewToolEnvironment = "linux"

const ComputerUsePreviewToolEnvironmentUbuntu ComputerUsePreviewToolEnvironment = "ubuntu"

const ComputerUsePreviewToolEnvironmentBrowser ComputerUsePreviewToolEnvironment = "browser"

Type ComputerUsePreview

The type of the computer use tool. Always `computer_use_preview`.

type WebSearchTool struct{…}

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type WebSearchToolType

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

One of the following:

const WebSearchToolTypeWebSearch WebSearchToolType = "web\_search"

const WebSearchToolTypeWebSearch2025\_08\_26 WebSearchToolType = "web\_search\_2025\_08\_26"

Filters WebSearchToolFiltersOptional

Filters for the search.

AllowedDomains []stringOptional

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

SearchContextSize WebSearchToolSearchContextSizeOptional

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

const WebSearchToolSearchContextSizeLow WebSearchToolSearchContextSize = "low"

const WebSearchToolSearchContextSizeMedium WebSearchToolSearchContextSize = "medium"

const WebSearchToolSearchContextSizeHigh WebSearchToolSearchContextSize = "high"

UserLocation WebSearchToolUserLocationOptional

The approximate location of the user.

City stringOptional

Free text input for the city of the user, e.g. `San Francisco`.

Country stringOptional

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

Region stringOptional

Free text input for the region of the user, e.g. `California`.

Timezone stringOptional

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

Type stringOptional

The type of location approximation. Always `approximate`.

type ToolMcp struct{…}

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

ServerLabel string

A label for this MCP server, used to identify it in tool calls.

Type Mcp

The type of the MCP tool. Always `mcp`.

AllowedTools ToolMcpAllowedToolsUnionOptional

List of allowed tool names or a filter object.

One of the following:

type ToolMcpAllowedToolsMcpAllowedTools []string

A string array of allowed tool names

type ToolMcpAllowedToolsMcpToolFilter struct{…}

A filter object to specify which tools are allowed.

ReadOnly boolOptional

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

ToolNames []stringOptional

List of allowed tool names.

Authorization stringOptional

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

ConnectorID stringOptional

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

const ToolMcpConnectorIDConnectorDropbox ToolMcpConnectorID = "connector\_dropbox"

const ToolMcpConnectorIDConnectorGmail ToolMcpConnectorID = "connector\_gmail"

const ToolMcpConnectorIDConnectorGooglecalendar ToolMcpConnectorID = "connector\_googlecalendar"

const ToolMcpConnectorIDConnectorGoogledrive ToolMcpConnectorID = "connector\_googledrive"

const ToolMcpConnectorIDConnectorMicrosoftteams ToolMcpConnectorID = "connector\_microsoftteams"

const ToolMcpConnectorIDConnectorOutlookcalendar ToolMcpConnectorID = "connector\_outlookcalendar"

const ToolMcpConnectorIDConnectorOutlookemail ToolMcpConnectorID = "connector\_outlookemail"

const ToolMcpConnectorIDConnectorSharepoint ToolMcpConnectorID = "connector\_sharepoint"

DeferLoading boolOptional

Whether this MCP tool is deferred and discovered via tool search.

Headers map[string, string]Optional

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

RequireApproval ToolMcpRequireApprovalUnionOptional

Specify which of the MCP server’s tools require approval.

One of the following:

type ToolMcpRequireApprovalMcpToolApprovalFilter struct{…}

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

Always ToolMcpRequireApprovalMcpToolApprovalFilterAlwaysOptional

A filter object to specify which tools are allowed.

ReadOnly boolOptional

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

ToolNames []stringOptional

List of allowed tool names.

Never ToolMcpRequireApprovalMcpToolApprovalFilterNeverOptional

A filter object to specify which tools are allowed.

ReadOnly boolOptional

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

ToolNames []stringOptional

List of allowed tool names.

type ToolMcpRequireApprovalMcpToolApprovalSetting string

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

One of the following:

const ToolMcpRequireApprovalMcpToolApprovalSettingAlways ToolMcpRequireApprovalMcpToolApprovalSetting = "always"

const ToolMcpRequireApprovalMcpToolApprovalSettingNever ToolMcpRequireApprovalMcpToolApprovalSetting = "never"

ServerDescription stringOptional

Optional description of the MCP server, used to provide more context.

ServerURL stringOptional

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

TunnelID stringOptional

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

type ToolCodeInterpreter struct{…}

A tool that runs Python code to help generate a response to a prompt.

Container ToolCodeInterpreterContainerUnion

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

One of the following:

string

type ToolCodeInterpreterContainerCodeInterpreterContainerAuto struct{…}

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

Type Auto

Always `auto`.

FileIDs []stringOptional

An optional list of uploaded files to make available to your code.

MemoryLimit stringOptional

The memory limit for the code interpreter container.

One of the following:

const ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit1g ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit = "1g"

const ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit4g ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit = "4g"

const ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit16g ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit = "16g"

const ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit64g ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit = "64g"

NetworkPolicy ToolCodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicyUnionOptional

Network access policy for the container.

One of the following:

type ContainerNetworkPolicyDisabled struct{…}

Type Disabled

Disable outbound network access. Always `disabled`.

type ContainerNetworkPolicyAllowlist struct{…}

AllowedDomains []string

A list of allowed domains when type is `allowlist`.

Type Allowlist

Allow outbound network access only to specified domains. Always `allowlist`.

DomainSecrets [][ContainerNetworkPolicyDomainSecret](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema))Optional

Optional domain-scoped secrets for allowlisted domains.

Domain string

The domain associated with the secret.

minLength1

Name string

The name of the secret to inject for the domain.

minLength1

Value string

The secret value to inject for the domain.

maxLength10485760

minLength1

Type CodeInterpreter

The type of the code interpreter tool. Always `code_interpreter`.

type ToolImageGeneration struct{…}

A tool that generates images using the GPT image models.

Type ImageGeneration

The type of the image generation tool. Always `image_generation`.

Action stringOptional

Whether to generate a new image or edit an existing image. Default: `auto`.

One of the following:

const ToolImageGenerationActionGenerate ToolImageGenerationAction = "generate"

const ToolImageGenerationActionEdit ToolImageGenerationAction = "edit"

const ToolImageGenerationActionAuto ToolImageGenerationAction = "auto"

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

One of the following:

const ToolImageGenerationBackgroundTransparent ToolImageGenerationBackground = "transparent"

const ToolImageGenerationBackgroundOpaque ToolImageGenerationBackground = "opaque"

const ToolImageGenerationBackgroundAuto ToolImageGenerationBackground = "auto"

InputFidelity stringOptional

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

One of the following:

const ToolImageGenerationInputFidelityHigh ToolImageGenerationInputFidelity = "high"

const ToolImageGenerationInputFidelityLow ToolImageGenerationInputFidelity = "low"

InputImageMask ToolImageGenerationInputImageMaskOptional

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

FileID stringOptional

File ID for the mask image.

ImageURL stringOptional

Base64-encoded mask image.

Model stringOptional

The image generation model to use. Default: `gpt-image-1`.

One of the following:

string

string

One of the following:

const ToolImageGenerationModelGPTImage1 ToolImageGenerationModel = "gpt-image-1"

const ToolImageGenerationModelGPTImage1Mini ToolImageGenerationModel = "gpt-image-1-mini"

const ToolImageGenerationModelGPTImage2 ToolImageGenerationModel = "gpt-image-2"

const ToolImageGenerationModelGPTImage2\_2026\_04\_21 ToolImageGenerationModel = "gpt-image-2-2026-04-21"

const ToolImageGenerationModelGPTImage1\_5 ToolImageGenerationModel = "gpt-image-1.5"

const ToolImageGenerationModelChatgptImageLatest ToolImageGenerationModel = "chatgpt-image-latest"

Moderation stringOptional

Moderation level for the generated image. Default: `auto`.

One of the following:

const ToolImageGenerationModerationAuto ToolImageGenerationModeration = "auto"

const ToolImageGenerationModerationLow ToolImageGenerationModeration = "low"

OutputCompression int64Optional

Compression level for the output image. Default: 100.

minimum0

maximum100

OutputFormat stringOptional

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

One of the following:

const ToolImageGenerationOutputFormatPNG ToolImageGenerationOutputFormat = "png"

const ToolImageGenerationOutputFormatWebP ToolImageGenerationOutputFormat = "webp"

const ToolImageGenerationOutputFormatJPEG ToolImageGenerationOutputFormat = "jpeg"

PartialImages int64Optional

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

Quality stringOptional

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

One of the following:

const ToolImageGenerationQualityLow ToolImageGenerationQuality = "low"

const ToolImageGenerationQualityMedium ToolImageGenerationQuality = "medium"

const ToolImageGenerationQualityHigh ToolImageGenerationQuality = "high"

const ToolImageGenerationQualityAuto ToolImageGenerationQuality = "auto"

Size stringOptional

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

One of the following:

string

string

One of the following:

const ToolImageGenerationSize1024x1024 ToolImageGenerationSize = "1024x1024"

const ToolImageGenerationSize1024x1536 ToolImageGenerationSize = "1024x1536"

const ToolImageGenerationSize1536x1024 ToolImageGenerationSize = "1536x1024"

const ToolImageGenerationSizeAuto ToolImageGenerationSize = "auto"

type ToolLocalShell struct{…}

A tool that allows the model to execute shell commands in a local environment.

Type LocalShell

The type of the local shell tool. Always `local_shell`.

type FunctionShellTool struct{…}

A tool that allows the model to execute shell commands.

Type Shell

The type of the shell tool. Always `shell`.

Environment FunctionShellToolEnvironmentUnionOptional

One of the following:

type ContainerAuto struct{…}

Type ContainerAuto

Automatically creates a container for this request

FileIDs []stringOptional

An optional list of uploaded files to make available to your code.

MemoryLimit ContainerAutoMemoryLimitOptional

The memory limit for the container.

One of the following:

const ContainerAutoMemoryLimit1g ContainerAutoMemoryLimit = "1g"

const ContainerAutoMemoryLimit4g ContainerAutoMemoryLimit = "4g"

const ContainerAutoMemoryLimit16g ContainerAutoMemoryLimit = "16g"

const ContainerAutoMemoryLimit64g ContainerAutoMemoryLimit = "64g"

NetworkPolicy ContainerAutoNetworkPolicyUnionOptional

Network access policy for the container.

One of the following:

type ContainerNetworkPolicyDisabled struct{…}

Type Disabled

Disable outbound network access. Always `disabled`.

type ContainerNetworkPolicyAllowlist struct{…}

AllowedDomains []string

A list of allowed domains when type is `allowlist`.

Type Allowlist

Allow outbound network access only to specified domains. Always `allowlist`.

DomainSecrets [][ContainerNetworkPolicyDomainSecret](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema))Optional

Optional domain-scoped secrets for allowlisted domains.

Domain string

The domain associated with the secret.

minLength1

Name string

The name of the secret to inject for the domain.

minLength1

Value string

The secret value to inject for the domain.

maxLength10485760

minLength1

Skills []ContainerAutoSkillUnionOptional

An optional list of skills referenced by id or inline data.

One of the following:

type SkillReference struct{…}

SkillID string

The ID of the referenced skill.

maxLength64

minLength1

Type SkillReference

References a skill created with the /v1/skills endpoint.

Version stringOptional

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

type InlineSkill struct{…}

Description string

The description of the skill.

Name string

The name of the skill.

Source [InlineSkillSource](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill_source%20%3E%20(schema))

Inline skill payload

Data string

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

MediaType ApplicationZip

The media type of the inline skill payload. Must be `application/zip`.

Type Base64

The type of the inline skill source. Must be `base64`.

Type Inline

Defines an inline skill for this request.

type LocalEnvironment struct{…}

Type Local

Use a local computer environment.

Skills [][LocalSkill](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20local_skill%20%3E%20(schema))Optional

An optional list of skills.

Description string

The description of the skill.

Name string

The name of the skill.

Path string

The path to the directory containing the skill.

type ContainerReference struct{…}

ContainerID string

The ID of the referenced container.

Type ContainerReference

References a container created with the /v1/containers endpoint

type CustomTool struct{…}

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

Name string

The name of the custom tool, used to identify it in tool calls.

Type Custom

The type of the custom tool. Always `custom`.

DeferLoading boolOptional

Whether this tool should be deferred and discovered via tool search.

Description stringOptional

Optional description of the custom tool, used to provide more context.

Format [CustomToolInputFormatUnion](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))Optional

The input format for the custom tool. Default is unconstrained text.

One of the following:

type CustomToolInputFormatText struct{…}

Unconstrained free-form text.

Type Text

Unconstrained text format. Always `text`.

type CustomToolInputFormatGrammar struct{…}

A grammar defined by the user.

Definition string

The grammar definition.

Syntax string

The syntax of the grammar definition. One of `lark` or `regex`.

One of the following:

const CustomToolInputFormatGrammarSyntaxLark CustomToolInputFormatGrammarSyntax = "lark"

const CustomToolInputFormatGrammarSyntaxRegex CustomToolInputFormatGrammarSyntax = "regex"

Type Grammar

Grammar format. Always `grammar`.

type NamespaceTool struct{…}

Groups function/custom tools under a shared namespace.

Description string

A description of the namespace shown to the model.

minLength1

Name string

The namespace name used in tool calls (for example, `crm`).

minLength1

Tools []NamespaceToolToolUnion

The function/custom tools available inside this namespace.

One of the following:

type NamespaceToolToolFunction struct{…}

Name string

maxLength128

minLength1

Type Function

DeferLoading boolOptional

Whether this function should be deferred and discovered via tool search.

Description stringOptional

Parameters anyOptional

Strict boolOptional

type CustomTool struct{…}

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

Name string

The name of the custom tool, used to identify it in tool calls.

Type Custom

The type of the custom tool. Always `custom`.

DeferLoading boolOptional

Whether this tool should be deferred and discovered via tool search.

Description stringOptional

Optional description of the custom tool, used to provide more context.

Format [CustomToolInputFormatUnion](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))Optional

The input format for the custom tool. Default is unconstrained text.

One of the following:

type CustomToolInputFormatText struct{…}

Unconstrained free-form text.

Type Text

Unconstrained text format. Always `text`.

type CustomToolInputFormatGrammar struct{…}

A grammar defined by the user.

Definition string

The grammar definition.

Syntax string

The syntax of the grammar definition. One of `lark` or `regex`.

One of the following:

const CustomToolInputFormatGrammarSyntaxLark CustomToolInputFormatGrammarSyntax = "lark"

const CustomToolInputFormatGrammarSyntaxRegex CustomToolInputFormatGrammarSyntax = "regex"

Type Grammar

Grammar format. Always `grammar`.

Type Namespace

The type of the tool. Always `namespace`.

type ToolSearchTool struct{…}

Hosted or BYOT tool search configuration for deferred tools.

Type ToolSearch

The type of the tool. Always `tool_search`.

Description stringOptional

Description shown to the model for a client-executed tool search tool.

Execution ToolSearchToolExecutionOptional

Whether tool search is executed by the server or by the client.

One of the following:

const ToolSearchToolExecutionServer ToolSearchToolExecution = "server"

const ToolSearchToolExecutionClient ToolSearchToolExecution = "client"

Parameters anyOptional

Parameter schema for a client-executed tool search tool.

type WebSearchPreviewTool struct{…}

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type WebSearchPreviewToolType

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

One of the following:

const WebSearchPreviewToolTypeWebSearchPreview WebSearchPreviewToolType = "web\_search\_preview"

const WebSearchPreviewToolTypeWebSearchPreview2025\_03\_11 WebSearchPreviewToolType = "web\_search\_preview\_2025\_03\_11"

SearchContentTypes []stringOptional

One of the following:

const WebSearchPreviewToolSearchContentTypeText WebSearchPreviewToolSearchContentType = "text"

const WebSearchPreviewToolSearchContentTypeImage WebSearchPreviewToolSearchContentType = "image"

SearchContextSize WebSearchPreviewToolSearchContextSizeOptional

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

const WebSearchPreviewToolSearchContextSizeLow WebSearchPreviewToolSearchContextSize = "low"

const WebSearchPreviewToolSearchContextSizeMedium WebSearchPreviewToolSearchContextSize = "medium"

const WebSearchPreviewToolSearchContextSizeHigh WebSearchPreviewToolSearchContextSize = "high"

UserLocation WebSearchPreviewToolUserLocationOptional

The user’s location.

Type Approximate

The type of location approximation. Always `approximate`.

City stringOptional

Free text input for the city of the user, e.g. `San Francisco`.

Country stringOptional

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

Region stringOptional

Free text input for the region of the user, e.g. `California`.

Timezone stringOptional

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

type ApplyPatchTool struct{…}

Allows the assistant to create, delete, or update files using unified diffs.

Type ApplyPatch

The type of the tool. Always `apply_patch`.

Type ToolSearchOutput

The type of the item. Always `tool_search_output`.

CreatedBy stringOptional

The identifier of the actor that created the item.

type ResponseOutputItemAdditionalTools struct{…}

ID string

The unique ID of the additional tools item.

Role string

The role that provided the additional tools.

One of the following:

const ResponseOutputItemAdditionalToolsRoleUnknown ResponseOutputItemAdditionalToolsRole = "unknown"

const ResponseOutputItemAdditionalToolsRoleUser ResponseOutputItemAdditionalToolsRole = "user"

const ResponseOutputItemAdditionalToolsRoleAssistant ResponseOutputItemAdditionalToolsRole = "assistant"

const ResponseOutputItemAdditionalToolsRoleSystem ResponseOutputItemAdditionalToolsRole = "system"

const ResponseOutputItemAdditionalToolsRoleCritic ResponseOutputItemAdditionalToolsRole = "critic"

const ResponseOutputItemAdditionalToolsRoleDiscriminator ResponseOutputItemAdditionalToolsRole = "discriminator"

const ResponseOutputItemAdditionalToolsRoleDeveloper ResponseOutputItemAdditionalToolsRole = "developer"

const ResponseOutputItemAdditionalToolsRoleTool ResponseOutputItemAdditionalToolsRole = "tool"

Tools [][ToolUnion](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20tool%20%3E%20(schema))

The additional tool definitions made available at this item.

One of the following:

type FunctionTool struct{…}

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

Name string

The name of the function to call.

Parameters map[string, any]

A JSON schema object describing the parameters of the function.

Strict bool

Whether to enforce strict parameter validation. Default `true`.

Type Function

The type of the function tool. Always `function`.

DeferLoading boolOptional

Whether this function is deferred and loaded via tool search.

Description stringOptional

A description of the function. Used by the model to determine whether or not to call the function.

type FileSearchTool struct{…}

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

Type FileSearch

The type of the file search tool. Always `file_search`.

VectorStoreIDs []string

The IDs of the vector stores to search.

Filters FileSearchToolFiltersUnionOptional

A filter to apply.

One of the following:

type ComparisonFilter struct{…}

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

Key string

The key to compare against the value.

Type ComparisonFilterType

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

const ComparisonFilterTypeEq ComparisonFilterType = "eq"

const ComparisonFilterTypeNe ComparisonFilterType = "ne"

const ComparisonFilterTypeGt ComparisonFilterType = "gt"

const ComparisonFilterTypeGte ComparisonFilterType = "gte"

const ComparisonFilterTypeLt ComparisonFilterType = "lt"

const ComparisonFilterTypeLte ComparisonFilterType = "lte"

const ComparisonFilterTypeIn ComparisonFilterType = "in"

const ComparisonFilterTypeNin ComparisonFilterType = "nin"

Value ComparisonFilterValueUnion

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

string

float64

bool

type ComparisonFilterValueArray []ComparisonFilterValueArrayItemUnion

One of the following:

string

float64

type CompoundFilter struct{…}

Combine multiple filters using `and` or `or`.

Filters [][ComparisonFilter](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema))

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

One of the following:

type ComparisonFilter struct{…}

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

Key string

The key to compare against the value.

Type ComparisonFilterType

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

const ComparisonFilterTypeEq ComparisonFilterType = "eq"

const ComparisonFilterTypeNe ComparisonFilterType = "ne"

const ComparisonFilterTypeGt ComparisonFilterType = "gt"

const ComparisonFilterTypeGte ComparisonFilterType = "gte"

const ComparisonFilterTypeLt ComparisonFilterType = "lt"

const ComparisonFilterTypeLte ComparisonFilterType = "lte"

const ComparisonFilterTypeIn ComparisonFilterType = "in"

const ComparisonFilterTypeNin ComparisonFilterType = "nin"

Value ComparisonFilterValueUnion

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

string

float64

bool

type ComparisonFilterValueArray []ComparisonFilterValueArrayItemUnion

One of the following:

string

float64

Type CompoundFilterType

Type of operation: `and` or `or`.

One of the following:

const CompoundFilterTypeAnd CompoundFilterType = "and"

const CompoundFilterTypeOr CompoundFilterType = "or"

MaxNumResults int64Optional

The maximum number of results to return. This number should be between 1 and 50 inclusive.

RankingOptions FileSearchToolRankingOptionsOptional

Ranking options for search.

HybridSearch FileSearchToolRankingOptionsHybridSearchOptional

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

EmbeddingWeight float64

The weight of the embedding in the reciprocal ranking fusion.

TextWeight float64

The weight of the text in the reciprocal ranking fusion.

Ranker stringOptional

The ranker to use for the file search.

One of the following:

const FileSearchToolRankingOptionsRankerAuto FileSearchToolRankingOptionsRanker = "auto"

const FileSearchToolRankingOptionsRankerDefault2024\_11\_15 FileSearchToolRankingOptionsRanker = "default-2024-11-15"

ScoreThreshold float64Optional

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

type ComputerTool struct{…}

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

Type Computer

The type of the computer tool. Always `computer`.

type ComputerUsePreviewTool struct{…}

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

DisplayHeight int64

The height of the computer display.

DisplayWidth int64

The width of the computer display.

Environment ComputerUsePreviewToolEnvironment

The type of computer environment to control.

One of the following:

const ComputerUsePreviewToolEnvironmentWindows ComputerUsePreviewToolEnvironment = "windows"

const ComputerUsePreviewToolEnvironmentMac ComputerUsePreviewToolEnvironment = "mac"

const ComputerUsePreviewToolEnvironmentLinux ComputerUsePreviewToolEnvironment = "linux"

const ComputerUsePreviewToolEnvironmentUbuntu ComputerUsePreviewToolEnvironment = "ubuntu"

const ComputerUsePreviewToolEnvironmentBrowser ComputerUsePreviewToolEnvironment = "browser"

Type ComputerUsePreview

The type of the computer use tool. Always `computer_use_preview`.

type WebSearchTool struct{…}

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type WebSearchToolType

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

One of the following:

const WebSearchToolTypeWebSearch WebSearchToolType = "web\_search"

const WebSearchToolTypeWebSearch2025\_08\_26 WebSearchToolType = "web\_search\_2025\_08\_26"

Filters WebSearchToolFiltersOptional

Filters for the search.

AllowedDomains []stringOptional

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

SearchContextSize WebSearchToolSearchContextSizeOptional

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

const WebSearchToolSearchContextSizeLow WebSearchToolSearchContextSize = "low"

const WebSearchToolSearchContextSizeMedium WebSearchToolSearchContextSize = "medium"

const WebSearchToolSearchContextSizeHigh WebSearchToolSearchContextSize = "high"

UserLocation WebSearchToolUserLocationOptional

The approximate location of the user.

City stringOptional

Free text input for the city of the user, e.g. `San Francisco`.

Country stringOptional

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

Region stringOptional

Free text input for the region of the user, e.g. `California`.

Timezone stringOptional

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

Type stringOptional

The type of location approximation. Always `approximate`.

type ToolMcp struct{…}

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

ServerLabel string

A label for this MCP server, used to identify it in tool calls.

Type Mcp

The type of the MCP tool. Always `mcp`.

AllowedTools ToolMcpAllowedToolsUnionOptional

List of allowed tool names or a filter object.

One of the following:

type ToolMcpAllowedToolsMcpAllowedTools []string

A string array of allowed tool names

type ToolMcpAllowedToolsMcpToolFilter struct{…}

A filter object to specify which tools are allowed.

ReadOnly boolOptional

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

ToolNames []stringOptional

List of allowed tool names.

Authorization stringOptional

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

ConnectorID stringOptional

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

const ToolMcpConnectorIDConnectorDropbox ToolMcpConnectorID = "connector\_dropbox"

const ToolMcpConnectorIDConnectorGmail ToolMcpConnectorID = "connector\_gmail"

const ToolMcpConnectorIDConnectorGooglecalendar ToolMcpConnectorID = "connector\_googlecalendar"

const ToolMcpConnectorIDConnectorGoogledrive ToolMcpConnectorID = "connector\_googledrive"

const ToolMcpConnectorIDConnectorMicrosoftteams ToolMcpConnectorID = "connector\_microsoftteams"

const ToolMcpConnectorIDConnectorOutlookcalendar ToolMcpConnectorID = "connector\_outlookcalendar"

const ToolMcpConnectorIDConnectorOutlookemail ToolMcpConnectorID = "connector\_outlookemail"

const ToolMcpConnectorIDConnectorSharepoint ToolMcpConnectorID = "connector\_sharepoint"

DeferLoading boolOptional

Whether this MCP tool is deferred and discovered via tool search.

Headers map[string, string]Optional

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

RequireApproval ToolMcpRequireApprovalUnionOptional

Specify which of the MCP server’s tools require approval.

One of the following:

type ToolMcpRequireApprovalMcpToolApprovalFilter struct{…}

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

Always ToolMcpRequireApprovalMcpToolApprovalFilterAlwaysOptional

A filter object to specify which tools are allowed.

ReadOnly boolOptional

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

ToolNames []stringOptional

List of allowed tool names.

Never ToolMcpRequireApprovalMcpToolApprovalFilterNeverOptional

A filter object to specify which tools are allowed.

ReadOnly boolOptional

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

ToolNames []stringOptional

List of allowed tool names.

type ToolMcpRequireApprovalMcpToolApprovalSetting string

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

One of the following:

const ToolMcpRequireApprovalMcpToolApprovalSettingAlways ToolMcpRequireApprovalMcpToolApprovalSetting = "always"

const ToolMcpRequireApprovalMcpToolApprovalSettingNever ToolMcpRequireApprovalMcpToolApprovalSetting = "never"

ServerDescription stringOptional

Optional description of the MCP server, used to provide more context.

ServerURL stringOptional

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

TunnelID stringOptional

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

type ToolCodeInterpreter struct{…}

A tool that runs Python code to help generate a response to a prompt.

Container ToolCodeInterpreterContainerUnion

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

One of the following:

string

type ToolCodeInterpreterContainerCodeInterpreterContainerAuto struct{…}

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

Type Auto

Always `auto`.

FileIDs []stringOptional

An optional list of uploaded files to make available to your code.

MemoryLimit stringOptional

The memory limit for the code interpreter container.

One of the following:

const ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit1g ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit = "1g"

const ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit4g ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit = "4g"

const ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit16g ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit = "16g"

const ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit64g ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit = "64g"

NetworkPolicy ToolCodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicyUnionOptional

Network access policy for the container.

One of the following:

type ContainerNetworkPolicyDisabled struct{…}

Type Disabled

Disable outbound network access. Always `disabled`.

type ContainerNetworkPolicyAllowlist struct{…}

AllowedDomains []string

A list of allowed domains when type is `allowlist`.

Type Allowlist

Allow outbound network access only to specified domains. Always `allowlist`.

DomainSecrets [][ContainerNetworkPolicyDomainSecret](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema))Optional

Optional domain-scoped secrets for allowlisted domains.

Domain string

The domain associated with the secret.

minLength1

Name string

The name of the secret to inject for the domain.

minLength1

Value string

The secret value to inject for the domain.

maxLength10485760

minLength1

Type CodeInterpreter

The type of the code interpreter tool. Always `code_interpreter`.

type ToolImageGeneration struct{…}

A tool that generates images using the GPT image models.

Type ImageGeneration

The type of the image generation tool. Always `image_generation`.

Action stringOptional

Whether to generate a new image or edit an existing image. Default: `auto`.

One of the following:

const ToolImageGenerationActionGenerate ToolImageGenerationAction = "generate"

const ToolImageGenerationActionEdit ToolImageGenerationAction = "edit"

const ToolImageGenerationActionAuto ToolImageGenerationAction = "auto"

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

One of the following:

const ToolImageGenerationBackgroundTransparent ToolImageGenerationBackground = "transparent"

const ToolImageGenerationBackgroundOpaque ToolImageGenerationBackground = "opaque"

const ToolImageGenerationBackgroundAuto ToolImageGenerationBackground = "auto"

InputFidelity stringOptional

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

One of the following:

const ToolImageGenerationInputFidelityHigh ToolImageGenerationInputFidelity = "high"

const ToolImageGenerationInputFidelityLow ToolImageGenerationInputFidelity = "low"

InputImageMask ToolImageGenerationInputImageMaskOptional

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

FileID stringOptional

File ID for the mask image.

ImageURL stringOptional

Base64-encoded mask image.

Model stringOptional

The image generation model to use. Default: `gpt-image-1`.

One of the following:

string

string

One of the following:

const ToolImageGenerationModelGPTImage1 ToolImageGenerationModel = "gpt-image-1"

const ToolImageGenerationModelGPTImage1Mini ToolImageGenerationModel = "gpt-image-1-mini"

const ToolImageGenerationModelGPTImage2 ToolImageGenerationModel = "gpt-image-2"

const ToolImageGenerationModelGPTImage2\_2026\_04\_21 ToolImageGenerationModel = "gpt-image-2-2026-04-21"

const ToolImageGenerationModelGPTImage1\_5 ToolImageGenerationModel = "gpt-image-1.5"

const ToolImageGenerationModelChatgptImageLatest ToolImageGenerationModel = "chatgpt-image-latest"

Moderation stringOptional

Moderation level for the generated image. Default: `auto`.

One of the following:

const ToolImageGenerationModerationAuto ToolImageGenerationModeration = "auto"

const ToolImageGenerationModerationLow ToolImageGenerationModeration = "low"

OutputCompression int64Optional

Compression level for the output image. Default: 100.

minimum0

maximum100

OutputFormat stringOptional

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

One of the following:

const ToolImageGenerationOutputFormatPNG ToolImageGenerationOutputFormat = "png"

const ToolImageGenerationOutputFormatWebP ToolImageGenerationOutputFormat = "webp"

const ToolImageGenerationOutputFormatJPEG ToolImageGenerationOutputFormat = "jpeg"

PartialImages int64Optional

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

Quality stringOptional

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

One of the following:

const ToolImageGenerationQualityLow ToolImageGenerationQuality = "low"

const ToolImageGenerationQualityMedium ToolImageGenerationQuality = "medium"

const ToolImageGenerationQualityHigh ToolImageGenerationQuality = "high"

const ToolImageGenerationQualityAuto ToolImageGenerationQuality = "auto"

Size stringOptional

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

One of the following:

string

string

One of the following:

const ToolImageGenerationSize1024x1024 ToolImageGenerationSize = "1024x1024"

const ToolImageGenerationSize1024x1536 ToolImageGenerationSize = "1024x1536"

const ToolImageGenerationSize1536x1024 ToolImageGenerationSize = "1536x1024"

const ToolImageGenerationSizeAuto ToolImageGenerationSize = "auto"

type ToolLocalShell struct{…}

A tool that allows the model to execute shell commands in a local environment.

Type LocalShell

The type of the local shell tool. Always `local_shell`.

type FunctionShellTool struct{…}

A tool that allows the model to execute shell commands.

Type Shell

The type of the shell tool. Always `shell`.

Environment FunctionShellToolEnvironmentUnionOptional

One of the following:

type ContainerAuto struct{…}

Type ContainerAuto

Automatically creates a container for this request

FileIDs []stringOptional

An optional list of uploaded files to make available to your code.

MemoryLimit ContainerAutoMemoryLimitOptional

The memory limit for the container.

One of the following:

const ContainerAutoMemoryLimit1g ContainerAutoMemoryLimit = "1g"

const ContainerAutoMemoryLimit4g ContainerAutoMemoryLimit = "4g"

const ContainerAutoMemoryLimit16g ContainerAutoMemoryLimit = "16g"

const ContainerAutoMemoryLimit64g ContainerAutoMemoryLimit = "64g"

NetworkPolicy ContainerAutoNetworkPolicyUnionOptional

Network access policy for the container.

One of the following:

type ContainerNetworkPolicyDisabled struct{…}

Type Disabled

Disable outbound network access. Always `disabled`.

type ContainerNetworkPolicyAllowlist struct{…}

AllowedDomains []string

A list of allowed domains when type is `allowlist`.

Type Allowlist

Allow outbound network access only to specified domains. Always `allowlist`.

DomainSecrets [][ContainerNetworkPolicyDomainSecret](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema))Optional

Optional domain-scoped secrets for allowlisted domains.

Domain string

The domain associated with the secret.

minLength1

Name string

The name of the secret to inject for the domain.

minLength1

Value string

The secret value to inject for the domain.

maxLength10485760

minLength1

Skills []ContainerAutoSkillUnionOptional

An optional list of skills referenced by id or inline data.

One of the following:

type SkillReference struct{…}

SkillID string

The ID of the referenced skill.

maxLength64

minLength1

Type SkillReference

References a skill created with the /v1/skills endpoint.

Version stringOptional

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

type InlineSkill struct{…}

Description string

The description of the skill.

Name string

The name of the skill.

Source [InlineSkillSource](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill_source%20%3E%20(schema))

Inline skill payload

Data string

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

MediaType ApplicationZip

The media type of the inline skill payload. Must be `application/zip`.

Type Base64

The type of the inline skill source. Must be `base64`.

Type Inline

Defines an inline skill for this request.

type LocalEnvironment struct{…}

Type Local

Use a local computer environment.

Skills [][LocalSkill](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20local_skill%20%3E%20(schema))Optional

An optional list of skills.

Description string

The description of the skill.

Name string

The name of the skill.

Path string

The path to the directory containing the skill.

type ContainerReference struct{…}

ContainerID string

The ID of the referenced container.

Type ContainerReference

References a container created with the /v1/containers endpoint

type CustomTool struct{…}

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

Name string

The name of the custom tool, used to identify it in tool calls.

Type Custom

The type of the custom tool. Always `custom`.

DeferLoading boolOptional

Whether this tool should be deferred and discovered via tool search.

Description stringOptional

Optional description of the custom tool, used to provide more context.

Format [CustomToolInputFormatUnion](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))Optional

The input format for the custom tool. Default is unconstrained text.

One of the following:

type CustomToolInputFormatText struct{…}

Unconstrained free-form text.

Type Text

Unconstrained text format. Always `text`.

type CustomToolInputFormatGrammar struct{…}

A grammar defined by the user.

Definition string

The grammar definition.

Syntax string

The syntax of the grammar definition. One of `lark` or `regex`.

One of the following:

const CustomToolInputFormatGrammarSyntaxLark CustomToolInputFormatGrammarSyntax = "lark"

const CustomToolInputFormatGrammarSyntaxRegex CustomToolInputFormatGrammarSyntax = "regex"

Type Grammar

Grammar format. Always `grammar`.

type NamespaceTool struct{…}

Groups function/custom tools under a shared namespace.

Description string

A description of the namespace shown to the model.

minLength1

Name string

The namespace name used in tool calls (for example, `crm`).

minLength1

Tools []NamespaceToolToolUnion

The function/custom tools available inside this namespace.

One of the following:

type NamespaceToolToolFunction struct{…}

Name string

maxLength128

minLength1

Type Function

DeferLoading boolOptional

Whether this function should be deferred and discovered via tool search.

Description stringOptional

Parameters anyOptional

Strict boolOptional

type CustomTool struct{…}

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

Name string

The name of the custom tool, used to identify it in tool calls.

Type Custom

The type of the custom tool. Always `custom`.

DeferLoading boolOptional

Whether this tool should be deferred and discovered via tool search.

Description stringOptional

Optional description of the custom tool, used to provide more context.

Format [CustomToolInputFormatUnion](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))Optional

The input format for the custom tool. Default is unconstrained text.

One of the following:

type CustomToolInputFormatText struct{…}

Unconstrained free-form text.

Type Text

Unconstrained text format. Always `text`.

type CustomToolInputFormatGrammar struct{…}

A grammar defined by the user.

Definition string

The grammar definition.

Syntax string

The syntax of the grammar definition. One of `lark` or `regex`.

One of the following:

const CustomToolInputFormatGrammarSyntaxLark CustomToolInputFormatGrammarSyntax = "lark"

const CustomToolInputFormatGrammarSyntaxRegex CustomToolInputFormatGrammarSyntax = "regex"

Type Grammar

Grammar format. Always `grammar`.

Type Namespace

The type of the tool. Always `namespace`.

type ToolSearchTool struct{…}

Hosted or BYOT tool search configuration for deferred tools.

Type ToolSearch

The type of the tool. Always `tool_search`.

Description stringOptional

Description shown to the model for a client-executed tool search tool.

Execution ToolSearchToolExecutionOptional

Whether tool search is executed by the server or by the client.

One of the following:

const ToolSearchToolExecutionServer ToolSearchToolExecution = "server"

const ToolSearchToolExecutionClient ToolSearchToolExecution = "client"

Parameters anyOptional

Parameter schema for a client-executed tool search tool.

type WebSearchPreviewTool struct{…}

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type WebSearchPreviewToolType

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

One of the following:

const WebSearchPreviewToolTypeWebSearchPreview WebSearchPreviewToolType = "web\_search\_preview"

const WebSearchPreviewToolTypeWebSearchPreview2025\_03\_11 WebSearchPreviewToolType = "web\_search\_preview\_2025\_03\_11"

SearchContentTypes []stringOptional

One of the following:

const WebSearchPreviewToolSearchContentTypeText WebSearchPreviewToolSearchContentType = "text"

const WebSearchPreviewToolSearchContentTypeImage WebSearchPreviewToolSearchContentType = "image"

SearchContextSize WebSearchPreviewToolSearchContextSizeOptional

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

const WebSearchPreviewToolSearchContextSizeLow WebSearchPreviewToolSearchContextSize = "low"

const WebSearchPreviewToolSearchContextSizeMedium WebSearchPreviewToolSearchContextSize = "medium"

const WebSearchPreviewToolSearchContextSizeHigh WebSearchPreviewToolSearchContextSize = "high"

UserLocation WebSearchPreviewToolUserLocationOptional

The user’s location.

Type Approximate

The type of location approximation. Always `approximate`.

City stringOptional

Free text input for the city of the user, e.g. `San Francisco`.

Country stringOptional

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

Region stringOptional

Free text input for the region of the user, e.g. `California`.

Timezone stringOptional

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

type ApplyPatchTool struct{…}

Allows the assistant to create, delete, or update files using unified diffs.

Type ApplyPatch

The type of the tool. Always `apply_patch`.

Type AdditionalTools

The type of the item. Always `additional_tools`.

type ResponseCompactionItem struct{…}

A compaction item generated by the [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).

ID string

The unique ID of the compaction item.

EncryptedContent string

The encrypted content that was produced by compaction.

Type Compaction

The type of the item. Always `compaction`.

CreatedBy stringOptional

The identifier of the actor that created the item.

type ResponseOutputItemImageGenerationCall struct{…}

An image generation request made by the model.

ID string

The unique ID of the image generation call.

Result string

The generated image encoded in base64.

Status string

The status of the image generation call.

One of the following:

const ResponseOutputItemImageGenerationCallStatusInProgress ResponseOutputItemImageGenerationCallStatus = "in\_progress"

const ResponseOutputItemImageGenerationCallStatusCompleted ResponseOutputItemImageGenerationCallStatus = "completed"

const ResponseOutputItemImageGenerationCallStatusGenerating ResponseOutputItemImageGenerationCallStatus = "generating"

const ResponseOutputItemImageGenerationCallStatusFailed ResponseOutputItemImageGenerationCallStatus = "failed"

Type ImageGenerationCall

The type of the image generation call. Always `image_generation_call`.

type ResponseCodeInterpreterToolCall struct{…}

A tool call to run code.

ID string

The unique ID of the code interpreter tool call.

Code string

The code to run, or null if not available.

ContainerID string

The ID of the container used to run the code.

Outputs []ResponseCodeInterpreterToolCallOutputUnion

The outputs generated by the code interpreter, such as logs or images.
Can be null if no outputs are available.

One of the following:

type ResponseCodeInterpreterToolCallOutputLogs struct{…}

The logs output from the code interpreter.

Logs string

The logs output from the code interpreter.

Type Logs

The type of the output. Always `logs`.

type ResponseCodeInterpreterToolCallOutputImage struct{…}

The image output from the code interpreter.

Type Image

The type of the output. Always `image`.

URL string

The URL of the image output from the code interpreter.

formaturi

Status ResponseCodeInterpreterToolCallStatus

The status of the code interpreter tool call. Valid values are `in_progress`, `completed`, `incomplete`, `interpreting`, and `failed`.

One of the following:

const ResponseCodeInterpreterToolCallStatusInProgress ResponseCodeInterpreterToolCallStatus = "in\_progress"

const ResponseCodeInterpreterToolCallStatusCompleted ResponseCodeInterpreterToolCallStatus = "completed"

const ResponseCodeInterpreterToolCallStatusIncomplete ResponseCodeInterpreterToolCallStatus = "incomplete"

const ResponseCodeInterpreterToolCallStatusInterpreting ResponseCodeInterpreterToolCallStatus = "interpreting"

const ResponseCodeInterpreterToolCallStatusFailed ResponseCodeInterpreterToolCallStatus = "failed"

Type CodeInterpreterCall

The type of the code interpreter tool call. Always `code_interpreter_call`.

type ResponseOutputItemLocalShellCall struct{…}

A tool call to run a command on the local shell.

ID string

The unique ID of the local shell call.

Action ResponseOutputItemLocalShellCallAction

Execute a shell command on the server.

Command []string

The command to run.

Env map[string, string]

Environment variables to set for the command.

Type Exec

The type of the local shell action. Always `exec`.

TimeoutMs int64Optional

Optional timeout in milliseconds for the command.

User stringOptional

Optional user to run the command as.

WorkingDirectory stringOptional

Optional working directory to run the command in.

CallID string

The unique ID of the local shell tool call generated by the model.

Status string

The status of the local shell call.

One of the following:

const ResponseOutputItemLocalShellCallStatusInProgress ResponseOutputItemLocalShellCallStatus = "in\_progress"

const ResponseOutputItemLocalShellCallStatusCompleted ResponseOutputItemLocalShellCallStatus = "completed"

const ResponseOutputItemLocalShellCallStatusIncomplete ResponseOutputItemLocalShellCallStatus = "incomplete"

Type LocalShellCall

The type of the local shell call. Always `local_shell_call`.

type ResponseOutputItemLocalShellCallOutput struct{…}

The output of a local shell tool call.

ID string

The unique ID of the local shell tool call generated by the model.

Output string

A JSON string of the output of the local shell tool call.

Type LocalShellCallOutput

The type of the local shell tool call output. Always `local_shell_call_output`.

Status stringOptional

The status of the item. One of `in_progress`, `completed`, or `incomplete`.

One of the following:

const ResponseOutputItemLocalShellCallOutputStatusInProgress ResponseOutputItemLocalShellCallOutputStatus = "in\_progress"

const ResponseOutputItemLocalShellCallOutputStatusCompleted ResponseOutputItemLocalShellCallOutputStatus = "completed"

const ResponseOutputItemLocalShellCallOutputStatusIncomplete ResponseOutputItemLocalShellCallOutputStatus = "incomplete"

type ResponseFunctionShellToolCall struct{…}

A tool call that executes one or more shell commands in a managed environment.

ID string

The unique ID of the shell tool call. Populated when this item is returned via API.

Action ResponseFunctionShellToolCallAction

The shell commands and limits that describe how to run the tool call.

Commands []string

MaxOutputLength int64

Optional maximum number of characters to return from each command.

TimeoutMs int64

Optional timeout in milliseconds for the commands.

CallID string

The unique ID of the shell tool call generated by the model.

Environment ResponseFunctionShellToolCallEnvironmentUnion

Represents the use of a local environment to perform shell actions.

One of the following:

type ResponseLocalEnvironment struct{…}

Represents the use of a local environment to perform shell actions.

Type Local

The environment type. Always `local`.

type ResponseContainerReference struct{…}

Represents a container created with /v1/containers.

ContainerID string

Type ContainerReference

The environment type. Always `container_reference`.

Status ResponseFunctionShellToolCallStatus

The status of the shell call. One of `in_progress`, `completed`, or `incomplete`.

One of the following:

const ResponseFunctionShellToolCallStatusInProgress ResponseFunctionShellToolCallStatus = "in\_progress"

const ResponseFunctionShellToolCallStatusCompleted ResponseFunctionShellToolCallStatus = "completed"

const ResponseFunctionShellToolCallStatusIncomplete ResponseFunctionShellToolCallStatus = "incomplete"

Type ShellCall

The type of the item. Always `shell_call`.

CreatedBy stringOptional

The ID of the entity that created this tool call.

type ResponseFunctionShellToolCallOutput struct{…}

The output of a shell tool call that was emitted.

ID string

The unique ID of the shell call output. Populated when this item is returned via API.

CallID string

The unique ID of the shell tool call generated by the model.

MaxOutputLength int64

The maximum length of the shell command output. This is generated by the model and should be passed back with the raw output.

Output []ResponseFunctionShellToolCallOutputOutput

An array of shell call output contents

Outcome ResponseFunctionShellToolCallOutputOutputOutcomeUnion

Represents either an exit outcome (with an exit code) or a timeout outcome for a shell call output chunk.

One of the following:

type ResponseFunctionShellToolCallOutputOutputOutcomeTimeout struct{…}

Indicates that the shell call exceeded its configured time limit.

Type Timeout

The outcome type. Always `timeout`.

type ResponseFunctionShellToolCallOutputOutputOutcomeExit struct{…}

Indicates that the shell commands finished and returned an exit code.

ExitCode int64

Exit code from the shell process.

Type Exit

The outcome type. Always `exit`.

Stderr string

The standard error output that was captured.

Stdout string

The standard output that was captured.

CreatedBy stringOptional

The identifier of the actor that created the item.

Status ResponseFunctionShellToolCallOutputStatus

The status of the shell call output. One of `in_progress`, `completed`, or `incomplete`.

One of the following:

const ResponseFunctionShellToolCallOutputStatusInProgress ResponseFunctionShellToolCallOutputStatus = "in\_progress"

const ResponseFunctionShellToolCallOutputStatusCompleted ResponseFunctionShellToolCallOutputStatus = "completed"

const ResponseFunctionShellToolCallOutputStatusIncomplete ResponseFunctionShellToolCallOutputStatus = "incomplete"

Type ShellCallOutput

The type of the shell call output. Always `shell_call_output`.

CreatedBy stringOptional

The identifier of the actor that created the item.

type ResponseApplyPatchToolCall struct{…}

A tool call that applies file diffs by creating, deleting, or updating files.

ID string

The unique ID of the apply patch tool call. Populated when this item is returned via API.

CallID string

The unique ID of the apply patch tool call generated by the model.

Operation ResponseApplyPatchToolCallOperationUnion

One of the create\_file, delete\_file, or update\_file operations applied via apply\_patch.

One of the following:

type ResponseApplyPatchToolCallOperationCreateFile struct{…}

Instruction describing how to create a file via the apply\_patch tool.

Diff string

Diff to apply.

Path string

Path of the file to create.

Type CreateFile

Create a new file with the provided diff.

type ResponseApplyPatchToolCallOperationDeleteFile struct{…}

Instruction describing how to delete a file via the apply\_patch tool.

Path string

Path of the file to delete.

Type DeleteFile

Delete the specified file.

type ResponseApplyPatchToolCallOperationUpdateFile struct{…}

Instruction describing how to update a file via the apply\_patch tool.

Diff string

Diff to apply.

Path string

Path of the file to update.

Type UpdateFile

Update an existing file with the provided diff.

Status ResponseApplyPatchToolCallStatus

The status of the apply patch tool call. One of `in_progress` or `completed`.

One of the following:

const ResponseApplyPatchToolCallStatusInProgress ResponseApplyPatchToolCallStatus = "in\_progress"

const ResponseApplyPatchToolCallStatusCompleted ResponseApplyPatchToolCallStatus = "completed"

Type ApplyPatchCall

The type of the item. Always `apply_patch_call`.

CreatedBy stringOptional

The ID of the entity that created this tool call.

type ResponseApplyPatchToolCallOutput struct{…}

The output emitted by an apply patch tool call.

ID string

The unique ID of the apply patch tool call output. Populated when this item is returned via API.

CallID string

The unique ID of the apply patch tool call generated by the model.

Status ResponseApplyPatchToolCallOutputStatus

The status of the apply patch tool call output. One of `completed` or `failed`.

One of the following:

const ResponseApplyPatchToolCallOutputStatusCompleted ResponseApplyPatchToolCallOutputStatus = "completed"

const ResponseApplyPatchToolCallOutputStatusFailed ResponseApplyPatchToolCallOutputStatus = "failed"

Type ApplyPatchCallOutput

The type of the item. Always `apply_patch_call_output`.

CreatedBy stringOptional

The ID of the entity that created this tool call output.

Output stringOptional

Optional textual output returned by the apply patch tool.

type ResponseOutputItemMcpCall struct{…}

An invocation of a tool on an MCP server.

ID string

The unique ID of the tool call.

Arguments string

A JSON string of the arguments passed to the tool.

Name string

The name of the tool that was run.

ServerLabel string

The label of the MCP server running the tool.

Type McpCall

The type of the item. Always `mcp_call`.

ApprovalRequestID stringOptional

Unique identifier for the MCP tool call approval request.
Include this value in a subsequent `mcp_approval_response` input to approve or reject the corresponding tool call.

Error stringOptional

The error from the tool call, if any.

Output stringOptional

The output from the tool call.

Status stringOptional

The status of the tool call. One of `in_progress`, `completed`, `incomplete`, `calling`, or `failed`.

One of the following:

const ResponseOutputItemMcpCallStatusInProgress ResponseOutputItemMcpCallStatus = "in\_progress"

const ResponseOutputItemMcpCallStatusCompleted ResponseOutputItemMcpCallStatus = "completed"

const ResponseOutputItemMcpCallStatusIncomplete ResponseOutputItemMcpCallStatus = "incomplete"

const ResponseOutputItemMcpCallStatusCalling ResponseOutputItemMcpCallStatus = "calling"

const ResponseOutputItemMcpCallStatusFailed ResponseOutputItemMcpCallStatus = "failed"

type ResponseOutputItemMcpListTools struct{…}

A list of tools available on an MCP server.

ID string

The unique ID of the list.

ServerLabel string

The label of the MCP server.

Tools []ResponseOutputItemMcpListToolsTool

The tools available on the server.

InputSchema any

The JSON schema describing the tool’s input.

Name string

The name of the tool.

Annotations anyOptional

Additional annotations about the tool.

Description stringOptional

The description of the tool.

Type McpListTools

The type of the item. Always `mcp_list_tools`.

Error stringOptional

Error message if the server could not list tools.

type ResponseOutputItemMcpApprovalRequest struct{…}

A request for human approval of a tool invocation.

ID string

The unique ID of the approval request.

Arguments string

A JSON string of arguments for the tool.

Name string

The name of the tool to run.

ServerLabel string

The label of the MCP server making the request.

Type McpApprovalRequest

The type of the item. Always `mcp_approval_request`.

type ResponseOutputItemMcpApprovalResponse struct{…}

A response to an MCP approval request.

ID string

The unique ID of the approval response

ApprovalRequestID string

The ID of the approval request being answered.

Approve bool

Whether the request was approved.

Type McpApprovalResponse

The type of the item. Always `mcp_approval_response`.

Reason stringOptional

Optional reason for the decision.

type ResponseCustomToolCall struct{…}

A call to a custom tool created by the model.

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

Namespace stringOptional

The namespace of the custom tool being called.

type ResponseCustomToolCallOutputItem struct{…}

The output of a custom tool call from your code, being sent back to the model.

ID string

The unique ID of the custom tool call output item.

Status string

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

One of the following:

const ResponseCustomToolCallOutputItemStatusInProgress ResponseCustomToolCallOutputItemStatus = "in\_progress"

const ResponseCustomToolCallOutputItemStatusCompleted ResponseCustomToolCallOutputItemStatus = "completed"

const ResponseCustomToolCallOutputItemStatusIncomplete ResponseCustomToolCallOutputItemStatus = "incomplete"

CreatedBy stringOptional

The identifier of the actor that created the item.

Usage [ResponseUsage](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20response_usage%20%3E%20(schema))

Token accounting for the compaction pass, including cached, reasoning, and total tokens.

InputTokens int64

The number of input tokens.

InputTokensDetails ResponseUsageInputTokensDetails

A detailed breakdown of the input tokens.

CachedTokens int64

The number of tokens that were retrieved from the cache.
[More on prompt caching](https://platform.openai.com/docs/guides/prompt-caching).

OutputTokens int64

The number of output tokens.

OutputTokensDetails ResponseUsageOutputTokensDetails

A detailed breakdown of the output tokens.

ReasoningTokens int64

The number of reasoning tokens.

TotalTokens int64

The total number of tokens used.

### Compact a response

Go

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
  "github.com/openai/openai-go/responses"

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  compactedResponse, err := client.Responses.Compact(context.TODO(), responses.ResponseCompactParams{
    Model: responses.ResponseCompactParamsModelGPT5_4,
  })
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", compactedResponse.ID)

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
      "id": "cmp_001",
      "type": "compaction",
      "encrypted_content": "gAAAAABpM0Yj-...="
  ],
  "usage": {
    "input_tokens": 139,
    "input_tokens_details": {
      "cached_tokens": 0
    "output_tokens": 438,
    "output_tokens_details": {
      "reasoning_tokens": 64
    "total_tokens": 577

##### Returns Examples

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
      "id": "cmp_001",
      "type": "compaction",
      "encrypted_content": "gAAAAABpM0Yj-...="
  ],
  "usage": {
    "input_tokens": 139,
    "input_tokens_details": {
      "cached_tokens": 0
    "output_tokens": 438,
    "output_tokens_details": {
      "reasoning_tokens": 64
    "total_tokens": 577
