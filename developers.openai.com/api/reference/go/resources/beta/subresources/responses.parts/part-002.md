<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/responses/ -->
<!-- part of: https://developers.openai.com/api/reference/go/resources/beta/subresources/responses/ -->

<!-- chunk-start -->

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

Actions [BetaComputerActionList](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_computer_action_list%20%3E%20(schema))Optional

Agent BetaResponseComputerToolCallAgentOptional

AgentName string

type BetaResponseComputerToolCallOutputItem struct{…}

ID string

The unique ID of the computer call tool output.

CallID string

Output [BetaResponseComputerToolCallOutputScreenshot](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_computer_tool_call_output_screenshot%20%3E%20(schema))

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

type BetaResponseOutputItemAddedEvent struct{…}

Emitted when a new output item is added.

Item [BetaResponseOutputItemUnion](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_item%20%3E%20(schema))

The output item that was added.

OutputIndex int64

The index of the output item that was added.

SequenceNumber int64

The sequence number of this event.

Type ResponseOutputItemAdded

The type of the event. Always `response.output_item.added`.

Agent BetaResponseOutputItemAddedEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseOutputItemDoneEvent struct{…}

Emitted when an output item is marked done.

Item [BetaResponseOutputItemUnion](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_item%20%3E%20(schema))

The output item that was marked done.

OutputIndex int64

The index of the output item that was marked done.

SequenceNumber int64

The sequence number of this event.

Type ResponseOutputItemDone

The type of the event. Always `response.output_item.done`.

Agent BetaResponseOutputItemDoneEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

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

type BetaResponseOutputRefusal struct{…}

Refusal string

Type Refusal

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

type BetaResponseOutputTextAnnotationAddedEvent struct{…}

Emitted when an annotation is added to output text content.

Annotation any

The annotation object being added. (See annotation schema for details.)

AnnotationIndex int64

The index of the annotation within the content part.

ContentIndex int64

The index of the content part within the output item.

ItemID string

The unique identifier of the item to which the annotation is being added.

OutputIndex int64

The index of the output item in the response’s output array.

SequenceNumber int64

The sequence number of this event.

Type ResponseOutputTextAnnotationAdded

The type of the event. Always ‘response.output\_text.annotation.added’.

Agent BetaResponseOutputTextAnnotationAddedEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponsePrompt struct{…}

Reference to a prompt template and its variables.
[Learn more](https://platform.openai.com/docs/guides/text?api-mode=responses#reusable-prompts).

ID string

The unique identifier of the prompt template to use.

Variables map[string, BetaResponsePromptVariableUnion]Optional

Optional map of values to substitute in for variables in your
prompt. The substitution values can either be strings, or other
Response input types like images or files.

string

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

Version stringOptional

Optional version of the prompt template.

type BetaResponseQueuedEvent struct{…}

Emitted when a response is queued and waiting to be processed.

Response [BetaResponse](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema))

The full response object that is queued.

SequenceNumber int64

The sequence number for this event.

Type ResponseQueued

The type of the event. Always ‘response.queued’.

Agent BetaResponseQueuedEventAgentOptional

The agent that owns this multi-agent streaming event.

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

type BetaResponseReasoningSummaryPartAddedEvent struct{…}

Emitted when a new reasoning summary part is added.

ItemID string

The ID of the item this summary part is associated with.

OutputIndex int64

The index of the output item this summary part is associated with.

Part BetaResponseReasoningSummaryPartAddedEventPart

The summary part that was added.

Text string

The text of the summary part.

Type SummaryText

The type of the summary part. Always `summary_text`.

SequenceNumber int64

The sequence number of this event.

SummaryIndex int64

The index of the summary part within the reasoning summary.

Type ResponseReasoningSummaryPartAdded

The type of the event. Always `response.reasoning_summary_part.added`.

Agent BetaResponseReasoningSummaryPartAddedEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseReasoningSummaryPartDoneEvent struct{…}

Emitted when a reasoning summary part is completed.

ItemID string

The ID of the item this summary part is associated with.

OutputIndex int64

The index of the output item this summary part is associated with.

Part BetaResponseReasoningSummaryPartDoneEventPart

The completed summary part.

Text string

The text of the summary part.

Type SummaryText

The type of the summary part. Always `summary_text`.

SequenceNumber int64

The sequence number of this event.

SummaryIndex int64

The index of the summary part within the reasoning summary.

Type ResponseReasoningSummaryPartDone

The type of the event. Always `response.reasoning_summary_part.done`.

Agent BetaResponseReasoningSummaryPartDoneEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

Status BetaResponseReasoningSummaryPartDoneEventStatusOptional

The completion status of the summary part. Omitted when the part completed
normally and set to `incomplete` when generation was interrupted.

type BetaResponseReasoningSummaryTextDeltaEvent struct{…}

Emitted when a delta is added to a reasoning summary text.

Delta string

The text delta that was added to the summary.

ItemID string

The ID of the item this summary text delta is associated with.

OutputIndex int64

The index of the output item this summary text delta is associated with.

SequenceNumber int64

The sequence number of this event.

SummaryIndex int64

The index of the summary part within the reasoning summary.

Type ResponseReasoningSummaryTextDelta

The type of the event. Always `response.reasoning_summary_text.delta`.

Agent BetaResponseReasoningSummaryTextDeltaEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseReasoningSummaryTextDoneEvent struct{…}

Emitted when a reasoning summary text is completed.

ItemID string

The ID of the item this summary text is associated with.

OutputIndex int64

The index of the output item this summary text is associated with.

SequenceNumber int64

The sequence number of this event.

SummaryIndex int64

The index of the summary part within the reasoning summary.

Text string

The full text of the completed reasoning summary.

Type ResponseReasoningSummaryTextDone

The type of the event. Always `response.reasoning_summary_text.done`.

Agent BetaResponseReasoningSummaryTextDoneEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseReasoningTextDeltaEvent struct{…}

Emitted when a delta is added to a reasoning text.

ContentIndex int64

The index of the reasoning content part this delta is associated with.

Delta string

The text delta that was added to the reasoning content.

ItemID string

The ID of the item this reasoning text delta is associated with.

OutputIndex int64

The index of the output item this reasoning text delta is associated with.

SequenceNumber int64

The sequence number of this event.

Type ResponseReasoningTextDelta

The type of the event. Always `response.reasoning_text.delta`.

Agent BetaResponseReasoningTextDeltaEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseReasoningTextDoneEvent struct{…}

Emitted when a reasoning text is completed.

ContentIndex int64

The index of the reasoning content part.

ItemID string

The ID of the item this reasoning text is associated with.

OutputIndex int64

The index of the output item this reasoning text is associated with.

SequenceNumber int64

The sequence number of this event.

Text string

The full text of the completed reasoning content.

Type ResponseReasoningTextDone

The type of the event. Always `response.reasoning_text.done`.

Agent BetaResponseReasoningTextDoneEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseRefusalDeltaEvent struct{…}

Emitted when there is a partial refusal text.

ContentIndex int64

The index of the content part that the refusal text is added to.

Delta string

The refusal text that is added.

ItemID string

The ID of the output item that the refusal text is added to.

OutputIndex int64

The index of the output item that the refusal text is added to.

SequenceNumber int64

The sequence number of this event.

Type ResponseRefusalDelta

The type of the event. Always `response.refusal.delta`.

Agent BetaResponseRefusalDeltaEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseRefusalDoneEvent struct{…}

Emitted when refusal text is finalized.

ContentIndex int64

The index of the content part that the refusal text is finalized.

ItemID string

The ID of the output item that the refusal text is finalized.

OutputIndex int64

The index of the output item that the refusal text is finalized.

Refusal string

The refusal text that is finalized.

SequenceNumber int64

The sequence number of this event.

Type ResponseRefusalDone

The type of the event. Always `response.refusal.done`.

Agent BetaResponseRefusalDoneEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseStatus string

The status of the response generation. One of `completed`, `failed`,
`in_progress`, `cancelled`, `queued`, or `incomplete`.

const BetaResponseStatusCompleted [BetaResponseStatus](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_status%20%3E%20(schema)) = "completed"

const BetaResponseStatusFailed [BetaResponseStatus](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_status%20%3E%20(schema)) = "failed"

const BetaResponseStatusInProgress [BetaResponseStatus](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_status%20%3E%20(schema)) = "in\_progress"

const BetaResponseStatusCancelled [BetaResponseStatus](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_status%20%3E%20(schema)) = "cancelled"

const BetaResponseStatusQueued [BetaResponseStatus](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_status%20%3E%20(schema)) = "queued"

const BetaResponseStatusIncomplete [BetaResponseStatus](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_status%20%3E%20(schema)) = "incomplete"

type BetaResponseStreamEventUnion interface{…}

Emitted when there is a partial audio response.

type BetaResponseAudioDeltaEvent struct{…}

Emitted when there is a partial audio response.

Delta string

A chunk of Base64 encoded response audio bytes.

SequenceNumber int64

A sequence number for this chunk of the stream response.

Type ResponseAudioDelta

The type of the event. Always `response.audio.delta`.

Agent BetaResponseAudioDeltaEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseAudioDoneEvent struct{…}

Emitted when the audio response is complete.

SequenceNumber int64

The sequence number of the delta.

Type ResponseAudioDone

The type of the event. Always `response.audio.done`.

Agent BetaResponseAudioDoneEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseAudioTranscriptDeltaEvent struct{…}

Emitted when there is a partial transcript of audio.

Delta string

The partial transcript of the audio response.

SequenceNumber int64

The sequence number of this event.

Type ResponseAudioTranscriptDelta

The type of the event. Always `response.audio.transcript.delta`.

Agent BetaResponseAudioTranscriptDeltaEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseAudioTranscriptDoneEvent struct{…}

Emitted when the full audio transcript is completed.

SequenceNumber int64

The sequence number of this event.

Type ResponseAudioTranscriptDone

The type of the event. Always `response.audio.transcript.done`.

Agent BetaResponseAudioTranscriptDoneEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseCodeInterpreterCallCodeDeltaEvent struct{…}

Emitted when a partial code snippet is streamed by the code interpreter.

Delta string

The partial code snippet being streamed by the code interpreter.

ItemID string

The unique identifier of the code interpreter tool call item.

OutputIndex int64

The index of the output item in the response for which the code is being streamed.

SequenceNumber int64

The sequence number of this event, used to order streaming events.

Type ResponseCodeInterpreterCallCodeDelta

The type of the event. Always `response.code_interpreter_call_code.delta`.

Agent BetaResponseCodeInterpreterCallCodeDeltaEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseCodeInterpreterCallCodeDoneEvent struct{…}

Emitted when the code snippet is finalized by the code interpreter.

Code string

The final code snippet output by the code interpreter.

ItemID string

The unique identifier of the code interpreter tool call item.

OutputIndex int64

The index of the output item in the response for which the code is finalized.

SequenceNumber int64

The sequence number of this event, used to order streaming events.

Type ResponseCodeInterpreterCallCodeDone

The type of the event. Always `response.code_interpreter_call_code.done`.

Agent BetaResponseCodeInterpreterCallCodeDoneEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseCodeInterpreterCallCompletedEvent struct{…}

Emitted when the code interpreter call is completed.

ItemID string

The unique identifier of the code interpreter tool call item.

OutputIndex int64

The index of the output item in the response for which the code interpreter call is completed.

SequenceNumber int64

The sequence number of this event, used to order streaming events.

Type ResponseCodeInterpreterCallCompleted

The type of the event. Always `response.code_interpreter_call.completed`.

Agent BetaResponseCodeInterpreterCallCompletedEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseCodeInterpreterCallInProgressEvent struct{…}

Emitted when a code interpreter call is in progress.

ItemID string

The unique identifier of the code interpreter tool call item.

OutputIndex int64

The index of the output item in the response for which the code interpreter call is in progress.

SequenceNumber int64

The sequence number of this event, used to order streaming events.

Type ResponseCodeInterpreterCallInProgress

The type of the event. Always `response.code_interpreter_call.in_progress`.

Agent BetaResponseCodeInterpreterCallInProgressEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseCodeInterpreterCallInterpretingEvent struct{…}

Emitted when the code interpreter is actively interpreting the code snippet.

ItemID string

The unique identifier of the code interpreter tool call item.

OutputIndex int64

The index of the output item in the response for which the code interpreter is interpreting code.

SequenceNumber int64

The sequence number of this event, used to order streaming events.

Type ResponseCodeInterpreterCallInterpreting

The type of the event. Always `response.code_interpreter_call.interpreting`.

Agent BetaResponseCodeInterpreterCallInterpretingEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseCompletedEvent struct{…}

Emitted when the model response is complete.

Response [BetaResponse](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema))

Properties of the completed response.

SequenceNumber int64

The sequence number for this event.

Type ResponseCompleted

The type of the event. Always `response.completed`.

Agent BetaResponseCompletedEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseContentPartAddedEvent struct{…}

Emitted when a new content part is added.

ContentIndex int64

The index of the content part that was added.

ItemID string

The ID of the output item that the content part was added to.

OutputIndex int64

The index of the output item that the content part was added to.

Part BetaResponseContentPartAddedEventPartUnion

The content part that was added.

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

type BetaResponseContentPartAddedEventPartReasoningText struct{…}

Text string

Type ReasoningText

SequenceNumber int64

The sequence number of this event.

Type ResponseContentPartAdded

The type of the event. Always `response.content_part.added`.

Agent BetaResponseContentPartAddedEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseContentPartDoneEvent struct{…}

Emitted when a content part is done.

ContentIndex int64

The index of the content part that is done.

ItemID string

The ID of the output item that the content part was added to.

OutputIndex int64

The index of the output item that the content part was added to.

Part BetaResponseContentPartDoneEventPartUnion

The content part that is done.

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

type BetaResponseContentPartDoneEventPartReasoningText struct{…}

Text string

Type ReasoningText

SequenceNumber int64

The sequence number of this event.

Type ResponseContentPartDone

The type of the event. Always `response.content_part.done`.

Agent BetaResponseContentPartDoneEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseCreatedEvent struct{…}

An event that is emitted when a response is created.

Response [BetaResponse](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema))

The response that was created.

SequenceNumber int64

The sequence number for this event.

Type ResponseCreated

The type of the event. Always `response.created`.

Agent BetaResponseCreatedEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseErrorEvent struct{…}

Emitted when an error occurs.

Code string

The error code.

Message string

The error message.

Param string

The error parameter.

SequenceNumber int64

The sequence number of this event.

Type Error

The type of the event. Always `error`.

Agent BetaResponseErrorEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseFileSearchCallCompletedEvent struct{…}

Emitted when a file search call is completed (results found).

ItemID string

The ID of the output item that the file search call is initiated.

OutputIndex int64

The index of the output item that the file search call is initiated.

SequenceNumber int64

The sequence number of this event.

Type ResponseFileSearchCallCompleted

The type of the event. Always `response.file_search_call.completed`.

Agent BetaResponseFileSearchCallCompletedEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseFileSearchCallInProgressEvent struct{…}

Emitted when a file search call is initiated.

ItemID string

The ID of the output item that the file search call is initiated.

OutputIndex int64

The index of the output item that the file search call is initiated.

SequenceNumber int64

The sequence number of this event.

Type ResponseFileSearchCallInProgress

The type of the event. Always `response.file_search_call.in_progress`.

Agent BetaResponseFileSearchCallInProgressEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseFileSearchCallSearchingEvent struct{…}

Emitted when a file search is currently searching.

ItemID string

The ID of the output item that the file search call is initiated.

OutputIndex int64

The index of the output item that the file search call is searching.

SequenceNumber int64

The sequence number of this event.

Type ResponseFileSearchCallSearching

The type of the event. Always `response.file_search_call.searching`.

Agent BetaResponseFileSearchCallSearchingEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseFunctionCallArgumentsDeltaEvent struct{…}

Emitted when there is a partial function-call arguments delta.

Delta string

The function-call arguments delta that is added.

ItemID string

The ID of the output item that the function-call arguments delta is added to.

OutputIndex int64

The index of the output item that the function-call arguments delta is added to.

SequenceNumber int64

The sequence number of this event.

Type ResponseFunctionCallArgumentsDelta

The type of the event. Always `response.function_call_arguments.delta`.

Agent BetaResponseFunctionCallArgumentsDeltaEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseFunctionCallArgumentsDoneEvent struct{…}

Emitted when function-call arguments are finalized.

Arguments string

The function-call arguments.

ItemID string

The ID of the item.

Name string

The name of the function that was called.

OutputIndex int64

The index of the output item.

SequenceNumber int64

The sequence number of this event.

Type ResponseFunctionCallArgumentsDone

Agent BetaResponseFunctionCallArgumentsDoneEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseInProgressEvent struct{…}

Emitted when the response is in progress.

Response [BetaResponse](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema))

The response that is in progress.

SequenceNumber int64

The sequence number of this event.

Type ResponseInProgress

The type of the event. Always `response.in_progress`.

Agent BetaResponseInProgressEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseFailedEvent struct{…}

An event that is emitted when a response fails.

Response [BetaResponse](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema))

The response that failed.

SequenceNumber int64

The sequence number of this event.

Type ResponseFailed

The type of the event. Always `response.failed`.

Agent BetaResponseFailedEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseIncompleteEvent struct{…}

An event that is emitted when a response finishes as incomplete.

Response [BetaResponse](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema))

The response that was incomplete.

SequenceNumber int64

The sequence number of this event.

Type ResponseIncomplete

The type of the event. Always `response.incomplete`.

Agent BetaResponseIncompleteEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseOutputItemAddedEvent struct{…}

Emitted when a new output item is added.

Item [BetaResponseOutputItemUnion](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_item%20%3E%20(schema))

The output item that was added.

OutputIndex int64

The index of the output item that was added.

SequenceNumber int64

The sequence number of this event.

Type ResponseOutputItemAdded

The type of the event. Always `response.output_item.added`.

Agent BetaResponseOutputItemAddedEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseOutputItemDoneEvent struct{…}

Emitted when an output item is marked done.

Item [BetaResponseOutputItemUnion](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_item%20%3E%20(schema))

The output item that was marked done.

OutputIndex int64

The index of the output item that was marked done.

SequenceNumber int64

The sequence number of this event.

Type ResponseOutputItemDone

The type of the event. Always `response.output_item.done`.

Agent BetaResponseOutputItemDoneEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseReasoningSummaryPartAddedEvent struct{…}

Emitted when a new reasoning summary part is added.

ItemID string

The ID of the item this summary part is associated with.

OutputIndex int64

The index of the output item this summary part is associated with.

Part BetaResponseReasoningSummaryPartAddedEventPart

The summary part that was added.

Text string

The text of the summary part.

Type SummaryText

The type of the summary part. Always `summary_text`.

SequenceNumber int64

The sequence number of this event.

SummaryIndex int64

The index of the summary part within the reasoning summary.

Type ResponseReasoningSummaryPartAdded

The type of the event. Always `response.reasoning_summary_part.added`.

Agent BetaResponseReasoningSummaryPartAddedEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseReasoningSummaryPartDoneEvent struct{…}

Emitted when a reasoning summary part is completed.

ItemID string

The ID of the item this summary part is associated with.

OutputIndex int64

The index of the output item this summary part is associated with.

Part BetaResponseReasoningSummaryPartDoneEventPart

The completed summary part.

Text string

The text of the summary part.

Type SummaryText

The type of the summary part. Always `summary_text`.

SequenceNumber int64

The sequence number of this event.

SummaryIndex int64

The index of the summary part within the reasoning summary.

Type ResponseReasoningSummaryPartDone

The type of the event. Always `response.reasoning_summary_part.done`.

Agent BetaResponseReasoningSummaryPartDoneEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

Status BetaResponseReasoningSummaryPartDoneEventStatusOptional

The completion status of the summary part. Omitted when the part completed
normally and set to `incomplete` when generation was interrupted.

type BetaResponseReasoningSummaryTextDeltaEvent struct{…}

Emitted when a delta is added to a reasoning summary text.

Delta string

The text delta that was added to the summary.

ItemID string

The ID of the item this summary text delta is associated with.

OutputIndex int64

The index of the output item this summary text delta is associated with.

SequenceNumber int64

The sequence number of this event.

SummaryIndex int64

The index of the summary part within the reasoning summary.

Type ResponseReasoningSummaryTextDelta

The type of the event. Always `response.reasoning_summary_text.delta`.

Agent BetaResponseReasoningSummaryTextDeltaEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseReasoningSummaryTextDoneEvent struct{…}

Emitted when a reasoning summary text is completed.

ItemID string

The ID of the item this summary text is associated with.

OutputIndex int64

The index of the output item this summary text is associated with.

SequenceNumber int64

The sequence number of this event.

SummaryIndex int64

The index of the summary part within the reasoning summary.

Text string

The full text of the completed reasoning summary.

Type ResponseReasoningSummaryTextDone

The type of the event. Always `response.reasoning_summary_text.done`.

Agent BetaResponseReasoningSummaryTextDoneEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseReasoningTextDeltaEvent struct{…}

Emitted when a delta is added to a reasoning text.

ContentIndex int64

The index of the reasoning content part this delta is associated with.

Delta string

The text delta that was added to the reasoning content.

ItemID string

The ID of the item this reasoning text delta is associated with.

OutputIndex int64

The index of the output item this reasoning text delta is associated with.

SequenceNumber int64

The sequence number of this event.

Type ResponseReasoningTextDelta

The type of the event. Always `response.reasoning_text.delta`.

Agent BetaResponseReasoningTextDeltaEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseReasoningTextDoneEvent struct{…}

Emitted when a reasoning text is completed.

ContentIndex int64

The index of the reasoning content part.

ItemID string

The ID of the item this reasoning text is associated with.

OutputIndex int64

The index of the output item this reasoning text is associated with.

SequenceNumber int64

The sequence number of this event.

Text string

The full text of the completed reasoning content.

Type ResponseReasoningTextDone

The type of the event. Always `response.reasoning_text.done`.

Agent BetaResponseReasoningTextDoneEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseRefusalDeltaEvent struct{…}

Emitted when there is a partial refusal text.

ContentIndex int64

The index of the content part that the refusal text is added to.

Delta string

The refusal text that is added.

ItemID string

The ID of the output item that the refusal text is added to.

OutputIndex int64

The index of the output item that the refusal text is added to.

SequenceNumber int64

The sequence number of this event.

Type ResponseRefusalDelta

The type of the event. Always `response.refusal.delta`.

Agent BetaResponseRefusalDeltaEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseRefusalDoneEvent struct{…}

Emitted when refusal text is finalized.

ContentIndex int64

The index of the content part that the refusal text is finalized.

ItemID string

The ID of the output item that the refusal text is finalized.

OutputIndex int64

The index of the output item that the refusal text is finalized.

Refusal string

The refusal text that is finalized.

SequenceNumber int64

The sequence number of this event.

Type ResponseRefusalDone

The type of the event. Always `response.refusal.done`.

Agent BetaResponseRefusalDoneEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseTextDeltaEvent struct{…}

Emitted when there is an additional text delta.

ContentIndex int64

The index of the content part that the text delta was added to.

Delta string

The text delta that was added.

ItemID string

The ID of the output item that the text delta was added to.

Logprobs []BetaResponseTextDeltaEventLogprob

The log probabilities of the tokens in the delta.

Token string

A possible text token.

Logprob float64

The log probability of this token.

TopLogprobs []BetaResponseTextDeltaEventLogprobTopLogprobOptional

The log probabilities of up to 20 of the most likely tokens.

Token stringOptional

A possible text token.

Logprob float64Optional

The log probability of this token.

OutputIndex int64

The index of the output item that the text delta was added to.

SequenceNumber int64

The sequence number for this event.

Type ResponseOutputTextDelta

The type of the event. Always `response.output_text.delta`.

Agent BetaResponseTextDeltaEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseTextDoneEvent struct{…}

Emitted when text content is finalized.

ContentIndex int64

The index of the content part that the text content is finalized.

ItemID string

The ID of the output item that the text content is finalized.

Logprobs []BetaResponseTextDoneEventLogprob

The log probabilities of the tokens in the delta.

Token string

A possible text token.

Logprob float64

The log probability of this token.

TopLogprobs []BetaResponseTextDoneEventLogprobTopLogprobOptional

The log probabilities of up to 20 of the most likely tokens.

Token stringOptional

A possible text token.

Logprob float64Optional

The log probability of this token.

OutputIndex int64

The index of the output item that the text content is finalized.

SequenceNumber int64

The sequence number for this event.

Text string

The text content that is finalized.

Type ResponseOutputTextDone

The type of the event. Always `response.output_text.done`.

Agent BetaResponseTextDoneEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseWebSearchCallCompletedEvent struct{…}

Emitted when a web search call is completed.

ItemID string

Unique ID for the output item associated with the web search call.

OutputIndex int64

The index of the output item that the web search call is associated with.

SequenceNumber int64

The sequence number of the web search call being processed.

Type ResponseWebSearchCallCompleted

The type of the event. Always `response.web_search_call.completed`.

Agent BetaResponseWebSearchCallCompletedEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseWebSearchCallInProgressEvent struct{…}

Emitted when a web search call is initiated.

ItemID string

Unique ID for the output item associated with the web search call.

OutputIndex int64

The index of the output item that the web search call is associated with.

SequenceNumber int64

The sequence number of the web search call being processed.

Type ResponseWebSearchCallInProgress

The type of the event. Always `response.web_search_call.in_progress`.

Agent BetaResponseWebSearchCallInProgressEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseWebSearchCallSearchingEvent struct{…}

Emitted when a web search call is executing.

ItemID string

Unique ID for the output item associated with the web search call.

OutputIndex int64

The index of the output item that the web search call is associated with.

SequenceNumber int64

The sequence number of the web search call being processed.

Type ResponseWebSearchCallSearching

The type of the event. Always `response.web_search_call.searching`.

Agent BetaResponseWebSearchCallSearchingEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseImageGenCallCompletedEvent struct{…}

Emitted when an image generation tool call has completed and the final image is available.

ItemID string

The unique identifier of the image generation item being processed.

OutputIndex int64

The index of the output item in the response’s output array.

SequenceNumber int64

The sequence number of this event.

Type ResponseImageGenerationCallCompleted

The type of the event. Always ‘response.image\_generation\_call.completed’.

Agent BetaResponseImageGenCallCompletedEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseImageGenCallGeneratingEvent struct{…}

Emitted when an image generation tool call is actively generating an image (intermediate state).

ItemID string

The unique identifier of the image generation item being processed.

OutputIndex int64

The index of the output item in the response’s output array.

SequenceNumber int64

The sequence number of the image generation item being processed.

Type ResponseImageGenerationCallGenerating

The type of the event. Always ‘response.image\_generation\_call.generating’.

Agent BetaResponseImageGenCallGeneratingEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseImageGenCallInProgressEvent struct{…}

Emitted when an image generation tool call is in progress.

ItemID string

The unique identifier of the image generation item being processed.

OutputIndex int64

The index of the output item in the response’s output array.

SequenceNumber int64

The sequence number of the image generation item being processed.

Type ResponseImageGenerationCallInProgress

The type of the event. Always ‘response.image\_generation\_call.in\_progress’.

Agent BetaResponseImageGenCallInProgressEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseImageGenCallPartialImageEvent struct{…}

Emitted when a partial image is available during image generation streaming.

ItemID string

The unique identifier of the image generation item being processed.

OutputIndex int64

The index of the output item in the response’s output array.

PartialImageB64 string

Base64-encoded partial image data, suitable for rendering as an image.

PartialImageIndex int64

0-based index for the partial image (backend is 1-based, but this is 0-based for the user).

SequenceNumber int64

The sequence number of the image generation item being processed.

Type ResponseImageGenerationCallPartialImage

The type of the event. Always ‘response.image\_generation\_call.partial\_image’.

Agent BetaResponseImageGenCallPartialImageEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseMcpCallArgumentsDeltaEvent struct{…}

Emitted when there is a delta (partial update) to the arguments of an MCP tool call.

Delta string

A JSON string containing the partial update to the arguments for the MCP tool call.

ItemID string

The unique identifier of the MCP tool call item being processed.

OutputIndex int64

The index of the output item in the response’s output array.

SequenceNumber int64

The sequence number of this event.

Type ResponseMcpCallArgumentsDelta

The type of the event. Always ‘response.mcp\_call\_arguments.delta’.

Agent BetaResponseMcpCallArgumentsDeltaEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseMcpCallArgumentsDoneEvent struct{…}

Emitted when the arguments for an MCP tool call are finalized.

Arguments string

A JSON string containing the finalized arguments for the MCP tool call.

ItemID string

The unique identifier of the MCP tool call item being processed.

OutputIndex int64

The index of the output item in the response’s output array.

SequenceNumber int64

The sequence number of this event.

Type ResponseMcpCallArgumentsDone

The type of the event. Always ‘response.mcp\_call\_arguments.done’.

Agent BetaResponseMcpCallArgumentsDoneEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseMcpCallCompletedEvent struct{…}

Emitted when an MCP tool call has completed successfully.

ItemID string

The ID of the MCP tool call item that completed.

OutputIndex int64

The index of the output item that completed.

SequenceNumber int64

The sequence number of this event.

Type ResponseMcpCallCompleted

The type of the event. Always ‘response.mcp\_call.completed’.

Agent BetaResponseMcpCallCompletedEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseMcpCallFailedEvent struct{…}

Emitted when an MCP tool call has failed.

ItemID string

The ID of the MCP tool call item that failed.

OutputIndex int64

The index of the output item that failed.

SequenceNumber int64

The sequence number of this event.

Type ResponseMcpCallFailed

The type of the event. Always ‘response.mcp\_call.failed’.

Agent BetaResponseMcpCallFailedEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseMcpCallInProgressEvent struct{…}

Emitted when an MCP tool call is in progress.

ItemID string

The unique identifier of the MCP tool call item being processed.

OutputIndex int64

The index of the output item in the response’s output array.

SequenceNumber int64

The sequence number of this event.

Type ResponseMcpCallInProgress

The type of the event. Always ‘response.mcp\_call.in\_progress’.

Agent BetaResponseMcpCallInProgressEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseMcpListToolsCompletedEvent struct{…}

Emitted when the list of available MCP tools has been successfully retrieved.

ItemID string

The ID of the MCP tool call item that produced this output.

OutputIndex int64

The index of the output item that was processed.

SequenceNumber int64

The sequence number of this event.

Type ResponseMcpListToolsCompleted

The type of the event. Always ‘response.mcp\_list\_tools.completed’.

Agent BetaResponseMcpListToolsCompletedEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseMcpListToolsFailedEvent struct{…}

Emitted when the attempt to list available MCP tools has failed.

ItemID string

The ID of the MCP tool call item that failed.

OutputIndex int64

The index of the output item that failed.

SequenceNumber int64

The sequence number of this event.

Type ResponseMcpListToolsFailed

The type of the event. Always ‘response.mcp\_list\_tools.failed’.

Agent BetaResponseMcpListToolsFailedEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseMcpListToolsInProgressEvent struct{…}

Emitted when the system is in the process of retrieving the list of available MCP tools.

ItemID string

The ID of the MCP tool call item that is being processed.

OutputIndex int64

The index of the output item that is being processed.

SequenceNumber int64

The sequence number of this event.

Type ResponseMcpListToolsInProgress

The type of the event. Always ‘response.mcp\_list\_tools.in\_progress’.

Agent BetaResponseMcpListToolsInProgressEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseOutputTextAnnotationAddedEvent struct{…}

Emitted when an annotation is added to output text content.

Annotation any

The annotation object being added. (See annotation schema for details.)

AnnotationIndex int64

The index of the annotation within the content part.

ContentIndex int64

The index of the content part within the output item.

ItemID string

The unique identifier of the item to which the annotation is being added.

OutputIndex int64

The index of the output item in the response’s output array.

SequenceNumber int64

The sequence number of this event.

Type ResponseOutputTextAnnotationAdded

The type of the event. Always ‘response.output\_text.annotation.added’.

Agent BetaResponseOutputTextAnnotationAddedEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseQueuedEvent struct{…}

Emitted when a response is queued and waiting to be processed.

Response [BetaResponse](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema))

The full response object that is queued.

SequenceNumber int64

The sequence number for this event.

Type ResponseQueued

The type of the event. Always ‘response.queued’.

Agent BetaResponseQueuedEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseCustomToolCallInputDeltaEvent struct{…}

Event representing a delta (partial update) to the input of a custom tool call.

Delta string

The incremental input data (delta) for the custom tool call.

ItemID string

Unique identifier for the API item associated with this event.

OutputIndex int64

The index of the output this delta applies to.

SequenceNumber int64

The sequence number of this event.

Type ResponseCustomToolCallInputDelta

The event type identifier.

Agent BetaResponseCustomToolCallInputDeltaEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseCustomToolCallInputDoneEvent struct{…}

Event indicating that input for a custom tool call is complete.

Input string

The complete input data for the custom tool call.

ItemID string

Unique identifier for the API item associated with this event.

OutputIndex int64

The index of the output this event applies to.

SequenceNumber int64

The sequence number of this event.

Type ResponseCustomToolCallInputDone

The event type identifier.

Agent BetaResponseCustomToolCallInputDoneEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseTextConfig struct{…}

Configuration options for a text response from the model. Can be plain
text or structured JSON data. Learn more:

* [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
* [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

Format [BetaResponseFormatTextConfigUnion](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_format_text_config%20%3E%20(schema))Optional

An object specifying the format that the model must output.

Configuring `{ "type": "json_schema" }` enables Structured Outputs,
which ensures the model will match your supplied JSON schema. Learn more in the
[Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

The default format is `{ "type": "text" }` with no additional options.

**Not recommended for gpt-4o and newer models:**

Setting to `{ "type": "json_object" }` enables the older JSON mode, which
ensures the message the model generates is valid JSON. Using `json_schema`
is preferred for models that support it.

Verbosity BetaResponseTextConfigVerbosityOptional

Constrains the verbosity of the model’s response. Lower values will result in
more concise responses, while higher values will result in more verbose responses.
Currently supported values are `low`, `medium`, and `high`.

const BetaResponseTextConfigVerbosityLow BetaResponseTextConfigVerbosity = "low"

const BetaResponseTextConfigVerbosityMedium BetaResponseTextConfigVerbosity = "medium"

const BetaResponseTextConfigVerbosityHigh BetaResponseTextConfigVerbosity = "high"

type BetaResponseTextDeltaEvent struct{…}

Emitted when there is an additional text delta.

ContentIndex int64

The index of the content part that the text delta was added to.

Delta string

The text delta that was added.

ItemID string

The ID of the output item that the text delta was added to.

Logprobs []BetaResponseTextDeltaEventLogprob

The log probabilities of the tokens in the delta.

Token string

A possible text token.

Logprob float64

The log probability of this token.

TopLogprobs []BetaResponseTextDeltaEventLogprobTopLogprobOptional

The log probabilities of up to 20 of the most likely tokens.

Token stringOptional

A possible text token.

Logprob float64Optional

The log probability of this token.

OutputIndex int64

The index of the output item that the text delta was added to.

SequenceNumber int64

The sequence number for this event.

Type ResponseOutputTextDelta

The type of the event. Always `response.output_text.delta`.

Agent BetaResponseTextDeltaEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseTextDoneEvent struct{…}

Emitted when text content is finalized.

ContentIndex int64

The index of the content part that the text content is finalized.

ItemID string

The ID of the output item that the text content is finalized.

Logprobs []BetaResponseTextDoneEventLogprob

The log probabilities of the tokens in the delta.

Token string

A possible text token.

Logprob float64

The log probability of this token.

TopLogprobs []BetaResponseTextDoneEventLogprobTopLogprobOptional

The log probabilities of up to 20 of the most likely tokens.

Token stringOptional

A possible text token.

Logprob float64Optional

The log probability of this token.

OutputIndex int64

The index of the output item that the text content is finalized.

SequenceNumber int64

The sequence number for this event.

Text string

The text content that is finalized.

Type ResponseOutputTextDone

The type of the event. Always `response.output_text.done`.

Agent BetaResponseTextDoneEventAgentOptional

The agent that owns this multi-agent streaming event.

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

type BetaResponseUsage struct{…}

Represents token usage details including input tokens, output tokens,
a breakdown of output tokens, and the total tokens used.

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

type BetaResponseWebSearchCallCompletedEvent struct{…}

Emitted when a web search call is completed.

ItemID string

Unique ID for the output item associated with the web search call.

OutputIndex int64

The index of the output item that the web search call is associated with.

SequenceNumber int64

The sequence number of the web search call being processed.

Type ResponseWebSearchCallCompleted

The type of the event. Always `response.web_search_call.completed`.

Agent BetaResponseWebSearchCallCompletedEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseWebSearchCallInProgressEvent struct{…}

Emitted when a web search call is initiated.

ItemID string

Unique ID for the output item associated with the web search call.

OutputIndex int64

The index of the output item that the web search call is associated with.

SequenceNumber int64

The sequence number of the web search call being processed.

Type ResponseWebSearchCallInProgress

The type of the event. Always `response.web_search_call.in_progress`.

Agent BetaResponseWebSearchCallInProgressEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseWebSearchCallSearchingEvent struct{…}

Emitted when a web search call is executing.

ItemID string

Unique ID for the output item associated with the web search call.

OutputIndex int64

The index of the output item that the web search call is associated with.

SequenceNumber int64

The sequence number of the web search call being processed.

Type ResponseWebSearchCallSearching

The type of the event. Always `response.web_search_call.searching`.

Agent BetaResponseWebSearchCallSearchingEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponsesClientEventUnion interface{…}

Client events accepted by the Responses WebSocket server.

BetaResponsesClientEventResponseCreate

Type ResponseCreate

The type of the client event. Always `response.create`.

Background boolOptional

Whether to run the model response in the background.
[Learn more](https://platform.openai.com/docs/guides/background).

ContextManagement []BetaResponsesClientEventResponseCreateContextManagementOptional

Context management configuration for this request.

Type string

The context management entry type. Currently only ‘compaction’ is supported.

CompactThreshold int64Optional

Token threshold at which compaction should be triggered for this entry.

minimum1000

Conversation BetaResponsesClientEventResponseCreateConversationUnionOptional

The conversation that this response belongs to. Items from this conversation are prepended to `input_items` for this response request.
Input items and output items from this response are automatically added to this conversation after this response completes.

string

type BetaResponseConversationParamResp struct{…}

The conversation that this response belongs to.

ID string

The unique ID of the conversation.

Include [][BetaResponseIncludable](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_includable%20%3E%20(schema))Optional

Specify additional output data to include in the model response. Currently supported values are:

* `web_search_call.action.sources`: Include the sources of the web search tool call.
* `code_interpreter_call.outputs`: Includes the outputs of python code execution in code interpreter tool call items.
* `computer_call_output.output.image_url`: Include image urls from the computer call output.
* `file_search_call.results`: Include the search results of the file search tool call.
* `message.input_image.image_url`: Include image urls from the input message.
* `message.output_text.logprobs`: Include logprobs with assistant messages.
* `reasoning.encrypted_content`: Includes an encrypted version of reasoning tokens in reasoning item outputs. This enables reasoning items to be used in multi-turn conversations when using the Responses API statelessly (like when the `store` parameter is set to `false`, or when an organization is enrolled in the zero data retention program).

const BetaResponseIncludableFileSearchCallResults [BetaResponseIncludable](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_includable%20%3E%20(schema)) = "file\_search\_call.results"

const BetaResponseIncludableWebSearchCallResults [BetaResponseIncludable](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_includable%20%3E%20(schema)) = "web\_search\_call.results"

const BetaResponseIncludableWebSearchCallActionSources [BetaResponseIncludable](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_includable%20%3E%20(schema)) = "web\_search\_call.action.sources"

const BetaResponseIncludableMessageInputImageImageURL [BetaResponseIncludable](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_includable%20%3E%20(schema)) = "message.input\_image.image\_url"

const BetaResponseIncludableComputerCallOutputOutputImageURL [BetaResponseIncludable](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_includable%20%3E%20(schema)) = "computer\_call\_output.output.image\_url"

const BetaResponseIncludableCodeInterpreterCallOutputs [BetaResponseIncludable](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_includable%20%3E%20(schema)) = "code\_interpreter\_call.outputs"

const BetaResponseIncludableReasoningEncryptedContent [BetaResponseIncludable](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_includable%20%3E%20(schema)) = "reasoning.encrypted\_content"

const BetaResponseIncludableMessageOutputTextLogprobs [BetaResponseIncludable](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_includable%20%3E%20(schema)) = "message.output\_text.logprobs"

Input BetaResponsesClientEventResponseCreateInputUnionOptional

Text, image, or file inputs to the model, used to generate a response.

Learn more:

* [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
* [Image inputs](https://platform.openai.com/docs/guides/images)
* [File inputs](https://platform.openai.com/docs/guides/pdf-files)
* [Conversation state](https://platform.openai.com/docs/guides/conversation-state)
* [Function calling](https://platform.openai.com/docs/guides/function-calling)

string

type BetaResponseInput [][BetaResponseInputItemUnion](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_item%20%3E%20(schema))

A list of one or many input items to the model, containing
different content types.

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

Actions [BetaComputerActionList](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_computer_action_list%20%3E%20(schema))Optional

Agent BetaResponseComputerToolCallAgentOptional

AgentName string

type BetaResponseInputItemComputerCallOutput struct{…}

The output of a computer tool call.

CallID string

maxLength64

minLength1

Output [BetaResponseComputerToolCallOutputScreenshot](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_computer_tool_call_output_screenshot%20%3E%20(schema))

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

Instructions stringOptional

A system (or developer) message inserted into the model’s context.

When using along with `previous_response_id`, the instructions from a previous
response will not be carried over to the next response. This makes it simple
to swap out system (or developer) messages in new responses.

MaxOutputTokens int64Optional

An upper bound for the number of tokens that can be generated for a response, including visible output tokens and [reasoning tokens](https://platform.openai.com/docs/guides/reasoning).

minimum16

MaxToolCalls int64Optional

The maximum number of total calls to built-in tools that can be processed in a response. This maximum number applies across all built-in tool calls, not per individual tool. Any further attempts to call a tool by the model will be ignored.

Metadata map[string, string]Optional

format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

Model BetaResponsesClientEventResponseCreateModelOptional

Model ID used to generate the response, like `gpt-4o` or `o3`. OpenAI
offers a wide range of models with different capabilities, performance
characteristics, and price points. Refer to the [model guide](https://platform.openai.com/docs/models)
to browse and compare available models.

BetaResponsesClientEventResponseCreateModel

const BetaResponsesClientEventResponseCreateModelGPT5\_6Sol BetaResponsesClientEventResponseCreateModel = "gpt-5.6-sol"

const BetaResponsesClientEventResponseCreateModelGPT5\_6Terra BetaResponsesClientEventResponseCreateModel = "gpt-5.6-terra"

const BetaResponsesClientEventResponseCreateModelGPT5\_6Luna BetaResponsesClientEventResponseCreateModel = "gpt-5.6-luna"

const BetaResponsesClientEventResponseCreateModelGPT5\_4 BetaResponsesClientEventResponseCreateModel = "gpt-5.4"

const BetaResponsesClientEventResponseCreateModelGPT5\_4Mini BetaResponsesClientEventResponseCreateModel = "gpt-5.4-mini"

const BetaResponsesClientEventResponseCreateModelGPT5\_4Nano BetaResponsesClientEventResponseCreateModel = "gpt-5.4-nano"

const BetaResponsesClientEventResponseCreateModelGPT5\_4Mini2026\_03\_17 BetaResponsesClientEventResponseCreateModel = "gpt-5.4-mini-2026-03-17"

const BetaResponsesClientEventResponseCreateModelGPT5\_4Nano2026\_03\_17 BetaResponsesClientEventResponseCreateModel = "gpt-5.4-nano-2026-03-17"

const BetaResponsesClientEventResponseCreateModelGPT5\_3ChatLatest BetaResponsesClientEventResponseCreateModel = "gpt-5.3-chat-latest"

const BetaResponsesClientEventResponseCreateModelGPT5\_2 BetaResponsesClientEventResponseCreateModel = "gpt-5.2"

const BetaResponsesClientEventResponseCreateModelGPT5\_2\_2025\_12\_11 BetaResponsesClientEventResponseCreateModel = "gpt-5.2-2025-12-11"

const BetaResponsesClientEventResponseCreateModelGPT5\_2ChatLatest BetaResponsesClientEventResponseCreateModel = "gpt-5.2-chat-latest"

const BetaResponsesClientEventResponseCreateModelGPT5\_2Pro BetaResponsesClientEventResponseCreateModel = "gpt-5.2-pro"

const BetaResponsesClientEventResponseCreateModelGPT5\_2Pro2025\_12\_11 BetaResponsesClientEventResponseCreateModel = "gpt-5.2-pro-2025-12-11"

const BetaResponsesClientEventResponseCreateModelGPT5\_1 BetaResponsesClientEventResponseCreateModel = "gpt-5.1"

const BetaResponsesClientEventResponseCreateModelGPT5\_1\_2025\_11\_13 BetaResponsesClientEventResponseCreateModel = "gpt-5.1-2025-11-13"

const BetaResponsesClientEventResponseCreateModelGPT5\_1Codex BetaResponsesClientEventResponseCreateModel = "gpt-5.1-codex"

const BetaResponsesClientEventResponseCreateModelGPT5\_1Mini BetaResponsesClientEventResponseCreateModel = "gpt-5.1-mini"

const BetaResponsesClientEventResponseCreateModelGPT5\_1ChatLatest BetaResponsesClientEventResponseCreateModel = "gpt-5.1-chat-latest"

const BetaResponsesClientEventResponseCreateModelGPT5 BetaResponsesClientEventResponseCreateModel = "gpt-5"

const BetaResponsesClientEventResponseCreateModelGPT5Mini BetaResponsesClientEventResponseCreateModel = "gpt-5-mini"

const BetaResponsesClientEventResponseCreateModelGPT5Nano BetaResponsesClientEventResponseCreateModel = "gpt-5-nano"

const BetaResponsesClientEventResponseCreateModelGPT5\_2025\_08\_07 BetaResponsesClientEventResponseCreateModel = "gpt-5-2025-08-07"

const BetaResponsesClientEventResponseCreateModelGPT5Mini2025\_08\_07 BetaResponsesClientEventResponseCreateModel = "gpt-5-mini-2025-08-07"

const BetaResponsesClientEventResponseCreateModelGPT5Nano2025\_08\_07 BetaResponsesClientEventResponseCreateModel = "gpt-5-nano-2025-08-07"

const BetaResponsesClientEventResponseCreateModelGPT5ChatLatest BetaResponsesClientEventResponseCreateModel = "gpt-5-chat-latest"

const BetaResponsesClientEventResponseCreateModelGPT4\_1 BetaResponsesClientEventResponseCreateModel = "gpt-4.1"

const BetaResponsesClientEventResponseCreateModelGPT4\_1Mini BetaResponsesClientEventResponseCreateModel = "gpt-4.1-mini"

const BetaResponsesClientEventResponseCreateModelGPT4\_1Nano BetaResponsesClientEventResponseCreateModel = "gpt-4.1-nano"

const BetaResponsesClientEventResponseCreateModelGPT4\_1\_2025\_04\_14 BetaResponsesClientEventResponseCreateModel = "gpt-4.1-2025-04-14"

const BetaResponsesClientEventResponseCreateModelGPT4\_1Mini2025\_04\_14 BetaResponsesClientEventResponseCreateModel = "gpt-4.1-mini-2025-04-14"

const BetaResponsesClientEventResponseCreateModelGPT4\_1Nano2025\_04\_14 BetaResponsesClientEventResponseCreateModel = "gpt-4.1-nano-2025-04-14"

const BetaResponsesClientEventResponseCreateModelO4Mini BetaResponsesClientEventResponseCreateModel = "o4-mini"

const BetaResponsesClientEventResponseCreateModelO4Mini2025\_04\_16 BetaResponsesClientEventResponseCreateModel = "o4-mini-2025-04-16"

const BetaResponsesClientEventResponseCreateModelO3 BetaResponsesClientEventResponseCreateModel = "o3"

const BetaResponsesClientEventResponseCreateModelO3\_2025\_04\_16 BetaResponsesClientEventResponseCreateModel = "o3-2025-04-16"

const BetaResponsesClientEventResponseCreateModelO3Mini BetaResponsesClientEventResponseCreateModel = "o3-mini"

const BetaResponsesClientEventResponseCreateModelO3Mini2025\_01\_31 BetaResponsesClientEventResponseCreateModel = "o3-mini-2025-01-31"

const BetaResponsesClientEventResponseCreateModelO1 BetaResponsesClientEventResponseCreateModel = "o1"

const BetaResponsesClientEventResponseCreateModelO1\_2024\_12\_17 BetaResponsesClientEventResponseCreateModel = "o1-2024-12-17"

const BetaResponsesClientEventResponseCreateModelO1Preview BetaResponsesClientEventResponseCreateModel = "o1-preview"

const BetaResponsesClientEventResponseCreateModelO1Preview2024\_09\_12 BetaResponsesClientEventResponseCreateModel = "o1-preview-2024-09-12"

const BetaResponsesClientEventResponseCreateModelO1Mini BetaResponsesClientEventResponseCreateModel = "o1-mini"

const BetaResponsesClientEventResponseCreateModelO1Mini2024\_09\_12 BetaResponsesClientEventResponseCreateModel = "o1-mini-2024-09-12"

const BetaResponsesClientEventResponseCreateModelGPT4o BetaResponsesClientEventResponseCreateModel = "gpt-4o"

const BetaResponsesClientEventResponseCreateModelGPT4o2024\_11\_20 BetaResponsesClientEventResponseCreateModel = "gpt-4o-2024-11-20"

const BetaResponsesClientEventResponseCreateModelGPT4o2024\_08\_06 BetaResponsesClientEventResponseCreateModel = "gpt-4o-2024-08-06"

const BetaResponsesClientEventResponseCreateModelGPT4o2024\_05\_13 BetaResponsesClientEventResponseCreateModel = "gpt-4o-2024-05-13"

const BetaResponsesClientEventResponseCreateModelGPT4oAudioPreview BetaResponsesClientEventResponseCreateModel = "gpt-4o-audio-preview"

const BetaResponsesClientEventResponseCreateModelGPT4oAudioPreview2024\_10\_01 BetaResponsesClientEventResponseCreateModel = "gpt-4o-audio-preview-2024-10-01"

const BetaResponsesClientEventResponseCreateModelGPT4oAudioPreview2024\_12\_17 BetaResponsesClientEventResponseCreateModel = "gpt-4o-audio-preview-2024-12-17"

const BetaResponsesClientEventResponseCreateModelGPT4oAudioPreview2025\_06\_03 BetaResponsesClientEventResponseCreateModel = "gpt-4o-audio-preview-2025-06-03"

const BetaResponsesClientEventResponseCreateModelGPT4oMiniAudioPreview BetaResponsesClientEventResponseCreateModel = "gpt-4o-mini-audio-preview"

const BetaResponsesClientEventResponseCreateModelGPT4oMiniAudioPreview2024\_12\_17 BetaResponsesClientEventResponseCreateModel = "gpt-4o-mini-audio-preview-2024-12-17"

const BetaResponsesClientEventResponseCreateModelGPT4oSearchPreview BetaResponsesClientEventResponseCreateModel = "gpt-4o-search-preview"

const BetaResponsesClientEventResponseCreateModelGPT4oMiniSearchPreview BetaResponsesClientEventResponseCreateModel = "gpt-4o-mini-search-preview"

const BetaResponsesClientEventResponseCreateModelGPT4oSearchPreview2025\_03\_11 BetaResponsesClientEventResponseCreateModel = "gpt-4o-search-preview-2025-03-11"

const BetaResponsesClientEventResponseCreateModelGPT4oMiniSearchPreview2025\_03\_11 BetaResponsesClientEventResponseCreateModel = "gpt-4o-mini-search-preview-2025-03-11"

const BetaResponsesClientEventResponseCreateModelChatgpt4oLatest BetaResponsesClientEventResponseCreateModel = "chatgpt-4o-latest"

const BetaResponsesClientEventResponseCreateModelCodexMiniLatest BetaResponsesClientEventResponseCreateModel = "codex-mini-latest"

const BetaResponsesClientEventResponseCreateModelGPT4oMini BetaResponsesClientEventResponseCreateModel = "gpt-4o-mini"

const BetaResponsesClientEventResponseCreateModelGPT4oMini2024\_07\_18 BetaResponsesClientEventResponseCreateModel = "gpt-4o-mini-2024-07-18"

const BetaResponsesClientEventResponseCreateModelGPT4Turbo BetaResponsesClientEventResponseCreateModel = "gpt-4-turbo"

const BetaResponsesClientEventResponseCreateModelGPT4Turbo2024\_04\_09 BetaResponsesClientEventResponseCreateModel = "gpt-4-turbo-2024-04-09"

const BetaResponsesClientEventResponseCreateModelGPT4\_0125Preview BetaResponsesClientEventResponseCreateModel = "gpt-4-0125-preview"

const BetaResponsesClientEventResponseCreateModelGPT4TurboPreview BetaResponsesClientEventResponseCreateModel = "gpt-4-turbo-preview"

const BetaResponsesClientEventResponseCreateModelGPT4\_1106Preview BetaResponsesClientEventResponseCreateModel = "gpt-4-1106-preview"

const BetaResponsesClientEventResponseCreateModelGPT4VisionPreview BetaResponsesClientEventResponseCreateModel = "gpt-4-vision-preview"

const BetaResponsesClientEventResponseCreateModelGPT4 BetaResponsesClientEventResponseCreateModel = "gpt-4"

const BetaResponsesClientEventResponseCreateModelGPT4\_0314 BetaResponsesClientEventResponseCreateModel = "gpt-4-0314"

const BetaResponsesClientEventResponseCreateModelGPT4\_0613 BetaResponsesClientEventResponseCreateModel = "gpt-4-0613"

const BetaResponsesClientEventResponseCreateModelGPT4\_32k BetaResponsesClientEventResponseCreateModel = "gpt-4-32k"

const BetaResponsesClientEventResponseCreateModelGPT4\_32k0314 BetaResponsesClientEventResponseCreateModel = "gpt-4-32k-0314"

const BetaResponsesClientEventResponseCreateModelGPT4\_32k0613 BetaResponsesClientEventResponseCreateModel = "gpt-4-32k-0613"

const BetaResponsesClientEventResponseCreateModelGPT3\_5Turbo BetaResponsesClientEventResponseCreateModel = "gpt-3.5-turbo"

const BetaResponsesClientEventResponseCreateModelGPT3\_5Turbo16k BetaResponsesClientEventResponseCreateModel = "gpt-3.5-turbo-16k"

const BetaResponsesClientEventResponseCreateModelGPT3\_5Turbo0301 BetaResponsesClientEventResponseCreateModel = "gpt-3.5-turbo-0301"

const BetaResponsesClientEventResponseCreateModelGPT3\_5Turbo0613 BetaResponsesClientEventResponseCreateModel = "gpt-3.5-turbo-0613"

const BetaResponsesClientEventResponseCreateModelGPT3\_5Turbo1106 BetaResponsesClientEventResponseCreateModel = "gpt-3.5-turbo-1106"

const BetaResponsesClientEventResponseCreateModelGPT3\_5Turbo0125 BetaResponsesClientEventResponseCreateModel = "gpt-3.5-turbo-0125"

const BetaResponsesClientEventResponseCreateModelGPT3\_5Turbo16k0613 BetaResponsesClientEventResponseCreateModel = "gpt-3.5-turbo-16k-0613"

const BetaResponsesClientEventResponseCreateModelO1Pro BetaResponsesClientEventResponseCreateModel = "o1-pro"

const BetaResponsesClientEventResponseCreateModelO1Pro2025\_03\_19 BetaResponsesClientEventResponseCreateModel = "o1-pro-2025-03-19"

const BetaResponsesClientEventResponseCreateModelO3Pro BetaResponsesClientEventResponseCreateModel = "o3-pro"

const BetaResponsesClientEventResponseCreateModelO3Pro2025\_06\_10 BetaResponsesClientEventResponseCreateModel = "o3-pro-2025-06-10"

const BetaResponsesClientEventResponseCreateModelO3DeepResearch BetaResponsesClientEventResponseCreateModel = "o3-deep-research"

const BetaResponsesClientEventResponseCreateModelO3DeepResearch2025\_06\_26 BetaResponsesClientEventResponseCreateModel = "o3-deep-research-2025-06-26"

const BetaResponsesClientEventResponseCreateModelO4MiniDeepResearch BetaResponsesClientEventResponseCreateModel = "o4-mini-deep-research"

const BetaResponsesClientEventResponseCreateModelO4MiniDeepResearch2025\_06\_26 BetaResponsesClientEventResponseCreateModel = "o4-mini-deep-research-2025-06-26"

const BetaResponsesClientEventResponseCreateModelComputerUsePreview BetaResponsesClientEventResponseCreateModel = "computer-use-preview"

const BetaResponsesClientEventResponseCreateModelComputerUsePreview2025\_03\_11 BetaResponsesClientEventResponseCreateModel = "computer-use-preview-2025-03-11"

const BetaResponsesClientEventResponseCreateModelGPT5Codex BetaResponsesClientEventResponseCreateModel = "gpt-5-codex"

const BetaResponsesClientEventResponseCreateModelGPT5Pro BetaResponsesClientEventResponseCreateModel = "gpt-5-pro"

const BetaResponsesClientEventResponseCreateModelGPT5Pro2025\_10\_06 BetaResponsesClientEventResponseCreateModel = "gpt-5-pro-2025-10-06"

const BetaResponsesClientEventResponseCreateModelGPT5\_1CodexMax BetaResponsesClientEventResponseCreateModel = "gpt-5.1-codex-max"

string

Moderation BetaResponsesClientEventResponseCreateModerationOptional

Configuration for running moderation on the input and output of this response.

Model string

The moderation model to use for moderated completions, e.g. ‘omni-moderation-latest’.

Policy BetaResponsesClientEventResponseCreateModerationPolicyOptional

The policy to apply to moderated response input and output.

Input BetaResponsesClientEventResponseCreateModerationPolicyInputOptional

The moderation policy for the response input.

Mode string

const BetaResponsesClientEventResponseCreateModerationPolicyInputModeScore BetaResponsesClientEventResponseCreateModerationPolicyInputMode = "score"

const BetaResponsesClientEventResponseCreateModerationPolicyInputModeBlock BetaResponsesClientEventResponseCreateModerationPolicyInputMode = "block"

Output BetaResponsesClientEventResponseCreateModerationPolicyOutputOptional

The moderation policy for the response output.

Mode string

const BetaResponsesClientEventResponseCreateModerationPolicyOutputModeScore BetaResponsesClientEventResponseCreateModerationPolicyOutputMode = "score"

const BetaResponsesClientEventResponseCreateModerationPolicyOutputModeBlock BetaResponsesClientEventResponseCreateModerationPolicyOutputMode = "block"

MultiAgent BetaResponsesClientEventResponseCreateMultiAgentOptional

Configuration for server-hosted multi-agent execution.

Enabled bool

Whether to enable server-hosted multi-agent execution for this response.

MaxConcurrentSubagents int64Optional

`max_concurrent_subagents` sets the maximum number of subagents that can be active simultaneously across the entire agent tree. It includes all descendants—children, grandchildren, and deeper subagents—but excludes the root agent.
The API does not impose a fixed upper bound on this setting. The default is `3`, which is recommended for most workloads. Multi-agent runs also have no fixed limit on tree depth or the total number of subagents created during a run.

minimum1

ParallelToolCalls boolOptional

Whether to allow the model to run tool calls in parallel.

PreviousResponseID stringOptional

The unique ID of the previous response to the model. Use this to
create multi-turn conversations. Learn more about
[conversation state](https://platform.openai.com/docs/guides/conversation-state). Cannot be used in conjunction with `conversation`.

Prompt [BetaResponsePrompt](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_prompt%20%3E%20(schema))Optional

Reference to a prompt template and its variables.
[Learn more](https://platform.openai.com/docs/guides/text?api-mode=responses#reusable-prompts).

PromptCacheKey stringOptional

Used by OpenAI to cache responses for similar requests to optimize your cache hit rates. Replaces the `user` field. [Learn more](https://platform.openai.com/docs/guides/prompt-caching).

PromptCacheOptions BetaResponsesClientEventResponseCreatePromptCacheOptionsOptional

Options for prompt caching. Supported for `gpt-5.6` and later models. By default, OpenAI automatically chooses one implicit cache breakpoint. You can add explicit breakpoints to content blocks with `prompt_cache_breakpoint`. Each request can write up to four breakpoints. For cache matching, OpenAI considers up to the latest 80 breakpoints in the conversation, without a content-block lookback limit. Set `mode` to `explicit` to disable the implicit breakpoint. The `ttl` defaults to `30m`, which is currently the only supported value. See the [prompt caching guide](https://platform.openai.com/docs/guides/prompt-caching) for current details.

Mode stringOptional

Controls whether OpenAI automatically creates an implicit cache breakpoint. Defaults to `implicit`. With `implicit`, OpenAI creates one implicit breakpoint and writes up to the latest three explicit breakpoints in the request. With `explicit`, OpenAI does not create an implicit breakpoint and writes up to the latest four explicit breakpoints. If there are no explicit breakpoints, the request does not use prompt caching.

const BetaResponsesClientEventResponseCreatePromptCacheOptionsModeImplicit BetaResponsesClientEventResponseCreatePromptCacheOptionsMode = "implicit"

const BetaResponsesClientEventResponseCreatePromptCacheOptionsModeExplicit BetaResponsesClientEventResponseCreatePromptCacheOptionsMode = "explicit"

Ttl stringOptional

The minimum lifetime applied to every implicit and explicit cache breakpoint written by the request. Defaults to `30m`, which is currently the only supported value. The backend may retain cache entries for longer.

DeprecatedPromptCacheRetention stringOptional

Deprecated. Use `prompt_cache_options.ttl` instead.

The retention policy for the prompt cache. Set to `24h` to enable extended prompt caching, which keeps cached prefixes active for longer, up to a maximum of 24 hours. [Learn more](https://platform.openai.com/docs/guides/prompt-caching#prompt-cache-retention).
This field expresses a maximum retention policy, while
`prompt_cache_options.ttl` expresses a minimum cache lifetime. The two
fields are independent and do not interact.
For `gpt-5.5`, `gpt-5.5-pro`, and future models, only `24h` is supported.

For older models that support both `in_memory` and `24h`, the default depends on your organization’s data retention policy:

* Organizations without ZDR enabled default to `24h`.
* Organizations with ZDR enabled default to `in_memory` when `prompt_cache_retention` is not specified.

const BetaResponsesClientEventResponseCreatePromptCacheRetentionInMemory BetaResponsesClientEventResponseCreatePromptCacheRetention = "in\_memory"

const BetaResponsesClientEventResponseCreatePromptCacheRetention24h BetaResponsesClientEventResponseCreatePromptCacheRetention = "24h"

Reasoning BetaResponsesClientEventResponseCreateReasoningOptional

**gpt-5 and o-series models only**

Configuration options for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).

Context stringOptional

Controls which reasoning items are rendered back to the model on later turns.
When returned on a response, this is the effective reasoning context mode
used for the response.

const BetaResponsesClientEventResponseCreateReasoningContextAuto BetaResponsesClientEventResponseCreateReasoningContext = "auto"

const BetaResponsesClientEventResponseCreateReasoningContextCurrentTurn BetaResponsesClientEventResponseCreateReasoningContext = "current\_turn"

const BetaResponsesClientEventResponseCreateReasoningContextAllTurns BetaResponsesClientEventResponseCreateReasoningContext = "all\_turns"

Effort stringOptional

Constrains effort on reasoning for reasoning models. Currently supported
values are `none`, `minimal`, `low`, `medium`, `high`, `xhigh`, and `max`.
Reducing reasoning effort can result in faster responses and fewer tokens
used on reasoning in a response. Not all reasoning models support every
value. See the
[reasoning guide](https://platform.openai.com/docs/guides/reasoning)
for model-specific support.

const BetaResponsesClientEventResponseCreateReasoningEffortNone BetaResponsesClientEventResponseCreateReasoningEffort = "none"

const BetaResponsesClientEventResponseCreateReasoningEffortMinimal BetaResponsesClientEventResponseCreateReasoningEffort = "minimal"

const BetaResponsesClientEventResponseCreateReasoningEffortLow BetaResponsesClientEventResponseCreateReasoningEffort = "low"

const BetaResponsesClientEventResponseCreateReasoningEffortMedium BetaResponsesClientEventResponseCreateReasoningEffort = "medium"

const BetaResponsesClientEventResponseCreateReasoningEffortHigh BetaResponsesClientEventResponseCreateReasoningEffort = "high"

const BetaResponsesClientEventResponseCreateReasoningEffortXhigh BetaResponsesClientEventResponseCreateReasoningEffort = "xhigh"

const BetaResponsesClientEventResponseCreateReasoningEffortMax BetaResponsesClientEventResponseCreateReasoningEffort = "max"

DeprecatedGenerateSummary stringOptional

**Deprecated:** use `summary` instead.

A summary of the reasoning performed by the model. This can be
useful for debugging and understanding the model’s reasoning process.
One of `auto`, `concise`, or `detailed`.

const BetaResponsesClientEventResponseCreateReasoningGenerateSummaryAuto BetaResponsesClientEventResponseCreateReasoningGenerateSummary = "auto"

const BetaResponsesClientEventResponseCreateReasoningGenerateSummaryConcise BetaResponsesClientEventResponseCreateReasoningGenerateSummary = "concise"

const BetaResponsesClientEventResponseCreateReasoningGenerateSummaryDetailed BetaResponsesClientEventResponseCreateReasoningGenerateSummary = "detailed"

Mode stringOptional

Controls the reasoning execution mode for the request.

When returned on a response, this is the effective execution mode.

string

string

const BetaResponsesClientEventResponseCreateReasoningModeStandard BetaResponsesClientEventResponseCreateReasoningMode = "standard"

const BetaResponsesClientEventResponseCreateReasoningModePro BetaResponsesClientEventResponseCreateReasoningMode = "pro"

Summary stringOptional

A summary of the reasoning performed by the model. This can be
useful for debugging and understanding the model’s reasoning process.
One of `auto`, `concise`, or `detailed`.

`concise` is supported for `computer-use-preview` models and all reasoning models after `gpt-5`.

const BetaResponsesClientEventResponseCreateReasoningSummaryAuto BetaResponsesClientEventResponseCreateReasoningSummary = "auto"

const BetaResponsesClientEventResponseCreateReasoningSummaryConcise BetaResponsesClientEventResponseCreateReasoningSummary = "concise"

const BetaResponsesClientEventResponseCreateReasoningSummaryDetailed BetaResponsesClientEventResponseCreateReasoningSummary = "detailed"

SafetyIdentifier stringOptional

A stable identifier used to help detect users of your application that may be violating OpenAI’s usage policies.
The IDs should be a string that uniquely identifies each user, with a maximum length of 64 characters. We recommend hashing their username or email address, in order to avoid sending us any identifying information. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).

maxLength64

ServiceTier stringOptional

Specifies the processing type used for serving the request.

* If set to ‘auto’, then the request will be processed with the service tier configured in the Project settings. Unless otherwise configured, the Project will use ‘default’.
* If set to ‘default’, then the request will be processed with the standard pricing and performance for the selected model.
* If set to ‘[flex](https://platform.openai.com/docs/guides/flex-processing)’ or ‘[priority](https://openai.com/api-priority-processing/)’, then the request will be processed with the corresponding service tier.
* When not set, the default behavior is ‘auto’.

When the `service_tier` parameter is set, the response body will include the `service_tier` value based on the processing mode actually used to serve the request. This response value may be different from the value set in the parameter.

const BetaResponsesClientEventResponseCreateServiceTierAuto BetaResponsesClientEventResponseCreateServiceTier = "auto"

const BetaResponsesClientEventResponseCreateServiceTierDefault BetaResponsesClientEventResponseCreateServiceTier = "default"

const BetaResponsesClientEventResponseCreateServiceTierFlex BetaResponsesClientEventResponseCreateServiceTier = "flex"

const BetaResponsesClientEventResponseCreateServiceTierScale BetaResponsesClientEventResponseCreateServiceTier = "scale"

const BetaResponsesClientEventResponseCreateServiceTierPriority BetaResponsesClientEventResponseCreateServiceTier = "priority"

Store boolOptional

Whether to store the generated model response for later retrieval via
API.

Stream boolOptional

If set to true, the model response data will be streamed to the client
as it is generated using [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format).
See the [Streaming section below](https://platform.openai.com/docs/api-reference/responses-streaming)
for more information.

StreamOptions BetaResponsesClientEventResponseCreateStreamOptionsOptional

Options for streaming responses. Only set this when you set `stream: true`.

IncludeObfuscation boolOptional

When true, stream obfuscation will be enabled. Stream obfuscation adds
random characters to an `obfuscation` field on streaming delta events to
normalize payload sizes as a mitigation to certain side-channel attacks.
These obfuscation fields are included by default, but add a small amount
of overhead to the data stream. You can set `include_obfuscation` to
false to optimize for bandwidth if you trust the network links between
your application and the OpenAI API.

Temperature float64Optional

What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.
We generally recommend altering this or `top_p` but not both.

minimum0

maximum2

Text [BetaResponseTextConfig](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_text_config%20%3E%20(schema))Optional

Configuration options for a text response from the model. Can be plain
text or structured JSON data. Learn more:

* [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
* [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

ToolChoice BetaResponsesClientEventResponseCreateToolChoiceUnionOptional

How the model should select which tool (or tools) to use when generating
a response. See the `tools` parameter to see how to specify which tools
the model can call.

type BetaToolChoiceOptions string

Controls which (if any) tool is called by the model.

`none` means the model will not call any tool and instead generates a message.

`auto` means the model can pick between generating a message or calling one or
more tools.

`required` means the model must call one or more tools.

const BetaToolChoiceOptionsNone [BetaToolChoiceOptions](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool_choice_options%20%3E%20(schema)) = "none"

const BetaToolChoiceOptionsAuto [BetaToolChoiceOptions](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool_choice_options%20%3E%20(schema)) = "auto"

const BetaToolChoiceOptionsRequired [BetaToolChoiceOptions](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool_choice_options%20%3E%20(schema)) = "required"

type BetaToolChoiceAllowed struct{…}

Constrains the tools available to the model to a pre-defined set.

Mode BetaToolChoiceAllowedMode

Constrains the tools available to the model to a pre-defined set.

`auto` allows the model to pick from among the allowed tools and generate a
message.

`required` requires the model to call one or more of the allowed tools.

const BetaToolChoiceAllowedModeAuto BetaToolChoiceAllowedMode = "auto"

const BetaToolChoiceAllowedModeRequired BetaToolChoiceAllowedMode = "required"

Tools []map[string, any]

A list of tool definitions that the model should be allowed to call.

For the Responses API, the list of tool definitions might look like:

  { "type": "function", "name": "get_weather" },
  { "type": "mcp", "server_label": "deepwiki" },
  { "type": "image_generation" }

Type AllowedTools

Allowed tool configuration type. Always `allowed_tools`.

type BetaToolChoiceTypes struct{…}

Indicates that the model should use a built-in tool to generate a response.
[Learn more about built-in tools](https://platform.openai.com/docs/guides/tools).

Type BetaToolChoiceTypesType

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

const BetaToolChoiceTypesTypeFileSearch BetaToolChoiceTypesType = "file\_search"

const BetaToolChoiceTypesTypeWebSearchPreview BetaToolChoiceTypesType = "web\_search\_preview"

const BetaToolChoiceTypesTypeComputer BetaToolChoiceTypesType = "computer"

const BetaToolChoiceTypesTypeComputerUsePreview BetaToolChoiceTypesType = "computer\_use\_preview"

const BetaToolChoiceTypesTypeComputerUse BetaToolChoiceTypesType = "computer\_use"

const BetaToolChoiceTypesTypeWebSearchPreview2025\_03\_11 BetaToolChoiceTypesType = "web\_search\_preview\_2025\_03\_11"

const BetaToolChoiceTypesTypeImageGeneration BetaToolChoiceTypesType = "image\_generation"

const BetaToolChoiceTypesTypeCodeInterpreter BetaToolChoiceTypesType = "code\_interpreter"

type BetaToolChoiceFunction struct{…}

Use this option to force the model to call a specific function.

Name string

Type Function

For function calling, the type is always `function`.

type BetaToolChoiceMcp struct{…}

Use this option to force the model to call a specific tool on a remote MCP server.

ServerLabel string

The label of the MCP server to use.

Type Mcp

For MCP tools, the type is always `mcp`.

Name stringOptional

The name of the tool to call on the server.

type BetaToolChoiceCustom struct{…}

Use this option to force the model to call a specific custom tool.

Name string

The name of the custom tool to call.

Type Custom

For custom tool calling, the type is always `custom`.

BetaResponsesClientEventResponseCreateToolChoiceBetaSpecificProgrammaticToolCallingParam

Type ProgrammaticToolCalling

The tool to call. Always `programmatic_tool_calling`.

type BetaToolChoiceApplyPatch struct{…}

Forces the model to call the apply\_patch tool when executing a tool call.

Type ApplyPatch

The tool to call. Always `apply_patch`.

type BetaToolChoiceShell struct{…}

Forces the model to call the shell tool when a tool call is required.

Type Shell

The tool to call. Always `shell`.

Tools [][BetaToolUnion](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))Optional

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

TopLogprobs int64Optional

An integer between 0 and 20 specifying the maximum number of most likely
tokens to return at each token position, each with an associated log
probability. In some cases, the number of returned tokens may be fewer than
requested.

minimum0

maximum20

TopP float64Optional

An alternative to sampling with temperature, called nucleus sampling,
where the model considers the results of the tokens with top\_p probability
mass. So 0.1 means only the tokens comprising the top 10% probability mass
are considered.

We generally recommend altering this or `temperature` but not both.

minimum0

maximum1

DeprecatedTruncation stringOptional

The truncation strategy to use for the model response.

* `auto`: If the input to this Response exceeds
  the model’s context window size, the model will truncate the
  response to fit the context window by dropping items from the beginning of the conversation.
* `disabled` (default): If the input size will exceed the context window
  size for a model, the request will fail with a 400 error.

const BetaResponsesClientEventResponseCreateTruncationAuto BetaResponsesClientEventResponseCreateTruncation = "auto"

const BetaResponsesClientEventResponseCreateTruncationDisabled BetaResponsesClientEventResponseCreateTruncation = "disabled"

DeprecatedUser stringOptional

This field is being replaced by `safety_identifier` and `prompt_cache_key`. Use `prompt_cache_key` instead to maintain caching optimizations.
A stable identifier for your end-users.
Used to boost cache hit rates by better bucketing similar requests and to help OpenAI detect and prevent abuse. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).

type BetaResponseInjectEvent struct{…}

Injects input items into an active response over a WebSocket connection.
The items are validated and committed atomically. Currently, the server
accepts client-owned tool outputs that resume a waiting agent.

Input [][BetaResponseInputItemUnion](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_item%20%3E%20(schema))

Input items to inject into the active response.

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

Actions [BetaComputerActionList](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_computer_action_list%20%3E%20(schema))Optional

Agent BetaResponseComputerToolCallAgentOptional

AgentName string

type BetaResponseInputItemComputerCallOutput struct{…}

The output of a computer tool call.

CallID string

maxLength64

minLength1

Output [BetaResponseComputerToolCallOutputScreenshot](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_computer_tool_call_output_screenshot%20%3E%20(schema))

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

ResponseID string

The ID of the active response that should receive the input.

Type ResponseInject

The event discriminator. Always `response.inject`.

type BetaResponsesServerEventUnion interface{…}

Server events emitted by the Responses WebSocket server.

type BetaResponseAudioDeltaEvent struct{…}

Emitted when there is a partial audio response.

Delta string

A chunk of Base64 encoded response audio bytes.

SequenceNumber int64

A sequence number for this chunk of the stream response.

Type ResponseAudioDelta

The type of the event. Always `response.audio.delta`.

Agent BetaResponseAudioDeltaEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseAudioDoneEvent struct{…}

Emitted when the audio response is complete.

SequenceNumber int64

The sequence number of the delta.

Type ResponseAudioDone

The type of the event. Always `response.audio.done`.

Agent BetaResponseAudioDoneEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseAudioTranscriptDeltaEvent struct{…}

Emitted when there is a partial transcript of audio.

Delta string

The partial transcript of the audio response.

SequenceNumber int64

The sequence number of this event.

Type ResponseAudioTranscriptDelta

The type of the event. Always `response.audio.transcript.delta`.

Agent BetaResponseAudioTranscriptDeltaEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseAudioTranscriptDoneEvent struct{…}

Emitted when the full audio transcript is completed.

SequenceNumber int64

The sequence number of this event.

Type ResponseAudioTranscriptDone

The type of the event. Always `response.audio.transcript.done`.

Agent BetaResponseAudioTranscriptDoneEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseCodeInterpreterCallCodeDeltaEvent struct{…}

Emitted when a partial code snippet is streamed by the code interpreter.

Delta string

The partial code snippet being streamed by the code interpreter.

ItemID string

The unique identifier of the code interpreter tool call item.

OutputIndex int64

The index of the output item in the response for which the code is being streamed.

SequenceNumber int64

The sequence number of this event, used to order streaming events.

Type ResponseCodeInterpreterCallCodeDelta

The type of the event. Always `response.code_interpreter_call_code.delta`.

Agent BetaResponseCodeInterpreterCallCodeDeltaEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseCodeInterpreterCallCodeDoneEvent struct{…}

Emitted when the code snippet is finalized by the code interpreter.

Code string

The final code snippet output by the code interpreter.

ItemID string

The unique identifier of the code interpreter tool call item.

OutputIndex int64

The index of the output item in the response for which the code is finalized.

SequenceNumber int64

The sequence number of this event, used to order streaming events.

Type ResponseCodeInterpreterCallCodeDone

The type of the event. Always `response.code_interpreter_call_code.done`.

Agent BetaResponseCodeInterpreterCallCodeDoneEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseCodeInterpreterCallCompletedEvent struct{…}

Emitted when the code interpreter call is completed.

ItemID string

The unique identifier of the code interpreter tool call item.

OutputIndex int64

The index of the output item in the response for which the code interpreter call is completed.

SequenceNumber int64

The sequence number of this event, used to order streaming events.

Type ResponseCodeInterpreterCallCompleted

The type of the event. Always `response.code_interpreter_call.completed`.

Agent BetaResponseCodeInterpreterCallCompletedEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseCodeInterpreterCallInProgressEvent struct{…}

Emitted when a code interpreter call is in progress.

ItemID string

The unique identifier of the code interpreter tool call item.

OutputIndex int64

The index of the output item in the response for which the code interpreter call is in progress.

SequenceNumber int64

The sequence number of this event, used to order streaming events.

Type ResponseCodeInterpreterCallInProgress

The type of the event. Always `response.code_interpreter_call.in_progress`.

Agent BetaResponseCodeInterpreterCallInProgressEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseCodeInterpreterCallInterpretingEvent struct{…}

Emitted when the code interpreter is actively interpreting the code snippet.

ItemID string

The unique identifier of the code interpreter tool call item.

OutputIndex int64

The index of the output item in the response for which the code interpreter is interpreting code.

SequenceNumber int64

The sequence number of this event, used to order streaming events.

Type ResponseCodeInterpreterCallInterpreting

The type of the event. Always `response.code_interpreter_call.interpreting`.

Agent BetaResponseCodeInterpreterCallInterpretingEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseCompletedEvent struct{…}

Emitted when the model response is complete.

Response [BetaResponse](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema))

Properties of the completed response.

SequenceNumber int64

The sequence number for this event.

Type ResponseCompleted

The type of the event. Always `response.completed`.

Agent BetaResponseCompletedEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseContentPartAddedEvent struct{…}

Emitted when a new content part is added.

ContentIndex int64

The index of the content part that was added.

ItemID string

The ID of the output item that the content part was added to.

OutputIndex int64

The index of the output item that the content part was added to.

Part BetaResponseContentPartAddedEventPartUnion

The content part that was added.

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

type BetaResponseContentPartAddedEventPartReasoningText struct{…}

Text string

Type ReasoningText

SequenceNumber int64

The sequence number of this event.

Type ResponseContentPartAdded

The type of the event. Always `response.content_part.added`.

Agent BetaResponseContentPartAddedEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseContentPartDoneEvent struct{…}

Emitted when a content part is done.

ContentIndex int64

The index of the content part that is done.

ItemID string

The ID of the output item that the content part was added to.

OutputIndex int64

The index of the output item that the content part was added to.

Part BetaResponseContentPartDoneEventPartUnion

The content part that is done.

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

type BetaResponseContentPartDoneEventPartReasoningText struct{…}

Text string

Type ReasoningText

SequenceNumber int64

The sequence number of this event.

Type ResponseContentPartDone

The type of the event. Always `response.content_part.done`.

Agent BetaResponseContentPartDoneEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseCreatedEvent struct{…}

An event that is emitted when a response is created.

Response [BetaResponse](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema))

The response that was created.

SequenceNumber int64

The sequence number for this event.

Type ResponseCreated

The type of the event. Always `response.created`.

Agent BetaResponseCreatedEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseErrorEvent struct{…}

Emitted when an error occurs.

Code string

The error code.

Message string

The error message.

Param string

The error parameter.

SequenceNumber int64

The sequence number of this event.

Type Error

The type of the event. Always `error`.

Agent BetaResponseErrorEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseFileSearchCallCompletedEvent struct{…}

Emitted when a file search call is completed (results found).

ItemID string

The ID of the output item that the file search call is initiated.

OutputIndex int64

The index of the output item that the file search call is initiated.

SequenceNumber int64

The sequence number of this event.

Type ResponseFileSearchCallCompleted

The type of the event. Always `response.file_search_call.completed`.

Agent BetaResponseFileSearchCallCompletedEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseFileSearchCallInProgressEvent struct{…}

Emitted when a file search call is initiated.

ItemID string

The ID of the output item that the file search call is initiated.

OutputIndex int64

The index of the output item that the file search call is initiated.

SequenceNumber int64

The sequence number of this event.

Type ResponseFileSearchCallInProgress

The type of the event. Always `response.file_search_call.in_progress`.

Agent BetaResponseFileSearchCallInProgressEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseFileSearchCallSearchingEvent struct{…}

Emitted when a file search is currently searching.

ItemID string

The ID of the output item that the file search call is initiated.

OutputIndex int64

The index of the output item that the file search call is searching.

SequenceNumber int64

The sequence number of this event.

Type ResponseFileSearchCallSearching

The type of the event. Always `response.file_search_call.searching`.

Agent BetaResponseFileSearchCallSearchingEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseFunctionCallArgumentsDeltaEvent struct{…}

Emitted when there is a partial function-call arguments delta.

Delta string

The function-call arguments delta that is added.

ItemID string

The ID of the output item that the function-call arguments delta is added to.

OutputIndex int64

The index of the output item that the function-call arguments delta is added to.

SequenceNumber int64

The sequence number of this event.

Type ResponseFunctionCallArgumentsDelta

The type of the event. Always `response.function_call_arguments.delta`.

Agent BetaResponseFunctionCallArgumentsDeltaEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseFunctionCallArgumentsDoneEvent struct{…}

Emitted when function-call arguments are finalized.

Arguments string

The function-call arguments.

ItemID string

The ID of the item.

Name string

The name of the function that was called.

OutputIndex int64

The index of the output item.

SequenceNumber int64

The sequence number of this event.

Type ResponseFunctionCallArgumentsDone

Agent BetaResponseFunctionCallArgumentsDoneEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseInProgressEvent struct{…}

Emitted when the response is in progress.

Response [BetaResponse](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema))

The response that is in progress.

SequenceNumber int64

The sequence number of this event.

Type ResponseInProgress

The type of the event. Always `response.in_progress`.

Agent BetaResponseInProgressEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseFailedEvent struct{…}

An event that is emitted when a response fails.

Response [BetaResponse](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema))

The response that failed.

SequenceNumber int64

The sequence number of this event.

Type ResponseFailed

The type of the event. Always `response.failed`.

Agent BetaResponseFailedEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseIncompleteEvent struct{…}

An event that is emitted when a response finishes as incomplete.

Response [BetaResponse](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema))

The response that was incomplete.

SequenceNumber int64

The sequence number of this event.

Type ResponseIncomplete

The type of the event. Always `response.incomplete`.

Agent BetaResponseIncompleteEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseOutputItemAddedEvent struct{…}

Emitted when a new output item is added.

Item [BetaResponseOutputItemUnion](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_item%20%3E%20(schema))

The output item that was added.

OutputIndex int64

The index of the output item that was added.

SequenceNumber int64

The sequence number of this event.

Type ResponseOutputItemAdded

The type of the event. Always `response.output_item.added`.

Agent BetaResponseOutputItemAddedEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseOutputItemDoneEvent struct{…}

Emitted when an output item is marked done.

Item [BetaResponseOutputItemUnion](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_item%20%3E%20(schema))

The output item that was marked done.

OutputIndex int64

The index of the output item that was marked done.

SequenceNumber int64

The sequence number of this event.

Type ResponseOutputItemDone

The type of the event. Always `response.output_item.done`.

Agent BetaResponseOutputItemDoneEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseReasoningSummaryPartAddedEvent struct{…}

Emitted when a new reasoning summary part is added.

ItemID string

The ID of the item this summary part is associated with.

OutputIndex int64

The index of the output item this summary part is associated with.

Part BetaResponseReasoningSummaryPartAddedEventPart

The summary part that was added.

Text string

The text of the summary part.

Type SummaryText

The type of the summary part. Always `summary_text`.

SequenceNumber int64

The sequence number of this event.

SummaryIndex int64

The index of the summary part within the reasoning summary.

Type ResponseReasoningSummaryPartAdded

The type of the event. Always `response.reasoning_summary_part.added`.

Agent BetaResponseReasoningSummaryPartAddedEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseReasoningSummaryPartDoneEvent struct{…}

Emitted when a reasoning summary part is completed.

ItemID string

The ID of the item this summary part is associated with.

OutputIndex int64

The index of the output item this summary part is associated with.

Part BetaResponseReasoningSummaryPartDoneEventPart

The completed summary part.

Text string

The text of the summary part.

Type SummaryText

The type of the summary part. Always `summary_text`.

SequenceNumber int64

The sequence number of this event.

SummaryIndex int64

The index of the summary part within the reasoning summary.

Type ResponseReasoningSummaryPartDone

The type of the event. Always `response.reasoning_summary_part.done`.

Agent BetaResponseReasoningSummaryPartDoneEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

Status BetaResponseReasoningSummaryPartDoneEventStatusOptional

The completion status of the summary part. Omitted when the part completed
normally and set to `incomplete` when generation was interrupted.

type BetaResponseReasoningSummaryTextDeltaEvent struct{…}

Emitted when a delta is added to a reasoning summary text.

Delta string

The text delta that was added to the summary.

ItemID string

The ID of the item this summary text delta is associated with.

OutputIndex int64

The index of the output item this summary text delta is associated with.

SequenceNumber int64

The sequence number of this event.

SummaryIndex int64

The index of the summary part within the reasoning summary.

Type ResponseReasoningSummaryTextDelta

The type of the event. Always `response.reasoning_summary_text.delta`.

Agent BetaResponseReasoningSummaryTextDeltaEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseReasoningSummaryTextDoneEvent struct{…}

Emitted when a reasoning summary text is completed.

ItemID string

The ID of the item this summary text is associated with.

OutputIndex int64

The index of the output item this summary text is associated with.

SequenceNumber int64

The sequence number of this event.

SummaryIndex int64

The index of the summary part within the reasoning summary.

Text string

The full text of the completed reasoning summary.

Type ResponseReasoningSummaryTextDone

The type of the event. Always `response.reasoning_summary_text.done`.

Agent BetaResponseReasoningSummaryTextDoneEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseReasoningTextDeltaEvent struct{…}

Emitted when a delta is added to a reasoning text.

ContentIndex int64

The index of the reasoning content part this delta is associated with.

Delta string

The text delta that was added to the reasoning content.

ItemID string

The ID of the item this reasoning text delta is associated with.

OutputIndex int64

The index of the output item this reasoning text delta is associated with.

SequenceNumber int64

The sequence number of this event.

Type ResponseReasoningTextDelta

The type of the event. Always `response.reasoning_text.delta`.

Agent BetaResponseReasoningTextDeltaEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseReasoningTextDoneEvent struct{…}

Emitted when a reasoning text is completed.

ContentIndex int64

The index of the reasoning content part.

ItemID string

The ID of the item this reasoning text is associated with.

OutputIndex int64

The index of the output item this reasoning text is associated with.

SequenceNumber int64

The sequence number of this event.

Text string

The full text of the completed reasoning content.

Type ResponseReasoningTextDone

The type of the event. Always `response.reasoning_text.done`.

Agent BetaResponseReasoningTextDoneEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseRefusalDeltaEvent struct{…}

Emitted when there is a partial refusal text.

ContentIndex int64

The index of the content part that the refusal text is added to.

Delta string

The refusal text that is added.

ItemID string

The ID of the output item that the refusal text is added to.

OutputIndex int64

The index of the output item that the refusal text is added to.

SequenceNumber int64

The sequence number of this event.

Type ResponseRefusalDelta

The type of the event. Always `response.refusal.delta`.

Agent BetaResponseRefusalDeltaEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseRefusalDoneEvent struct{…}

Emitted when refusal text is finalized.

ContentIndex int64

The index of the content part that the refusal text is finalized.

ItemID string

The ID of the output item that the refusal text is finalized.

OutputIndex int64

The index of the output item that the refusal text is finalized.

Refusal string

The refusal text that is finalized.

SequenceNumber int64

The sequence number of this event.

Type ResponseRefusalDone

The type of the event. Always `response.refusal.done`.

Agent BetaResponseRefusalDoneEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseTextDeltaEvent struct{…}

Emitted when there is an additional text delta.

ContentIndex int64

The index of the content part that the text delta was added to.

Delta string

The text delta that was added.

ItemID string

The ID of the output item that the text delta was added to.

Logprobs []BetaResponseTextDeltaEventLogprob

The log probabilities of the tokens in the delta.

Token string

A possible text token.

Logprob float64

The log probability of this token.

TopLogprobs []BetaResponseTextDeltaEventLogprobTopLogprobOptional

The log probabilities of up to 20 of the most likely tokens.

Token stringOptional

A possible text token.

Logprob float64Optional

The log probability of this token.

OutputIndex int64

The index of the output item that the text delta was added to.

SequenceNumber int64

The sequence number for this event.

Type ResponseOutputTextDelta

The type of the event. Always `response.output_text.delta`.

Agent BetaResponseTextDeltaEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseTextDoneEvent struct{…}

Emitted when text content is finalized.

ContentIndex int64

The index of the content part that the text content is finalized.

ItemID string

The ID of the output item that the text content is finalized.

Logprobs []BetaResponseTextDoneEventLogprob

The log probabilities of the tokens in the delta.

Token string

A possible text token.

Logprob float64

The log probability of this token.

TopLogprobs []BetaResponseTextDoneEventLogprobTopLogprobOptional

The log probabilities of up to 20 of the most likely tokens.

Token stringOptional

A possible text token.

Logprob float64Optional

The log probability of this token.

OutputIndex int64

The index of the output item that the text content is finalized.

SequenceNumber int64

The sequence number for this event.

Text string

The text content that is finalized.

Type ResponseOutputTextDone

The type of the event. Always `response.output_text.done`.

Agent BetaResponseTextDoneEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseWebSearchCallCompletedEvent struct{…}

Emitted when a web search call is completed.

ItemID string

Unique ID for the output item associated with the web search call.

OutputIndex int64

The index of the output item that the web search call is associated with.

SequenceNumber int64

The sequence number of the web search call being processed.

Type ResponseWebSearchCallCompleted

The type of the event. Always `response.web_search_call.completed`.

Agent BetaResponseWebSearchCallCompletedEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseWebSearchCallInProgressEvent struct{…}

Emitted when a web search call is initiated.

ItemID string

Unique ID for the output item associated with the web search call.

OutputIndex int64

The index of the output item that the web search call is associated with.

SequenceNumber int64

The sequence number of the web search call being processed.

Type ResponseWebSearchCallInProgress

The type of the event. Always `response.web_search_call.in_progress`.

Agent BetaResponseWebSearchCallInProgressEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseWebSearchCallSearchingEvent struct{…}

Emitted when a web search call is executing.

ItemID string

Unique ID for the output item associated with the web search call.

OutputIndex int64

The index of the output item that the web search call is associated with.

SequenceNumber int64

The sequence number of the web search call being processed.

Type ResponseWebSearchCallSearching

The type of the event. Always `response.web_search_call.searching`.

Agent BetaResponseWebSearchCallSearchingEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseImageGenCallCompletedEvent struct{…}

Emitted when an image generation tool call has completed and the final image is available.

ItemID string

The unique identifier of the image generation item being processed.

OutputIndex int64

The index of the output item in the response’s output array.

SequenceNumber int64

The sequence number of this event.

Type ResponseImageGenerationCallCompleted

The type of the event. Always ‘response.image\_generation\_call.completed’.

Agent BetaResponseImageGenCallCompletedEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseImageGenCallGeneratingEvent struct{…}

Emitted when an image generation tool call is actively generating an image (intermediate state).

ItemID string

The unique identifier of the image generation item being processed.

OutputIndex int64

The index of the output item in the response’s output array.

SequenceNumber int64

The sequence number of the image generation item being processed.

Type ResponseImageGenerationCallGenerating

The type of the event. Always ‘response.image\_generation\_call.generating’.

Agent BetaResponseImageGenCallGeneratingEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseImageGenCallInProgressEvent struct{…}

Emitted when an image generation tool call is in progress.

ItemID string

The unique identifier of the image generation item being processed.

OutputIndex int64

The index of the output item in the response’s output array.

SequenceNumber int64

The sequence number of the image generation item being processed.

Type ResponseImageGenerationCallInProgress

The type of the event. Always ‘response.image\_generation\_call.in\_progress’.

Agent BetaResponseImageGenCallInProgressEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseImageGenCallPartialImageEvent struct{…}

Emitted when a partial image is available during image generation streaming.

ItemID string

The unique identifier of the image generation item being processed.

OutputIndex int64

The index of the output item in the response’s output array.

PartialImageB64 string

Base64-encoded partial image data, suitable for rendering as an image.

PartialImageIndex int64

0-based index for the partial image (backend is 1-based, but this is 0-based for the user).

SequenceNumber int64

The sequence number of the image generation item being processed.

Type ResponseImageGenerationCallPartialImage

The type of the event. Always ‘response.image\_generation\_call.partial\_image’.

Agent BetaResponseImageGenCallPartialImageEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseMcpCallArgumentsDeltaEvent struct{…}

Emitted when there is a delta (partial update) to the arguments of an MCP tool call.

Delta string

A JSON string containing the partial update to the arguments for the MCP tool call.

ItemID string

The unique identifier of the MCP tool call item being processed.

OutputIndex int64

The index of the output item in the response’s output array.

SequenceNumber int64

The sequence number of this event.

Type ResponseMcpCallArgumentsDelta

The type of the event. Always ‘response.mcp\_call\_arguments.delta’.

Agent BetaResponseMcpCallArgumentsDeltaEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseMcpCallArgumentsDoneEvent struct{…}

Emitted when the arguments for an MCP tool call are finalized.

Arguments string

A JSON string containing the finalized arguments for the MCP tool call.

ItemID string

The unique identifier of the MCP tool call item being processed.

OutputIndex int64

The index of the output item in the response’s output array.

SequenceNumber int64

The sequence number of this event.

Type ResponseMcpCallArgumentsDone

The type of the event. Always ‘response.mcp\_call\_arguments.done’.

Agent BetaResponseMcpCallArgumentsDoneEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseMcpCallCompletedEvent struct{…}

Emitted when an MCP tool call has completed successfully.

ItemID string

The ID of the MCP tool call item that completed.

OutputIndex int64

The index of the output item that completed.

SequenceNumber int64

The sequence number of this event.

Type ResponseMcpCallCompleted

The type of the event. Always ‘response.mcp\_call.completed’.

Agent BetaResponseMcpCallCompletedEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseMcpCallFailedEvent struct{…}

Emitted when an MCP tool call has failed.

ItemID string

The ID of the MCP tool call item that failed.

OutputIndex int64

The index of the output item that failed.

SequenceNumber int64

The sequence number of this event.

Type ResponseMcpCallFailed

The type of the event. Always ‘response.mcp\_call.failed’.

Agent BetaResponseMcpCallFailedEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseMcpCallInProgressEvent struct{…}

Emitted when an MCP tool call is in progress.

ItemID string

The unique identifier of the MCP tool call item being processed.

OutputIndex int64

The index of the output item in the response’s output array.

SequenceNumber int64

The sequence number of this event.

Type ResponseMcpCallInProgress

The type of the event. Always ‘response.mcp\_call.in\_progress’.

Agent BetaResponseMcpCallInProgressEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseMcpListToolsCompletedEvent struct{…}

Emitted when the list of available MCP tools has been successfully retrieved.

ItemID string

The ID of the MCP tool call item that produced this output.

OutputIndex int64

The index of the output item that was processed.

SequenceNumber int64

The sequence number of this event.

Type ResponseMcpListToolsCompleted

The type of the event. Always ‘response.mcp\_list\_tools.completed’.

Agent BetaResponseMcpListToolsCompletedEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseMcpListToolsFailedEvent struct{…}

Emitted when the attempt to list available MCP tools has failed.

ItemID string

The ID of the MCP tool call item that failed.

OutputIndex int64

The index of the output item that failed.

SequenceNumber int64

The sequence number of this event.

Type ResponseMcpListToolsFailed

The type of the event. Always ‘response.mcp\_list\_tools.failed’.

Agent BetaResponseMcpListToolsFailedEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseMcpListToolsInProgressEvent struct{…}

Emitted when the system is in the process of retrieving the list of available MCP tools.

ItemID string

The ID of the MCP tool call item that is being processed.

OutputIndex int64

The index of the output item that is being processed.

SequenceNumber int64

The sequence number of this event.

Type ResponseMcpListToolsInProgress

The type of the event. Always ‘response.mcp\_list\_tools.in\_progress’.

Agent BetaResponseMcpListToolsInProgressEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseOutputTextAnnotationAddedEvent struct{…}

Emitted when an annotation is added to output text content.

Annotation any

The annotation object being added. (See annotation schema for details.)

AnnotationIndex int64

The index of the annotation within the content part.

ContentIndex int64

The index of the content part within the output item.

ItemID string

The unique identifier of the item to which the annotation is being added.

OutputIndex int64

The index of the output item in the response’s output array.

SequenceNumber int64

The sequence number of this event.

Type ResponseOutputTextAnnotationAdded

The type of the event. Always ‘response.output\_text.annotation.added’.

Agent BetaResponseOutputTextAnnotationAddedEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseQueuedEvent struct{…}

Emitted when a response is queued and waiting to be processed.

Response [BetaResponse](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema))

The full response object that is queued.

SequenceNumber int64

The sequence number for this event.

Type ResponseQueued

The type of the event. Always ‘response.queued’.

Agent BetaResponseQueuedEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseCustomToolCallInputDeltaEvent struct{…}

Event representing a delta (partial update) to the input of a custom tool call.

Delta string

The incremental input data (delta) for the custom tool call.

ItemID string

Unique identifier for the API item associated with this event.

OutputIndex int64

The index of the output this delta applies to.

SequenceNumber int64

The sequence number of this event.

Type ResponseCustomToolCallInputDelta

The event type identifier.

Agent BetaResponseCustomToolCallInputDeltaEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseCustomToolCallInputDoneEvent struct{…}

Event indicating that input for a custom tool call is complete.

Input string

The complete input data for the custom tool call.

ItemID string

Unique identifier for the API item associated with this event.

OutputIndex int64

The index of the output this event applies to.

SequenceNumber int64

The sequence number of this event.

Type ResponseCustomToolCallInputDone

The event type identifier.

Agent BetaResponseCustomToolCallInputDoneEventAgentOptional

The agent that owns this multi-agent streaming event.

AgentName string

type BetaResponseInjectCreatedEvent struct{…}

Emitted when all injected input items were validated and committed to the
active response.

ResponseID string

The ID of the response that accepted the input.

SequenceNumber int64

The sequence number for this event.

Type ResponseInjectCreated

The event discriminator. Always `response.inject.created`.

StreamID stringOptional

The multiplexed WebSocket stream that emitted the event. This field is
present only when WebSocket multiplexing is enabled separately.

type BetaResponseInjectFailedEvent struct{…}

Emitted when injected input could not be committed to a response. The event
returns the uncommitted raw input so the client can retry it in another
response when appropriate.

Error BetaResponseInjectFailedEventError

Information about why the input was not committed.

Code string

A machine-readable error code.

const BetaResponseInjectFailedEventErrorCodeResponseAlreadyCompleted BetaResponseInjectFailedEventErrorCode = "response\_already\_completed"

const BetaResponseInjectFailedEventErrorCodeResponseNotFound BetaResponseInjectFailedEventErrorCode = "response\_not\_found"

Message string

A human-readable description of the error.

Input [][BetaResponseInputItemUnion](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_item%20%3E%20(schema))

The raw input items that were not committed.

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

Actions [BetaComputerActionList](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_computer_action_list%20%3E%20(schema))Optional

Agent BetaResponseComputerToolCallAgentOptional

AgentName string

type BetaResponseInputItemComputerCallOutput struct{…}

The output of a computer tool call.

CallID string

maxLength64

minLength1

Output [BetaResponseComputerToolCallOutputScreenshot](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_computer_tool_call_output_screenshot%20%3E%20(schema))

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

ResponseID string

The ID of the response that rejected the input.

SequenceNumber int64

The sequence number for this event.

Type ResponseInjectFailed

The event discriminator. Always `response.inject.failed`.

StreamID stringOptional

The multiplexed WebSocket stream that emitted the event. This field is
present only when WebSocket multiplexing is enabled separately.

type BetaSkillReference struct{…}

SkillID string

maxLength64

minLength1

Type SkillReference

Version stringOptional

type BetaToolUnion interface{…}

A tool that can be used to generate a response.

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

type BetaToolChoiceAllowed struct{…}

Constrains the tools available to the model to a pre-defined set.

Mode BetaToolChoiceAllowedMode

Constrains the tools available to the model to a pre-defined set.

`auto` allows the model to pick from among the allowed tools and generate a
message.

`required` requires the model to call one or more of the allowed tools.

const BetaToolChoiceAllowedModeAuto BetaToolChoiceAllowedMode = "auto"

const BetaToolChoiceAllowedModeRequired BetaToolChoiceAllowedMode = "required"

Tools []map[string, any]

A list of tool definitions that the model should be allowed to call.

For the Responses API, the list of tool definitions might look like:

  { "type": "function", "name": "get_weather" },
  { "type": "mcp", "server_label": "deepwiki" },
  { "type": "image_generation" }

Type AllowedTools

Allowed tool configuration type. Always `allowed_tools`.

type BetaToolChoiceApplyPatch struct{…}

Forces the model to call the apply\_patch tool when executing a tool call.

Type ApplyPatch

The tool to call. Always `apply_patch`.

type BetaToolChoiceCustom struct{…}

Use this option to force the model to call a specific custom tool.

Name string

The name of the custom tool to call.

Type Custom

For custom tool calling, the type is always `custom`.

type BetaToolChoiceFunction struct{…}

Use this option to force the model to call a specific function.

Name string

Type Function

For function calling, the type is always `function`.

type BetaToolChoiceMcp struct{…}

Use this option to force the model to call a specific tool on a remote MCP server.

ServerLabel string

The label of the MCP server to use.

Type Mcp

For MCP tools, the type is always `mcp`.

Name stringOptional

The name of the tool to call on the server.

type BetaToolChoiceOptions string

Controls which (if any) tool is called by the model.

`none` means the model will not call any tool and instead generates a message.

`auto` means the model can pick between generating a message or calling one or
more tools.

`required` means the model must call one or more tools.

const BetaToolChoiceOptionsNone [BetaToolChoiceOptions](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool_choice_options%20%3E%20(schema)) = "none"

const BetaToolChoiceOptionsAuto [BetaToolChoiceOptions](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool_choice_options%20%3E%20(schema)) = "auto"

const BetaToolChoiceOptionsRequired [BetaToolChoiceOptions](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool_choice_options%20%3E%20(schema)) = "required"

type BetaToolChoiceShell struct{…}

Forces the model to call the shell tool when a tool call is required.

Type Shell

The tool to call. Always `shell`.

type BetaToolChoiceTypes struct{…}

Indicates that the model should use a built-in tool to generate a response.
[Learn more about built-in tools](https://platform.openai.com/docs/guides/tools).

Type BetaToolChoiceTypesType

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

const BetaToolChoiceTypesTypeFileSearch BetaToolChoiceTypesType = "file\_search"

const BetaToolChoiceTypesTypeWebSearchPreview BetaToolChoiceTypesType = "web\_search\_preview"

const BetaToolChoiceTypesTypeComputer BetaToolChoiceTypesType = "computer"

const BetaToolChoiceTypesTypeComputerUsePreview BetaToolChoiceTypesType = "computer\_use\_preview"

const BetaToolChoiceTypesTypeComputerUse BetaToolChoiceTypesType = "computer\_use"

const BetaToolChoiceTypesTypeWebSearchPreview2025\_03\_11 BetaToolChoiceTypesType = "web\_search\_preview\_2025\_03\_11"

const BetaToolChoiceTypesTypeImageGeneration BetaToolChoiceTypesType = "image\_generation"

const BetaToolChoiceTypesTypeCodeInterpreter BetaToolChoiceTypesType = "code\_interpreter"

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

#### ResponsesInput Items

##### [List input items](/api/reference/go/resources/beta/subresources/responses/subresources/input_items/methods/list)

client.Beta.Responses.InputItems.List(ctx, responseID, params) (\*CursorPage[[BetaResponseItemUnion](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_item%20%3E%20(schema))], error)

GET/responses/{response\_id}/input\_items

##### ModelsExpand Collapse

type BetaResponseItemList struct{…}

A list of Response items.

Data [][BetaResponseItemUnion](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_item%20%3E%20(schema))

A list of items used to generate this response.

type BetaResponseInputMessageItem struct{…}

ID string

The unique ID of the message input.

Content [BetaResponseInputMessageContentList](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_message_content_list%20%3E%20(schema))

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

Actions [BetaComputerActionList](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_computer_action_list%20%3E%20(schema))Optional

Agent BetaResponseComputerToolCallAgentOptional

AgentName string

type BetaResponseComputerToolCallOutputItem struct{…}

ID string

The unique ID of the computer call tool output.

CallID string

Output [BetaResponseComputerToolCallOutputScreenshot](/api/reference/go/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_computer_tool_call_output_screenshot%20%3E%20(schema))

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

FirstID string

The ID of the first item in the list.

HasMore bool

Whether there are more items available.

LastID string

The ID of the last item in the list.

Object List

The type of object returned, must be `list`.

#### ResponsesInput Tokens

##### [Get input token counts](/api/reference/go/resources/beta/subresources/responses/subresources/input_tokens/methods/count)

client.Beta.Responses.InputTokens.Count(ctx, params) (\*[BetaResponseInputTokenCountResponse](/api/reference/go/resources/beta#(resource)%20beta.responses.input_tokens%20%3E%20(model)%20BetaResponseInputTokenCountResponse%20%3E%20(schema)), error)

POST/responses/input\_tokens
