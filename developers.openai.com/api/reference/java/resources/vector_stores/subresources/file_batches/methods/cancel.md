<!-- source: https://developers.openai.com/api/reference/java/resources/vector_stores/subresources/file_batches/methods/cancel/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Vector Stores](/api/reference/java/resources/vector_stores)

[File Batches](/api/reference/java/resources/vector_stores/subresources/file_batches)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Cancel vector store file batch

[VectorStoreFileBatch](/api/reference/java/resources/vector_stores#(resource)%20vector_stores.file_batches%20%3E%20(model)%20vector_store_file_batch%20%3E%20(schema)) vectorStores().fileBatches().cancel(FileBatchCancelParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/vector\_stores/{vector\_store\_id}/file\_batches/{batch\_id}/cancel

Cancel a vector store file batch. This attempts to cancel the processing of files in this batch as soon as possible.

##### ParametersExpand Collapse

FileBatchCancelParams params

String vectorStoreId

Optional<String> batchId

##### ReturnsExpand Collapse

class VectorStoreFileBatch:

A batch of files attached to a vector store.

String id

The identifier, which can be referenced in API endpoints.

long createdAt

The Unix timestamp (in seconds) for when the vector store files batch was created.

formatunixtime

FileCounts fileCounts

long cancelled

The number of files that where cancelled.

long completed

The number of files that have been processed.

long failed

The number of files that have failed to process.

long inProgress

The number of files that are currently being processed.

long total

The total number of files.

JsonValue; object\_ "vector\_store.files\_batch"constant"vector\_store.files\_batch"constant

The object type, which is always `vector_store.file_batch`.

Status status

The status of the vector store files batch, which can be either `in_progress`, `completed`, `cancelled` or `failed`.

One of the following:

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

CANCELLED("cancelled")

FAILED("failed")

String vectorStoreId

The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) that the [File](https://platform.openai.com/docs/api-reference/files) is attached to.

### Cancel vector store file batch

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
import com.openai.models.vectorstores.filebatches.FileBatchCancelParams;
import com.openai.models.vectorstores.filebatches.VectorStoreFileBatch;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        FileBatchCancelParams params = FileBatchCancelParams.builder()
            .vectorStoreId("vector_store_id")
            .batchId("batch_id")
            .build();
        VectorStoreFileBatch vectorStoreFileBatch = client.vectorStores().fileBatches().cancel(params);

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
