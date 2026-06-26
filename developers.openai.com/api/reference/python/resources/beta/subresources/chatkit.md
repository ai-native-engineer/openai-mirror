<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/chatkit/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Beta](/api/reference/python/resources/beta)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# ChatKit

##### ModelsExpand Collapse

class ChatKitWorkflow: …

Workflow metadata and state returned for the session.

id: str

Identifier of the workflow backing the session.

state\_variables: Optional[Dict[str, Union[str, bool, float]]]

State variable key-value pairs applied when invoking the workflow. Defaults to null when no overrides were provided.

One of the following:

str

bool

float

tracing: Tracing

Tracing settings applied to the workflow.

enabled: bool

Indicates whether tracing is enabled.

version: Optional[str]

Specific workflow version used for the session. Defaults to null when using the latest deployment.

#### ChatKitSessions

##### [Cancel chat session](/api/reference/python/resources/beta/subresources/chatkit/subresources/sessions/methods/cancel)

beta.chatkit.sessions.cancel(strsession\_id)  -> [ChatSession](/api/reference/python/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session%20%3E%20(schema))

POST/chatkit/sessions/{session\_id}/cancel

##### [Create ChatKit session](/api/reference/python/resources/beta/subresources/chatkit/subresources/sessions/methods/create)

beta.chatkit.sessions.create(SessionCreateParams\*\*kwargs)  -> [ChatSession](/api/reference/python/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session%20%3E%20(schema))

POST/chatkit/sessions

#### ChatKitThreads

##### [List ChatKit thread items](/api/reference/python/resources/beta/subresources/chatkit/subresources/threads/methods/list_items)

beta.chatkit.threads.list\_items(strthread\_id, ThreadListItemsParams\*\*kwargs)  -> SyncConversationCursorPage[Data]

GET/chatkit/threads/{thread\_id}/items

##### [Retrieve ChatKit thread](/api/reference/python/resources/beta/subresources/chatkit/subresources/threads/methods/retrieve)

beta.chatkit.threads.retrieve(strthread\_id)  -> [ChatKitThread](/api/reference/python/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread%20%3E%20(schema))

GET/chatkit/threads/{thread\_id}

##### [Delete ChatKit thread](/api/reference/python/resources/beta/subresources/chatkit/subresources/threads/methods/delete)

beta.chatkit.threads.delete(strthread\_id)  -> [ThreadDeleteResponse](/api/reference/python/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20thread_delete_response%20%3E%20(schema))

DELETE/chatkit/threads/{thread\_id}

##### [List ChatKit threads](/api/reference/python/resources/beta/subresources/chatkit/subresources/threads/methods/list)

beta.chatkit.threads.list(ThreadListParams\*\*kwargs)  -> SyncConversationCursorPage[[ChatKitThread](/api/reference/python/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread%20%3E%20(schema))]

GET/chatkit/threads

##### ModelsExpand Collapse

class ChatSession: …

Represents a ChatKit session and its resolved configuration.

id: str

Identifier for the ChatKit session.

chatkit\_configuration: [ChatSessionChatKitConfiguration](/api/reference/python/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_chatkit_configuration%20%3E%20(schema))

Resolved ChatKit feature configuration for the session.

client\_secret: str

Ephemeral client secret that authenticates session requests.

expires\_at: int

Unix timestamp (in seconds) for when the session expires.

formatunixtime

max\_requests\_per\_1\_minute: int

Convenience copy of the per-minute request limit.

object: Literal["chatkit.session"]

Type discriminator that is always `chatkit.session`.

rate\_limits: [ChatSessionRateLimits](/api/reference/python/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_rate_limits%20%3E%20(schema))

Resolved rate limit values.

status: [ChatSessionStatus](/api/reference/python/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_status%20%3E%20(schema))

Current lifecycle state of the session.

user: str

User identifier associated with the session.

workflow: [ChatKitWorkflow](/api/reference/python/resources/beta#(resource)%20beta.chatkit%20%3E%20(model)%20chatkit_workflow%20%3E%20(schema))

Workflow metadata for the session.

class ChatSessionAutomaticThreadTitling: …

Automatic thread title preferences for the session.

enabled: bool

Whether automatic thread titling is enabled.

class ChatSessionChatKitConfiguration: …

ChatKit configuration for the session.

automatic\_thread\_titling: [ChatSessionAutomaticThreadTitling](/api/reference/python/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_automatic_thread_titling%20%3E%20(schema))

Automatic thread titling preferences.

file\_upload: [ChatSessionFileUpload](/api/reference/python/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_file_upload%20%3E%20(schema))

Upload settings for the session.

history: [ChatSessionHistory](/api/reference/python/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_history%20%3E%20(schema))

History retention configuration.

class ChatSessionChatKitConfigurationParam: …

Optional per-session configuration settings for ChatKit behavior.

automatic\_thread\_titling: Optional[AutomaticThreadTitling]

Configuration for automatic thread titling. When omitted, automatic thread titling is enabled by default.

enabled: Optional[bool]

Enable automatic thread title generation. Defaults to true.

file\_upload: Optional[FileUpload]

Configuration for upload enablement and limits. When omitted, uploads are disabled by default (max\_files 10, max\_file\_size 512 MB).

enabled: Optional[bool]

Enable uploads for this session. Defaults to false.

max\_file\_size: Optional[int]

Maximum size in megabytes for each uploaded file. Defaults to 512 MB, which is the maximum allowable size.

maximum512

minimum1

max\_files: Optional[int]

Maximum number of files that can be uploaded to the session. Defaults to 10.

minimum1

history: Optional[History]

Configuration for chat history retention. When omitted, history is enabled by default with no limit on recent\_threads (null).

enabled: Optional[bool]

Enables chat users to access previous ChatKit threads. Defaults to true.

recent\_threads: Optional[int]

Number of recent ChatKit threads users have access to. Defaults to unlimited when unset.

minimum1

class ChatSessionExpiresAfterParam: …

Controls when the session expires relative to an anchor timestamp.

anchor: Literal["created\_at"]

Base timestamp used to calculate expiration. Currently fixed to `created_at`.

seconds: int

Number of seconds after the anchor when the session expires.

maximum600

minimum1

formatint64

class ChatSessionFileUpload: …

Upload permissions and limits applied to the session.

enabled: bool

Indicates if uploads are enabled for the session.

max\_file\_size: Optional[int]

Maximum upload size in megabytes.

max\_files: Optional[int]

Maximum number of uploads allowed during the session.

class ChatSessionHistory: …

History retention preferences returned for the session.

enabled: bool

Indicates if chat history is persisted for the session.

recent\_threads: Optional[int]

Number of prior threads surfaced in history views. Defaults to null when all history is retained.

class ChatSessionRateLimits: …

Active per-minute request limit for the session.

max\_requests\_per\_1\_minute: int

Maximum allowed requests per one-minute window.

class ChatSessionRateLimitsParam: …

Controls request rate limits for the session.

max\_requests\_per\_1\_minute: Optional[int]

Maximum number of requests allowed per minute for the session. Defaults to 10.

minimum1

Literal["active", "expired", "cancelled"]

One of the following:

"active"

"expired"

"cancelled"

class ChatSessionWorkflowParam: …

Workflow reference and overrides applied to the chat session.

id: str

Identifier for the workflow invoked by the session.

state\_variables: Optional[Dict[str, Union[str, bool, float]]]

State variables forwarded to the workflow. Keys may be up to 64 characters, values must be primitive types, and the map defaults to an empty object.

One of the following:

str

bool

float

tracing: Optional[Tracing]

Optional tracing overrides for the workflow invocation. When omitted, tracing is enabled by default.

enabled: Optional[bool]

Whether tracing is enabled during the session. Defaults to true.

version: Optional[str]

Specific workflow version to run. Defaults to the latest deployed version.

class ChatKitAttachment: …

Attachment metadata included on thread items.

id: str

Identifier for the attachment.

mime\_type: str

MIME type of the attachment.

name: str

Original display name for the attachment.

preview\_url: Optional[str]

Preview URL for rendering the attachment inline.

formaturi

type: Literal["image", "file"]

Attachment discriminator.

One of the following:

"image"

"file"

class ChatKitResponseOutputText: …

Assistant response text accompanied by optional annotations.

annotations: List[Annotation]

Ordered list of annotations attached to the response text.

One of the following:

class AnnotationFile: …

Annotation that references an uploaded file.

source: AnnotationFileSource

File attachment referenced by the annotation.

filename: str

Filename referenced by the annotation.

type: Literal["file"]

Type discriminator that is always `file`.

type: Literal["file"]

Type discriminator that is always `file` for this annotation.

class AnnotationURL: …

Annotation that references a URL.

source: AnnotationURLSource

URL referenced by the annotation.

type: Literal["url"]

Type discriminator that is always `url`.

url: str

URL referenced by the annotation.

formaturi

type: Literal["url"]

Type discriminator that is always `url` for this annotation.

text: str

Assistant generated text.

type: Literal["output\_text"]

Type discriminator that is always `output_text`.

class ChatKitThread: …

Represents a ChatKit thread and its current status.

id: str

Identifier of the thread.

created\_at: int

Unix timestamp (in seconds) for when the thread was created.

formatunixtime

object: Literal["chatkit.thread"]

Type discriminator that is always `chatkit.thread`.

status: Status

Current status for the thread. Defaults to `active` for newly created threads.

One of the following:

class StatusActive: …

Indicates that a thread is active.

type: Literal["active"]

Status discriminator that is always `active`.

class StatusLocked: …

Indicates that a thread is locked and cannot accept new input.

reason: Optional[str]

Reason that the thread was locked. Defaults to null when no reason is recorded.

type: Literal["locked"]

Status discriminator that is always `locked`.

class StatusClosed: …

Indicates that a thread has been closed.

reason: Optional[str]

Reason that the thread was closed. Defaults to null when no reason is recorded.

type: Literal["closed"]

Status discriminator that is always `closed`.

title: Optional[str]

Optional human-readable title for the thread. Defaults to null when no title has been generated.

user: str

Free-form string that identifies your end user who owns the thread.

class ChatKitThreadAssistantMessageItem: …

Assistant-authored message within a thread.

id: str

Identifier of the thread item.

content: List[[ChatKitResponseOutputText](/api/reference/python/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_response_output_text%20%3E%20(schema))]

Ordered assistant response segments.

annotations: List[Annotation]

Ordered list of annotations attached to the response text.

One of the following:

class AnnotationFile: …

Annotation that references an uploaded file.

source: AnnotationFileSource

File attachment referenced by the annotation.

filename: str

Filename referenced by the annotation.

type: Literal["file"]

Type discriminator that is always `file`.

type: Literal["file"]

Type discriminator that is always `file` for this annotation.

class AnnotationURL: …

Annotation that references a URL.

source: AnnotationURLSource

URL referenced by the annotation.

type: Literal["url"]

Type discriminator that is always `url`.

url: str

URL referenced by the annotation.

formaturi

type: Literal["url"]

Type discriminator that is always `url` for this annotation.

text: str

Assistant generated text.

type: Literal["output\_text"]

Type discriminator that is always `output_text`.

created\_at: int

Unix timestamp (in seconds) for when the item was created.

formatunixtime

object: Literal["chatkit.thread\_item"]

Type discriminator that is always `chatkit.thread_item`.

thread\_id: str

Identifier of the parent thread.

type: Literal["chatkit.assistant\_message"]

Type discriminator that is always `chatkit.assistant_message`.

class ChatKitThreadItemList: …

A paginated list of thread items rendered for the ChatKit API.

data: List[Data]

A list of items

One of the following:

class ChatKitThreadUserMessageItem: …

User-authored messages within a thread.

id: str

Identifier of the thread item.

attachments: List[[ChatKitAttachment](/api/reference/python/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_attachment%20%3E%20(schema))]

Attachments associated with the user message. Defaults to an empty list.

id: str

Identifier for the attachment.

mime\_type: str

MIME type of the attachment.

name: str

Original display name for the attachment.

preview\_url: Optional[str]

Preview URL for rendering the attachment inline.

formaturi

type: Literal["image", "file"]

Attachment discriminator.

One of the following:

"image"

"file"

content: List[Content]

Ordered content elements supplied by the user.

One of the following:

class ContentInputText: …

Text block that a user contributed to the thread.

text: str

Plain-text content supplied by the user.

type: Literal["input\_text"]

Type discriminator that is always `input_text`.

class ContentQuotedText: …

Quoted snippet that the user referenced in their message.

text: str

Quoted text content.

type: Literal["quoted\_text"]

Type discriminator that is always `quoted_text`.

created\_at: int

Unix timestamp (in seconds) for when the item was created.

formatunixtime

inference\_options: Optional[InferenceOptions]

Inference overrides applied to the message. Defaults to null when unset.

model: Optional[str]

Model name that generated the response. Defaults to null when using the session default.

tool\_choice: Optional[InferenceOptionsToolChoice]

Preferred tool to invoke. Defaults to null when ChatKit should auto-select.

id: str

Identifier of the requested tool.

object: Literal["chatkit.thread\_item"]

Type discriminator that is always `chatkit.thread_item`.

thread\_id: str

Identifier of the parent thread.

type: Literal["chatkit.user\_message"]

class ChatKitThreadAssistantMessageItem: …

Assistant-authored message within a thread.

id: str

Identifier of the thread item.

content: List[[ChatKitResponseOutputText](/api/reference/python/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_response_output_text%20%3E%20(schema))]

Ordered assistant response segments.

annotations: List[Annotation]

Ordered list of annotations attached to the response text.

One of the following:

class AnnotationFile: …

Annotation that references an uploaded file.

source: AnnotationFileSource

File attachment referenced by the annotation.

filename: str

Filename referenced by the annotation.

type: Literal["file"]

Type discriminator that is always `file`.

type: Literal["file"]

Type discriminator that is always `file` for this annotation.

class AnnotationURL: …

Annotation that references a URL.

source: AnnotationURLSource

URL referenced by the annotation.

type: Literal["url"]

Type discriminator that is always `url`.

url: str

URL referenced by the annotation.

formaturi

type: Literal["url"]

Type discriminator that is always `url` for this annotation.

text: str

Assistant generated text.

type: Literal["output\_text"]

Type discriminator that is always `output_text`.

created\_at: int

Unix timestamp (in seconds) for when the item was created.

formatunixtime

object: Literal["chatkit.thread\_item"]

Type discriminator that is always `chatkit.thread_item`.

thread\_id: str

Identifier of the parent thread.

type: Literal["chatkit.assistant\_message"]

Type discriminator that is always `chatkit.assistant_message`.

class ChatKitWidgetItem: …

Thread item that renders a widget payload.

id: str

Identifier of the thread item.

created\_at: int

Unix timestamp (in seconds) for when the item was created.

formatunixtime

object: Literal["chatkit.thread\_item"]

Type discriminator that is always `chatkit.thread_item`.

thread\_id: str

Identifier of the parent thread.

type: Literal["chatkit.widget"]

Type discriminator that is always `chatkit.widget`.

widget: str

Serialized widget payload rendered in the UI.

class DataChatKitClientToolCall: …

Record of a client side tool invocation initiated by the assistant.

id: str

Identifier of the thread item.

arguments: str

JSON-encoded arguments that were sent to the tool.

call\_id: str

Identifier for the client tool call.

created\_at: int

Unix timestamp (in seconds) for when the item was created.

formatunixtime

name: str

Tool name that was invoked.

object: Literal["chatkit.thread\_item"]

Type discriminator that is always `chatkit.thread_item`.

output: Optional[str]

JSON-encoded output captured from the tool. Defaults to null while execution is in progress.

status: Literal["in\_progress", "completed"]

Execution status for the tool call.

One of the following:

"in\_progress"

"completed"

thread\_id: str

Identifier of the parent thread.

type: Literal["chatkit.client\_tool\_call"]

Type discriminator that is always `chatkit.client_tool_call`.

class DataChatKitTask: …

Task emitted by the workflow to show progress and status updates.

id: str

Identifier of the thread item.

created\_at: int

Unix timestamp (in seconds) for when the item was created.

formatunixtime

heading: Optional[str]

Optional heading for the task. Defaults to null when not provided.

object: Literal["chatkit.thread\_item"]

Type discriminator that is always `chatkit.thread_item`.

summary: Optional[str]

Optional summary that describes the task. Defaults to null when omitted.

task\_type: Literal["custom", "thought"]

Subtype for the task.

One of the following:

"custom"

"thought"

thread\_id: str

Identifier of the parent thread.

type: Literal["chatkit.task"]

Type discriminator that is always `chatkit.task`.

class DataChatKitTaskGroup: …

Collection of workflow tasks grouped together in the thread.

id: str

Identifier of the thread item.

created\_at: int

Unix timestamp (in seconds) for when the item was created.

formatunixtime

object: Literal["chatkit.thread\_item"]

Type discriminator that is always `chatkit.thread_item`.

tasks: List[DataChatKitTaskGroupTask]

Tasks included in the group.

heading: Optional[str]

Optional heading for the grouped task. Defaults to null when not provided.

summary: Optional[str]

Optional summary that describes the grouped task. Defaults to null when omitted.

type: Literal["custom", "thought"]

Subtype for the grouped task.

One of the following:

"custom"

"thought"

thread\_id: str

Identifier of the parent thread.

type: Literal["chatkit.task\_group"]

Type discriminator that is always `chatkit.task_group`.

first\_id: Optional[str]

The ID of the first item in the list.

has\_more: bool

Whether there are more items available.

last\_id: Optional[str]

The ID of the last item in the list.

object: Literal["list"]

The type of object returned, must be `list`.

class ChatKitThreadUserMessageItem: …

User-authored messages within a thread.

id: str

Identifier of the thread item.

attachments: List[[ChatKitAttachment](/api/reference/python/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_attachment%20%3E%20(schema))]

Attachments associated with the user message. Defaults to an empty list.

id: str

Identifier for the attachment.

mime\_type: str

MIME type of the attachment.

name: str

Original display name for the attachment.

preview\_url: Optional[str]

Preview URL for rendering the attachment inline.

formaturi

type: Literal["image", "file"]

Attachment discriminator.

One of the following:

"image"

"file"

content: List[Content]

Ordered content elements supplied by the user.

One of the following:

class ContentInputText: …

Text block that a user contributed to the thread.

text: str

Plain-text content supplied by the user.

type: Literal["input\_text"]

Type discriminator that is always `input_text`.

class ContentQuotedText: …

Quoted snippet that the user referenced in their message.

text: str

Quoted text content.

type: Literal["quoted\_text"]

Type discriminator that is always `quoted_text`.

created\_at: int

Unix timestamp (in seconds) for when the item was created.

formatunixtime

inference\_options: Optional[InferenceOptions]

Inference overrides applied to the message. Defaults to null when unset.

model: Optional[str]

Model name that generated the response. Defaults to null when using the session default.

tool\_choice: Optional[InferenceOptionsToolChoice]

Preferred tool to invoke. Defaults to null when ChatKit should auto-select.

id: str

Identifier of the requested tool.

object: Literal["chatkit.thread\_item"]

Type discriminator that is always `chatkit.thread_item`.

thread\_id: str

Identifier of the parent thread.

type: Literal["chatkit.user\_message"]

class ChatKitWidgetItem: …

Thread item that renders a widget payload.

id: str

Identifier of the thread item.

created\_at: int

Unix timestamp (in seconds) for when the item was created.

formatunixtime

object: Literal["chatkit.thread\_item"]

Type discriminator that is always `chatkit.thread_item`.

thread\_id: str

Identifier of the parent thread.

type: Literal["chatkit.widget"]

Type discriminator that is always `chatkit.widget`.

widget: str

Serialized widget payload rendered in the UI.

class ThreadDeleteResponse: …

Confirmation payload returned after deleting a thread.

id: str

Identifier of the deleted thread.

deleted: bool

Indicates that the thread has been deleted.

object: Literal["chatkit.thread.deleted"]

Type discriminator that is always `chatkit.thread.deleted`.
