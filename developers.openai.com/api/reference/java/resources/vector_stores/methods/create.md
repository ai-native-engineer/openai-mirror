<!-- source: https://developers.openai.com/api/reference/java/resources/vector_stores/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Vector Stores](/api/reference/java/resources/vector_stores)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create vector store

[VectorStore](/api/reference/java/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)) vectorStores().create(VectorStoreCreateParamsparams = VectorStoreCreateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/vector\_stores

Create a vector store.

##### ParametersExpand Collapse

VectorStoreCreateParams params

Optional<[FileChunkingStrategyParam](/api/reference/java/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20file_chunking_strategy_param%20%3E%20(schema))> chunkingStrategy

The chunking strategy used to chunk the file(s). If not set, will use the `auto` strategy. Only applicable if `file_ids` is non-empty.

Optional<String> description

A description for the vector store. Can be used to describe the vector store’s purpose.

Optional<ExpiresAfter> expiresAfter

The expiration policy for a vector store.

JsonValue; anchor "last\_active\_at"constant"last\_active\_at"constant

Anchor timestamp after which the expiration policy applies. Supported anchors: `last_active_at`.

long days

The number of days after the anchor time that the vector store will expire.

minimum1

maximum365

Optional<List<String>> fileIds

A list of [File](https://platform.openai.com/docs/api-reference/files) IDs that the vector store should use. Useful for tools like `file_search` that can access files.

Optional<Metadata> metadata

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

Optional<String> name

The name of the vector store.

##### ReturnsExpand Collapse

class VectorStore:

A vector store is a collection of processed files can be used by the `file_search` tool.

String id

The identifier, which can be referenced in API endpoints.

long createdAt

The Unix timestamp (in seconds) for when the vector store was created.

formatunixtime

FileCounts fileCounts

long cancelled

The number of files that were cancelled.

long completed

The number of files that have been successfully processed.

long failed

The number of files that have failed to process.

long inProgress

The number of files that are currently being processed.

long total

The total number of files.

Optional<Long> lastActiveAt

The Unix timestamp (in seconds) for when the vector store was last active.

formatunixtime

Optional<Metadata> metadata

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

String name

The name of the vector store.

JsonValue; object\_ "vector\_store"constant"vector\_store"constant

The object type, which is always `vector_store`.

Status status

The status of the vector store, which can be either `expired`, `in_progress`, or `completed`. A status of `completed` indicates that the vector store is ready for use.

One of the following:

EXPIRED("expired")

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

long usageBytes

The total number of bytes used by the files in the vector store.

Optional<ExpiresAfter> expiresAfter

The expiration policy for a vector store.

JsonValue; anchor "last\_active\_at"constant"last\_active\_at"constant

Anchor timestamp after which the expiration policy applies. Supported anchors: `last_active_at`.

long days

The number of days after the anchor time that the vector store will expire.

minimum1

maximum365

Optional<Long> expiresAt

The Unix timestamp (in seconds) for when the vector store will expire.

formatunixtime

### Create vector store

Java

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.vectorstores.VectorStore;
import com.openai.models.vectorstores.VectorStoreCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        VectorStore vectorStore = client.vectorStores().create();

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
