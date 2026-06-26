<!-- source: https://developers.openai.com/api/reference/typescript/resources/vector_stores/subresources/file_batches/ -->

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

# File Batches

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
