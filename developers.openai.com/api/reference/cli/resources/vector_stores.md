<!-- source: https://developers.openai.com/api/reference/cli/resources/vector_stores/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Vector Stores

##### [List vector stores](/api/reference/cli/resources/vector_stores/methods/list)

$ openai vector-stores list

GET/vector\_stores

##### [Create vector store](/api/reference/cli/resources/vector_stores/methods/create)

$ openai vector-stores create

POST/vector\_stores

##### [Retrieve vector store](/api/reference/cli/resources/vector_stores/methods/retrieve)

$ openai vector-stores retrieve

GET/vector\_stores/{vector\_store\_id}

##### [Modify vector store](/api/reference/cli/resources/vector_stores/methods/update)

$ openai vector-stores update

POST/vector\_stores/{vector\_store\_id}

##### [Delete vector store](/api/reference/cli/resources/vector_stores/methods/delete)

$ openai vector-stores delete

DELETE/vector\_stores/{vector\_store\_id}

##### [Search vector store](/api/reference/cli/resources/vector_stores/methods/search)

$ openai vector-stores search

POST/vector\_stores/{vector\_store\_id}/search

##### ModelsExpand Collapse

auto\_file\_chunking\_strategy\_param: object { type }

The default strategy. This strategy currently uses a `max_chunk_size_tokens` of `800` and `chunk_overlap_tokens` of `400`.

type: "auto"

Always `auto`.

file\_chunking\_strategy: [StaticFileChunkingStrategyObject](/api/reference/cli/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy_object%20%3E%20(schema)) { static, type }  or [OtherFileChunkingStrategyObject](/api/reference/cli/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20other_file_chunking_strategy_object%20%3E%20(schema)) { type }

The strategy used to chunk the file.

static\_file\_chunking\_strategy\_object: object { static, type }

static: object { chunk\_overlap\_tokens, max\_chunk\_size\_tokens }

chunk\_overlap\_tokens: number

The number of tokens that overlap between chunks. The default value is `400`.

Note that the overlap must not exceed half of `max_chunk_size_tokens`.

max\_chunk\_size\_tokens: number

The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

type: "static"

Always `static`.

other\_file\_chunking\_strategy\_object: object { type }

This is returned when the chunking strategy is unknown. Typically, this is because the file was indexed before the `chunking_strategy` concept was introduced in the API.

type: "other"

Always `other`.

file\_chunking\_strategy\_param: [AutoFileChunkingStrategyParam](/api/reference/cli/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20auto_file_chunking_strategy_param%20%3E%20(schema)) { type }  or [StaticFileChunkingStrategyObjectParam](/api/reference/cli/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy_object_param%20%3E%20(schema)) { static, type }

The chunking strategy used to chunk the file(s). If not set, will use the `auto` strategy. Only applicable if `file_ids` is non-empty.

auto\_file\_chunking\_strategy\_param: object { type }

The default strategy. This strategy currently uses a `max_chunk_size_tokens` of `800` and `chunk_overlap_tokens` of `400`.

type: "auto"

Always `auto`.

static\_file\_chunking\_strategy\_object\_param: object { static, type }

Customize your own chunking strategy by setting chunk size and chunk overlap.

static: object { chunk\_overlap\_tokens, max\_chunk\_size\_tokens }

chunk\_overlap\_tokens: number

The number of tokens that overlap between chunks. The default value is `400`.

Note that the overlap must not exceed half of `max_chunk_size_tokens`.

max\_chunk\_size\_tokens: number

The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

type: "static"

Always `static`.

other\_file\_chunking\_strategy\_object: object { type }

This is returned when the chunking strategy is unknown. Typically, this is because the file was indexed before the `chunking_strategy` concept was introduced in the API.

type: "other"

Always `other`.

static\_file\_chunking\_strategy: object { chunk\_overlap\_tokens, max\_chunk\_size\_tokens }

chunk\_overlap\_tokens: number

The number of tokens that overlap between chunks. The default value is `400`.

Note that the overlap must not exceed half of `max_chunk_size_tokens`.

max\_chunk\_size\_tokens: number

The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

static\_file\_chunking\_strategy\_object: object { static, type }

static: object { chunk\_overlap\_tokens, max\_chunk\_size\_tokens }

chunk\_overlap\_tokens: number

The number of tokens that overlap between chunks. The default value is `400`.

Note that the overlap must not exceed half of `max_chunk_size_tokens`.

max\_chunk\_size\_tokens: number

The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

type: "static"

Always `static`.

static\_file\_chunking\_strategy\_object\_param: object { static, type }

Customize your own chunking strategy by setting chunk size and chunk overlap.

static: object { chunk\_overlap\_tokens, max\_chunk\_size\_tokens }

chunk\_overlap\_tokens: number

The number of tokens that overlap between chunks. The default value is `400`.

Note that the overlap must not exceed half of `max_chunk_size_tokens`.

max\_chunk\_size\_tokens: number

The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

type: "static"

Always `static`.

vector\_store: object { id, created\_at, file\_counts, 8 more }

A vector store is a collection of processed files can be used by the `file_search` tool.

id: string

The identifier, which can be referenced in API endpoints.

created\_at: number

The Unix timestamp (in seconds) for when the vector store was created.

file\_counts: object { cancelled, completed, failed, 2 more }

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

last\_active\_at: number

The Unix timestamp (in seconds) for when the vector store was last active.

metadata: map[string]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

name: string

The name of the vector store.

object: "vector\_store"

The object type, which is always `vector_store`.

status: "expired" or "in\_progress" or "completed"

The status of the vector store, which can be either `expired`, `in_progress`, or `completed`. A status of `completed` indicates that the vector store is ready for use.

"expired"

"in\_progress"

"completed"

usage\_bytes: number

The total number of bytes used by the files in the vector store.

expires\_after: optional object { anchor, days }

The expiration policy for a vector store.

anchor: "last\_active\_at"

Anchor timestamp after which the expiration policy applies. Supported anchors: `last_active_at`.

days: number

The number of days after the anchor time that the vector store will expire.

expires\_at: optional number

The Unix timestamp (in seconds) for when the vector store will expire.

vector\_store\_deleted: object { id, deleted, object }

id: string

deleted: boolean

object: "vector\_store.deleted"

#### Vector StoresFiles

##### [List vector store files](/api/reference/cli/resources/vector_stores/subresources/files/methods/list)

$ openai vector-stores:files list

GET/vector\_stores/{vector\_store\_id}/files

##### [Create vector store file](/api/reference/cli/resources/vector_stores/subresources/files/methods/create)

$ openai vector-stores:files create

POST/vector\_stores/{vector\_store\_id}/files

##### [Update vector store file attributes](/api/reference/cli/resources/vector_stores/subresources/files/methods/update)

$ openai vector-stores:files update

POST/vector\_stores/{vector\_store\_id}/files/{file\_id}

##### [Retrieve vector store file](/api/reference/cli/resources/vector_stores/subresources/files/methods/retrieve)

$ openai vector-stores:files retrieve

GET/vector\_stores/{vector\_store\_id}/files/{file\_id}

##### [Delete vector store file](/api/reference/cli/resources/vector_stores/subresources/files/methods/delete)

$ openai vector-stores:files delete

DELETE/vector\_stores/{vector\_store\_id}/files/{file\_id}

##### [Retrieve vector store file content](/api/reference/cli/resources/vector_stores/subresources/files/methods/content)

$ openai vector-stores:files content

GET/vector\_stores/{vector\_store\_id}/files/{file\_id}/content

##### ModelsExpand Collapse

vector\_store\_file: object { id, created\_at, last\_error, 6 more }

A list of files attached to a vector store.

id: string

The identifier, which can be referenced in API endpoints.

created\_at: number

The Unix timestamp (in seconds) for when the vector store file was created.

last\_error: object { code, message }

The last error associated with this vector store file. Will be `null` if there are no errors.

code: "server\_error" or "unsupported\_file" or "invalid\_file"

One of `server_error`, `unsupported_file`, or `invalid_file`.

"server\_error"

"unsupported\_file"

"invalid\_file"

message: string

A human-readable description of the error.

object: "vector\_store.file"

The object type, which is always `vector_store.file`.

status: "in\_progress" or "completed" or "cancelled" or "failed"

The status of the vector store file, which can be either `in_progress`, `completed`, `cancelled`, or `failed`. The status `completed` indicates that the vector store file is ready for use.

"in\_progress"

"completed"

"cancelled"

"failed"

usage\_bytes: number

The total vector store usage in bytes. Note that this may be different from the original file size.

vector\_store\_id: string

The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) that the [File](https://platform.openai.com/docs/api-reference/files) is attached to.

attributes: optional map[string or number or boolean]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.

union\_member\_0: string

union\_member\_1: number

union\_member\_2: boolean

chunking\_strategy: optional [StaticFileChunkingStrategyObject](/api/reference/cli/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy_object%20%3E%20(schema)) { static, type }  or [OtherFileChunkingStrategyObject](/api/reference/cli/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20other_file_chunking_strategy_object%20%3E%20(schema)) { type }

The strategy used to chunk the file.

static\_file\_chunking\_strategy\_object: object { static, type }

static: object { chunk\_overlap\_tokens, max\_chunk\_size\_tokens }

chunk\_overlap\_tokens: number

The number of tokens that overlap between chunks. The default value is `400`.

Note that the overlap must not exceed half of `max_chunk_size_tokens`.

max\_chunk\_size\_tokens: number

The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

type: "static"

Always `static`.

other\_file\_chunking\_strategy\_object: object { type }

This is returned when the chunking strategy is unknown. Typically, this is because the file was indexed before the `chunking_strategy` concept was introduced in the API.

type: "other"

Always `other`.

vector\_store\_file\_deleted: object { id, deleted, object }

id: string

deleted: boolean

object: "vector\_store.file.deleted"

#### Vector StoresFile Batches

##### [Create vector store file batch](/api/reference/cli/resources/vector_stores/subresources/file_batches/methods/create)

$ openai vector-stores:file-batches create

POST/vector\_stores/{vector\_store\_id}/file\_batches

##### [Retrieve vector store file batch](/api/reference/cli/resources/vector_stores/subresources/file_batches/methods/retrieve)

$ openai vector-stores:file-batches retrieve

GET/vector\_stores/{vector\_store\_id}/file\_batches/{batch\_id}

##### [Cancel vector store file batch](/api/reference/cli/resources/vector_stores/subresources/file_batches/methods/cancel)

$ openai vector-stores:file-batches cancel

POST/vector\_stores/{vector\_store\_id}/file\_batches/{batch\_id}/cancel

##### [List vector store files in a batch](/api/reference/cli/resources/vector_stores/subresources/file_batches/methods/list_files)

$ openai vector-stores:file-batches list-files

GET/vector\_stores/{vector\_store\_id}/file\_batches/{batch\_id}/files

##### ModelsExpand Collapse

vector\_store\_file\_batch: object { id, created\_at, file\_counts, 3 more }

A batch of files attached to a vector store.

id: string

The identifier, which can be referenced in API endpoints.

created\_at: number

The Unix timestamp (in seconds) for when the vector store files batch was created.

file\_counts: object { cancelled, completed, failed, 2 more }

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

status: "in\_progress" or "completed" or "cancelled" or "failed"

The status of the vector store files batch, which can be either `in_progress`, `completed`, `cancelled` or `failed`.

"in\_progress"

"completed"

"cancelled"

"failed"

vector\_store\_id: string

The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) that the [File](https://platform.openai.com/docs/api-reference/files) is attached to.
