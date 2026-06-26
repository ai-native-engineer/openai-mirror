<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/chatkit/subresources/threads/methods/list_items/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Beta](/api/reference/go/resources/beta)

[ChatKit](/api/reference/go/resources/beta/subresources/chatkit)

[Threads](/api/reference/go/resources/beta/subresources/chatkit/subresources/threads)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List ChatKit thread items

client.Beta.ChatKit.Threads.ListItems(ctx, threadID, query) (\*ConversationCursorPage[ChatKitThreadItemListDataUnion], error)

GET/chatkit/threads/{thread\_id}/items

List items that belong to a ChatKit thread.

##### ParametersExpand Collapse

threadID string

query BetaChatKitThreadListItemsParams

After param.Field[string]Optional

List items created after this thread item ID. Defaults to null for the first page.

Before param.Field[string]Optional

List items created before this thread item ID. Defaults to null for the newest results.

Limit param.Field[int64]Optional

Maximum number of thread items to return. Defaults to 20.

minimum0

maximum100

Order param.Field[[BetaChatKitThreadListItemsParamsOrder](/api/reference/go/resources/beta/subresources/chatkit/subresources/threads/methods/list_items#(resource)%20beta.chatkit.threads%20%3E%20(method)%20list_items%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))]Optional

Sort order for results by creation time. Defaults to `desc`.

const BetaChatKitThreadListItemsParamsOrderAsc [BetaChatKitThreadListItemsParamsOrder](/api/reference/go/resources/beta/subresources/chatkit/subresources/threads/methods/list_items#(resource)%20beta.chatkit.threads%20%3E%20(method)%20list_items%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)) = "asc"

const BetaChatKitThreadListItemsParamsOrderDesc [BetaChatKitThreadListItemsParamsOrder](/api/reference/go/resources/beta/subresources/chatkit/subresources/threads/methods/list_items#(resource)%20beta.chatkit.threads%20%3E%20(method)%20list_items%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)) = "desc"

##### ReturnsExpand Collapse

type ChatKitThreadItemListDataUnion interface{…}

User-authored messages within a thread.

One of the following:

type ChatKitThreadUserMessageItem struct{…}

User-authored messages within a thread.

ID string

Identifier of the thread item.

Attachments [][ChatKitAttachment](/api/reference/go/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_attachment%20%3E%20(schema))

Attachments associated with the user message. Defaults to an empty list.

ID string

Identifier for the attachment.

MimeType string

MIME type of the attachment.

Name string

Original display name for the attachment.

PreviewURL string

Preview URL for rendering the attachment inline.

formaturi

Type ChatKitAttachmentType

Attachment discriminator.

One of the following:

const ChatKitAttachmentTypeImage ChatKitAttachmentType = "image"

const ChatKitAttachmentTypeFile ChatKitAttachmentType = "file"

Content []ChatKitThreadUserMessageItemContentUnion

Ordered content elements supplied by the user.

One of the following:

type ChatKitThreadUserMessageItemContentInputText struct{…}

Text block that a user contributed to the thread.

Text string

Plain-text content supplied by the user.

Type InputText

Type discriminator that is always `input_text`.

type ChatKitThreadUserMessageItemContentQuotedText struct{…}

Quoted snippet that the user referenced in their message.

Text string

Quoted text content.

Type QuotedText

Type discriminator that is always `quoted_text`.

CreatedAt int64

Unix timestamp (in seconds) for when the item was created.

formatunixtime

InferenceOptions ChatKitThreadUserMessageItemInferenceOptions

Inference overrides applied to the message. Defaults to null when unset.

Model string

Model name that generated the response. Defaults to null when using the session default.

ToolChoice ChatKitThreadUserMessageItemInferenceOptionsToolChoice

Preferred tool to invoke. Defaults to null when ChatKit should auto-select.

ID string

Identifier of the requested tool.

Object ChatKitThreadItem

Type discriminator that is always `chatkit.thread_item`.

ThreadID string

Identifier of the parent thread.

Type ChatKitUserMessage

type ChatKitThreadAssistantMessageItem struct{…}

Assistant-authored message within a thread.

ID string

Identifier of the thread item.

Content [][ChatKitResponseOutputText](/api/reference/go/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_response_output_text%20%3E%20(schema))

Ordered assistant response segments.

Annotations []ChatKitResponseOutputTextAnnotationUnion

Ordered list of annotations attached to the response text.

One of the following:

type ChatKitResponseOutputTextAnnotationFile struct{…}

Annotation that references an uploaded file.

Source ChatKitResponseOutputTextAnnotationFileSource

File attachment referenced by the annotation.

Filename string

Filename referenced by the annotation.

Type File

Type discriminator that is always `file`.

Type File

Type discriminator that is always `file` for this annotation.

type ChatKitResponseOutputTextAnnotationURL struct{…}

Annotation that references a URL.

Source ChatKitResponseOutputTextAnnotationURLSource

URL referenced by the annotation.

Type URL

Type discriminator that is always `url`.

URL string

URL referenced by the annotation.

formaturi

Type URL

Type discriminator that is always `url` for this annotation.

Text string

Assistant generated text.

Type OutputText

Type discriminator that is always `output_text`.

CreatedAt int64

Unix timestamp (in seconds) for when the item was created.

formatunixtime

Object ChatKitThreadItem

Type discriminator that is always `chatkit.thread_item`.

ThreadID string

Identifier of the parent thread.

Type ChatKitAssistantMessage

Type discriminator that is always `chatkit.assistant_message`.

type ChatKitWidgetItem struct{…}

Thread item that renders a widget payload.

ID string

Identifier of the thread item.

CreatedAt int64

Unix timestamp (in seconds) for when the item was created.

formatunixtime

Object ChatKitThreadItem

Type discriminator that is always `chatkit.thread_item`.

ThreadID string

Identifier of the parent thread.

Type ChatKitWidget

Type discriminator that is always `chatkit.widget`.

Widget string

Serialized widget payload rendered in the UI.

type ChatKitThreadItemListDataChatKitClientToolCall struct{…}

Record of a client side tool invocation initiated by the assistant.

ID string

Identifier of the thread item.

Arguments string

JSON-encoded arguments that were sent to the tool.

CallID string

Identifier for the client tool call.

CreatedAt int64

Unix timestamp (in seconds) for when the item was created.

formatunixtime

Name string

Tool name that was invoked.

Object ChatKitThreadItem

Type discriminator that is always `chatkit.thread_item`.

Output string

JSON-encoded output captured from the tool. Defaults to null while execution is in progress.

Status string

Execution status for the tool call.

One of the following:

const ChatKitThreadItemListDataChatKitClientToolCallStatusInProgress ChatKitThreadItemListDataChatKitClientToolCallStatus = "in\_progress"

const ChatKitThreadItemListDataChatKitClientToolCallStatusCompleted ChatKitThreadItemListDataChatKitClientToolCallStatus = "completed"

ThreadID string

Identifier of the parent thread.

Type ChatKitClientToolCall

Type discriminator that is always `chatkit.client_tool_call`.

type ChatKitThreadItemListDataChatKitTask struct{…}

Task emitted by the workflow to show progress and status updates.

ID string

Identifier of the thread item.

CreatedAt int64

Unix timestamp (in seconds) for when the item was created.

formatunixtime

Heading string

Optional heading for the task. Defaults to null when not provided.

Object ChatKitThreadItem

Type discriminator that is always `chatkit.thread_item`.

Summary string

Optional summary that describes the task. Defaults to null when omitted.

TaskType string

Subtype for the task.

One of the following:

const ChatKitThreadItemListDataChatKitTaskTaskTypeCustom ChatKitThreadItemListDataChatKitTaskTaskType = "custom"

const ChatKitThreadItemListDataChatKitTaskTaskTypeThought ChatKitThreadItemListDataChatKitTaskTaskType = "thought"

ThreadID string

Identifier of the parent thread.

Type ChatKitTask

Type discriminator that is always `chatkit.task`.

type ChatKitThreadItemListDataChatKitTaskGroup struct{…}

Collection of workflow tasks grouped together in the thread.

ID string

Identifier of the thread item.

CreatedAt int64

Unix timestamp (in seconds) for when the item was created.

formatunixtime

Object ChatKitThreadItem

Type discriminator that is always `chatkit.thread_item`.

Tasks []ChatKitThreadItemListDataChatKitTaskGroupTask

Tasks included in the group.

Heading string

Optional heading for the grouped task. Defaults to null when not provided.

Summary string

Optional summary that describes the grouped task. Defaults to null when omitted.

Type string

Subtype for the grouped task.

One of the following:

const ChatKitThreadItemListDataChatKitTaskGroupTaskTypeCustom ChatKitThreadItemListDataChatKitTaskGroupTaskType = "custom"

const ChatKitThreadItemListDataChatKitTaskGroupTaskTypeThought ChatKitThreadItemListDataChatKitTaskGroupTaskType = "thought"

ThreadID string

Identifier of the parent thread.

Type ChatKitTaskGroup

Type discriminator that is always `chatkit.task_group`.

### List ChatKit thread items

Go

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"

func main() {
  client := openai.NewClient()
  page, err := client.Beta.ChatKit.Threads.ListItems(
    context.TODO(),
    "cthr_123",
    openai.BetaChatKitThreadListItemsParams{

  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", page)

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
