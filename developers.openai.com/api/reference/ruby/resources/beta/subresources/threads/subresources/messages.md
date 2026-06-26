<!-- source: https://developers.openai.com/api/reference/ruby/resources/beta/subresources/threads/subresources/messages/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Beta](/api/reference/ruby/resources/beta)

[Threads](/api/reference/ruby/resources/beta/subresources/threads)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Messages

Build Assistants that can call models and use tools.

##### [List messages](/api/reference/ruby/resources/beta/subresources/threads/subresources/messages/methods/list)

Deprecated

beta.threads.messages.list(thread\_id, \*\*kwargs) -> CursorPage<[Message](/api/reference/ruby/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)) { id, assistant\_id, attachments, 11 more } >

GET/threads/{thread\_id}/messages

##### [Create message](/api/reference/ruby/resources/beta/subresources/threads/subresources/messages/methods/create)

Deprecated

beta.threads.messages.create(thread\_id, \*\*kwargs) -> [Message](/api/reference/ruby/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)) { id, assistant\_id, attachments, 11 more }

POST/threads/{thread\_id}/messages

##### [Modify message](/api/reference/ruby/resources/beta/subresources/threads/subresources/messages/methods/update)

Deprecated

beta.threads.messages.update(message\_id, \*\*kwargs) -> [Message](/api/reference/ruby/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)) { id, assistant\_id, attachments, 11 more }

POST/threads/{thread\_id}/messages/{message\_id}

##### [Retrieve message](/api/reference/ruby/resources/beta/subresources/threads/subresources/messages/methods/retrieve)

Deprecated

beta.threads.messages.retrieve(message\_id, \*\*kwargs) -> [Message](/api/reference/ruby/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)) { id, assistant\_id, attachments, 11 more }

GET/threads/{thread\_id}/messages/{message\_id}

##### [Delete message](/api/reference/ruby/resources/beta/subresources/threads/subresources/messages/methods/delete)

Deprecated

beta.threads.messages.delete(message\_id, \*\*kwargs) -> [MessageDeleted](/api/reference/ruby/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_deleted%20%3E%20(schema)) { id, deleted, object }

DELETE/threads/{thread\_id}/messages/{message\_id}

##### ModelsExpand Collapse

Annotation = [FileCitationAnnotation](/api/reference/ruby/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_annotation%20%3E%20(schema)) { end\_index, file\_citation, start\_index, 2 more }  | [FilePathAnnotation](/api/reference/ruby/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20file_path_annotation%20%3E%20(schema)) { end\_index, file\_path, start\_index, 2 more }

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

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

AnnotationDelta = [FileCitationDeltaAnnotation](/api/reference/ruby/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_delta_annotation%20%3E%20(schema)) { index, type, end\_index, 3 more }  | [FilePathDeltaAnnotation](/api/reference/ruby/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20file_path_delta_annotation%20%3E%20(schema)) { index, type, end\_index, 3 more }

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

One of the following:

class FileCitationDeltaAnnotation { index, type, end\_index, 3 more }

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

index: Integer

The index of the annotation in the text content part.

type: :file\_citation

Always `file_citation`.

end\_index: Integer

minimum0

file\_citation: FileCitation{ file\_id, quote}

file\_id: String

The ID of the specific File the citation is from.

quote: String

The specific quote in the file.

start\_index: Integer

minimum0

text: String

The text in the message content that needs to be replaced.

class FilePathDeltaAnnotation { index, type, end\_index, 3 more }

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

index: Integer

The index of the annotation in the text content part.

type: :file\_path

Always `file_path`.

end\_index: Integer

minimum0

file\_path: FilePath{ file\_id}

file\_id: String

The ID of the file that was generated.

start\_index: Integer

minimum0

text: String

The text in the message content that needs to be replaced.

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

class FileCitationDeltaAnnotation { index, type, end\_index, 3 more }

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

index: Integer

The index of the annotation in the text content part.

type: :file\_citation

Always `file_citation`.

end\_index: Integer

minimum0

file\_citation: FileCitation{ file\_id, quote}

file\_id: String

The ID of the specific File the citation is from.

quote: String

The specific quote in the file.

start\_index: Integer

minimum0

text: String

The text in the message content that needs to be replaced.

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

class FilePathDeltaAnnotation { index, type, end\_index, 3 more }

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

index: Integer

The index of the annotation in the text content part.

type: :file\_path

Always `file_path`.

end\_index: Integer

minimum0

file\_path: FilePath{ file\_id}

file\_id: String

The ID of the file that was generated.

start\_index: Integer

minimum0

text: String

The text in the message content that needs to be replaced.

class ImageFile { file\_id, detail }

file\_id: String

The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

detail: :auto | :low | :high

Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

One of the following:

:auto

:low

:high

class ImageFileContentBlock { image\_file, type }

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

image\_file: [ImageFile](/api/reference/ruby/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file%20%3E%20(schema)) { file\_id, detail }

type: :image\_file

Always `image_file`.

class ImageFileDelta { detail, file\_id }

detail: :auto | :low | :high

Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

One of the following:

:auto

:low

:high

file\_id: String

The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

class ImageFileDeltaBlock { index, type, image\_file }

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

index: Integer

The index of the content part in the message.

type: :image\_file

Always `image_file`.

image\_file: [ImageFileDelta](/api/reference/ruby/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_delta%20%3E%20(schema)) { detail, file\_id }

class ImageURL { url, detail }

url: String

The external URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

formaturi

detail: :auto | :low | :high

Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`. Default value is `auto`

One of the following:

:auto

:low

:high

class ImageURLContentBlock { image\_url, type }

References an image URL in the content of a message.

image\_url: [ImageURL](/api/reference/ruby/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url%20%3E%20(schema)) { url, detail }

type: :image\_url

The type of the content part.

class ImageURLDelta { detail, url }

detail: :auto | :low | :high

Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`.

One of the following:

:auto

:low

:high

url: String

The URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

formaturi

class ImageURLDeltaBlock { index, type, image\_url }

References an image URL in the content of a message.

index: Integer

The index of the content part in the message.

type: :image\_url

Always `image_url`.

image\_url: [ImageURLDelta](/api/reference/ruby/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_delta%20%3E%20(schema)) { detail, url }

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

type: :image\_file

Always `image_file`.

class ImageURLContentBlock { image\_url, type }

References an image URL in the content of a message.

image\_url: [ImageURL](/api/reference/ruby/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url%20%3E%20(schema)) { url, detail }

type: :image\_url

The type of the content part.

class TextContentBlock { text, type }

The text content that is part of a message.

text: [Text](/api/reference/ruby/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text%20%3E%20(schema)) { annotations, value }

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

MessageContent = [ImageFileContentBlock](/api/reference/ruby/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_content_block%20%3E%20(schema)) { image\_file, type }  | [ImageURLContentBlock](/api/reference/ruby/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_content_block%20%3E%20(schema)) { image\_url, type }  | [TextContentBlock](/api/reference/ruby/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text_content_block%20%3E%20(schema)) { text, type }  | [RefusalContentBlock](/api/reference/ruby/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20refusal_content_block%20%3E%20(schema)) { refusal, type }

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

One of the following:

class ImageFileContentBlock { image\_file, type }

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

image\_file: [ImageFile](/api/reference/ruby/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file%20%3E%20(schema)) { file\_id, detail }

type: :image\_file

Always `image_file`.

class ImageURLContentBlock { image\_url, type }

References an image URL in the content of a message.

image\_url: [ImageURL](/api/reference/ruby/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url%20%3E%20(schema)) { url, detail }

type: :image\_url

The type of the content part.

class TextContentBlock { text, type }

The text content that is part of a message.

text: [Text](/api/reference/ruby/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text%20%3E%20(schema)) { annotations, value }

type: :text

Always `text`.

class RefusalContentBlock { refusal, type }

The refusal content generated by the assistant.

refusal: String

type: :refusal

Always `refusal`.

MessageContentDelta = [ImageFileDeltaBlock](/api/reference/ruby/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_delta_block%20%3E%20(schema)) { index, type, image\_file }  | [TextDeltaBlock](/api/reference/ruby/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text_delta_block%20%3E%20(schema)) { index, type, text }  | [RefusalDeltaBlock](/api/reference/ruby/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20refusal_delta_block%20%3E%20(schema)) { index, type, refusal }  | [ImageURLDeltaBlock](/api/reference/ruby/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_delta_block%20%3E%20(schema)) { index, type, image\_url }

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

One of the following:

class ImageFileDeltaBlock { index, type, image\_file }

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

index: Integer

The index of the content part in the message.

type: :image\_file

Always `image_file`.

image\_file: [ImageFileDelta](/api/reference/ruby/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_delta%20%3E%20(schema)) { detail, file\_id }

class TextDeltaBlock { index, type, text }

The text content that is part of a message.

index: Integer

The index of the content part in the message.

type: :text

Always `text`.

text: [TextDelta](/api/reference/ruby/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text_delta%20%3E%20(schema)) { annotations, value }

class RefusalDeltaBlock { index, type, refusal }

The refusal content that is part of a message.

index: Integer

The index of the refusal part in the message.

type: :refusal

Always `refusal`.

refusal: String

class ImageURLDeltaBlock { index, type, image\_url }

References an image URL in the content of a message.

index: Integer

The index of the content part in the message.

type: :image\_url

Always `image_url`.

image\_url: [ImageURLDelta](/api/reference/ruby/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_delta%20%3E%20(schema)) { detail, url }

MessageContentPartParam = [ImageFileContentBlock](/api/reference/ruby/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_content_block%20%3E%20(schema)) { image\_file, type }  | [ImageURLContentBlock](/api/reference/ruby/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_content_block%20%3E%20(schema)) { image\_url, type }  | [TextContentBlockParam](/api/reference/ruby/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text_content_block_param%20%3E%20(schema)) { text, type }

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

One of the following:

class ImageFileContentBlock { image\_file, type }

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

image\_file: [ImageFile](/api/reference/ruby/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file%20%3E%20(schema)) { file\_id, detail }

type: :image\_file

Always `image_file`.

class ImageURLContentBlock { image\_url, type }

References an image URL in the content of a message.

image\_url: [ImageURL](/api/reference/ruby/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url%20%3E%20(schema)) { url, detail }

type: :image\_url

The type of the content part.

class TextContentBlockParam { text, type }

The text content that is part of a message.

text: String

Text content to be sent to the model

type: :text

Always `text`.

class MessageDeleted { id, deleted, object }

id: String

deleted: bool

object: :"thread.message.deleted"

class MessageDelta { content, role }

The delta containing the fields that have changed on the Message.

content: Array[[MessageContentDelta](/api/reference/ruby/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_content_delta%20%3E%20(schema))]

The content of the message in array of text and/or images.

One of the following:

class ImageFileDeltaBlock { index, type, image\_file }

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

index: Integer

The index of the content part in the message.

type: :image\_file

Always `image_file`.

image\_file: [ImageFileDelta](/api/reference/ruby/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_delta%20%3E%20(schema)) { detail, file\_id }

class TextDeltaBlock { index, type, text }

The text content that is part of a message.

index: Integer

The index of the content part in the message.

type: :text

Always `text`.

text: [TextDelta](/api/reference/ruby/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text_delta%20%3E%20(schema)) { annotations, value }

class RefusalDeltaBlock { index, type, refusal }

The refusal content that is part of a message.

index: Integer

The index of the refusal part in the message.

type: :refusal

Always `refusal`.

refusal: String

class ImageURLDeltaBlock { index, type, image\_url }

References an image URL in the content of a message.

index: Integer

The index of the content part in the message.

type: :image\_url

Always `image_url`.

image\_url: [ImageURLDelta](/api/reference/ruby/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_delta%20%3E%20(schema)) { detail, url }

role: :user | :assistant

The entity that produced the message. One of `user` or `assistant`.

One of the following:

:user

:assistant

class MessageDeltaEvent { id, delta, object }

Represents a message delta i.e. any changed fields on a message during streaming.

id: String

The identifier of the message, which can be referenced in API endpoints.

delta: [MessageDelta](/api/reference/ruby/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_delta%20%3E%20(schema)) { content, role }

The delta containing the fields that have changed on the Message.

object: :"thread.message.delta"

The object type, which is always `thread.message.delta`.

class RefusalContentBlock { refusal, type }

The refusal content generated by the assistant.

refusal: String

type: :refusal

Always `refusal`.

class RefusalDeltaBlock { index, type, refusal }

The refusal content that is part of a message.

index: Integer

The index of the refusal part in the message.

type: :refusal

Always `refusal`.

refusal: String

class Text { annotations, value }

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

class TextContentBlock { text, type }

The text content that is part of a message.

text: [Text](/api/reference/ruby/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text%20%3E%20(schema)) { annotations, value }

type: :text

Always `text`.

class TextContentBlockParam { text, type }

The text content that is part of a message.

text: String

Text content to be sent to the model

type: :text

Always `text`.

class TextDelta { annotations, value }

annotations: Array[[AnnotationDelta](/api/reference/ruby/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20annotation_delta%20%3E%20(schema))]

One of the following:

class FileCitationDeltaAnnotation { index, type, end\_index, 3 more }

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

index: Integer

The index of the annotation in the text content part.

type: :file\_citation

Always `file_citation`.

end\_index: Integer

minimum0

file\_citation: FileCitation{ file\_id, quote}

file\_id: String

The ID of the specific File the citation is from.

quote: String

The specific quote in the file.

start\_index: Integer

minimum0

text: String

The text in the message content that needs to be replaced.

class FilePathDeltaAnnotation { index, type, end\_index, 3 more }

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

index: Integer

The index of the annotation in the text content part.

type: :file\_path

Always `file_path`.

end\_index: Integer

minimum0

file\_path: FilePath{ file\_id}

file\_id: String

The ID of the file that was generated.

start\_index: Integer

minimum0

text: String

The text in the message content that needs to be replaced.

value: String

The data that makes up the text.

class TextDeltaBlock { index, type, text }

The text content that is part of a message.

index: Integer

The index of the content part in the message.

type: :text

Always `text`.

text: [TextDelta](/api/reference/ruby/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text_delta%20%3E%20(schema)) { annotations, value }
