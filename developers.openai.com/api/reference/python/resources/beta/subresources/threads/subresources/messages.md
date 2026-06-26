<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/threads/subresources/messages/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Beta](/api/reference/python/resources/beta)

[Threads](/api/reference/python/resources/beta/subresources/threads)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Messages

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
