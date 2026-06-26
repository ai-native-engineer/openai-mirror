<!-- source: https://developers.openai.com/api/reference/resources/vector_stores/subresources/file_batches/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Vector Stores](/api/reference/resources/vector_stores)

[File Batches](/api/reference/resources/vector_stores/subresources/file_batches)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve vector store file batch

GET/vector\_stores/{vector\_store\_id}/file\_batches/{batch\_id}

Retrieves a vector store file batch.

##### Path ParametersExpand Collapse

vector\_store\_id: string

batch\_id: string

##### ReturnsExpand Collapse

VectorStoreFileBatch object { id, created\_at, file\_counts, 3 more }

A batch of files attached to a vector store.

id: string

The identifier, which can be referenced in API endpoints.

created\_at: number

The Unix timestamp (in seconds) for when the vector store files batch was created.

formatunixtime

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

One of the following:

"in\_progress"

"completed"

"cancelled"

"failed"

vector\_store\_id: string

The ID of the [vector store](/docs/api-reference/vector-stores/object) that the [File](/docs/api-reference/files) is attached to.

### Retrieve vector store file batch

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl https://api.openai.com/v1/vector_stores/vs_abc123/file_batches/vsfb_abc123 \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "OpenAI-Beta: assistants=v2"

  "id": "vsfb_abc123",
  "object": "vector_store.file_batch",
  "created_at": 1699061776,
  "vector_store_id": "vs_abc123",
  "status": "in_progress",
  "file_counts": {
    "in_progress": 1,
    "completed": 1,
    "failed": 0,
    "cancelled": 0,
    "total": 0,

##### Returns Examples

  "id": "vsfb_abc123",
  "object": "vector_store.file_batch",
  "created_at": 1699061776,
  "vector_store_id": "vs_abc123",
  "status": "in_progress",
  "file_counts": {
    "in_progress": 1,
    "completed": 1,
    "failed": 0,
    "cancelled": 0,
    "total": 0,
