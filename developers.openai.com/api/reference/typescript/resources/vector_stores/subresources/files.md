<!-- source: https://developers.openai.com/api/reference/typescript/resources/vector_stores/subresources/files/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Vector Stores](/api/reference/typescript/resources/vector_stores)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Files

##### [List vector store files](/api/reference/typescript/resources/vector_stores/subresources/files/methods/list)

client.vectorStores.files.list(stringvectorStoreID, FileListParams { after, before, filter, 2 more } query?, RequestOptionsoptions?): CursorPage<[VectorStoreFile](/api/reference/typescript/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema)) { id, created\_at, last\_error, 6 more } >

GET/vector\_stores/{vector\_store\_id}/files

##### [Create vector store file](/api/reference/typescript/resources/vector_stores/subresources/files/methods/create)

client.vectorStores.files.create(stringvectorStoreID, FileCreateParams { file\_id, attributes, chunking\_strategy } body, RequestOptionsoptions?): [VectorStoreFile](/api/reference/typescript/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema)) { id, created\_at, last\_error, 6 more }

POST/vector\_stores/{vector\_store\_id}/files

##### [Update vector store file attributes](/api/reference/typescript/resources/vector_stores/subresources/files/methods/update)

client.vectorStores.files.update(stringfileID, FileUpdateParams { vector\_store\_id, attributes } params, RequestOptionsoptions?): [VectorStoreFile](/api/reference/typescript/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema)) { id, created\_at, last\_error, 6 more }

POST/vector\_stores/{vector\_store\_id}/files/{file\_id}

##### [Retrieve vector store file](/api/reference/typescript/resources/vector_stores/subresources/files/methods/retrieve)

client.vectorStores.files.retrieve(stringfileID, FileRetrieveParams { vector\_store\_id } params, RequestOptionsoptions?): [VectorStoreFile](/api/reference/typescript/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema)) { id, created\_at, last\_error, 6 more }

GET/vector\_stores/{vector\_store\_id}/files/{file\_id}

##### [Delete vector store file](/api/reference/typescript/resources/vector_stores/subresources/files/methods/delete)

client.vectorStores.files.delete(stringfileID, FileDeleteParams { vector\_store\_id } params, RequestOptionsoptions?): [VectorStoreFileDeleted](/api/reference/typescript/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file_deleted%20%3E%20(schema)) { id, deleted, object }

DELETE/vector\_stores/{vector\_store\_id}/files/{file\_id}

##### [Retrieve vector store file content](/api/reference/typescript/resources/vector_stores/subresources/files/methods/content)

client.vectorStores.files.content(stringfileID, FileContentParams { vector\_store\_id } params, RequestOptionsoptions?): Page<[FileContentResponse](/api/reference/typescript/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20file_content_response%20%3E%20(schema)) { text, type } >

GET/vector\_stores/{vector\_store\_id}/files/{file\_id}/content

##### ModelsExpand Collapse

VectorStoreFile { id, created\_at, last\_error, 6 more }

A list of files attached to a vector store.

id: string

The identifier, which can be referenced in API endpoints.

created\_at: number

The Unix timestamp (in seconds) for when the vector store file was created.

formatunixtime

last\_error: LastError | null

The last error associated with this vector store file. Will be `null` if there are no errors.

code: "server\_error" | "unsupported\_file" | "invalid\_file"

One of `server_error`, `unsupported_file`, or `invalid_file`.

One of the following:

"server\_error"

"unsupported\_file"

"invalid\_file"

message: string

A human-readable description of the error.

object: "vector\_store.file"

The object type, which is always `vector_store.file`.

status: "in\_progress" | "completed" | "cancelled" | "failed"

The status of the vector store file, which can be either `in_progress`, `completed`, `cancelled`, or `failed`. The status `completed` indicates that the vector store file is ready for use.

One of the following:

"in\_progress"

"completed"

"cancelled"

"failed"

usage\_bytes: number

The total vector store usage in bytes. Note that this may be different from the original file size.

vector\_store\_id: string

The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) that the [File](https://platform.openai.com/docs/api-reference/files) is attached to.

attributes?: Record<string, string | number | boolean> | null

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.

One of the following:

string

number

boolean

chunking\_strategy?: [FileChunkingStrategy](/api/reference/typescript/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20file_chunking_strategy%20%3E%20(schema))

The strategy used to chunk the file.

VectorStoreFileDeleted { id, deleted, object }

id: string

deleted: boolean

object: "vector\_store.file.deleted"

FileContentResponse { text, type }

text?: string

The text content

type?: string

The content type (currently only `"text"`)
