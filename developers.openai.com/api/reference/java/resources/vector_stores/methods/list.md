<!-- source: https://developers.openai.com/api/reference/java/resources/vector_stores/methods/list/ -->

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

# List vector stores

VectorStoreListPage vectorStores().list(VectorStoreListParamsparams = VectorStoreListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/vector\_stores

Returns a list of vector stores.

##### ParametersExpand Collapse

VectorStoreListParams params

Optional<String> after

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

Optional<String> before

A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with obj\_foo, your subsequent call can include before=obj\_foo in order to fetch the previous page of the list.

Optional<Long> limit

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

Optional<[Order](/api/reference/java/resources/vector_stores/methods/list#(resource)%20vector_stores%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))> order

Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

ASC("asc")

DESC("desc")

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

### List vector stores

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
import com.openai.models.vectorstores.VectorStoreListPage;
import com.openai.models.vectorstores.VectorStoreListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        VectorStoreListPage page = client.vectorStores().list();

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
