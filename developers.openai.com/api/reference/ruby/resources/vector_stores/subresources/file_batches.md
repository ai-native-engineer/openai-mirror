<!-- source: https://developers.openai.com/api/reference/ruby/resources/vector_stores/subresources/file_batches/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Vector Stores](/api/reference/ruby/resources/vector_stores)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# File Batches

##### [Create vector store file batch](/api/reference/ruby/resources/vector_stores/subresources/file_batches/methods/create)

vector\_stores.file\_batches.create(vector\_store\_id, \*\*kwargs) -> [VectorStoreFileBatch](/api/reference/ruby/resources/vector_stores#(resource)%20vector_stores.file_batches%20%3E%20(model)%20vector_store_file_batch%20%3E%20(schema)) { id, created\_at, file\_counts, 3 more }

POST/vector\_stores/{vector\_store\_id}/file\_batches

##### [Retrieve vector store file batch](/api/reference/ruby/resources/vector_stores/subresources/file_batches/methods/retrieve)

vector\_stores.file\_batches.retrieve(batch\_id, \*\*kwargs) -> [VectorStoreFileBatch](/api/reference/ruby/resources/vector_stores#(resource)%20vector_stores.file_batches%20%3E%20(model)%20vector_store_file_batch%20%3E%20(schema)) { id, created\_at, file\_counts, 3 more }

GET/vector\_stores/{vector\_store\_id}/file\_batches/{batch\_id}

##### [Cancel vector store file batch](/api/reference/ruby/resources/vector_stores/subresources/file_batches/methods/cancel)

vector\_stores.file\_batches.cancel(batch\_id, \*\*kwargs) -> [VectorStoreFileBatch](/api/reference/ruby/resources/vector_stores#(resource)%20vector_stores.file_batches%20%3E%20(model)%20vector_store_file_batch%20%3E%20(schema)) { id, created\_at, file\_counts, 3 more }

POST/vector\_stores/{vector\_store\_id}/file\_batches/{batch\_id}/cancel

##### [List vector store files in a batch](/api/reference/ruby/resources/vector_stores/subresources/file_batches/methods/list_files)

vector\_stores.file\_batches.list\_files(batch\_id, \*\*kwargs) -> CursorPage<[VectorStoreFile](/api/reference/ruby/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema)) { id, created\_at, last\_error, 6 more } >

GET/vector\_stores/{vector\_store\_id}/file\_batches/{batch\_id}/files

##### ModelsExpand Collapse

class VectorStoreFileBatch { id, created\_at, file\_counts, 3 more }

A batch of files attached to a vector store.

id: String

The identifier, which can be referenced in API endpoints.

created\_at: Integer

The Unix timestamp (in seconds) for when the vector store files batch was created.

formatunixtime

file\_counts: FileCounts{ cancelled, completed, failed, 2 more}

cancelled: Integer

The number of files that where cancelled.

completed: Integer

The number of files that have been processed.

failed: Integer

The number of files that have failed to process.

in\_progress: Integer

The number of files that are currently being processed.

total: Integer

The total number of files.

object: :"vector\_store.files\_batch"

The object type, which is always `vector_store.file_batch`.

status: :in\_progress | :completed | :cancelled | :failed

The status of the vector store files batch, which can be either `in_progress`, `completed`, `cancelled` or `failed`.

One of the following:

:in\_progress

:completed

:cancelled

:failed

vector\_store\_id: String

The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) that the [File](https://platform.openai.com/docs/api-reference/files) is attached to.
