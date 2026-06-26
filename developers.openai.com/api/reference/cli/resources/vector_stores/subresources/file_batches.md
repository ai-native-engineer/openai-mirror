<!-- source: https://developers.openai.com/api/reference/cli/resources/vector_stores/subresources/file_batches/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Vector Stores](/api/reference/cli/resources/vector_stores)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# File Batches

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
