<!-- source: https://developers.openai.com/api/reference/python/resources/vector_stores/methods/retrieve/ -->

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

# Retrieve vector store

vector\_stores.retrieve(strvector\_store\_id)  -> [VectorStore](/api/reference/python/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema))

GET/vector\_stores/{vector\_store\_id}

Retrieves a vector store.

##### ParametersExpand Collapse

vector\_store\_id: str

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

### Retrieve vector store

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

vector_store = client.vector_stores.retrieve(
  vector_store_id="vs_abc123"
print(vector_store)

  "id": "vs_abc123",
  "object": "vector_store",
  "created_at": 1699061776

##### Returns Examples

  "id": "vs_abc123",
  "object": "vector_store",
  "created_at": 1699061776
