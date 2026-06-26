<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/chatkit/subresources/threads/methods/list_items/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Beta](/api/reference/python/resources/beta)

[ChatKit](/api/reference/python/resources/beta/subresources/chatkit)

[Threads](/api/reference/python/resources/beta/subresources/chatkit/subresources/threads)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List ChatKit thread items

beta.chatkit.threads.list\_items(strthread\_id, ThreadListItemsParams\*\*kwargs)  -> SyncConversationCursorPage[Data]

GET/chatkit/threads/{thread\_id}/items

List items that belong to a ChatKit thread.

##### ParametersExpand Collapse

thread\_id: str

after: Optional[str]

List items created after this thread item ID. Defaults to null for the first page.

before: Optional[str]

List items created before this thread item ID. Defaults to null for the newest results.

limit: Optional[int]

Maximum number of thread items to return. Defaults to 20.

minimum0

maximum100

order: Optional[Literal["asc", "desc"]]

Sort order for results by creation time. Defaults to `desc`.

One of the following:

"asc"

"desc"

##### ReturnsExpand Collapse

Data

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

### List ChatKit thread items

Python

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

from openai import OpenAI

client = OpenAI()
page = client.beta.chatkit.threads.list_items(
    thread_id="cthr_123",
page = page.data[0]
print(page)

  "data": [
      "id": "cthi_user_001",
      "object": "chatkit.thread_item",
      "type": "user_message",
      "content": [
          "type": "input_text",
          "text": "I need help debugging an onboarding issue."
      ],
      "attachments": []
      "id": "cthi_assistant_002",
      "object": "chatkit.thread_item",
      "type": "assistant_message",
      "content": [
          "type": "output_text",
          "text": "Let's start by confirming the workflow version you deployed."
      ]
  ],
  "has_more": false,
  "object": "list"

##### Returns Examples

  "data": [
      "id": "cthi_user_001",
      "object": "chatkit.thread_item",
      "type": "user_message",
      "content": [
          "type": "input_text",
          "text": "I need help debugging an onboarding issue."
      ],
      "attachments": []
      "id": "cthi_assistant_002",
      "object": "chatkit.thread_item",
      "type": "assistant_message",
      "content": [
          "type": "output_text",
          "text": "Let's start by confirming the workflow version you deployed."
      ]
  ],
  "has_more": false,
  "object": "list"
