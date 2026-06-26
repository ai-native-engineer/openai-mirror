<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/chatkit/subresources/threads/methods/list_items/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Beta](/api/reference/java/resources/beta)

[ChatKit](/api/reference/java/resources/beta/subresources/chatkit)

[Threads](/api/reference/java/resources/beta/subresources/chatkit/subresources/threads)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List ChatKit thread items

ThreadListItemsPage beta().chatkit().threads().listItems(ThreadListItemsParamsparams = ThreadListItemsParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/chatkit/threads/{thread\_id}/items

List items that belong to a ChatKit thread.

##### ParametersExpand Collapse

ThreadListItemsParams params

Optional<String> threadId

Optional<String> after

List items created after this thread item ID. Defaults to null for the first page.

Optional<String> before

List items created before this thread item ID. Defaults to null for the newest results.

Optional<Long> limit

Maximum number of thread items to return. Defaults to 20.

minimum0

maximum100

Optional<[Order](/api/reference/java/resources/beta/subresources/chatkit/subresources/threads/methods/list_items#(resource)%20beta.chatkit.threads%20%3E%20(method)%20list_items%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))> order

Sort order for results by creation time. Defaults to `desc`.

ASC("asc")

DESC("desc")

##### ReturnsExpand Collapse

class Data: A class that can be one of several variants.union

User-authored messages within a thread.

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

### List ChatKit thread items

Java

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.chatkit.threads.ThreadListItemsPage;
import com.openai.models.beta.chatkit.threads.ThreadListItemsParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ThreadListItemsPage page = client.beta().chatkit().threads().listItems("cthr_123");

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
