<!-- source: https://developers.openai.com/api/reference/python/resources/vector_stores/methods/create/ -->

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

# Create vector store

vector\_stores.create(VectorStoreCreateParams\*\*kwargs)  -> [VectorStore](/api/reference/python/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema))

POST/vector\_stores

Create a vector store.

##### ParametersExpand Collapse

chunking\_strategy: Optional[[FileChunkingStrategyParam](/api/reference/python/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20file_chunking_strategy_param%20%3E%20(schema))]

The chunking strategy used to chunk the file(s). If not set, will use the `auto` strategy. Only applicable if `file_ids` is non-empty.

One of the following:

class AutoFileChunkingStrategyParam: …

The default strategy. This strategy currently uses a `max_chunk_size_tokens` of `800` and `chunk_overlap_tokens` of `400`.

type: Literal["auto"]

Always `auto`.

class StaticFileChunkingStrategyObjectParam: …

Customize your own chunking strategy by setting chunk size and chunk overlap.

static: [StaticFileChunkingStrategy](/api/reference/python/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy%20%3E%20(schema))

chunk\_overlap\_tokens: int

The number of tokens that overlap between chunks. The default value is `400`.

Note that the overlap must not exceed half of `max_chunk_size_tokens`.

max\_chunk\_size\_tokens: int

The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

minimum100

maximum4096

type: Literal["static"]

Always `static`.

description: Optional[str]

A description for the vector store. Can be used to describe the vector store’s purpose.

expires\_after: Optional[[ExpiresAfter](/api/reference/python/resources/vector_stores/methods/create#(resource)%20vector_stores%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20expires_after%20%3E%20(schema))]

The expiration policy for a vector store.

anchor: Literal["last\_active\_at"]

Anchor timestamp after which the expiration policy applies. Supported anchors: `last_active_at`.

days: int

The number of days after the anchor time that the vector store will expire.

minimum1

maximum365

file\_ids: Optional[Sequence[str]]

A list of [File](https://platform.openai.com/docs/api-reference/files) IDs that the vector store should use. Useful for tools like `file_search` that can access files.

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

name: Optional[str]

The name of the vector store.

##### ReturnsExpand Collapse

class VectorStore: …

A vector store is a collection of processed files can be used by the `file_search` tool.

id: str

The identifier, which can be referenced in API endpoints.

created\_at: int

The Unix timestamp (in seconds) for when the vector store was created.

formatunixtime

file\_counts: FileCounts

cancelled: int

The number of files that were cancelled.

completed: int

The number of files that have been successfully processed.

failed: int

The number of files that have failed to process.

in\_progress: int

The number of files that are currently being processed.

total: int

The total number of files.

last\_active\_at: Optional[int]

The Unix timestamp (in seconds) for when the vector store was last active.

formatunixtime

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

name: str

The name of the vector store.

object: Literal["vector\_store"]

The object type, which is always `vector_store`.

status: Literal["expired", "in\_progress", "completed"]

The status of the vector store, which can be either `expired`, `in_progress`, or `completed`. A status of `completed` indicates that the vector store is ready for use.

One of the following:

"expired"

"in\_progress"

"completed"

usage\_bytes: int

The total number of bytes used by the files in the vector store.

expires\_after: Optional[ExpiresAfter]

The expiration policy for a vector store.

anchor: Literal["last\_active\_at"]

Anchor timestamp after which the expiration policy applies. Supported anchors: `last_active_at`.

days: int

The number of days after the anchor time that the vector store will expire.

minimum1

maximum365

expires\_at: Optional[int]

The Unix timestamp (in seconds) for when the vector store will expire.

formatunixtime

### Create vector store

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

vector_store = client.vector_stores.create(
  name="Support FAQ"
print(vector_store)

  "id": "vs_abc123",
  "object": "vector_store",
  "created_at": 1699061776,
  "name": "Support FAQ",
  "description": "Contains commonly asked questions and answers, organized by topic.",
  "bytes": 139920,
  "file_counts": {
    "in_progress": 0,
    "completed": 3,
    "failed": 0,
    "cancelled": 0,
    "total": 3

##### Returns Examples

  "id": "vs_abc123",
  "object": "vector_store",
  "created_at": 1699061776,
  "name": "Support FAQ",
  "description": "Contains commonly asked questions and answers, organized by topic.",
  "bytes": 139920,
  "file_counts": {
    "in_progress": 0,
    "completed": 3,
    "failed": 0,
    "cancelled": 0,
    "total": 3
