<!-- source: https://developers.openai.com/api/reference/resources/vector_stores/subresources/file_batches/methods/list_files/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Vector Stores](/api/reference/resources/vector_stores)

[File Batches](/api/reference/resources/vector_stores/subresources/file_batches)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List vector store files in a batch

GET/vector\_stores/{vector\_store\_id}/file\_batches/{batch\_id}/files

Returns a list of vector store files in a batch.

##### Path ParametersExpand Collapse

vector\_store\_id: string

batch\_id: string

##### Query ParametersExpand Collapse

after: optional string

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

before: optional string

A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with obj\_foo, your subsequent call can include before=obj\_foo in order to fetch the previous page of the list.

filter: optional "in\_progress" or "completed" or "failed" or "cancelled"

Filter by file status. One of `in_progress`, `completed`, `failed`, `cancelled`.

One of the following:

"in\_progress"

"completed"

"failed"

"cancelled"

limit: optional number

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

order: optional "asc" or "desc"

Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

One of the following:

"asc"

"desc"

##### ReturnsExpand Collapse

data: array of [VectorStoreFile](/api/reference/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema)) { id, created\_at, last\_error, 6 more }

id: string

The identifier, which can be referenced in API endpoints.

created\_at: number

The Unix timestamp (in seconds) for when the vector store file was created.

formatunixtime

last\_error: object { code, message }

The last error associated with this vector store file. Will be `null` if there are no errors.

code: "server\_error" or "unsupported\_file" or "invalid\_file"

One of `server_error`, `unsupported_file`, or `invalid_file`.

One of the following:

"server\_error"

"unsupported\_file"

"invalid\_file"

message: string

A human-readable description of the error.

object: "vector\_store.file"

The object type, which is always `vector_store.file`.

status: "in\_progress" or "completed" or "cancelled" or "failed"

The status of the vector store file, which can be either `in_progress`, `completed`, `cancelled`, or `failed`. The status `completed` indicates that the vector store file is ready for use.

One of the following:

"in\_progress"

"completed"

"cancelled"

"failed"

usage\_bytes: number

The total vector store usage in bytes. Note that this may be different from the original file size.

vector\_store\_id: string

The ID of the [vector store](/docs/api-reference/vector-stores/object) that the [File](/docs/api-reference/files) is attached to.

attributes: optional map[string or number or boolean]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.

One of the following:

string

number

boolean

chunking\_strategy: optional [StaticFileChunkingStrategyObject](/api/reference/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy_object%20%3E%20(schema)) { static, type }  or [OtherFileChunkingStrategyObject](/api/reference/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20other_file_chunking_strategy_object%20%3E%20(schema)) { type }

The strategy used to chunk the file.

One of the following:

StaticFileChunkingStrategyObject object { static, type }

static: [StaticFileChunkingStrategy](/api/reference/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy%20%3E%20(schema)) { chunk\_overlap\_tokens, max\_chunk\_size\_tokens }

chunk\_overlap\_tokens: number

The number of tokens that overlap between chunks. The default value is `400`.

Note that the overlap must not exceed half of `max_chunk_size_tokens`.

max\_chunk\_size\_tokens: number

The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

minimum100

maximum4096

type: "static"

Always `static`.

OtherFileChunkingStrategyObject object { type }

This is returned when the chunking strategy is unknown. Typically, this is because the file was indexed before the `chunking_strategy` concept was introduced in the API.

type: "other"

Always `other`.

first\_id: string

has\_more: boolean

last\_id: string

object: string

### List vector store files in a batch

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl https://api.openai.com/v1/vector_stores/vs_abc123/files_batches/vsfb_abc123/files \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "OpenAI-Beta: assistants=v2"

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
