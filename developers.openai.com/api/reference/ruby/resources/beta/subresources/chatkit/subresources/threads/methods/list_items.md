<!-- source: https://developers.openai.com/api/reference/ruby/resources/beta/subresources/chatkit/subresources/threads/methods/list_items/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Beta](/api/reference/ruby/resources/beta)

[ChatKit](/api/reference/ruby/resources/beta/subresources/chatkit)

[Threads](/api/reference/ruby/resources/beta/subresources/chatkit/subresources/threads)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List ChatKit thread items

beta.chatkit.threads.list\_items(thread\_id, \*\*kwargs) -> ConversationCursorPage<[ChatKitThreadUserMessageItem](/api/reference/ruby/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_user_message_item%20%3E%20(schema)) { id, attachments, content, 5 more }  | [ChatKitThreadAssistantMessageItem](/api/reference/ruby/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_assistant_message_item%20%3E%20(schema)) { id, content, created\_at, 3 more }  | [ChatKitWidgetItem](/api/reference/ruby/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_widget_item%20%3E%20(schema)) { id, created\_at, object, 3 more }  | 3 more>

GET/chatkit/threads/{thread\_id}/items

List items that belong to a ChatKit thread.

##### ParametersExpand Collapse

thread\_id: String

after: String

List items created after this thread item ID. Defaults to null for the first page.

before: String

List items created before this thread item ID. Defaults to null for the newest results.

limit: Integer

Maximum number of thread items to return. Defaults to 20.

minimum0

maximum100

order: :asc | :desc

Sort order for results by creation time. Defaults to `desc`.

One of the following:

:asc

:desc

##### ReturnsExpand Collapse

[ChatKitThreadUserMessageItem](/api/reference/ruby/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_user_message_item%20%3E%20(schema)) { id, attachments, content, 5 more }  | [ChatKitThreadAssistantMessageItem](/api/reference/ruby/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_assistant_message_item%20%3E%20(schema)) { id, content, created\_at, 3 more }  | [ChatKitWidgetItem](/api/reference/ruby/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_widget_item%20%3E%20(schema)) { id, created\_at, object, 3 more }  | 3 more

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

### List ChatKit thread items

Ruby

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

require "openai"

openai = OpenAI::Client.new

page = openai.beta.chatkit.threads.list_items("cthr_123")

puts(page)

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
