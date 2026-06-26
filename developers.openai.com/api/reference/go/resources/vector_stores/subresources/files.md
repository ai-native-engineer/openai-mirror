<!-- source: https://developers.openai.com/api/reference/go/resources/vector_stores/subresources/files/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Vector Stores](/api/reference/go/resources/vector_stores)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Files

##### [List vector store files](/api/reference/go/resources/vector_stores/subresources/files/methods/list)

client.VectorStores.Files.List(ctx, vectorStoreID, query) (\*CursorPage[[VectorStoreFile](/api/reference/go/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema))], error)

GET/vector\_stores/{vector\_store\_id}/files

##### [Create vector store file](/api/reference/go/resources/vector_stores/subresources/files/methods/create)

client.VectorStores.Files.New(ctx, vectorStoreID, body) (\*[VectorStoreFile](/api/reference/go/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema)), error)

POST/vector\_stores/{vector\_store\_id}/files

##### [Update vector store file attributes](/api/reference/go/resources/vector_stores/subresources/files/methods/update)

client.VectorStores.Files.Update(ctx, vectorStoreID, fileID, body) (\*[VectorStoreFile](/api/reference/go/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema)), error)

POST/vector\_stores/{vector\_store\_id}/files/{file\_id}

##### [Retrieve vector store file](/api/reference/go/resources/vector_stores/subresources/files/methods/retrieve)

client.VectorStores.Files.Get(ctx, vectorStoreID, fileID) (\*[VectorStoreFile](/api/reference/go/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema)), error)

GET/vector\_stores/{vector\_store\_id}/files/{file\_id}

##### [Delete vector store file](/api/reference/go/resources/vector_stores/subresources/files/methods/delete)

client.VectorStores.Files.Delete(ctx, vectorStoreID, fileID) (\*[VectorStoreFileDeleted](/api/reference/go/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file_deleted%20%3E%20(schema)), error)

DELETE/vector\_stores/{vector\_store\_id}/files/{file\_id}

##### [Retrieve vector store file content](/api/reference/go/resources/vector_stores/subresources/files/methods/content)

client.VectorStores.Files.Content(ctx, vectorStoreID, fileID) (\*Page[[VectorStoreFileContentResponse](/api/reference/go/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20VectorStoreFileContentResponse%20%3E%20(schema))], error)

GET/vector\_stores/{vector\_store\_id}/files/{file\_id}/content

##### ModelsExpand Collapse

type VectorStoreFile struct{…}

A list of files attached to a vector store.

ID string

The identifier, which can be referenced in API endpoints.

CreatedAt int64

The Unix timestamp (in seconds) for when the vector store file was created.

formatunixtime

LastError VectorStoreFileLastError

The last error associated with this vector store file. Will be `null` if there are no errors.

Code string

One of `server_error`, `unsupported_file`, or `invalid_file`.

One of the following:

const VectorStoreFileLastErrorCodeServerError VectorStoreFileLastErrorCode = "server\_error"

const VectorStoreFileLastErrorCodeUnsupportedFile VectorStoreFileLastErrorCode = "unsupported\_file"

const VectorStoreFileLastErrorCodeInvalidFile VectorStoreFileLastErrorCode = "invalid\_file"

Message string

A human-readable description of the error.

Object VectorStoreFile

The object type, which is always `vector_store.file`.

Status VectorStoreFileStatus

The status of the vector store file, which can be either `in_progress`, `completed`, `cancelled`, or `failed`. The status `completed` indicates that the vector store file is ready for use.

One of the following:

const VectorStoreFileStatusInProgress VectorStoreFileStatus = "in\_progress"

const VectorStoreFileStatusCompleted VectorStoreFileStatus = "completed"

const VectorStoreFileStatusCancelled VectorStoreFileStatus = "cancelled"

const VectorStoreFileStatusFailed VectorStoreFileStatus = "failed"

UsageBytes int64

The total vector store usage in bytes. Note that this may be different from the original file size.

VectorStoreID string

The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) that the [File](https://platform.openai.com/docs/api-reference/files) is attached to.

Attributes map[string, VectorStoreFileAttributeUnion]Optional

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.

One of the following:

string

float64

bool

ChunkingStrategy [FileChunkingStrategyUnion](/api/reference/go/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20file_chunking_strategy%20%3E%20(schema))Optional

The strategy used to chunk the file.

type VectorStoreFileDeleted struct{…}

ID string

Deleted bool

Object VectorStoreFileDeleted
