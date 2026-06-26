<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/chatkit/subresources/threads/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Beta](/api/reference/java/resources/beta)

[ChatKit](/api/reference/java/resources/beta/subresources/chatkit)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Threads

##### [List ChatKit thread items](/api/reference/java/resources/beta/subresources/chatkit/subresources/threads/methods/list_items)

ThreadListItemsPage beta().chatkit().threads().listItems(ThreadListItemsParamsparams = ThreadListItemsParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/chatkit/threads/{thread\_id}/items

##### [Retrieve ChatKit thread](/api/reference/java/resources/beta/subresources/chatkit/subresources/threads/methods/retrieve)

[ChatKitThread](/api/reference/java/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread%20%3E%20(schema)) beta().chatkit().threads().retrieve(ThreadRetrieveParamsparams = ThreadRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/chatkit/threads/{thread\_id}

##### [Delete ChatKit thread](/api/reference/java/resources/beta/subresources/chatkit/subresources/threads/methods/delete)

[ThreadDeleteResponse](/api/reference/java/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20ThreadDeleteResponse%20%3E%20(schema)) beta().chatkit().threads().delete(ThreadDeleteParamsparams = ThreadDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/chatkit/threads/{thread\_id}

##### [List ChatKit threads](/api/reference/java/resources/beta/subresources/chatkit/subresources/threads/methods/list)

ThreadListPage beta().chatkit().threads().list(ThreadListParamsparams = ThreadListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/chatkit/threads

##### ModelsExpand Collapse

class ChatSession:

Represents a ChatKit session and its resolved configuration.

String id

Identifier for the ChatKit session.

[ChatSessionChatKitConfiguration](/api/reference/java/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_chatkit_configuration%20%3E%20(schema)) chatkitConfiguration

Resolved ChatKit feature configuration for the session.

String clientSecret

Ephemeral client secret that authenticates session requests.

long expiresAt

Unix timestamp (in seconds) for when the session expires.

formatunixtime

long maxRequestsPer1Minute

Convenience copy of the per-minute request limit.

JsonValue; object\_ "chatkit.session"constant"chatkit.session"constant

Type discriminator that is always `chatkit.session`.

[ChatSessionRateLimits](/api/reference/java/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_rate_limits%20%3E%20(schema)) rateLimits

Resolved rate limit values.

[ChatSessionStatus](/api/reference/java/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_status%20%3E%20(schema)) status

Current lifecycle state of the session.

String user

User identifier associated with the session.

[ChatKitWorkflow](/api/reference/java/resources/beta#(resource)%20beta.chatkit%20%3E%20(model)%20chatkit_workflow%20%3E%20(schema)) workflow

Workflow metadata for the session.

class ChatSessionAutomaticThreadTitling:

Automatic thread title preferences for the session.

boolean enabled

Whether automatic thread titling is enabled.

class ChatSessionChatKitConfiguration:

ChatKit configuration for the session.

[ChatSessionAutomaticThreadTitling](/api/reference/java/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_automatic_thread_titling%20%3E%20(schema)) automaticThreadTitling

Automatic thread titling preferences.

[ChatSessionFileUpload](/api/reference/java/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_file_upload%20%3E%20(schema)) fileUpload

Upload settings for the session.

[ChatSessionHistory](/api/reference/java/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_history%20%3E%20(schema)) history

History retention configuration.

class ChatSessionChatKitConfigurationParam:

Optional per-session configuration settings for ChatKit behavior.

Optional<AutomaticThreadTitling> automaticThreadTitling

Configuration for automatic thread titling. When omitted, automatic thread titling is enabled by default.

Optional<Boolean> enabled

Enable automatic thread title generation. Defaults to true.

Optional<FileUpload> fileUpload

Configuration for upload enablement and limits. When omitted, uploads are disabled by default (max\_files 10, max\_file\_size 512 MB).

Optional<Boolean> enabled

Enable uploads for this session. Defaults to false.

Optional<Long> maxFileSize

Maximum size in megabytes for each uploaded file. Defaults to 512 MB, which is the maximum allowable size.

maximum512

minimum1

Optional<Long> maxFiles

Maximum number of files that can be uploaded to the session. Defaults to 10.

minimum1

Optional<History> history

Configuration for chat history retention. When omitted, history is enabled by default with no limit on recent\_threads (null).

Optional<Boolean> enabled

Enables chat users to access previous ChatKit threads. Defaults to true.

Optional<Long> recentThreads

Number of recent ChatKit threads users have access to. Defaults to unlimited when unset.

minimum1

class ChatSessionExpiresAfterParam:

Controls when the session expires relative to an anchor timestamp.

JsonValue; anchor "created\_at"constant"created\_at"constant

Base timestamp used to calculate expiration. Currently fixed to `created_at`.

long seconds

Number of seconds after the anchor when the session expires.

maximum600

minimum1

formatint64

class ChatSessionFileUpload:

Upload permissions and limits applied to the session.

boolean enabled

Indicates if uploads are enabled for the session.

Optional<Long> maxFileSize

Maximum upload size in megabytes.

Optional<Long> maxFiles

Maximum number of uploads allowed during the session.

class ChatSessionHistory:

History retention preferences returned for the session.

boolean enabled

Indicates if chat history is persisted for the session.

Optional<Long> recentThreads

Number of prior threads surfaced in history views. Defaults to null when all history is retained.

class ChatSessionRateLimits:

Active per-minute request limit for the session.

long maxRequestsPer1Minute

Maximum allowed requests per one-minute window.

class ChatSessionRateLimitsParam:

Controls request rate limits for the session.

Optional<Long> maxRequestsPer1Minute

Maximum number of requests allowed per minute for the session. Defaults to 10.

minimum1

enum ChatSessionStatus:

ACTIVE("active")

EXPIRED("expired")

CANCELLED("cancelled")

class ChatSessionWorkflowParam:

Workflow reference and overrides applied to the chat session.

String id

Identifier for the workflow invoked by the session.

Optional<StateVariables> stateVariables

State variables forwarded to the workflow. Keys may be up to 64 characters, values must be primitive types, and the map defaults to an empty object.

One of the following:

String

boolean

double

Optional<Tracing> tracing

Optional tracing overrides for the workflow invocation. When omitted, tracing is enabled by default.

Optional<Boolean> enabled

Whether tracing is enabled during the session. Defaults to true.

Optional<String> version

Specific workflow version to run. Defaults to the latest deployed version.

class ChatKitAttachment:

Attachment metadata included on thread items.

String id

Identifier for the attachment.

String mimeType

MIME type of the attachment.

String name

Original display name for the attachment.

Optional<String> previewUrl

Preview URL for rendering the attachment inline.

formaturi

Type type

Attachment discriminator.

One of the following:

IMAGE("image")

FILE("file")

class ChatKitResponseOutputText:

Assistant response text accompanied by optional annotations.

List<Annotation> annotations

Ordered list of annotations attached to the response text.

One of the following:

class File:

Annotation that references an uploaded file.

Source source

File attachment referenced by the annotation.

String filename

Filename referenced by the annotation.

JsonValue; type "file"constant"file"constant

Type discriminator that is always `file`.

JsonValue; type "file"constant"file"constant

Type discriminator that is always `file` for this annotation.

class Url:

Annotation that references a URL.

Source source

URL referenced by the annotation.

JsonValue; type "url"constant"url"constant

Type discriminator that is always `url`.

String url

URL referenced by the annotation.

formaturi

JsonValue; type "url"constant"url"constant

Type discriminator that is always `url` for this annotation.

String text

Assistant generated text.

JsonValue; type "output\_text"constant"output\_text"constant

Type discriminator that is always `output_text`.

class ChatKitThread:

Represents a ChatKit thread and its current status.

String id

Identifier of the thread.

long createdAt

Unix timestamp (in seconds) for when the thread was created.

formatunixtime

JsonValue; object\_ "chatkit.thread"constant"chatkit.thread"constant

Type discriminator that is always `chatkit.thread`.

Status status

Current status for the thread. Defaults to `active` for newly created threads.

One of the following:

JsonValue;

JsonValue; type "active"constant"active"constant

Status discriminator that is always `active`.

class Locked:

Indicates that a thread is locked and cannot accept new input.

Optional<String> reason

Reason that the thread was locked. Defaults to null when no reason is recorded.

JsonValue; type "locked"constant"locked"constant

Status discriminator that is always `locked`.

class Closed:

Indicates that a thread has been closed.

Optional<String> reason

Reason that the thread was closed. Defaults to null when no reason is recorded.

JsonValue; type "closed"constant"closed"constant

Status discriminator that is always `closed`.

Optional<String> title

Optional human-readable title for the thread. Defaults to null when no title has been generated.

String user

Free-form string that identifies your end user who owns the thread.

class ChatKitThreadAssistantMessageItem:

Assistant-authored message within a thread.

String id

Identifier of the thread item.

List<[ChatKitResponseOutputText](/api/reference/java/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_response_output_text%20%3E%20(schema))> content

Ordered assistant response segments.

List<Annotation> annotations

Ordered list of annotations attached to the response text.

One of the following:

class File:

Annotation that references an uploaded file.

Source source

File attachment referenced by the annotation.

String filename

Filename referenced by the annotation.

JsonValue; type "file"constant"file"constant

Type discriminator that is always `file`.

JsonValue; type "file"constant"file"constant

Type discriminator that is always `file` for this annotation.

class Url:

Annotation that references a URL.

Source source

URL referenced by the annotation.

JsonValue; type "url"constant"url"constant

Type discriminator that is always `url`.

String url

URL referenced by the annotation.

formaturi

JsonValue; type "url"constant"url"constant

Type discriminator that is always `url` for this annotation.

String text

Assistant generated text.

JsonValue; type "output\_text"constant"output\_text"constant

Type discriminator that is always `output_text`.

long createdAt

Unix timestamp (in seconds) for when the item was created.

formatunixtime

JsonValue; object\_ "chatkit.thread\_item"constant"chatkit.thread\_item"constant

Type discriminator that is always `chatkit.thread_item`.

String threadId

Identifier of the parent thread.

JsonValue; type "chatkit.assistant\_message"constant"chatkit.assistant\_message"constant

Type discriminator that is always `chatkit.assistant_message`.

class ChatKitThreadItemList:

A paginated list of thread items rendered for the ChatKit API.

List<Data> data

A list of items

One of the following:

class ChatKitThreadUserMessageItem:

User-authored messages within a thread.

String id

Identifier of the thread item.

List<[ChatKitAttachment](/api/reference/java/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_attachment%20%3E%20(schema))> attachments

Attachments associated with the user message. Defaults to an empty list.

String id

Identifier for the attachment.

String mimeType

MIME type of the attachment.

String name

Original display name for the attachment.

Optional<String> previewUrl

Preview URL for rendering the attachment inline.

formaturi

Type type

Attachment discriminator.

One of the following:

IMAGE("image")

FILE("file")

List<Content> content

Ordered content elements supplied by the user.

One of the following:

class InputText:

Text block that a user contributed to the thread.

String text

Plain-text content supplied by the user.

JsonValue; type "input\_text"constant"input\_text"constant

Type discriminator that is always `input_text`.

class QuotedText:

Quoted snippet that the user referenced in their message.

String text

Quoted text content.

JsonValue; type "quoted\_text"constant"quoted\_text"constant

Type discriminator that is always `quoted_text`.

long createdAt

Unix timestamp (in seconds) for when the item was created.

formatunixtime

Optional<InferenceOptions> inferenceOptions

Inference overrides applied to the message. Defaults to null when unset.

Optional<String> model

Model name that generated the response. Defaults to null when using the session default.

Optional<ToolChoice> toolChoice

Preferred tool to invoke. Defaults to null when ChatKit should auto-select.

String id

Identifier of the requested tool.

JsonValue; object\_ "chatkit.thread\_item"constant"chatkit.thread\_item"constant

Type discriminator that is always `chatkit.thread_item`.

String threadId

Identifier of the parent thread.

JsonValue; type "chatkit.user\_message"constant"chatkit.user\_message"constant

class ChatKitThreadAssistantMessageItem:

Assistant-authored message within a thread.

String id

Identifier of the thread item.

List<[ChatKitResponseOutputText](/api/reference/java/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_response_output_text%20%3E%20(schema))> content

Ordered assistant response segments.

List<Annotation> annotations

Ordered list of annotations attached to the response text.

One of the following:

class File:

Annotation that references an uploaded file.

Source source

File attachment referenced by the annotation.

String filename

Filename referenced by the annotation.

JsonValue; type "file"constant"file"constant

Type discriminator that is always `file`.

JsonValue; type "file"constant"file"constant

Type discriminator that is always `file` for this annotation.

class Url:

Annotation that references a URL.

Source source

URL referenced by the annotation.

JsonValue; type "url"constant"url"constant

Type discriminator that is always `url`.

String url

URL referenced by the annotation.

formaturi

JsonValue; type "url"constant"url"constant

Type discriminator that is always `url` for this annotation.

String text

Assistant generated text.

JsonValue; type "output\_text"constant"output\_text"constant

Type discriminator that is always `output_text`.

long createdAt

Unix timestamp (in seconds) for when the item was created.

formatunixtime

JsonValue; object\_ "chatkit.thread\_item"constant"chatkit.thread\_item"constant

Type discriminator that is always `chatkit.thread_item`.

String threadId

Identifier of the parent thread.

JsonValue; type "chatkit.assistant\_message"constant"chatkit.assistant\_message"constant

Type discriminator that is always `chatkit.assistant_message`.

class ChatKitWidgetItem:

Thread item that renders a widget payload.

String id

Identifier of the thread item.

long createdAt

Unix timestamp (in seconds) for when the item was created.

formatunixtime

JsonValue; object\_ "chatkit.thread\_item"constant"chatkit.thread\_item"constant

Type discriminator that is always `chatkit.thread_item`.

String threadId

Identifier of the parent thread.

JsonValue; type "chatkit.widget"constant"chatkit.widget"constant

Type discriminator that is always `chatkit.widget`.

String widget

Serialized widget payload rendered in the UI.

class ChatKitClientToolCall:

Record of a client side tool invocation initiated by the assistant.

String id

Identifier of the thread item.

String arguments

JSON-encoded arguments that were sent to the tool.

String callId

Identifier for the client tool call.

long createdAt

Unix timestamp (in seconds) for when the item was created.

formatunixtime

String name

Tool name that was invoked.

JsonValue; object\_ "chatkit.thread\_item"constant"chatkit.thread\_item"constant

Type discriminator that is always `chatkit.thread_item`.

Optional<String> output

JSON-encoded output captured from the tool. Defaults to null while execution is in progress.

Status status

Execution status for the tool call.

One of the following:

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

String threadId

Identifier of the parent thread.

JsonValue; type "chatkit.client\_tool\_call"constant"chatkit.client\_tool\_call"constant

Type discriminator that is always `chatkit.client_tool_call`.

class ChatKitTask:

Task emitted by the workflow to show progress and status updates.

String id

Identifier of the thread item.

long createdAt

Unix timestamp (in seconds) for when the item was created.

formatunixtime

Optional<String> heading

Optional heading for the task. Defaults to null when not provided.

JsonValue; object\_ "chatkit.thread\_item"constant"chatkit.thread\_item"constant

Type discriminator that is always `chatkit.thread_item`.

Optional<String> summary

Optional summary that describes the task. Defaults to null when omitted.

TaskType taskType

Subtype for the task.

One of the following:

CUSTOM("custom")

THOUGHT("thought")

String threadId

Identifier of the parent thread.

JsonValue; type "chatkit.task"constant"chatkit.task"constant

Type discriminator that is always `chatkit.task`.

class ChatKitTaskGroup:

Collection of workflow tasks grouped together in the thread.

String id

Identifier of the thread item.

long createdAt

Unix timestamp (in seconds) for when the item was created.

formatunixtime

JsonValue; object\_ "chatkit.thread\_item"constant"chatkit.thread\_item"constant

Type discriminator that is always `chatkit.thread_item`.

List<Task> tasks

Tasks included in the group.

Optional<String> heading

Optional heading for the grouped task. Defaults to null when not provided.

Optional<String> summary

Optional summary that describes the grouped task. Defaults to null when omitted.

Type type

Subtype for the grouped task.

One of the following:

CUSTOM("custom")

THOUGHT("thought")

String threadId

Identifier of the parent thread.

JsonValue; type "chatkit.task\_group"constant"chatkit.task\_group"constant

Type discriminator that is always `chatkit.task_group`.

Optional<String> firstId

The ID of the first item in the list.

boolean hasMore

Whether there are more items available.

Optional<String> lastId

The ID of the last item in the list.

JsonValue; object\_ "list"constant"list"constant

The type of object returned, must be `list`.

class ChatKitThreadUserMessageItem:

User-authored messages within a thread.

String id

Identifier of the thread item.

List<[ChatKitAttachment](/api/reference/java/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_attachment%20%3E%20(schema))> attachments

Attachments associated with the user message. Defaults to an empty list.

String id

Identifier for the attachment.

String mimeType

MIME type of the attachment.

String name

Original display name for the attachment.

Optional<String> previewUrl

Preview URL for rendering the attachment inline.

formaturi

Type type

Attachment discriminator.

One of the following:

IMAGE("image")

FILE("file")

List<Content> content

Ordered content elements supplied by the user.

One of the following:

class InputText:

Text block that a user contributed to the thread.

String text

Plain-text content supplied by the user.

JsonValue; type "input\_text"constant"input\_text"constant

Type discriminator that is always `input_text`.

class QuotedText:

Quoted snippet that the user referenced in their message.

String text

Quoted text content.

JsonValue; type "quoted\_text"constant"quoted\_text"constant

Type discriminator that is always `quoted_text`.

long createdAt

Unix timestamp (in seconds) for when the item was created.

formatunixtime

Optional<InferenceOptions> inferenceOptions

Inference overrides applied to the message. Defaults to null when unset.

Optional<String> model

Model name that generated the response. Defaults to null when using the session default.

Optional<ToolChoice> toolChoice

Preferred tool to invoke. Defaults to null when ChatKit should auto-select.

String id

Identifier of the requested tool.

JsonValue; object\_ "chatkit.thread\_item"constant"chatkit.thread\_item"constant

Type discriminator that is always `chatkit.thread_item`.

String threadId

Identifier of the parent thread.

JsonValue; type "chatkit.user\_message"constant"chatkit.user\_message"constant

class ChatKitWidgetItem:

Thread item that renders a widget payload.

String id

Identifier of the thread item.

long createdAt

Unix timestamp (in seconds) for when the item was created.

formatunixtime

JsonValue; object\_ "chatkit.thread\_item"constant"chatkit.thread\_item"constant

Type discriminator that is always `chatkit.thread_item`.

String threadId

Identifier of the parent thread.

JsonValue; type "chatkit.widget"constant"chatkit.widget"constant

Type discriminator that is always `chatkit.widget`.

String widget

Serialized widget payload rendered in the UI.
