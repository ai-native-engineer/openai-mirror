<!-- source: https://developers.openai.com/api/reference/resources/beta/subresources/chatkit/subresources/threads/methods/list_items/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Beta](/api/reference/resources/beta)

[ChatKit](/api/reference/resources/beta/subresources/chatkit)

[Threads](/api/reference/resources/beta/subresources/chatkit/subresources/threads)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List ChatKit thread items

GET/chatkit/threads/{thread\_id}/items

List items that belong to a ChatKit thread.

##### Path ParametersExpand Collapse

thread\_id: string

##### Query ParametersExpand Collapse

after: optional string

List items created after this thread item ID. Defaults to null for the first page.

before: optional string

List items created before this thread item ID. Defaults to null for the newest results.

limit: optional number

Maximum number of thread items to return. Defaults to 20.

minimum0

maximum100

order: optional "asc" or "desc"

Sort order for results by creation time. Defaults to `desc`.

One of the following:

"asc"

"desc"

##### ReturnsExpand Collapse

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

### List ChatKit thread items

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl "https://api.openai.com/v1/chatkit/threads/cthr_abc123/items?limit=3" \
  -H "OpenAI-Beta: chatkit_beta=v1" \
  -H "Authorization: Bearer $OPENAI_API_KEY"

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
