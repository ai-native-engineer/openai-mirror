<!-- source: https://developers.openai.com/api/reference/java/resources/vector_stores/subresources/file_batches/methods/list_files/ -->

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

# List vector store files in a batch

FileBatchListFilesPage vectorStores().fileBatches().listFiles(FileBatchListFilesParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/vector\_stores/{vector\_store\_id}/file\_batches/{batch\_id}/files

Returns a list of vector store files in a batch.

##### ParametersExpand Collapse

FileBatchListFilesParams params

String vectorStoreId

Optional<String> batchId

Optional<String> after

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

Optional<String> before

A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with obj\_foo, your subsequent call can include before=obj\_foo in order to fetch the previous page of the list.

Optional<[Filter](/api/reference/java/resources/vector_stores/subresources/file_batches/methods/list_files#(resource)%20vector_stores.file_batches%20%3E%20(method)%20list_files%20%3E%20(params)%20default%20%3E%20(param)%20filter%20%3E%20(schema))> filter

Filter by file status. One of `in_progress`, `completed`, `failed`, `cancelled`.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

FAILED("failed")

CANCELLED("cancelled")

Optional<Long> limit

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

Optional<[Order](/api/reference/java/resources/vector_stores/subresources/file_batches/methods/list_files#(resource)%20vector_stores.file_batches%20%3E%20(method)%20list_files%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))> order

Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

ASC("asc")

DESC("desc")

##### ReturnsExpand Collapse

class VectorStoreFile:

A list of files attached to a vector store.

String id

The identifier, which can be referenced in API endpoints.

long createdAt

The Unix timestamp (in seconds) for when the vector store file was created.

formatunixtime

Optional<LastError> lastError

The last error associated with this vector store file. Will be `null` if there are no errors.

Code code

One of `server_error`, `unsupported_file`, or `invalid_file`.

One of the following:

SERVER\_ERROR("server\_error")

UNSUPPORTED\_FILE("unsupported\_file")

INVALID\_FILE("invalid\_file")

String message

A human-readable description of the error.

JsonValue; object\_ "vector\_store.file"constant"vector\_store.file"constant

The object type, which is always `vector_store.file`.

Status status

The status of the vector store file, which can be either `in_progress`, `completed`, `cancelled`, or `failed`. The status `completed` indicates that the vector store file is ready for use.

One of the following:

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

CANCELLED("cancelled")

FAILED("failed")

long usageBytes

The total vector store usage in bytes. Note that this may be different from the original file size.

String vectorStoreId

The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) that the [File](https://platform.openai.com/docs/api-reference/files) is attached to.

Optional<Attributes> attributes

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.

One of the following:

String

double

boolean

Optional<[FileChunkingStrategy](/api/reference/java/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20file_chunking_strategy%20%3E%20(schema))> chunkingStrategy

The strategy used to chunk the file.

One of the following:

class StaticFileChunkingStrategyObject:

[StaticFileChunkingStrategy](/api/reference/java/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy%20%3E%20(schema)) static\_

long chunkOverlapTokens

The number of tokens that overlap between chunks. The default value is `400`.

Note that the overlap must not exceed half of `max_chunk_size_tokens`.

long maxChunkSizeTokens

The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

minimum100

maximum4096

JsonValue; type "static"constant"static"constant

Always `static`.

class OtherFileChunkingStrategyObject:

This is returned when the chunking strategy is unknown. Typically, this is because the file was indexed before the `chunking_strategy` concept was introduced in the API.

JsonValue; type "other"constant"other"constant

Always `other`.

### List vector store files in a batch

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
import com.openai.models.vectorstores.filebatches.FileBatchListFilesPage;
import com.openai.models.vectorstores.filebatches.FileBatchListFilesParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        FileBatchListFilesParams params = FileBatchListFilesParams.builder()
            .vectorStoreId("vector_store_id")
            .batchId("batch_id")
            .build();
        FileBatchListFilesPage page = client.vectorStores().fileBatches().listFiles(params);

  "object": "list",
  "data": [
      "id": "file-abc123",
      "object": "vector_store.file",
      "created_at": 1699061776,
      "vector_store_id": "vs_abc123"
      "id": "file-abc456",
      "object": "vector_store.file",
      "created_at": 1699061776,
      "vector_store_id": "vs_abc123"
  ],
  "first_id": "file-abc123",
  "last_id": "file-abc456",
  "has_more": false

##### Returns Examples

  "object": "list",
  "data": [
      "id": "file-abc123",
      "object": "vector_store.file",
      "created_at": 1699061776,
      "vector_store_id": "vs_abc123"
      "id": "file-abc456",
      "object": "vector_store.file",
      "created_at": 1699061776,
      "vector_store_id": "vs_abc123"
  ],
  "first_id": "file-abc123",
  "last_id": "file-abc456",
  "has_more": false
