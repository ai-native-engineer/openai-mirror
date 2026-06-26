<!-- source: https://developers.openai.com/api/reference/python/resources/vector_stores/methods/list/ -->

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

# List vector stores

vector\_stores.list(VectorStoreListParams\*\*kwargs)  -> SyncCursorPage[[VectorStore](/api/reference/python/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema))]

GET/vector\_stores

Returns a list of vector stores.

##### ParametersExpand Collapse

after: Optional[str]

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

before: Optional[str]

A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with obj\_foo, your subsequent call can include before=obj\_foo in order to fetch the previous page of the list.

limit: Optional[int]

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

order: Optional[Literal["asc", "desc"]]

Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

One of the following:

"asc"

"desc"

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

### List vector stores

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

vector_stores = client.vector_stores.list()
print(vector_stores)

  "object": "list",
  "data": [
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
      "id": "vs_abc456",
      "object": "vector_store",
      "created_at": 1699061776,
      "name": "Support FAQ v2",
      "description": null,
      "bytes": 139920,
      "file_counts": {
        "in_progress": 0,
        "completed": 3,
        "failed": 0,
        "cancelled": 0,
        "total": 3
  ],
  "first_id": "vs_abc123",
  "last_id": "vs_abc456",
  "has_more": false

##### Returns Examples

  "object": "list",
  "data": [
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
      "id": "vs_abc456",
      "object": "vector_store",
      "created_at": 1699061776,
      "name": "Support FAQ v2",
      "description": null,
      "bytes": 139920,
      "file_counts": {
        "in_progress": 0,
        "completed": 3,
        "failed": 0,
        "cancelled": 0,
        "total": 3
  ],
  "first_id": "vs_abc123",
  "last_id": "vs_abc456",
  "has_more": false
