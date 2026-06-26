<!-- source: https://developers.openai.com/api/reference/cli/resources/vector_stores/subresources/file_batches/methods/cancel/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Vector Stores](/api/reference/cli/resources/vector_stores)

[File Batches](/api/reference/cli/resources/vector_stores/subresources/file_batches)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Cancel vector store file batch

$ openai vector-stores:file-batches cancel

POST/vector\_stores/{vector\_store\_id}/file\_batches/{batch\_id}/cancel

Cancel a vector store file batch. This attempts to cancel the processing of files in this batch as soon as possible.

##### ParametersExpand Collapse

--vector-store-id: string

The ID of the vector store that the file batch belongs to.

--batch-id: string

The ID of the file batch to cancel.

##### ReturnsExpand Collapse

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

### Cancel vector store file batch

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai vector-stores:file-batches cancel \
  --api-key 'My API Key' \
  --vector-store-id vector_store_id \
  --batch-id batch_id

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
