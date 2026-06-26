<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/chatkit/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Beta](/api/reference/go/resources/beta)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# ChatKit

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

#### ChatKitSessions

##### [Cancel chat session](/api/reference/go/resources/beta/subresources/chatkit/subresources/sessions/methods/cancel)

client.Beta.ChatKit.Sessions.Cancel(ctx, sessionID) (\*[ChatSession](/api/reference/go/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session%20%3E%20(schema)), error)

POST/chatkit/sessions/{session\_id}/cancel

##### [Create ChatKit session](/api/reference/go/resources/beta/subresources/chatkit/subresources/sessions/methods/create)

client.Beta.ChatKit.Sessions.New(ctx, body) (\*[ChatSession](/api/reference/go/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session%20%3E%20(schema)), error)

POST/chatkit/sessions

#### ChatKitThreads

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
