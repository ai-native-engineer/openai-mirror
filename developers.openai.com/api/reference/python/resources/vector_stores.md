<!-- source: https://developers.openai.com/api/reference/python/resources/vector_stores/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Vector Stores

##### [List vector stores](/api/reference/python/resources/vector_stores/methods/list)

vector\_stores.list(VectorStoreListParams\*\*kwargs)  -> SyncCursorPage[[VectorStore](/api/reference/python/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema))]

GET/vector\_stores

##### [Create vector store](/api/reference/python/resources/vector_stores/methods/create)

vector\_stores.create(VectorStoreCreateParams\*\*kwargs)  -> [VectorStore](/api/reference/python/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema))

POST/vector\_stores

##### [Retrieve vector store](/api/reference/python/resources/vector_stores/methods/retrieve)

vector\_stores.retrieve(strvector\_store\_id)  -> [VectorStore](/api/reference/python/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema))

GET/vector\_stores/{vector\_store\_id}

##### [Modify vector store](/api/reference/python/resources/vector_stores/methods/update)

vector\_stores.update(strvector\_store\_id, VectorStoreUpdateParams\*\*kwargs)  -> [VectorStore](/api/reference/python/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema))

POST/vector\_stores/{vector\_store\_id}

##### [Delete vector store](/api/reference/python/resources/vector_stores/methods/delete)

vector\_stores.delete(strvector\_store\_id)  -> [VectorStoreDeleted](/api/reference/python/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20vector_store_deleted%20%3E%20(schema))

DELETE/vector\_stores/{vector\_store\_id}

##### [Search vector store](/api/reference/python/resources/vector_stores/methods/search)

vector\_stores.search(strvector\_store\_id, VectorStoreSearchParams\*\*kwargs)  -> SyncPage[[VectorStoreSearchResponse](/api/reference/python/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20vector_store_search_response%20%3E%20(schema))]

POST/vector\_stores/{vector\_store\_id}/search

##### ModelsExpand Collapse

class AutoFileChunkingStrategyParam: …

The default strategy. This strategy currently uses a `max_chunk_size_tokens` of `800` and `chunk_overlap_tokens` of `400`.

type: Literal["auto"]

Always `auto`.

[FileChunkingStrategy](/api/reference/python/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20file_chunking_strategy%20%3E%20(schema))

The strategy used to chunk the file.

One of the following:

class StaticFileChunkingStrategyObject: …

static: [StaticFileChunkingStrategy](/api/reference/python/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy%20%3E%20(schema))

type: Literal["static"]

Always `static`.

class OtherFileChunkingStrategyObject: …

This is returned when the chunking strategy is unknown. Typically, this is because the file was indexed before the `chunking_strategy` concept was introduced in the API.

type: Literal["other"]

Always `other`.

[FileChunkingStrategyParam](/api/reference/python/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20file_chunking_strategy_param%20%3E%20(schema))

The chunking strategy used to chunk the file(s). If not set, will use the `auto` strategy. Only applicable if `file_ids` is non-empty.

One of the following:

class AutoFileChunkingStrategyParam: …

The default strategy. This strategy currently uses a `max_chunk_size_tokens` of `800` and `chunk_overlap_tokens` of `400`.

type: Literal["auto"]

Always `auto`.

class StaticFileChunkingStrategyObjectParam: …

Customize your own chunking strategy by setting chunk size and chunk overlap.

static: [StaticFileChunkingStrategy](/api/reference/python/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy%20%3E%20(schema))

type: Literal["static"]

Always `static`.

class OtherFileChunkingStrategyObject: …

This is returned when the chunking strategy is unknown. Typically, this is because the file was indexed before the `chunking_strategy` concept was introduced in the API.

type: Literal["other"]

Always `other`.

class StaticFileChunkingStrategy: …

chunk\_overlap\_tokens: int

The number of tokens that overlap between chunks. The default value is `400`.

Note that the overlap must not exceed half of `max_chunk_size_tokens`.

max\_chunk\_size\_tokens: int

The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

minimum100

maximum4096

class StaticFileChunkingStrategyObject: …

static: [StaticFileChunkingStrategy](/api/reference/python/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy%20%3E%20(schema))

type: Literal["static"]

Always `static`.

class StaticFileChunkingStrategyObjectParam: …

Customize your own chunking strategy by setting chunk size and chunk overlap.

static: [StaticFileChunkingStrategy](/api/reference/python/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy%20%3E%20(schema))

type: Literal["static"]

Always `static`.

class VectorStore: …

A vector store is a collection of processed files can be used by the `file_search` tool.

id: str

The identifier, which can be referenced in API endpoints.

created\_at: int

The Unix timestamp (in seconds) for when the vector store was created.

formatunixtime

file\_counts: FileCounts

cancelled: int

The number of files that were cancelled.

completed: int

The number of files that have been successfully processed.

failed: int

The number of files that have failed to process.

in\_progress: int

The number of files that are currently being processed.

total: int

The total number of files.

last\_active\_at: Optional[int]

The Unix timestamp (in seconds) for when the vector store was last active.

formatunixtime

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

name: str

The name of the vector store.

object: Literal["vector\_store"]

The object type, which is always `vector_store`.

status: Literal["expired", "in\_progress", "completed"]

The status of the vector store, which can be either `expired`, `in_progress`, or `completed`. A status of `completed` indicates that the vector store is ready for use.

One of the following:

"expired"

"in\_progress"

"completed"

usage\_bytes: int

The total number of bytes used by the files in the vector store.

expires\_after: Optional[ExpiresAfter]

The expiration policy for a vector store.

anchor: Literal["last\_active\_at"]

Anchor timestamp after which the expiration policy applies. Supported anchors: `last_active_at`.

days: int

The number of days after the anchor time that the vector store will expire.

minimum1

maximum365

expires\_at: Optional[int]

The Unix timestamp (in seconds) for when the vector store will expire.

formatunixtime

class VectorStoreDeleted: …

id: str

deleted: bool

object: Literal["vector\_store.deleted"]

class VectorStoreSearchResponse: …

attributes: Optional[Dict[str, Union[str, float, bool]]]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.

One of the following:

str

float

bool

content: List[Content]

Content chunks from the file.

text: str

The text content returned from search.

type: Literal["text"]

The type of content.

file\_id: str

The ID of the vector store file.

filename: str

The name of the vector store file.

score: float

The similarity score for the result.

minimum0

maximum1

#### Vector StoresFiles

##### [List vector store files](/api/reference/python/resources/vector_stores/subresources/files/methods/list)

vector\_stores.files.list(strvector\_store\_id, FileListParams\*\*kwargs)  -> SyncCursorPage[[VectorStoreFile](/api/reference/python/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema))]

GET/vector\_stores/{vector\_store\_id}/files

##### [Create vector store file](/api/reference/python/resources/vector_stores/subresources/files/methods/create)

vector\_stores.files.create(strvector\_store\_id, FileCreateParams\*\*kwargs)  -> [VectorStoreFile](/api/reference/python/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema))

POST/vector\_stores/{vector\_store\_id}/files

##### [Update vector store file attributes](/api/reference/python/resources/vector_stores/subresources/files/methods/update)

vector\_stores.files.update(strfile\_id, FileUpdateParams\*\*kwargs)  -> [VectorStoreFile](/api/reference/python/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema))

POST/vector\_stores/{vector\_store\_id}/files/{file\_id}

##### [Retrieve vector store file](/api/reference/python/resources/vector_stores/subresources/files/methods/retrieve)

vector\_stores.files.retrieve(strfile\_id, FileRetrieveParams\*\*kwargs)  -> [VectorStoreFile](/api/reference/python/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema))

GET/vector\_stores/{vector\_store\_id}/files/{file\_id}

##### [Delete vector store file](/api/reference/python/resources/vector_stores/subresources/files/methods/delete)

vector\_stores.files.delete(strfile\_id, FileDeleteParams\*\*kwargs)  -> [VectorStoreFileDeleted](/api/reference/python/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file_deleted%20%3E%20(schema))

DELETE/vector\_stores/{vector\_store\_id}/files/{file\_id}

##### [Retrieve vector store file content](/api/reference/python/resources/vector_stores/subresources/files/methods/content)

vector\_stores.files.content(strfile\_id, FileContentParams\*\*kwargs)  -> SyncPage[[FileContentResponse](/api/reference/python/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20file_content_response%20%3E%20(schema))]

GET/vector\_stores/{vector\_store\_id}/files/{file\_id}/content

##### ModelsExpand Collapse

class VectorStoreFile: …

A list of files attached to a vector store.

id: str

The identifier, which can be referenced in API endpoints.

created\_at: int

The Unix timestamp (in seconds) for when the vector store file was created.

formatunixtime

last\_error: Optional[LastError]

The last error associated with this vector store file. Will be `null` if there are no errors.

code: Literal["server\_error", "unsupported\_file", "invalid\_file"]

One of `server_error`, `unsupported_file`, or `invalid_file`.

One of the following:

"server\_error"

"unsupported\_file"

"invalid\_file"

message: str

A human-readable description of the error.

object: Literal["vector\_store.file"]

The object type, which is always `vector_store.file`.

status: Literal["in\_progress", "completed", "cancelled", "failed"]

The status of the vector store file, which can be either `in_progress`, `completed`, `cancelled`, or `failed`. The status `completed` indicates that the vector store file is ready for use.

One of the following:

"in\_progress"

"completed"

"cancelled"

"failed"

usage\_bytes: int

The total vector store usage in bytes. Note that this may be different from the original file size.

vector\_store\_id: str

The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) that the [File](https://platform.openai.com/docs/api-reference/files) is attached to.

attributes: Optional[Dict[str, Union[str, float, bool]]]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.

One of the following:

str

float

bool

chunking\_strategy: Optional[FileChunkingStrategy]

The strategy used to chunk the file.

class VectorStoreFileDeleted: …

id: str

deleted: bool

object: Literal["vector\_store.file.deleted"]

class FileContentResponse: …

text: Optional[str]

The text content

type: Optional[str]

The content type (currently only `"text"`)

#### Vector StoresFile Batches

##### [Create vector store file batch](/api/reference/python/resources/vector_stores/subresources/file_batches/methods/create)

vector\_stores.file\_batches.create(strvector\_store\_id, FileBatchCreateParams\*\*kwargs)  -> [VectorStoreFileBatch](/api/reference/python/resources/vector_stores#(resource)%20vector_stores.file_batches%20%3E%20(model)%20vector_store_file_batch%20%3E%20(schema))

POST/vector\_stores/{vector\_store\_id}/file\_batches

##### [Retrieve vector store file batch](/api/reference/python/resources/vector_stores/subresources/file_batches/methods/retrieve)

vector\_stores.file\_batches.retrieve(strbatch\_id, FileBatchRetrieveParams\*\*kwargs)  -> [VectorStoreFileBatch](/api/reference/python/resources/vector_stores#(resource)%20vector_stores.file_batches%20%3E%20(model)%20vector_store_file_batch%20%3E%20(schema))

GET/vector\_stores/{vector\_store\_id}/file\_batches/{batch\_id}

##### [Cancel vector store file batch](/api/reference/python/resources/vector_stores/subresources/file_batches/methods/cancel)

vector\_stores.file\_batches.cancel(strbatch\_id, FileBatchCancelParams\*\*kwargs)  -> [VectorStoreFileBatch](/api/reference/python/resources/vector_stores#(resource)%20vector_stores.file_batches%20%3E%20(model)%20vector_store_file_batch%20%3E%20(schema))

POST/vector\_stores/{vector\_store\_id}/file\_batches/{batch\_id}/cancel

##### [List vector store files in a batch](/api/reference/python/resources/vector_stores/subresources/file_batches/methods/list_files)

vector\_stores.file\_batches.list\_files(strbatch\_id, FileBatchListFilesParams\*\*kwargs)  -> SyncCursorPage[[VectorStoreFile](/api/reference/python/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema))]

GET/vector\_stores/{vector\_store\_id}/file\_batches/{batch\_id}/files

##### ModelsExpand Collapse

class VectorStoreFileBatch: …

A batch of files attached to a vector store.

id: str

The identifier, which can be referenced in API endpoints.

created\_at: int

The Unix timestamp (in seconds) for when the vector store files batch was created.

formatunixtime

file\_counts: FileCounts

cancelled: int

The number of files that where cancelled.

completed: int

The number of files that have been processed.

failed: int

The number of files that have failed to process.

in\_progress: int

The number of files that are currently being processed.

total: int

The total number of files.

object: Literal["vector\_store.files\_batch"]

The object type, which is always `vector_store.file_batch`.

status: Literal["in\_progress", "completed", "cancelled", "failed"]

The status of the vector store files batch, which can be either `in_progress`, `completed`, `cancelled` or `failed`.

One of the following:

"in\_progress"

"completed"

"cancelled"

"failed"

vector\_store\_id: str

The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) that the [File](https://platform.openai.com/docs/api-reference/files) is attached to.
