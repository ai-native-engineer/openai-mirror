<!-- source: https://developers.openai.com/api/reference/java/resources/vector_stores/subresources/files/methods/update/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Vector Stores](/api/reference/java/resources/vector_stores)

[Files](/api/reference/java/resources/vector_stores/subresources/files)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Update vector store file attributes

[VectorStoreFile](/api/reference/java/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema)) vectorStores().files().update(FileUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/vector\_stores/{vector\_store\_id}/files/{file\_id}

Update attributes on a vector store file.

##### ParametersExpand Collapse

FileUpdateParams params

String vectorStoreId

Optional<String> fileId

Optional<Attributes> attributes

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.

String

double

boolean

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

### Update vector store file attributes

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
import com.openai.core.JsonValue;
import com.openai.models.vectorstores.files.FileUpdateParams;
import com.openai.models.vectorstores.files.VectorStoreFile;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        FileUpdateParams params = FileUpdateParams.builder()
            .vectorStoreId("vs_abc123")
            .fileId("file-abc123")
            .attributes(FileUpdateParams.Attributes.builder()
                .putAdditionalProperty("foo", JsonValue.from("string"))
                .build())
            .build();
        VectorStoreFile vectorStoreFile = client.vectorStores().files().update(params);

  "id": "file-abc123",
  "object": "vector_store.file",
  "usage_bytes": 1234,
  "created_at": 1699061776,
  "vector_store_id": "vs_abcd",
  "status": "completed",
  "last_error": null,
  "chunking_strategy": {...},
  "attributes": {"key1": "value1", "key2": 2}

##### Returns Examples

  "id": "file-abc123",
  "object": "vector_store.file",
  "usage_bytes": 1234,
  "created_at": 1699061776,
  "vector_store_id": "vs_abcd",
  "status": "completed",
  "last_error": null,
  "chunking_strategy": {...},
  "attributes": {"key1": "value1", "key2": 2}
