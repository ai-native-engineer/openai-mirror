<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/threads/subresources/messages/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Beta](/api/reference/java/resources/beta)

[Threads](/api/reference/java/resources/beta/subresources/threads)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Messages

Build Assistants that can call models and use tools.

##### [List messages](/api/reference/java/resources/beta/subresources/threads/subresources/messages/methods/list)

Deprecated

MessageListPage beta().threads().messages().list(MessageListParamsparams = MessageListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/threads/{thread\_id}/messages

##### [Create message](/api/reference/java/resources/beta/subresources/threads/subresources/messages/methods/create)

Deprecated

[Message](/api/reference/java/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)) beta().threads().messages().create(MessageCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/threads/{thread\_id}/messages

##### [Modify message](/api/reference/java/resources/beta/subresources/threads/subresources/messages/methods/update)

Deprecated

[Message](/api/reference/java/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)) beta().threads().messages().update(MessageUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/threads/{thread\_id}/messages/{message\_id}

##### [Retrieve message](/api/reference/java/resources/beta/subresources/threads/subresources/messages/methods/retrieve)

Deprecated

[Message](/api/reference/java/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)) beta().threads().messages().retrieve(MessageRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/threads/{thread\_id}/messages/{message\_id}

##### [Delete message](/api/reference/java/resources/beta/subresources/threads/subresources/messages/methods/delete)

Deprecated

[MessageDeleted](/api/reference/java/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_deleted%20%3E%20(schema)) beta().threads().messages().delete(MessageDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

DELETE/threads/{thread\_id}/messages/{message\_id}

##### ModelsExpand Collapse

class Annotation: A class that can be one of several variants.union

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

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

class AnnotationDelta: A class that can be one of several variants.union

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

class FileCitationDeltaAnnotation:

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

long index

The index of the annotation in the text content part.

JsonValue; type "file\_citation"constant"file\_citation"constant

Always `file_citation`.

Optional<Long> endIndex

minimum0

Optional<FileCitation> fileCitation

Optional<String> fileId

The ID of the specific File the citation is from.

Optional<String> quote

The specific quote in the file.

Optional<Long> startIndex

minimum0

Optional<String> text

The text in the message content that needs to be replaced.

class FilePathDeltaAnnotation:

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

long index

The index of the annotation in the text content part.

JsonValue; type "file\_path"constant"file\_path"constant

Always `file_path`.

Optional<Long> endIndex

minimum0

Optional<FilePath> filePath

Optional<String> fileId

The ID of the file that was generated.

Optional<Long> startIndex

minimum0

Optional<String> text

The text in the message content that needs to be replaced.

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

class FileCitationDeltaAnnotation:

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

long index

The index of the annotation in the text content part.

JsonValue; type "file\_citation"constant"file\_citation"constant

Always `file_citation`.

Optional<Long> endIndex

minimum0

Optional<FileCitation> fileCitation

Optional<String> fileId

The ID of the specific File the citation is from.

Optional<String> quote

The specific quote in the file.

Optional<Long> startIndex

minimum0

Optional<String> text

The text in the message content that needs to be replaced.

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

class FilePathDeltaAnnotation:

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

long index

The index of the annotation in the text content part.

JsonValue; type "file\_path"constant"file\_path"constant

Always `file_path`.

Optional<Long> endIndex

minimum0

Optional<FilePath> filePath

Optional<String> fileId

The ID of the file that was generated.

Optional<Long> startIndex

minimum0

Optional<String> text

The text in the message content that needs to be replaced.

class ImageFile:

String fileId

The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

Optional<Detail> detail

Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

One of the following:

AUTO("auto")

LOW("low")

HIGH("high")

class ImageFileContentBlock:

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

[ImageFile](/api/reference/java/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file%20%3E%20(schema)) imageFile

JsonValue; type "image\_file"constant"image\_file"constant

Always `image_file`.

class ImageFileDelta:

Optional<Detail> detail

Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

One of the following:

AUTO("auto")

LOW("low")

HIGH("high")

Optional<String> fileId

The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

class ImageFileDeltaBlock:

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

long index

The index of the content part in the message.

JsonValue; type "image\_file"constant"image\_file"constant

Always `image_file`.

Optional<[ImageFileDelta](/api/reference/java/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_delta%20%3E%20(schema))> imageFile

class ImageUrl:

String url

The external URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

formaturi

Optional<Detail> detail

Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`. Default value is `auto`

One of the following:

AUTO("auto")

LOW("low")

HIGH("high")

class ImageUrlContentBlock:

References an image URL in the content of a message.

[ImageUrl](/api/reference/java/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url%20%3E%20(schema)) imageUrl

JsonValue; type "image\_url"constant"image\_url"constant

The type of the content part.

class ImageUrlDelta:

Optional<Detail> detail

Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`.

One of the following:

AUTO("auto")

LOW("low")

HIGH("high")

Optional<String> url

The URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

formaturi

class ImageUrlDeltaBlock:

References an image URL in the content of a message.

long index

The index of the content part in the message.

JsonValue; type "image\_url"constant"image\_url"constant

Always `image_url`.

Optional<[ImageUrlDelta](/api/reference/java/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_delta%20%3E%20(schema))> imageUrl

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

JsonValue; type "image\_file"constant"image\_file"constant

Always `image_file`.

class ImageUrlContentBlock:

References an image URL in the content of a message.

[ImageUrl](/api/reference/java/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url%20%3E%20(schema)) imageUrl

JsonValue; type "image\_url"constant"image\_url"constant

The type of the content part.

class TextContentBlock:

The text content that is part of a message.

[Text](/api/reference/java/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text%20%3E%20(schema)) text

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

class MessageContent: A class that can be one of several variants.union

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

class ImageFileContentBlock:

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

[ImageFile](/api/reference/java/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file%20%3E%20(schema)) imageFile

JsonValue; type "image\_file"constant"image\_file"constant

Always `image_file`.

class ImageUrlContentBlock:

References an image URL in the content of a message.

[ImageUrl](/api/reference/java/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url%20%3E%20(schema)) imageUrl

JsonValue; type "image\_url"constant"image\_url"constant

The type of the content part.

class TextContentBlock:

The text content that is part of a message.

[Text](/api/reference/java/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text%20%3E%20(schema)) text

JsonValue; type "text"constant"text"constant

Always `text`.

class RefusalContentBlock:

The refusal content generated by the assistant.

String refusal

JsonValue; type "refusal"constant"refusal"constant

Always `refusal`.

class MessageContentDelta: A class that can be one of several variants.union

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

class ImageFileDeltaBlock:

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

long index

The index of the content part in the message.

JsonValue; type "image\_file"constant"image\_file"constant

Always `image_file`.

Optional<[ImageFileDelta](/api/reference/java/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_delta%20%3E%20(schema))> imageFile

class TextDeltaBlock:

The text content that is part of a message.

long index

The index of the content part in the message.

JsonValue; type "text"constant"text"constant

Always `text`.

Optional<[TextDelta](/api/reference/java/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text_delta%20%3E%20(schema))> text

class RefusalDeltaBlock:

The refusal content that is part of a message.

long index

The index of the refusal part in the message.

JsonValue; type "refusal"constant"refusal"constant

Always `refusal`.

Optional<String> refusal

class ImageUrlDeltaBlock:

References an image URL in the content of a message.

long index

The index of the content part in the message.

JsonValue; type "image\_url"constant"image\_url"constant

Always `image_url`.

Optional<[ImageUrlDelta](/api/reference/java/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_delta%20%3E%20(schema))> imageUrl

class MessageContentPartParam: A class that can be one of several variants.union

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

class ImageFileContentBlock:

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

[ImageFile](/api/reference/java/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file%20%3E%20(schema)) imageFile

JsonValue; type "image\_file"constant"image\_file"constant

Always `image_file`.

class ImageUrlContentBlock:

References an image URL in the content of a message.

[ImageUrl](/api/reference/java/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url%20%3E%20(schema)) imageUrl

JsonValue; type "image\_url"constant"image\_url"constant

The type of the content part.

class TextContentBlockParam:

The text content that is part of a message.

String text

Text content to be sent to the model

JsonValue; type "text"constant"text"constant

Always `text`.

class MessageDeleted:

String id

boolean deleted

JsonValue; object\_ "thread.message.deleted"constant"thread.message.deleted"constant

class MessageDelta:

The delta containing the fields that have changed on the Message.

Optional<List<[MessageContentDelta](/api/reference/java/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_content_delta%20%3E%20(schema))>> content

The content of the message in array of text and/or images.

One of the following:

class ImageFileDeltaBlock:

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

long index

The index of the content part in the message.

JsonValue; type "image\_file"constant"image\_file"constant

Always `image_file`.

Optional<[ImageFileDelta](/api/reference/java/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_delta%20%3E%20(schema))> imageFile

class TextDeltaBlock:

The text content that is part of a message.

long index

The index of the content part in the message.

JsonValue; type "text"constant"text"constant

Always `text`.

Optional<[TextDelta](/api/reference/java/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text_delta%20%3E%20(schema))> text

class RefusalDeltaBlock:

The refusal content that is part of a message.

long index

The index of the refusal part in the message.

JsonValue; type "refusal"constant"refusal"constant

Always `refusal`.

Optional<String> refusal

class ImageUrlDeltaBlock:

References an image URL in the content of a message.

long index

The index of the content part in the message.

JsonValue; type "image\_url"constant"image\_url"constant

Always `image_url`.

Optional<[ImageUrlDelta](/api/reference/java/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_delta%20%3E%20(schema))> imageUrl

Optional<Role> role

The entity that produced the message. One of `user` or `assistant`.

One of the following:

USER("user")

ASSISTANT("assistant")

class MessageDeltaEvent:

Represents a message delta i.e. any changed fields on a message during streaming.

String id

The identifier of the message, which can be referenced in API endpoints.

[MessageDelta](/api/reference/java/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_delta%20%3E%20(schema)) delta

The delta containing the fields that have changed on the Message.

JsonValue; object\_ "thread.message.delta"constant"thread.message.delta"constant

The object type, which is always `thread.message.delta`.

class RefusalContentBlock:

The refusal content generated by the assistant.

String refusal

JsonValue; type "refusal"constant"refusal"constant

Always `refusal`.

class RefusalDeltaBlock:

The refusal content that is part of a message.

long index

The index of the refusal part in the message.

JsonValue; type "refusal"constant"refusal"constant

Always `refusal`.

Optional<String> refusal

class Text:

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

class TextContentBlock:

The text content that is part of a message.

[Text](/api/reference/java/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text%20%3E%20(schema)) text

JsonValue; type "text"constant"text"constant

Always `text`.

class TextContentBlockParam:

The text content that is part of a message.

String text

Text content to be sent to the model

JsonValue; type "text"constant"text"constant

Always `text`.

class TextDelta:

Optional<List<[AnnotationDelta](/api/reference/java/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20annotation_delta%20%3E%20(schema))>> annotations

One of the following:

class FileCitationDeltaAnnotation:

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

long index

The index of the annotation in the text content part.

JsonValue; type "file\_citation"constant"file\_citation"constant

Always `file_citation`.

Optional<Long> endIndex

minimum0

Optional<FileCitation> fileCitation

Optional<String> fileId

The ID of the specific File the citation is from.

Optional<String> quote

The specific quote in the file.

Optional<Long> startIndex

minimum0

Optional<String> text

The text in the message content that needs to be replaced.

class FilePathDeltaAnnotation:

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

long index

The index of the annotation in the text content part.

JsonValue; type "file\_path"constant"file\_path"constant

Always `file_path`.

Optional<Long> endIndex

minimum0

Optional<FilePath> filePath

Optional<String> fileId

The ID of the file that was generated.

Optional<Long> startIndex

minimum0

Optional<String> text

The text in the message content that needs to be replaced.

Optional<String> value

The data that makes up the text.

class TextDeltaBlock:

The text content that is part of a message.

long index

The index of the content part in the message.

JsonValue; type "text"constant"text"constant

Always `text`.

Optional<[TextDelta](/api/reference/java/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text_delta%20%3E%20(schema))> text
