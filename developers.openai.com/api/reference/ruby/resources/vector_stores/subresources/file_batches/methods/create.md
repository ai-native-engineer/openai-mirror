<!-- source: https://developers.openai.com/api/reference/ruby/resources/vector_stores/subresources/file_batches/methods/create/ -->

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

# Create vector store file batch

vector\_stores.file\_batches.create(vector\_store\_id, \*\*kwargs) -> [VectorStoreFileBatch](/api/reference/ruby/resources/vector_stores#(resource)%20vector_stores.file_batches%20%3E%20(model)%20vector_store_file_batch%20%3E%20(schema)) { id, created\_at, file\_counts, 3 more }

POST/vector\_stores/{vector\_store\_id}/file\_batches

Create a vector store file batch.

##### ParametersExpand Collapse

vector\_store\_id: String

attributes: Hash[Symbol, String | Float | bool]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.

One of the following:

String = String

Float = Float

UnionMember2 = bool

chunking\_strategy: [FileChunkingStrategyParam](/api/reference/ruby/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20file_chunking_strategy_param%20%3E%20(schema))

The chunking strategy used to chunk the file(s). If not set, will use the `auto` strategy. Only applicable if `file_ids` is non-empty.

One of the following:

class AutoFileChunkingStrategyParam { type }

The default strategy. This strategy currently uses a `max_chunk_size_tokens` of `800` and `chunk_overlap_tokens` of `400`.

type: :auto

Always `auto`.

class StaticFileChunkingStrategyObjectParam { static, type }

Customize your own chunking strategy by setting chunk size and chunk overlap.

static: [StaticFileChunkingStrategy](/api/reference/ruby/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy%20%3E%20(schema)) { chunk\_overlap\_tokens, max\_chunk\_size\_tokens }

chunk\_overlap\_tokens: Integer

The number of tokens that overlap between chunks. The default value is `400`.

Note that the overlap must not exceed half of `max_chunk_size_tokens`.

max\_chunk\_size\_tokens: Integer

The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

minimum100

maximum4096

type: :static

Always `static`.

file\_ids: Array[String]

A list of [File](https://platform.openai.com/docs/api-reference/files) IDs that the vector store should use. Useful for tools like `file_search` that can access files. If `attributes` or `chunking_strategy` are provided, they will be applied to all files in the batch. The maximum batch size is 2000 files. This endpoint is recommended for multi-file ingestion and helps reduce per-vector-store write request pressure. Mutually exclusive with `files`.

files: Array[File{ file\_id, attributes, chunking\_strategy}]

A list of objects that each include a `file_id` plus optional `attributes` or `chunking_strategy`. Use this when you need to override metadata for specific files. The global `attributes` or `chunking_strategy` will be ignored and must be specified for each file. The maximum batch size is 2000 files. This endpoint is recommended for multi-file ingestion and helps reduce per-vector-store write request pressure. Mutually exclusive with `file_ids`.

file\_id: String

A [File](https://platform.openai.com/docs/api-reference/files) ID that the vector store should use. Useful for tools like `file_search` that can access files. For multi-file ingestion, we recommend [`file_batches`](https://platform.openai.com/docs/api-reference/vector-stores-file-batches/createBatch) to minimize per-vector-store write requests.

attributes: Hash[Symbol, String | Float | bool]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.

One of the following:

String = String

Float = Float

UnionMember2 = bool

chunking\_strategy: [FileChunkingStrategyParam](/api/reference/ruby/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20file_chunking_strategy_param%20%3E%20(schema))

The chunking strategy used to chunk the file(s). If not set, will use the `auto` strategy. Only applicable if `file_ids` is non-empty.

One of the following:

class AutoFileChunkingStrategyParam { type }

The default strategy. This strategy currently uses a `max_chunk_size_tokens` of `800` and `chunk_overlap_tokens` of `400`.

type: :auto

Always `auto`.

class StaticFileChunkingStrategyObjectParam { static, type }

Customize your own chunking strategy by setting chunk size and chunk overlap.

static: [StaticFileChunkingStrategy](/api/reference/ruby/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy%20%3E%20(schema)) { chunk\_overlap\_tokens, max\_chunk\_size\_tokens }

chunk\_overlap\_tokens: Integer

The number of tokens that overlap between chunks. The default value is `400`.

Note that the overlap must not exceed half of `max_chunk_size_tokens`.

max\_chunk\_size\_tokens: Integer

The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

minimum100

maximum4096

type: :static

Always `static`.

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

### Create vector store file batch

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

vector_store_file_batch = openai.vector_stores.file_batches.create("vs_abc123")

puts(vector_store_file_batch)

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
