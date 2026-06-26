<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/threads/subresources/messages/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Beta](/api/reference/go/resources/beta)

[Threads](/api/reference/go/resources/beta/subresources/threads)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Messages

Build Assistants that can call models and use tools.

##### [List messages](/api/reference/go/resources/beta/subresources/threads/subresources/messages/methods/list)

Deprecated

client.Beta.Threads.Messages.List(ctx, threadID, query) (\*CursorPage[[Message](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema))], error)

GET/threads/{thread\_id}/messages

##### [Create message](/api/reference/go/resources/beta/subresources/threads/subresources/messages/methods/create)

Deprecated

client.Beta.Threads.Messages.New(ctx, threadID, body) (\*[Message](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)), error)

POST/threads/{thread\_id}/messages

##### [Modify message](/api/reference/go/resources/beta/subresources/threads/subresources/messages/methods/update)

Deprecated

client.Beta.Threads.Messages.Update(ctx, threadID, messageID, body) (\*[Message](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)), error)

POST/threads/{thread\_id}/messages/{message\_id}

##### [Retrieve message](/api/reference/go/resources/beta/subresources/threads/subresources/messages/methods/retrieve)

Deprecated

client.Beta.Threads.Messages.Get(ctx, threadID, messageID) (\*[Message](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)), error)

GET/threads/{thread\_id}/messages/{message\_id}

##### [Delete message](/api/reference/go/resources/beta/subresources/threads/subresources/messages/methods/delete)

Deprecated

client.Beta.Threads.Messages.Delete(ctx, threadID, messageID) (\*[MessageDeleted](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_deleted%20%3E%20(schema)), error)

DELETE/threads/{thread\_id}/messages/{message\_id}

##### ModelsExpand Collapse

type AnnotationUnion interface{…}

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

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

type AnnotationDeltaUnion interface{…}

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

One of the following:

type FileCitationDeltaAnnotation struct{…}

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

Index int64

The index of the annotation in the text content part.

Type FileCitation

Always `file_citation`.

EndIndex int64Optional

minimum0

FileCitation FileCitationDeltaAnnotationFileCitationOptional

FileID stringOptional

The ID of the specific File the citation is from.

Quote stringOptional

The specific quote in the file.

StartIndex int64Optional

minimum0

Text stringOptional

The text in the message content that needs to be replaced.

type FilePathDeltaAnnotation struct{…}

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

Index int64

The index of the annotation in the text content part.

Type FilePath

Always `file_path`.

EndIndex int64Optional

minimum0

FilePath FilePathDeltaAnnotationFilePathOptional

FileID stringOptional

The ID of the file that was generated.

StartIndex int64Optional

minimum0

Text stringOptional

The text in the message content that needs to be replaced.

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

type FileCitationDeltaAnnotation struct{…}

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

Index int64

The index of the annotation in the text content part.

Type FileCitation

Always `file_citation`.

EndIndex int64Optional

minimum0

FileCitation FileCitationDeltaAnnotationFileCitationOptional

FileID stringOptional

The ID of the specific File the citation is from.

Quote stringOptional

The specific quote in the file.

StartIndex int64Optional

minimum0

Text stringOptional

The text in the message content that needs to be replaced.

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

type FilePathDeltaAnnotation struct{…}

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

Index int64

The index of the annotation in the text content part.

Type FilePath

Always `file_path`.

EndIndex int64Optional

minimum0

FilePath FilePathDeltaAnnotationFilePathOptional

FileID stringOptional

The ID of the file that was generated.

StartIndex int64Optional

minimum0

Text stringOptional

The text in the message content that needs to be replaced.

type ImageFile struct{…}

FileID string

The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

Detail ImageFileDetailOptional

Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

One of the following:

const ImageFileDetailAuto ImageFileDetail = "auto"

const ImageFileDetailLow ImageFileDetail = "low"

const ImageFileDetailHigh ImageFileDetail = "high"

type ImageFileContentBlock struct{…}

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

ImageFile [ImageFile](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file%20%3E%20(schema))

Type ImageFile

Always `image_file`.

type ImageFileDelta struct{…}

Detail ImageFileDeltaDetailOptional

Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

One of the following:

const ImageFileDeltaDetailAuto ImageFileDeltaDetail = "auto"

const ImageFileDeltaDetailLow ImageFileDeltaDetail = "low"

const ImageFileDeltaDetailHigh ImageFileDeltaDetail = "high"

FileID stringOptional

The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

type ImageFileDeltaBlock struct{…}

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

Index int64

The index of the content part in the message.

Type ImageFile

Always `image_file`.

ImageFile [ImageFileDelta](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_delta%20%3E%20(schema))Optional

type ImageURL struct{…}

URL string

The external URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

formaturi

Detail ImageURLDetailOptional

Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`. Default value is `auto`

One of the following:

const ImageURLDetailAuto ImageURLDetail = "auto"

const ImageURLDetailLow ImageURLDetail = "low"

const ImageURLDetailHigh ImageURLDetail = "high"

type ImageURLContentBlock struct{…}

References an image URL in the content of a message.

ImageURL [ImageURL](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url%20%3E%20(schema))

Type ImageURL

The type of the content part.

type ImageURLDelta struct{…}

Detail ImageURLDeltaDetailOptional

Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`.

One of the following:

const ImageURLDeltaDetailAuto ImageURLDeltaDetail = "auto"

const ImageURLDeltaDetailLow ImageURLDeltaDetail = "low"

const ImageURLDeltaDetailHigh ImageURLDeltaDetail = "high"

URL stringOptional

The URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

formaturi

type ImageURLDeltaBlock struct{…}

References an image URL in the content of a message.

Index int64

The index of the content part in the message.

Type ImageURL

Always `image_url`.

ImageURL [ImageURLDelta](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_delta%20%3E%20(schema))Optional

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

Type ImageFile

Always `image_file`.

type ImageURLContentBlock struct{…}

References an image URL in the content of a message.

ImageURL [ImageURL](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url%20%3E%20(schema))

Type ImageURL

The type of the content part.

type TextContentBlock struct{…}

The text content that is part of a message.

Text [Text](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text%20%3E%20(schema))

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

type MessageContentUnion interface{…}

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

One of the following:

type ImageFileContentBlock struct{…}

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

ImageFile [ImageFile](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file%20%3E%20(schema))

Type ImageFile

Always `image_file`.

type ImageURLContentBlock struct{…}

References an image URL in the content of a message.

ImageURL [ImageURL](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url%20%3E%20(schema))

Type ImageURL

The type of the content part.

type TextContentBlock struct{…}

The text content that is part of a message.

Text [Text](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text%20%3E%20(schema))

Type Text

Always `text`.

type RefusalContentBlock struct{…}

The refusal content generated by the assistant.

Refusal string

Type Refusal

Always `refusal`.

type MessageContentDeltaUnion interface{…}

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

One of the following:

type ImageFileDeltaBlock struct{…}

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

Index int64

The index of the content part in the message.

Type ImageFile

Always `image_file`.

ImageFile [ImageFileDelta](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_delta%20%3E%20(schema))Optional

type TextDeltaBlock struct{…}

The text content that is part of a message.

Index int64

The index of the content part in the message.

Type Text

Always `text`.

Text [TextDelta](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text_delta%20%3E%20(schema))Optional

type RefusalDeltaBlock struct{…}

The refusal content that is part of a message.

Index int64

The index of the refusal part in the message.

Type Refusal

Always `refusal`.

Refusal stringOptional

type ImageURLDeltaBlock struct{…}

References an image URL in the content of a message.

Index int64

The index of the content part in the message.

Type ImageURL

Always `image_url`.

ImageURL [ImageURLDelta](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_delta%20%3E%20(schema))Optional

type MessageContentPartParamUnionResp interface{…}

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

One of the following:

type ImageFileContentBlock struct{…}

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

ImageFile [ImageFile](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file%20%3E%20(schema))

Type ImageFile

Always `image_file`.

type ImageURLContentBlock struct{…}

References an image URL in the content of a message.

ImageURL [ImageURL](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url%20%3E%20(schema))

Type ImageURL

The type of the content part.

type TextContentBlockParam struct{…}

The text content that is part of a message.

Text string

Text content to be sent to the model

Type Text

Always `text`.

type MessageDeleted struct{…}

ID string

Deleted bool

Object ThreadMessageDeleted

type MessageDelta struct{…}

The delta containing the fields that have changed on the Message.

Content [][MessageContentDeltaUnion](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_content_delta%20%3E%20(schema))Optional

The content of the message in array of text and/or images.

One of the following:

type ImageFileDeltaBlock struct{…}

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

Index int64

The index of the content part in the message.

Type ImageFile

Always `image_file`.

ImageFile [ImageFileDelta](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_delta%20%3E%20(schema))Optional

type TextDeltaBlock struct{…}

The text content that is part of a message.

Index int64

The index of the content part in the message.

Type Text

Always `text`.

Text [TextDelta](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text_delta%20%3E%20(schema))Optional

type RefusalDeltaBlock struct{…}

The refusal content that is part of a message.

Index int64

The index of the refusal part in the message.

Type Refusal

Always `refusal`.

Refusal stringOptional

type ImageURLDeltaBlock struct{…}

References an image URL in the content of a message.

Index int64

The index of the content part in the message.

Type ImageURL

Always `image_url`.

ImageURL [ImageURLDelta](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_delta%20%3E%20(schema))Optional

Role MessageDeltaRoleOptional

The entity that produced the message. One of `user` or `assistant`.

One of the following:

const MessageDeltaRoleUser MessageDeltaRole = "user"

const MessageDeltaRoleAssistant MessageDeltaRole = "assistant"

type MessageDeltaEvent struct{…}

Represents a message delta i.e. any changed fields on a message during streaming.

ID string

The identifier of the message, which can be referenced in API endpoints.

Delta [MessageDelta](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_delta%20%3E%20(schema))

The delta containing the fields that have changed on the Message.

Object ThreadMessageDelta

The object type, which is always `thread.message.delta`.

type RefusalContentBlock struct{…}

The refusal content generated by the assistant.

Refusal string

Type Refusal

Always `refusal`.

type RefusalDeltaBlock struct{…}

The refusal content that is part of a message.

Index int64

The index of the refusal part in the message.

Type Refusal

Always `refusal`.

Refusal stringOptional

type Text struct{…}

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

type TextContentBlock struct{…}

The text content that is part of a message.

Text [Text](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text%20%3E%20(schema))

Type Text

Always `text`.

type TextContentBlockParam struct{…}

The text content that is part of a message.

Text string

Text content to be sent to the model

Type Text

Always `text`.

type TextDelta struct{…}

Annotations [][AnnotationDeltaUnion](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20annotation_delta%20%3E%20(schema))Optional

One of the following:

type FileCitationDeltaAnnotation struct{…}

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

Index int64

The index of the annotation in the text content part.

Type FileCitation

Always `file_citation`.

EndIndex int64Optional

minimum0

FileCitation FileCitationDeltaAnnotationFileCitationOptional

FileID stringOptional

The ID of the specific File the citation is from.

Quote stringOptional

The specific quote in the file.

StartIndex int64Optional

minimum0

Text stringOptional

The text in the message content that needs to be replaced.

type FilePathDeltaAnnotation struct{…}

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

Index int64

The index of the annotation in the text content part.

Type FilePath

Always `file_path`.

EndIndex int64Optional

minimum0

FilePath FilePathDeltaAnnotationFilePathOptional

FileID stringOptional

The ID of the file that was generated.

StartIndex int64Optional

minimum0

Text stringOptional

The text in the message content that needs to be replaced.

Value stringOptional

The data that makes up the text.

type TextDeltaBlock struct{…}

The text content that is part of a message.

Index int64

The index of the content part in the message.

Type Text

Always `text`.

Text [TextDelta](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text_delta%20%3E%20(schema))Optional
