<!-- source: https://developers.openai.com/api/reference/go/resources/vector_stores/subresources/files/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Vector Stores](/api/reference/go/resources/vector_stores)

[Files](/api/reference/go/resources/vector_stores/subresources/files)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List vector store files

client.VectorStores.Files.List(ctx, vectorStoreID, query) (\*CursorPage[[VectorStoreFile](/api/reference/go/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema))], error)

GET/vector\_stores/{vector\_store\_id}/files

Returns a list of vector store files.

##### ParametersExpand Collapse

vectorStoreID string

query VectorStoreFileListParams

After param.Field[string]Optional

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

Before param.Field[string]Optional

A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with obj\_foo, your subsequent call can include before=obj\_foo in order to fetch the previous page of the list.

Filter param.Field[[VectorStoreFileListParamsFilter](/api/reference/go/resources/vector_stores/subresources/files/methods/list#(resource)%20vector_stores.files%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20filter%20%3E%20(schema))]Optional

Filter by file status. One of `in_progress`, `completed`, `failed`, `cancelled`.

const VectorStoreFileListParamsFilterInProgress [VectorStoreFileListParamsFilter](/api/reference/go/resources/vector_stores/subresources/files/methods/list#(resource)%20vector_stores.files%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20filter%20%3E%20(schema)) = "in\_progress"

const VectorStoreFileListParamsFilterCompleted [VectorStoreFileListParamsFilter](/api/reference/go/resources/vector_stores/subresources/files/methods/list#(resource)%20vector_stores.files%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20filter%20%3E%20(schema)) = "completed"

const VectorStoreFileListParamsFilterFailed [VectorStoreFileListParamsFilter](/api/reference/go/resources/vector_stores/subresources/files/methods/list#(resource)%20vector_stores.files%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20filter%20%3E%20(schema)) = "failed"

const VectorStoreFileListParamsFilterCancelled [VectorStoreFileListParamsFilter](/api/reference/go/resources/vector_stores/subresources/files/methods/list#(resource)%20vector_stores.files%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20filter%20%3E%20(schema)) = "cancelled"

Limit param.Field[int64]Optional

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

Order param.Field[[VectorStoreFileListParamsOrder](/api/reference/go/resources/vector_stores/subresources/files/methods/list#(resource)%20vector_stores.files%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))]Optional

Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

const VectorStoreFileListParamsOrderAsc [VectorStoreFileListParamsOrder](/api/reference/go/resources/vector_stores/subresources/files/methods/list#(resource)%20vector_stores.files%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)) = "asc"

const VectorStoreFileListParamsOrderDesc [VectorStoreFileListParamsOrder](/api/reference/go/resources/vector_stores/subresources/files/methods/list#(resource)%20vector_stores.files%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)) = "desc"

##### ReturnsExpand Collapse

type VectorStoreFile struct{…}

A list of files attached to a vector store.

ID string

The identifier, which can be referenced in API endpoints.

CreatedAt int64

The Unix timestamp (in seconds) for when the vector store file was created.

formatunixtime

LastError VectorStoreFileLastError

The last error associated with this vector store file. Will be `null` if there are no errors.

Code string

One of `server_error`, `unsupported_file`, or `invalid_file`.

One of the following:

const VectorStoreFileLastErrorCodeServerError VectorStoreFileLastErrorCode = "server\_error"

const VectorStoreFileLastErrorCodeUnsupportedFile VectorStoreFileLastErrorCode = "unsupported\_file"

const VectorStoreFileLastErrorCodeInvalidFile VectorStoreFileLastErrorCode = "invalid\_file"

Message string

A human-readable description of the error.

Object VectorStoreFile

The object type, which is always `vector_store.file`.

Status VectorStoreFileStatus

The status of the vector store file, which can be either `in_progress`, `completed`, `cancelled`, or `failed`. The status `completed` indicates that the vector store file is ready for use.

One of the following:

const VectorStoreFileStatusInProgress VectorStoreFileStatus = "in\_progress"

const VectorStoreFileStatusCompleted VectorStoreFileStatus = "completed"

const VectorStoreFileStatusCancelled VectorStoreFileStatus = "cancelled"

const VectorStoreFileStatusFailed VectorStoreFileStatus = "failed"

UsageBytes int64

The total vector store usage in bytes. Note that this may be different from the original file size.

VectorStoreID string

The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) that the [File](https://platform.openai.com/docs/api-reference/files) is attached to.

Attributes map[string, VectorStoreFileAttributeUnion]Optional

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.

One of the following:

string

float64

bool

ChunkingStrategy [FileChunkingStrategyUnion](/api/reference/go/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20file_chunking_strategy%20%3E%20(schema))Optional

The strategy used to chunk the file.

One of the following:

type StaticFileChunkingStrategyObject struct{…}

Static [StaticFileChunkingStrategy](/api/reference/go/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy%20%3E%20(schema))

ChunkOverlapTokens int64

The number of tokens that overlap between chunks. The default value is `400`.

Note that the overlap must not exceed half of `max_chunk_size_tokens`.

MaxChunkSizeTokens int64

The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

minimum100

maximum4096

Type Static

Always `static`.

type OtherFileChunkingStrategyObject struct{…}

This is returned when the chunking strategy is unknown. Typically, this is because the file was indexed before the `chunking_strategy` concept was introduced in the API.

Type Other

Always `other`.

### List vector store files

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
  page, err := client.VectorStores.Files.List(
    context.TODO(),
    "vector_store_id",
    openai.VectorStoreFileListParams{

  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", page)

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
