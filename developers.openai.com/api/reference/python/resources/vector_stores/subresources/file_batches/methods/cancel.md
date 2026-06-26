<!-- source: https://developers.openai.com/api/reference/python/resources/vector_stores/subresources/file_batches/methods/cancel/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Vector Stores](/api/reference/python/resources/vector_stores)

[File Batches](/api/reference/python/resources/vector_stores/subresources/file_batches)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Cancel vector store file batch

vector\_stores.file\_batches.cancel(strbatch\_id, FileBatchCancelParams\*\*kwargs)  -> [VectorStoreFileBatch](/api/reference/python/resources/vector_stores#(resource)%20vector_stores.file_batches%20%3E%20(model)%20vector_store_file_batch%20%3E%20(schema))

POST/vector\_stores/{vector\_store\_id}/file\_batches/{batch\_id}/cancel

Cancel a vector store file batch. This attempts to cancel the processing of files in this batch as soon as possible.

##### ParametersExpand Collapse

vector\_store\_id: str

batch\_id: str

##### ReturnsExpand Collapse

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

### Cancel vector store file batch

Python

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

from openai import OpenAI
client = OpenAI()

deleted_vector_store_file_batch = client.vector_stores.file_batches.cancel(
    vector_store_id="vs_abc123",
    file_batch_id="vsfb_abc123"
print(deleted_vector_store_file_batch)

  "id": "vsfb_abc123",
  "object": "vector_store.file_batch",
  "created_at": 1699061776,
  "vector_store_id": "vs_abc123",
  "status": "in_progress",
  "file_counts": {
    "in_progress": 12,
    "completed": 3,
    "failed": 0,
    "cancelled": 0,
    "total": 15,

##### Returns Examples

  "id": "vsfb_abc123",
  "object": "vector_store.file_batch",
  "created_at": 1699061776,
  "vector_store_id": "vs_abc123",
  "status": "in_progress",
  "file_counts": {
    "in_progress": 12,
    "completed": 3,
    "failed": 0,
    "cancelled": 0,
    "total": 15,
