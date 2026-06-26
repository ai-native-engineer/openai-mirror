<!-- source: https://developers.openai.com/api/reference/typescript/resources/vector_stores/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Vector Stores](/api/reference/typescript/resources/vector_stores)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List vector stores

client.vectorStores.list(VectorStoreListParams { after, before, limit, order } query?, RequestOptionsoptions?): CursorPage<[VectorStore](/api/reference/typescript/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)) { id, created\_at, file\_counts, 8 more } >

GET/vector\_stores

Returns a list of vector stores.

##### ParametersExpand Collapse

query: VectorStoreListParams { after, before, limit, order }

after?: string

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

before?: string

A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with obj\_foo, your subsequent call can include before=obj\_foo in order to fetch the previous page of the list.

limit?: number

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

order?: "asc" | "desc"

Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

One of the following:

"asc"

"desc"

##### ReturnsExpand Collapse

VectorStore { id, created\_at, file\_counts, 8 more }

A vector store is a collection of processed files can be used by the `file_search` tool.

id: string

The identifier, which can be referenced in API endpoints.

created\_at: number

The Unix timestamp (in seconds) for when the vector store was created.

formatunixtime

file\_counts: FileCounts { cancelled, completed, failed, 2 more }

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

last\_active\_at: number | null

The Unix timestamp (in seconds) for when the vector store was last active.

formatunixtime

metadata: [Metadata](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema)) | null

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

name: string

The name of the vector store.

object: "vector\_store"

The object type, which is always `vector_store`.

status: "expired" | "in\_progress" | "completed"

The status of the vector store, which can be either `expired`, `in_progress`, or `completed`. A status of `completed` indicates that the vector store is ready for use.

One of the following:

"expired"

"in\_progress"

"completed"

usage\_bytes: number

The total number of bytes used by the files in the vector store.

expires\_after?: ExpiresAfter { anchor, days }

The expiration policy for a vector store.

anchor: "last\_active\_at"

Anchor timestamp after which the expiration policy applies. Supported anchors: `last_active_at`.

days: number

The number of days after the anchor time that the vector store will expire.

minimum1

maximum365

expires\_at?: number | null

The Unix timestamp (in seconds) for when the vector store will expire.

formatunixtime

### List vector stores

TypeScript

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import OpenAI from "openai";
const openai = new OpenAI();

async function main() {
  const vectorStores = await openai.vectorStores.list();
  console.log(vectorStores);

main();

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
