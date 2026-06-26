<!-- source: https://developers.openai.com/api/reference/go/resources/vector_stores/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Vector Stores

##### [List vector stores](/api/reference/go/resources/vector_stores/methods/list)

client.VectorStores.List(ctx, query) (\*CursorPage[[VectorStore](/api/reference/go/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema))], error)

GET/vector\_stores

##### [Create vector store](/api/reference/go/resources/vector_stores/methods/create)

client.VectorStores.New(ctx, body) (\*[VectorStore](/api/reference/go/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)), error)

POST/vector\_stores

##### [Retrieve vector store](/api/reference/go/resources/vector_stores/methods/retrieve)

client.VectorStores.Get(ctx, vectorStoreID) (\*[VectorStore](/api/reference/go/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)), error)

GET/vector\_stores/{vector\_store\_id}

##### [Modify vector store](/api/reference/go/resources/vector_stores/methods/update)

client.VectorStores.Update(ctx, vectorStoreID, body) (\*[VectorStore](/api/reference/go/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)), error)

POST/vector\_stores/{vector\_store\_id}

##### [Delete vector store](/api/reference/go/resources/vector_stores/methods/delete)

client.VectorStores.Delete(ctx, vectorStoreID) (\*[VectorStoreDeleted](/api/reference/go/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20vector_store_deleted%20%3E%20(schema)), error)

DELETE/vector\_stores/{vector\_store\_id}

##### [Search vector store](/api/reference/go/resources/vector_stores/methods/search)

client.VectorStores.Search(ctx, vectorStoreID, body) (\*Page[[VectorStoreSearchResponse](/api/reference/go/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20VectorStoreSearchResponse%20%3E%20(schema))], error)

POST/vector\_stores/{vector\_store\_id}/search

##### ModelsExpand Collapse

type AutoFileChunkingStrategyParamResp struct{…}

The default strategy. This strategy currently uses a `max_chunk_size_tokens` of `800` and `chunk_overlap_tokens` of `400`.

Type Auto

Always `auto`.

type FileChunkingStrategyUnion interface{…}

The strategy used to chunk the file.

One of the following:

type StaticFileChunkingStrategyObject struct{…}

Static [StaticFileChunkingStrategy](/api/reference/go/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy%20%3E%20(schema))

Type Static

Always `static`.

type OtherFileChunkingStrategyObject struct{…}

This is returned when the chunking strategy is unknown. Typically, this is because the file was indexed before the `chunking_strategy` concept was introduced in the API.

Type Other

Always `other`.

type FileChunkingStrategyParamUnionResp interface{…}

The chunking strategy used to chunk the file(s). If not set, will use the `auto` strategy. Only applicable if `file_ids` is non-empty.

One of the following:

type AutoFileChunkingStrategyParamResp struct{…}

The default strategy. This strategy currently uses a `max_chunk_size_tokens` of `800` and `chunk_overlap_tokens` of `400`.

Type Auto

Always `auto`.

type StaticFileChunkingStrategyObjectParamResp struct{…}

Customize your own chunking strategy by setting chunk size and chunk overlap.

Static [StaticFileChunkingStrategy](/api/reference/go/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy%20%3E%20(schema))

Type Static

Always `static`.

type OtherFileChunkingStrategyObject struct{…}

This is returned when the chunking strategy is unknown. Typically, this is because the file was indexed before the `chunking_strategy` concept was introduced in the API.

Type Other

Always `other`.

type StaticFileChunkingStrategy struct{…}

ChunkOverlapTokens int64

The number of tokens that overlap between chunks. The default value is `400`.

Note that the overlap must not exceed half of `max_chunk_size_tokens`.

MaxChunkSizeTokens int64

The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

minimum100

maximum4096

type StaticFileChunkingStrategyObject struct{…}

Static [StaticFileChunkingStrategy](/api/reference/go/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy%20%3E%20(schema))

Type Static

Always `static`.

type StaticFileChunkingStrategyObjectParamResp struct{…}

Customize your own chunking strategy by setting chunk size and chunk overlap.

Static [StaticFileChunkingStrategy](/api/reference/go/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy%20%3E%20(schema))

Type Static

Always `static`.

type VectorStore struct{…}

A vector store is a collection of processed files can be used by the `file_search` tool.

ID string

The identifier, which can be referenced in API endpoints.

CreatedAt int64

The Unix timestamp (in seconds) for when the vector store was created.

formatunixtime

FileCounts VectorStoreFileCounts

Cancelled int64

The number of files that were cancelled.

Completed int64

The number of files that have been successfully processed.

Failed int64

The number of files that have failed to process.

InProgress int64

The number of files that are currently being processed.

Total int64

The total number of files.

LastActiveAt int64

The Unix timestamp (in seconds) for when the vector store was last active.

formatunixtime

Metadata [Metadata](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

Name string

The name of the vector store.

Object VectorStore

The object type, which is always `vector_store`.

Status VectorStoreStatus

The status of the vector store, which can be either `expired`, `in_progress`, or `completed`. A status of `completed` indicates that the vector store is ready for use.

One of the following:

const VectorStoreStatusExpired VectorStoreStatus = "expired"

const VectorStoreStatusInProgress VectorStoreStatus = "in\_progress"

const VectorStoreStatusCompleted VectorStoreStatus = "completed"

UsageBytes int64

The total number of bytes used by the files in the vector store.

ExpiresAfter VectorStoreExpiresAfterOptional

The expiration policy for a vector store.

Anchor LastActiveAt

Anchor timestamp after which the expiration policy applies. Supported anchors: `last_active_at`.

Days int64

The number of days after the anchor time that the vector store will expire.

minimum1

maximum365

ExpiresAt int64Optional

The Unix timestamp (in seconds) for when the vector store will expire.

formatunixtime

type VectorStoreDeleted struct{…}

ID string

Deleted bool

Object VectorStoreDeleted

#### Vector StoresFiles

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

#### Vector StoresFile Batches

##### [Create vector store file batch](/api/reference/go/resources/vector_stores/subresources/file_batches/methods/create)

client.VectorStores.FileBatches.New(ctx, vectorStoreID, body) (\*[VectorStoreFileBatch](/api/reference/go/resources/vector_stores#(resource)%20vector_stores.file_batches%20%3E%20(model)%20vector_store_file_batch%20%3E%20(schema)), error)

POST/vector\_stores/{vector\_store\_id}/file\_batches

##### [Retrieve vector store file batch](/api/reference/go/resources/vector_stores/subresources/file_batches/methods/retrieve)

client.VectorStores.FileBatches.Get(ctx, vectorStoreID, batchID) (\*[VectorStoreFileBatch](/api/reference/go/resources/vector_stores#(resource)%20vector_stores.file_batches%20%3E%20(model)%20vector_store_file_batch%20%3E%20(schema)), error)

GET/vector\_stores/{vector\_store\_id}/file\_batches/{batch\_id}

##### [Cancel vector store file batch](/api/reference/go/resources/vector_stores/subresources/file_batches/methods/cancel)

client.VectorStores.FileBatches.Cancel(ctx, vectorStoreID, batchID) (\*[VectorStoreFileBatch](/api/reference/go/resources/vector_stores#(resource)%20vector_stores.file_batches%20%3E%20(model)%20vector_store_file_batch%20%3E%20(schema)), error)

POST/vector\_stores/{vector\_store\_id}/file\_batches/{batch\_id}/cancel

##### [List vector store files in a batch](/api/reference/go/resources/vector_stores/subresources/file_batches/methods/list_files)

client.VectorStores.FileBatches.ListFiles(ctx, vectorStoreID, batchID, query) (\*CursorPage[[VectorStoreFile](/api/reference/go/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema))], error)

GET/vector\_stores/{vector\_store\_id}/file\_batches/{batch\_id}/files

##### ModelsExpand Collapse

type VectorStoreFileBatch struct{…}

A batch of files attached to a vector store.

ID string

The identifier, which can be referenced in API endpoints.

CreatedAt int64

The Unix timestamp (in seconds) for when the vector store files batch was created.

formatunixtime

FileCounts VectorStoreFileBatchFileCounts

Cancelled int64

The number of files that where cancelled.

Completed int64

The number of files that have been processed.

Failed int64

The number of files that have failed to process.

InProgress int64

The number of files that are currently being processed.

Total int64

The total number of files.

Object VectorStoreFilesBatch

The object type, which is always `vector_store.file_batch`.

Status VectorStoreFileBatchStatus

The status of the vector store files batch, which can be either `in_progress`, `completed`, `cancelled` or `failed`.

One of the following:

const VectorStoreFileBatchStatusInProgress VectorStoreFileBatchStatus = "in\_progress"

const VectorStoreFileBatchStatusCompleted VectorStoreFileBatchStatus = "completed"

const VectorStoreFileBatchStatusCancelled VectorStoreFileBatchStatus = "cancelled"

const VectorStoreFileBatchStatusFailed VectorStoreFileBatchStatus = "failed"

VectorStoreID string

The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) that the [File](https://platform.openai.com/docs/api-reference/files) is attached to.
