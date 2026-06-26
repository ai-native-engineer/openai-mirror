<!-- source: https://developers.openai.com/api/reference/typescript/resources/vector_stores/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Vector Stores

##### [List vector stores](/api/reference/typescript/resources/vector_stores/methods/list)

client.vectorStores.list(VectorStoreListParams { after, before, limit, order } query?, RequestOptionsoptions?): CursorPage<[VectorStore](/api/reference/typescript/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)) { id, created\_at, file\_counts, 8 more } >

GET/vector\_stores

##### [Create vector store](/api/reference/typescript/resources/vector_stores/methods/create)

client.vectorStores.create(VectorStoreCreateParams { chunking\_strategy, description, expires\_after, 3 more } body, RequestOptionsoptions?): [VectorStore](/api/reference/typescript/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)) { id, created\_at, file\_counts, 8 more }

POST/vector\_stores

##### [Retrieve vector store](/api/reference/typescript/resources/vector_stores/methods/retrieve)

client.vectorStores.retrieve(stringvectorStoreID, RequestOptionsoptions?): [VectorStore](/api/reference/typescript/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)) { id, created\_at, file\_counts, 8 more }

GET/vector\_stores/{vector\_store\_id}

##### [Modify vector store](/api/reference/typescript/resources/vector_stores/methods/update)

client.vectorStores.update(stringvectorStoreID, VectorStoreUpdateParams { expires\_after, metadata, name } body, RequestOptionsoptions?): [VectorStore](/api/reference/typescript/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)) { id, created\_at, file\_counts, 8 more }

POST/vector\_stores/{vector\_store\_id}

##### [Delete vector store](/api/reference/typescript/resources/vector_stores/methods/delete)

client.vectorStores.delete(stringvectorStoreID, RequestOptionsoptions?): [VectorStoreDeleted](/api/reference/typescript/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20vector_store_deleted%20%3E%20(schema)) { id, deleted, object }

DELETE/vector\_stores/{vector\_store\_id}

##### [Search vector store](/api/reference/typescript/resources/vector_stores/methods/search)

client.vectorStores.search(stringvectorStoreID, VectorStoreSearchParams { query, filters, max\_num\_results, 2 more } body, RequestOptionsoptions?): Page<[VectorStoreSearchResponse](/api/reference/typescript/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20vector_store_search_response%20%3E%20(schema)) { attributes, content, file\_id, 2 more } >

POST/vector\_stores/{vector\_store\_id}/search

##### ModelsExpand Collapse

AutoFileChunkingStrategyParam { type }

The default strategy. This strategy currently uses a `max_chunk_size_tokens` of `800` and `chunk_overlap_tokens` of `400`.

type: "auto"

Always `auto`.

FileChunkingStrategy = [StaticFileChunkingStrategyObject](/api/reference/typescript/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy_object%20%3E%20(schema)) { static, type }  | [OtherFileChunkingStrategyObject](/api/reference/typescript/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20other_file_chunking_strategy_object%20%3E%20(schema)) { type }

The strategy used to chunk the file.

One of the following:

StaticFileChunkingStrategyObject { static, type }

static: [StaticFileChunkingStrategy](/api/reference/typescript/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy%20%3E%20(schema)) { chunk\_overlap\_tokens, max\_chunk\_size\_tokens }

type: "static"

Always `static`.

OtherFileChunkingStrategyObject { type }

This is returned when the chunking strategy is unknown. Typically, this is because the file was indexed before the `chunking_strategy` concept was introduced in the API.

type: "other"

Always `other`.

FileChunkingStrategyParam = [AutoFileChunkingStrategyParam](/api/reference/typescript/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20auto_file_chunking_strategy_param%20%3E%20(schema)) { type }  | [StaticFileChunkingStrategyObjectParam](/api/reference/typescript/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy_object_param%20%3E%20(schema)) { static, type }

The chunking strategy used to chunk the file(s). If not set, will use the `auto` strategy. Only applicable if `file_ids` is non-empty.

One of the following:

AutoFileChunkingStrategyParam { type }

The default strategy. This strategy currently uses a `max_chunk_size_tokens` of `800` and `chunk_overlap_tokens` of `400`.

type: "auto"

Always `auto`.

StaticFileChunkingStrategyObjectParam { static, type }

Customize your own chunking strategy by setting chunk size and chunk overlap.

static: [StaticFileChunkingStrategy](/api/reference/typescript/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy%20%3E%20(schema)) { chunk\_overlap\_tokens, max\_chunk\_size\_tokens }

type: "static"

Always `static`.

OtherFileChunkingStrategyObject { type }

This is returned when the chunking strategy is unknown. Typically, this is because the file was indexed before the `chunking_strategy` concept was introduced in the API.

type: "other"

Always `other`.

StaticFileChunkingStrategy { chunk\_overlap\_tokens, max\_chunk\_size\_tokens }

chunk\_overlap\_tokens: number

The number of tokens that overlap between chunks. The default value is `400`.

Note that the overlap must not exceed half of `max_chunk_size_tokens`.

max\_chunk\_size\_tokens: number

The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

minimum100

maximum4096

StaticFileChunkingStrategyObject { static, type }

static: [StaticFileChunkingStrategy](/api/reference/typescript/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy%20%3E%20(schema)) { chunk\_overlap\_tokens, max\_chunk\_size\_tokens }

type: "static"

Always `static`.

StaticFileChunkingStrategyObjectParam { static, type }

Customize your own chunking strategy by setting chunk size and chunk overlap.

static: [StaticFileChunkingStrategy](/api/reference/typescript/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy%20%3E%20(schema)) { chunk\_overlap\_tokens, max\_chunk\_size\_tokens }

type: "static"

Always `static`.

VectorStore { id, created\_at, file\_counts, 8 more }

A vector store is a collection of processed files can be used by the `file_search` tool.

id: string

The identifier, which can be referenced in API endpoints.

created\_at: number

The Unix timestamp (in seconds) for when the vector store was created.

formatunixtime

file\_counts: FileCounts { cancelled, completed, failed, 2 more }

cancelled: number

The number of files that were cancelled.

completed: number

The number of files that have been successfully processed.

failed: number

The number of files that have failed to process.

in\_progress: number

The number of files that are currently being processed.

total: number

The total number of files.

last\_active\_at: number | null

The Unix timestamp (in seconds) for when the vector store was last active.

formatunixtime

metadata: [Metadata](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema)) | null

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

name: string

The name of the vector store.

object: "vector\_store"

The object type, which is always `vector_store`.

status: "expired" | "in\_progress" | "completed"

The status of the vector store, which can be either `expired`, `in_progress`, or `completed`. A status of `completed` indicates that the vector store is ready for use.

One of the following:

"expired"

"in\_progress"

"completed"

usage\_bytes: number

The total number of bytes used by the files in the vector store.

expires\_after?: ExpiresAfter { anchor, days }

The expiration policy for a vector store.

anchor: "last\_active\_at"

Anchor timestamp after which the expiration policy applies. Supported anchors: `last_active_at`.

days: number

The number of days after the anchor time that the vector store will expire.

minimum1

maximum365

expires\_at?: number | null

The Unix timestamp (in seconds) for when the vector store will expire.

formatunixtime

VectorStoreDeleted { id, deleted, object }

id: string

deleted: boolean

object: "vector\_store.deleted"

VectorStoreSearchResponse { attributes, content, file\_id, 2 more }

attributes: Record<string, string | number | boolean> | null

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.

One of the following:

string

number

boolean

content: Array<Content>

Content chunks from the file.

text: string

The text content returned from search.

type: "text"

The type of content.

file\_id: string

The ID of the vector store file.

filename: string

The name of the vector store file.

score: number

The similarity score for the result.

minimum0

maximum1

#### Vector StoresFiles

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

#### Vector StoresFile Batches

##### [Create vector store file batch](/api/reference/typescript/resources/vector_stores/subresources/file_batches/methods/create)

client.vectorStores.fileBatches.create(stringvectorStoreID, FileBatchCreateParams { attributes, chunking\_strategy, file\_ids, files } body, RequestOptionsoptions?): [VectorStoreFileBatch](/api/reference/typescript/resources/vector_stores#(resource)%20vector_stores.file_batches%20%3E%20(model)%20vector_store_file_batch%20%3E%20(schema)) { id, created\_at, file\_counts, 3 more }

POST/vector\_stores/{vector\_store\_id}/file\_batches

##### [Retrieve vector store file batch](/api/reference/typescript/resources/vector_stores/subresources/file_batches/methods/retrieve)

client.vectorStores.fileBatches.retrieve(stringbatchID, FileBatchRetrieveParams { vector\_store\_id } params, RequestOptionsoptions?): [VectorStoreFileBatch](/api/reference/typescript/resources/vector_stores#(resource)%20vector_stores.file_batches%20%3E%20(model)%20vector_store_file_batch%20%3E%20(schema)) { id, created\_at, file\_counts, 3 more }

GET/vector\_stores/{vector\_store\_id}/file\_batches/{batch\_id}

##### [Cancel vector store file batch](/api/reference/typescript/resources/vector_stores/subresources/file_batches/methods/cancel)

client.vectorStores.fileBatches.cancel(stringbatchID, FileBatchCancelParams { vector\_store\_id } params, RequestOptionsoptions?): [VectorStoreFileBatch](/api/reference/typescript/resources/vector_stores#(resource)%20vector_stores.file_batches%20%3E%20(model)%20vector_store_file_batch%20%3E%20(schema)) { id, created\_at, file\_counts, 3 more }

POST/vector\_stores/{vector\_store\_id}/file\_batches/{batch\_id}/cancel

##### [List vector store files in a batch](/api/reference/typescript/resources/vector_stores/subresources/file_batches/methods/list_files)

client.vectorStores.fileBatches.listFiles(stringbatchID, FileBatchListFilesParams { vector\_store\_id, after, before, 3 more } params, RequestOptionsoptions?): CursorPage<[VectorStoreFile](/api/reference/typescript/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema)) { id, created\_at, last\_error, 6 more } >

GET/vector\_stores/{vector\_store\_id}/file\_batches/{batch\_id}/files

##### ModelsExpand Collapse

VectorStoreFileBatch { id, created\_at, file\_counts, 3 more }

A batch of files attached to a vector store.

id: string

The identifier, which can be referenced in API endpoints.

created\_at: number

The Unix timestamp (in seconds) for when the vector store files batch was created.

formatunixtime

file\_counts: FileCounts { cancelled, completed, failed, 2 more }

cancelled: number

The number of files that where cancelled.

completed: number

The number of files that have been processed.

failed: number

The number of files that have failed to process.

in\_progress: number

The number of files that are currently being processed.

total: number

The total number of files.

object: "vector\_store.files\_batch"

The object type, which is always `vector_store.file_batch`.

status: "in\_progress" | "completed" | "cancelled" | "failed"

The status of the vector store files batch, which can be either `in_progress`, `completed`, `cancelled` or `failed`.

One of the following:

"in\_progress"

"completed"

"cancelled"

"failed"

vector\_store\_id: string

The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) that the [File](https://platform.openai.com/docs/api-reference/files) is attached to.
