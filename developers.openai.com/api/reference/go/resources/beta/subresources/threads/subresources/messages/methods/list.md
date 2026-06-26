<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/threads/subresources/messages/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Beta](/api/reference/go/resources/beta)

[Threads](/api/reference/go/resources/beta/subresources/threads)

[Messages](/api/reference/go/resources/beta/subresources/threads/subresources/messages)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List messages

Deprecated: The Assistants API is deprecated in favor of the Responses API

client.Beta.Threads.Messages.List(ctx, threadID, query) (\*CursorPage[[Message](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema))], error)

GET/threads/{thread\_id}/messages

Returns a list of messages for a given thread.

##### ParametersExpand Collapse

threadID string

query BetaThreadMessageListParams

After param.Field[string]Optional

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

Before param.Field[string]Optional

A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with obj\_foo, your subsequent call can include before=obj\_foo in order to fetch the previous page of the list.

Limit param.Field[int64]Optional

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

Order param.Field[[BetaThreadMessageListParamsOrder](/api/reference/go/resources/beta/subresources/threads/subresources/messages/methods/list#(resource)%20beta.threads.messages%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))]Optional

Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

const BetaThreadMessageListParamsOrderAsc [BetaThreadMessageListParamsOrder](/api/reference/go/resources/beta/subresources/threads/subresources/messages/methods/list#(resource)%20beta.threads.messages%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)) = "asc"

const BetaThreadMessageListParamsOrderDesc [BetaThreadMessageListParamsOrder](/api/reference/go/resources/beta/subresources/threads/subresources/messages/methods/list#(resource)%20beta.threads.messages%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)) = "desc"

RunID param.Field[string]Optional

Filter messages by the run ID that generated them.

##### ReturnsExpand Collapse

type Message struct{…}

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

ID string

The identifier, which can be referenced in API endpoints.

AssistantID string

If applicable, the ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) that authored this message.

Attachments []MessageAttachment

A list of files attached to the message, and the tools they were added to.

FileID stringOptional

The ID of the file to attach to the message.

Tools []MessageAttachmentToolUnionOptional

The tools to add this file to.

One of the following:

type CodeInterpreterTool struct{…}

Type CodeInterpreter

The type of tool being defined: `code_interpreter`

type MessageAttachmentToolAssistantToolsFileSearchTypeOnly struct{…}

Type FileSearch

The type of tool being defined: `file_search`

CompletedAt int64

The Unix timestamp (in seconds) for when the message was completed.

formatunixtime

Content [][MessageContentUnion](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_content%20%3E%20(schema))

The content of the message in array of text and/or images.

One of the following:

type ImageFileContentBlock struct{…}

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

ImageFile [ImageFile](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file%20%3E%20(schema))

FileID string

The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

Detail ImageFileDetailOptional

Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

One of the following:

const ImageFileDetailAuto ImageFileDetail = "auto"

const ImageFileDetailLow ImageFileDetail = "low"

const ImageFileDetailHigh ImageFileDetail = "high"

Type ImageFile

Always `image_file`.

type ImageURLContentBlock struct{…}

References an image URL in the content of a message.

ImageURL [ImageURL](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url%20%3E%20(schema))

URL string

The external URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

formaturi

Detail ImageURLDetailOptional

Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`. Default value is `auto`

One of the following:

const ImageURLDetailAuto ImageURLDetail = "auto"

const ImageURLDetailLow ImageURLDetail = "low"

const ImageURLDetailHigh ImageURLDetail = "high"

Type ImageURL

The type of the content part.

type TextContentBlock struct{…}

The text content that is part of a message.

Text [Text](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text%20%3E%20(schema))

Annotations [][AnnotationUnion](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20annotation%20%3E%20(schema))

One of the following:

type FileCitationAnnotation struct{…}

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

EndIndex int64

minimum0

FileCitation FileCitationAnnotationFileCitation

FileID string

The ID of the specific File the citation is from.

StartIndex int64

minimum0

Text string

The text in the message content that needs to be replaced.

Type FileCitation

Always `file_citation`.

type FilePathAnnotation struct{…}

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

EndIndex int64

minimum0

FilePath FilePathAnnotationFilePath

FileID string

The ID of the file that was generated.

StartIndex int64

minimum0

Text string

The text in the message content that needs to be replaced.

Type FilePath

Always `file_path`.

Value string

The data that makes up the text.

Type Text

Always `text`.

type RefusalContentBlock struct{…}

The refusal content generated by the assistant.

Refusal string

Type Refusal

Always `refusal`.

CreatedAt int64

The Unix timestamp (in seconds) for when the message was created.

formatunixtime

IncompleteAt int64

The Unix timestamp (in seconds) for when the message was marked as incomplete.

formatunixtime

IncompleteDetails MessageIncompleteDetails

On an incomplete message, details about why the message is incomplete.

Reason string

The reason the message is incomplete.

One of the following:

const MessageIncompleteDetailsReasonContentFilter MessageIncompleteDetailsReason = "content\_filter"

const MessageIncompleteDetailsReasonMaxTokens MessageIncompleteDetailsReason = "max\_tokens"

const MessageIncompleteDetailsReasonRunCancelled MessageIncompleteDetailsReason = "run\_cancelled"

const MessageIncompleteDetailsReasonRunExpired MessageIncompleteDetailsReason = "run\_expired"

const MessageIncompleteDetailsReasonRunFailed MessageIncompleteDetailsReason = "run\_failed"

Metadata [Metadata](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

Object ThreadMessage

The object type, which is always `thread.message`.

Role MessageRole

The entity that produced the message. One of `user` or `assistant`.

One of the following:

const MessageRoleUser MessageRole = "user"

const MessageRoleAssistant MessageRole = "assistant"

RunID string

The ID of the [run](https://platform.openai.com/docs/api-reference/runs) associated with the creation of this message. Value is `null` when messages are created manually using the create message or create thread endpoints.

Status MessageStatus

The status of the message, which can be either `in_progress`, `incomplete`, or `completed`.

One of the following:

const MessageStatusInProgress MessageStatus = "in\_progress"

const MessageStatusIncomplete MessageStatus = "incomplete"

const MessageStatusCompleted MessageStatus = "completed"

ThreadID string

The [thread](https://platform.openai.com/docs/api-reference/threads) ID that this message belongs to.

### List messages

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
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  page, err := client.Beta.Threads.Messages.List(
    context.TODO(),
    "thread_id",
    openai.BetaThreadMessageListParams{

  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", page)

  "object": "list",
  "data": [
      "id": "msg_abc123",
      "object": "thread.message",
      "created_at": 1699016383,
      "assistant_id": null,
      "thread_id": "thread_abc123",
      "run_id": null,
      "role": "user",
      "content": [
          "type": "text",
          "text": {
            "value": "How does AI work? Explain it in simple terms.",
            "annotations": []
      ],
      "attachments": [],
      "metadata": {}
      "id": "msg_abc456",
      "object": "thread.message",
      "created_at": 1699016383,
      "assistant_id": null,
      "thread_id": "thread_abc123",
      "run_id": null,
      "role": "user",
      "content": [
          "type": "text",
          "text": {
            "value": "Hello, what is AI?",
            "annotations": []
      ],
      "attachments": [],
      "metadata": {}
  ],
  "first_id": "msg_abc123",
  "last_id": "msg_abc456",
  "has_more": false

##### Returns Examples

  "object": "list",
  "data": [
      "id": "msg_abc123",
      "object": "thread.message",
      "created_at": 1699016383,
      "assistant_id": null,
      "thread_id": "thread_abc123",
      "run_id": null,
      "role": "user",
      "content": [
          "type": "text",
          "text": {
            "value": "How does AI work? Explain it in simple terms.",
            "annotations": []
      ],
      "attachments": [],
      "metadata": {}
      "id": "msg_abc456",
      "object": "thread.message",
      "created_at": 1699016383,
      "assistant_id": null,
      "thread_id": "thread_abc123",
      "run_id": null,
      "role": "user",
      "content": [
          "type": "text",
          "text": {
            "value": "Hello, what is AI?",
            "annotations": []
      ],
      "attachments": [],
      "metadata": {}
  ],
  "first_id": "msg_abc123",
  "last_id": "msg_abc456",
  "has_more": false
