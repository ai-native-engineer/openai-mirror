<!-- source: https://developers.openai.com/api/reference/ruby/resources/beta/subresources/threads/subresources/messages/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Beta](/api/reference/ruby/resources/beta)

[Threads](/api/reference/ruby/resources/beta/subresources/threads)

[Messages](/api/reference/ruby/resources/beta/subresources/threads/subresources/messages)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List messages

Deprecated: The Assistants API is deprecated in favor of the Responses API

beta.threads.messages.list(thread\_id, \*\*kwargs) -> CursorPage<[Message](/api/reference/ruby/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)) { id, assistant\_id, attachments, 11 more } >

GET/threads/{thread\_id}/messages

Returns a list of messages for a given thread.

##### ParametersExpand Collapse

thread\_id: String

after: String

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

before: String

A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with obj\_foo, your subsequent call can include before=obj\_foo in order to fetch the previous page of the list.

limit: Integer

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

order: :asc | :desc

Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

One of the following:

:asc

:desc

run\_id: String

Filter messages by the run ID that generated them.

##### ReturnsExpand Collapse

class Message { id, assistant\_id, attachments, 11 more }

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

id: String

The identifier, which can be referenced in API endpoints.

assistant\_id: String

If applicable, the ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) that authored this message.

attachments: Array[Attachment{ file\_id, tools}]

A list of files attached to the message, and the tools they were added to.

file\_id: String

The ID of the file to attach to the message.

tools: Array[[CodeInterpreterTool](/api/reference/ruby/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20code_interpreter_tool%20%3E%20(schema)) { type }  | AssistantToolsFileSearchTypeOnly{ type}]

The tools to add this file to.

One of the following:

class CodeInterpreterTool { type }

type: :code\_interpreter

The type of tool being defined: `code_interpreter`

class AssistantToolsFileSearchTypeOnly { type }

type: :file\_search

The type of tool being defined: `file_search`

completed\_at: Integer

The Unix timestamp (in seconds) for when the message was completed.

formatunixtime

content: Array[[MessageContent](/api/reference/ruby/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_content%20%3E%20(schema))]

The content of the message in array of text and/or images.

One of the following:

class ImageFileContentBlock { image\_file, type }

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

image\_file: [ImageFile](/api/reference/ruby/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file%20%3E%20(schema)) { file\_id, detail }

file\_id: String

The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

detail: :auto | :low | :high

Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

One of the following:

:auto

:low

:high

type: :image\_file

Always `image_file`.

class ImageURLContentBlock { image\_url, type }

References an image URL in the content of a message.

image\_url: [ImageURL](/api/reference/ruby/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url%20%3E%20(schema)) { url, detail }

url: String

The external URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

formaturi

detail: :auto | :low | :high

Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`. Default value is `auto`

One of the following:

:auto

:low

:high

type: :image\_url

The type of the content part.

class TextContentBlock { text, type }

The text content that is part of a message.

text: [Text](/api/reference/ruby/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text%20%3E%20(schema)) { annotations, value }

annotations: Array[[Annotation](/api/reference/ruby/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20annotation%20%3E%20(schema))]

One of the following:

class FileCitationAnnotation { end\_index, file\_citation, start\_index, 2 more }

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

end\_index: Integer

minimum0

file\_citation: FileCitation{ file\_id}

file\_id: String

The ID of the specific File the citation is from.

start\_index: Integer

minimum0

text: String

The text in the message content that needs to be replaced.

type: :file\_citation

Always `file_citation`.

class FilePathAnnotation { end\_index, file\_path, start\_index, 2 more }

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

end\_index: Integer

minimum0

file\_path: FilePath{ file\_id}

file\_id: String

The ID of the file that was generated.

start\_index: Integer

minimum0

text: String

The text in the message content that needs to be replaced.

type: :file\_path

Always `file_path`.

value: String

The data that makes up the text.

type: :text

Always `text`.

class RefusalContentBlock { refusal, type }

The refusal content generated by the assistant.

refusal: String

type: :refusal

Always `refusal`.

created\_at: Integer

The Unix timestamp (in seconds) for when the message was created.

formatunixtime

incomplete\_at: Integer

The Unix timestamp (in seconds) for when the message was marked as incomplete.

formatunixtime

incomplete\_details: IncompleteDetails{ reason}

On an incomplete message, details about why the message is incomplete.

reason: :content\_filter | :max\_tokens | :run\_cancelled | 2 more

The reason the message is incomplete.

One of the following:

:content\_filter

:max\_tokens

:run\_cancelled

:run\_expired

:run\_failed

metadata: [Metadata](/api/reference/ruby/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

object: :"thread.message"

The object type, which is always `thread.message`.

role: :user | :assistant

The entity that produced the message. One of `user` or `assistant`.

One of the following:

:user

:assistant

run\_id: String

The ID of the [run](https://platform.openai.com/docs/api-reference/runs) associated with the creation of this message. Value is `null` when messages are created manually using the create message or create thread endpoints.

status: :in\_progress | :incomplete | :completed

The status of the message, which can be either `in_progress`, `incomplete`, or `completed`.

One of the following:

:in\_progress

:incomplete

:completed

thread\_id: String

The [thread](https://platform.openai.com/docs/api-reference/threads) ID that this message belongs to.

### List messages

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

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.beta.threads.messages.list("thread_id")

puts(page)

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
