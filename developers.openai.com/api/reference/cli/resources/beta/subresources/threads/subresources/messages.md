<!-- source: https://developers.openai.com/api/reference/cli/resources/beta/subresources/threads/subresources/messages/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Beta](/api/reference/cli/resources/beta)

[Threads](/api/reference/cli/resources/beta/subresources/threads)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Messages

Build Assistants that can call models and use tools.

##### [List messages](/api/reference/cli/resources/beta/subresources/threads/subresources/messages/methods/list)

Deprecated

$ openai beta:threads:messages list

GET/threads/{thread\_id}/messages

##### [Create message](/api/reference/cli/resources/beta/subresources/threads/subresources/messages/methods/create)

Deprecated

$ openai beta:threads:messages create

POST/threads/{thread\_id}/messages

##### [Modify message](/api/reference/cli/resources/beta/subresources/threads/subresources/messages/methods/update)

Deprecated

$ openai beta:threads:messages update

POST/threads/{thread\_id}/messages/{message\_id}

##### [Retrieve message](/api/reference/cli/resources/beta/subresources/threads/subresources/messages/methods/retrieve)

Deprecated

$ openai beta:threads:messages retrieve

GET/threads/{thread\_id}/messages/{message\_id}

##### [Delete message](/api/reference/cli/resources/beta/subresources/threads/subresources/messages/methods/delete)

Deprecated

$ openai beta:threads:messages delete

DELETE/threads/{thread\_id}/messages/{message\_id}

##### ModelsExpand Collapse

annotation: [FileCitationAnnotation](/api/reference/cli/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_annotation%20%3E%20(schema)) { end\_index, file\_citation, start\_index, 2 more }  or [FilePathAnnotation](/api/reference/cli/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20file_path_annotation%20%3E%20(schema)) { end\_index, file\_path, start\_index, 2 more }

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

file\_citation\_annotation: object { end\_index, file\_citation, start\_index, 2 more }

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

end\_index: number

file\_citation: object { file\_id }

file\_id: string

The ID of the specific File the citation is from.

start\_index: number

text: string

The text in the message content that needs to be replaced.

type: "file\_citation"

Always `file_citation`.

file\_path\_annotation: object { end\_index, file\_path, start\_index, 2 more }

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

end\_index: number

file\_path: object { file\_id }

file\_id: string

The ID of the file that was generated.

start\_index: number

text: string

The text in the message content that needs to be replaced.

type: "file\_path"

Always `file_path`.

annotation\_delta: [FileCitationDeltaAnnotation](/api/reference/cli/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_delta_annotation%20%3E%20(schema)) { index, type, end\_index, 3 more }  or [FilePathDeltaAnnotation](/api/reference/cli/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20file_path_delta_annotation%20%3E%20(schema)) { index, type, end\_index, 3 more }

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

file\_citation\_delta\_annotation: object { index, type, end\_index, 3 more }

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

index: number

The index of the annotation in the text content part.

type: "file\_citation"

Always `file_citation`.

end\_index: optional number

file\_citation: optional object { file\_id, quote }

file\_id: optional string

The ID of the specific File the citation is from.

quote: optional string

The specific quote in the file.

start\_index: optional number

text: optional string

The text in the message content that needs to be replaced.

file\_path\_delta\_annotation: object { index, type, end\_index, 3 more }

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

index: number

The index of the annotation in the text content part.

type: "file\_path"

Always `file_path`.

end\_index: optional number

file\_path: optional object { file\_id }

file\_id: optional string

The ID of the file that was generated.

start\_index: optional number

text: optional string

The text in the message content that needs to be replaced.

file\_citation\_annotation: object { end\_index, file\_citation, start\_index, 2 more }

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

end\_index: number

file\_citation: object { file\_id }

file\_id: string

The ID of the specific File the citation is from.

start\_index: number

text: string

The text in the message content that needs to be replaced.

type: "file\_citation"

Always `file_citation`.

file\_citation\_delta\_annotation: object { index, type, end\_index, 3 more }

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

index: number

The index of the annotation in the text content part.

type: "file\_citation"

Always `file_citation`.

end\_index: optional number

file\_citation: optional object { file\_id, quote }

file\_id: optional string

The ID of the specific File the citation is from.

quote: optional string

The specific quote in the file.

start\_index: optional number

text: optional string

The text in the message content that needs to be replaced.

file\_path\_annotation: object { end\_index, file\_path, start\_index, 2 more }

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

end\_index: number

file\_path: object { file\_id }

file\_id: string

The ID of the file that was generated.

start\_index: number

text: string

The text in the message content that needs to be replaced.

type: "file\_path"

Always `file_path`.

file\_path\_delta\_annotation: object { index, type, end\_index, 3 more }

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

index: number

The index of the annotation in the text content part.

type: "file\_path"

Always `file_path`.

end\_index: optional number

file\_path: optional object { file\_id }

file\_id: optional string

The ID of the file that was generated.

start\_index: optional number

text: optional string

The text in the message content that needs to be replaced.

image\_file: object { file\_id, detail }

file\_id: string

The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

detail: optional "auto" or "low" or "high"

Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

"auto"

"low"

"high"

image\_file\_content\_block: object { image\_file, type }

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

image\_file: object { file\_id, detail }

file\_id: string

The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

detail: optional "auto" or "low" or "high"

Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

"auto"

"low"

"high"

type: "image\_file"

Always `image_file`.

image\_file\_delta: object { detail, file\_id }

detail: optional "auto" or "low" or "high"

Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

"auto"

"low"

"high"

file\_id: optional string

The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

image\_file\_delta\_block: object { index, type, image\_file }

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

index: number

The index of the content part in the message.

type: "image\_file"

Always `image_file`.

image\_file: optional object { detail, file\_id }

detail: optional "auto" or "low" or "high"

Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

"auto"

"low"

"high"

file\_id: optional string

The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

image\_url: object { url, detail }

url: string

The external URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

detail: optional "auto" or "low" or "high"

Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`. Default value is `auto`

"auto"

"low"

"high"

image\_url\_content\_block: object { image\_url, type }

References an image URL in the content of a message.

image\_url: object { url, detail }

url: string

The external URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

detail: optional "auto" or "low" or "high"

Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`. Default value is `auto`

"auto"

"low"

"high"

type: "image\_url"

The type of the content part.

image\_url\_delta: object { detail, url }

detail: optional "auto" or "low" or "high"

Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`.

"auto"

"low"

"high"

url: optional string

The URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

image\_url\_delta\_block: object { index, type, image\_url }

References an image URL in the content of a message.

index: number

The index of the content part in the message.

type: "image\_url"

Always `image_url`.

image\_url: optional object { detail, url }

detail: optional "auto" or "low" or "high"

Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`.

"auto"

"low"

"high"

url: optional string

The URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

message: object { id, assistant\_id, attachments, 11 more }

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

id: string

The identifier, which can be referenced in API endpoints.

assistant\_id: string

If applicable, the ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) that authored this message.

attachments: array of object { file\_id, tools }

A list of files attached to the message, and the tools they were added to.

file\_id: optional string

The ID of the file to attach to the message.

tools: optional array of [CodeInterpreterTool](/api/reference/cli/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20code_interpreter_tool%20%3E%20(schema)) { type }  or object { type }

The tools to add this file to.

code\_interpreter\_tool: object { type }

type: "code\_interpreter"

The type of tool being defined: `code_interpreter`

AssistantToolsFileSearchTypeOnly: object { type }

completed\_at: number

The Unix timestamp (in seconds) for when the message was completed.

content: array of [MessageContent](/api/reference/cli/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_content%20%3E%20(schema))

The content of the message in array of text and/or images.

image\_file\_content\_block: object { image\_file, type }

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

image\_file: object { file\_id, detail }

file\_id: string

The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

detail: optional "auto" or "low" or "high"

Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

"auto"

"low"

"high"

type: "image\_file"

Always `image_file`.

image\_url\_content\_block: object { image\_url, type }

References an image URL in the content of a message.

image\_url: object { url, detail }

url: string

The external URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

detail: optional "auto" or "low" or "high"

Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`. Default value is `auto`

"auto"

"low"

"high"

type: "image\_url"

The type of the content part.

text\_content\_block: object { text, type }

The text content that is part of a message.

text: object { annotations, value }

annotations: array of [Annotation](/api/reference/cli/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20annotation%20%3E%20(schema))

file\_citation\_annotation: object { end\_index, file\_citation, start\_index, 2 more }

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

end\_index: number

file\_citation: object { file\_id }

file\_id: string

The ID of the specific File the citation is from.

start\_index: number

text: string

The text in the message content that needs to be replaced.

type: "file\_citation"

Always `file_citation`.

file\_path\_annotation: object { end\_index, file\_path, start\_index, 2 more }

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

end\_index: number

file\_path: object { file\_id }

file\_id: string

The ID of the file that was generated.

start\_index: number

text: string

The text in the message content that needs to be replaced.

type: "file\_path"

Always `file_path`.

value: string

The data that makes up the text.

type: "text"

Always `text`.

refusal\_content\_block: object { refusal, type }

The refusal content generated by the assistant.

refusal: string

type: "refusal"

Always `refusal`.

created\_at: number

The Unix timestamp (in seconds) for when the message was created.

incomplete\_at: number

The Unix timestamp (in seconds) for when the message was marked as incomplete.

incomplete\_details: object { reason }

On an incomplete message, details about why the message is incomplete.

reason: "content\_filter" or "max\_tokens" or "run\_cancelled" or 2 more

The reason the message is incomplete.

"content\_filter"

"max\_tokens"

"run\_cancelled"

"run\_expired"

"run\_failed"

metadata: map[string]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

object: "thread.message"

The object type, which is always `thread.message`.

role: "user" or "assistant"

The entity that produced the message. One of `user` or `assistant`.

"user"

"assistant"

run\_id: string

The ID of the [run](https://platform.openai.com/docs/api-reference/runs) associated with the creation of this message. Value is `null` when messages are created manually using the create message or create thread endpoints.

status: "in\_progress" or "incomplete" or "completed"

The status of the message, which can be either `in_progress`, `incomplete`, or `completed`.

"in\_progress"

"incomplete"

"completed"

thread\_id: string

The [thread](https://platform.openai.com/docs/api-reference/threads) ID that this message belongs to.

message\_content: [ImageFileContentBlock](/api/reference/cli/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_content_block%20%3E%20(schema)) { image\_file, type }  or [ImageURLContentBlock](/api/reference/cli/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_content_block%20%3E%20(schema)) { image\_url, type }  or [TextContentBlock](/api/reference/cli/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text_content_block%20%3E%20(schema)) { text, type }  or [RefusalContentBlock](/api/reference/cli/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20refusal_content_block%20%3E%20(schema)) { refusal, type }

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

image\_file\_content\_block: object { image\_file, type }

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

image\_file: object { file\_id, detail }

file\_id: string

The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

detail: optional "auto" or "low" or "high"

Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

"auto"

"low"

"high"

type: "image\_file"

Always `image_file`.

image\_url\_content\_block: object { image\_url, type }

References an image URL in the content of a message.

image\_url: object { url, detail }

url: string

The external URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

detail: optional "auto" or "low" or "high"

Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`. Default value is `auto`

"auto"

"low"

"high"

type: "image\_url"

The type of the content part.

text\_content\_block: object { text, type }

The text content that is part of a message.

text: object { annotations, value }

annotations: array of [Annotation](/api/reference/cli/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20annotation%20%3E%20(schema))

file\_citation\_annotation: object { end\_index, file\_citation, start\_index, 2 more }

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

end\_index: number

file\_citation: object { file\_id }

file\_id: string

The ID of the specific File the citation is from.

start\_index: number

text: string

The text in the message content that needs to be replaced.

type: "file\_citation"

Always `file_citation`.

file\_path\_annotation: object { end\_index, file\_path, start\_index, 2 more }

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

end\_index: number

file\_path: object { file\_id }

file\_id: string

The ID of the file that was generated.

start\_index: number

text: string

The text in the message content that needs to be replaced.

type: "file\_path"

Always `file_path`.

value: string

The data that makes up the text.

type: "text"

Always `text`.

refusal\_content\_block: object { refusal, type }

The refusal content generated by the assistant.

refusal: string

type: "refusal"

Always `refusal`.

message\_content\_delta: [ImageFileDeltaBlock](/api/reference/cli/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_delta_block%20%3E%20(schema)) { index, type, image\_file }  or [TextDeltaBlock](/api/reference/cli/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text_delta_block%20%3E%20(schema)) { index, type, text }  or [RefusalDeltaBlock](/api/reference/cli/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20refusal_delta_block%20%3E%20(schema)) { index, type, refusal }  or [ImageURLDeltaBlock](/api/reference/cli/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_delta_block%20%3E%20(schema)) { index, type, image\_url }

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

image\_file\_delta\_block: object { index, type, image\_file }

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

index: number

The index of the content part in the message.

type: "image\_file"

Always `image_file`.

image\_file: optional object { detail, file\_id }

detail: optional "auto" or "low" or "high"

Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

"auto"

"low"

"high"

file\_id: optional string

The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

text\_delta\_block: object { index, type, text }

The text content that is part of a message.

index: number

The index of the content part in the message.

type: "text"

Always `text`.

text: optional object { annotations, value }

annotations: optional array of [AnnotationDelta](/api/reference/cli/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20annotation_delta%20%3E%20(schema))

file\_citation\_delta\_annotation: object { index, type, end\_index, 3 more }

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

index: number

The index of the annotation in the text content part.

type: "file\_citation"

Always `file_citation`.

end\_index: optional number

file\_citation: optional object { file\_id, quote }

file\_id: optional string

The ID of the specific File the citation is from.

quote: optional string

The specific quote in the file.

start\_index: optional number

text: optional string

The text in the message content that needs to be replaced.

file\_path\_delta\_annotation: object { index, type, end\_index, 3 more }

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

index: number

The index of the annotation in the text content part.

type: "file\_path"

Always `file_path`.

end\_index: optional number

file\_path: optional object { file\_id }

file\_id: optional string

The ID of the file that was generated.

start\_index: optional number

text: optional string

The text in the message content that needs to be replaced.

value: optional string

The data that makes up the text.

refusal\_delta\_block: object { index, type, refusal }

The refusal content that is part of a message.

index: number

The index of the refusal part in the message.

type: "refusal"

Always `refusal`.

refusal: optional string

image\_url\_delta\_block: object { index, type, image\_url }

References an image URL in the content of a message.

index: number

The index of the content part in the message.

type: "image\_url"

Always `image_url`.

image\_url: optional object { detail, url }

detail: optional "auto" or "low" or "high"

Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`.

"auto"

"low"

"high"

url: optional string

The URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

message\_content\_part\_param: [ImageFileContentBlock](/api/reference/cli/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_content_block%20%3E%20(schema)) { image\_file, type }  or [ImageURLContentBlock](/api/reference/cli/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_content_block%20%3E%20(schema)) { image\_url, type }  or [TextContentBlockParam](/api/reference/cli/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text_content_block_param%20%3E%20(schema)) { text, type }

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

image\_file\_content\_block: object { image\_file, type }

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

image\_file: object { file\_id, detail }

file\_id: string

The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

detail: optional "auto" or "low" or "high"

Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

"auto"

"low"

"high"

type: "image\_file"

Always `image_file`.

image\_url\_content\_block: object { image\_url, type }

References an image URL in the content of a message.

image\_url: object { url, detail }

url: string

The external URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

detail: optional "auto" or "low" or "high"

Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`. Default value is `auto`

"auto"

"low"

"high"

type: "image\_url"

The type of the content part.

text\_content\_block\_param: object { text, type }

The text content that is part of a message.

text: string

Text content to be sent to the model

type: "text"

Always `text`.

message\_deleted: object { id, deleted, object }

id: string

deleted: boolean

object: "thread.message.deleted"

message\_delta: object { content, role }

The delta containing the fields that have changed on the Message.

content: optional array of [MessageContentDelta](/api/reference/cli/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_content_delta%20%3E%20(schema))

The content of the message in array of text and/or images.

image\_file\_delta\_block: object { index, type, image\_file }

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

index: number

The index of the content part in the message.

type: "image\_file"

Always `image_file`.

image\_file: optional object { detail, file\_id }

detail: optional "auto" or "low" or "high"

Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

"auto"

"low"

"high"

file\_id: optional string

The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

text\_delta\_block: object { index, type, text }

The text content that is part of a message.

index: number

The index of the content part in the message.

type: "text"

Always `text`.

text: optional object { annotations, value }

annotations: optional array of [AnnotationDelta](/api/reference/cli/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20annotation_delta%20%3E%20(schema))

file\_citation\_delta\_annotation: object { index, type, end\_index, 3 more }

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

index: number

The index of the annotation in the text content part.

type: "file\_citation"

Always `file_citation`.

end\_index: optional number

file\_citation: optional object { file\_id, quote }

file\_id: optional string

The ID of the specific File the citation is from.

quote: optional string

The specific quote in the file.

start\_index: optional number

text: optional string

The text in the message content that needs to be replaced.

file\_path\_delta\_annotation: object { index, type, end\_index, 3 more }

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

index: number

The index of the annotation in the text content part.

type: "file\_path"

Always `file_path`.

end\_index: optional number

file\_path: optional object { file\_id }

file\_id: optional string

The ID of the file that was generated.

start\_index: optional number

text: optional string

The text in the message content that needs to be replaced.

value: optional string

The data that makes up the text.

refusal\_delta\_block: object { index, type, refusal }

The refusal content that is part of a message.

index: number

The index of the refusal part in the message.

type: "refusal"

Always `refusal`.

refusal: optional string

image\_url\_delta\_block: object { index, type, image\_url }

References an image URL in the content of a message.

index: number

The index of the content part in the message.

type: "image\_url"

Always `image_url`.

image\_url: optional object { detail, url }

detail: optional "auto" or "low" or "high"

Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`.

"auto"

"low"

"high"

url: optional string

The URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

role: optional "user" or "assistant"

The entity that produced the message. One of `user` or `assistant`.

"user"

"assistant"

message\_delta\_event: object { id, delta, object }

Represents a message delta i.e. any changed fields on a message during streaming.

id: string

The identifier of the message, which can be referenced in API endpoints.

delta: object { content, role }

The delta containing the fields that have changed on the Message.

content: optional array of [MessageContentDelta](/api/reference/cli/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_content_delta%20%3E%20(schema))

The content of the message in array of text and/or images.

image\_file\_delta\_block: object { index, type, image\_file }

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

index: number

The index of the content part in the message.

type: "image\_file"

Always `image_file`.

image\_file: optional object { detail, file\_id }

detail: optional "auto" or "low" or "high"

Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

"auto"

"low"

"high"

file\_id: optional string

The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

text\_delta\_block: object { index, type, text }

The text content that is part of a message.

index: number

The index of the content part in the message.

type: "text"

Always `text`.

text: optional object { annotations, value }

annotations: optional array of [AnnotationDelta](/api/reference/cli/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20annotation_delta%20%3E%20(schema))

file\_citation\_delta\_annotation: object { index, type, end\_index, 3 more }

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

index: number

The index of the annotation in the text content part.

type: "file\_citation"

Always `file_citation`.

end\_index: optional number

file\_citation: optional object { file\_id, quote }

file\_id: optional string

The ID of the specific File the citation is from.

quote: optional string

The specific quote in the file.

start\_index: optional number

text: optional string

The text in the message content that needs to be replaced.

file\_path\_delta\_annotation: object { index, type, end\_index, 3 more }

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

index: number

The index of the annotation in the text content part.

type: "file\_path"

Always `file_path`.

end\_index: optional number

file\_path: optional object { file\_id }

file\_id: optional string

The ID of the file that was generated.

start\_index: optional number

text: optional string

The text in the message content that needs to be replaced.

value: optional string

The data that makes up the text.

refusal\_delta\_block: object { index, type, refusal }

The refusal content that is part of a message.

index: number

The index of the refusal part in the message.

type: "refusal"

Always `refusal`.

refusal: optional string

image\_url\_delta\_block: object { index, type, image\_url }

References an image URL in the content of a message.

index: number

The index of the content part in the message.

type: "image\_url"

Always `image_url`.

image\_url: optional object { detail, url }

detail: optional "auto" or "low" or "high"

Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`.

"auto"

"low"

"high"

url: optional string

The URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

role: optional "user" or "assistant"

The entity that produced the message. One of `user` or `assistant`.

"user"

"assistant"

object: "thread.message.delta"

The object type, which is always `thread.message.delta`.

refusal\_content\_block: object { refusal, type }

The refusal content generated by the assistant.

refusal: string

type: "refusal"

Always `refusal`.

refusal\_delta\_block: object { index, type, refusal }

The refusal content that is part of a message.

index: number

The index of the refusal part in the message.

type: "refusal"

Always `refusal`.

refusal: optional string

text: object { annotations, value }

annotations: array of [Annotation](/api/reference/cli/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20annotation%20%3E%20(schema))

file\_citation\_annotation: object { end\_index, file\_citation, start\_index, 2 more }

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

end\_index: number

file\_citation: object { file\_id }

file\_id: string

The ID of the specific File the citation is from.

start\_index: number

text: string

The text in the message content that needs to be replaced.

type: "file\_citation"

Always `file_citation`.

file\_path\_annotation: object { end\_index, file\_path, start\_index, 2 more }

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

end\_index: number

file\_path: object { file\_id }

file\_id: string

The ID of the file that was generated.

start\_index: number

text: string

The text in the message content that needs to be replaced.

type: "file\_path"

Always `file_path`.

value: string

The data that makes up the text.

text\_content\_block: object { text, type }

The text content that is part of a message.

text: object { annotations, value }

annotations: array of [Annotation](/api/reference/cli/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20annotation%20%3E%20(schema))

file\_citation\_annotation: object { end\_index, file\_citation, start\_index, 2 more }

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

end\_index: number

file\_citation: object { file\_id }

file\_id: string

The ID of the specific File the citation is from.

start\_index: number

text: string

The text in the message content that needs to be replaced.

type: "file\_citation"

Always `file_citation`.

file\_path\_annotation: object { end\_index, file\_path, start\_index, 2 more }

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

end\_index: number

file\_path: object { file\_id }

file\_id: string

The ID of the file that was generated.

start\_index: number

text: string

The text in the message content that needs to be replaced.

type: "file\_path"

Always `file_path`.

value: string

The data that makes up the text.

type: "text"

Always `text`.

text\_content\_block\_param: object { text, type }

The text content that is part of a message.

text: string

Text content to be sent to the model

type: "text"

Always `text`.

text\_delta: object { annotations, value }

annotations: optional array of [AnnotationDelta](/api/reference/cli/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20annotation_delta%20%3E%20(schema))

file\_citation\_delta\_annotation: object { index, type, end\_index, 3 more }

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

index: number

The index of the annotation in the text content part.

type: "file\_citation"

Always `file_citation`.

end\_index: optional number

file\_citation: optional object { file\_id, quote }

file\_id: optional string

The ID of the specific File the citation is from.

quote: optional string

The specific quote in the file.

start\_index: optional number

text: optional string

The text in the message content that needs to be replaced.

file\_path\_delta\_annotation: object { index, type, end\_index, 3 more }

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

index: number

The index of the annotation in the text content part.

type: "file\_path"

Always `file_path`.

end\_index: optional number

file\_path: optional object { file\_id }

file\_id: optional string

The ID of the file that was generated.

start\_index: optional number

text: optional string

The text in the message content that needs to be replaced.

value: optional string

The data that makes up the text.

text\_delta\_block: object { index, type, text }

The text content that is part of a message.

index: number

The index of the content part in the message.

type: "text"

Always `text`.

text: optional object { annotations, value }

annotations: optional array of [AnnotationDelta](/api/reference/cli/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20annotation_delta%20%3E%20(schema))

file\_citation\_delta\_annotation: object { index, type, end\_index, 3 more }

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

index: number

The index of the annotation in the text content part.

type: "file\_citation"

Always `file_citation`.

end\_index: optional number

file\_citation: optional object { file\_id, quote }

file\_id: optional string

The ID of the specific File the citation is from.

quote: optional string

The specific quote in the file.

start\_index: optional number

text: optional string

The text in the message content that needs to be replaced.

file\_path\_delta\_annotation: object { index, type, end\_index, 3 more }

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

index: number

The index of the annotation in the text content part.

type: "file\_path"

Always `file_path`.

end\_index: optional number

file\_path: optional object { file\_id }

file\_id: optional string

The ID of the file that was generated.

start\_index: optional number

text: optional string

The text in the message content that needs to be replaced.

value: optional string

The data that makes up the text.
