<!-- source: https://developers.openai.com/api/reference/go/resources/beta/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Beta

#### BetaChatKit

##### ModelsExpand Collapse

type ChatKitWorkflow struct{…}

Workflow metadata and state returned for the session.

ID string

Identifier of the workflow backing the session.

StateVariables map[string, ChatKitWorkflowStateVariableUnion]

State variable key-value pairs applied when invoking the workflow. Defaults to null when no overrides were provided.

One of the following:

string

bool

float64

Tracing ChatKitWorkflowTracing

Tracing settings applied to the workflow.

Enabled bool

Indicates whether tracing is enabled.

Version string

Specific workflow version used for the session. Defaults to null when using the latest deployment.

#### BetaChatKitSessions

##### [Cancel chat session](/api/reference/go/resources/beta/subresources/chatkit/subresources/sessions/methods/cancel)

client.Beta.ChatKit.Sessions.Cancel(ctx, sessionID) (\*[ChatSession](/api/reference/go/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session%20%3E%20(schema)), error)

POST/chatkit/sessions/{session\_id}/cancel

##### [Create ChatKit session](/api/reference/go/resources/beta/subresources/chatkit/subresources/sessions/methods/create)

client.Beta.ChatKit.Sessions.New(ctx, body) (\*[ChatSession](/api/reference/go/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session%20%3E%20(schema)), error)

POST/chatkit/sessions

#### BetaChatKitThreads

##### [List ChatKit thread items](/api/reference/go/resources/beta/subresources/chatkit/subresources/threads/methods/list_items)

client.Beta.ChatKit.Threads.ListItems(ctx, threadID, query) (\*ConversationCursorPage[ChatKitThreadItemListDataUnion], error)

GET/chatkit/threads/{thread\_id}/items

##### [Retrieve ChatKit thread](/api/reference/go/resources/beta/subresources/chatkit/subresources/threads/methods/retrieve)

client.Beta.ChatKit.Threads.Get(ctx, threadID) (\*[ChatKitThread](/api/reference/go/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread%20%3E%20(schema)), error)

GET/chatkit/threads/{thread\_id}

##### [Delete ChatKit thread](/api/reference/go/resources/beta/subresources/chatkit/subresources/threads/methods/delete)

client.Beta.ChatKit.Threads.Delete(ctx, threadID) (\*[BetaChatKitThreadDeleteResponse](/api/reference/go/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20BetaChatKitThreadDeleteResponse%20%3E%20(schema)), error)

DELETE/chatkit/threads/{thread\_id}

##### [List ChatKit threads](/api/reference/go/resources/beta/subresources/chatkit/subresources/threads/methods/list)

client.Beta.ChatKit.Threads.List(ctx, query) (\*ConversationCursorPage[[ChatKitThread](/api/reference/go/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread%20%3E%20(schema))], error)

GET/chatkit/threads

##### ModelsExpand Collapse

type ChatSession struct{…}

Represents a ChatKit session and its resolved configuration.

ID string

Identifier for the ChatKit session.

ChatKitConfiguration [ChatSessionChatKitConfiguration](/api/reference/go/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_chatkit_configuration%20%3E%20(schema))

Resolved ChatKit feature configuration for the session.

ClientSecret string

Ephemeral client secret that authenticates session requests.

ExpiresAt int64

Unix timestamp (in seconds) for when the session expires.

formatunixtime

MaxRequestsPer1Minute int64

Convenience copy of the per-minute request limit.

Object ChatKitSession

Type discriminator that is always `chatkit.session`.

RateLimits [ChatSessionRateLimits](/api/reference/go/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_rate_limits%20%3E%20(schema))

Resolved rate limit values.

Status [ChatSessionStatus](/api/reference/go/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_status%20%3E%20(schema))

Current lifecycle state of the session.

User string

User identifier associated with the session.

Workflow [ChatKitWorkflow](/api/reference/go/resources/beta#(resource)%20beta.chatkit%20%3E%20(model)%20chatkit_workflow%20%3E%20(schema))

Workflow metadata for the session.

type ChatSessionAutomaticThreadTitling struct{…}

Automatic thread title preferences for the session.

Enabled bool

Whether automatic thread titling is enabled.

type ChatSessionChatKitConfiguration struct{…}

ChatKit configuration for the session.

AutomaticThreadTitling [ChatSessionAutomaticThreadTitling](/api/reference/go/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_automatic_thread_titling%20%3E%20(schema))

Automatic thread titling preferences.

FileUpload [ChatSessionFileUpload](/api/reference/go/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_file_upload%20%3E%20(schema))

Upload settings for the session.

History [ChatSessionHistory](/api/reference/go/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_history%20%3E%20(schema))

History retention configuration.

type ChatSessionChatKitConfigurationParamResp struct{…}

Optional per-session configuration settings for ChatKit behavior.

AutomaticThreadTitling ChatSessionChatKitConfigurationParamAutomaticThreadTitlingRespOptional

Configuration for automatic thread titling. When omitted, automatic thread titling is enabled by default.

Enabled boolOptional

Enable automatic thread title generation. Defaults to true.

FileUpload ChatSessionChatKitConfigurationParamFileUploadRespOptional

Configuration for upload enablement and limits. When omitted, uploads are disabled by default (max\_files 10, max\_file\_size 512 MB).

Enabled boolOptional

Enable uploads for this session. Defaults to false.

MaxFileSize int64Optional

Maximum size in megabytes for each uploaded file. Defaults to 512 MB, which is the maximum allowable size.

maximum512

minimum1

MaxFiles int64Optional

Maximum number of files that can be uploaded to the session. Defaults to 10.

minimum1

History ChatSessionChatKitConfigurationParamHistoryRespOptional

Configuration for chat history retention. When omitted, history is enabled by default with no limit on recent\_threads (null).

Enabled boolOptional

Enables chat users to access previous ChatKit threads. Defaults to true.

RecentThreads int64Optional

Number of recent ChatKit threads users have access to. Defaults to unlimited when unset.

minimum1

type ChatSessionExpiresAfterParamResp struct{…}

Controls when the session expires relative to an anchor timestamp.

Anchor CreatedAt

Base timestamp used to calculate expiration. Currently fixed to `created_at`.

Seconds int64

Number of seconds after the anchor when the session expires.

maximum600

minimum1

formatint64

type ChatSessionFileUpload struct{…}

Upload permissions and limits applied to the session.

Enabled bool

Indicates if uploads are enabled for the session.

MaxFileSize int64

Maximum upload size in megabytes.

MaxFiles int64

Maximum number of uploads allowed during the session.

type ChatSessionHistory struct{…}

History retention preferences returned for the session.

Enabled bool

Indicates if chat history is persisted for the session.

RecentThreads int64

Number of prior threads surfaced in history views. Defaults to null when all history is retained.

type ChatSessionRateLimits struct{…}

Active per-minute request limit for the session.

MaxRequestsPer1Minute int64

Maximum allowed requests per one-minute window.

type ChatSessionRateLimitsParamResp struct{…}

Controls request rate limits for the session.

MaxRequestsPer1Minute int64Optional

Maximum number of requests allowed per minute for the session. Defaults to 10.

minimum1

type ChatSessionStatus string

One of the following:

const ChatSessionStatusActive [ChatSessionStatus](/api/reference/go/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_status%20%3E%20(schema)) = "active"

const ChatSessionStatusExpired [ChatSessionStatus](/api/reference/go/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_status%20%3E%20(schema)) = "expired"

const ChatSessionStatusCancelled [ChatSessionStatus](/api/reference/go/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_status%20%3E%20(schema)) = "cancelled"

type ChatSessionWorkflowParamResp struct{…}

Workflow reference and overrides applied to the chat session.

ID string

Identifier for the workflow invoked by the session.

StateVariables map[string, ChatSessionWorkflowParamStateVariableUnionResp]Optional

State variables forwarded to the workflow. Keys may be up to 64 characters, values must be primitive types, and the map defaults to an empty object.

One of the following:

string

bool

float64

Tracing ChatSessionWorkflowParamTracingRespOptional

Optional tracing overrides for the workflow invocation. When omitted, tracing is enabled by default.

Enabled boolOptional

Whether tracing is enabled during the session. Defaults to true.

Version stringOptional

Specific workflow version to run. Defaults to the latest deployed version.

type ChatKitAttachment struct{…}

Attachment metadata included on thread items.

ID string

Identifier for the attachment.

MimeType string

MIME type of the attachment.

Name string

Original display name for the attachment.

PreviewURL string

Preview URL for rendering the attachment inline.

formaturi

Type ChatKitAttachmentType

Attachment discriminator.

One of the following:

const ChatKitAttachmentTypeImage ChatKitAttachmentType = "image"

const ChatKitAttachmentTypeFile ChatKitAttachmentType = "file"

type ChatKitResponseOutputText struct{…}

Assistant response text accompanied by optional annotations.

Annotations []ChatKitResponseOutputTextAnnotationUnion

Ordered list of annotations attached to the response text.

One of the following:

type ChatKitResponseOutputTextAnnotationFile struct{…}

Annotation that references an uploaded file.

Source ChatKitResponseOutputTextAnnotationFileSource

File attachment referenced by the annotation.

Filename string

Filename referenced by the annotation.

Type File

Type discriminator that is always `file`.

Type File

Type discriminator that is always `file` for this annotation.

type ChatKitResponseOutputTextAnnotationURL struct{…}

Annotation that references a URL.

Source ChatKitResponseOutputTextAnnotationURLSource

URL referenced by the annotation.

Type URL

Type discriminator that is always `url`.

URL string

URL referenced by the annotation.

formaturi

Type URL

Type discriminator that is always `url` for this annotation.

Text string

Assistant generated text.

Type OutputText

Type discriminator that is always `output_text`.

type ChatKitThread struct{…}

Represents a ChatKit thread and its current status.

ID string

Identifier of the thread.

CreatedAt int64

Unix timestamp (in seconds) for when the thread was created.

formatunixtime

Object ChatKitThread

Type discriminator that is always `chatkit.thread`.

Status ChatKitThreadStatusUnion

Current status for the thread. Defaults to `active` for newly created threads.

One of the following:

type ChatKitThreadStatusActive struct{…}

Indicates that a thread is active.

Type Active

Status discriminator that is always `active`.

type ChatKitThreadStatusLocked struct{…}

Indicates that a thread is locked and cannot accept new input.

Reason string

Reason that the thread was locked. Defaults to null when no reason is recorded.

Type Locked

Status discriminator that is always `locked`.

type ChatKitThreadStatusClosed struct{…}

Indicates that a thread has been closed.

Reason string

Reason that the thread was closed. Defaults to null when no reason is recorded.

Type Closed

Status discriminator that is always `closed`.

Title string

Optional human-readable title for the thread. Defaults to null when no title has been generated.

User string

Free-form string that identifies your end user who owns the thread.

type ChatKitThreadAssistantMessageItem struct{…}

Assistant-authored message within a thread.

ID string

Identifier of the thread item.

Content [][ChatKitResponseOutputText](/api/reference/go/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_response_output_text%20%3E%20(schema))

Ordered assistant response segments.

Annotations []ChatKitResponseOutputTextAnnotationUnion

Ordered list of annotations attached to the response text.

One of the following:

type ChatKitResponseOutputTextAnnotationFile struct{…}

Annotation that references an uploaded file.

Source ChatKitResponseOutputTextAnnotationFileSource

File attachment referenced by the annotation.

Filename string

Filename referenced by the annotation.

Type File

Type discriminator that is always `file`.

Type File

Type discriminator that is always `file` for this annotation.

type ChatKitResponseOutputTextAnnotationURL struct{…}

Annotation that references a URL.

Source ChatKitResponseOutputTextAnnotationURLSource

URL referenced by the annotation.

Type URL

Type discriminator that is always `url`.

URL string

URL referenced by the annotation.

formaturi

Type URL

Type discriminator that is always `url` for this annotation.

Text string

Assistant generated text.

Type OutputText

Type discriminator that is always `output_text`.

CreatedAt int64

Unix timestamp (in seconds) for when the item was created.

formatunixtime

Object ChatKitThreadItem

Type discriminator that is always `chatkit.thread_item`.

ThreadID string

Identifier of the parent thread.

Type ChatKitAssistantMessage

Type discriminator that is always `chatkit.assistant_message`.

type ChatKitThreadItemList struct{…}

A paginated list of thread items rendered for the ChatKit API.

Data []ChatKitThreadItemListDataUnion

A list of items

One of the following:

type ChatKitThreadUserMessageItem struct{…}

User-authored messages within a thread.

ID string

Identifier of the thread item.

Attachments [][ChatKitAttachment](/api/reference/go/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_attachment%20%3E%20(schema))

Attachments associated with the user message. Defaults to an empty list.

ID string

Identifier for the attachment.

MimeType string

MIME type of the attachment.

Name string

Original display name for the attachment.

PreviewURL string

Preview URL for rendering the attachment inline.

formaturi

Type ChatKitAttachmentType

Attachment discriminator.

One of the following:

const ChatKitAttachmentTypeImage ChatKitAttachmentType = "image"

const ChatKitAttachmentTypeFile ChatKitAttachmentType = "file"

Content []ChatKitThreadUserMessageItemContentUnion

Ordered content elements supplied by the user.

One of the following:

type ChatKitThreadUserMessageItemContentInputText struct{…}

Text block that a user contributed to the thread.

Text string

Plain-text content supplied by the user.

Type InputText

Type discriminator that is always `input_text`.

type ChatKitThreadUserMessageItemContentQuotedText struct{…}

Quoted snippet that the user referenced in their message.

Text string

Quoted text content.

Type QuotedText

Type discriminator that is always `quoted_text`.

CreatedAt int64

Unix timestamp (in seconds) for when the item was created.

formatunixtime

InferenceOptions ChatKitThreadUserMessageItemInferenceOptions

Inference overrides applied to the message. Defaults to null when unset.

Model string

Model name that generated the response. Defaults to null when using the session default.

ToolChoice ChatKitThreadUserMessageItemInferenceOptionsToolChoice

Preferred tool to invoke. Defaults to null when ChatKit should auto-select.

ID string

Identifier of the requested tool.

Object ChatKitThreadItem

Type discriminator that is always `chatkit.thread_item`.

ThreadID string

Identifier of the parent thread.

Type ChatKitUserMessage

type ChatKitThreadAssistantMessageItem struct{…}

Assistant-authored message within a thread.

ID string

Identifier of the thread item.

Content [][ChatKitResponseOutputText](/api/reference/go/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_response_output_text%20%3E%20(schema))

Ordered assistant response segments.

Annotations []ChatKitResponseOutputTextAnnotationUnion

Ordered list of annotations attached to the response text.

One of the following:

type ChatKitResponseOutputTextAnnotationFile struct{…}

Annotation that references an uploaded file.

Source ChatKitResponseOutputTextAnnotationFileSource

File attachment referenced by the annotation.

Filename string

Filename referenced by the annotation.

Type File

Type discriminator that is always `file`.

Type File

Type discriminator that is always `file` for this annotation.

type ChatKitResponseOutputTextAnnotationURL struct{…}

Annotation that references a URL.

Source ChatKitResponseOutputTextAnnotationURLSource

URL referenced by the annotation.

Type URL

Type discriminator that is always `url`.

URL string

URL referenced by the annotation.

formaturi

Type URL

Type discriminator that is always `url` for this annotation.

Text string

Assistant generated text.

Type OutputText

Type discriminator that is always `output_text`.

CreatedAt int64

Unix timestamp (in seconds) for when the item was created.

formatunixtime

Object ChatKitThreadItem

Type discriminator that is always `chatkit.thread_item`.

ThreadID string

Identifier of the parent thread.

Type ChatKitAssistantMessage

Type discriminator that is always `chatkit.assistant_message`.

type ChatKitWidgetItem struct{…}

Thread item that renders a widget payload.

ID string

Identifier of the thread item.

CreatedAt int64

Unix timestamp (in seconds) for when the item was created.

formatunixtime

Object ChatKitThreadItem

Type discriminator that is always `chatkit.thread_item`.

ThreadID string

Identifier of the parent thread.

Type ChatKitWidget

Type discriminator that is always `chatkit.widget`.

Widget string

Serialized widget payload rendered in the UI.

type ChatKitThreadItemListDataChatKitClientToolCall struct{…}

Record of a client side tool invocation initiated by the assistant.

ID string

Identifier of the thread item.

Arguments string

JSON-encoded arguments that were sent to the tool.

CallID string

Identifier for the client tool call.

CreatedAt int64

Unix timestamp (in seconds) for when the item was created.

formatunixtime

Name string

Tool name that was invoked.

Object ChatKitThreadItem

Type discriminator that is always `chatkit.thread_item`.

Output string

JSON-encoded output captured from the tool. Defaults to null while execution is in progress.

Status string

Execution status for the tool call.

One of the following:

const ChatKitThreadItemListDataChatKitClientToolCallStatusInProgress ChatKitThreadItemListDataChatKitClientToolCallStatus = "in\_progress"

const ChatKitThreadItemListDataChatKitClientToolCallStatusCompleted ChatKitThreadItemListDataChatKitClientToolCallStatus = "completed"

ThreadID string

Identifier of the parent thread.

Type ChatKitClientToolCall

Type discriminator that is always `chatkit.client_tool_call`.

type ChatKitThreadItemListDataChatKitTask struct{…}

Task emitted by the workflow to show progress and status updates.

ID string

Identifier of the thread item.

CreatedAt int64

Unix timestamp (in seconds) for when the item was created.

formatunixtime

Heading string

Optional heading for the task. Defaults to null when not provided.

Object ChatKitThreadItem

Type discriminator that is always `chatkit.thread_item`.

Summary string

Optional summary that describes the task. Defaults to null when omitted.

TaskType string

Subtype for the task.

One of the following:

const ChatKitThreadItemListDataChatKitTaskTaskTypeCustom ChatKitThreadItemListDataChatKitTaskTaskType = "custom"

const ChatKitThreadItemListDataChatKitTaskTaskTypeThought ChatKitThreadItemListDataChatKitTaskTaskType = "thought"

ThreadID string

Identifier of the parent thread.

Type ChatKitTask

Type discriminator that is always `chatkit.task`.

type ChatKitThreadItemListDataChatKitTaskGroup struct{…}

Collection of workflow tasks grouped together in the thread.

ID string

Identifier of the thread item.

CreatedAt int64

Unix timestamp (in seconds) for when the item was created.

formatunixtime

Object ChatKitThreadItem

Type discriminator that is always `chatkit.thread_item`.

Tasks []ChatKitThreadItemListDataChatKitTaskGroupTask

Tasks included in the group.

Heading string

Optional heading for the grouped task. Defaults to null when not provided.

Summary string

Optional summary that describes the grouped task. Defaults to null when omitted.

Type string

Subtype for the grouped task.

One of the following:

const ChatKitThreadItemListDataChatKitTaskGroupTaskTypeCustom ChatKitThreadItemListDataChatKitTaskGroupTaskType = "custom"

const ChatKitThreadItemListDataChatKitTaskGroupTaskTypeThought ChatKitThreadItemListDataChatKitTaskGroupTaskType = "thought"

ThreadID string

Identifier of the parent thread.

Type ChatKitTaskGroup

Type discriminator that is always `chatkit.task_group`.

FirstID string

The ID of the first item in the list.

HasMore bool

Whether there are more items available.

LastID string

The ID of the last item in the list.

Object List

The type of object returned, must be `list`.

type ChatKitThreadUserMessageItem struct{…}

User-authored messages within a thread.

ID string

Identifier of the thread item.

Attachments [][ChatKitAttachment](/api/reference/go/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_attachment%20%3E%20(schema))

Attachments associated with the user message. Defaults to an empty list.

ID string

Identifier for the attachment.

MimeType string

MIME type of the attachment.

Name string

Original display name for the attachment.

PreviewURL string

Preview URL for rendering the attachment inline.

formaturi

Type ChatKitAttachmentType

Attachment discriminator.

One of the following:

const ChatKitAttachmentTypeImage ChatKitAttachmentType = "image"

const ChatKitAttachmentTypeFile ChatKitAttachmentType = "file"

Content []ChatKitThreadUserMessageItemContentUnion

Ordered content elements supplied by the user.

One of the following:

type ChatKitThreadUserMessageItemContentInputText struct{…}

Text block that a user contributed to the thread.

Text string

Plain-text content supplied by the user.

Type InputText

Type discriminator that is always `input_text`.

type ChatKitThreadUserMessageItemContentQuotedText struct{…}

Quoted snippet that the user referenced in their message.

Text string

Quoted text content.

Type QuotedText

Type discriminator that is always `quoted_text`.

CreatedAt int64

Unix timestamp (in seconds) for when the item was created.

formatunixtime

InferenceOptions ChatKitThreadUserMessageItemInferenceOptions

Inference overrides applied to the message. Defaults to null when unset.

Model string

Model name that generated the response. Defaults to null when using the session default.

ToolChoice ChatKitThreadUserMessageItemInferenceOptionsToolChoice

Preferred tool to invoke. Defaults to null when ChatKit should auto-select.

ID string

Identifier of the requested tool.

Object ChatKitThreadItem

Type discriminator that is always `chatkit.thread_item`.

ThreadID string

Identifier of the parent thread.

Type ChatKitUserMessage

type ChatKitWidgetItem struct{…}

Thread item that renders a widget payload.

ID string

Identifier of the thread item.

CreatedAt int64

Unix timestamp (in seconds) for when the item was created.

formatunixtime

Object ChatKitThreadItem

Type discriminator that is always `chatkit.thread_item`.

ThreadID string

Identifier of the parent thread.

Type ChatKitWidget

Type discriminator that is always `chatkit.widget`.

Widget string

Serialized widget payload rendered in the UI.

#### BetaAssistants

Build Assistants that can call models and use tools.

##### [List assistants](/api/reference/go/resources/beta/subresources/assistants/methods/list)

Deprecated

client.Beta.Assistants.List(ctx, query) (\*CursorPage[[Assistant](/api/reference/go/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema))], error)

GET/assistants

##### [Create assistant](/api/reference/go/resources/beta/subresources/assistants/methods/create)

Deprecated

client.Beta.Assistants.New(ctx, body) (\*[Assistant](/api/reference/go/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema)), error)

POST/assistants

##### [Retrieve assistant](/api/reference/go/resources/beta/subresources/assistants/methods/retrieve)

Deprecated

client.Beta.Assistants.Get(ctx, assistantID) (\*[Assistant](/api/reference/go/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema)), error)

GET/assistants/{assistant\_id}

##### [Modify assistant](/api/reference/go/resources/beta/subresources/assistants/methods/update)

Deprecated

client.Beta.Assistants.Update(ctx, assistantID, body) (\*[Assistant](/api/reference/go/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema)), error)

POST/assistants/{assistant\_id}

##### [Delete assistant](/api/reference/go/resources/beta/subresources/assistants/methods/delete)

Deprecated

client.Beta.Assistants.Delete(ctx, assistantID) (\*[AssistantDeleted](/api/reference/go/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant_deleted%20%3E%20(schema)), error)

DELETE/assistants/{assistant\_id}

##### ModelsExpand Collapse

type Assistant struct{…}

Represents an `assistant` that can call the model and use tools.

ID string

The identifier, which can be referenced in API endpoints.

CreatedAt int64

The Unix timestamp (in seconds) for when the assistant was created.

formatunixtime

Description string

The description of the assistant. The maximum length is 512 characters.

maxLength512

Instructions string

The system instructions that the assistant uses. The maximum length is 256,000 characters.

maxLength256000

Metadata [Metadata](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

Model string

ID of the model to use. You can use the [List models](https://platform.openai.com/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](https://platform.openai.com/docs/models) for descriptions of them.

Name string

The name of the assistant. The maximum length is 256 characters.

maxLength256

Object Assistant

The object type, which is always `assistant`.

Tools [][AssistantToolUnion](/api/reference/go/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant_tool%20%3E%20(schema))

A list of tool enabled on the assistant. There can be a maximum of 128 tools per assistant. Tools can be of types `code_interpreter`, `file_search`, or `function`.

One of the following:

type CodeInterpreterTool struct{…}

Type CodeInterpreter

The type of tool being defined: `code_interpreter`

type FileSearchTool struct{…}

Type FileSearch

The type of tool being defined: `file_search`

FileSearch FileSearchToolFileSearchOptional

Overrides for the file search tool.

MaxNumResults int64Optional

The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

minimum1

maximum50

RankingOptions FileSearchToolFileSearchRankingOptionsOptional

The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score\_threshold of 0.

See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

ScoreThreshold float64

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

Ranker stringOptional

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

const FileSearchToolFileSearchRankingOptionsRankerAuto FileSearchToolFileSearchRankingOptionsRanker = "auto"

const FileSearchToolFileSearchRankingOptionsRankerDefault2024\_08\_21 FileSearchToolFileSearchRankingOptionsRanker = "default\_2024\_08\_21"

type FunctionTool struct{…}

Function [FunctionDefinition](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema))

Type Function

The type of tool being defined: `function`

ResponseFormat [AssistantResponseFormatOptionUnion](/api/reference/go/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20assistant_response_format_option%20%3E%20(schema))Optional

Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly “stuck” request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

Temperature float64Optional

What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

minimum0

maximum2

ToolResources AssistantToolResourcesOptional

A set of resources that are used by the assistant’s tools. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

CodeInterpreter AssistantToolResourcesCodeInterpreterOptional

FileIDs []stringOptional

A list of [file](https://platform.openai.com/docs/api-reference/files) IDs made available to the `code\_interpreter“ tool. There can be a maximum of 20 files associated with the tool.

FileSearch AssistantToolResourcesFileSearchOptional

VectorStoreIDs []stringOptional

The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) attached to this assistant. There can be a maximum of 1 vector store attached to the assistant.

TopP float64Optional

An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top\_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.

We generally recommend altering this or temperature but not both.

minimum0

maximum1

type AssistantDeleted struct{…}

ID string

Deleted bool

Object AssistantDeleted

type AssistantStreamEventUnion interface{…}

Represents an event emitted when streaming a Run.

Each event in a server-sent events stream has an `event` and `data` property:

event: thread.created
data: {"id": "thread_123", "object": "thread", ...}

We emit events whenever a new object is created, transitions to a new state, or is being
streamed in parts (deltas). For example, we emit `thread.run.created` when a new run
is created, `thread.run.completed` when a run completes, and so on. When an Assistant chooses
to create a message during a run, we emit a `thread.message.created event`, a
`thread.message.in_progress` event, many `thread.message.delta` events, and finally a
`thread.message.completed` event.

We may add additional events over time, so we recommend handling unknown events gracefully
in your code. See the [Assistants API quickstart](https://platform.openai.com/docs/assistants/overview) to learn how to
integrate the Assistants API with streaming.

One of the following:

type AssistantStreamEventThreadCreated struct{…}

Occurs when a new [thread](https://platform.openai.com/docs/api-reference/threads/object) is created.

Data [Thread](/api/reference/go/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20thread%20%3E%20(schema))

Represents a thread that contains [messages](https://platform.openai.com/docs/api-reference/messages).

Event ThreadCreated

Enabled boolOptional

Whether to enable input audio transcription.

type AssistantStreamEventThreadRunCreated struct{…}

Occurs when a new [run](https://platform.openai.com/docs/api-reference/runs/object) is created.

Data [Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadRunCreated

type AssistantStreamEventThreadRunQueued struct{…}

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) moves to a `queued` status.

Data [Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadRunQueued

type AssistantStreamEventThreadRunInProgress struct{…}

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) moves to an `in_progress` status.

Data [Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadRunInProgress

type AssistantStreamEventThreadRunRequiresAction struct{…}

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) moves to a `requires_action` status.

Data [Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadRunRequiresAction

type AssistantStreamEventThreadRunCompleted struct{…}

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) is completed.

Data [Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadRunCompleted

type AssistantStreamEventThreadRunIncomplete struct{…}

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) ends with status `incomplete`.

Data [Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadRunIncomplete

type AssistantStreamEventThreadRunFailed struct{…}

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) fails.

Data [Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadRunFailed

type AssistantStreamEventThreadRunCancelling struct{…}

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) moves to a `cancelling` status.

Data [Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadRunCancelling

type AssistantStreamEventThreadRunCancelled struct{…}

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) is cancelled.

Data [Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadRunCancelled

type AssistantStreamEventThreadRunExpired struct{…}

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) expires.

Data [Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadRunExpired

type AssistantStreamEventThreadRunStepCreated struct{…}

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) is created.

Data [RunStep](/api/reference/go/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

Event ThreadRunStepCreated

type AssistantStreamEventThreadRunStepInProgress struct{…}

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) moves to an `in_progress` state.

Data [RunStep](/api/reference/go/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

Event ThreadRunStepInProgress

type AssistantStreamEventThreadRunStepDelta struct{…}

Occurs when parts of a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) are being streamed.

Data [RunStepDeltaEvent](/api/reference/go/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta_event%20%3E%20(schema))

Represents a run step delta i.e. any changed fields on a run step during streaming.

Event ThreadRunStepDelta

type AssistantStreamEventThreadRunStepCompleted struct{…}

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) is completed.

Data [RunStep](/api/reference/go/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

Event ThreadRunStepCompleted

type AssistantStreamEventThreadRunStepFailed struct{…}

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) fails.

Data [RunStep](/api/reference/go/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

Event ThreadRunStepFailed

type AssistantStreamEventThreadRunStepCancelled struct{…}

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) is cancelled.

Data [RunStep](/api/reference/go/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

Event ThreadRunStepCancelled

type AssistantStreamEventThreadRunStepExpired struct{…}

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) expires.

Data [RunStep](/api/reference/go/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

Event ThreadRunStepExpired

type AssistantStreamEventThreadMessageCreated struct{…}

Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) is created.

Data [Message](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema))

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadMessageCreated

type AssistantStreamEventThreadMessageInProgress struct{…}

Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) moves to an `in_progress` state.

Data [Message](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema))

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadMessageInProgress

type AssistantStreamEventThreadMessageDelta struct{…}

Occurs when parts of a [Message](https://platform.openai.com/docs/api-reference/messages/object) are being streamed.

Data [MessageDeltaEvent](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_delta_event%20%3E%20(schema))

Represents a message delta i.e. any changed fields on a message during streaming.

Event ThreadMessageDelta

type AssistantStreamEventThreadMessageCompleted struct{…}

Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) is completed.

Data [Message](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema))

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadMessageCompleted

type AssistantStreamEventThreadMessageIncomplete struct{…}

Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) ends before it is completed.

Data [Message](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema))

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadMessageIncomplete

type AssistantStreamEventErrorEvent struct{…}

Occurs when an [error](https://platform.openai.com/docs/guides/error-codes#api-errors) occurs. This can happen due to an internal server error or a timeout.

Data [ErrorObject](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20error_object%20%3E%20(schema))

Event Error

type AssistantToolUnion interface{…}

One of the following:

type CodeInterpreterTool struct{…}

Type CodeInterpreter

The type of tool being defined: `code_interpreter`

type FileSearchTool struct{…}

Type FileSearch

The type of tool being defined: `file_search`

FileSearch FileSearchToolFileSearchOptional

Overrides for the file search tool.

MaxNumResults int64Optional

The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

minimum1

maximum50

RankingOptions FileSearchToolFileSearchRankingOptionsOptional

The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score\_threshold of 0.

See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

ScoreThreshold float64

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

Ranker stringOptional

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

const FileSearchToolFileSearchRankingOptionsRankerAuto FileSearchToolFileSearchRankingOptionsRanker = "auto"

const FileSearchToolFileSearchRankingOptionsRankerDefault2024\_08\_21 FileSearchToolFileSearchRankingOptionsRanker = "default\_2024\_08\_21"

type FunctionTool struct{…}

Function [FunctionDefinition](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema))

Type Function

The type of tool being defined: `function`

type CodeInterpreterTool struct{…}

Type CodeInterpreter

The type of tool being defined: `code_interpreter`

type FileSearchTool struct{…}

Type FileSearch

The type of tool being defined: `file_search`

FileSearch FileSearchToolFileSearchOptional

Overrides for the file search tool.

MaxNumResults int64Optional

The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

minimum1

maximum50

RankingOptions FileSearchToolFileSearchRankingOptionsOptional

The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score\_threshold of 0.

See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

ScoreThreshold float64

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

Ranker stringOptional

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

const FileSearchToolFileSearchRankingOptionsRankerAuto FileSearchToolFileSearchRankingOptionsRanker = "auto"

const FileSearchToolFileSearchRankingOptionsRankerDefault2024\_08\_21 FileSearchToolFileSearchRankingOptionsRanker = "default\_2024\_08\_21"

type FunctionTool struct{…}

Function [FunctionDefinition](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema))

Type Function

The type of tool being defined: `function`

type MessageStreamEventUnion interface{…}

Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) is created.

One of the following:

MessageStreamEventThreadMessageCreated

Data [Message](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema))

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadMessageCreated

MessageStreamEventThreadMessageInProgress

Data [Message](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema))

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadMessageInProgress

MessageStreamEventThreadMessageDelta

Data [MessageDeltaEvent](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_delta_event%20%3E%20(schema))

Represents a message delta i.e. any changed fields on a message during streaming.

Event ThreadMessageDelta

MessageStreamEventThreadMessageCompleted

Data [Message](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema))

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadMessageCompleted

MessageStreamEventThreadMessageIncomplete

Data [Message](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema))

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadMessageIncomplete

type RunStepStreamEventUnion interface{…}

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) is created.

One of the following:

RunStepStreamEventThreadRunStepCreated

Data [RunStep](/api/reference/go/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

Event ThreadRunStepCreated

RunStepStreamEventThreadRunStepInProgress

Data [RunStep](/api/reference/go/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

Event ThreadRunStepInProgress

RunStepStreamEventThreadRunStepDelta

Data [RunStepDeltaEvent](/api/reference/go/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta_event%20%3E%20(schema))

Represents a run step delta i.e. any changed fields on a run step during streaming.

Event ThreadRunStepDelta

RunStepStreamEventThreadRunStepCompleted

Data [RunStep](/api/reference/go/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

Event ThreadRunStepCompleted

RunStepStreamEventThreadRunStepFailed

Data [RunStep](/api/reference/go/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

Event ThreadRunStepFailed

RunStepStreamEventThreadRunStepCancelled

Data [RunStep](/api/reference/go/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

Event ThreadRunStepCancelled

RunStepStreamEventThreadRunStepExpired

Data [RunStep](/api/reference/go/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

Event ThreadRunStepExpired

type RunStreamEventUnion interface{…}

Occurs when a new [run](https://platform.openai.com/docs/api-reference/runs/object) is created.

One of the following:

RunStreamEventThreadRunCreated

Data [Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadRunCreated

RunStreamEventThreadRunQueued

Data [Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadRunQueued

RunStreamEventThreadRunInProgress

Data [Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadRunInProgress

RunStreamEventThreadRunRequiresAction

Data [Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadRunRequiresAction

RunStreamEventThreadRunCompleted

Data [Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadRunCompleted

RunStreamEventThreadRunIncomplete

Data [Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadRunIncomplete

RunStreamEventThreadRunFailed

Data [Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadRunFailed

RunStreamEventThreadRunCancelling

Data [Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadRunCancelling

RunStreamEventThreadRunCancelled

Data [Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadRunCancelled

RunStreamEventThreadRunExpired

Data [Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadRunExpired

type ThreadStreamEvent struct{…}

Occurs when a new [thread](https://platform.openai.com/docs/api-reference/threads/object) is created.

Data [Thread](/api/reference/go/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20thread%20%3E%20(schema))

Represents a thread that contains [messages](https://platform.openai.com/docs/api-reference/messages).

Event ThreadCreated

Enabled boolOptional

Whether to enable input audio transcription.

#### BetaThreads

Build Assistants that can call models and use tools.

##### [Create thread](/api/reference/go/resources/beta/subresources/threads/methods/create)

Deprecated

client.Beta.Threads.New(ctx, body) (\*[Thread](/api/reference/go/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20thread%20%3E%20(schema)), error)

POST/threads

##### [Create thread and run](/api/reference/go/resources/beta/subresources/threads/methods/create_and_run)

Deprecated

client.Beta.Threads.NewAndRun(ctx, body) (\*[Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)), error)

POST/threads/runs

##### [Retrieve thread](/api/reference/go/resources/beta/subresources/threads/methods/retrieve)

Deprecated

client.Beta.Threads.Get(ctx, threadID) (\*[Thread](/api/reference/go/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20thread%20%3E%20(schema)), error)

GET/threads/{thread\_id}

##### [Modify thread](/api/reference/go/resources/beta/subresources/threads/methods/update)

Deprecated

client.Beta.Threads.Update(ctx, threadID, body) (\*[Thread](/api/reference/go/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20thread%20%3E%20(schema)), error)

POST/threads/{thread\_id}

##### [Delete thread](/api/reference/go/resources/beta/subresources/threads/methods/delete)

Deprecated

client.Beta.Threads.Delete(ctx, threadID) (\*[ThreadDeleted](/api/reference/go/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20thread_deleted%20%3E%20(schema)), error)

DELETE/threads/{thread\_id}

##### ModelsExpand Collapse

type AssistantResponseFormatOptionUnion interface{…}

Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly “stuck” request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

One of the following:

type Auto string

`auto` is the default value

type ResponseFormatText struct{…}

Default response format. Used to generate text responses.

Type Text

The type of response format being defined. Always `text`.

type ResponseFormatJSONObject struct{…}

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

Type JSONObject

The type of response format being defined. Always `json_object`.

type ResponseFormatJSONSchema struct{…}

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

JSONSchema ResponseFormatJSONSchemaJSONSchema

Structured Outputs configuration options, including a JSON Schema.

Name string

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

Description stringOptional

A description of what the response format is for, used by the model to
determine how to respond in the format.

Schema map[string, any]Optional

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

Strict boolOptional

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

Type JSONSchema

The type of response format being defined. Always `json_schema`.

type AssistantToolChoice struct{…}

Specifies a tool the model should use. Use to force the model to call a specific tool.

Type AssistantToolChoiceType

The type of the tool. If type is `function`, the function name must be set

One of the following:

const AssistantToolChoiceTypeFunction AssistantToolChoiceType = "function"

const AssistantToolChoiceTypeCodeInterpreter AssistantToolChoiceType = "code\_interpreter"

const AssistantToolChoiceTypeFileSearch AssistantToolChoiceType = "file\_search"

Function [AssistantToolChoiceFunction](/api/reference/go/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_function%20%3E%20(schema))Optional

type AssistantToolChoiceFunction struct{…}

Name string

The name of the function to call.

type AssistantToolChoiceOptionUnion interface{…}

Controls which (if any) tool is called by the model.
`none` means the model will not call any tools and instead generates a message.
`auto` is the default value and means the model can pick between generating a message or calling one or more tools.
`required` means the model must call one or more tools before responding to the user.
Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

One of the following:

type AssistantToolChoiceOptionAuto string

`none` means the model will not call any tools and instead generates a message. `auto` means the model can pick between generating a message or calling one or more tools. `required` means the model must call one or more tools before responding to the user.

One of the following:

const AssistantToolChoiceOptionAutoNone AssistantToolChoiceOptionAuto = "none"

const AssistantToolChoiceOptionAutoAuto AssistantToolChoiceOptionAuto = "auto"

const AssistantToolChoiceOptionAutoRequired AssistantToolChoiceOptionAuto = "required"

type AssistantToolChoice struct{…}

Specifies a tool the model should use. Use to force the model to call a specific tool.

Type AssistantToolChoiceType

The type of the tool. If type is `function`, the function name must be set

One of the following:

const AssistantToolChoiceTypeFunction AssistantToolChoiceType = "function"

const AssistantToolChoiceTypeCodeInterpreter AssistantToolChoiceType = "code\_interpreter"

const AssistantToolChoiceTypeFileSearch AssistantToolChoiceType = "file\_search"

Function [AssistantToolChoiceFunction](/api/reference/go/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_function%20%3E%20(schema))Optional

type Thread struct{…}

Represents a thread that contains [messages](https://platform.openai.com/docs/api-reference/messages).

ID string

The identifier, which can be referenced in API endpoints.

CreatedAt int64

The Unix timestamp (in seconds) for when the thread was created.

formatunixtime

Metadata [Metadata](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

Object Thread

The object type, which is always `thread`.

ToolResources ThreadToolResources

A set of resources that are made available to the assistant’s tools in this thread. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

CodeInterpreter ThreadToolResourcesCodeInterpreterOptional

FileIDs []stringOptional

A list of [file](https://platform.openai.com/docs/api-reference/files) IDs made available to the `code_interpreter` tool. There can be a maximum of 20 files associated with the tool.

FileSearch ThreadToolResourcesFileSearchOptional

VectorStoreIDs []stringOptional

The [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) attached to this thread. There can be a maximum of 1 vector store attached to the thread.

type ThreadDeleted struct{…}

ID string

Deleted bool

Object ThreadDeleted

#### BetaThreadsRuns

Build Assistants that can call models and use tools.

##### [List runs](/api/reference/go/resources/beta/subresources/threads/subresources/runs/methods/list)

Deprecated

client.Beta.Threads.Runs.List(ctx, threadID, query) (\*CursorPage[[Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))], error)

GET/threads/{thread\_id}/runs

##### [Create run](/api/reference/go/resources/beta/subresources/threads/subresources/runs/methods/create)

Deprecated

client.Beta.Threads.Runs.New(ctx, threadID, params) (\*[Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)), error)

POST/threads/{thread\_id}/runs

##### [Retrieve run](/api/reference/go/resources/beta/subresources/threads/subresources/runs/methods/retrieve)

Deprecated

client.Beta.Threads.Runs.Get(ctx, threadID, runID) (\*[Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)), error)

GET/threads/{thread\_id}/runs/{run\_id}

##### [Modify run](/api/reference/go/resources/beta/subresources/threads/subresources/runs/methods/update)

Deprecated

client.Beta.Threads.Runs.Update(ctx, threadID, runID, body) (\*[Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)), error)

POST/threads/{thread\_id}/runs/{run\_id}

##### [Submit tool outputs to run](/api/reference/go/resources/beta/subresources/threads/subresources/runs/methods/submit_tool_outputs)

Deprecated

client.Beta.Threads.Runs.SubmitToolOutputs(ctx, threadID, runID, body) (\*[Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)), error)

POST/threads/{thread\_id}/runs/{run\_id}/submit\_tool\_outputs

##### [Cancel a run](/api/reference/go/resources/beta/subresources/threads/subresources/runs/methods/cancel)

Deprecated

client.Beta.Threads.Runs.Cancel(ctx, threadID, runID) (\*[Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)), error)

POST/threads/{thread\_id}/runs/{run\_id}/cancel

##### ModelsExpand Collapse

type RequiredActionFunctionToolCall struct{…}

Tool call objects

ID string

The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

Function RequiredActionFunctionToolCallFunction

The function definition.

Arguments string

The arguments that the model expects you to pass to the function.

Name string

The name of the function.

Type Function

The type of tool call the output is required for. For now, this is always `function`.

type Run struct{…}

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

ID string

The identifier, which can be referenced in API endpoints.

AssistantID string

The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for execution of this run.

CancelledAt int64

The Unix timestamp (in seconds) for when the run was cancelled.

formatunixtime

CompletedAt int64

The Unix timestamp (in seconds) for when the run was completed.

formatunixtime

CreatedAt int64

The Unix timestamp (in seconds) for when the run was created.

formatunixtime

ExpiresAt int64

The Unix timestamp (in seconds) for when the run will expire.

formatunixtime

FailedAt int64

The Unix timestamp (in seconds) for when the run failed.

formatunixtime

IncompleteDetails RunIncompleteDetails

Details on why the run is incomplete. Will be `null` if the run is not incomplete.

Reason stringOptional

The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

One of the following:

const RunIncompleteDetailsReasonMaxCompletionTokens RunIncompleteDetailsReason = "max\_completion\_tokens"

const RunIncompleteDetailsReasonMaxPromptTokens RunIncompleteDetailsReason = "max\_prompt\_tokens"

Instructions string

The instructions that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

LastError RunLastError

The last error associated with this run. Will be `null` if there are no errors.

Code string

One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

One of the following:

const RunLastErrorCodeServerError RunLastErrorCode = "server\_error"

const RunLastErrorCodeRateLimitExceeded RunLastErrorCode = "rate\_limit\_exceeded"

const RunLastErrorCodeInvalidPrompt RunLastErrorCode = "invalid\_prompt"

Message string

A human-readable description of the error.

MaxCompletionTokens int64

The maximum number of completion tokens specified to have been used over the course of the run.

minimum256

MaxPromptTokens int64

The maximum number of prompt tokens specified to have been used over the course of the run.

minimum256

Metadata [Metadata](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

Model string

The model that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

Object ThreadRun

The object type, which is always `thread.run`.

ParallelToolCalls bool

Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

RequiredAction RunRequiredAction

Details on the action required to continue the run. Will be `null` if no action is required.

SubmitToolOutputs RunRequiredActionSubmitToolOutputs

Details on the tool outputs needed for this run to continue.

ToolCalls [][RequiredActionFunctionToolCall](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20required_action_function_tool_call%20%3E%20(schema))

A list of the relevant tool calls.

ID string

The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

Function RequiredActionFunctionToolCallFunction

The function definition.

Arguments string

The arguments that the model expects you to pass to the function.

Name string

The name of the function.

Type Function

The type of tool call the output is required for. For now, this is always `function`.

Type SubmitToolOutputs

For now, this is always `submit_tool_outputs`.

ResponseFormat [AssistantResponseFormatOptionUnion](/api/reference/go/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20assistant_response_format_option%20%3E%20(schema))

Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly “stuck” request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

StartedAt int64

The Unix timestamp (in seconds) for when the run was started.

formatunixtime

Status [RunStatus](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run_status%20%3E%20(schema))

The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

ThreadID string

The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

ToolChoice [AssistantToolChoiceOptionUnion](/api/reference/go/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_option%20%3E%20(schema))

Controls which (if any) tool is called by the model.
`none` means the model will not call any tools and instead generates a message.
`auto` is the default value and means the model can pick between generating a message or calling one or more tools.
`required` means the model must call one or more tools before responding to the user.
Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

Tools [][AssistantToolUnion](/api/reference/go/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant_tool%20%3E%20(schema))

The list of tools that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

One of the following:

type CodeInterpreterTool struct{…}

Type CodeInterpreter

The type of tool being defined: `code_interpreter`

type FileSearchTool struct{…}

Type FileSearch

The type of tool being defined: `file_search`

FileSearch FileSearchToolFileSearchOptional

Overrides for the file search tool.

MaxNumResults int64Optional

The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

minimum1

maximum50

RankingOptions FileSearchToolFileSearchRankingOptionsOptional

The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score\_threshold of 0.

See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

ScoreThreshold float64

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

Ranker stringOptional

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

const FileSearchToolFileSearchRankingOptionsRankerAuto FileSearchToolFileSearchRankingOptionsRanker = "auto"

const FileSearchToolFileSearchRankingOptionsRankerDefault2024\_08\_21 FileSearchToolFileSearchRankingOptionsRanker = "default\_2024\_08\_21"

type FunctionTool struct{…}

Function [FunctionDefinition](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema))

Type Function

The type of tool being defined: `function`

TruncationStrategy RunTruncationStrategy

Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

Type string

The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

One of the following:

const RunTruncationStrategyTypeAuto RunTruncationStrategyType = "auto"

const RunTruncationStrategyTypeLastMessages RunTruncationStrategyType = "last\_messages"

LastMessages int64Optional

The number of most recent messages from the thread when constructing the context for the run.

minimum1

Usage RunUsage

Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

CompletionTokens int64

Number of completion tokens used over the course of the run.

PromptTokens int64

Number of prompt tokens used over the course of the run.

TotalTokens int64

Total number of tokens used (prompt + completion).

Temperature float64Optional

The sampling temperature used for this run. If not set, defaults to 1.

TopP float64Optional

The nucleus sampling value used for this run. If not set, defaults to 1.

type RunStatus string

The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

One of the following:

const RunStatusQueued [RunStatus](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run_status%20%3E%20(schema)) = "queued"

const RunStatusInProgress [RunStatus](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run_status%20%3E%20(schema)) = "in\_progress"

const RunStatusRequiresAction [RunStatus](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run_status%20%3E%20(schema)) = "requires\_action"

const RunStatusCancelling [RunStatus](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run_status%20%3E%20(schema)) = "cancelling"

const RunStatusCancelled [RunStatus](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run_status%20%3E%20(schema)) = "cancelled"

const RunStatusFailed [RunStatus](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run_status%20%3E%20(schema)) = "failed"

const RunStatusCompleted [RunStatus](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run_status%20%3E%20(schema)) = "completed"

const RunStatusIncomplete [RunStatus](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run_status%20%3E%20(schema)) = "incomplete"

const RunStatusExpired [RunStatus](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run_status%20%3E%20(schema)) = "expired"

#### BetaThreadsRunsSteps

Build Assistants that can call models and use tools.

##### [List run steps](/api/reference/go/resources/beta/subresources/threads/subresources/runs/subresources/steps/methods/list)

Deprecated

client.Beta.Threads.Runs.Steps.List(ctx, threadID, runID, query) (\*CursorPage[[RunStep](/api/reference/go/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))], error)

GET/threads/{thread\_id}/runs/{run\_id}/steps

##### [Retrieve run step](/api/reference/go/resources/beta/subresources/threads/subresources/runs/subresources/steps/methods/retrieve)

Deprecated

client.Beta.Threads.Runs.Steps.Get(ctx, threadID, runID, stepID, query) (\*[RunStep](/api/reference/go/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)), error)

GET/threads/{thread\_id}/runs/{run\_id}/steps/{step\_id}

##### ModelsExpand Collapse

type CodeInterpreterLogs struct{…}

Text output from the Code Interpreter tool call as part of a run step.

Index int64

The index of the output in the outputs array.

Type Logs

Always `logs`.

Logs stringOptional

The text output from the Code Interpreter tool call.

type CodeInterpreterOutputImage struct{…}

Index int64

The index of the output in the outputs array.

Type Image

Always `image`.

Image CodeInterpreterOutputImageImageOptional

FileID stringOptional

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

type CodeInterpreterToolCall struct{…}

Details of the Code Interpreter tool call the run step was involved in.

ID string

The ID of the tool call.

CodeInterpreter CodeInterpreterToolCallCodeInterpreter

The Code Interpreter tool call definition.

Input string

The input to the Code Interpreter tool call.

Outputs []CodeInterpreterToolCallCodeInterpreterOutputUnion

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

type CodeInterpreterToolCallCodeInterpreterOutputLogs struct{…}

Text output from the Code Interpreter tool call as part of a run step.

Logs string

The text output from the Code Interpreter tool call.

Type Logs

Always `logs`.

type CodeInterpreterToolCallCodeInterpreterOutputImage struct{…}

Image CodeInterpreterToolCallCodeInterpreterOutputImageImage

FileID string

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

Type Image

Always `image`.

Type CodeInterpreter

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

type CodeInterpreterToolCallDelta struct{…}

Details of the Code Interpreter tool call the run step was involved in.

Index int64

The index of the tool call in the tool calls array.

Type CodeInterpreter

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

ID stringOptional

The ID of the tool call.

CodeInterpreter CodeInterpreterToolCallDeltaCodeInterpreterOptional

The Code Interpreter tool call definition.

Input stringOptional

The input to the Code Interpreter tool call.

Outputs []CodeInterpreterToolCallDeltaCodeInterpreterOutputUnionOptional

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

type CodeInterpreterLogs struct{…}

Text output from the Code Interpreter tool call as part of a run step.

Index int64

The index of the output in the outputs array.

Type Logs

Always `logs`.

Logs stringOptional

The text output from the Code Interpreter tool call.

type CodeInterpreterOutputImage struct{…}

Index int64

The index of the output in the outputs array.

Type Image

Always `image`.

Image CodeInterpreterOutputImageImageOptional

FileID stringOptional

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

type FileSearchToolCall struct{…}

ID string

The ID of the tool call object.

FileSearch FileSearchToolCallFileSearch

For now, this is always going to be an empty object.

RankingOptions FileSearchToolCallFileSearchRankingOptionsOptional

The ranking options for the file search.

Ranker string

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

const FileSearchToolCallFileSearchRankingOptionsRankerAuto FileSearchToolCallFileSearchRankingOptionsRanker = "auto"

const FileSearchToolCallFileSearchRankingOptionsRankerDefault2024\_08\_21 FileSearchToolCallFileSearchRankingOptionsRanker = "default\_2024\_08\_21"

ScoreThreshold float64

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

Results []FileSearchToolCallFileSearchResultOptional

The results of the file search.

FileID string

The ID of the file that result was found in.

FileName string

The name of the file that result was found in.

Score float64

The score of the result. All values must be a floating point number between 0 and 1.

minimum0

maximum1

Content []FileSearchToolCallFileSearchResultContentOptional

The content of the result that was found. The content is only included if requested via the include query parameter.

Text stringOptional

The text content of the file.

Type stringOptional

The type of the content.

Type FileSearch

The type of tool call. This is always going to be `file_search` for this type of tool call.

type FileSearchToolCallDelta struct{…}

FileSearch any

For now, this is always going to be an empty object.

Index int64

The index of the tool call in the tool calls array.

Type FileSearch

The type of tool call. This is always going to be `file_search` for this type of tool call.

ID stringOptional

The ID of the tool call object.

type FunctionToolCall struct{…}

ID string

The ID of the tool call object.

Function FunctionToolCallFunction

The definition of the function that was called.

Arguments string

The arguments passed to the function.

Name string

The name of the function.

Output string

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

Type Function

The type of tool call. This is always going to be `function` for this type of tool call.

type FunctionToolCallDelta struct{…}

Index int64

The index of the tool call in the tool calls array.

Type Function

The type of tool call. This is always going to be `function` for this type of tool call.

ID stringOptional

The ID of the tool call object.

Function FunctionToolCallDeltaFunctionOptional

The definition of the function that was called.

Arguments stringOptional

The arguments passed to the function.

Name stringOptional

The name of the function.

Output stringOptional

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

type MessageCreationStepDetails struct{…}

Details of the message creation by the run step.

MessageCreation MessageCreationStepDetailsMessageCreation

MessageID string

The ID of the message that was created by this run step.

Type MessageCreation

Always `message_creation`.

type RunStep struct{…}

Represents a step in execution of a run.

ID string

The identifier of the run step, which can be referenced in API endpoints.

AssistantID string

The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) associated with the run step.

CancelledAt int64

The Unix timestamp (in seconds) for when the run step was cancelled.

formatunixtime

CompletedAt int64

The Unix timestamp (in seconds) for when the run step completed.

formatunixtime

CreatedAt int64

The Unix timestamp (in seconds) for when the run step was created.

formatunixtime

ExpiredAt int64

The Unix timestamp (in seconds) for when the run step expired. A step is considered expired if the parent run is expired.

formatunixtime

FailedAt int64

The Unix timestamp (in seconds) for when the run step failed.

formatunixtime

LastError RunStepLastError

The last error associated with this run step. Will be `null` if there are no errors.

Code string

One of `server_error` or `rate_limit_exceeded`.

One of the following:

const RunStepLastErrorCodeServerError RunStepLastErrorCode = "server\_error"

const RunStepLastErrorCodeRateLimitExceeded RunStepLastErrorCode = "rate\_limit\_exceeded"

Message string

A human-readable description of the error.

Metadata [Metadata](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

Object ThreadRunStep

The object type, which is always `thread.run.step`.

RunID string

The ID of the [run](https://platform.openai.com/docs/api-reference/runs) that this run step is a part of.

Status RunStepStatus

The status of the run step, which can be either `in_progress`, `cancelled`, `failed`, `completed`, or `expired`.

One of the following:

const RunStepStatusInProgress RunStepStatus = "in\_progress"

const RunStepStatusCancelled RunStepStatus = "cancelled"

const RunStepStatusFailed RunStepStatus = "failed"

const RunStepStatusCompleted RunStepStatus = "completed"

const RunStepStatusExpired RunStepStatus = "expired"

StepDetails RunStepStepDetailsUnion

The details of the run step.

One of the following:

type MessageCreationStepDetails struct{…}

Details of the message creation by the run step.

MessageCreation MessageCreationStepDetailsMessageCreation

MessageID string

The ID of the message that was created by this run step.

Type MessageCreation

Always `message_creation`.

type ToolCallsStepDetails struct{…}

Details of the tool call.

ToolCalls [][ToolCallUnion](/api/reference/go/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call%20%3E%20(schema))

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

One of the following:

type CodeInterpreterToolCall struct{…}

Details of the Code Interpreter tool call the run step was involved in.

ID string

The ID of the tool call.

CodeInterpreter CodeInterpreterToolCallCodeInterpreter

The Code Interpreter tool call definition.

Input string

The input to the Code Interpreter tool call.

Outputs []CodeInterpreterToolCallCodeInterpreterOutputUnion

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

type CodeInterpreterToolCallCodeInterpreterOutputLogs struct{…}

Text output from the Code Interpreter tool call as part of a run step.

Logs string

The text output from the Code Interpreter tool call.

Type Logs

Always `logs`.

type CodeInterpreterToolCallCodeInterpreterOutputImage struct{…}

Image CodeInterpreterToolCallCodeInterpreterOutputImageImage

FileID string

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

Type Image

Always `image`.

Type CodeInterpreter

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

type FileSearchToolCall struct{…}

ID string

The ID of the tool call object.

FileSearch FileSearchToolCallFileSearch

For now, this is always going to be an empty object.

RankingOptions FileSearchToolCallFileSearchRankingOptionsOptional

The ranking options for the file search.

Ranker string

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

const FileSearchToolCallFileSearchRankingOptionsRankerAuto FileSearchToolCallFileSearchRankingOptionsRanker = "auto"

const FileSearchToolCallFileSearchRankingOptionsRankerDefault2024\_08\_21 FileSearchToolCallFileSearchRankingOptionsRanker = "default\_2024\_08\_21"

ScoreThreshold float64

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

Results []FileSearchToolCallFileSearchResultOptional

The results of the file search.

FileID string

The ID of the file that result was found in.

FileName string

The name of the file that result was found in.

Score float64

The score of the result. All values must be a floating point number between 0 and 1.

minimum0

maximum1

Content []FileSearchToolCallFileSearchResultContentOptional

The content of the result that was found. The content is only included if requested via the include query parameter.

Text stringOptional

The text content of the file.

Type stringOptional

The type of the content.

Type FileSearch

The type of tool call. This is always going to be `file_search` for this type of tool call.

type FunctionToolCall struct{…}

ID string

The ID of the tool call object.

Function FunctionToolCallFunction

The definition of the function that was called.

Arguments string

The arguments passed to the function.

Name string

The name of the function.

Output string

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

Type Function

The type of tool call. This is always going to be `function` for this type of tool call.

Type ToolCalls

Always `tool_calls`.

ThreadID string

The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was run.

Type RunStepType

The type of run step, which can be either `message_creation` or `tool_calls`.

One of the following:

const RunStepTypeMessageCreation RunStepType = "message\_creation"

const RunStepTypeToolCalls RunStepType = "tool\_calls"

Usage RunStepUsage

Usage statistics related to the run step. This value will be `null` while the run step’s status is `in_progress`.

CompletionTokens int64

Number of completion tokens used over the course of the run step.

PromptTokens int64

Number of prompt tokens used over the course of the run step.

TotalTokens int64

Total number of tokens used (prompt + completion).

type RunStepDelta struct{…}

The delta containing the fields that have changed on the run step.

StepDetails RunStepDeltaStepDetailsUnionOptional

The details of the run step.

One of the following:

type RunStepDeltaMessageDelta struct{…}

Details of the message creation by the run step.

Type MessageCreation

Always `message_creation`.

MessageCreation RunStepDeltaMessageDeltaMessageCreationOptional

MessageID stringOptional

The ID of the message that was created by this run step.

type ToolCallDeltaObject struct{…}

Details of the tool call.

Type ToolCalls

Always `tool_calls`.

ToolCalls [][ToolCallDeltaUnion](/api/reference/go/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call_delta%20%3E%20(schema))Optional

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

One of the following:

type CodeInterpreterToolCallDelta struct{…}

Details of the Code Interpreter tool call the run step was involved in.

Index int64

The index of the tool call in the tool calls array.

Type CodeInterpreter

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

ID stringOptional

The ID of the tool call.

CodeInterpreter CodeInterpreterToolCallDeltaCodeInterpreterOptional

The Code Interpreter tool call definition.

Input stringOptional

The input to the Code Interpreter tool call.

Outputs []CodeInterpreterToolCallDeltaCodeInterpreterOutputUnionOptional

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

type CodeInterpreterLogs struct{…}

Text output from the Code Interpreter tool call as part of a run step.

Index int64

The index of the output in the outputs array.

Type Logs

Always `logs`.

Logs stringOptional

The text output from the Code Interpreter tool call.

type CodeInterpreterOutputImage struct{…}

Index int64

The index of the output in the outputs array.

Type Image

Always `image`.

Image CodeInterpreterOutputImageImageOptional

FileID stringOptional

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

type FileSearchToolCallDelta struct{…}

FileSearch any

For now, this is always going to be an empty object.

Index int64

The index of the tool call in the tool calls array.

Type FileSearch

The type of tool call. This is always going to be `file_search` for this type of tool call.

ID stringOptional

The ID of the tool call object.

type FunctionToolCallDelta struct{…}

Index int64

The index of the tool call in the tool calls array.

Type Function

The type of tool call. This is always going to be `function` for this type of tool call.

ID stringOptional

The ID of the tool call object.

Function FunctionToolCallDeltaFunctionOptional

The definition of the function that was called.

Arguments stringOptional

The arguments passed to the function.

Name stringOptional

The name of the function.

Output stringOptional

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

type RunStepDeltaEvent struct{…}

Represents a run step delta i.e. any changed fields on a run step during streaming.

ID string

The identifier of the run step, which can be referenced in API endpoints.

Delta [RunStepDelta](/api/reference/go/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta%20%3E%20(schema))

The delta containing the fields that have changed on the run step.

Object ThreadRunStepDelta

The object type, which is always `thread.run.step.delta`.

type RunStepDeltaMessageDelta struct{…}

Details of the message creation by the run step.

Type MessageCreation

Always `message_creation`.

MessageCreation RunStepDeltaMessageDeltaMessageCreationOptional

MessageID stringOptional

The ID of the message that was created by this run step.

type RunStepInclude string

type ToolCallUnion interface{…}

Details of the Code Interpreter tool call the run step was involved in.

One of the following:

type CodeInterpreterToolCall struct{…}

Details of the Code Interpreter tool call the run step was involved in.

ID string

The ID of the tool call.

CodeInterpreter CodeInterpreterToolCallCodeInterpreter

The Code Interpreter tool call definition.

Input string

The input to the Code Interpreter tool call.

Outputs []CodeInterpreterToolCallCodeInterpreterOutputUnion

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

type CodeInterpreterToolCallCodeInterpreterOutputLogs struct{…}

Text output from the Code Interpreter tool call as part of a run step.

Logs string

The text output from the Code Interpreter tool call.

Type Logs

Always `logs`.

type CodeInterpreterToolCallCodeInterpreterOutputImage struct{…}

Image CodeInterpreterToolCallCodeInterpreterOutputImageImage

FileID string

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

Type Image

Always `image`.

Type CodeInterpreter

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

type FileSearchToolCall struct{…}

ID string

The ID of the tool call object.

FileSearch FileSearchToolCallFileSearch

For now, this is always going to be an empty object.

RankingOptions FileSearchToolCallFileSearchRankingOptionsOptional

The ranking options for the file search.

Ranker string

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

const FileSearchToolCallFileSearchRankingOptionsRankerAuto FileSearchToolCallFileSearchRankingOptionsRanker = "auto"

const FileSearchToolCallFileSearchRankingOptionsRankerDefault2024\_08\_21 FileSearchToolCallFileSearchRankingOptionsRanker = "default\_2024\_08\_21"

ScoreThreshold float64

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

Results []FileSearchToolCallFileSearchResultOptional

The results of the file search.

FileID string

The ID of the file that result was found in.

FileName string

The name of the file that result was found in.

Score float64

The score of the result. All values must be a floating point number between 0 and 1.

minimum0

maximum1

Content []FileSearchToolCallFileSearchResultContentOptional

The content of the result that was found. The content is only included if requested via the include query parameter.

Text stringOptional

The text content of the file.

Type stringOptional

The type of the content.

Type FileSearch

The type of tool call. This is always going to be `file_search` for this type of tool call.

type FunctionToolCall struct{…}

ID string

The ID of the tool call object.

Function FunctionToolCallFunction

The definition of the function that was called.

Arguments string

The arguments passed to the function.

Name string

The name of the function.

Output string

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

Type Function

The type of tool call. This is always going to be `function` for this type of tool call.

type ToolCallDeltaUnion interface{…}

Details of the Code Interpreter tool call the run step was involved in.

One of the following:

type CodeInterpreterToolCallDelta struct{…}

Details of the Code Interpreter tool call the run step was involved in.

Index int64

The index of the tool call in the tool calls array.

Type CodeInterpreter

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

ID stringOptional

The ID of the tool call.

CodeInterpreter CodeInterpreterToolCallDeltaCodeInterpreterOptional

The Code Interpreter tool call definition.

Input stringOptional

The input to the Code Interpreter tool call.

Outputs []CodeInterpreterToolCallDeltaCodeInterpreterOutputUnionOptional

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

type CodeInterpreterLogs struct{…}

Text output from the Code Interpreter tool call as part of a run step.

Index int64

The index of the output in the outputs array.

Type Logs

Always `logs`.

Logs stringOptional

The text output from the Code Interpreter tool call.

type CodeInterpreterOutputImage struct{…}

Index int64

The index of the output in the outputs array.

Type Image

Always `image`.

Image CodeInterpreterOutputImageImageOptional

FileID stringOptional

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

type FileSearchToolCallDelta struct{…}

FileSearch any

For now, this is always going to be an empty object.

Index int64

The index of the tool call in the tool calls array.

Type FileSearch

The type of tool call. This is always going to be `file_search` for this type of tool call.

ID stringOptional

The ID of the tool call object.

type FunctionToolCallDelta struct{…}

Index int64

The index of the tool call in the tool calls array.

Type Function

The type of tool call. This is always going to be `function` for this type of tool call.

ID stringOptional

The ID of the tool call object.

Function FunctionToolCallDeltaFunctionOptional

The definition of the function that was called.

Arguments stringOptional

The arguments passed to the function.

Name stringOptional

The name of the function.

Output stringOptional

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

type ToolCallDeltaObject struct{…}

Details of the tool call.

Type ToolCalls

Always `tool_calls`.

ToolCalls [][ToolCallDeltaUnion](/api/reference/go/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call_delta%20%3E%20(schema))Optional

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

One of the following:

type CodeInterpreterToolCallDelta struct{…}

Details of the Code Interpreter tool call the run step was involved in.

Index int64

The index of the tool call in the tool calls array.

Type CodeInterpreter

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

ID stringOptional

The ID of the tool call.

CodeInterpreter CodeInterpreterToolCallDeltaCodeInterpreterOptional

The Code Interpreter tool call definition.

Input stringOptional

The input to the Code Interpreter tool call.

Outputs []CodeInterpreterToolCallDeltaCodeInterpreterOutputUnionOptional

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

type CodeInterpreterLogs struct{…}

Text output from the Code Interpreter tool call as part of a run step.

Index int64

The index of the output in the outputs array.

Type Logs

Always `logs`.

Logs stringOptional

The text output from the Code Interpreter tool call.

type CodeInterpreterOutputImage struct{…}

Index int64

The index of the output in the outputs array.

Type Image

Always `image`.

Image CodeInterpreterOutputImageImageOptional

FileID stringOptional

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

type FileSearchToolCallDelta struct{…}

FileSearch any

For now, this is always going to be an empty object.

Index int64

The index of the tool call in the tool calls array.

Type FileSearch

The type of tool call. This is always going to be `file_search` for this type of tool call.

ID stringOptional

The ID of the tool call object.

type FunctionToolCallDelta struct{…}

Index int64

The index of the tool call in the tool calls array.

Type Function

The type of tool call. This is always going to be `function` for this type of tool call.

ID stringOptional

The ID of the tool call object.

Function FunctionToolCallDeltaFunctionOptional

The definition of the function that was called.

Arguments stringOptional

The arguments passed to the function.

Name stringOptional

The name of the function.

Output stringOptional

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

type ToolCallsStepDetails struct{…}

Details of the tool call.

ToolCalls [][ToolCallUnion](/api/reference/go/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call%20%3E%20(schema))

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

One of the following:

type CodeInterpreterToolCall struct{…}

Details of the Code Interpreter tool call the run step was involved in.

ID string

The ID of the tool call.

CodeInterpreter CodeInterpreterToolCallCodeInterpreter

The Code Interpreter tool call definition.

Input string

The input to the Code Interpreter tool call.

Outputs []CodeInterpreterToolCallCodeInterpreterOutputUnion

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

type CodeInterpreterToolCallCodeInterpreterOutputLogs struct{…}

Text output from the Code Interpreter tool call as part of a run step.

Logs string

The text output from the Code Interpreter tool call.

Type Logs

Always `logs`.

type CodeInterpreterToolCallCodeInterpreterOutputImage struct{…}

Image CodeInterpreterToolCallCodeInterpreterOutputImageImage

FileID string

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

Type Image

Always `image`.

Type CodeInterpreter

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

type FileSearchToolCall struct{…}

ID string

The ID of the tool call object.

FileSearch FileSearchToolCallFileSearch

For now, this is always going to be an empty object.

RankingOptions FileSearchToolCallFileSearchRankingOptionsOptional

The ranking options for the file search.

Ranker string

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

const FileSearchToolCallFileSearchRankingOptionsRankerAuto FileSearchToolCallFileSearchRankingOptionsRanker = "auto"

const FileSearchToolCallFileSearchRankingOptionsRankerDefault2024\_08\_21 FileSearchToolCallFileSearchRankingOptionsRanker = "default\_2024\_08\_21"

ScoreThreshold float64

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

Results []FileSearchToolCallFileSearchResultOptional

The results of the file search.

FileID string

The ID of the file that result was found in.

FileName string

The name of the file that result was found in.

Score float64

The score of the result. All values must be a floating point number between 0 and 1.

minimum0

maximum1

Content []FileSearchToolCallFileSearchResultContentOptional

The content of the result that was found. The content is only included if requested via the include query parameter.

Text stringOptional

The text content of the file.

Type stringOptional

The type of the content.

Type FileSearch

The type of tool call. This is always going to be `file_search` for this type of tool call.

type FunctionToolCall struct{…}

ID string

The ID of the tool call object.

Function FunctionToolCallFunction

The definition of the function that was called.

Arguments string

The arguments passed to the function.

Name string

The name of the function.

Output string

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

Type Function

The type of tool call. This is always going to be `function` for this type of tool call.

Type ToolCalls

Always `tool_calls`.

#### BetaThreadsMessages

Build Assistants that can call models and use tools.

##### [List messages](/api/reference/go/resources/beta/subresources/threads/subresources/messages/methods/list)

Deprecated

client.Beta.Threads.Messages.List(ctx, threadID, query) (\*CursorPage[[Message](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema))], error)

GET/threads/{thread\_id}/messages

##### [Create message](/api/reference/go/resources/beta/subresources/threads/subresources/messages/methods/create)

Deprecated

client.Beta.Threads.Messages.New(ctx, threadID, body) (\*[Message](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)), error)

POST/threads/{thread\_id}/messages

##### [Modify message](/api/reference/go/resources/beta/subresources/threads/subresources/messages/methods/update)

Deprecated

client.Beta.Threads.Messages.Update(ctx, threadID, messageID, body) (\*[Message](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)), error)

POST/threads/{thread\_id}/messages/{message\_id}

##### [Retrieve message](/api/reference/go/resources/beta/subresources/threads/subresources/messages/methods/retrieve)

Deprecated

client.Beta.Threads.Messages.Get(ctx, threadID, messageID) (\*[Message](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)), error)

GET/threads/{thread\_id}/messages/{message\_id}

##### [Delete message](/api/reference/go/resources/beta/subresources/threads/subresources/messages/methods/delete)

Deprecated

client.Beta.Threads.Messages.Delete(ctx, threadID, messageID) (\*[MessageDeleted](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_deleted%20%3E%20(schema)), error)

DELETE/threads/{thread\_id}/messages/{message\_id}

##### ModelsExpand Collapse

type AnnotationUnion interface{…}

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

One of the following:

type FileCitationAnnotation struct{…}

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

EndIndex int64

minimum0

FileCitation FileCitationAnnotationFileCitation

FileID string

The ID of the specific File the citation is from.

StartIndex int64

minimum0

Text string

The text in the message content that needs to be replaced.

Type FileCitation

Always `file_citation`.

type FilePathAnnotation struct{…}

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

EndIndex int64

minimum0

FilePath FilePathAnnotationFilePath

FileID string

The ID of the file that was generated.

StartIndex int64

minimum0

Text string

The text in the message content that needs to be replaced.

Type FilePath

Always `file_path`.

type AnnotationDeltaUnion interface{…}

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

One of the following:

type FileCitationDeltaAnnotation struct{…}

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

Index int64

The index of the annotation in the text content part.

Type FileCitation

Always `file_citation`.

EndIndex int64Optional

minimum0

FileCitation FileCitationDeltaAnnotationFileCitationOptional

FileID stringOptional

The ID of the specific File the citation is from.

Quote stringOptional

The specific quote in the file.

StartIndex int64Optional

minimum0

Text stringOptional

The text in the message content that needs to be replaced.

type FilePathDeltaAnnotation struct{…}

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

Index int64

The index of the annotation in the text content part.

Type FilePath

Always `file_path`.

EndIndex int64Optional

minimum0

FilePath FilePathDeltaAnnotationFilePathOptional

FileID stringOptional

The ID of the file that was generated.

StartIndex int64Optional

minimum0

Text stringOptional

The text in the message content that needs to be replaced.

type FileCitationAnnotation struct{…}

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

EndIndex int64

minimum0

FileCitation FileCitationAnnotationFileCitation

FileID string

The ID of the specific File the citation is from.

StartIndex int64

minimum0

Text string

The text in the message content that needs to be replaced.

Type FileCitation

Always `file_citation`.

type FileCitationDeltaAnnotation struct{…}

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

Index int64

The index of the annotation in the text content part.

Type FileCitation

Always `file_citation`.

EndIndex int64Optional

minimum0

FileCitation FileCitationDeltaAnnotationFileCitationOptional

FileID stringOptional

The ID of the specific File the citation is from.

Quote stringOptional

The specific quote in the file.

StartIndex int64Optional

minimum0

Text stringOptional

The text in the message content that needs to be replaced.

type FilePathAnnotation struct{…}

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

EndIndex int64

minimum0

FilePath FilePathAnnotationFilePath

FileID string

The ID of the file that was generated.

StartIndex int64

minimum0

Text string

The text in the message content that needs to be replaced.

Type FilePath

Always `file_path`.

type FilePathDeltaAnnotation struct{…}

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

Index int64

The index of the annotation in the text content part.

Type FilePath

Always `file_path`.

EndIndex int64Optional

minimum0

FilePath FilePathDeltaAnnotationFilePathOptional

FileID stringOptional

The ID of the file that was generated.

StartIndex int64Optional

minimum0

Text stringOptional

The text in the message content that needs to be replaced.

type ImageFile struct{…}

FileID string

The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

Detail ImageFileDetailOptional

Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

One of the following:

const ImageFileDetailAuto ImageFileDetail = "auto"

const ImageFileDetailLow ImageFileDetail = "low"

const ImageFileDetailHigh ImageFileDetail = "high"

type ImageFileContentBlock struct{…}

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

ImageFile [ImageFile](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file%20%3E%20(schema))

Type ImageFile

Always `image_file`.

type ImageFileDelta struct{…}

Detail ImageFileDeltaDetailOptional

Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

One of the following:

const ImageFileDeltaDetailAuto ImageFileDeltaDetail = "auto"

const ImageFileDeltaDetailLow ImageFileDeltaDetail = "low"

const ImageFileDeltaDetailHigh ImageFileDeltaDetail = "high"

FileID stringOptional

The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

type ImageFileDeltaBlock struct{…}

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

Index int64

The index of the content part in the message.

Type ImageFile

Always `image_file`.

ImageFile [ImageFileDelta](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_delta%20%3E%20(schema))Optional

type ImageURL struct{…}

URL string

The external URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

formaturi

Detail ImageURLDetailOptional

Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`. Default value is `auto`

One of the following:

const ImageURLDetailAuto ImageURLDetail = "auto"

const ImageURLDetailLow ImageURLDetail = "low"

const ImageURLDetailHigh ImageURLDetail = "high"

type ImageURLContentBlock struct{…}

References an image URL in the content of a message.

ImageURL [ImageURL](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url%20%3E%20(schema))

Type ImageURL

The type of the content part.

type ImageURLDelta struct{…}

Detail ImageURLDeltaDetailOptional

Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`.

One of the following:

const ImageURLDeltaDetailAuto ImageURLDeltaDetail = "auto"

const ImageURLDeltaDetailLow ImageURLDeltaDetail = "low"

const ImageURLDeltaDetailHigh ImageURLDeltaDetail = "high"

URL stringOptional

The URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

formaturi

type ImageURLDeltaBlock struct{…}

References an image URL in the content of a message.

Index int64

The index of the content part in the message.

Type ImageURL

Always `image_url`.

ImageURL [ImageURLDelta](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_delta%20%3E%20(schema))Optional

type Message struct{…}

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

ID string

The identifier, which can be referenced in API endpoints.

AssistantID string

If applicable, the ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) that authored this message.

Attachments []MessageAttachment

A list of files attached to the message, and the tools they were added to.

FileID stringOptional

The ID of the file to attach to the message.

Tools []MessageAttachmentToolUnionOptional

The tools to add this file to.

One of the following:

type CodeInterpreterTool struct{…}

Type CodeInterpreter

The type of tool being defined: `code_interpreter`

type MessageAttachmentToolAssistantToolsFileSearchTypeOnly struct{…}

Type FileSearch

The type of tool being defined: `file_search`

CompletedAt int64

The Unix timestamp (in seconds) for when the message was completed.

formatunixtime

Content [][MessageContentUnion](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_content%20%3E%20(schema))

The content of the message in array of text and/or images.

One of the following:

type ImageFileContentBlock struct{…}

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

ImageFile [ImageFile](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file%20%3E%20(schema))

Type ImageFile

Always `image_file`.

type ImageURLContentBlock struct{…}

References an image URL in the content of a message.

ImageURL [ImageURL](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url%20%3E%20(schema))

Type ImageURL

The type of the content part.

type TextContentBlock struct{…}

The text content that is part of a message.

Text [Text](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text%20%3E%20(schema))

Type Text

Always `text`.

type RefusalContentBlock struct{…}

The refusal content generated by the assistant.

Refusal string

Type Refusal

Always `refusal`.

CreatedAt int64

The Unix timestamp (in seconds) for when the message was created.

formatunixtime

IncompleteAt int64

The Unix timestamp (in seconds) for when the message was marked as incomplete.

formatunixtime

IncompleteDetails MessageIncompleteDetails

On an incomplete message, details about why the message is incomplete.

Reason string

The reason the message is incomplete.

One of the following:

const MessageIncompleteDetailsReasonContentFilter MessageIncompleteDetailsReason = "content\_filter"

const MessageIncompleteDetailsReasonMaxTokens MessageIncompleteDetailsReason = "max\_tokens"

const MessageIncompleteDetailsReasonRunCancelled MessageIncompleteDetailsReason = "run\_cancelled"

const MessageIncompleteDetailsReasonRunExpired MessageIncompleteDetailsReason = "run\_expired"

const MessageIncompleteDetailsReasonRunFailed MessageIncompleteDetailsReason = "run\_failed"

Metadata [Metadata](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

Object ThreadMessage

The object type, which is always `thread.message`.

Role MessageRole

The entity that produced the message. One of `user` or `assistant`.

One of the following:

const MessageRoleUser MessageRole = "user"

const MessageRoleAssistant MessageRole = "assistant"

RunID string

The ID of the [run](https://platform.openai.com/docs/api-reference/runs) associated with the creation of this message. Value is `null` when messages are created manually using the create message or create thread endpoints.

Status MessageStatus

The status of the message, which can be either `in_progress`, `incomplete`, or `completed`.

One of the following:

const MessageStatusInProgress MessageStatus = "in\_progress"

const MessageStatusIncomplete MessageStatus = "incomplete"

const MessageStatusCompleted MessageStatus = "completed"

ThreadID string

The [thread](https://platform.openai.com/docs/api-reference/threads) ID that this message belongs to.

type MessageContentUnion interface{…}

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

One of the following:

type ImageFileContentBlock struct{…}

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

ImageFile [ImageFile](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file%20%3E%20(schema))

Type ImageFile

Always `image_file`.

type ImageURLContentBlock struct{…}

References an image URL in the content of a message.

ImageURL [ImageURL](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url%20%3E%20(schema))

Type ImageURL

The type of the content part.

type TextContentBlock struct{…}

The text content that is part of a message.

Text [Text](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text%20%3E%20(schema))

Type Text

Always `text`.

type RefusalContentBlock struct{…}

The refusal content generated by the assistant.

Refusal string

Type Refusal

Always `refusal`.

type MessageContentDeltaUnion interface{…}

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

One of the following:

type ImageFileDeltaBlock struct{…}

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

Index int64

The index of the content part in the message.

Type ImageFile

Always `image_file`.

ImageFile [ImageFileDelta](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_delta%20%3E%20(schema))Optional

type TextDeltaBlock struct{…}

The text content that is part of a message.

Index int64

The index of the content part in the message.

Type Text

Always `text`.

Text [TextDelta](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text_delta%20%3E%20(schema))Optional

type RefusalDeltaBlock struct{…}

The refusal content that is part of a message.

Index int64

The index of the refusal part in the message.

Type Refusal

Always `refusal`.

Refusal stringOptional

type ImageURLDeltaBlock struct{…}

References an image URL in the content of a message.

Index int64

The index of the content part in the message.

Type ImageURL

Always `image_url`.

ImageURL [ImageURLDelta](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_delta%20%3E%20(schema))Optional

type MessageContentPartParamUnionResp interface{…}

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

One of the following:

type ImageFileContentBlock struct{…}

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

ImageFile [ImageFile](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file%20%3E%20(schema))

Type ImageFile

Always `image_file`.

type ImageURLContentBlock struct{…}

References an image URL in the content of a message.

ImageURL [ImageURL](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url%20%3E%20(schema))

Type ImageURL

The type of the content part.

type TextContentBlockParam struct{…}

The text content that is part of a message.

Text string

Text content to be sent to the model

Type Text

Always `text`.

type MessageDeleted struct{…}

ID string

Deleted bool

Object ThreadMessageDeleted

type MessageDelta struct{…}

The delta containing the fields that have changed on the Message.

Content [][MessageContentDeltaUnion](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_content_delta%20%3E%20(schema))Optional

The content of the message in array of text and/or images.

One of the following:

type ImageFileDeltaBlock struct{…}

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

Index int64

The index of the content part in the message.

Type ImageFile

Always `image_file`.

ImageFile [ImageFileDelta](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_delta%20%3E%20(schema))Optional

type TextDeltaBlock struct{…}

The text content that is part of a message.

Index int64

The index of the content part in the message.

Type Text

Always `text`.

Text [TextDelta](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text_delta%20%3E%20(schema))Optional

type RefusalDeltaBlock struct{…}

The refusal content that is part of a message.

Index int64

The index of the refusal part in the message.

Type Refusal

Always `refusal`.

Refusal stringOptional

type ImageURLDeltaBlock struct{…}

References an image URL in the content of a message.

Index int64

The index of the content part in the message.

Type ImageURL

Always `image_url`.

ImageURL [ImageURLDelta](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_delta%20%3E%20(schema))Optional

Role MessageDeltaRoleOptional

The entity that produced the message. One of `user` or `assistant`.

One of the following:

const MessageDeltaRoleUser MessageDeltaRole = "user"

const MessageDeltaRoleAssistant MessageDeltaRole = "assistant"

type MessageDeltaEvent struct{…}

Represents a message delta i.e. any changed fields on a message during streaming.

ID string

The identifier of the message, which can be referenced in API endpoints.

Delta [MessageDelta](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_delta%20%3E%20(schema))

The delta containing the fields that have changed on the Message.

Object ThreadMessageDelta

The object type, which is always `thread.message.delta`.

type RefusalContentBlock struct{…}

The refusal content generated by the assistant.

Refusal string

Type Refusal

Always `refusal`.

type RefusalDeltaBlock struct{…}

The refusal content that is part of a message.

Index int64

The index of the refusal part in the message.

Type Refusal

Always `refusal`.

Refusal stringOptional

type Text struct{…}

Annotations [][AnnotationUnion](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20annotation%20%3E%20(schema))

One of the following:

type FileCitationAnnotation struct{…}

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

EndIndex int64

minimum0

FileCitation FileCitationAnnotationFileCitation

FileID string

The ID of the specific File the citation is from.

StartIndex int64

minimum0

Text string

The text in the message content that needs to be replaced.

Type FileCitation

Always `file_citation`.

type FilePathAnnotation struct{…}

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

EndIndex int64

minimum0

FilePath FilePathAnnotationFilePath

FileID string

The ID of the file that was generated.

StartIndex int64

minimum0

Text string

The text in the message content that needs to be replaced.

Type FilePath

Always `file_path`.

Value string

The data that makes up the text.

type TextContentBlock struct{…}

The text content that is part of a message.

Text [Text](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text%20%3E%20(schema))

Type Text

Always `text`.

type TextContentBlockParam struct{…}

The text content that is part of a message.

Text string

Text content to be sent to the model

Type Text

Always `text`.

type TextDelta struct{…}

Annotations [][AnnotationDeltaUnion](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20annotation_delta%20%3E%20(schema))Optional

One of the following:

type FileCitationDeltaAnnotation struct{…}

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

Index int64

The index of the annotation in the text content part.

Type FileCitation

Always `file_citation`.

EndIndex int64Optional

minimum0

FileCitation FileCitationDeltaAnnotationFileCitationOptional

FileID stringOptional

The ID of the specific File the citation is from.

Quote stringOptional

The specific quote in the file.

StartIndex int64Optional

minimum0

Text stringOptional

The text in the message content that needs to be replaced.

type FilePathDeltaAnnotation struct{…}

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

Index int64

The index of the annotation in the text content part.

Type FilePath

Always `file_path`.

EndIndex int64Optional

minimum0

FilePath FilePathDeltaAnnotationFilePathOptional

FileID stringOptional

The ID of the file that was generated.

StartIndex int64Optional

minimum0

Text stringOptional

The text in the message content that needs to be replaced.

Value stringOptional

The data that makes up the text.

type TextDeltaBlock struct{…}

The text content that is part of a message.

Index int64

The index of the content part in the message.

Type Text

Always `text`.

Text [TextDelta](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text_delta%20%3E%20(schema))Optional
