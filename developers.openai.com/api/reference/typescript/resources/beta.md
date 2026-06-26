<!-- source: https://developers.openai.com/api/reference/typescript/resources/beta/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

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

ChatKitWorkflow { id, state\_variables, tracing, version }

Workflow metadata and state returned for the session.

id: string

Identifier of the workflow backing the session.

state\_variables: Record<string, string | boolean | number> | null

State variable key-value pairs applied when invoking the workflow. Defaults to null when no overrides were provided.

One of the following:

string

boolean

number

tracing: Tracing { enabled }

Tracing settings applied to the workflow.

enabled: boolean

Indicates whether tracing is enabled.

version: string | null

Specific workflow version used for the session. Defaults to null when using the latest deployment.

#### BetaChatKitSessions

##### [Cancel chat session](/api/reference/typescript/resources/beta/subresources/chatkit/subresources/sessions/methods/cancel)

client.beta.chatkit.sessions.cancel(stringsessionID, RequestOptionsoptions?): [ChatSession](/api/reference/typescript/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session%20%3E%20(schema)) { id, chatkit\_configuration, client\_secret, 7 more }

POST/chatkit/sessions/{session\_id}/cancel

##### [Create ChatKit session](/api/reference/typescript/resources/beta/subresources/chatkit/subresources/sessions/methods/create)

client.beta.chatkit.sessions.create(SessionCreateParams { user, workflow, chatkit\_configuration, 2 more } body, RequestOptionsoptions?): [ChatSession](/api/reference/typescript/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session%20%3E%20(schema)) { id, chatkit\_configuration, client\_secret, 7 more }

POST/chatkit/sessions

#### BetaChatKitThreads

##### [List ChatKit thread items](/api/reference/typescript/resources/beta/subresources/chatkit/subresources/threads/methods/list_items)

client.beta.chatkit.threads.listItems(stringthreadID, ThreadListItemsParams { after, before, limit, order } query?, RequestOptionsoptions?): ConversationCursorPage<[ChatKitThreadUserMessageItem](/api/reference/typescript/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_user_message_item%20%3E%20(schema)) { id, attachments, content, 5 more }  | [ChatKitThreadAssistantMessageItem](/api/reference/typescript/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_assistant_message_item%20%3E%20(schema)) { id, content, created\_at, 3 more }  | [ChatKitWidgetItem](/api/reference/typescript/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_widget_item%20%3E%20(schema)) { id, created\_at, object, 3 more }  | 3 more>

GET/chatkit/threads/{thread\_id}/items

##### [Retrieve ChatKit thread](/api/reference/typescript/resources/beta/subresources/chatkit/subresources/threads/methods/retrieve)

client.beta.chatkit.threads.retrieve(stringthreadID, RequestOptionsoptions?): [ChatKitThread](/api/reference/typescript/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread%20%3E%20(schema)) { id, created\_at, object, 3 more }

GET/chatkit/threads/{thread\_id}

##### [Delete ChatKit thread](/api/reference/typescript/resources/beta/subresources/chatkit/subresources/threads/methods/delete)

client.beta.chatkit.threads.delete(stringthreadID, RequestOptionsoptions?): [ThreadDeleteResponse](/api/reference/typescript/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20thread_delete_response%20%3E%20(schema)) { id, deleted, object }

DELETE/chatkit/threads/{thread\_id}

##### [List ChatKit threads](/api/reference/typescript/resources/beta/subresources/chatkit/subresources/threads/methods/list)

client.beta.chatkit.threads.list(ThreadListParams { after, before, limit, 2 more } query?, RequestOptionsoptions?): ConversationCursorPage<[ChatKitThread](/api/reference/typescript/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread%20%3E%20(schema)) { id, created\_at, object, 3 more } >

GET/chatkit/threads

##### ModelsExpand Collapse

ChatSession { id, chatkit\_configuration, client\_secret, 7 more }

Represents a ChatKit session and its resolved configuration.

id: string

Identifier for the ChatKit session.

chatkit\_configuration: [ChatSessionChatKitConfiguration](/api/reference/typescript/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_chatkit_configuration%20%3E%20(schema)) { automatic\_thread\_titling, file\_upload, history }

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

rate\_limits: [ChatSessionRateLimits](/api/reference/typescript/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_rate_limits%20%3E%20(schema)) { max\_requests\_per\_1\_minute }

Resolved rate limit values.

status: [ChatSessionStatus](/api/reference/typescript/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_status%20%3E%20(schema))

Current lifecycle state of the session.

user: string

User identifier associated with the session.

workflow: [ChatKitWorkflow](/api/reference/typescript/resources/beta#(resource)%20beta.chatkit%20%3E%20(model)%20chatkit_workflow%20%3E%20(schema)) { id, state\_variables, tracing, version }

Workflow metadata for the session.

ChatSessionAutomaticThreadTitling { enabled }

Automatic thread title preferences for the session.

enabled: boolean

Whether automatic thread titling is enabled.

ChatSessionChatKitConfiguration { automatic\_thread\_titling, file\_upload, history }

ChatKit configuration for the session.

automatic\_thread\_titling: [ChatSessionAutomaticThreadTitling](/api/reference/typescript/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_automatic_thread_titling%20%3E%20(schema)) { enabled }

Automatic thread titling preferences.

file\_upload: [ChatSessionFileUpload](/api/reference/typescript/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_file_upload%20%3E%20(schema)) { enabled, max\_file\_size, max\_files }

Upload settings for the session.

history: [ChatSessionHistory](/api/reference/typescript/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_history%20%3E%20(schema)) { enabled, recent\_threads }

History retention configuration.

ChatSessionChatKitConfigurationParam { automatic\_thread\_titling, file\_upload, history }

Optional per-session configuration settings for ChatKit behavior.

automatic\_thread\_titling?: AutomaticThreadTitling { enabled }

Configuration for automatic thread titling. When omitted, automatic thread titling is enabled by default.

enabled?: boolean

Enable automatic thread title generation. Defaults to true.

file\_upload?: FileUpload { enabled, max\_file\_size, max\_files }

Configuration for upload enablement and limits. When omitted, uploads are disabled by default (max\_files 10, max\_file\_size 512 MB).

enabled?: boolean

Enable uploads for this session. Defaults to false.

max\_file\_size?: number

Maximum size in megabytes for each uploaded file. Defaults to 512 MB, which is the maximum allowable size.

maximum512

minimum1

max\_files?: number

Maximum number of files that can be uploaded to the session. Defaults to 10.

minimum1

history?: History { enabled, recent\_threads }

Configuration for chat history retention. When omitted, history is enabled by default with no limit on recent\_threads (null).

enabled?: boolean

Enables chat users to access previous ChatKit threads. Defaults to true.

recent\_threads?: number

Number of recent ChatKit threads users have access to. Defaults to unlimited when unset.

minimum1

ChatSessionExpiresAfterParam { anchor, seconds }

Controls when the session expires relative to an anchor timestamp.

anchor: "created\_at"

Base timestamp used to calculate expiration. Currently fixed to `created_at`.

seconds: number

Number of seconds after the anchor when the session expires.

maximum600

minimum1

formatint64

ChatSessionFileUpload { enabled, max\_file\_size, max\_files }

Upload permissions and limits applied to the session.

enabled: boolean

Indicates if uploads are enabled for the session.

max\_file\_size: number | null

Maximum upload size in megabytes.

max\_files: number | null

Maximum number of uploads allowed during the session.

ChatSessionHistory { enabled, recent\_threads }

History retention preferences returned for the session.

enabled: boolean

Indicates if chat history is persisted for the session.

recent\_threads: number | null

Number of prior threads surfaced in history views. Defaults to null when all history is retained.

ChatSessionRateLimits { max\_requests\_per\_1\_minute }

Active per-minute request limit for the session.

max\_requests\_per\_1\_minute: number

Maximum allowed requests per one-minute window.

ChatSessionRateLimitsParam { max\_requests\_per\_1\_minute }

Controls request rate limits for the session.

max\_requests\_per\_1\_minute?: number

Maximum number of requests allowed per minute for the session. Defaults to 10.

minimum1

ChatSessionStatus = "active" | "expired" | "cancelled"

One of the following:

"active"

"expired"

"cancelled"

ChatSessionWorkflowParam { id, state\_variables, tracing, version }

Workflow reference and overrides applied to the chat session.

id: string

Identifier for the workflow invoked by the session.

state\_variables?: Record<string, string | boolean | number>

State variables forwarded to the workflow. Keys may be up to 64 characters, values must be primitive types, and the map defaults to an empty object.

One of the following:

string

boolean

number

tracing?: Tracing { enabled }

Optional tracing overrides for the workflow invocation. When omitted, tracing is enabled by default.

enabled?: boolean

Whether tracing is enabled during the session. Defaults to true.

version?: string

Specific workflow version to run. Defaults to the latest deployed version.

ChatKitAttachment { id, mime\_type, name, 2 more }

Attachment metadata included on thread items.

id: string

Identifier for the attachment.

mime\_type: string

MIME type of the attachment.

name: string

Original display name for the attachment.

preview\_url: string | null

Preview URL for rendering the attachment inline.

formaturi

type: "image" | "file"

Attachment discriminator.

One of the following:

"image"

"file"

ChatKitResponseOutputText { annotations, text, type }

Assistant response text accompanied by optional annotations.

annotations: Array<File { source, type }  | URL { source, type } >

Ordered list of annotations attached to the response text.

One of the following:

File { source, type }

Annotation that references an uploaded file.

source: Source { filename, type }

File attachment referenced by the annotation.

filename: string

Filename referenced by the annotation.

type: "file"

Type discriminator that is always `file`.

type: "file"

Type discriminator that is always `file` for this annotation.

URL { source, type }

Annotation that references a URL.

source: Source { type, url }

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

ChatKitThread { id, created\_at, object, 3 more }

Represents a ChatKit thread and its current status.

id: string

Identifier of the thread.

created\_at: number

Unix timestamp (in seconds) for when the thread was created.

formatunixtime

object: "chatkit.thread"

Type discriminator that is always `chatkit.thread`.

status: Active { type }  | Locked { reason, type }  | Closed { reason, type }

Current status for the thread. Defaults to `active` for newly created threads.

One of the following:

Active { type }

Indicates that a thread is active.

type: "active"

Status discriminator that is always `active`.

Locked { reason, type }

Indicates that a thread is locked and cannot accept new input.

reason: string | null

Reason that the thread was locked. Defaults to null when no reason is recorded.

type: "locked"

Status discriminator that is always `locked`.

Closed { reason, type }

Indicates that a thread has been closed.

reason: string | null

Reason that the thread was closed. Defaults to null when no reason is recorded.

type: "closed"

Status discriminator that is always `closed`.

title: string | null

Optional human-readable title for the thread. Defaults to null when no title has been generated.

user: string

Free-form string that identifies your end user who owns the thread.

ChatKitThreadAssistantMessageItem { id, content, created\_at, 3 more }

Assistant-authored message within a thread.

id: string

Identifier of the thread item.

content: Array<[ChatKitResponseOutputText](/api/reference/typescript/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_response_output_text%20%3E%20(schema)) { annotations, text, type } >

Ordered assistant response segments.

annotations: Array<File { source, type }  | URL { source, type } >

Ordered list of annotations attached to the response text.

One of the following:

File { source, type }

Annotation that references an uploaded file.

source: Source { filename, type }

File attachment referenced by the annotation.

filename: string

Filename referenced by the annotation.

type: "file"

Type discriminator that is always `file`.

type: "file"

Type discriminator that is always `file` for this annotation.

URL { source, type }

Annotation that references a URL.

source: Source { type, url }

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

ChatKitThreadItemList { data, first\_id, has\_more, 2 more }

A paginated list of thread items rendered for the ChatKit API.

data: Array<[ChatKitThreadUserMessageItem](/api/reference/typescript/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_user_message_item%20%3E%20(schema)) { id, attachments, content, 5 more }  | [ChatKitThreadAssistantMessageItem](/api/reference/typescript/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_assistant_message_item%20%3E%20(schema)) { id, content, created\_at, 3 more }  | [ChatKitWidgetItem](/api/reference/typescript/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_widget_item%20%3E%20(schema)) { id, created\_at, object, 3 more }  | 3 more>

A list of items

One of the following:

ChatKitThreadUserMessageItem { id, attachments, content, 5 more }

User-authored messages within a thread.

id: string

Identifier of the thread item.

attachments: Array<[ChatKitAttachment](/api/reference/typescript/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_attachment%20%3E%20(schema)) { id, mime\_type, name, 2 more } >

Attachments associated with the user message. Defaults to an empty list.

id: string

Identifier for the attachment.

mime\_type: string

MIME type of the attachment.

name: string

Original display name for the attachment.

preview\_url: string | null

Preview URL for rendering the attachment inline.

formaturi

type: "image" | "file"

Attachment discriminator.

One of the following:

"image"

"file"

content: Array<InputText { text, type }  | QuotedText { text, type } >

Ordered content elements supplied by the user.

One of the following:

InputText { text, type }

Text block that a user contributed to the thread.

text: string

Plain-text content supplied by the user.

type: "input\_text"

Type discriminator that is always `input_text`.

QuotedText { text, type }

Quoted snippet that the user referenced in their message.

text: string

Quoted text content.

type: "quoted\_text"

Type discriminator that is always `quoted_text`.

created\_at: number

Unix timestamp (in seconds) for when the item was created.

formatunixtime

inference\_options: InferenceOptions | null

Inference overrides applied to the message. Defaults to null when unset.

model: string | null

Model name that generated the response. Defaults to null when using the session default.

tool\_choice: ToolChoice | null

Preferred tool to invoke. Defaults to null when ChatKit should auto-select.

id: string

Identifier of the requested tool.

object: "chatkit.thread\_item"

Type discriminator that is always `chatkit.thread_item`.

thread\_id: string

Identifier of the parent thread.

type: "chatkit.user\_message"

ChatKitThreadAssistantMessageItem { id, content, created\_at, 3 more }

Assistant-authored message within a thread.

id: string

Identifier of the thread item.

content: Array<[ChatKitResponseOutputText](/api/reference/typescript/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_response_output_text%20%3E%20(schema)) { annotations, text, type } >

Ordered assistant response segments.

annotations: Array<File { source, type }  | URL { source, type } >

Ordered list of annotations attached to the response text.

One of the following:

File { source, type }

Annotation that references an uploaded file.

source: Source { filename, type }

File attachment referenced by the annotation.

filename: string

Filename referenced by the annotation.

type: "file"

Type discriminator that is always `file`.

type: "file"

Type discriminator that is always `file` for this annotation.

URL { source, type }

Annotation that references a URL.

source: Source { type, url }

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

ChatKitWidgetItem { id, created\_at, object, 3 more }

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

ChatKitClientToolCall { id, arguments, call\_id, 7 more }

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

output: string | null

JSON-encoded output captured from the tool. Defaults to null while execution is in progress.

status: "in\_progress" | "completed"

Execution status for the tool call.

One of the following:

"in\_progress"

"completed"

thread\_id: string

Identifier of the parent thread.

type: "chatkit.client\_tool\_call"

Type discriminator that is always `chatkit.client_tool_call`.

ChatKitTask { id, created\_at, heading, 5 more }

Task emitted by the workflow to show progress and status updates.

id: string

Identifier of the thread item.

created\_at: number

Unix timestamp (in seconds) for when the item was created.

formatunixtime

heading: string | null

Optional heading for the task. Defaults to null when not provided.

object: "chatkit.thread\_item"

Type discriminator that is always `chatkit.thread_item`.

summary: string | null

Optional summary that describes the task. Defaults to null when omitted.

task\_type: "custom" | "thought"

Subtype for the task.

One of the following:

"custom"

"thought"

thread\_id: string

Identifier of the parent thread.

type: "chatkit.task"

Type discriminator that is always `chatkit.task`.

ChatKitTaskGroup { id, created\_at, object, 3 more }

Collection of workflow tasks grouped together in the thread.

id: string

Identifier of the thread item.

created\_at: number

Unix timestamp (in seconds) for when the item was created.

formatunixtime

object: "chatkit.thread\_item"

Type discriminator that is always `chatkit.thread_item`.

tasks: Array<Task>

Tasks included in the group.

heading: string | null

Optional heading for the grouped task. Defaults to null when not provided.

summary: string | null

Optional summary that describes the grouped task. Defaults to null when omitted.

type: "custom" | "thought"

Subtype for the grouped task.

One of the following:

"custom"

"thought"

thread\_id: string

Identifier of the parent thread.

type: "chatkit.task\_group"

Type discriminator that is always `chatkit.task_group`.

first\_id: string | null

The ID of the first item in the list.

has\_more: boolean

Whether there are more items available.

last\_id: string | null

The ID of the last item in the list.

object: "list"

The type of object returned, must be `list`.

ChatKitThreadUserMessageItem { id, attachments, content, 5 more }

User-authored messages within a thread.

id: string

Identifier of the thread item.

attachments: Array<[ChatKitAttachment](/api/reference/typescript/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_attachment%20%3E%20(schema)) { id, mime\_type, name, 2 more } >

Attachments associated with the user message. Defaults to an empty list.

id: string

Identifier for the attachment.

mime\_type: string

MIME type of the attachment.

name: string

Original display name for the attachment.

preview\_url: string | null

Preview URL for rendering the attachment inline.

formaturi

type: "image" | "file"

Attachment discriminator.

One of the following:

"image"

"file"

content: Array<InputText { text, type }  | QuotedText { text, type } >

Ordered content elements supplied by the user.

One of the following:

InputText { text, type }

Text block that a user contributed to the thread.

text: string

Plain-text content supplied by the user.

type: "input\_text"

Type discriminator that is always `input_text`.

QuotedText { text, type }

Quoted snippet that the user referenced in their message.

text: string

Quoted text content.

type: "quoted\_text"

Type discriminator that is always `quoted_text`.

created\_at: number

Unix timestamp (in seconds) for when the item was created.

formatunixtime

inference\_options: InferenceOptions | null

Inference overrides applied to the message. Defaults to null when unset.

model: string | null

Model name that generated the response. Defaults to null when using the session default.

tool\_choice: ToolChoice | null

Preferred tool to invoke. Defaults to null when ChatKit should auto-select.

id: string

Identifier of the requested tool.

object: "chatkit.thread\_item"

Type discriminator that is always `chatkit.thread_item`.

thread\_id: string

Identifier of the parent thread.

type: "chatkit.user\_message"

ChatKitWidgetItem { id, created\_at, object, 3 more }

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

ThreadDeleteResponse { id, deleted, object }

Confirmation payload returned after deleting a thread.

id: string

Identifier of the deleted thread.

deleted: boolean

Indicates that the thread has been deleted.

object: "chatkit.thread.deleted"

Type discriminator that is always `chatkit.thread.deleted`.

#### BetaAssistants

Build Assistants that can call models and use tools.

##### [List assistants](/api/reference/typescript/resources/beta/subresources/assistants/methods/list)

Deprecated

client.beta.assistants.list(AssistantListParams { after, before, limit, order } query?, RequestOptionsoptions?): CursorPage<[Assistant](/api/reference/typescript/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema)) { id, created\_at, description, 10 more } >

GET/assistants

##### [Create assistant](/api/reference/typescript/resources/beta/subresources/assistants/methods/create)

Deprecated

client.beta.assistants.create(AssistantCreateParams { model, description, instructions, 8 more } body, RequestOptionsoptions?): [Assistant](/api/reference/typescript/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema)) { id, created\_at, description, 10 more }

POST/assistants

##### [Retrieve assistant](/api/reference/typescript/resources/beta/subresources/assistants/methods/retrieve)

Deprecated

client.beta.assistants.retrieve(stringassistantID, RequestOptionsoptions?): [Assistant](/api/reference/typescript/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema)) { id, created\_at, description, 10 more }

GET/assistants/{assistant\_id}

##### [Modify assistant](/api/reference/typescript/resources/beta/subresources/assistants/methods/update)

Deprecated

client.beta.assistants.update(stringassistantID, AssistantUpdateParams { description, instructions, metadata, 8 more } body, RequestOptionsoptions?): [Assistant](/api/reference/typescript/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema)) { id, created\_at, description, 10 more }

POST/assistants/{assistant\_id}

##### [Delete assistant](/api/reference/typescript/resources/beta/subresources/assistants/methods/delete)

Deprecated

client.beta.assistants.delete(stringassistantID, RequestOptionsoptions?): [AssistantDeleted](/api/reference/typescript/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant_deleted%20%3E%20(schema)) { id, deleted, object }

DELETE/assistants/{assistant\_id}

##### ModelsExpand Collapse

Assistant { id, created\_at, description, 10 more }

Represents an `assistant` that can call the model and use tools.

id: string

The identifier, which can be referenced in API endpoints.

created\_at: number

The Unix timestamp (in seconds) for when the assistant was created.

formatunixtime

description: string | null

The description of the assistant. The maximum length is 512 characters.

maxLength512

instructions: string | null

The system instructions that the assistant uses. The maximum length is 256,000 characters.

maxLength256000

metadata: [Metadata](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema)) | null

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: string

ID of the model to use. You can use the [List models](https://platform.openai.com/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](https://platform.openai.com/docs/models) for descriptions of them.

name: string | null

The name of the assistant. The maximum length is 256 characters.

maxLength256

object: "assistant"

The object type, which is always `assistant`.

tools: Array<[AssistantTool](/api/reference/typescript/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant_tool%20%3E%20(schema))>

A list of tool enabled on the assistant. There can be a maximum of 128 tools per assistant. Tools can be of types `code_interpreter`, `file_search`, or `function`.

One of the following:

CodeInterpreterTool { type }

type: "code\_interpreter"

The type of tool being defined: `code_interpreter`

FileSearchTool { type, file\_search }

type: "file\_search"

The type of tool being defined: `file_search`

file\_search?: FileSearch { max\_num\_results, ranking\_options }

Overrides for the file search tool.

max\_num\_results?: number

The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

minimum1

maximum50

ranking\_options?: RankingOptions { score\_threshold, ranker }

The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score\_threshold of 0.

See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

score\_threshold: number

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

ranker?: "auto" | "default\_2024\_08\_21"

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

"default\_2024\_08\_21"

FunctionTool { function, type }

function: [FunctionDefinition](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema)) { name, description, parameters, strict }

type: "function"

The type of tool being defined: `function`

response\_format?: [AssistantResponseFormatOption](/api/reference/typescript/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20assistant_response_format_option%20%3E%20(schema)) | null

Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly “stuck” request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

temperature?: number | null

What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

minimum0

maximum2

tool\_resources?: ToolResources | null

A set of resources that are used by the assistant’s tools. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

code\_interpreter?: CodeInterpreter { file\_ids }

file\_ids?: Array<string>

A list of [file](https://platform.openai.com/docs/api-reference/files) IDs made available to the `code\_interpreter“ tool. There can be a maximum of 20 files associated with the tool.

file\_search?: FileSearch { vector\_store\_ids }

vector\_store\_ids?: Array<string>

The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) attached to this assistant. There can be a maximum of 1 vector store attached to the assistant.

top\_p?: number | null

An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top\_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.

We generally recommend altering this or temperature but not both.

minimum0

maximum1

AssistantDeleted { id, deleted, object }

id: string

deleted: boolean

object: "assistant.deleted"

AssistantStreamEvent = ThreadCreated { data, event, enabled }  | ThreadRunCreated { data, event }  | ThreadRunQueued { data, event }  | 21 more

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

ThreadCreated { data, event, enabled }

Occurs when a new [thread](https://platform.openai.com/docs/api-reference/threads/object) is created.

data: [Thread](/api/reference/typescript/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20thread%20%3E%20(schema)) { id, created\_at, metadata, 2 more }

Represents a thread that contains [messages](https://platform.openai.com/docs/api-reference/messages).

event: "thread.created"

enabled?: boolean

Whether to enable input audio transcription.

ThreadRunCreated { data, event }

Occurs when a new [run](https://platform.openai.com/docs/api-reference/runs/object) is created.

data: [Run](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: "thread.run.created"

ThreadRunQueued { data, event }

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) moves to a `queued` status.

data: [Run](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: "thread.run.queued"

ThreadRunInProgress { data, event }

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) moves to an `in_progress` status.

data: [Run](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: "thread.run.in\_progress"

ThreadRunRequiresAction { data, event }

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) moves to a `requires_action` status.

data: [Run](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: "thread.run.requires\_action"

ThreadRunCompleted { data, event }

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) is completed.

data: [Run](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: "thread.run.completed"

ThreadRunIncomplete { data, event }

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) ends with status `incomplete`.

data: [Run](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: "thread.run.incomplete"

ThreadRunFailed { data, event }

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) fails.

data: [Run](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: "thread.run.failed"

ThreadRunCancelling { data, event }

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) moves to a `cancelling` status.

data: [Run](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: "thread.run.cancelling"

ThreadRunCancelled { data, event }

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) is cancelled.

data: [Run](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: "thread.run.cancelled"

ThreadRunExpired { data, event }

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) expires.

data: [Run](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: "thread.run.expired"

ThreadRunStepCreated { data, event }

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) is created.

data: [RunStep](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 13 more }

Represents a step in execution of a run.

event: "thread.run.step.created"

ThreadRunStepInProgress { data, event }

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) moves to an `in_progress` state.

data: [RunStep](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 13 more }

Represents a step in execution of a run.

event: "thread.run.step.in\_progress"

ThreadRunStepDelta { data, event }

Occurs when parts of a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) are being streamed.

data: [RunStepDeltaEvent](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta_event%20%3E%20(schema)) { id, delta, object }

Represents a run step delta i.e. any changed fields on a run step during streaming.

event: "thread.run.step.delta"

ThreadRunStepCompleted { data, event }

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) is completed.

data: [RunStep](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 13 more }

Represents a step in execution of a run.

event: "thread.run.step.completed"

ThreadRunStepFailed { data, event }

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) fails.

data: [RunStep](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 13 more }

Represents a step in execution of a run.

event: "thread.run.step.failed"

ThreadRunStepCancelled { data, event }

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) is cancelled.

data: [RunStep](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 13 more }

Represents a step in execution of a run.

event: "thread.run.step.cancelled"

ThreadRunStepExpired { data, event }

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) expires.

data: [RunStep](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 13 more }

Represents a step in execution of a run.

event: "thread.run.step.expired"

ThreadMessageCreated { data, event }

Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) is created.

data: [Message](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)) { id, assistant\_id, attachments, 11 more }

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

event: "thread.message.created"

ThreadMessageInProgress { data, event }

Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) moves to an `in_progress` state.

data: [Message](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)) { id, assistant\_id, attachments, 11 more }

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

event: "thread.message.in\_progress"

ThreadMessageDelta { data, event }

Occurs when parts of a [Message](https://platform.openai.com/docs/api-reference/messages/object) are being streamed.

data: [MessageDeltaEvent](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_delta_event%20%3E%20(schema)) { id, delta, object }

Represents a message delta i.e. any changed fields on a message during streaming.

event: "thread.message.delta"

ThreadMessageCompleted { data, event }

Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) is completed.

data: [Message](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)) { id, assistant\_id, attachments, 11 more }

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

event: "thread.message.completed"

ThreadMessageIncomplete { data, event }

Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) ends before it is completed.

data: [Message](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)) { id, assistant\_id, attachments, 11 more }

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

event: "thread.message.incomplete"

ErrorEvent { data, event }

Occurs when an [error](https://platform.openai.com/docs/guides/error-codes#api-errors) occurs. This can happen due to an internal server error or a timeout.

data: [ErrorObject](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20error_object%20%3E%20(schema)) { code, message, param, type }

event: "error"

AssistantTool = [CodeInterpreterTool](/api/reference/typescript/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20code_interpreter_tool%20%3E%20(schema)) { type }  | [FileSearchTool](/api/reference/typescript/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20file_search_tool%20%3E%20(schema)) { type, file\_search }  | [FunctionTool](/api/reference/typescript/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20function_tool%20%3E%20(schema)) { function, type }

One of the following:

CodeInterpreterTool { type }

type: "code\_interpreter"

The type of tool being defined: `code_interpreter`

FileSearchTool { type, file\_search }

type: "file\_search"

The type of tool being defined: `file_search`

file\_search?: FileSearch { max\_num\_results, ranking\_options }

Overrides for the file search tool.

max\_num\_results?: number

The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

minimum1

maximum50

ranking\_options?: RankingOptions { score\_threshold, ranker }

The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score\_threshold of 0.

See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

score\_threshold: number

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

ranker?: "auto" | "default\_2024\_08\_21"

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

"default\_2024\_08\_21"

FunctionTool { function, type }

function: [FunctionDefinition](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema)) { name, description, parameters, strict }

type: "function"

The type of tool being defined: `function`

CodeInterpreterTool { type }

type: "code\_interpreter"

The type of tool being defined: `code_interpreter`

FileSearchTool { type, file\_search }

type: "file\_search"

The type of tool being defined: `file_search`

file\_search?: FileSearch { max\_num\_results, ranking\_options }

Overrides for the file search tool.

max\_num\_results?: number

The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

minimum1

maximum50

ranking\_options?: RankingOptions { score\_threshold, ranker }

The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score\_threshold of 0.

See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

score\_threshold: number

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

ranker?: "auto" | "default\_2024\_08\_21"

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

"default\_2024\_08\_21"

FunctionTool { function, type }

function: [FunctionDefinition](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema)) { name, description, parameters, strict }

type: "function"

The type of tool being defined: `function`

MessageStreamEvent = ThreadMessageCreated { data, event }  | ThreadMessageInProgress { data, event }  | ThreadMessageDelta { data, event }  | 2 more

Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) is created.

One of the following:

ThreadMessageCreated { data, event }

Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) is created.

data: [Message](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)) { id, assistant\_id, attachments, 11 more }

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

event: "thread.message.created"

ThreadMessageInProgress { data, event }

Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) moves to an `in_progress` state.

data: [Message](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)) { id, assistant\_id, attachments, 11 more }

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

event: "thread.message.in\_progress"

ThreadMessageDelta { data, event }

Occurs when parts of a [Message](https://platform.openai.com/docs/api-reference/messages/object) are being streamed.

data: [MessageDeltaEvent](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_delta_event%20%3E%20(schema)) { id, delta, object }

Represents a message delta i.e. any changed fields on a message during streaming.

event: "thread.message.delta"

ThreadMessageCompleted { data, event }

Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) is completed.

data: [Message](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)) { id, assistant\_id, attachments, 11 more }

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

event: "thread.message.completed"

ThreadMessageIncomplete { data, event }

Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) ends before it is completed.

data: [Message](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)) { id, assistant\_id, attachments, 11 more }

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

event: "thread.message.incomplete"

RunStepStreamEvent = ThreadRunStepCreated { data, event }  | ThreadRunStepInProgress { data, event }  | ThreadRunStepDelta { data, event }  | 4 more

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) is created.

One of the following:

ThreadRunStepCreated { data, event }

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) is created.

data: [RunStep](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 13 more }

Represents a step in execution of a run.

event: "thread.run.step.created"

ThreadRunStepInProgress { data, event }

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) moves to an `in_progress` state.

data: [RunStep](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 13 more }

Represents a step in execution of a run.

event: "thread.run.step.in\_progress"

ThreadRunStepDelta { data, event }

Occurs when parts of a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) are being streamed.

data: [RunStepDeltaEvent](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta_event%20%3E%20(schema)) { id, delta, object }

Represents a run step delta i.e. any changed fields on a run step during streaming.

event: "thread.run.step.delta"

ThreadRunStepCompleted { data, event }

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) is completed.

data: [RunStep](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 13 more }

Represents a step in execution of a run.

event: "thread.run.step.completed"

ThreadRunStepFailed { data, event }

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) fails.

data: [RunStep](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 13 more }

Represents a step in execution of a run.

event: "thread.run.step.failed"

ThreadRunStepCancelled { data, event }

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) is cancelled.

data: [RunStep](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 13 more }

Represents a step in execution of a run.

event: "thread.run.step.cancelled"

ThreadRunStepExpired { data, event }

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) expires.

data: [RunStep](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 13 more }

Represents a step in execution of a run.

event: "thread.run.step.expired"

RunStreamEvent = ThreadRunCreated { data, event }  | ThreadRunQueued { data, event }  | ThreadRunInProgress { data, event }  | 7 more

Occurs when a new [run](https://platform.openai.com/docs/api-reference/runs/object) is created.

One of the following:

ThreadRunCreated { data, event }

Occurs when a new [run](https://platform.openai.com/docs/api-reference/runs/object) is created.

data: [Run](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: "thread.run.created"

ThreadRunQueued { data, event }

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) moves to a `queued` status.

data: [Run](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: "thread.run.queued"

ThreadRunInProgress { data, event }

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) moves to an `in_progress` status.

data: [Run](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: "thread.run.in\_progress"

ThreadRunRequiresAction { data, event }

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) moves to a `requires_action` status.

data: [Run](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: "thread.run.requires\_action"

ThreadRunCompleted { data, event }

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) is completed.

data: [Run](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: "thread.run.completed"

ThreadRunIncomplete { data, event }

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) ends with status `incomplete`.

data: [Run](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: "thread.run.incomplete"

ThreadRunFailed { data, event }

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) fails.

data: [Run](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: "thread.run.failed"

ThreadRunCancelling { data, event }

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) moves to a `cancelling` status.

data: [Run](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: "thread.run.cancelling"

ThreadRunCancelled { data, event }

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) is cancelled.

data: [Run](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: "thread.run.cancelled"

ThreadRunExpired { data, event }

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) expires.

data: [Run](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: "thread.run.expired"

ThreadStreamEvent { data, event, enabled }

Occurs when a new [thread](https://platform.openai.com/docs/api-reference/threads/object) is created.

data: [Thread](/api/reference/typescript/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20thread%20%3E%20(schema)) { id, created\_at, metadata, 2 more }

Represents a thread that contains [messages](https://platform.openai.com/docs/api-reference/messages).

event: "thread.created"

enabled?: boolean

Whether to enable input audio transcription.

#### BetaThreads

Build Assistants that can call models and use tools.

##### [Create thread](/api/reference/typescript/resources/beta/subresources/threads/methods/create)

Deprecated

client.beta.threads.create(ThreadCreateParams { messages, metadata, tool\_resources } body?, RequestOptionsoptions?): [Thread](/api/reference/typescript/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20thread%20%3E%20(schema)) { id, created\_at, metadata, 2 more }

POST/threads

##### [Create thread and run](/api/reference/typescript/resources/beta/subresources/threads/methods/create_and_run)

Deprecated

client.beta.threads.createAndRun(ThreadCreateAndRunParamsbody, RequestOptionsoptions?): [Run](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }  | Stream<[AssistantStreamEvent](/api/reference/typescript/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema))>

POST/threads/runs

##### [Retrieve thread](/api/reference/typescript/resources/beta/subresources/threads/methods/retrieve)

Deprecated

client.beta.threads.retrieve(stringthreadID, RequestOptionsoptions?): [Thread](/api/reference/typescript/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20thread%20%3E%20(schema)) { id, created\_at, metadata, 2 more }

GET/threads/{thread\_id}

##### [Modify thread](/api/reference/typescript/resources/beta/subresources/threads/methods/update)

Deprecated

client.beta.threads.update(stringthreadID, ThreadUpdateParams { metadata, tool\_resources } body, RequestOptionsoptions?): [Thread](/api/reference/typescript/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20thread%20%3E%20(schema)) { id, created\_at, metadata, 2 more }

POST/threads/{thread\_id}

##### [Delete thread](/api/reference/typescript/resources/beta/subresources/threads/methods/delete)

Deprecated

client.beta.threads.delete(stringthreadID, RequestOptionsoptions?): [ThreadDeleted](/api/reference/typescript/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20thread_deleted%20%3E%20(schema)) { id, deleted, object }

DELETE/threads/{thread\_id}

##### ModelsExpand Collapse

AssistantResponseFormatOption = "auto" | [ResponseFormatText](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20response_format_text%20%3E%20(schema)) { type }  | [ResponseFormatJSONObject](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20response_format_json_object%20%3E%20(schema)) { type }  | [ResponseFormatJSONSchema](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)) { json\_schema, type }

Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly “stuck” request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

One of the following:

"auto"

"auto"

ResponseFormatText { type }

Default response format. Used to generate text responses.

type: "text"

The type of response format being defined. Always `text`.

ResponseFormatJSONObject { type }

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type: "json\_object"

The type of response format being defined. Always `json_object`.

ResponseFormatJSONSchema { json\_schema, type }

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

json\_schema: JSONSchema { name, description, schema, strict }

Structured Outputs configuration options, including a JSON Schema.

name: string

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

description?: string

A description of what the response format is for, used by the model to
determine how to respond in the format.

schema?: Record<string, unknown>

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

strict?: boolean | null

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

type: "json\_schema"

The type of response format being defined. Always `json_schema`.

AssistantToolChoice { type, function }

Specifies a tool the model should use. Use to force the model to call a specific tool.

type: "function" | "code\_interpreter" | "file\_search"

The type of the tool. If type is `function`, the function name must be set

One of the following:

"function"

"code\_interpreter"

"file\_search"

function?: [AssistantToolChoiceFunction](/api/reference/typescript/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_function%20%3E%20(schema)) { name }

AssistantToolChoiceFunction { name }

name: string

The name of the function to call.

AssistantToolChoiceOption = "none" | "auto" | "required" | [AssistantToolChoice](/api/reference/typescript/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice%20%3E%20(schema)) { type, function }

Controls which (if any) tool is called by the model.
`none` means the model will not call any tools and instead generates a message.
`auto` is the default value and means the model can pick between generating a message or calling one or more tools.
`required` means the model must call one or more tools before responding to the user.
Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

One of the following:

"none" | "auto" | "required"

"none"

"auto"

"required"

AssistantToolChoice { type, function }

Specifies a tool the model should use. Use to force the model to call a specific tool.

type: "function" | "code\_interpreter" | "file\_search"

The type of the tool. If type is `function`, the function name must be set

One of the following:

"function"

"code\_interpreter"

"file\_search"

function?: [AssistantToolChoiceFunction](/api/reference/typescript/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_function%20%3E%20(schema)) { name }

Thread { id, created\_at, metadata, 2 more }

Represents a thread that contains [messages](https://platform.openai.com/docs/api-reference/messages).

id: string

The identifier, which can be referenced in API endpoints.

created\_at: number

The Unix timestamp (in seconds) for when the thread was created.

formatunixtime

metadata: [Metadata](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema)) | null

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

object: "thread"

The object type, which is always `thread`.

tool\_resources: ToolResources | null

A set of resources that are made available to the assistant’s tools in this thread. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

code\_interpreter?: CodeInterpreter { file\_ids }

file\_ids?: Array<string>

A list of [file](https://platform.openai.com/docs/api-reference/files) IDs made available to the `code_interpreter` tool. There can be a maximum of 20 files associated with the tool.

file\_search?: FileSearch { vector\_store\_ids }

vector\_store\_ids?: Array<string>

The [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) attached to this thread. There can be a maximum of 1 vector store attached to the thread.

ThreadDeleted { id, deleted, object }

id: string

deleted: boolean

object: "thread.deleted"

#### BetaThreadsRuns

Build Assistants that can call models and use tools.

##### [List runs](/api/reference/typescript/resources/beta/subresources/threads/subresources/runs/methods/list)

Deprecated

client.beta.threads.runs.list(stringthreadID, RunListParams { after, before, limit, order } query?, RequestOptionsoptions?): CursorPage<[Run](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more } >

GET/threads/{thread\_id}/runs

##### [Create run](/api/reference/typescript/resources/beta/subresources/threads/subresources/runs/methods/create)

Deprecated

client.beta.threads.runs.create(stringthreadID, RunCreateParamsparams, RequestOptionsoptions?): [Run](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }  | Stream<[AssistantStreamEvent](/api/reference/typescript/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema))>

POST/threads/{thread\_id}/runs

##### [Retrieve run](/api/reference/typescript/resources/beta/subresources/threads/subresources/runs/methods/retrieve)

Deprecated

client.beta.threads.runs.retrieve(stringrunID, RunRetrieveParams { thread\_id } params, RequestOptionsoptions?): [Run](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

GET/threads/{thread\_id}/runs/{run\_id}

##### [Modify run](/api/reference/typescript/resources/beta/subresources/threads/subresources/runs/methods/update)

Deprecated

client.beta.threads.runs.update(stringrunID, RunUpdateParams { thread\_id, metadata } params, RequestOptionsoptions?): [Run](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

POST/threads/{thread\_id}/runs/{run\_id}

##### [Submit tool outputs to run](/api/reference/typescript/resources/beta/subresources/threads/subresources/runs/methods/submit_tool_outputs)

Deprecated

client.beta.threads.runs.submitToolOutputs(stringrunID, RunSubmitToolOutputsParamsparams, RequestOptionsoptions?): [Run](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }  | Stream<[AssistantStreamEvent](/api/reference/typescript/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema))>

POST/threads/{thread\_id}/runs/{run\_id}/submit\_tool\_outputs

##### [Cancel a run](/api/reference/typescript/resources/beta/subresources/threads/subresources/runs/methods/cancel)

Deprecated

client.beta.threads.runs.cancel(stringrunID, RunCancelParams { thread\_id } params, RequestOptionsoptions?): [Run](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

POST/threads/{thread\_id}/runs/{run\_id}/cancel

##### ModelsExpand Collapse

RequiredActionFunctionToolCall { id, function, type }

Tool call objects

id: string

The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

function: Function { arguments, name }

The function definition.

arguments: string

The arguments that the model expects you to pass to the function.

name: string

The name of the function.

type: "function"

The type of tool call the output is required for. For now, this is always `function`.

Run { id, assistant\_id, cancelled\_at, 24 more }

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

id: string

The identifier, which can be referenced in API endpoints.

assistant\_id: string

The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for execution of this run.

cancelled\_at: number | null

The Unix timestamp (in seconds) for when the run was cancelled.

formatunixtime

completed\_at: number | null

The Unix timestamp (in seconds) for when the run was completed.

formatunixtime

created\_at: number

The Unix timestamp (in seconds) for when the run was created.

formatunixtime

expires\_at: number | null

The Unix timestamp (in seconds) for when the run will expire.

formatunixtime

failed\_at: number | null

The Unix timestamp (in seconds) for when the run failed.

formatunixtime

incomplete\_details: IncompleteDetails | null

Details on why the run is incomplete. Will be `null` if the run is not incomplete.

reason?: "max\_completion\_tokens" | "max\_prompt\_tokens"

The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

One of the following:

"max\_completion\_tokens"

"max\_prompt\_tokens"

instructions: string

The instructions that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

last\_error: LastError | null

The last error associated with this run. Will be `null` if there are no errors.

code: "server\_error" | "rate\_limit\_exceeded" | "invalid\_prompt"

One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

One of the following:

"server\_error"

"rate\_limit\_exceeded"

"invalid\_prompt"

message: string

A human-readable description of the error.

max\_completion\_tokens: number | null

The maximum number of completion tokens specified to have been used over the course of the run.

minimum256

max\_prompt\_tokens: number | null

The maximum number of prompt tokens specified to have been used over the course of the run.

minimum256

metadata: [Metadata](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema)) | null

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: string

The model that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

object: "thread.run"

The object type, which is always `thread.run`.

parallel\_tool\_calls: boolean

Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

required\_action: RequiredAction | null

Details on the action required to continue the run. Will be `null` if no action is required.

submit\_tool\_outputs: SubmitToolOutputs { tool\_calls }

Details on the tool outputs needed for this run to continue.

tool\_calls: Array<[RequiredActionFunctionToolCall](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20required_action_function_tool_call%20%3E%20(schema)) { id, function, type } >

A list of the relevant tool calls.

id: string

The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

function: Function { arguments, name }

The function definition.

arguments: string

The arguments that the model expects you to pass to the function.

name: string

The name of the function.

type: "function"

The type of tool call the output is required for. For now, this is always `function`.

type: "submit\_tool\_outputs"

For now, this is always `submit_tool_outputs`.

response\_format: [AssistantResponseFormatOption](/api/reference/typescript/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20assistant_response_format_option%20%3E%20(schema)) | null

Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly “stuck” request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

started\_at: number | null

The Unix timestamp (in seconds) for when the run was started.

formatunixtime

status: [RunStatus](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run_status%20%3E%20(schema))

The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

thread\_id: string

The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

tool\_choice: [AssistantToolChoiceOption](/api/reference/typescript/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_option%20%3E%20(schema)) | null

Controls which (if any) tool is called by the model.
`none` means the model will not call any tools and instead generates a message.
`auto` is the default value and means the model can pick between generating a message or calling one or more tools.
`required` means the model must call one or more tools before responding to the user.
Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

tools: Array<[AssistantTool](/api/reference/typescript/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant_tool%20%3E%20(schema))>

The list of tools that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

One of the following:

CodeInterpreterTool { type }

type: "code\_interpreter"

The type of tool being defined: `code_interpreter`

FileSearchTool { type, file\_search }

type: "file\_search"

The type of tool being defined: `file_search`

file\_search?: FileSearch { max\_num\_results, ranking\_options }

Overrides for the file search tool.

max\_num\_results?: number

The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

minimum1

maximum50

ranking\_options?: RankingOptions { score\_threshold, ranker }

The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score\_threshold of 0.

See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

score\_threshold: number

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

ranker?: "auto" | "default\_2024\_08\_21"

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

"default\_2024\_08\_21"

FunctionTool { function, type }

function: [FunctionDefinition](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema)) { name, description, parameters, strict }

type: "function"

The type of tool being defined: `function`

truncation\_strategy: TruncationStrategy | null

Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

type: "auto" | "last\_messages"

The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

One of the following:

"auto"

"last\_messages"

last\_messages?: number | null

The number of most recent messages from the thread when constructing the context for the run.

minimum1

usage: Usage | null

Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

completion\_tokens: number

Number of completion tokens used over the course of the run.

prompt\_tokens: number

Number of prompt tokens used over the course of the run.

total\_tokens: number

Total number of tokens used (prompt + completion).

temperature?: number | null

The sampling temperature used for this run. If not set, defaults to 1.

top\_p?: number | null

The nucleus sampling value used for this run. If not set, defaults to 1.

RunStatus = "queued" | "in\_progress" | "requires\_action" | 6 more

The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

One of the following:

"queued"

"in\_progress"

"requires\_action"

"cancelling"

"cancelled"

"failed"

"completed"

"incomplete"

"expired"

#### BetaThreadsRunsSteps

Build Assistants that can call models and use tools.

##### [List run steps](/api/reference/typescript/resources/beta/subresources/threads/subresources/runs/subresources/steps/methods/list)

Deprecated

client.beta.threads.runs.steps.list(stringrunID, StepListParams { thread\_id, after, before, 3 more } params, RequestOptionsoptions?): CursorPage<[RunStep](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 13 more } >

GET/threads/{thread\_id}/runs/{run\_id}/steps

##### [Retrieve run step](/api/reference/typescript/resources/beta/subresources/threads/subresources/runs/subresources/steps/methods/retrieve)

Deprecated

client.beta.threads.runs.steps.retrieve(stringstepID, StepRetrieveParams { thread\_id, run\_id, include } params, RequestOptionsoptions?): [RunStep](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 13 more }

GET/threads/{thread\_id}/runs/{run\_id}/steps/{step\_id}

##### ModelsExpand Collapse

CodeInterpreterLogs { index, type, logs }

Text output from the Code Interpreter tool call as part of a run step.

index: number

The index of the output in the outputs array.

type: "logs"

Always `logs`.

logs?: string

The text output from the Code Interpreter tool call.

CodeInterpreterOutputImage { index, type, image }

index: number

The index of the output in the outputs array.

type: "image"

Always `image`.

image?: Image { file\_id }

file\_id?: string

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

CodeInterpreterToolCall { id, code\_interpreter, type }

Details of the Code Interpreter tool call the run step was involved in.

id: string

The ID of the tool call.

code\_interpreter: CodeInterpreter { input, outputs }

The Code Interpreter tool call definition.

input: string

The input to the Code Interpreter tool call.

outputs: Array<Logs { logs, type }  | Image { image, type } >

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

Logs { logs, type }

Text output from the Code Interpreter tool call as part of a run step.

logs: string

The text output from the Code Interpreter tool call.

type: "logs"

Always `logs`.

Image { image, type }

image: Image { file\_id }

file\_id: string

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

type: "image"

Always `image`.

type: "code\_interpreter"

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

CodeInterpreterToolCallDelta { index, type, id, code\_interpreter }

Details of the Code Interpreter tool call the run step was involved in.

index: number

The index of the tool call in the tool calls array.

type: "code\_interpreter"

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

id?: string

The ID of the tool call.

code\_interpreter?: CodeInterpreter { input, outputs }

The Code Interpreter tool call definition.

input?: string

The input to the Code Interpreter tool call.

outputs?: Array<[CodeInterpreterLogs](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema)) { index, type, logs }  | [CodeInterpreterOutputImage](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)) { index, type, image } >

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

CodeInterpreterLogs { index, type, logs }

Text output from the Code Interpreter tool call as part of a run step.

index: number

The index of the output in the outputs array.

type: "logs"

Always `logs`.

logs?: string

The text output from the Code Interpreter tool call.

CodeInterpreterOutputImage { index, type, image }

index: number

The index of the output in the outputs array.

type: "image"

Always `image`.

image?: Image { file\_id }

file\_id?: string

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

FileSearchToolCall { id, file\_search, type }

id: string

The ID of the tool call object.

file\_search: FileSearch { ranking\_options, results }

For now, this is always going to be an empty object.

ranking\_options?: RankingOptions { ranker, score\_threshold }

The ranking options for the file search.

ranker: "auto" | "default\_2024\_08\_21"

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

"default\_2024\_08\_21"

score\_threshold: number

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

results?: Array<Result>

The results of the file search.

file\_id: string

The ID of the file that result was found in.

file\_name: string

The name of the file that result was found in.

score: number

The score of the result. All values must be a floating point number between 0 and 1.

minimum0

maximum1

content?: Array<Content>

The content of the result that was found. The content is only included if requested via the include query parameter.

text?: string

The text content of the file.

type?: "text"

The type of the content.

type: "file\_search"

The type of tool call. This is always going to be `file_search` for this type of tool call.

FileSearchToolCallDelta { file\_search, index, type, id }

file\_search: unknown

For now, this is always going to be an empty object.

index: number

The index of the tool call in the tool calls array.

type: "file\_search"

The type of tool call. This is always going to be `file_search` for this type of tool call.

id?: string

The ID of the tool call object.

FunctionToolCall { id, function, type }

id: string

The ID of the tool call object.

function: Function { arguments, name, output }

The definition of the function that was called.

arguments: string

The arguments passed to the function.

name: string

The name of the function.

output: string | null

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

type: "function"

The type of tool call. This is always going to be `function` for this type of tool call.

FunctionToolCallDelta { index, type, id, function }

index: number

The index of the tool call in the tool calls array.

type: "function"

The type of tool call. This is always going to be `function` for this type of tool call.

id?: string

The ID of the tool call object.

function?: Function { arguments, name, output }

The definition of the function that was called.

arguments?: string

The arguments passed to the function.

name?: string

The name of the function.

output?: string | null

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

MessageCreationStepDetails { message\_creation, type }

Details of the message creation by the run step.

message\_creation: MessageCreation { message\_id }

message\_id: string

The ID of the message that was created by this run step.

type: "message\_creation"

Always `message_creation`.

RunStep { id, assistant\_id, cancelled\_at, 13 more }

Represents a step in execution of a run.

id: string

The identifier of the run step, which can be referenced in API endpoints.

assistant\_id: string

The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) associated with the run step.

cancelled\_at: number | null

The Unix timestamp (in seconds) for when the run step was cancelled.

formatunixtime

completed\_at: number | null

The Unix timestamp (in seconds) for when the run step completed.

formatunixtime

created\_at: number

The Unix timestamp (in seconds) for when the run step was created.

formatunixtime

expired\_at: number | null

The Unix timestamp (in seconds) for when the run step expired. A step is considered expired if the parent run is expired.

formatunixtime

failed\_at: number | null

The Unix timestamp (in seconds) for when the run step failed.

formatunixtime

last\_error: LastError | null

The last error associated with this run step. Will be `null` if there are no errors.

code: "server\_error" | "rate\_limit\_exceeded"

One of `server_error` or `rate_limit_exceeded`.

One of the following:

"server\_error"

"rate\_limit\_exceeded"

message: string

A human-readable description of the error.

metadata: [Metadata](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema)) | null

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

object: "thread.run.step"

The object type, which is always `thread.run.step`.

run\_id: string

The ID of the [run](https://platform.openai.com/docs/api-reference/runs) that this run step is a part of.

status: "in\_progress" | "cancelled" | "failed" | 2 more

The status of the run step, which can be either `in_progress`, `cancelled`, `failed`, `completed`, or `expired`.

One of the following:

"in\_progress"

"cancelled"

"failed"

"completed"

"expired"

step\_details: [MessageCreationStepDetails](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20message_creation_step_details%20%3E%20(schema)) { message\_creation, type }  | [ToolCallsStepDetails](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_calls_step_details%20%3E%20(schema)) { tool\_calls, type }

The details of the run step.

One of the following:

MessageCreationStepDetails { message\_creation, type }

Details of the message creation by the run step.

message\_creation: MessageCreation { message\_id }

message\_id: string

The ID of the message that was created by this run step.

type: "message\_creation"

Always `message_creation`.

ToolCallsStepDetails { tool\_calls, type }

Details of the tool call.

tool\_calls: Array<[ToolCall](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call%20%3E%20(schema))>

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

One of the following:

CodeInterpreterToolCall { id, code\_interpreter, type }

Details of the Code Interpreter tool call the run step was involved in.

id: string

The ID of the tool call.

code\_interpreter: CodeInterpreter { input, outputs }

The Code Interpreter tool call definition.

input: string

The input to the Code Interpreter tool call.

outputs: Array<Logs { logs, type }  | Image { image, type } >

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

Logs { logs, type }

Text output from the Code Interpreter tool call as part of a run step.

logs: string

The text output from the Code Interpreter tool call.

type: "logs"

Always `logs`.

Image { image, type }

image: Image { file\_id }

file\_id: string

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

type: "image"

Always `image`.

type: "code\_interpreter"

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

FileSearchToolCall { id, file\_search, type }

id: string

The ID of the tool call object.

file\_search: FileSearch { ranking\_options, results }

For now, this is always going to be an empty object.

ranking\_options?: RankingOptions { ranker, score\_threshold }

The ranking options for the file search.

ranker: "auto" | "default\_2024\_08\_21"

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

"default\_2024\_08\_21"

score\_threshold: number

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

results?: Array<Result>

The results of the file search.

file\_id: string

The ID of the file that result was found in.

file\_name: string

The name of the file that result was found in.

score: number

The score of the result. All values must be a floating point number between 0 and 1.

minimum0

maximum1

content?: Array<Content>

The content of the result that was found. The content is only included if requested via the include query parameter.

text?: string

The text content of the file.

type?: "text"

The type of the content.

type: "file\_search"

The type of tool call. This is always going to be `file_search` for this type of tool call.

FunctionToolCall { id, function, type }

id: string

The ID of the tool call object.

function: Function { arguments, name, output }

The definition of the function that was called.

arguments: string

The arguments passed to the function.

name: string

The name of the function.

output: string | null

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

type: "function"

The type of tool call. This is always going to be `function` for this type of tool call.

type: "tool\_calls"

Always `tool_calls`.

thread\_id: string

The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was run.

type: "message\_creation" | "tool\_calls"

The type of run step, which can be either `message_creation` or `tool_calls`.

One of the following:

"message\_creation"

"tool\_calls"

usage: Usage | null

Usage statistics related to the run step. This value will be `null` while the run step’s status is `in_progress`.

completion\_tokens: number

Number of completion tokens used over the course of the run step.

prompt\_tokens: number

Number of prompt tokens used over the course of the run step.

total\_tokens: number

Total number of tokens used (prompt + completion).

RunStepDelta { step\_details }

The delta containing the fields that have changed on the run step.

step\_details?: [RunStepDeltaMessageDelta](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta_message_delta%20%3E%20(schema)) { type, message\_creation }  | [ToolCallDeltaObject](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call_delta_object%20%3E%20(schema)) { type, tool\_calls }

The details of the run step.

One of the following:

RunStepDeltaMessageDelta { type, message\_creation }

Details of the message creation by the run step.

type: "message\_creation"

Always `message_creation`.

message\_creation?: MessageCreation { message\_id }

message\_id?: string

The ID of the message that was created by this run step.

ToolCallDeltaObject { type, tool\_calls }

Details of the tool call.

type: "tool\_calls"

Always `tool_calls`.

tool\_calls?: Array<[ToolCallDelta](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call_delta%20%3E%20(schema))>

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

One of the following:

CodeInterpreterToolCallDelta { index, type, id, code\_interpreter }

Details of the Code Interpreter tool call the run step was involved in.

index: number

The index of the tool call in the tool calls array.

type: "code\_interpreter"

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

id?: string

The ID of the tool call.

code\_interpreter?: CodeInterpreter { input, outputs }

The Code Interpreter tool call definition.

input?: string

The input to the Code Interpreter tool call.

outputs?: Array<[CodeInterpreterLogs](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema)) { index, type, logs }  | [CodeInterpreterOutputImage](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)) { index, type, image } >

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

CodeInterpreterLogs { index, type, logs }

Text output from the Code Interpreter tool call as part of a run step.

index: number

The index of the output in the outputs array.

type: "logs"

Always `logs`.

logs?: string

The text output from the Code Interpreter tool call.

CodeInterpreterOutputImage { index, type, image }

index: number

The index of the output in the outputs array.

type: "image"

Always `image`.

image?: Image { file\_id }

file\_id?: string

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

FileSearchToolCallDelta { file\_search, index, type, id }

file\_search: unknown

For now, this is always going to be an empty object.

index: number

The index of the tool call in the tool calls array.

type: "file\_search"

The type of tool call. This is always going to be `file_search` for this type of tool call.

id?: string

The ID of the tool call object.

FunctionToolCallDelta { index, type, id, function }

index: number

The index of the tool call in the tool calls array.

type: "function"

The type of tool call. This is always going to be `function` for this type of tool call.

id?: string

The ID of the tool call object.

function?: Function { arguments, name, output }

The definition of the function that was called.

arguments?: string

The arguments passed to the function.

name?: string

The name of the function.

output?: string | null

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

RunStepDeltaEvent { id, delta, object }

Represents a run step delta i.e. any changed fields on a run step during streaming.

id: string

The identifier of the run step, which can be referenced in API endpoints.

delta: [RunStepDelta](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta%20%3E%20(schema)) { step\_details }

The delta containing the fields that have changed on the run step.

object: "thread.run.step.delta"

The object type, which is always `thread.run.step.delta`.

RunStepDeltaMessageDelta { type, message\_creation }

Details of the message creation by the run step.

type: "message\_creation"

Always `message_creation`.

message\_creation?: MessageCreation { message\_id }

message\_id?: string

The ID of the message that was created by this run step.

RunStepInclude = "step\_details.tool\_calls[\*].file\_search.results[\*].content"

ToolCall = [CodeInterpreterToolCall](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)) { id, code\_interpreter, type }  | [FileSearchToolCall](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)) { id, file\_search, type }  | [FunctionToolCall](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema)) { id, function, type }

Details of the Code Interpreter tool call the run step was involved in.

One of the following:

CodeInterpreterToolCall { id, code\_interpreter, type }

Details of the Code Interpreter tool call the run step was involved in.

id: string

The ID of the tool call.

code\_interpreter: CodeInterpreter { input, outputs }

The Code Interpreter tool call definition.

input: string

The input to the Code Interpreter tool call.

outputs: Array<Logs { logs, type }  | Image { image, type } >

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

Logs { logs, type }

Text output from the Code Interpreter tool call as part of a run step.

logs: string

The text output from the Code Interpreter tool call.

type: "logs"

Always `logs`.

Image { image, type }

image: Image { file\_id }

file\_id: string

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

type: "image"

Always `image`.

type: "code\_interpreter"

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

FileSearchToolCall { id, file\_search, type }

id: string

The ID of the tool call object.

file\_search: FileSearch { ranking\_options, results }

For now, this is always going to be an empty object.

ranking\_options?: RankingOptions { ranker, score\_threshold }

The ranking options for the file search.

ranker: "auto" | "default\_2024\_08\_21"

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

"default\_2024\_08\_21"

score\_threshold: number

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

results?: Array<Result>

The results of the file search.

file\_id: string

The ID of the file that result was found in.

file\_name: string

The name of the file that result was found in.

score: number

The score of the result. All values must be a floating point number between 0 and 1.

minimum0

maximum1

content?: Array<Content>

The content of the result that was found. The content is only included if requested via the include query parameter.

text?: string

The text content of the file.

type?: "text"

The type of the content.

type: "file\_search"

The type of tool call. This is always going to be `file_search` for this type of tool call.

FunctionToolCall { id, function, type }

id: string

The ID of the tool call object.

function: Function { arguments, name, output }

The definition of the function that was called.

arguments: string

The arguments passed to the function.

name: string

The name of the function.

output: string | null

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

type: "function"

The type of tool call. This is always going to be `function` for this type of tool call.

ToolCallDelta = [CodeInterpreterToolCallDelta](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call_delta%20%3E%20(schema)) { index, type, id, code\_interpreter }  | [FileSearchToolCallDelta](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call_delta%20%3E%20(schema)) { file\_search, index, type, id }  | [FunctionToolCallDelta](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema)) { index, type, id, function }

Details of the Code Interpreter tool call the run step was involved in.

One of the following:

CodeInterpreterToolCallDelta { index, type, id, code\_interpreter }

Details of the Code Interpreter tool call the run step was involved in.

index: number

The index of the tool call in the tool calls array.

type: "code\_interpreter"

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

id?: string

The ID of the tool call.

code\_interpreter?: CodeInterpreter { input, outputs }

The Code Interpreter tool call definition.

input?: string

The input to the Code Interpreter tool call.

outputs?: Array<[CodeInterpreterLogs](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema)) { index, type, logs }  | [CodeInterpreterOutputImage](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)) { index, type, image } >

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

CodeInterpreterLogs { index, type, logs }

Text output from the Code Interpreter tool call as part of a run step.

index: number

The index of the output in the outputs array.

type: "logs"

Always `logs`.

logs?: string

The text output from the Code Interpreter tool call.

CodeInterpreterOutputImage { index, type, image }

index: number

The index of the output in the outputs array.

type: "image"

Always `image`.

image?: Image { file\_id }

file\_id?: string

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

FileSearchToolCallDelta { file\_search, index, type, id }

file\_search: unknown

For now, this is always going to be an empty object.

index: number

The index of the tool call in the tool calls array.

type: "file\_search"

The type of tool call. This is always going to be `file_search` for this type of tool call.

id?: string

The ID of the tool call object.

FunctionToolCallDelta { index, type, id, function }

index: number

The index of the tool call in the tool calls array.

type: "function"

The type of tool call. This is always going to be `function` for this type of tool call.

id?: string

The ID of the tool call object.

function?: Function { arguments, name, output }

The definition of the function that was called.

arguments?: string

The arguments passed to the function.

name?: string

The name of the function.

output?: string | null

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

ToolCallDeltaObject { type, tool\_calls }

Details of the tool call.

type: "tool\_calls"

Always `tool_calls`.

tool\_calls?: Array<[ToolCallDelta](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call_delta%20%3E%20(schema))>

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

One of the following:

CodeInterpreterToolCallDelta { index, type, id, code\_interpreter }

Details of the Code Interpreter tool call the run step was involved in.

index: number

The index of the tool call in the tool calls array.

type: "code\_interpreter"

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

id?: string

The ID of the tool call.

code\_interpreter?: CodeInterpreter { input, outputs }

The Code Interpreter tool call definition.

input?: string

The input to the Code Interpreter tool call.

outputs?: Array<[CodeInterpreterLogs](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema)) { index, type, logs }  | [CodeInterpreterOutputImage](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)) { index, type, image } >

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

CodeInterpreterLogs { index, type, logs }

Text output from the Code Interpreter tool call as part of a run step.

index: number

The index of the output in the outputs array.

type: "logs"

Always `logs`.

logs?: string

The text output from the Code Interpreter tool call.

CodeInterpreterOutputImage { index, type, image }

index: number

The index of the output in the outputs array.

type: "image"

Always `image`.

image?: Image { file\_id }

file\_id?: string

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

FileSearchToolCallDelta { file\_search, index, type, id }

file\_search: unknown

For now, this is always going to be an empty object.

index: number

The index of the tool call in the tool calls array.

type: "file\_search"

The type of tool call. This is always going to be `file_search` for this type of tool call.

id?: string

The ID of the tool call object.

FunctionToolCallDelta { index, type, id, function }

index: number

The index of the tool call in the tool calls array.

type: "function"

The type of tool call. This is always going to be `function` for this type of tool call.

id?: string

The ID of the tool call object.

function?: Function { arguments, name, output }

The definition of the function that was called.

arguments?: string

The arguments passed to the function.

name?: string

The name of the function.

output?: string | null

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

ToolCallsStepDetails { tool\_calls, type }

Details of the tool call.

tool\_calls: Array<[ToolCall](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call%20%3E%20(schema))>

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

One of the following:

CodeInterpreterToolCall { id, code\_interpreter, type }

Details of the Code Interpreter tool call the run step was involved in.

id: string

The ID of the tool call.

code\_interpreter: CodeInterpreter { input, outputs }

The Code Interpreter tool call definition.

input: string

The input to the Code Interpreter tool call.

outputs: Array<Logs { logs, type }  | Image { image, type } >

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

Logs { logs, type }

Text output from the Code Interpreter tool call as part of a run step.

logs: string

The text output from the Code Interpreter tool call.

type: "logs"

Always `logs`.

Image { image, type }

image: Image { file\_id }

file\_id: string

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

type: "image"

Always `image`.

type: "code\_interpreter"

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

FileSearchToolCall { id, file\_search, type }

id: string

The ID of the tool call object.

file\_search: FileSearch { ranking\_options, results }

For now, this is always going to be an empty object.

ranking\_options?: RankingOptions { ranker, score\_threshold }

The ranking options for the file search.

ranker: "auto" | "default\_2024\_08\_21"

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

"default\_2024\_08\_21"

score\_threshold: number

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

results?: Array<Result>

The results of the file search.

file\_id: string

The ID of the file that result was found in.

file\_name: string

The name of the file that result was found in.

score: number

The score of the result. All values must be a floating point number between 0 and 1.

minimum0

maximum1

content?: Array<Content>

The content of the result that was found. The content is only included if requested via the include query parameter.

text?: string

The text content of the file.

type?: "text"

The type of the content.

type: "file\_search"

The type of tool call. This is always going to be `file_search` for this type of tool call.

FunctionToolCall { id, function, type }

id: string

The ID of the tool call object.

function: Function { arguments, name, output }

The definition of the function that was called.

arguments: string

The arguments passed to the function.

name: string

The name of the function.

output: string | null

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

type: "function"

The type of tool call. This is always going to be `function` for this type of tool call.

type: "tool\_calls"

Always `tool_calls`.

#### BetaThreadsMessages

Build Assistants that can call models and use tools.

##### [List messages](/api/reference/typescript/resources/beta/subresources/threads/subresources/messages/methods/list)

Deprecated

client.beta.threads.messages.list(stringthreadID, MessageListParams { after, before, limit, 2 more } query?, RequestOptionsoptions?): CursorPage<[Message](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)) { id, assistant\_id, attachments, 11 more } >

GET/threads/{thread\_id}/messages

##### [Create message](/api/reference/typescript/resources/beta/subresources/threads/subresources/messages/methods/create)

Deprecated

client.beta.threads.messages.create(stringthreadID, MessageCreateParams { content, role, attachments, metadata } body, RequestOptionsoptions?): [Message](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)) { id, assistant\_id, attachments, 11 more }

POST/threads/{thread\_id}/messages

##### [Modify message](/api/reference/typescript/resources/beta/subresources/threads/subresources/messages/methods/update)

Deprecated

client.beta.threads.messages.update(stringmessageID, MessageUpdateParams { thread\_id, metadata } params, RequestOptionsoptions?): [Message](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)) { id, assistant\_id, attachments, 11 more }

POST/threads/{thread\_id}/messages/{message\_id}

##### [Retrieve message](/api/reference/typescript/resources/beta/subresources/threads/subresources/messages/methods/retrieve)

Deprecated

client.beta.threads.messages.retrieve(stringmessageID, MessageRetrieveParams { thread\_id } params, RequestOptionsoptions?): [Message](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)) { id, assistant\_id, attachments, 11 more }

GET/threads/{thread\_id}/messages/{message\_id}

##### [Delete message](/api/reference/typescript/resources/beta/subresources/threads/subresources/messages/methods/delete)

Deprecated

client.beta.threads.messages.delete(stringmessageID, MessageDeleteParams { thread\_id } params, RequestOptionsoptions?): [MessageDeleted](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_deleted%20%3E%20(schema)) { id, deleted, object }

DELETE/threads/{thread\_id}/messages/{message\_id}

##### ModelsExpand Collapse

Annotation = [FileCitationAnnotation](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_annotation%20%3E%20(schema)) { end\_index, file\_citation, start\_index, 2 more }  | [FilePathAnnotation](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20file_path_annotation%20%3E%20(schema)) { end\_index, file\_path, start\_index, 2 more }

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

One of the following:

FileCitationAnnotation { end\_index, file\_citation, start\_index, 2 more }

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

end\_index: number

minimum0

file\_citation: FileCitation { file\_id }

file\_id: string

The ID of the specific File the citation is from.

start\_index: number

minimum0

text: string

The text in the message content that needs to be replaced.

type: "file\_citation"

Always `file_citation`.

FilePathAnnotation { end\_index, file\_path, start\_index, 2 more }

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

end\_index: number

minimum0

file\_path: FilePath { file\_id }

file\_id: string

The ID of the file that was generated.

start\_index: number

minimum0

text: string

The text in the message content that needs to be replaced.

type: "file\_path"

Always `file_path`.

AnnotationDelta = [FileCitationDeltaAnnotation](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_delta_annotation%20%3E%20(schema)) { index, type, end\_index, 3 more }  | [FilePathDeltaAnnotation](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20file_path_delta_annotation%20%3E%20(schema)) { index, type, end\_index, 3 more }

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

One of the following:

FileCitationDeltaAnnotation { index, type, end\_index, 3 more }

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

index: number

The index of the annotation in the text content part.

type: "file\_citation"

Always `file_citation`.

end\_index?: number

minimum0

file\_citation?: FileCitation { file\_id, quote }

file\_id?: string

The ID of the specific File the citation is from.

quote?: string

The specific quote in the file.

start\_index?: number

minimum0

text?: string

The text in the message content that needs to be replaced.

FilePathDeltaAnnotation { index, type, end\_index, 3 more }

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

index: number

The index of the annotation in the text content part.

type: "file\_path"

Always `file_path`.

end\_index?: number

minimum0

file\_path?: FilePath { file\_id }

file\_id?: string

The ID of the file that was generated.

start\_index?: number

minimum0

text?: string

The text in the message content that needs to be replaced.

FileCitationAnnotation { end\_index, file\_citation, start\_index, 2 more }

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

end\_index: number

minimum0

file\_citation: FileCitation { file\_id }

file\_id: string

The ID of the specific File the citation is from.

start\_index: number

minimum0

text: string

The text in the message content that needs to be replaced.

type: "file\_citation"

Always `file_citation`.

FileCitationDeltaAnnotation { index, type, end\_index, 3 more }

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

index: number

The index of the annotation in the text content part.

type: "file\_citation"

Always `file_citation`.

end\_index?: number

minimum0

file\_citation?: FileCitation { file\_id, quote }

file\_id?: string

The ID of the specific File the citation is from.

quote?: string

The specific quote in the file.

start\_index?: number

minimum0

text?: string

The text in the message content that needs to be replaced.

FilePathAnnotation { end\_index, file\_path, start\_index, 2 more }

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

end\_index: number

minimum0

file\_path: FilePath { file\_id }

file\_id: string

The ID of the file that was generated.

start\_index: number

minimum0

text: string

The text in the message content that needs to be replaced.

type: "file\_path"

Always `file_path`.

FilePathDeltaAnnotation { index, type, end\_index, 3 more }

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

index: number

The index of the annotation in the text content part.

type: "file\_path"

Always `file_path`.

end\_index?: number

minimum0

file\_path?: FilePath { file\_id }

file\_id?: string

The ID of the file that was generated.

start\_index?: number

minimum0

text?: string

The text in the message content that needs to be replaced.

ImageFile { file\_id, detail }

file\_id: string

The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

detail?: "auto" | "low" | "high"

Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

One of the following:

"auto"

"low"

"high"

ImageFileContentBlock { image\_file, type }

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

image\_file: [ImageFile](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file%20%3E%20(schema)) { file\_id, detail }

type: "image\_file"

Always `image_file`.

ImageFileDelta { detail, file\_id }

detail?: "auto" | "low" | "high"

Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

One of the following:

"auto"

"low"

"high"

file\_id?: string

The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

ImageFileDeltaBlock { index, type, image\_file }

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

index: number

The index of the content part in the message.

type: "image\_file"

Always `image_file`.

image\_file?: [ImageFileDelta](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_delta%20%3E%20(schema)) { detail, file\_id }

ImageURL { url, detail }

url: string

The external URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

formaturi

detail?: "auto" | "low" | "high"

Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`. Default value is `auto`

One of the following:

"auto"

"low"

"high"

ImageURLContentBlock { image\_url, type }

References an image URL in the content of a message.

image\_url: [ImageURL](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url%20%3E%20(schema)) { url, detail }

type: "image\_url"

The type of the content part.

ImageURLDelta { detail, url }

detail?: "auto" | "low" | "high"

Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`.

One of the following:

"auto"

"low"

"high"

url?: string

The URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

formaturi

ImageURLDeltaBlock { index, type, image\_url }

References an image URL in the content of a message.

index: number

The index of the content part in the message.

type: "image\_url"

Always `image_url`.

image\_url?: [ImageURLDelta](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_delta%20%3E%20(schema)) { detail, url }

Message { id, assistant\_id, attachments, 11 more }

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

id: string

The identifier, which can be referenced in API endpoints.

assistant\_id: string | null

If applicable, the ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) that authored this message.

attachments: Array<Attachment> | null

A list of files attached to the message, and the tools they were added to.

file\_id?: string

The ID of the file to attach to the message.

tools?: Array<[CodeInterpreterTool](/api/reference/typescript/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20code_interpreter_tool%20%3E%20(schema)) { type }  | AssistantToolsFileSearchTypeOnly { type } >

The tools to add this file to.

One of the following:

CodeInterpreterTool { type }

type: "code\_interpreter"

The type of tool being defined: `code_interpreter`

AssistantToolsFileSearchTypeOnly { type }

type: "file\_search"

The type of tool being defined: `file_search`

completed\_at: number | null

The Unix timestamp (in seconds) for when the message was completed.

formatunixtime

content: Array<[MessageContent](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_content%20%3E%20(schema))>

The content of the message in array of text and/or images.

One of the following:

ImageFileContentBlock { image\_file, type }

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

image\_file: [ImageFile](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file%20%3E%20(schema)) { file\_id, detail }

type: "image\_file"

Always `image_file`.

ImageURLContentBlock { image\_url, type }

References an image URL in the content of a message.

image\_url: [ImageURL](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url%20%3E%20(schema)) { url, detail }

type: "image\_url"

The type of the content part.

TextContentBlock { text, type }

The text content that is part of a message.

text: [Text](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text%20%3E%20(schema)) { annotations, value }

type: "text"

Always `text`.

RefusalContentBlock { refusal, type }

The refusal content generated by the assistant.

refusal: string

type: "refusal"

Always `refusal`.

created\_at: number

The Unix timestamp (in seconds) for when the message was created.

formatunixtime

incomplete\_at: number | null

The Unix timestamp (in seconds) for when the message was marked as incomplete.

formatunixtime

incomplete\_details: IncompleteDetails | null

On an incomplete message, details about why the message is incomplete.

reason: "content\_filter" | "max\_tokens" | "run\_cancelled" | 2 more

The reason the message is incomplete.

One of the following:

"content\_filter"

"max\_tokens"

"run\_cancelled"

"run\_expired"

"run\_failed"

metadata: [Metadata](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema)) | null

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

object: "thread.message"

The object type, which is always `thread.message`.

role: "user" | "assistant"

The entity that produced the message. One of `user` or `assistant`.

One of the following:

"user"

"assistant"

run\_id: string | null

The ID of the [run](https://platform.openai.com/docs/api-reference/runs) associated with the creation of this message. Value is `null` when messages are created manually using the create message or create thread endpoints.

status: "in\_progress" | "incomplete" | "completed"

The status of the message, which can be either `in_progress`, `incomplete`, or `completed`.

One of the following:

"in\_progress"

"incomplete"

"completed"

thread\_id: string

The [thread](https://platform.openai.com/docs/api-reference/threads) ID that this message belongs to.

MessageContent = [ImageFileContentBlock](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_content_block%20%3E%20(schema)) { image\_file, type }  | [ImageURLContentBlock](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_content_block%20%3E%20(schema)) { image\_url, type }  | [TextContentBlock](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text_content_block%20%3E%20(schema)) { text, type }  | [RefusalContentBlock](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20refusal_content_block%20%3E%20(schema)) { refusal, type }

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

One of the following:

ImageFileContentBlock { image\_file, type }

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

image\_file: [ImageFile](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file%20%3E%20(schema)) { file\_id, detail }

type: "image\_file"

Always `image_file`.

ImageURLContentBlock { image\_url, type }

References an image URL in the content of a message.

image\_url: [ImageURL](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url%20%3E%20(schema)) { url, detail }

type: "image\_url"

The type of the content part.

TextContentBlock { text, type }

The text content that is part of a message.

text: [Text](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text%20%3E%20(schema)) { annotations, value }

type: "text"

Always `text`.

RefusalContentBlock { refusal, type }

The refusal content generated by the assistant.

refusal: string

type: "refusal"

Always `refusal`.

MessageContentDelta = [ImageFileDeltaBlock](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_delta_block%20%3E%20(schema)) { index, type, image\_file }  | [TextDeltaBlock](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text_delta_block%20%3E%20(schema)) { index, type, text }  | [RefusalDeltaBlock](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20refusal_delta_block%20%3E%20(schema)) { index, type, refusal }  | [ImageURLDeltaBlock](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_delta_block%20%3E%20(schema)) { index, type, image\_url }

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

One of the following:

ImageFileDeltaBlock { index, type, image\_file }

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

index: number

The index of the content part in the message.

type: "image\_file"

Always `image_file`.

image\_file?: [ImageFileDelta](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_delta%20%3E%20(schema)) { detail, file\_id }

TextDeltaBlock { index, type, text }

The text content that is part of a message.

index: number

The index of the content part in the message.

type: "text"

Always `text`.

text?: [TextDelta](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text_delta%20%3E%20(schema)) { annotations, value }

RefusalDeltaBlock { index, type, refusal }

The refusal content that is part of a message.

index: number

The index of the refusal part in the message.

type: "refusal"

Always `refusal`.

refusal?: string

ImageURLDeltaBlock { index, type, image\_url }

References an image URL in the content of a message.

index: number

The index of the content part in the message.

type: "image\_url"

Always `image_url`.

image\_url?: [ImageURLDelta](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_delta%20%3E%20(schema)) { detail, url }

MessageContentPartParam = [ImageFileContentBlock](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_content_block%20%3E%20(schema)) { image\_file, type }  | [ImageURLContentBlock](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_content_block%20%3E%20(schema)) { image\_url, type }  | [TextContentBlockParam](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text_content_block_param%20%3E%20(schema)) { text, type }

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

One of the following:

ImageFileContentBlock { image\_file, type }

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

image\_file: [ImageFile](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file%20%3E%20(schema)) { file\_id, detail }

type: "image\_file"

Always `image_file`.

ImageURLContentBlock { image\_url, type }

References an image URL in the content of a message.

image\_url: [ImageURL](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url%20%3E%20(schema)) { url, detail }

type: "image\_url"

The type of the content part.

TextContentBlockParam { text, type }

The text content that is part of a message.

text: string

Text content to be sent to the model

type: "text"

Always `text`.

MessageDeleted { id, deleted, object }

id: string

deleted: boolean

object: "thread.message.deleted"

MessageDelta { content, role }

The delta containing the fields that have changed on the Message.

content?: Array<[MessageContentDelta](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_content_delta%20%3E%20(schema))>

The content of the message in array of text and/or images.

One of the following:

ImageFileDeltaBlock { index, type, image\_file }

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

index: number

The index of the content part in the message.

type: "image\_file"

Always `image_file`.

image\_file?: [ImageFileDelta](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_delta%20%3E%20(schema)) { detail, file\_id }

TextDeltaBlock { index, type, text }

The text content that is part of a message.

index: number

The index of the content part in the message.

type: "text"

Always `text`.

text?: [TextDelta](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text_delta%20%3E%20(schema)) { annotations, value }

RefusalDeltaBlock { index, type, refusal }

The refusal content that is part of a message.

index: number

The index of the refusal part in the message.

type: "refusal"

Always `refusal`.

refusal?: string

ImageURLDeltaBlock { index, type, image\_url }

References an image URL in the content of a message.

index: number

The index of the content part in the message.

type: "image\_url"

Always `image_url`.

image\_url?: [ImageURLDelta](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_delta%20%3E%20(schema)) { detail, url }

role?: "user" | "assistant"

The entity that produced the message. One of `user` or `assistant`.

One of the following:

"user"

"assistant"

MessageDeltaEvent { id, delta, object }

Represents a message delta i.e. any changed fields on a message during streaming.

id: string

The identifier of the message, which can be referenced in API endpoints.

delta: [MessageDelta](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_delta%20%3E%20(schema)) { content, role }

The delta containing the fields that have changed on the Message.

object: "thread.message.delta"

The object type, which is always `thread.message.delta`.

RefusalContentBlock { refusal, type }

The refusal content generated by the assistant.

refusal: string

type: "refusal"

Always `refusal`.

RefusalDeltaBlock { index, type, refusal }

The refusal content that is part of a message.

index: number

The index of the refusal part in the message.

type: "refusal"

Always `refusal`.

refusal?: string

Text { annotations, value }

annotations: Array<[Annotation](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20annotation%20%3E%20(schema))>

One of the following:

FileCitationAnnotation { end\_index, file\_citation, start\_index, 2 more }

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

end\_index: number

minimum0

file\_citation: FileCitation { file\_id }

file\_id: string

The ID of the specific File the citation is from.

start\_index: number

minimum0

text: string

The text in the message content that needs to be replaced.

type: "file\_citation"

Always `file_citation`.

FilePathAnnotation { end\_index, file\_path, start\_index, 2 more }

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

end\_index: number

minimum0

file\_path: FilePath { file\_id }

file\_id: string

The ID of the file that was generated.

start\_index: number

minimum0

text: string

The text in the message content that needs to be replaced.

type: "file\_path"

Always `file_path`.

value: string

The data that makes up the text.

TextContentBlock { text, type }

The text content that is part of a message.

text: [Text](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text%20%3E%20(schema)) { annotations, value }

type: "text"

Always `text`.

TextContentBlockParam { text, type }

The text content that is part of a message.

text: string

Text content to be sent to the model

type: "text"

Always `text`.

TextDelta { annotations, value }

annotations?: Array<[AnnotationDelta](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20annotation_delta%20%3E%20(schema))>

One of the following:

FileCitationDeltaAnnotation { index, type, end\_index, 3 more }

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

index: number

The index of the annotation in the text content part.

type: "file\_citation"

Always `file_citation`.

end\_index?: number

minimum0

file\_citation?: FileCitation { file\_id, quote }

file\_id?: string

The ID of the specific File the citation is from.

quote?: string

The specific quote in the file.

start\_index?: number

minimum0

text?: string

The text in the message content that needs to be replaced.

FilePathDeltaAnnotation { index, type, end\_index, 3 more }

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

index: number

The index of the annotation in the text content part.

type: "file\_path"

Always `file_path`.

end\_index?: number

minimum0

file\_path?: FilePath { file\_id }

file\_id?: string

The ID of the file that was generated.

start\_index?: number

minimum0

text?: string

The text in the message content that needs to be replaced.

value?: string

The data that makes up the text.

TextDeltaBlock { index, type, text }

The text content that is part of a message.

index: number

The index of the content part in the message.

type: "text"

Always `text`.

text?: [TextDelta](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text_delta%20%3E%20(schema)) { annotations, value }
