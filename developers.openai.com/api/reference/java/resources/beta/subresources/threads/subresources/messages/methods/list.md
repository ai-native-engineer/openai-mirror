<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/threads/subresources/messages/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Beta](/api/reference/java/resources/beta)

[Threads](/api/reference/java/resources/beta/subresources/threads)

[Messages](/api/reference/java/resources/beta/subresources/threads/subresources/messages)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List messages

Deprecated: The Assistants API is deprecated in favor of the Responses API

MessageListPage beta().threads().messages().list(MessageListParamsparams = MessageListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/threads/{thread\_id}/messages

Returns a list of messages for a given thread.

##### ParametersExpand Collapse

MessageListParams params

Optional<String> threadId

Optional<String> after

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

Optional<String> before

A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with obj\_foo, your subsequent call can include before=obj\_foo in order to fetch the previous page of the list.

Optional<Long> limit

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

Optional<[Order](/api/reference/java/resources/beta/subresources/threads/subresources/messages/methods/list#(resource)%20beta.threads.messages%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))> order

Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

ASC("asc")

DESC("desc")

Optional<String> runId

Filter messages by the run ID that generated them.

##### ReturnsExpand Collapse

class Message:

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

String id

The identifier, which can be referenced in API endpoints.

Optional<String> assistantId

If applicable, the ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) that authored this message.

Optional<List<Attachment>> attachments

A list of files attached to the message, and the tools they were added to.

Optional<String> fileId

The ID of the file to attach to the message.

Optional<List<Tool>> tools

The tools to add this file to.

One of the following:

class CodeInterpreterTool:

JsonValue; type "code\_interpreter"constant"code\_interpreter"constant

The type of tool being defined: `code_interpreter`

JsonValue;

JsonValue; type "file\_search"constant"file\_search"constant

The type of tool being defined: `file_search`

Optional<Long> completedAt

The Unix timestamp (in seconds) for when the message was completed.

formatunixtime

List<[MessageContent](/api/reference/java/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_content%20%3E%20(schema))> content

The content of the message in array of text and/or images.

One of the following:

class ImageFileContentBlock:

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

[ImageFile](/api/reference/java/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file%20%3E%20(schema)) imageFile

String fileId

The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

Optional<Detail> detail

Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

One of the following:

AUTO("auto")

LOW("low")

HIGH("high")

JsonValue; type "image\_file"constant"image\_file"constant

Always `image_file`.

class ImageUrlContentBlock:

References an image URL in the content of a message.

[ImageUrl](/api/reference/java/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url%20%3E%20(schema)) imageUrl

String url

The external URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

formaturi

Optional<Detail> detail

Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`. Default value is `auto`

One of the following:

AUTO("auto")

LOW("low")

HIGH("high")

JsonValue; type "image\_url"constant"image\_url"constant

The type of the content part.

class TextContentBlock:

The text content that is part of a message.

[Text](/api/reference/java/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text%20%3E%20(schema)) text

List<[Annotation](/api/reference/java/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20annotation%20%3E%20(schema))> annotations

One of the following:

class FileCitationAnnotation:

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

long endIndex

minimum0

FileCitation fileCitation

String fileId

The ID of the specific File the citation is from.

long startIndex

minimum0

String text

The text in the message content that needs to be replaced.

JsonValue; type "file\_citation"constant"file\_citation"constant

Always `file_citation`.

class FilePathAnnotation:

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

long endIndex

minimum0

FilePath filePath

String fileId

The ID of the file that was generated.

long startIndex

minimum0

String text

The text in the message content that needs to be replaced.

JsonValue; type "file\_path"constant"file\_path"constant

Always `file_path`.

String value

The data that makes up the text.

JsonValue; type "text"constant"text"constant

Always `text`.

class RefusalContentBlock:

The refusal content generated by the assistant.

String refusal

JsonValue; type "refusal"constant"refusal"constant

Always `refusal`.

long createdAt

The Unix timestamp (in seconds) for when the message was created.

formatunixtime

Optional<Long> incompleteAt

The Unix timestamp (in seconds) for when the message was marked as incomplete.

formatunixtime

Optional<IncompleteDetails> incompleteDetails

On an incomplete message, details about why the message is incomplete.

Reason reason

The reason the message is incomplete.

One of the following:

CONTENT\_FILTER("content\_filter")

MAX\_TOKENS("max\_tokens")

RUN\_CANCELLED("run\_cancelled")

RUN\_EXPIRED("run\_expired")

RUN\_FAILED("run\_failed")

Optional<Metadata> metadata

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

JsonValue; object\_ "thread.message"constant"thread.message"constant

The object type, which is always `thread.message`.

Role role

The entity that produced the message. One of `user` or `assistant`.

One of the following:

USER("user")

ASSISTANT("assistant")

Optional<String> runId

The ID of the [run](https://platform.openai.com/docs/api-reference/runs) associated with the creation of this message. Value is `null` when messages are created manually using the create message or create thread endpoints.

Status status

The status of the message, which can be either `in_progress`, `incomplete`, or `completed`.

One of the following:

IN\_PROGRESS("in\_progress")

INCOMPLETE("incomplete")

COMPLETED("completed")

String threadId

The [thread](https://platform.openai.com/docs/api-reference/threads) ID that this message belongs to.

### List messages

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
import com.openai.models.beta.threads.messages.MessageListPage;
import com.openai.models.beta.threads.messages.MessageListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        MessageListPage page = client.beta().threads().messages().list("thread_id");

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
