<!-- source: https://developers.openai.com/api/reference/ruby/resources/vector_stores/subresources/file_batches/methods/cancel/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Vector Stores](/api/reference/ruby/resources/vector_stores)

[File Batches](/api/reference/ruby/resources/vector_stores/subresources/file_batches)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Cancel vector store file batch

vector\_stores.file\_batches.cancel(batch\_id, \*\*kwargs) -> [VectorStoreFileBatch](/api/reference/ruby/resources/vector_stores#(resource)%20vector_stores.file_batches%20%3E%20(model)%20vector_store_file_batch%20%3E%20(schema)) { id, created\_at, file\_counts, 3 more }

POST/vector\_stores/{vector\_store\_id}/file\_batches/{batch\_id}/cancel

Cancel a vector store file batch. This attempts to cancel the processing of files in this batch as soon as possible.

##### ParametersExpand Collapse

vector\_store\_id: String

batch\_id: String

##### ReturnsExpand Collapse

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

### Cancel vector store file batch

Ruby

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

vector_store_file_batch = openai.vector_stores.file_batches.cancel("batch_id", vector_store_id: "vector_store_id")

puts(vector_store_file_batch)

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
