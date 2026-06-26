<!-- source: https://developers.openai.com/api/reference/go/resources/vector_stores/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Vector Stores](/api/reference/go/resources/vector_stores)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List vector stores

client.VectorStores.List(ctx, query) (\*CursorPage[[VectorStore](/api/reference/go/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema))], error)

GET/vector\_stores

Returns a list of vector stores.

##### ParametersExpand Collapse

query VectorStoreListParams

After param.Field[string]Optional

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

Before param.Field[string]Optional

A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with obj\_foo, your subsequent call can include before=obj\_foo in order to fetch the previous page of the list.

Limit param.Field[int64]Optional

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

Order param.Field[[VectorStoreListParamsOrder](/api/reference/go/resources/vector_stores/methods/list#(resource)%20vector_stores%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))]Optional

Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

const VectorStoreListParamsOrderAsc [VectorStoreListParamsOrder](/api/reference/go/resources/vector_stores/methods/list#(resource)%20vector_stores%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)) = "asc"

const VectorStoreListParamsOrderDesc [VectorStoreListParamsOrder](/api/reference/go/resources/vector_stores/methods/list#(resource)%20vector_stores%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)) = "desc"

##### ReturnsExpand Collapse

type VectorStore struct{…}

A vector store is a collection of processed files can be used by the `file_search` tool.

ID string

The identifier, which can be referenced in API endpoints.

CreatedAt int64

The Unix timestamp (in seconds) for when the vector store was created.

formatunixtime

FileCounts VectorStoreFileCounts

Cancelled int64

The number of files that were cancelled.

Completed int64

The number of files that have been successfully processed.

Failed int64

The number of files that have failed to process.

InProgress int64

The number of files that are currently being processed.

Total int64

The total number of files.

LastActiveAt int64

The Unix timestamp (in seconds) for when the vector store was last active.

formatunixtime

Metadata [Metadata](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

Name string

The name of the vector store.

Object VectorStore

The object type, which is always `vector_store`.

Status VectorStoreStatus

The status of the vector store, which can be either `expired`, `in_progress`, or `completed`. A status of `completed` indicates that the vector store is ready for use.

One of the following:

const VectorStoreStatusExpired VectorStoreStatus = "expired"

const VectorStoreStatusInProgress VectorStoreStatus = "in\_progress"

const VectorStoreStatusCompleted VectorStoreStatus = "completed"

UsageBytes int64

The total number of bytes used by the files in the vector store.

ExpiresAfter VectorStoreExpiresAfterOptional

The expiration policy for a vector store.

Anchor LastActiveAt

Anchor timestamp after which the expiration policy applies. Supported anchors: `last_active_at`.

Days int64

The number of days after the anchor time that the vector store will expire.

minimum1

maximum365

ExpiresAt int64Optional

The Unix timestamp (in seconds) for when the vector store will expire.

formatunixtime

### List vector stores

Go

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  page, err := client.VectorStores.List(context.TODO(), openai.VectorStoreListParams{

  })
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", page)

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
