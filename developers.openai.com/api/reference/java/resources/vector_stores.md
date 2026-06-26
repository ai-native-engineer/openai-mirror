<!-- source: https://developers.openai.com/api/reference/java/resources/vector_stores/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Vector Stores

##### [List vector stores](/api/reference/java/resources/vector_stores/methods/list)

VectorStoreListPage vectorStores().list(VectorStoreListParamsparams = VectorStoreListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/vector\_stores

##### [Create vector store](/api/reference/java/resources/vector_stores/methods/create)

[VectorStore](/api/reference/java/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)) vectorStores().create(VectorStoreCreateParamsparams = VectorStoreCreateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/vector\_stores

##### [Retrieve vector store](/api/reference/java/resources/vector_stores/methods/retrieve)

[VectorStore](/api/reference/java/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)) vectorStores().retrieve(VectorStoreRetrieveParamsparams = VectorStoreRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/vector\_stores/{vector\_store\_id}

##### [Modify vector store](/api/reference/java/resources/vector_stores/methods/update)

[VectorStore](/api/reference/java/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)) vectorStores().update(VectorStoreUpdateParamsparams = VectorStoreUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/vector\_stores/{vector\_store\_id}

##### [Delete vector store](/api/reference/java/resources/vector_stores/methods/delete)

[VectorStoreDeleted](/api/reference/java/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20vector_store_deleted%20%3E%20(schema)) vectorStores().delete(VectorStoreDeleteParamsparams = VectorStoreDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/vector\_stores/{vector\_store\_id}

##### [Search vector store](/api/reference/java/resources/vector_stores/methods/search)

VectorStoreSearchPage vectorStores().search(VectorStoreSearchParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/vector\_stores/{vector\_store\_id}/search

##### ModelsExpand Collapse

class AutoFileChunkingStrategyParam:

The default strategy. This strategy currently uses a `max_chunk_size_tokens` of `800` and `chunk_overlap_tokens` of `400`.

JsonValue; type "auto"constant"auto"constant

Always `auto`.

class FileChunkingStrategy: A class that can be one of several variants.union

The strategy used to chunk the file.

class StaticFileChunkingStrategyObject:

[StaticFileChunkingStrategy](/api/reference/java/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy%20%3E%20(schema)) static\_

JsonValue; type "static"constant"static"constant

Always `static`.

class OtherFileChunkingStrategyObject:

This is returned when the chunking strategy is unknown. Typically, this is because the file was indexed before the `chunking_strategy` concept was introduced in the API.

JsonValue; type "other"constant"other"constant

Always `other`.

class FileChunkingStrategyParam: A class that can be one of several variants.union

The chunking strategy used to chunk the file(s). If not set, will use the `auto` strategy. Only applicable if `file_ids` is non-empty.

class AutoFileChunkingStrategyParam:

The default strategy. This strategy currently uses a `max_chunk_size_tokens` of `800` and `chunk_overlap_tokens` of `400`.

JsonValue; type "auto"constant"auto"constant

Always `auto`.

class StaticFileChunkingStrategyObjectParam:

Customize your own chunking strategy by setting chunk size and chunk overlap.

[StaticFileChunkingStrategy](/api/reference/java/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy%20%3E%20(schema)) static\_

JsonValue; type "static"constant"static"constant

Always `static`.

class OtherFileChunkingStrategyObject:

This is returned when the chunking strategy is unknown. Typically, this is because the file was indexed before the `chunking_strategy` concept was introduced in the API.

JsonValue; type "other"constant"other"constant

Always `other`.

class StaticFileChunkingStrategy:

long chunkOverlapTokens

The number of tokens that overlap between chunks. The default value is `400`.

Note that the overlap must not exceed half of `max_chunk_size_tokens`.

long maxChunkSizeTokens

The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

minimum100

maximum4096

class StaticFileChunkingStrategyObject:

[StaticFileChunkingStrategy](/api/reference/java/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy%20%3E%20(schema)) static\_

JsonValue; type "static"constant"static"constant

Always `static`.

class StaticFileChunkingStrategyObjectParam:

Customize your own chunking strategy by setting chunk size and chunk overlap.

[StaticFileChunkingStrategy](/api/reference/java/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy%20%3E%20(schema)) static\_

JsonValue; type "static"constant"static"constant

Always `static`.

class VectorStore:

A vector store is a collection of processed files can be used by the `file_search` tool.

String id

The identifier, which can be referenced in API endpoints.

long createdAt

The Unix timestamp (in seconds) for when the vector store was created.

formatunixtime

FileCounts fileCounts

long cancelled

The number of files that were cancelled.

long completed

The number of files that have been successfully processed.

long failed

The number of files that have failed to process.

long inProgress

The number of files that are currently being processed.

long total

The total number of files.

Optional<Long> lastActiveAt

The Unix timestamp (in seconds) for when the vector store was last active.

formatunixtime

Optional<Metadata> metadata

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

String name

The name of the vector store.

JsonValue; object\_ "vector\_store"constant"vector\_store"constant

The object type, which is always `vector_store`.

Status status

The status of the vector store, which can be either `expired`, `in_progress`, or `completed`. A status of `completed` indicates that the vector store is ready for use.

One of the following:

EXPIRED("expired")

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

long usageBytes

The total number of bytes used by the files in the vector store.

Optional<ExpiresAfter> expiresAfter

The expiration policy for a vector store.

JsonValue; anchor "last\_active\_at"constant"last\_active\_at"constant

Anchor timestamp after which the expiration policy applies. Supported anchors: `last_active_at`.

long days

The number of days after the anchor time that the vector store will expire.

minimum1

maximum365

Optional<Long> expiresAt

The Unix timestamp (in seconds) for when the vector store will expire.

formatunixtime

class VectorStoreDeleted:

String id

boolean deleted

JsonValue; object\_ "vector\_store.deleted"constant"vector\_store.deleted"constant

#### Vector StoresFiles

##### [List vector store files](/api/reference/java/resources/vector_stores/subresources/files/methods/list)

FileListPage vectorStores().files().list(FileListParamsparams = FileListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/vector\_stores/{vector\_store\_id}/files

##### [Create vector store file](/api/reference/java/resources/vector_stores/subresources/files/methods/create)

[VectorStoreFile](/api/reference/java/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema)) vectorStores().files().create(FileCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/vector\_stores/{vector\_store\_id}/files

##### [Update vector store file attributes](/api/reference/java/resources/vector_stores/subresources/files/methods/update)

[VectorStoreFile](/api/reference/java/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema)) vectorStores().files().update(FileUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/vector\_stores/{vector\_store\_id}/files/{file\_id}

##### [Retrieve vector store file](/api/reference/java/resources/vector_stores/subresources/files/methods/retrieve)

[VectorStoreFile](/api/reference/java/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema)) vectorStores().files().retrieve(FileRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/vector\_stores/{vector\_store\_id}/files/{file\_id}

##### [Delete vector store file](/api/reference/java/resources/vector_stores/subresources/files/methods/delete)

[VectorStoreFileDeleted](/api/reference/java/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file_deleted%20%3E%20(schema)) vectorStores().files().delete(FileDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

DELETE/vector\_stores/{vector\_store\_id}/files/{file\_id}

##### [Retrieve vector store file content](/api/reference/java/resources/vector_stores/subresources/files/methods/content)

FileContentPage vectorStores().files().content(FileContentParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/vector\_stores/{vector\_store\_id}/files/{file\_id}/content

##### ModelsExpand Collapse

class VectorStoreFile:

A list of files attached to a vector store.

String id

The identifier, which can be referenced in API endpoints.

long createdAt

The Unix timestamp (in seconds) for when the vector store file was created.

formatunixtime

Optional<LastError> lastError

The last error associated with this vector store file. Will be `null` if there are no errors.

Code code

One of `server_error`, `unsupported_file`, or `invalid_file`.

One of the following:

SERVER\_ERROR("server\_error")

UNSUPPORTED\_FILE("unsupported\_file")

INVALID\_FILE("invalid\_file")

String message

A human-readable description of the error.

JsonValue; object\_ "vector\_store.file"constant"vector\_store.file"constant

The object type, which is always `vector_store.file`.

Status status

The status of the vector store file, which can be either `in_progress`, `completed`, `cancelled`, or `failed`. The status `completed` indicates that the vector store file is ready for use.

One of the following:

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

CANCELLED("cancelled")

FAILED("failed")

long usageBytes

The total vector store usage in bytes. Note that this may be different from the original file size.

String vectorStoreId

The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) that the [File](https://platform.openai.com/docs/api-reference/files) is attached to.

Optional<Attributes> attributes

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.

One of the following:

String

double

boolean

Optional<[FileChunkingStrategy](/api/reference/java/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20file_chunking_strategy%20%3E%20(schema))> chunkingStrategy

The strategy used to chunk the file.

class VectorStoreFileDeleted:

String id

boolean deleted

JsonValue; object\_ "vector\_store.file.deleted"constant"vector\_store.file.deleted"constant

#### Vector StoresFile Batches

##### [Create vector store file batch](/api/reference/java/resources/vector_stores/subresources/file_batches/methods/create)

[VectorStoreFileBatch](/api/reference/java/resources/vector_stores#(resource)%20vector_stores.file_batches%20%3E%20(model)%20vector_store_file_batch%20%3E%20(schema)) vectorStores().fileBatches().create(FileBatchCreateParamsparams = FileBatchCreateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/vector\_stores/{vector\_store\_id}/file\_batches

##### [Retrieve vector store file batch](/api/reference/java/resources/vector_stores/subresources/file_batches/methods/retrieve)

[VectorStoreFileBatch](/api/reference/java/resources/vector_stores#(resource)%20vector_stores.file_batches%20%3E%20(model)%20vector_store_file_batch%20%3E%20(schema)) vectorStores().fileBatches().retrieve(FileBatchRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/vector\_stores/{vector\_store\_id}/file\_batches/{batch\_id}

##### [Cancel vector store file batch](/api/reference/java/resources/vector_stores/subresources/file_batches/methods/cancel)

[VectorStoreFileBatch](/api/reference/java/resources/vector_stores#(resource)%20vector_stores.file_batches%20%3E%20(model)%20vector_store_file_batch%20%3E%20(schema)) vectorStores().fileBatches().cancel(FileBatchCancelParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/vector\_stores/{vector\_store\_id}/file\_batches/{batch\_id}/cancel

##### [List vector store files in a batch](/api/reference/java/resources/vector_stores/subresources/file_batches/methods/list_files)

FileBatchListFilesPage vectorStores().fileBatches().listFiles(FileBatchListFilesParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/vector\_stores/{vector\_store\_id}/file\_batches/{batch\_id}/files

##### ModelsExpand Collapse

class VectorStoreFileBatch:

A batch of files attached to a vector store.

String id

The identifier, which can be referenced in API endpoints.

long createdAt

The Unix timestamp (in seconds) for when the vector store files batch was created.

formatunixtime

FileCounts fileCounts

long cancelled

The number of files that where cancelled.

long completed

The number of files that have been processed.

long failed

The number of files that have failed to process.

long inProgress

The number of files that are currently being processed.

long total

The total number of files.

JsonValue; object\_ "vector\_store.files\_batch"constant"vector\_store.files\_batch"constant

The object type, which is always `vector_store.file_batch`.

Status status

The status of the vector store files batch, which can be either `in_progress`, `completed`, `cancelled` or `failed`.

One of the following:

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

CANCELLED("cancelled")

FAILED("failed")

String vectorStoreId

The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) that the [File](https://platform.openai.com/docs/api-reference/files) is attached to.
