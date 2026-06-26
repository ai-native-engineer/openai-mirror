<!-- source: https://developers.openai.com/api/reference/ruby/resources/vector_stores/methods/retrieve/ -->

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

# Retrieve vector store

vector\_stores.retrieve(vector\_store\_id) -> [VectorStore](/api/reference/ruby/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)) { id, created\_at, file\_counts, 8 more }

GET/vector\_stores/{vector\_store\_id}

Retrieves a vector store.

##### ParametersExpand Collapse

vector\_store\_id: String

##### ReturnsExpand Collapse

class VectorStore { id, created\_at, file\_counts, 8 more }

A vector store is a collection of processed files can be used by the `file_search` tool.

id: String

The identifier, which can be referenced in API endpoints.

created\_at: Integer

The Unix timestamp (in seconds) for when the vector store was created.

formatunixtime

file\_counts: FileCounts{ cancelled, completed, failed, 2 more}

cancelled: Integer

The number of files that were cancelled.

completed: Integer

The number of files that have been successfully processed.

failed: Integer

The number of files that have failed to process.

in\_progress: Integer

The number of files that are currently being processed.

total: Integer

The total number of files.

last\_active\_at: Integer

The Unix timestamp (in seconds) for when the vector store was last active.

formatunixtime

metadata: [Metadata](/api/reference/ruby/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

name: String

The name of the vector store.

object: :vector\_store

The object type, which is always `vector_store`.

status: :expired | :in\_progress | :completed

The status of the vector store, which can be either `expired`, `in_progress`, or `completed`. A status of `completed` indicates that the vector store is ready for use.

One of the following:

:expired

:in\_progress

:completed

usage\_bytes: Integer

The total number of bytes used by the files in the vector store.

expires\_after: ExpiresAfter{ anchor, days}

The expiration policy for a vector store.

anchor: :last\_active\_at

Anchor timestamp after which the expiration policy applies. Supported anchors: `last_active_at`.

days: Integer

The number of days after the anchor time that the vector store will expire.

minimum1

maximum365

expires\_at: Integer

The Unix timestamp (in seconds) for when the vector store will expire.

formatunixtime

### Retrieve vector store

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

vector_store = openai.vector_stores.retrieve("vector_store_id")

puts(vector_store)

  "id": "vs_abc123",
  "object": "vector_store",
  "created_at": 1699061776

##### Returns Examples

  "id": "vs_abc123",
  "object": "vector_store",
  "created_at": 1699061776
