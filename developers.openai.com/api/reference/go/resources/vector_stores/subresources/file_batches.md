<!-- source: https://developers.openai.com/api/reference/go/resources/vector_stores/subresources/file_batches/ -->

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

# File Batches

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
