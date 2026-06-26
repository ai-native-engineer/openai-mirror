<!-- source: https://developers.openai.com/api/reference/go/resources/vector_stores/subresources/file_batches/methods/cancel/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Vector Stores](/api/reference/go/resources/vector_stores)

[File Batches](/api/reference/go/resources/vector_stores/subresources/file_batches)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Cancel vector store file batch

client.VectorStores.FileBatches.Cancel(ctx, vectorStoreID, batchID) (\*[VectorStoreFileBatch](/api/reference/go/resources/vector_stores#(resource)%20vector_stores.file_batches%20%3E%20(model)%20vector_store_file_batch%20%3E%20(schema)), error)

POST/vector\_stores/{vector\_store\_id}/file\_batches/{batch\_id}/cancel

Cancel a vector store file batch. This attempts to cancel the processing of files in this batch as soon as possible.

##### ParametersExpand Collapse

vectorStoreID string

batchID string

##### ReturnsExpand Collapse

type VectorStoreFileBatch struct{…}

A batch of files attached to a vector store.

ID string

The identifier, which can be referenced in API endpoints.

CreatedAt int64

The Unix timestamp (in seconds) for when the vector store files batch was created.

formatunixtime

FileCounts VectorStoreFileBatchFileCounts

Cancelled int64

The number of files that where cancelled.

Completed int64

The number of files that have been processed.

Failed int64

The number of files that have failed to process.

InProgress int64

The number of files that are currently being processed.

Total int64

The total number of files.

Object VectorStoreFilesBatch

The object type, which is always `vector_store.file_batch`.

Status VectorStoreFileBatchStatus

The status of the vector store files batch, which can be either `in_progress`, `completed`, `cancelled` or `failed`.

One of the following:

const VectorStoreFileBatchStatusInProgress VectorStoreFileBatchStatus = "in\_progress"

const VectorStoreFileBatchStatusCompleted VectorStoreFileBatchStatus = "completed"

const VectorStoreFileBatchStatusCancelled VectorStoreFileBatchStatus = "cancelled"

const VectorStoreFileBatchStatusFailed VectorStoreFileBatchStatus = "failed"

VectorStoreID string

The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) that the [File](https://platform.openai.com/docs/api-reference/files) is attached to.

### Cancel vector store file batch

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
  vectorStoreFileBatch, err := client.VectorStores.FileBatches.Cancel(
    context.TODO(),
    "vector_store_id",
    "batch_id",
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", vectorStoreFileBatch.ID)

  "id": "vsfb_abc123",
  "object": "vector_store.file_batch",
  "created_at": 1699061776,
  "vector_store_id": "vs_abc123",
  "status": "in_progress",
  "file_counts": {
    "in_progress": 12,
    "completed": 3,
    "failed": 0,
    "cancelled": 0,
    "total": 15,

##### Returns Examples

  "id": "vsfb_abc123",
  "object": "vector_store.file_batch",
  "created_at": 1699061776,
  "vector_store_id": "vs_abc123",
  "status": "in_progress",
  "file_counts": {
    "in_progress": 12,
    "completed": 3,
    "failed": 0,
    "cancelled": 0,
    "total": 15,
