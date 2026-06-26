<!-- source: https://developers.openai.com/api/reference/resources/vector_stores/subresources/files/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Vector Stores](/api/reference/resources/vector_stores)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Files

##### [List vector store files](/api/reference/resources/vector_stores/subresources/files/methods/list)

GET/vector\_stores/{vector\_store\_id}/files

##### [Create vector store file](/api/reference/resources/vector_stores/subresources/files/methods/create)

POST/vector\_stores/{vector\_store\_id}/files

##### [Update vector store file attributes](/api/reference/resources/vector_stores/subresources/files/methods/update)

POST/vector\_stores/{vector\_store\_id}/files/{file\_id}

##### [Retrieve vector store file](/api/reference/resources/vector_stores/subresources/files/methods/retrieve)

GET/vector\_stores/{vector\_store\_id}/files/{file\_id}

##### [Delete vector store file](/api/reference/resources/vector_stores/subresources/files/methods/delete)

DELETE/vector\_stores/{vector\_store\_id}/files/{file\_id}

##### [Retrieve vector store file content](/api/reference/resources/vector_stores/subresources/files/methods/content)

GET/vector\_stores/{vector\_store\_id}/files/{file\_id}/content

##### ModelsExpand Collapse

VectorStoreFile object { id, created\_at, last\_error, 6 more }

A list of files attached to a vector store.

id: string

The identifier, which can be referenced in API endpoints.

created\_at: number

The Unix timestamp (in seconds) for when the vector store file was created.

formatunixtime

last\_error: object { code, message }

The last error associated with this vector store file. Will be `null` if there are no errors.

code: "server\_error" or "unsupported\_file" or "invalid\_file"

One of `server_error`, `unsupported_file`, or `invalid_file`.

One of the following:

"server\_error"

"unsupported\_file"

"invalid\_file"

message: string

A human-readable description of the error.

object: "vector\_store.file"

The object type, which is always `vector_store.file`.

status: "in\_progress" or "completed" or "cancelled" or "failed"

The status of the vector store file, which can be either `in_progress`, `completed`, `cancelled`, or `failed`. The status `completed` indicates that the vector store file is ready for use.

One of the following:

"in\_progress"

"completed"

"cancelled"

"failed"

usage\_bytes: number

The total vector store usage in bytes. Note that this may be different from the original file size.

vector\_store\_id: string

The ID of the [vector store](/docs/api-reference/vector-stores/object) that the [File](/docs/api-reference/files) is attached to.

attributes: optional map[string or number or boolean]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.

One of the following:

string

number

boolean

chunking\_strategy: optional [StaticFileChunkingStrategyObject](/api/reference/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy_object%20%3E%20(schema)) { static, type }  or [OtherFileChunkingStrategyObject](/api/reference/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20other_file_chunking_strategy_object%20%3E%20(schema)) { type }

The strategy used to chunk the file.

One of the following:

StaticFileChunkingStrategyObject object { static, type }

static: [StaticFileChunkingStrategy](/api/reference/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy%20%3E%20(schema)) { chunk\_overlap\_tokens, max\_chunk\_size\_tokens }

type: "static"

Always `static`.

OtherFileChunkingStrategyObject object { type }

This is returned when the chunking strategy is unknown. Typically, this is because the file was indexed before the `chunking_strategy` concept was introduced in the API.

type: "other"

Always `other`.

VectorStoreFileDeleted object { id, deleted, object }

id: string

deleted: boolean

object: "vector\_store.file.deleted"

FileContentResponse object { text, type }

text: optional string

The text content

type: optional string

The content type (currently only `"text"`)
