<!-- source: https://developers.openai.com/api/reference/python/resources/vector_stores/subresources/file_batches/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Vector Stores](/api/reference/python/resources/vector_stores)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# File Batches

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
