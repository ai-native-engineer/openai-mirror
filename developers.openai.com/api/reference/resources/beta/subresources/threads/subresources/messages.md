<!-- source: https://developers.openai.com/api/reference/resources/beta/subresources/threads/subresources/messages/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Beta](/api/reference/resources/beta)

[Threads](/api/reference/resources/beta/subresources/threads)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Messages

Build Assistants that can call models and use tools.

##### [List messages](/api/reference/resources/beta/subresources/threads/subresources/messages/methods/list)

Deprecated

GET/threads/{thread\_id}/messages

##### [Create message](/api/reference/resources/beta/subresources/threads/subresources/messages/methods/create)

Deprecated

POST/threads/{thread\_id}/messages

##### [Modify message](/api/reference/resources/beta/subresources/threads/subresources/messages/methods/update)

Deprecated

POST/threads/{thread\_id}/messages/{message\_id}

##### [Retrieve message](/api/reference/resources/beta/subresources/threads/subresources/messages/methods/retrieve)

Deprecated

GET/threads/{thread\_id}/messages/{message\_id}

##### [Delete message](/api/reference/resources/beta/subresources/threads/subresources/messages/methods/delete)

Deprecated

DELETE/threads/{thread\_id}/messages/{message\_id}

##### ModelsExpand Collapse

FileCitationAnnotation object { end\_index, file\_citation, start\_index, 2 more }

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

end\_index: number

minimum0

file\_citation: object { file\_id }

file\_id: string

The ID of the specific File the citation is from.

start\_index: number

minimum0

text: string

The text in the message content that needs to be replaced.

type: "file\_citation"

Always `file_citation`.

FileCitationDeltaAnnotation object { index, type, end\_index, 3 more }

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

index: number

The index of the annotation in the text content part.

type: "file\_citation"

Always `file_citation`.

end\_index: optional number

minimum0

file\_citation: optional object { file\_id, quote }

file\_id: optional string

The ID of the specific File the citation is from.

quote: optional string

The specific quote in the file.

start\_index: optional number

minimum0

text: optional string

The text in the message content that needs to be replaced.

FilePathAnnotation object { end\_index, file\_path, start\_index, 2 more }

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

end\_index: number

minimum0

file\_path: object { file\_id }

file\_id: string

The ID of the file that was generated.

start\_index: number

minimum0

text: string

The text in the message content that needs to be replaced.

type: "file\_path"

Always `file_path`.

FilePathDeltaAnnotation object { index, type, end\_index, 3 more }

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

index: number

The index of the annotation in the text content part.

type: "file\_path"

Always `file_path`.

end\_index: optional number

minimum0

file\_path: optional object { file\_id }

file\_id: optional string

The ID of the file that was generated.

start\_index: optional number

minimum0

text: optional string

The text in the message content that needs to be replaced.

ImageFile object { file\_id, detail }

file\_id: string

The [File](/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

detail: optional "auto" or "low" or "high"

Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

One of the following:

"auto"

"low"

"high"

ImageFileContentBlock object { image\_file, type }

References an image [File](/docs/api-reference/files) in the content of a message.

image\_file: [ImageFile](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file%20%3E%20(schema)) { file\_id, detail }

type: "image\_file"

Always `image_file`.

ImageFileDelta object { detail, file\_id }

detail: optional "auto" or "low" or "high"

Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

One of the following:

"auto"

"low"

"high"

file\_id: optional string

The [File](/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

ImageFileDeltaBlock object { index, type, image\_file }

References an image [File](/docs/api-reference/files) in the content of a message.

index: number

The index of the content part in the message.

type: "image\_file"

Always `image_file`.

image\_file: optional [ImageFileDelta](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_delta%20%3E%20(schema)) { detail, file\_id }

ImageURL object { url, detail }

url: string

The external URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

formaturi

detail: optional "auto" or "low" or "high"

Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`. Default value is `auto`

One of the following:

"auto"

"low"

"high"

ImageURLContentBlock object { image\_url, type }

References an image URL in the content of a message.

image\_url: [ImageURL](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url%20%3E%20(schema)) { url, detail }

type: "image\_url"

The type of the content part.

ImageURLDelta object { detail, url }

detail: optional "auto" or "low" or "high"

Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`.

One of the following:

"auto"

"low"

"high"

url: optional string

The URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

formaturi

ImageURLDeltaBlock object { index, type, image\_url }

References an image URL in the content of a message.

index: number

The index of the content part in the message.

type: "image\_url"

Always `image_url`.

image\_url: optional [ImageURLDelta](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_delta%20%3E%20(schema)) { detail, url }

Message object { id, assistant\_id, attachments, 11 more }

Represents a message within a [thread](/docs/api-reference/threads).

id: string

The identifier, which can be referenced in API endpoints.

assistant\_id: string

If applicable, the ID of the [assistant](/docs/api-reference/assistants) that authored this message.

attachments: array of object { file\_id, tools }

A list of files attached to the message, and the tools they were added to.

file\_id: optional string

The ID of the file to attach to the message.

tools: optional array of [CodeInterpreterTool](/api/reference/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20code_interpreter_tool%20%3E%20(schema)) { type }  or object { type }

The tools to add this file to.

One of the following:

CodeInterpreterTool object { type }

type: "code\_interpreter"

The type of tool being defined: `code_interpreter`

FileSearchTool object { type }

type: "file\_search"

The type of tool being defined: `file_search`

completed\_at: number

The Unix timestamp (in seconds) for when the message was completed.

formatunixtime

content: array of [ImageFileContentBlock](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_content_block%20%3E%20(schema)) { image\_file, type }  or [ImageURLContentBlock](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_content_block%20%3E%20(schema)) { image\_url, type }  or [TextContentBlock](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text_content_block%20%3E%20(schema)) { text, type }  or [RefusalContentBlock](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20refusal_content_block%20%3E%20(schema)) { refusal, type }

The content of the message in array of text and/or images.

One of the following:

ImageFileContentBlock object { image\_file, type }

References an image [File](/docs/api-reference/files) in the content of a message.

image\_file: [ImageFile](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file%20%3E%20(schema)) { file\_id, detail }

type: "image\_file"

Always `image_file`.

ImageURLContentBlock object { image\_url, type }

References an image URL in the content of a message.

image\_url: [ImageURL](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url%20%3E%20(schema)) { url, detail }

type: "image\_url"

The type of the content part.

TextContentBlock object { text, type }

The text content that is part of a message.

text: [Text](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text%20%3E%20(schema)) { annotations, value }

type: "text"

Always `text`.

RefusalContentBlock object { refusal, type }

The refusal content generated by the assistant.

refusal: string

type: "refusal"

Always `refusal`.

created\_at: number

The Unix timestamp (in seconds) for when the message was created.

formatunixtime

incomplete\_at: number

The Unix timestamp (in seconds) for when the message was marked as incomplete.

formatunixtime

incomplete\_details: object { reason }

On an incomplete message, details about why the message is incomplete.

reason: "content\_filter" or "max\_tokens" or "run\_cancelled" or 2 more

The reason the message is incomplete.

One of the following:

"content\_filter"

"max\_tokens"

"run\_cancelled"

"run\_expired"

"run\_failed"

metadata: [Metadata](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

object: "thread.message"

The object type, which is always `thread.message`.

role: "user" or "assistant"

The entity that produced the message. One of `user` or `assistant`.

One of the following:

"user"

"assistant"

run\_id: string

The ID of the [run](/docs/api-reference/runs) associated with the creation of this message. Value is `null` when messages are created manually using the create message or create thread endpoints.

status: "in\_progress" or "incomplete" or "completed"

The status of the message, which can be either `in_progress`, `incomplete`, or `completed`.

One of the following:

"in\_progress"

"incomplete"

"completed"

thread\_id: string

The [thread](/docs/api-reference/threads) ID that this message belongs to.

MessageDeleted object { id, deleted, object }

id: string

deleted: boolean

object: "thread.message.deleted"

MessageDelta object { content, role }

The delta containing the fields that have changed on the Message.

content: optional array of [ImageFileDeltaBlock](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_delta_block%20%3E%20(schema)) { index, type, image\_file }  or [TextDeltaBlock](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text_delta_block%20%3E%20(schema)) { index, type, text }  or [RefusalDeltaBlock](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20refusal_delta_block%20%3E%20(schema)) { index, type, refusal }  or [ImageURLDeltaBlock](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_delta_block%20%3E%20(schema)) { index, type, image\_url }

The content of the message in array of text and/or images.

One of the following:

ImageFileDeltaBlock object { index, type, image\_file }

References an image [File](/docs/api-reference/files) in the content of a message.

index: number

The index of the content part in the message.

type: "image\_file"

Always `image_file`.

image\_file: optional [ImageFileDelta](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_delta%20%3E%20(schema)) { detail, file\_id }

TextDeltaBlock object { index, type, text }

The text content that is part of a message.

index: number

The index of the content part in the message.

type: "text"

Always `text`.

text: optional [TextDelta](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text_delta%20%3E%20(schema)) { annotations, value }

RefusalDeltaBlock object { index, type, refusal }

The refusal content that is part of a message.

index: number

The index of the refusal part in the message.

type: "refusal"

Always `refusal`.

refusal: optional string

ImageURLDeltaBlock object { index, type, image\_url }

References an image URL in the content of a message.

index: number

The index of the content part in the message.

type: "image\_url"

Always `image_url`.

image\_url: optional [ImageURLDelta](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_delta%20%3E%20(schema)) { detail, url }

role: optional "user" or "assistant"

The entity that produced the message. One of `user` or `assistant`.

One of the following:

"user"

"assistant"

MessageDeltaEvent object { id, delta, object }

Represents a message delta i.e. any changed fields on a message during streaming.

id: string

The identifier of the message, which can be referenced in API endpoints.

delta: [MessageDelta](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_delta%20%3E%20(schema)) { content, role }

The delta containing the fields that have changed on the Message.

object: "thread.message.delta"

The object type, which is always `thread.message.delta`.

RefusalContentBlock object { refusal, type }

The refusal content generated by the assistant.

refusal: string

type: "refusal"

Always `refusal`.

RefusalDeltaBlock object { index, type, refusal }

The refusal content that is part of a message.

index: number

The index of the refusal part in the message.

type: "refusal"

Always `refusal`.

refusal: optional string

Text object { annotations, value }

annotations: array of [FileCitationAnnotation](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_annotation%20%3E%20(schema)) { end\_index, file\_citation, start\_index, 2 more }  or [FilePathAnnotation](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20file_path_annotation%20%3E%20(schema)) { end\_index, file\_path, start\_index, 2 more }

One of the following:

FileCitationAnnotation object { end\_index, file\_citation, start\_index, 2 more }

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

end\_index: number

minimum0

file\_citation: object { file\_id }

file\_id: string

The ID of the specific File the citation is from.

start\_index: number

minimum0

text: string

The text in the message content that needs to be replaced.

type: "file\_citation"

Always `file_citation`.

FilePathAnnotation object { end\_index, file\_path, start\_index, 2 more }

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

end\_index: number

minimum0

file\_path: object { file\_id }

file\_id: string

The ID of the file that was generated.

start\_index: number

minimum0

text: string

The text in the message content that needs to be replaced.

type: "file\_path"

Always `file_path`.

value: string

The data that makes up the text.

TextContentBlock object { text, type }

The text content that is part of a message.

text: [Text](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text%20%3E%20(schema)) { annotations, value }

type: "text"

Always `text`.

TextContentBlockParam object { text, type }

The text content that is part of a message.

text: string

Text content to be sent to the model

type: "text"

Always `text`.

TextDelta object { annotations, value }

annotations: optional array of [FileCitationDeltaAnnotation](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_delta_annotation%20%3E%20(schema)) { index, type, end\_index, 3 more }  or [FilePathDeltaAnnotation](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20file_path_delta_annotation%20%3E%20(schema)) { index, type, end\_index, 3 more }

One of the following:

FileCitationDeltaAnnotation object { index, type, end\_index, 3 more }

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

index: number

The index of the annotation in the text content part.

type: "file\_citation"

Always `file_citation`.

end\_index: optional number

minimum0

file\_citation: optional object { file\_id, quote }

file\_id: optional string

The ID of the specific File the citation is from.

quote: optional string

The specific quote in the file.

start\_index: optional number

minimum0

text: optional string

The text in the message content that needs to be replaced.

FilePathDeltaAnnotation object { index, type, end\_index, 3 more }

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

index: number

The index of the annotation in the text content part.

type: "file\_path"

Always `file_path`.

end\_index: optional number

minimum0

file\_path: optional object { file\_id }

file\_id: optional string

The ID of the file that was generated.

start\_index: optional number

minimum0

text: optional string

The text in the message content that needs to be replaced.

value: optional string

The data that makes up the text.

TextDeltaBlock object { index, type, text }

The text content that is part of a message.

index: number

The index of the content part in the message.

type: "text"

Always `text`.

text: optional [TextDelta](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text_delta%20%3E%20(schema)) { annotations, value }
