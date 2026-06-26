<!-- source: https://developers.openai.com/api/reference/ruby/resources/beta/subresources/chatkit/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Beta](/api/reference/ruby/resources/beta)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# ChatKit

##### ModelsExpand Collapse

class ChatKitWorkflow { id, state\_variables, tracing, version }

Workflow metadata and state returned for the session.

id: String

Identifier of the workflow backing the session.

state\_variables: Hash[Symbol, String | bool | Float]

State variable key-value pairs applied when invoking the workflow. Defaults to null when no overrides were provided.

One of the following:

String = String

UnionMember1 = bool

Float = Float

tracing: Tracing{ enabled}

Tracing settings applied to the workflow.

enabled: bool

Indicates whether tracing is enabled.

version: String

Specific workflow version used for the session. Defaults to null when using the latest deployment.

#### ChatKitSessions

##### [Cancel chat session](/api/reference/ruby/resources/beta/subresources/chatkit/subresources/sessions/methods/cancel)

beta.chatkit.sessions.cancel(session\_id) -> [ChatSession](/api/reference/ruby/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session%20%3E%20(schema)) { id, chatkit\_configuration, client\_secret, 7 more }

POST/chatkit/sessions/{session\_id}/cancel

##### [Create ChatKit session](/api/reference/ruby/resources/beta/subresources/chatkit/subresources/sessions/methods/create)

beta.chatkit.sessions.create(\*\*kwargs) -> [ChatSession](/api/reference/ruby/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session%20%3E%20(schema)) { id, chatkit\_configuration, client\_secret, 7 more }

POST/chatkit/sessions

#### ChatKitThreads

##### [List ChatKit thread items](/api/reference/ruby/resources/beta/subresources/chatkit/subresources/threads/methods/list_items)

beta.chatkit.threads.list\_items(thread\_id, \*\*kwargs) -> ConversationCursorPage<[ChatKitThreadUserMessageItem](/api/reference/ruby/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_user_message_item%20%3E%20(schema)) { id, attachments, content, 5 more }  | [ChatKitThreadAssistantMessageItem](/api/reference/ruby/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_assistant_message_item%20%3E%20(schema)) { id, content, created\_at, 3 more }  | [ChatKitWidgetItem](/api/reference/ruby/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_widget_item%20%3E%20(schema)) { id, created\_at, object, 3 more }  | 3 more>

GET/chatkit/threads/{thread\_id}/items

##### [Retrieve ChatKit thread](/api/reference/ruby/resources/beta/subresources/chatkit/subresources/threads/methods/retrieve)

beta.chatkit.threads.retrieve(thread\_id) -> [ChatKitThread](/api/reference/ruby/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread%20%3E%20(schema)) { id, created\_at, object, 3 more }

GET/chatkit/threads/{thread\_id}

##### [Delete ChatKit thread](/api/reference/ruby/resources/beta/subresources/chatkit/subresources/threads/methods/delete)

beta.chatkit.threads.delete(thread\_id) -> [ThreadDeleteResponse](/api/reference/ruby/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20thread_delete_response%20%3E%20(schema)) { id, deleted, object }

DELETE/chatkit/threads/{thread\_id}

##### [List ChatKit threads](/api/reference/ruby/resources/beta/subresources/chatkit/subresources/threads/methods/list)

beta.chatkit.threads.list(\*\*kwargs) -> ConversationCursorPage<[ChatKitThread](/api/reference/ruby/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread%20%3E%20(schema)) { id, created\_at, object, 3 more } >

GET/chatkit/threads

##### ModelsExpand Collapse

class ChatSession { id, chatkit\_configuration, client\_secret, 7 more }

Represents a ChatKit session and its resolved configuration.

id: String

Identifier for the ChatKit session.

chatkit\_configuration: [ChatSessionChatKitConfiguration](/api/reference/ruby/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_chatkit_configuration%20%3E%20(schema)) { automatic\_thread\_titling, file\_upload, history }

Resolved ChatKit feature configuration for the session.

client\_secret: String

Ephemeral client secret that authenticates session requests.

expires\_at: Integer

Unix timestamp (in seconds) for when the session expires.

formatunixtime

max\_requests\_per\_1\_minute: Integer

Convenience copy of the per-minute request limit.

object: :"chatkit.session"

Type discriminator that is always `chatkit.session`.

rate\_limits: [ChatSessionRateLimits](/api/reference/ruby/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_rate_limits%20%3E%20(schema)) { max\_requests\_per\_1\_minute }

Resolved rate limit values.

status: [ChatSessionStatus](/api/reference/ruby/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_status%20%3E%20(schema))

Current lifecycle state of the session.

user: String

User identifier associated with the session.

workflow: [ChatKitWorkflow](/api/reference/ruby/resources/beta#(resource)%20beta.chatkit%20%3E%20(model)%20chatkit_workflow%20%3E%20(schema)) { id, state\_variables, tracing, version }

Workflow metadata for the session.

class ChatSessionAutomaticThreadTitling { enabled }

Automatic thread title preferences for the session.

enabled: bool

Whether automatic thread titling is enabled.

class ChatSessionChatKitConfiguration { automatic\_thread\_titling, file\_upload, history }

ChatKit configuration for the session.

automatic\_thread\_titling: [ChatSessionAutomaticThreadTitling](/api/reference/ruby/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_automatic_thread_titling%20%3E%20(schema)) { enabled }

Automatic thread titling preferences.

file\_upload: [ChatSessionFileUpload](/api/reference/ruby/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_file_upload%20%3E%20(schema)) { enabled, max\_file\_size, max\_files }

Upload settings for the session.

history: [ChatSessionHistory](/api/reference/ruby/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_history%20%3E%20(schema)) { enabled, recent\_threads }

History retention configuration.

class ChatSessionChatKitConfigurationParam { automatic\_thread\_titling, file\_upload, history }

Optional per-session configuration settings for ChatKit behavior.

automatic\_thread\_titling: AutomaticThreadTitling{ enabled}

Configuration for automatic thread titling. When omitted, automatic thread titling is enabled by default.

enabled: bool

Enable automatic thread title generation. Defaults to true.

file\_upload: FileUpload{ enabled, max\_file\_size, max\_files}

Configuration for upload enablement and limits. When omitted, uploads are disabled by default (max\_files 10, max\_file\_size 512 MB).

enabled: bool

Enable uploads for this session. Defaults to false.

max\_file\_size: Integer

Maximum size in megabytes for each uploaded file. Defaults to 512 MB, which is the maximum allowable size.

maximum512

minimum1

max\_files: Integer

Maximum number of files that can be uploaded to the session. Defaults to 10.

minimum1

history: History{ enabled, recent\_threads}

Configuration for chat history retention. When omitted, history is enabled by default with no limit on recent\_threads (null).

enabled: bool

Enables chat users to access previous ChatKit threads. Defaults to true.

recent\_threads: Integer

Number of recent ChatKit threads users have access to. Defaults to unlimited when unset.

minimum1

class ChatSessionExpiresAfterParam { anchor, seconds }

Controls when the session expires relative to an anchor timestamp.

anchor: :created\_at

Base timestamp used to calculate expiration. Currently fixed to `created_at`.

seconds: Integer

Number of seconds after the anchor when the session expires.

maximum600

minimum1

formatint64

class ChatSessionFileUpload { enabled, max\_file\_size, max\_files }

Upload permissions and limits applied to the session.

enabled: bool

Indicates if uploads are enabled for the session.

max\_file\_size: Integer

Maximum upload size in megabytes.

max\_files: Integer

Maximum number of uploads allowed during the session.

class ChatSessionHistory { enabled, recent\_threads }

History retention preferences returned for the session.

enabled: bool

Indicates if chat history is persisted for the session.

recent\_threads: Integer

Number of prior threads surfaced in history views. Defaults to null when all history is retained.

class ChatSessionRateLimits { max\_requests\_per\_1\_minute }

Active per-minute request limit for the session.

max\_requests\_per\_1\_minute: Integer

Maximum allowed requests per one-minute window.

class ChatSessionRateLimitsParam { max\_requests\_per\_1\_minute }

Controls request rate limits for the session.

max\_requests\_per\_1\_minute: Integer

Maximum number of requests allowed per minute for the session. Defaults to 10.

minimum1

ChatSessionStatus = :active | :expired | :cancelled

One of the following:

:active

:expired

:cancelled

class ChatSessionWorkflowParam { id, state\_variables, tracing, version }

Workflow reference and overrides applied to the chat session.

id: String

Identifier for the workflow invoked by the session.

state\_variables: Hash[Symbol, String | bool | Float]

State variables forwarded to the workflow. Keys may be up to 64 characters, values must be primitive types, and the map defaults to an empty object.

One of the following:

String = String

UnionMember1 = bool

Float = Float

tracing: Tracing{ enabled}

Optional tracing overrides for the workflow invocation. When omitted, tracing is enabled by default.

enabled: bool

Whether tracing is enabled during the session. Defaults to true.

version: String

Specific workflow version to run. Defaults to the latest deployed version.

class ChatKitAttachment { id, mime\_type, name, 2 more }

Attachment metadata included on thread items.

id: String

Identifier for the attachment.

mime\_type: String

MIME type of the attachment.

name: String

Original display name for the attachment.

preview\_url: String

Preview URL for rendering the attachment inline.

formaturi

type: :image | :file

Attachment discriminator.

One of the following:

:image

:file

class ChatKitResponseOutputText { annotations, text, type }

Assistant response text accompanied by optional annotations.

annotations: Array[File{ source, type} | URL{ source, type}]

Ordered list of annotations attached to the response text.

One of the following:

class File { source, type }

Annotation that references an uploaded file.

source: Source{ filename, type}

File attachment referenced by the annotation.

filename: String

Filename referenced by the annotation.

type: :file

Type discriminator that is always `file`.

type: :file

Type discriminator that is always `file` for this annotation.

class URL { source, type }

Annotation that references a URL.

source: Source{ type, url}

URL referenced by the annotation.

type: :url

Type discriminator that is always `url`.

url: String

URL referenced by the annotation.

formaturi

type: :url

Type discriminator that is always `url` for this annotation.

text: String

Assistant generated text.

type: :output\_text

Type discriminator that is always `output_text`.

class ChatKitThread { id, created\_at, object, 3 more }

Represents a ChatKit thread and its current status.

id: String

Identifier of the thread.

created\_at: Integer

Unix timestamp (in seconds) for when the thread was created.

formatunixtime

object: :"chatkit.thread"

Type discriminator that is always `chatkit.thread`.

status: Active{ type} | Locked{ reason, type} | Closed{ reason, type}

Current status for the thread. Defaults to `active` for newly created threads.

One of the following:

class Active { type }

Indicates that a thread is active.

type: :active

Status discriminator that is always `active`.

class Locked { reason, type }

Indicates that a thread is locked and cannot accept new input.

reason: String

Reason that the thread was locked. Defaults to null when no reason is recorded.

type: :locked

Status discriminator that is always `locked`.

class Closed { reason, type }

Indicates that a thread has been closed.

reason: String

Reason that the thread was closed. Defaults to null when no reason is recorded.

type: :closed

Status discriminator that is always `closed`.

title: String

Optional human-readable title for the thread. Defaults to null when no title has been generated.

user: String

Free-form string that identifies your end user who owns the thread.

class ChatKitThreadAssistantMessageItem { id, content, created\_at, 3 more }

Assistant-authored message within a thread.

id: String

Identifier of the thread item.

content: Array[[ChatKitResponseOutputText](/api/reference/ruby/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_response_output_text%20%3E%20(schema)) { annotations, text, type } ]

Ordered assistant response segments.

annotations: Array[File{ source, type} | URL{ source, type}]

Ordered list of annotations attached to the response text.

One of the following:

class File { source, type }

Annotation that references an uploaded file.

source: Source{ filename, type}

File attachment referenced by the annotation.

filename: String

Filename referenced by the annotation.

type: :file

Type discriminator that is always `file`.

type: :file

Type discriminator that is always `file` for this annotation.

class URL { source, type }

Annotation that references a URL.

source: Source{ type, url}

URL referenced by the annotation.

type: :url

Type discriminator that is always `url`.

url: String

URL referenced by the annotation.

formaturi

type: :url

Type discriminator that is always `url` for this annotation.

text: String

Assistant generated text.

type: :output\_text

Type discriminator that is always `output_text`.

created\_at: Integer

Unix timestamp (in seconds) for when the item was created.

formatunixtime

object: :"chatkit.thread\_item"

Type discriminator that is always `chatkit.thread_item`.

thread\_id: String

Identifier of the parent thread.

type: :"chatkit.assistant\_message"

Type discriminator that is always `chatkit.assistant_message`.

class ChatKitThreadItemList { data, first\_id, has\_more, 2 more }

A paginated list of thread items rendered for the ChatKit API.

data: Array[[ChatKitThreadUserMessageItem](/api/reference/ruby/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_user_message_item%20%3E%20(schema)) { id, attachments, content, 5 more }  | [ChatKitThreadAssistantMessageItem](/api/reference/ruby/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_assistant_message_item%20%3E%20(schema)) { id, content, created\_at, 3 more }  | [ChatKitWidgetItem](/api/reference/ruby/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_widget_item%20%3E%20(schema)) { id, created\_at, object, 3 more }  | 3 more]

A list of items

One of the following:

class ChatKitThreadUserMessageItem { id, attachments, content, 5 more }

User-authored messages within a thread.

id: String

Identifier of the thread item.

attachments: Array[[ChatKitAttachment](/api/reference/ruby/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_attachment%20%3E%20(schema)) { id, mime\_type, name, 2 more } ]

Attachments associated with the user message. Defaults to an empty list.

id: String

Identifier for the attachment.

mime\_type: String

MIME type of the attachment.

name: String

Original display name for the attachment.

preview\_url: String

Preview URL for rendering the attachment inline.

formaturi

type: :image | :file

Attachment discriminator.

One of the following:

:image

:file

content: Array[InputText{ text, type} | QuotedText{ text, type}]

Ordered content elements supplied by the user.

One of the following:

class InputText { text, type }

Text block that a user contributed to the thread.

text: String

Plain-text content supplied by the user.

type: :input\_text

Type discriminator that is always `input_text`.

class QuotedText { text, type }

Quoted snippet that the user referenced in their message.

text: String

Quoted text content.

type: :quoted\_text

Type discriminator that is always `quoted_text`.

created\_at: Integer

Unix timestamp (in seconds) for when the item was created.

formatunixtime

inference\_options: InferenceOptions{ model, tool\_choice}

Inference overrides applied to the message. Defaults to null when unset.

model: String

Model name that generated the response. Defaults to null when using the session default.

tool\_choice: ToolChoice{ id}

Preferred tool to invoke. Defaults to null when ChatKit should auto-select.

id: String

Identifier of the requested tool.

object: :"chatkit.thread\_item"

Type discriminator that is always `chatkit.thread_item`.

thread\_id: String

Identifier of the parent thread.

type: :"chatkit.user\_message"

class ChatKitThreadAssistantMessageItem { id, content, created\_at, 3 more }

Assistant-authored message within a thread.

id: String

Identifier of the thread item.

content: Array[[ChatKitResponseOutputText](/api/reference/ruby/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_response_output_text%20%3E%20(schema)) { annotations, text, type } ]

Ordered assistant response segments.

annotations: Array[File{ source, type} | URL{ source, type}]

Ordered list of annotations attached to the response text.

One of the following:

class File { source, type }

Annotation that references an uploaded file.

source: Source{ filename, type}

File attachment referenced by the annotation.

filename: String

Filename referenced by the annotation.

type: :file

Type discriminator that is always `file`.

type: :file

Type discriminator that is always `file` for this annotation.

class URL { source, type }

Annotation that references a URL.

source: Source{ type, url}

URL referenced by the annotation.

type: :url

Type discriminator that is always `url`.

url: String

URL referenced by the annotation.

formaturi

type: :url

Type discriminator that is always `url` for this annotation.

text: String

Assistant generated text.

type: :output\_text

Type discriminator that is always `output_text`.

created\_at: Integer

Unix timestamp (in seconds) for when the item was created.

formatunixtime

object: :"chatkit.thread\_item"

Type discriminator that is always `chatkit.thread_item`.

thread\_id: String

Identifier of the parent thread.

type: :"chatkit.assistant\_message"

Type discriminator that is always `chatkit.assistant_message`.

class ChatKitWidgetItem { id, created\_at, object, 3 more }

Thread item that renders a widget payload.

id: String

Identifier of the thread item.

created\_at: Integer

Unix timestamp (in seconds) for when the item was created.

formatunixtime

object: :"chatkit.thread\_item"

Type discriminator that is always `chatkit.thread_item`.

thread\_id: String

Identifier of the parent thread.

type: :"chatkit.widget"

Type discriminator that is always `chatkit.widget`.

widget: String

Serialized widget payload rendered in the UI.

class ChatKitClientToolCall { id, arguments, call\_id, 7 more }

Record of a client side tool invocation initiated by the assistant.

id: String

Identifier of the thread item.

arguments: String

JSON-encoded arguments that were sent to the tool.

call\_id: String

Identifier for the client tool call.

created\_at: Integer

Unix timestamp (in seconds) for when the item was created.

formatunixtime

name: String

Tool name that was invoked.

object: :"chatkit.thread\_item"

Type discriminator that is always `chatkit.thread_item`.

output: String

JSON-encoded output captured from the tool. Defaults to null while execution is in progress.

status: :in\_progress | :completed

Execution status for the tool call.

One of the following:

:in\_progress

:completed

thread\_id: String

Identifier of the parent thread.

type: :"chatkit.client\_tool\_call"

Type discriminator that is always `chatkit.client_tool_call`.

class ChatKitTask { id, created\_at, heading, 5 more }

Task emitted by the workflow to show progress and status updates.

id: String

Identifier of the thread item.

created\_at: Integer

Unix timestamp (in seconds) for when the item was created.

formatunixtime

heading: String

Optional heading for the task. Defaults to null when not provided.

object: :"chatkit.thread\_item"

Type discriminator that is always `chatkit.thread_item`.

summary: String

Optional summary that describes the task. Defaults to null when omitted.

task\_type: :custom | :thought

Subtype for the task.

One of the following:

:custom

:thought

thread\_id: String

Identifier of the parent thread.

type: :"chatkit.task"

Type discriminator that is always `chatkit.task`.

class ChatKitTaskGroup { id, created\_at, object, 3 more }

Collection of workflow tasks grouped together in the thread.

id: String

Identifier of the thread item.

created\_at: Integer

Unix timestamp (in seconds) for when the item was created.

formatunixtime

object: :"chatkit.thread\_item"

Type discriminator that is always `chatkit.thread_item`.

tasks: Array[Task{ heading, summary, type}]

Tasks included in the group.

heading: String

Optional heading for the grouped task. Defaults to null when not provided.

summary: String

Optional summary that describes the grouped task. Defaults to null when omitted.

type: :custom | :thought

Subtype for the grouped task.

One of the following:

:custom

:thought

thread\_id: String

Identifier of the parent thread.

type: :"chatkit.task\_group"

Type discriminator that is always `chatkit.task_group`.

first\_id: String

The ID of the first item in the list.

has\_more: bool

Whether there are more items available.

last\_id: String

The ID of the last item in the list.

object: :list

The type of object returned, must be `list`.

class ChatKitThreadUserMessageItem { id, attachments, content, 5 more }

User-authored messages within a thread.

id: String

Identifier of the thread item.

attachments: Array[[ChatKitAttachment](/api/reference/ruby/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_attachment%20%3E%20(schema)) { id, mime\_type, name, 2 more } ]

Attachments associated with the user message. Defaults to an empty list.

id: String

Identifier for the attachment.

mime\_type: String

MIME type of the attachment.

name: String

Original display name for the attachment.

preview\_url: String

Preview URL for rendering the attachment inline.

formaturi

type: :image | :file

Attachment discriminator.

One of the following:

:image

:file

content: Array[InputText{ text, type} | QuotedText{ text, type}]

Ordered content elements supplied by the user.

One of the following:

class InputText { text, type }

Text block that a user contributed to the thread.

text: String

Plain-text content supplied by the user.

type: :input\_text

Type discriminator that is always `input_text`.

class QuotedText { text, type }

Quoted snippet that the user referenced in their message.

text: String

Quoted text content.

type: :quoted\_text

Type discriminator that is always `quoted_text`.

created\_at: Integer

Unix timestamp (in seconds) for when the item was created.

formatunixtime

inference\_options: InferenceOptions{ model, tool\_choice}

Inference overrides applied to the message. Defaults to null when unset.

model: String

Model name that generated the response. Defaults to null when using the session default.

tool\_choice: ToolChoice{ id}

Preferred tool to invoke. Defaults to null when ChatKit should auto-select.

id: String

Identifier of the requested tool.

object: :"chatkit.thread\_item"

Type discriminator that is always `chatkit.thread_item`.

thread\_id: String

Identifier of the parent thread.

type: :"chatkit.user\_message"

class ChatKitWidgetItem { id, created\_at, object, 3 more }

Thread item that renders a widget payload.

id: String

Identifier of the thread item.

created\_at: Integer

Unix timestamp (in seconds) for when the item was created.

formatunixtime

object: :"chatkit.thread\_item"

Type discriminator that is always `chatkit.thread_item`.

thread\_id: String

Identifier of the parent thread.

type: :"chatkit.widget"

Type discriminator that is always `chatkit.widget`.

widget: String

Serialized widget payload rendered in the UI.

class ThreadDeleteResponse { id, deleted, object }

Confirmation payload returned after deleting a thread.

id: String

Identifier of the deleted thread.

deleted: bool

Indicates that the thread has been deleted.

object: :"chatkit.thread.deleted"

Type discriminator that is always `chatkit.thread.deleted`.
