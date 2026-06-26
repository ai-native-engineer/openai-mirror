<!-- source: https://developers.openai.com/api/reference/resources/vector_stores/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Vector Stores](/api/reference/resources/vector_stores)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve vector store

GET/vector\_stores/{vector\_store\_id}

Retrieves a vector store.

##### Path ParametersExpand Collapse

vector\_store\_id: string

##### ReturnsExpand Collapse

VectorStore object { id, created\_at, file\_counts, 8 more }

A vector store is a collection of processed files can be used by the `file_search` tool.

id: string

The identifier, which can be referenced in API endpoints.

created\_at: number

The Unix timestamp (in seconds) for when the vector store was created.

formatunixtime

file\_counts: object { cancelled, completed, failed, 2 more }

cancelled: number

The number of files that were cancelled.

completed: number

The number of files that have been successfully processed.

failed: number

The number of files that have failed to process.

in\_progress: number

The number of files that are currently being processed.

total: number

The total number of files.

last\_active\_at: number

The Unix timestamp (in seconds) for when the vector store was last active.

formatunixtime

metadata: [Metadata](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

name: string

The name of the vector store.

object: "vector\_store"

The object type, which is always `vector_store`.

status: "expired" or "in\_progress" or "completed"

The status of the vector store, which can be either `expired`, `in_progress`, or `completed`. A status of `completed` indicates that the vector store is ready for use.

One of the following:

"expired"

"in\_progress"

"completed"

usage\_bytes: number

The total number of bytes used by the files in the vector store.

expires\_after: optional object { anchor, days }

The expiration policy for a vector store.

anchor: "last\_active\_at"

Anchor timestamp after which the expiration policy applies. Supported anchors: `last_active_at`.

days: number

The number of days after the anchor time that the vector store will expire.

minimum1

maximum365

expires\_at: optional number

The Unix timestamp (in seconds) for when the vector store will expire.

formatunixtime

### Retrieve vector store

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl https://api.openai.com/v1/vector_stores/vs_abc123 \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "OpenAI-Beta: assistants=v2"

  "id": "vs_abc123",
  "object": "vector_store",
  "created_at": 1699061776

##### Returns Examples

  "id": "vs_abc123",
  "object": "vector_store",
  "created_at": 1699061776
