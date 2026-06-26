<!-- source: https://developers.openai.com/api/reference/resources/beta/subresources/chatkit/subresources/threads/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Beta](/api/reference/resources/beta)

[ChatKit](/api/reference/resources/beta/subresources/chatkit)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Threads

##### [List ChatKit thread items](/api/reference/resources/beta/subresources/chatkit/subresources/threads/methods/list_items)

GET/chatkit/threads/{thread\_id}/items

##### [Retrieve ChatKit thread](/api/reference/resources/beta/subresources/chatkit/subresources/threads/methods/retrieve)

GET/chatkit/threads/{thread\_id}

##### [Delete ChatKit thread](/api/reference/resources/beta/subresources/chatkit/subresources/threads/methods/delete)

DELETE/chatkit/threads/{thread\_id}

##### [List ChatKit threads](/api/reference/resources/beta/subresources/chatkit/subresources/threads/methods/list)

GET/chatkit/threads

##### ModelsExpand Collapse

ChatSession object { id, chatkit\_configuration, client\_secret, 7 more }

Represents a ChatKit session and its resolved configuration.

id: string

Identifier for the ChatKit session.

chatkit\_configuration: [ChatSessionChatKitConfiguration](/api/reference/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_chatkit_configuration%20%3E%20(schema)) { automatic\_thread\_titling, file\_upload, history }

Resolved ChatKit feature configuration for the session.

client\_secret: string

Ephemeral client secret that authenticates session requests.

expires\_at: number

Unix timestamp (in seconds) for when the session expires.

formatunixtime

max\_requests\_per\_1\_minute: number

Convenience copy of the per-minute request limit.

object: "chatkit.session"

Type discriminator that is always `chatkit.session`.

rate\_limits: [ChatSessionRateLimits](/api/reference/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_rate_limits%20%3E%20(schema)) { max\_requests\_per\_1\_minute }

Resolved rate limit values.

status: [ChatSessionStatus](/api/reference/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_status%20%3E%20(schema))

Current lifecycle state of the session.

user: string

User identifier associated with the session.

workflow: [ChatKitWorkflow](/api/reference/resources/beta#(resource)%20beta.chatkit%20%3E%20(model)%20chatkit_workflow%20%3E%20(schema)) { id, state\_variables, tracing, version }

Workflow metadata for the session.

ChatSessionAutomaticThreadTitling object { enabled }

Automatic thread title preferences for the session.

enabled: boolean

Whether automatic thread titling is enabled.

ChatSessionChatKitConfiguration object { automatic\_thread\_titling, file\_upload, history }

ChatKit configuration for the session.

automatic\_thread\_titling: [ChatSessionAutomaticThreadTitling](/api/reference/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_automatic_thread_titling%20%3E%20(schema)) { enabled }

Automatic thread titling preferences.

file\_upload: [ChatSessionFileUpload](/api/reference/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_file_upload%20%3E%20(schema)) { enabled, max\_file\_size, max\_files }

Upload settings for the session.

history: [ChatSessionHistory](/api/reference/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_history%20%3E%20(schema)) { enabled, recent\_threads }

History retention configuration.

ChatSessionChatKitConfigurationParam object { automatic\_thread\_titling, file\_upload, history }

Optional per-session configuration settings for ChatKit behavior.

automatic\_thread\_titling: optional object { enabled }

Configuration for automatic thread titling. When omitted, automatic thread titling is enabled by default.

enabled: optional boolean

Enable automatic thread title generation. Defaults to true.

file\_upload: optional object { enabled, max\_file\_size, max\_files }

Configuration for upload enablement and limits. When omitted, uploads are disabled by default (max\_files 10, max\_file\_size 512 MB).

enabled: optional boolean

Enable uploads for this session. Defaults to false.

max\_file\_size: optional number

Maximum size in megabytes for each uploaded file. Defaults to 512 MB, which is the maximum allowable size.

maximum512

minimum1

max\_files: optional number

Maximum number of files that can be uploaded to the session. Defaults to 10.

minimum1

history: optional object { enabled, recent\_threads }

Configuration for chat history retention. When omitted, history is enabled by default with no limit on recent\_threads (null).

enabled: optional boolean

Enables chat users to access previous ChatKit threads. Defaults to true.

recent\_threads: optional number

Number of recent ChatKit threads users have access to. Defaults to unlimited when unset.

minimum1

ChatSessionExpiresAfterParam object { anchor, seconds }

Controls when the session expires relative to an anchor timestamp.

anchor: "created\_at"

Base timestamp used to calculate expiration. Currently fixed to `created_at`.

seconds: number

Number of seconds after the anchor when the session expires.

maximum600

minimum1

formatint64

ChatSessionFileUpload object { enabled, max\_file\_size, max\_files }

Upload permissions and limits applied to the session.

enabled: boolean

Indicates if uploads are enabled for the session.

max\_file\_size: number

Maximum upload size in megabytes.

max\_files: number

Maximum number of uploads allowed during the session.

ChatSessionHistory object { enabled, recent\_threads }

History retention preferences returned for the session.

enabled: boolean

Indicates if chat history is persisted for the session.

recent\_threads: number

Number of prior threads surfaced in history views. Defaults to null when all history is retained.

ChatSessionRateLimits object { max\_requests\_per\_1\_minute }

Active per-minute request limit for the session.

max\_requests\_per\_1\_minute: number

Maximum allowed requests per one-minute window.

ChatSessionRateLimitsParam object { max\_requests\_per\_1\_minute }

Controls request rate limits for the session.

max\_requests\_per\_1\_minute: optional number

Maximum number of requests allowed per minute for the session. Defaults to 10.

minimum1

ChatSessionStatus = "active" or "expired" or "cancelled"

One of the following:

"active"

"expired"

"cancelled"

ChatSessionWorkflowParam object { id, state\_variables, tracing, version }

Workflow reference and overrides applied to the chat session.

id: string

Identifier for the workflow invoked by the session.

state\_variables: optional map[string or boolean or number]

State variables forwarded to the workflow. Keys may be up to 64 characters, values must be primitive types, and the map defaults to an empty object.

One of the following:

string

boolean

number

tracing: optional object { enabled }

Optional tracing overrides for the workflow invocation. When omitted, tracing is enabled by default.

enabled: optional boolean

Whether tracing is enabled during the session. Defaults to true.

version: optional string

Specific workflow version to run. Defaults to the latest deployed version.

ChatKitAttachment object { id, mime\_type, name, 2 more }

Attachment metadata included on thread items.

id: string

Identifier for the attachment.

mime\_type: string

MIME type of the attachment.

name: string

Original display name for the attachment.

preview\_url: string

Preview URL for rendering the attachment inline.

formaturi

type: "image" or "file"

Attachment discriminator.

One of the following:

"image"

"file"

ChatKitResponseOutputText object { annotations, text, type }

Assistant response text accompanied by optional annotations.

annotations: array of object { source, type }  or object { source, type }

Ordered list of annotations attached to the response text.

One of the following:

File object { source, type }

Annotation that references an uploaded file.

source: object { filename, type }

File attachment referenced by the annotation.

filename: string

Filename referenced by the annotation.

type: "file"

Type discriminator that is always `file`.

type: "file"

Type discriminator that is always `file` for this annotation.

URL object { source, type }

Annotation that references a URL.

source: object { type, url }

URL referenced by the annotation.

type: "url"

Type discriminator that is always `url`.

url: string

URL referenced by the annotation.

formaturi

type: "url"

Type discriminator that is always `url` for this annotation.

text: string

Assistant generated text.

type: "output\_text"

Type discriminator that is always `output_text`.

ChatKitThread object { id, created\_at, object, 3 more }

Represents a ChatKit thread and its current status.

id: string

Identifier of the thread.

created\_at: number

Unix timestamp (in seconds) for when the thread was created.

formatunixtime

object: "chatkit.thread"

Type discriminator that is always `chatkit.thread`.

status: object { type }  or object { reason, type }  or object { reason, type }

Current status for the thread. Defaults to `active` for newly created threads.

One of the following:

Active object { type }

Indicates that a thread is active.

type: "active"

Status discriminator that is always `active`.

Locked object { reason, type }

Indicates that a thread is locked and cannot accept new input.

reason: string

Reason that the thread was locked. Defaults to null when no reason is recorded.

type: "locked"

Status discriminator that is always `locked`.

Closed object { reason, type }

Indicates that a thread has been closed.

reason: string

Reason that the thread was closed. Defaults to null when no reason is recorded.

type: "closed"

Status discriminator that is always `closed`.

title: string

Optional human-readable title for the thread. Defaults to null when no title has been generated.

user: string

Free-form string that identifies your end user who owns the thread.

ChatKitThreadAssistantMessageItem object { id, content, created\_at, 3 more }

Assistant-authored message within a thread.

id: string

Identifier of the thread item.

content: array of [ChatKitResponseOutputText](/api/reference/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_response_output_text%20%3E%20(schema)) { annotations, text, type }

Ordered assistant response segments.

annotations: array of object { source, type }  or object { source, type }

Ordered list of annotations attached to the response text.

One of the following:

File object { source, type }

Annotation that references an uploaded file.

source: object { filename, type }

File attachment referenced by the annotation.

filename: string

Filename referenced by the annotation.

type: "file"

Type discriminator that is always `file`.

type: "file"

Type discriminator that is always `file` for this annotation.

URL object { source, type }

Annotation that references a URL.

source: object { type, url }

URL referenced by the annotation.

type: "url"

Type discriminator that is always `url`.

url: string

URL referenced by the annotation.

formaturi

type: "url"

Type discriminator that is always `url` for this annotation.

text: string

Assistant generated text.

type: "output\_text"

Type discriminator that is always `output_text`.

created\_at: number

Unix timestamp (in seconds) for when the item was created.

formatunixtime

object: "chatkit.thread\_item"

Type discriminator that is always `chatkit.thread_item`.

thread\_id: string

Identifier of the parent thread.

type: "chatkit.assistant\_message"

Type discriminator that is always `chatkit.assistant_message`.

ChatKitThreadItemList object { data, first\_id, has\_more, 2 more }

A paginated list of thread items rendered for the ChatKit API.

data: array of [ChatKitThreadUserMessageItem](/api/reference/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_user_message_item%20%3E%20(schema)) { id, attachments, content, 5 more }  or [ChatKitThreadAssistantMessageItem](/api/reference/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_assistant_message_item%20%3E%20(schema)) { id, content, created\_at, 3 more }  or [ChatKitWidgetItem](/api/reference/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_widget_item%20%3E%20(schema)) { id, created\_at, object, 3 more }  or 3 more

A list of items

One of the following:

ChatKitThreadUserMessageItem object { id, attachments, content, 5 more }

User-authored messages within a thread.

id: string

Identifier of the thread item.

attachments: array of [ChatKitAttachment](/api/reference/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_attachment%20%3E%20(schema)) { id, mime\_type, name, 2 more }

Attachments associated with the user message. Defaults to an empty list.

id: string

Identifier for the attachment.

mime\_type: string

MIME type of the attachment.

name: string

Original display name for the attachment.

preview\_url: string

Preview URL for rendering the attachment inline.

formaturi

type: "image" or "file"

Attachment discriminator.

One of the following:

"image"

"file"

content: array of object { text, type }  or object { text, type }

Ordered content elements supplied by the user.

One of the following:

InputText object { text, type }

Text block that a user contributed to the thread.

text: string

Plain-text content supplied by the user.

type: "input\_text"

Type discriminator that is always `input_text`.

QuotedText object { text, type }

Quoted snippet that the user referenced in their message.

text: string

Quoted text content.

type: "quoted\_text"

Type discriminator that is always `quoted_text`.

created\_at: number

Unix timestamp (in seconds) for when the item was created.

formatunixtime

inference\_options: object { model, tool\_choice }

Inference overrides applied to the message. Defaults to null when unset.

model: string

Model name that generated the response. Defaults to null when using the session default.

tool\_choice: object { id }

Preferred tool to invoke. Defaults to null when ChatKit should auto-select.

id: string

Identifier of the requested tool.

object: "chatkit.thread\_item"

Type discriminator that is always `chatkit.thread_item`.

thread\_id: string

Identifier of the parent thread.

type: "chatkit.user\_message"

ChatKitThreadAssistantMessageItem object { id, content, created\_at, 3 more }

Assistant-authored message within a thread.

id: string

Identifier of the thread item.

content: array of [ChatKitResponseOutputText](/api/reference/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_response_output_text%20%3E%20(schema)) { annotations, text, type }

Ordered assistant response segments.

annotations: array of object { source, type }  or object { source, type }

Ordered list of annotations attached to the response text.

One of the following:

File object { source, type }

Annotation that references an uploaded file.

source: object { filename, type }

File attachment referenced by the annotation.

filename: string

Filename referenced by the annotation.

type: "file"

Type discriminator that is always `file`.

type: "file"

Type discriminator that is always `file` for this annotation.

URL object { source, type }

Annotation that references a URL.

source: object { type, url }

URL referenced by the annotation.

type: "url"

Type discriminator that is always `url`.

url: string

URL referenced by the annotation.

formaturi

type: "url"

Type discriminator that is always `url` for this annotation.

text: string

Assistant generated text.

type: "output\_text"

Type discriminator that is always `output_text`.

created\_at: number

Unix timestamp (in seconds) for when the item was created.

formatunixtime

object: "chatkit.thread\_item"

Type discriminator that is always `chatkit.thread_item`.

thread\_id: string

Identifier of the parent thread.

type: "chatkit.assistant\_message"

Type discriminator that is always `chatkit.assistant_message`.

ChatKitWidgetItem object { id, created\_at, object, 3 more }

Thread item that renders a widget payload.

id: string

Identifier of the thread item.

created\_at: number

Unix timestamp (in seconds) for when the item was created.

formatunixtime

object: "chatkit.thread\_item"

Type discriminator that is always `chatkit.thread_item`.

thread\_id: string

Identifier of the parent thread.

type: "chatkit.widget"

Type discriminator that is always `chatkit.widget`.

widget: string

Serialized widget payload rendered in the UI.

ChatKitClientToolCall object { id, arguments, call\_id, 7 more }

Record of a client side tool invocation initiated by the assistant.

id: string

Identifier of the thread item.

arguments: string

JSON-encoded arguments that were sent to the tool.

call\_id: string

Identifier for the client tool call.

created\_at: number

Unix timestamp (in seconds) for when the item was created.

formatunixtime

name: string

Tool name that was invoked.

object: "chatkit.thread\_item"

Type discriminator that is always `chatkit.thread_item`.

output: string

JSON-encoded output captured from the tool. Defaults to null while execution is in progress.

status: "in\_progress" or "completed"

Execution status for the tool call.

One of the following:

"in\_progress"

"completed"

thread\_id: string

Identifier of the parent thread.

type: "chatkit.client\_tool\_call"

Type discriminator that is always `chatkit.client_tool_call`.

ChatKitTask object { id, created\_at, heading, 5 more }

Task emitted by the workflow to show progress and status updates.

id: string

Identifier of the thread item.

created\_at: number

Unix timestamp (in seconds) for when the item was created.

formatunixtime

heading: string

Optional heading for the task. Defaults to null when not provided.

object: "chatkit.thread\_item"

Type discriminator that is always `chatkit.thread_item`.

summary: string

Optional summary that describes the task. Defaults to null when omitted.

task\_type: "custom" or "thought"

Subtype for the task.

One of the following:

"custom"

"thought"

thread\_id: string

Identifier of the parent thread.

type: "chatkit.task"

Type discriminator that is always `chatkit.task`.

ChatKitTaskGroup object { id, created\_at, object, 3 more }

Collection of workflow tasks grouped together in the thread.

id: string

Identifier of the thread item.

created\_at: number

Unix timestamp (in seconds) for when the item was created.

formatunixtime

object: "chatkit.thread\_item"

Type discriminator that is always `chatkit.thread_item`.

tasks: array of object { heading, summary, type }

Tasks included in the group.

heading: string

Optional heading for the grouped task. Defaults to null when not provided.

summary: string

Optional summary that describes the grouped task. Defaults to null when omitted.

type: "custom" or "thought"

Subtype for the grouped task.

One of the following:

"custom"

"thought"

thread\_id: string

Identifier of the parent thread.

type: "chatkit.task\_group"

Type discriminator that is always `chatkit.task_group`.

first\_id: string

The ID of the first item in the list.

has\_more: boolean

Whether there are more items available.

last\_id: string

The ID of the last item in the list.

object: "list"

The type of object returned, must be `list`.

ChatKitThreadUserMessageItem object { id, attachments, content, 5 more }

User-authored messages within a thread.

id: string

Identifier of the thread item.

attachments: array of [ChatKitAttachment](/api/reference/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_attachment%20%3E%20(schema)) { id, mime\_type, name, 2 more }

Attachments associated with the user message. Defaults to an empty list.

id: string

Identifier for the attachment.

mime\_type: string

MIME type of the attachment.

name: string

Original display name for the attachment.

preview\_url: string

Preview URL for rendering the attachment inline.

formaturi

type: "image" or "file"

Attachment discriminator.

One of the following:

"image"

"file"

content: array of object { text, type }  or object { text, type }

Ordered content elements supplied by the user.

One of the following:

InputText object { text, type }

Text block that a user contributed to the thread.

text: string

Plain-text content supplied by the user.

type: "input\_text"

Type discriminator that is always `input_text`.

QuotedText object { text, type }

Quoted snippet that the user referenced in their message.

text: string

Quoted text content.

type: "quoted\_text"

Type discriminator that is always `quoted_text`.

created\_at: number

Unix timestamp (in seconds) for when the item was created.

formatunixtime

inference\_options: object { model, tool\_choice }

Inference overrides applied to the message. Defaults to null when unset.

model: string

Model name that generated the response. Defaults to null when using the session default.

tool\_choice: object { id }

Preferred tool to invoke. Defaults to null when ChatKit should auto-select.

id: string

Identifier of the requested tool.

object: "chatkit.thread\_item"

Type discriminator that is always `chatkit.thread_item`.

thread\_id: string

Identifier of the parent thread.

type: "chatkit.user\_message"

ChatKitWidgetItem object { id, created\_at, object, 3 more }

Thread item that renders a widget payload.

id: string

Identifier of the thread item.

created\_at: number

Unix timestamp (in seconds) for when the item was created.

formatunixtime

object: "chatkit.thread\_item"

Type discriminator that is always `chatkit.thread_item`.

thread\_id: string

Identifier of the parent thread.

type: "chatkit.widget"

Type discriminator that is always `chatkit.widget`.

widget: string

Serialized widget payload rendered in the UI.

ThreadDeleteResponse object { id, deleted, object }

Confirmation payload returned after deleting a thread.

id: string

Identifier of the deleted thread.

deleted: boolean

Indicates that the thread has been deleted.

object: "chatkit.thread.deleted"

Type discriminator that is always `chatkit.thread.deleted`.
