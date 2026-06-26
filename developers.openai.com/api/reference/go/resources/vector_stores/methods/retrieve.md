<!-- source: https://developers.openai.com/api/reference/go/resources/vector_stores/methods/retrieve/ -->

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

# Retrieve vector store

client.VectorStores.Get(ctx, vectorStoreID) (\*[VectorStore](/api/reference/go/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)), error)

GET/vector\_stores/{vector\_store\_id}

Retrieves a vector store.

##### ParametersExpand Collapse

vectorStoreID string

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

### Retrieve vector store

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
  vectorStore, err := client.VectorStores.Get(context.TODO(), "vector_store_id")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", vectorStore.ID)

  "id": "vs_abc123",
  "object": "vector_store",
  "created_at": 1699061776

##### Returns Examples

  "id": "vs_abc123",
  "object": "vector_store",
  "created_at": 1699061776
