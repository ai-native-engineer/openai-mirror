<!-- source: https://developers.openai.com/api/reference/python/resources/beta/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

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

#### BetaChatKitSessions

##### [Cancel chat session](/api/reference/python/resources/beta/subresources/chatkit/subresources/sessions/methods/cancel)

beta.chatkit.sessions.cancel(strsession\_id)  -> [ChatSession](/api/reference/python/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session%20%3E%20(schema))

POST/chatkit/sessions/{session\_id}/cancel

##### [Create ChatKit session](/api/reference/python/resources/beta/subresources/chatkit/subresources/sessions/methods/create)

beta.chatkit.sessions.create(SessionCreateParams\*\*kwargs)  -> [ChatSession](/api/reference/python/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session%20%3E%20(schema))

POST/chatkit/sessions

#### BetaChatKitThreads

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

#### BetaAssistants

Build Assistants that can call models and use tools.

##### [List assistants](/api/reference/python/resources/beta/subresources/assistants/methods/list)

Deprecated

beta.assistants.list(AssistantListParams\*\*kwargs)  -> SyncCursorPage[[Assistant](/api/reference/python/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema))]

GET/assistants

##### [Create assistant](/api/reference/python/resources/beta/subresources/assistants/methods/create)

Deprecated

beta.assistants.create(AssistantCreateParams\*\*kwargs)  -> [Assistant](/api/reference/python/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema))

POST/assistants

##### [Retrieve assistant](/api/reference/python/resources/beta/subresources/assistants/methods/retrieve)

Deprecated

beta.assistants.retrieve(strassistant\_id)  -> [Assistant](/api/reference/python/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema))

GET/assistants/{assistant\_id}

##### [Modify assistant](/api/reference/python/resources/beta/subresources/assistants/methods/update)

Deprecated

beta.assistants.update(strassistant\_id, AssistantUpdateParams\*\*kwargs)  -> [Assistant](/api/reference/python/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema))

POST/assistants/{assistant\_id}

##### [Delete assistant](/api/reference/python/resources/beta/subresources/assistants/methods/delete)

Deprecated

beta.assistants.delete(strassistant\_id)  -> [AssistantDeleted](/api/reference/python/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant_deleted%20%3E%20(schema))

DELETE/assistants/{assistant\_id}

##### ModelsExpand Collapse

class Assistant: …

Represents an `assistant` that can call the model and use tools.

id: str

The identifier, which can be referenced in API endpoints.

created\_at: int

The Unix timestamp (in seconds) for when the assistant was created.

formatunixtime

description: Optional[str]

The description of the assistant. The maximum length is 512 characters.

maxLength512

instructions: Optional[str]

The system instructions that the assistant uses. The maximum length is 256,000 characters.

maxLength256000

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: str

ID of the model to use. You can use the [List models](https://platform.openai.com/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](https://platform.openai.com/docs/models) for descriptions of them.

name: Optional[str]

The name of the assistant. The maximum length is 256 characters.

maxLength256

object: Literal["assistant"]

The object type, which is always `assistant`.

tools: List[[AssistantTool](/api/reference/python/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant_tool%20%3E%20(schema))]

A list of tool enabled on the assistant. There can be a maximum of 128 tools per assistant. Tools can be of types `code_interpreter`, `file_search`, or `function`.

One of the following:

class CodeInterpreterTool: …

type: Literal["code\_interpreter"]

The type of tool being defined: `code_interpreter`

class FileSearchTool: …

type: Literal["file\_search"]

The type of tool being defined: `file_search`

file\_search: Optional[FileSearch]

Overrides for the file search tool.

max\_num\_results: Optional[int]

The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

minimum1

maximum50

ranking\_options: Optional[FileSearchRankingOptions]

The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score\_threshold of 0.

See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

score\_threshold: float

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

ranker: Optional[Literal["auto", "default\_2024\_08\_21"]]

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

"default\_2024\_08\_21"

class FunctionTool: …

function: [FunctionDefinition](/api/reference/python/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema))

type: Literal["function"]

The type of tool being defined: `function`

response\_format: Optional[AssistantResponseFormatOption]

Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly “stuck” request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

temperature: Optional[float]

What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

minimum0

maximum2

tool\_resources: Optional[ToolResources]

A set of resources that are used by the assistant’s tools. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

code\_interpreter: Optional[ToolResourcesCodeInterpreter]

file\_ids: Optional[List[str]]

A list of [file](https://platform.openai.com/docs/api-reference/files) IDs made available to the `code\_interpreter“ tool. There can be a maximum of 20 files associated with the tool.

file\_search: Optional[ToolResourcesFileSearch]

vector\_store\_ids: Optional[List[str]]

The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) attached to this assistant. There can be a maximum of 1 vector store attached to the assistant.

top\_p: Optional[float]

An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top\_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.

We generally recommend altering this or temperature but not both.

minimum0

maximum1

class AssistantDeleted: …

id: str

deleted: bool

object: Literal["assistant.deleted"]

[AssistantStreamEvent](/api/reference/python/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema))

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

class ThreadCreated: …

Occurs when a new [thread](https://platform.openai.com/docs/api-reference/threads/object) is created.

data: [Thread](/api/reference/python/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20thread%20%3E%20(schema))

Represents a thread that contains [messages](https://platform.openai.com/docs/api-reference/messages).

event: Literal["thread.created"]

enabled: Optional[bool]

Whether to enable input audio transcription.

class ThreadRunCreated: …

Occurs when a new [run](https://platform.openai.com/docs/api-reference/runs/object) is created.

data: [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.run.created"]

class ThreadRunQueued: …

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) moves to a `queued` status.

data: [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.run.queued"]

class ThreadRunInProgress: …

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) moves to an `in_progress` status.

data: [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.run.in\_progress"]

class ThreadRunRequiresAction: …

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) moves to a `requires_action` status.

data: [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.run.requires\_action"]

class ThreadRunCompleted: …

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) is completed.

data: [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.run.completed"]

class ThreadRunIncomplete: …

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) ends with status `incomplete`.

data: [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.run.incomplete"]

class ThreadRunFailed: …

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) fails.

data: [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.run.failed"]

class ThreadRunCancelling: …

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) moves to a `cancelling` status.

data: [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.run.cancelling"]

class ThreadRunCancelled: …

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) is cancelled.

data: [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.run.cancelled"]

class ThreadRunExpired: …

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) expires.

data: [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.run.expired"]

class ThreadRunStepCreated: …

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) is created.

data: [RunStep](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

event: Literal["thread.run.step.created"]

class ThreadRunStepInProgress: …

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) moves to an `in_progress` state.

data: [RunStep](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

event: Literal["thread.run.step.in\_progress"]

class ThreadRunStepDelta: …

Occurs when parts of a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) are being streamed.

data: [RunStepDeltaEvent](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta_event%20%3E%20(schema))

Represents a run step delta i.e. any changed fields on a run step during streaming.

event: Literal["thread.run.step.delta"]

class ThreadRunStepCompleted: …

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) is completed.

data: [RunStep](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

event: Literal["thread.run.step.completed"]

class ThreadRunStepFailed: …

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) fails.

data: [RunStep](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

event: Literal["thread.run.step.failed"]

class ThreadRunStepCancelled: …

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) is cancelled.

data: [RunStep](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

event: Literal["thread.run.step.cancelled"]

class ThreadRunStepExpired: …

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) expires.

data: [RunStep](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

event: Literal["thread.run.step.expired"]

class ThreadMessageCreated: …

Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) is created.

data: [Message](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema))

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.message.created"]

class ThreadMessageInProgress: …

Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) moves to an `in_progress` state.

data: [Message](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema))

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.message.in\_progress"]

class ThreadMessageDelta: …

Occurs when parts of a [Message](https://platform.openai.com/docs/api-reference/messages/object) are being streamed.

data: [MessageDeltaEvent](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_delta_event%20%3E%20(schema))

Represents a message delta i.e. any changed fields on a message during streaming.

event: Literal["thread.message.delta"]

class ThreadMessageCompleted: …

Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) is completed.

data: [Message](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema))

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.message.completed"]

class ThreadMessageIncomplete: …

Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) ends before it is completed.

data: [Message](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema))

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.message.incomplete"]

class ErrorEvent: …

Occurs when an [error](https://platform.openai.com/docs/guides/error-codes#api-errors) occurs. This can happen due to an internal server error or a timeout.

data: [ErrorObject](/api/reference/python/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20error_object%20%3E%20(schema))

event: Literal["error"]

[AssistantTool](/api/reference/python/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant_tool%20%3E%20(schema))

One of the following:

class CodeInterpreterTool: …

type: Literal["code\_interpreter"]

The type of tool being defined: `code_interpreter`

class FileSearchTool: …

type: Literal["file\_search"]

The type of tool being defined: `file_search`

file\_search: Optional[FileSearch]

Overrides for the file search tool.

max\_num\_results: Optional[int]

The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

minimum1

maximum50

ranking\_options: Optional[FileSearchRankingOptions]

The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score\_threshold of 0.

See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

score\_threshold: float

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

ranker: Optional[Literal["auto", "default\_2024\_08\_21"]]

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

"default\_2024\_08\_21"

class FunctionTool: …

function: [FunctionDefinition](/api/reference/python/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema))

type: Literal["function"]

The type of tool being defined: `function`

class CodeInterpreterTool: …

type: Literal["code\_interpreter"]

The type of tool being defined: `code_interpreter`

class FileSearchTool: …

type: Literal["file\_search"]

The type of tool being defined: `file_search`

file\_search: Optional[FileSearch]

Overrides for the file search tool.

max\_num\_results: Optional[int]

The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

minimum1

maximum50

ranking\_options: Optional[FileSearchRankingOptions]

The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score\_threshold of 0.

See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

score\_threshold: float

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

ranker: Optional[Literal["auto", "default\_2024\_08\_21"]]

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

"default\_2024\_08\_21"

class FunctionTool: …

function: [FunctionDefinition](/api/reference/python/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema))

type: Literal["function"]

The type of tool being defined: `function`

[MessageStreamEvent](/api/reference/python/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20message_stream_event%20%3E%20(schema))

Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) is created.

One of the following:

class ThreadMessageCreated: …

Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) is created.

data: [Message](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema))

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.message.created"]

class ThreadMessageInProgress: …

Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) moves to an `in_progress` state.

data: [Message](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema))

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.message.in\_progress"]

class ThreadMessageDelta: …

Occurs when parts of a [Message](https://platform.openai.com/docs/api-reference/messages/object) are being streamed.

data: [MessageDeltaEvent](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_delta_event%20%3E%20(schema))

Represents a message delta i.e. any changed fields on a message during streaming.

event: Literal["thread.message.delta"]

class ThreadMessageCompleted: …

Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) is completed.

data: [Message](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema))

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.message.completed"]

class ThreadMessageIncomplete: …

Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) ends before it is completed.

data: [Message](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema))

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.message.incomplete"]

[RunStepStreamEvent](/api/reference/python/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20run_step_stream_event%20%3E%20(schema))

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) is created.

One of the following:

class ThreadRunStepCreated: …

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) is created.

data: [RunStep](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

event: Literal["thread.run.step.created"]

class ThreadRunStepInProgress: …

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) moves to an `in_progress` state.

data: [RunStep](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

event: Literal["thread.run.step.in\_progress"]

class ThreadRunStepDelta: …

Occurs when parts of a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) are being streamed.

data: [RunStepDeltaEvent](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta_event%20%3E%20(schema))

Represents a run step delta i.e. any changed fields on a run step during streaming.

event: Literal["thread.run.step.delta"]

class ThreadRunStepCompleted: …

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) is completed.

data: [RunStep](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

event: Literal["thread.run.step.completed"]

class ThreadRunStepFailed: …

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) fails.

data: [RunStep](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

event: Literal["thread.run.step.failed"]

class ThreadRunStepCancelled: …

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) is cancelled.

data: [RunStep](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

event: Literal["thread.run.step.cancelled"]

class ThreadRunStepExpired: …

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) expires.

data: [RunStep](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

event: Literal["thread.run.step.expired"]

[RunStreamEvent](/api/reference/python/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20run_stream_event%20%3E%20(schema))

Occurs when a new [run](https://platform.openai.com/docs/api-reference/runs/object) is created.

One of the following:

class ThreadRunCreated: …

Occurs when a new [run](https://platform.openai.com/docs/api-reference/runs/object) is created.

data: [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.run.created"]

class ThreadRunQueued: …

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) moves to a `queued` status.

data: [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.run.queued"]

class ThreadRunInProgress: …

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) moves to an `in_progress` status.

data: [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.run.in\_progress"]

class ThreadRunRequiresAction: …

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) moves to a `requires_action` status.

data: [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.run.requires\_action"]

class ThreadRunCompleted: …

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) is completed.

data: [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.run.completed"]

class ThreadRunIncomplete: …

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) ends with status `incomplete`.

data: [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.run.incomplete"]

class ThreadRunFailed: …

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) fails.

data: [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.run.failed"]

class ThreadRunCancelling: …

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) moves to a `cancelling` status.

data: [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.run.cancelling"]

class ThreadRunCancelled: …

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) is cancelled.

data: [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.run.cancelled"]

class ThreadRunExpired: …

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) expires.

data: [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.run.expired"]

class ThreadStreamEvent: …

Occurs when a new [thread](https://platform.openai.com/docs/api-reference/threads/object) is created.

data: [Thread](/api/reference/python/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20thread%20%3E%20(schema))

Represents a thread that contains [messages](https://platform.openai.com/docs/api-reference/messages).

event: Literal["thread.created"]

enabled: Optional[bool]

Whether to enable input audio transcription.

#### BetaThreads

Build Assistants that can call models and use tools.

##### [Create thread](/api/reference/python/resources/beta/subresources/threads/methods/create)

Deprecated

beta.threads.create(ThreadCreateParams\*\*kwargs)  -> [Thread](/api/reference/python/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20thread%20%3E%20(schema))

POST/threads

##### [Create thread and run](/api/reference/python/resources/beta/subresources/threads/methods/create_and_run)

Deprecated

beta.threads.create\_and\_run(ThreadCreateAndRunParams\*\*kwargs)  -> [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

POST/threads/runs

##### [Retrieve thread](/api/reference/python/resources/beta/subresources/threads/methods/retrieve)

Deprecated

beta.threads.retrieve(strthread\_id)  -> [Thread](/api/reference/python/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20thread%20%3E%20(schema))

GET/threads/{thread\_id}

##### [Modify thread](/api/reference/python/resources/beta/subresources/threads/methods/update)

Deprecated

beta.threads.update(strthread\_id, ThreadUpdateParams\*\*kwargs)  -> [Thread](/api/reference/python/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20thread%20%3E%20(schema))

POST/threads/{thread\_id}

##### [Delete thread](/api/reference/python/resources/beta/subresources/threads/methods/delete)

Deprecated

beta.threads.delete(strthread\_id)  -> [ThreadDeleted](/api/reference/python/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20thread_deleted%20%3E%20(schema))

DELETE/threads/{thread\_id}

##### ModelsExpand Collapse

[AssistantResponseFormatOption](/api/reference/python/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20assistant_response_format_option%20%3E%20(schema))

Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly “stuck” request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

One of the following:

Literal["auto"]

`auto` is the default value

class ResponseFormatText: …

Default response format. Used to generate text responses.

type: Literal["text"]

The type of response format being defined. Always `text`.

class ResponseFormatJSONObject: …

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type: Literal["json\_object"]

The type of response format being defined. Always `json_object`.

class ResponseFormatJSONSchema: …

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

json\_schema: JSONSchema

Structured Outputs configuration options, including a JSON Schema.

name: str

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

description: Optional[str]

A description of what the response format is for, used by the model to
determine how to respond in the format.

schema: Optional[Dict[str, object]]

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

strict: Optional[bool]

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

type: Literal["json\_schema"]

The type of response format being defined. Always `json_schema`.

class AssistantToolChoice: …

Specifies a tool the model should use. Use to force the model to call a specific tool.

type: Literal["function", "code\_interpreter", "file\_search"]

The type of the tool. If type is `function`, the function name must be set

One of the following:

"function"

"code\_interpreter"

"file\_search"

function: Optional[AssistantToolChoiceFunction]

class AssistantToolChoiceFunction: …

name: str

The name of the function to call.

[AssistantToolChoiceOption](/api/reference/python/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_option%20%3E%20(schema))

Controls which (if any) tool is called by the model.
`none` means the model will not call any tools and instead generates a message.
`auto` is the default value and means the model can pick between generating a message or calling one or more tools.
`required` means the model must call one or more tools before responding to the user.
Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

One of the following:

Literal["none", "auto", "required"]

`none` means the model will not call any tools and instead generates a message. `auto` means the model can pick between generating a message or calling one or more tools. `required` means the model must call one or more tools before responding to the user.

One of the following:

"none"

"auto"

"required"

class AssistantToolChoice: …

Specifies a tool the model should use. Use to force the model to call a specific tool.

type: Literal["function", "code\_interpreter", "file\_search"]

The type of the tool. If type is `function`, the function name must be set

One of the following:

"function"

"code\_interpreter"

"file\_search"

function: Optional[AssistantToolChoiceFunction]

class Thread: …

Represents a thread that contains [messages](https://platform.openai.com/docs/api-reference/messages).

id: str

The identifier, which can be referenced in API endpoints.

created\_at: int

The Unix timestamp (in seconds) for when the thread was created.

formatunixtime

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

object: Literal["thread"]

The object type, which is always `thread`.

tool\_resources: Optional[ToolResources]

A set of resources that are made available to the assistant’s tools in this thread. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

code\_interpreter: Optional[ToolResourcesCodeInterpreter]

file\_ids: Optional[List[str]]

A list of [file](https://platform.openai.com/docs/api-reference/files) IDs made available to the `code_interpreter` tool. There can be a maximum of 20 files associated with the tool.

file\_search: Optional[ToolResourcesFileSearch]

vector\_store\_ids: Optional[List[str]]

The [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) attached to this thread. There can be a maximum of 1 vector store attached to the thread.

class ThreadDeleted: …

id: str

deleted: bool

object: Literal["thread.deleted"]

#### BetaThreadsRuns

Build Assistants that can call models and use tools.

##### [List runs](/api/reference/python/resources/beta/subresources/threads/subresources/runs/methods/list)

Deprecated

beta.threads.runs.list(strthread\_id, RunListParams\*\*kwargs)  -> SyncCursorPage[[Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))]

GET/threads/{thread\_id}/runs

##### [Create run](/api/reference/python/resources/beta/subresources/threads/subresources/runs/methods/create)

Deprecated

beta.threads.runs.create(strthread\_id, RunCreateParams\*\*kwargs)  -> [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

POST/threads/{thread\_id}/runs

##### [Retrieve run](/api/reference/python/resources/beta/subresources/threads/subresources/runs/methods/retrieve)

Deprecated

beta.threads.runs.retrieve(strrun\_id, RunRetrieveParams\*\*kwargs)  -> [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

GET/threads/{thread\_id}/runs/{run\_id}

##### [Modify run](/api/reference/python/resources/beta/subresources/threads/subresources/runs/methods/update)

Deprecated

beta.threads.runs.update(strrun\_id, RunUpdateParams\*\*kwargs)  -> [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

POST/threads/{thread\_id}/runs/{run\_id}

##### [Submit tool outputs to run](/api/reference/python/resources/beta/subresources/threads/subresources/runs/methods/submit_tool_outputs)

Deprecated

beta.threads.runs.submit\_tool\_outputs(strrun\_id, RunSubmitToolOutputsParams\*\*kwargs)  -> [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

POST/threads/{thread\_id}/runs/{run\_id}/submit\_tool\_outputs

##### [Cancel a run](/api/reference/python/resources/beta/subresources/threads/subresources/runs/methods/cancel)

Deprecated

beta.threads.runs.cancel(strrun\_id, RunCancelParams\*\*kwargs)  -> [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

POST/threads/{thread\_id}/runs/{run\_id}/cancel

##### ModelsExpand Collapse

class RequiredActionFunctionToolCall: …

Tool call objects

id: str

The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

function: Function

The function definition.

arguments: str

The arguments that the model expects you to pass to the function.

name: str

The name of the function.

type: Literal["function"]

The type of tool call the output is required for. For now, this is always `function`.

class Run: …

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

id: str

The identifier, which can be referenced in API endpoints.

assistant\_id: str

The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for execution of this run.

cancelled\_at: Optional[int]

The Unix timestamp (in seconds) for when the run was cancelled.

formatunixtime

completed\_at: Optional[int]

The Unix timestamp (in seconds) for when the run was completed.

formatunixtime

created\_at: int

The Unix timestamp (in seconds) for when the run was created.

formatunixtime

expires\_at: Optional[int]

The Unix timestamp (in seconds) for when the run will expire.

formatunixtime

failed\_at: Optional[int]

The Unix timestamp (in seconds) for when the run failed.

formatunixtime

incomplete\_details: Optional[IncompleteDetails]

Details on why the run is incomplete. Will be `null` if the run is not incomplete.

reason: Optional[Literal["max\_completion\_tokens", "max\_prompt\_tokens"]]

The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

One of the following:

"max\_completion\_tokens"

"max\_prompt\_tokens"

instructions: str

The instructions that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

last\_error: Optional[LastError]

The last error associated with this run. Will be `null` if there are no errors.

code: Literal["server\_error", "rate\_limit\_exceeded", "invalid\_prompt"]

One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

One of the following:

"server\_error"

"rate\_limit\_exceeded"

"invalid\_prompt"

message: str

A human-readable description of the error.

max\_completion\_tokens: Optional[int]

The maximum number of completion tokens specified to have been used over the course of the run.

minimum256

max\_prompt\_tokens: Optional[int]

The maximum number of prompt tokens specified to have been used over the course of the run.

minimum256

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: str

The model that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

object: Literal["thread.run"]

The object type, which is always `thread.run`.

parallel\_tool\_calls: bool

Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

required\_action: Optional[RequiredAction]

Details on the action required to continue the run. Will be `null` if no action is required.

submit\_tool\_outputs: RequiredActionSubmitToolOutputs

Details on the tool outputs needed for this run to continue.

tool\_calls: List[[RequiredActionFunctionToolCall](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20required_action_function_tool_call%20%3E%20(schema))]

A list of the relevant tool calls.

id: str

The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

function: Function

The function definition.

arguments: str

The arguments that the model expects you to pass to the function.

name: str

The name of the function.

type: Literal["function"]

The type of tool call the output is required for. For now, this is always `function`.

type: Literal["submit\_tool\_outputs"]

For now, this is always `submit_tool_outputs`.

response\_format: Optional[AssistantResponseFormatOption]

Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly “stuck” request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

started\_at: Optional[int]

The Unix timestamp (in seconds) for when the run was started.

formatunixtime

status: [RunStatus](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run_status%20%3E%20(schema))

The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

thread\_id: str

The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

tool\_choice: Optional[AssistantToolChoiceOption]

Controls which (if any) tool is called by the model.
`none` means the model will not call any tools and instead generates a message.
`auto` is the default value and means the model can pick between generating a message or calling one or more tools.
`required` means the model must call one or more tools before responding to the user.
Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

tools: List[[AssistantTool](/api/reference/python/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant_tool%20%3E%20(schema))]

The list of tools that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

One of the following:

class CodeInterpreterTool: …

type: Literal["code\_interpreter"]

The type of tool being defined: `code_interpreter`

class FileSearchTool: …

type: Literal["file\_search"]

The type of tool being defined: `file_search`

file\_search: Optional[FileSearch]

Overrides for the file search tool.

max\_num\_results: Optional[int]

The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

minimum1

maximum50

ranking\_options: Optional[FileSearchRankingOptions]

The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score\_threshold of 0.

See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

score\_threshold: float

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

ranker: Optional[Literal["auto", "default\_2024\_08\_21"]]

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

"default\_2024\_08\_21"

class FunctionTool: …

function: [FunctionDefinition](/api/reference/python/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema))

type: Literal["function"]

The type of tool being defined: `function`

truncation\_strategy: Optional[TruncationStrategy]

Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

type: Literal["auto", "last\_messages"]

The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

One of the following:

"auto"

"last\_messages"

last\_messages: Optional[int]

The number of most recent messages from the thread when constructing the context for the run.

minimum1

usage: Optional[Usage]

Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

completion\_tokens: int

Number of completion tokens used over the course of the run.

prompt\_tokens: int

Number of prompt tokens used over the course of the run.

total\_tokens: int

Total number of tokens used (prompt + completion).

temperature: Optional[float]

The sampling temperature used for this run. If not set, defaults to 1.

top\_p: Optional[float]

The nucleus sampling value used for this run. If not set, defaults to 1.

Literal["queued", "in\_progress", "requires\_action", 6 more]

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

##### [List run steps](/api/reference/python/resources/beta/subresources/threads/subresources/runs/subresources/steps/methods/list)

Deprecated

beta.threads.runs.steps.list(strrun\_id, StepListParams\*\*kwargs)  -> SyncCursorPage[[RunStep](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))]

GET/threads/{thread\_id}/runs/{run\_id}/steps

##### [Retrieve run step](/api/reference/python/resources/beta/subresources/threads/subresources/runs/subresources/steps/methods/retrieve)

Deprecated

beta.threads.runs.steps.retrieve(strstep\_id, StepRetrieveParams\*\*kwargs)  -> [RunStep](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

GET/threads/{thread\_id}/runs/{run\_id}/steps/{step\_id}

##### ModelsExpand Collapse

class CodeInterpreterLogs: …

Text output from the Code Interpreter tool call as part of a run step.

index: int

The index of the output in the outputs array.

type: Literal["logs"]

Always `logs`.

logs: Optional[str]

The text output from the Code Interpreter tool call.

class CodeInterpreterOutputImage: …

index: int

The index of the output in the outputs array.

type: Literal["image"]

Always `image`.

image: Optional[Image]

file\_id: Optional[str]

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

class CodeInterpreterToolCall: …

Details of the Code Interpreter tool call the run step was involved in.

id: str

The ID of the tool call.

code\_interpreter: CodeInterpreter

The Code Interpreter tool call definition.

input: str

The input to the Code Interpreter tool call.

outputs: List[CodeInterpreterOutput]

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

class CodeInterpreterOutputLogs: …

Text output from the Code Interpreter tool call as part of a run step.

logs: str

The text output from the Code Interpreter tool call.

type: Literal["logs"]

Always `logs`.

class CodeInterpreterOutputImage: …

image: CodeInterpreterOutputImageImage

file\_id: str

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

type: Literal["image"]

Always `image`.

type: Literal["code\_interpreter"]

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

class CodeInterpreterToolCallDelta: …

Details of the Code Interpreter tool call the run step was involved in.

index: int

The index of the tool call in the tool calls array.

type: Literal["code\_interpreter"]

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

id: Optional[str]

The ID of the tool call.

code\_interpreter: Optional[CodeInterpreter]

The Code Interpreter tool call definition.

input: Optional[str]

The input to the Code Interpreter tool call.

outputs: Optional[List[CodeInterpreterOutput]]

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

class CodeInterpreterLogs: …

Text output from the Code Interpreter tool call as part of a run step.

index: int

The index of the output in the outputs array.

type: Literal["logs"]

Always `logs`.

logs: Optional[str]

The text output from the Code Interpreter tool call.

class CodeInterpreterOutputImage: …

index: int

The index of the output in the outputs array.

type: Literal["image"]

Always `image`.

image: Optional[Image]

file\_id: Optional[str]

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

class FileSearchToolCall: …

id: str

The ID of the tool call object.

file\_search: FileSearch

For now, this is always going to be an empty object.

ranking\_options: Optional[FileSearchRankingOptions]

The ranking options for the file search.

ranker: Literal["auto", "default\_2024\_08\_21"]

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

"default\_2024\_08\_21"

score\_threshold: float

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

results: Optional[List[FileSearchResult]]

The results of the file search.

file\_id: str

The ID of the file that result was found in.

file\_name: str

The name of the file that result was found in.

score: float

The score of the result. All values must be a floating point number between 0 and 1.

minimum0

maximum1

content: Optional[List[FileSearchResultContent]]

The content of the result that was found. The content is only included if requested via the include query parameter.

text: Optional[str]

The text content of the file.

type: Optional[Literal["text"]]

The type of the content.

type: Literal["file\_search"]

The type of tool call. This is always going to be `file_search` for this type of tool call.

class FileSearchToolCallDelta: …

file\_search: object

For now, this is always going to be an empty object.

index: int

The index of the tool call in the tool calls array.

type: Literal["file\_search"]

The type of tool call. This is always going to be `file_search` for this type of tool call.

id: Optional[str]

The ID of the tool call object.

class FunctionToolCall: …

id: str

The ID of the tool call object.

function: Function

The definition of the function that was called.

arguments: str

The arguments passed to the function.

name: str

The name of the function.

output: Optional[str]

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

type: Literal["function"]

The type of tool call. This is always going to be `function` for this type of tool call.

class FunctionToolCallDelta: …

index: int

The index of the tool call in the tool calls array.

type: Literal["function"]

The type of tool call. This is always going to be `function` for this type of tool call.

id: Optional[str]

The ID of the tool call object.

function: Optional[Function]

The definition of the function that was called.

arguments: Optional[str]

The arguments passed to the function.

name: Optional[str]

The name of the function.

output: Optional[str]

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

class MessageCreationStepDetails: …

Details of the message creation by the run step.

message\_creation: MessageCreation

message\_id: str

The ID of the message that was created by this run step.

type: Literal["message\_creation"]

Always `message_creation`.

class RunStep: …

Represents a step in execution of a run.

id: str

The identifier of the run step, which can be referenced in API endpoints.

assistant\_id: str

The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) associated with the run step.

cancelled\_at: Optional[int]

The Unix timestamp (in seconds) for when the run step was cancelled.

formatunixtime

completed\_at: Optional[int]

The Unix timestamp (in seconds) for when the run step completed.

formatunixtime

created\_at: int

The Unix timestamp (in seconds) for when the run step was created.

formatunixtime

expired\_at: Optional[int]

The Unix timestamp (in seconds) for when the run step expired. A step is considered expired if the parent run is expired.

formatunixtime

failed\_at: Optional[int]

The Unix timestamp (in seconds) for when the run step failed.

formatunixtime

last\_error: Optional[LastError]

The last error associated with this run step. Will be `null` if there are no errors.

code: Literal["server\_error", "rate\_limit\_exceeded"]

One of `server_error` or `rate_limit_exceeded`.

One of the following:

"server\_error"

"rate\_limit\_exceeded"

message: str

A human-readable description of the error.

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

object: Literal["thread.run.step"]

The object type, which is always `thread.run.step`.

run\_id: str

The ID of the [run](https://platform.openai.com/docs/api-reference/runs) that this run step is a part of.

status: Literal["in\_progress", "cancelled", "failed", 2 more]

The status of the run step, which can be either `in_progress`, `cancelled`, `failed`, `completed`, or `expired`.

One of the following:

"in\_progress"

"cancelled"

"failed"

"completed"

"expired"

step\_details: StepDetails

The details of the run step.

One of the following:

class MessageCreationStepDetails: …

Details of the message creation by the run step.

message\_creation: MessageCreation

message\_id: str

The ID of the message that was created by this run step.

type: Literal["message\_creation"]

Always `message_creation`.

class ToolCallsStepDetails: …

Details of the tool call.

tool\_calls: List[[ToolCall](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call%20%3E%20(schema))]

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

One of the following:

class CodeInterpreterToolCall: …

Details of the Code Interpreter tool call the run step was involved in.

id: str

The ID of the tool call.

code\_interpreter: CodeInterpreter

The Code Interpreter tool call definition.

input: str

The input to the Code Interpreter tool call.

outputs: List[CodeInterpreterOutput]

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

class CodeInterpreterOutputLogs: …

Text output from the Code Interpreter tool call as part of a run step.

logs: str

The text output from the Code Interpreter tool call.

type: Literal["logs"]

Always `logs`.

class CodeInterpreterOutputImage: …

image: CodeInterpreterOutputImageImage

file\_id: str

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

type: Literal["image"]

Always `image`.

type: Literal["code\_interpreter"]

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

class FileSearchToolCall: …

id: str

The ID of the tool call object.

file\_search: FileSearch

For now, this is always going to be an empty object.

ranking\_options: Optional[FileSearchRankingOptions]

The ranking options for the file search.

ranker: Literal["auto", "default\_2024\_08\_21"]

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

"default\_2024\_08\_21"

score\_threshold: float

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

results: Optional[List[FileSearchResult]]

The results of the file search.

file\_id: str

The ID of the file that result was found in.

file\_name: str

The name of the file that result was found in.

score: float

The score of the result. All values must be a floating point number between 0 and 1.

minimum0

maximum1

content: Optional[List[FileSearchResultContent]]

The content of the result that was found. The content is only included if requested via the include query parameter.

text: Optional[str]

The text content of the file.

type: Optional[Literal["text"]]

The type of the content.

type: Literal["file\_search"]

The type of tool call. This is always going to be `file_search` for this type of tool call.

class FunctionToolCall: …

id: str

The ID of the tool call object.

function: Function

The definition of the function that was called.

arguments: str

The arguments passed to the function.

name: str

The name of the function.

output: Optional[str]

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

type: Literal["function"]

The type of tool call. This is always going to be `function` for this type of tool call.

type: Literal["tool\_calls"]

Always `tool_calls`.

thread\_id: str

The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was run.

type: Literal["message\_creation", "tool\_calls"]

The type of run step, which can be either `message_creation` or `tool_calls`.

One of the following:

"message\_creation"

"tool\_calls"

usage: Optional[Usage]

Usage statistics related to the run step. This value will be `null` while the run step’s status is `in_progress`.

completion\_tokens: int

Number of completion tokens used over the course of the run step.

prompt\_tokens: int

Number of prompt tokens used over the course of the run step.

total\_tokens: int

Total number of tokens used (prompt + completion).

class RunStepDelta: …

The delta containing the fields that have changed on the run step.

step\_details: Optional[StepDetails]

The details of the run step.

One of the following:

class RunStepDeltaMessageDelta: …

Details of the message creation by the run step.

type: Literal["message\_creation"]

Always `message_creation`.

message\_creation: Optional[MessageCreation]

message\_id: Optional[str]

The ID of the message that was created by this run step.

class ToolCallDeltaObject: …

Details of the tool call.

type: Literal["tool\_calls"]

Always `tool_calls`.

tool\_calls: Optional[List[[ToolCallDelta](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call_delta%20%3E%20(schema))]]

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

One of the following:

class CodeInterpreterToolCallDelta: …

Details of the Code Interpreter tool call the run step was involved in.

index: int

The index of the tool call in the tool calls array.

type: Literal["code\_interpreter"]

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

id: Optional[str]

The ID of the tool call.

code\_interpreter: Optional[CodeInterpreter]

The Code Interpreter tool call definition.

input: Optional[str]

The input to the Code Interpreter tool call.

outputs: Optional[List[CodeInterpreterOutput]]

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

class CodeInterpreterLogs: …

Text output from the Code Interpreter tool call as part of a run step.

index: int

The index of the output in the outputs array.

type: Literal["logs"]

Always `logs`.

logs: Optional[str]

The text output from the Code Interpreter tool call.

class CodeInterpreterOutputImage: …

index: int

The index of the output in the outputs array.

type: Literal["image"]

Always `image`.

image: Optional[Image]

file\_id: Optional[str]

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

class FileSearchToolCallDelta: …

file\_search: object

For now, this is always going to be an empty object.

index: int

The index of the tool call in the tool calls array.

type: Literal["file\_search"]

The type of tool call. This is always going to be `file_search` for this type of tool call.

id: Optional[str]

The ID of the tool call object.

class FunctionToolCallDelta: …

index: int

The index of the tool call in the tool calls array.

type: Literal["function"]

The type of tool call. This is always going to be `function` for this type of tool call.

id: Optional[str]

The ID of the tool call object.

function: Optional[Function]

The definition of the function that was called.

arguments: Optional[str]

The arguments passed to the function.

name: Optional[str]

The name of the function.

output: Optional[str]

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

class RunStepDeltaEvent: …

Represents a run step delta i.e. any changed fields on a run step during streaming.

id: str

The identifier of the run step, which can be referenced in API endpoints.

delta: [RunStepDelta](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta%20%3E%20(schema))

The delta containing the fields that have changed on the run step.

object: Literal["thread.run.step.delta"]

The object type, which is always `thread.run.step.delta`.

class RunStepDeltaMessageDelta: …

Details of the message creation by the run step.

type: Literal["message\_creation"]

Always `message_creation`.

message\_creation: Optional[MessageCreation]

message\_id: Optional[str]

The ID of the message that was created by this run step.

Literal["step\_details.tool\_calls[\*].file\_search.results[\*].content"]

[ToolCall](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call%20%3E%20(schema))

Details of the Code Interpreter tool call the run step was involved in.

One of the following:

class CodeInterpreterToolCall: …

Details of the Code Interpreter tool call the run step was involved in.

id: str

The ID of the tool call.

code\_interpreter: CodeInterpreter

The Code Interpreter tool call definition.

input: str

The input to the Code Interpreter tool call.

outputs: List[CodeInterpreterOutput]

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

class CodeInterpreterOutputLogs: …

Text output from the Code Interpreter tool call as part of a run step.

logs: str

The text output from the Code Interpreter tool call.

type: Literal["logs"]

Always `logs`.

class CodeInterpreterOutputImage: …

image: CodeInterpreterOutputImageImage

file\_id: str

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

type: Literal["image"]

Always `image`.

type: Literal["code\_interpreter"]

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

class FileSearchToolCall: …

id: str

The ID of the tool call object.

file\_search: FileSearch

For now, this is always going to be an empty object.

ranking\_options: Optional[FileSearchRankingOptions]

The ranking options for the file search.

ranker: Literal["auto", "default\_2024\_08\_21"]

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

"default\_2024\_08\_21"

score\_threshold: float

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

results: Optional[List[FileSearchResult]]

The results of the file search.

file\_id: str

The ID of the file that result was found in.

file\_name: str

The name of the file that result was found in.

score: float

The score of the result. All values must be a floating point number between 0 and 1.

minimum0

maximum1

content: Optional[List[FileSearchResultContent]]

The content of the result that was found. The content is only included if requested via the include query parameter.

text: Optional[str]

The text content of the file.

type: Optional[Literal["text"]]

The type of the content.

type: Literal["file\_search"]

The type of tool call. This is always going to be `file_search` for this type of tool call.

class FunctionToolCall: …

id: str

The ID of the tool call object.

function: Function

The definition of the function that was called.

arguments: str

The arguments passed to the function.

name: str

The name of the function.

output: Optional[str]

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

type: Literal["function"]

The type of tool call. This is always going to be `function` for this type of tool call.

[ToolCallDelta](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call_delta%20%3E%20(schema))

Details of the Code Interpreter tool call the run step was involved in.

One of the following:

class CodeInterpreterToolCallDelta: …

Details of the Code Interpreter tool call the run step was involved in.

index: int

The index of the tool call in the tool calls array.

type: Literal["code\_interpreter"]

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

id: Optional[str]

The ID of the tool call.

code\_interpreter: Optional[CodeInterpreter]

The Code Interpreter tool call definition.

input: Optional[str]

The input to the Code Interpreter tool call.

outputs: Optional[List[CodeInterpreterOutput]]

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

class CodeInterpreterLogs: …

Text output from the Code Interpreter tool call as part of a run step.

index: int

The index of the output in the outputs array.

type: Literal["logs"]

Always `logs`.

logs: Optional[str]

The text output from the Code Interpreter tool call.

class CodeInterpreterOutputImage: …

index: int

The index of the output in the outputs array.

type: Literal["image"]

Always `image`.

image: Optional[Image]

file\_id: Optional[str]

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

class FileSearchToolCallDelta: …

file\_search: object

For now, this is always going to be an empty object.

index: int

The index of the tool call in the tool calls array.

type: Literal["file\_search"]

The type of tool call. This is always going to be `file_search` for this type of tool call.

id: Optional[str]

The ID of the tool call object.

class FunctionToolCallDelta: …

index: int

The index of the tool call in the tool calls array.

type: Literal["function"]

The type of tool call. This is always going to be `function` for this type of tool call.

id: Optional[str]

The ID of the tool call object.

function: Optional[Function]

The definition of the function that was called.

arguments: Optional[str]

The arguments passed to the function.

name: Optional[str]

The name of the function.

output: Optional[str]

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

class ToolCallDeltaObject: …

Details of the tool call.

type: Literal["tool\_calls"]

Always `tool_calls`.

tool\_calls: Optional[List[[ToolCallDelta](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call_delta%20%3E%20(schema))]]

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

One of the following:

class CodeInterpreterToolCallDelta: …

Details of the Code Interpreter tool call the run step was involved in.

index: int

The index of the tool call in the tool calls array.

type: Literal["code\_interpreter"]

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

id: Optional[str]

The ID of the tool call.

code\_interpreter: Optional[CodeInterpreter]

The Code Interpreter tool call definition.

input: Optional[str]

The input to the Code Interpreter tool call.

outputs: Optional[List[CodeInterpreterOutput]]

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

class CodeInterpreterLogs: …

Text output from the Code Interpreter tool call as part of a run step.

index: int

The index of the output in the outputs array.

type: Literal["logs"]

Always `logs`.

logs: Optional[str]

The text output from the Code Interpreter tool call.

class CodeInterpreterOutputImage: …

index: int

The index of the output in the outputs array.

type: Literal["image"]

Always `image`.

image: Optional[Image]

file\_id: Optional[str]

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

class FileSearchToolCallDelta: …

file\_search: object

For now, this is always going to be an empty object.

index: int

The index of the tool call in the tool calls array.

type: Literal["file\_search"]

The type of tool call. This is always going to be `file_search` for this type of tool call.

id: Optional[str]

The ID of the tool call object.

class FunctionToolCallDelta: …

index: int

The index of the tool call in the tool calls array.

type: Literal["function"]

The type of tool call. This is always going to be `function` for this type of tool call.

id: Optional[str]

The ID of the tool call object.

function: Optional[Function]

The definition of the function that was called.

arguments: Optional[str]

The arguments passed to the function.

name: Optional[str]

The name of the function.

output: Optional[str]

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

class ToolCallsStepDetails: …

Details of the tool call.

tool\_calls: List[[ToolCall](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call%20%3E%20(schema))]

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

One of the following:

class CodeInterpreterToolCall: …

Details of the Code Interpreter tool call the run step was involved in.

id: str

The ID of the tool call.

code\_interpreter: CodeInterpreter

The Code Interpreter tool call definition.

input: str

The input to the Code Interpreter tool call.

outputs: List[CodeInterpreterOutput]

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

class CodeInterpreterOutputLogs: …

Text output from the Code Interpreter tool call as part of a run step.

logs: str

The text output from the Code Interpreter tool call.

type: Literal["logs"]

Always `logs`.

class CodeInterpreterOutputImage: …

image: CodeInterpreterOutputImageImage

file\_id: str

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

type: Literal["image"]

Always `image`.

type: Literal["code\_interpreter"]

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

class FileSearchToolCall: …

id: str

The ID of the tool call object.

file\_search: FileSearch

For now, this is always going to be an empty object.

ranking\_options: Optional[FileSearchRankingOptions]

The ranking options for the file search.

ranker: Literal["auto", "default\_2024\_08\_21"]

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

"default\_2024\_08\_21"

score\_threshold: float

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

results: Optional[List[FileSearchResult]]

The results of the file search.

file\_id: str

The ID of the file that result was found in.

file\_name: str

The name of the file that result was found in.

score: float

The score of the result. All values must be a floating point number between 0 and 1.

minimum0

maximum1

content: Optional[List[FileSearchResultContent]]

The content of the result that was found. The content is only included if requested via the include query parameter.

text: Optional[str]

The text content of the file.

type: Optional[Literal["text"]]

The type of the content.

type: Literal["file\_search"]

The type of tool call. This is always going to be `file_search` for this type of tool call.

class FunctionToolCall: …

id: str

The ID of the tool call object.

function: Function

The definition of the function that was called.

arguments: str

The arguments passed to the function.

name: str

The name of the function.

output: Optional[str]

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

type: Literal["function"]

The type of tool call. This is always going to be `function` for this type of tool call.

type: Literal["tool\_calls"]

Always `tool_calls`.

#### BetaThreadsMessages

Build Assistants that can call models and use tools.

##### [List messages](/api/reference/python/resources/beta/subresources/threads/subresources/messages/methods/list)

Deprecated

beta.threads.messages.list(strthread\_id, MessageListParams\*\*kwargs)  -> SyncCursorPage[[Message](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema))]

GET/threads/{thread\_id}/messages

##### [Create message](/api/reference/python/resources/beta/subresources/threads/subresources/messages/methods/create)

Deprecated

beta.threads.messages.create(strthread\_id, MessageCreateParams\*\*kwargs)  -> [Message](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema))

POST/threads/{thread\_id}/messages

##### [Modify message](/api/reference/python/resources/beta/subresources/threads/subresources/messages/methods/update)

Deprecated

beta.threads.messages.update(strmessage\_id, MessageUpdateParams\*\*kwargs)  -> [Message](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema))

POST/threads/{thread\_id}/messages/{message\_id}

##### [Retrieve message](/api/reference/python/resources/beta/subresources/threads/subresources/messages/methods/retrieve)

Deprecated

beta.threads.messages.retrieve(strmessage\_id, MessageRetrieveParams\*\*kwargs)  -> [Message](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema))

GET/threads/{thread\_id}/messages/{message\_id}

##### [Delete message](/api/reference/python/resources/beta/subresources/threads/subresources/messages/methods/delete)

Deprecated

beta.threads.messages.delete(strmessage\_id, MessageDeleteParams\*\*kwargs)  -> [MessageDeleted](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_deleted%20%3E%20(schema))

DELETE/threads/{thread\_id}/messages/{message\_id}

##### ModelsExpand Collapse

[Annotation](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20annotation%20%3E%20(schema))

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

One of the following:

class FileCitationAnnotation: …

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

end\_index: int

minimum0

file\_citation: FileCitation

file\_id: str

The ID of the specific File the citation is from.

start\_index: int

minimum0

text: str

The text in the message content that needs to be replaced.

type: Literal["file\_citation"]

Always `file_citation`.

class FilePathAnnotation: …

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

end\_index: int

minimum0

file\_path: FilePath

file\_id: str

The ID of the file that was generated.

start\_index: int

minimum0

text: str

The text in the message content that needs to be replaced.

type: Literal["file\_path"]

Always `file_path`.

[AnnotationDelta](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20annotation_delta%20%3E%20(schema))

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

One of the following:

class FileCitationDeltaAnnotation: …

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

index: int

The index of the annotation in the text content part.

type: Literal["file\_citation"]

Always `file_citation`.

end\_index: Optional[int]

minimum0

file\_citation: Optional[FileCitation]

file\_id: Optional[str]

The ID of the specific File the citation is from.

quote: Optional[str]

The specific quote in the file.

start\_index: Optional[int]

minimum0

text: Optional[str]

The text in the message content that needs to be replaced.

class FilePathDeltaAnnotation: …

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

index: int

The index of the annotation in the text content part.

type: Literal["file\_path"]

Always `file_path`.

end\_index: Optional[int]

minimum0

file\_path: Optional[FilePath]

file\_id: Optional[str]

The ID of the file that was generated.

start\_index: Optional[int]

minimum0

text: Optional[str]

The text in the message content that needs to be replaced.

class FileCitationAnnotation: …

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

end\_index: int

minimum0

file\_citation: FileCitation

file\_id: str

The ID of the specific File the citation is from.

start\_index: int

minimum0

text: str

The text in the message content that needs to be replaced.

type: Literal["file\_citation"]

Always `file_citation`.

class FileCitationDeltaAnnotation: …

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

index: int

The index of the annotation in the text content part.

type: Literal["file\_citation"]

Always `file_citation`.

end\_index: Optional[int]

minimum0

file\_citation: Optional[FileCitation]

file\_id: Optional[str]

The ID of the specific File the citation is from.

quote: Optional[str]

The specific quote in the file.

start\_index: Optional[int]

minimum0

text: Optional[str]

The text in the message content that needs to be replaced.

class FilePathAnnotation: …

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

end\_index: int

minimum0

file\_path: FilePath

file\_id: str

The ID of the file that was generated.

start\_index: int

minimum0

text: str

The text in the message content that needs to be replaced.

type: Literal["file\_path"]

Always `file_path`.

class FilePathDeltaAnnotation: …

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

index: int

The index of the annotation in the text content part.

type: Literal["file\_path"]

Always `file_path`.

end\_index: Optional[int]

minimum0

file\_path: Optional[FilePath]

file\_id: Optional[str]

The ID of the file that was generated.

start\_index: Optional[int]

minimum0

text: Optional[str]

The text in the message content that needs to be replaced.

class ImageFile: …

file\_id: str

The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

detail: Optional[Literal["auto", "low", "high"]]

Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

One of the following:

"auto"

"low"

"high"

class ImageFileContentBlock: …

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

image\_file: [ImageFile](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file%20%3E%20(schema))

type: Literal["image\_file"]

Always `image_file`.

class ImageFileDelta: …

detail: Optional[Literal["auto", "low", "high"]]

Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

One of the following:

"auto"

"low"

"high"

file\_id: Optional[str]

The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

class ImageFileDeltaBlock: …

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

index: int

The index of the content part in the message.

type: Literal["image\_file"]

Always `image_file`.

image\_file: Optional[ImageFileDelta]

class ImageURL: …

url: str

The external URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

formaturi

detail: Optional[Literal["auto", "low", "high"]]

Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`. Default value is `auto`

One of the following:

"auto"

"low"

"high"

class ImageURLContentBlock: …

References an image URL in the content of a message.

image\_url: [ImageURL](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url%20%3E%20(schema))

type: Literal["image\_url"]

The type of the content part.

class ImageURLDelta: …

detail: Optional[Literal["auto", "low", "high"]]

Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`.

One of the following:

"auto"

"low"

"high"

url: Optional[str]

The URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

formaturi

class ImageURLDeltaBlock: …

References an image URL in the content of a message.

index: int

The index of the content part in the message.

type: Literal["image\_url"]

Always `image_url`.

image\_url: Optional[ImageURLDelta]

class Message: …

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

id: str

The identifier, which can be referenced in API endpoints.

assistant\_id: Optional[str]

If applicable, the ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) that authored this message.

attachments: Optional[List[Attachment]]

A list of files attached to the message, and the tools they were added to.

file\_id: Optional[str]

The ID of the file to attach to the message.

tools: Optional[List[AttachmentTool]]

The tools to add this file to.

One of the following:

class CodeInterpreterTool: …

type: Literal["code\_interpreter"]

The type of tool being defined: `code_interpreter`

class AttachmentToolAssistantToolsFileSearchTypeOnly: …

type: Literal["file\_search"]

The type of tool being defined: `file_search`

completed\_at: Optional[int]

The Unix timestamp (in seconds) for when the message was completed.

formatunixtime

content: List[[MessageContent](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_content%20%3E%20(schema))]

The content of the message in array of text and/or images.

One of the following:

class ImageFileContentBlock: …

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

image\_file: [ImageFile](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file%20%3E%20(schema))

type: Literal["image\_file"]

Always `image_file`.

class ImageURLContentBlock: …

References an image URL in the content of a message.

image\_url: [ImageURL](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url%20%3E%20(schema))

type: Literal["image\_url"]

The type of the content part.

class TextContentBlock: …

The text content that is part of a message.

text: [Text](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text%20%3E%20(schema))

type: Literal["text"]

Always `text`.

class RefusalContentBlock: …

The refusal content generated by the assistant.

refusal: str

type: Literal["refusal"]

Always `refusal`.

created\_at: int

The Unix timestamp (in seconds) for when the message was created.

formatunixtime

incomplete\_at: Optional[int]

The Unix timestamp (in seconds) for when the message was marked as incomplete.

formatunixtime

incomplete\_details: Optional[IncompleteDetails]

On an incomplete message, details about why the message is incomplete.

reason: Literal["content\_filter", "max\_tokens", "run\_cancelled", 2 more]

The reason the message is incomplete.

One of the following:

"content\_filter"

"max\_tokens"

"run\_cancelled"

"run\_expired"

"run\_failed"

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

object: Literal["thread.message"]

The object type, which is always `thread.message`.

role: Literal["user", "assistant"]

The entity that produced the message. One of `user` or `assistant`.

One of the following:

"user"

"assistant"

run\_id: Optional[str]

The ID of the [run](https://platform.openai.com/docs/api-reference/runs) associated with the creation of this message. Value is `null` when messages are created manually using the create message or create thread endpoints.

status: Literal["in\_progress", "incomplete", "completed"]

The status of the message, which can be either `in_progress`, `incomplete`, or `completed`.

One of the following:

"in\_progress"

"incomplete"

"completed"

thread\_id: str

The [thread](https://platform.openai.com/docs/api-reference/threads) ID that this message belongs to.

[MessageContent](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_content%20%3E%20(schema))

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

One of the following:

class ImageFileContentBlock: …

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

image\_file: [ImageFile](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file%20%3E%20(schema))

type: Literal["image\_file"]

Always `image_file`.

class ImageURLContentBlock: …

References an image URL in the content of a message.

image\_url: [ImageURL](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url%20%3E%20(schema))

type: Literal["image\_url"]

The type of the content part.

class TextContentBlock: …

The text content that is part of a message.

text: [Text](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text%20%3E%20(schema))

type: Literal["text"]

Always `text`.

class RefusalContentBlock: …

The refusal content generated by the assistant.

refusal: str

type: Literal["refusal"]

Always `refusal`.

[MessageContentDelta](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_content_delta%20%3E%20(schema))

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

One of the following:

class ImageFileDeltaBlock: …

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

index: int

The index of the content part in the message.

type: Literal["image\_file"]

Always `image_file`.

image\_file: Optional[ImageFileDelta]

class TextDeltaBlock: …

The text content that is part of a message.

index: int

The index of the content part in the message.

type: Literal["text"]

Always `text`.

text: Optional[TextDelta]

class RefusalDeltaBlock: …

The refusal content that is part of a message.

index: int

The index of the refusal part in the message.

type: Literal["refusal"]

Always `refusal`.

refusal: Optional[str]

class ImageURLDeltaBlock: …

References an image URL in the content of a message.

index: int

The index of the content part in the message.

type: Literal["image\_url"]

Always `image_url`.

image\_url: Optional[ImageURLDelta]

[MessageContentPartParam](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_content_part_param%20%3E%20(schema))

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

One of the following:

class ImageFileContentBlock: …

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

image\_file: [ImageFile](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file%20%3E%20(schema))

type: Literal["image\_file"]

Always `image_file`.

class ImageURLContentBlock: …

References an image URL in the content of a message.

image\_url: [ImageURL](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url%20%3E%20(schema))

type: Literal["image\_url"]

The type of the content part.

class TextContentBlockParam: …

The text content that is part of a message.

text: str

Text content to be sent to the model

type: Literal["text"]

Always `text`.

class MessageDeleted: …

id: str

deleted: bool

object: Literal["thread.message.deleted"]

class MessageDelta: …

The delta containing the fields that have changed on the Message.

content: Optional[List[[MessageContentDelta](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_content_delta%20%3E%20(schema))]]

The content of the message in array of text and/or images.

One of the following:

class ImageFileDeltaBlock: …

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

index: int

The index of the content part in the message.

type: Literal["image\_file"]

Always `image_file`.

image\_file: Optional[ImageFileDelta]

class TextDeltaBlock: …

The text content that is part of a message.

index: int

The index of the content part in the message.

type: Literal["text"]

Always `text`.

text: Optional[TextDelta]

class RefusalDeltaBlock: …

The refusal content that is part of a message.

index: int

The index of the refusal part in the message.

type: Literal["refusal"]

Always `refusal`.

refusal: Optional[str]

class ImageURLDeltaBlock: …

References an image URL in the content of a message.

index: int

The index of the content part in the message.

type: Literal["image\_url"]

Always `image_url`.

image\_url: Optional[ImageURLDelta]

role: Optional[Literal["user", "assistant"]]

The entity that produced the message. One of `user` or `assistant`.

One of the following:

"user"

"assistant"

class MessageDeltaEvent: …

Represents a message delta i.e. any changed fields on a message during streaming.

id: str

The identifier of the message, which can be referenced in API endpoints.

delta: [MessageDelta](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_delta%20%3E%20(schema))

The delta containing the fields that have changed on the Message.

object: Literal["thread.message.delta"]

The object type, which is always `thread.message.delta`.

class RefusalContentBlock: …

The refusal content generated by the assistant.

refusal: str

type: Literal["refusal"]

Always `refusal`.

class RefusalDeltaBlock: …

The refusal content that is part of a message.

index: int

The index of the refusal part in the message.

type: Literal["refusal"]

Always `refusal`.

refusal: Optional[str]

class Text: …

annotations: List[[Annotation](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20annotation%20%3E%20(schema))]

One of the following:

class FileCitationAnnotation: …

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

end\_index: int

minimum0

file\_citation: FileCitation

file\_id: str

The ID of the specific File the citation is from.

start\_index: int

minimum0

text: str

The text in the message content that needs to be replaced.

type: Literal["file\_citation"]

Always `file_citation`.

class FilePathAnnotation: …

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

end\_index: int

minimum0

file\_path: FilePath

file\_id: str

The ID of the file that was generated.

start\_index: int

minimum0

text: str

The text in the message content that needs to be replaced.

type: Literal["file\_path"]

Always `file_path`.

value: str

The data that makes up the text.

class TextContentBlock: …

The text content that is part of a message.

text: [Text](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text%20%3E%20(schema))

type: Literal["text"]

Always `text`.

class TextContentBlockParam: …

The text content that is part of a message.

text: str

Text content to be sent to the model

type: Literal["text"]

Always `text`.

class TextDelta: …

annotations: Optional[List[[AnnotationDelta](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20annotation_delta%20%3E%20(schema))]]

One of the following:

class FileCitationDeltaAnnotation: …

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

index: int

The index of the annotation in the text content part.

type: Literal["file\_citation"]

Always `file_citation`.

end\_index: Optional[int]

minimum0

file\_citation: Optional[FileCitation]

file\_id: Optional[str]

The ID of the specific File the citation is from.

quote: Optional[str]

The specific quote in the file.

start\_index: Optional[int]

minimum0

text: Optional[str]

The text in the message content that needs to be replaced.

class FilePathDeltaAnnotation: …

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

index: int

The index of the annotation in the text content part.

type: Literal["file\_path"]

Always `file_path`.

end\_index: Optional[int]

minimum0

file\_path: Optional[FilePath]

file\_id: Optional[str]

The ID of the file that was generated.

start\_index: Optional[int]

minimum0

text: Optional[str]

The text in the message content that needs to be replaced.

value: Optional[str]

The data that makes up the text.

class TextDeltaBlock: …

The text content that is part of a message.

index: int

The index of the content part in the message.

type: Literal["text"]

Always `text`.

text: Optional[TextDelta]
