<!-- source: https://developers.openai.com/api/reference/ruby/resources/vector_stores/subresources/files/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Vector Stores](/api/reference/ruby/resources/vector_stores)

[Files](/api/reference/ruby/resources/vector_stores/subresources/files)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve vector store file

vector\_stores.files.retrieve(file\_id, \*\*kwargs) -> [VectorStoreFile](/api/reference/ruby/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema)) { id, created\_at, last\_error, 6 more }

GET/vector\_stores/{vector\_store\_id}/files/{file\_id}

Retrieves a vector store file.

##### ParametersExpand Collapse

vector\_store\_id: String

file\_id: String

##### ReturnsExpand Collapse

class VectorStoreFile { id, created\_at, last\_error, 6 more }

A list of files attached to a vector store.

id: String

The identifier, which can be referenced in API endpoints.

created\_at: Integer

The Unix timestamp (in seconds) for when the vector store file was created.

formatunixtime

last\_error: LastError{ code, message}

The last error associated with this vector store file. Will be `null` if there are no errors.

code: :server\_error | :unsupported\_file | :invalid\_file

One of `server_error`, `unsupported_file`, or `invalid_file`.

One of the following:

:server\_error

:unsupported\_file

:invalid\_file

message: String

A human-readable description of the error.

object: :"vector\_store.file"

The object type, which is always `vector_store.file`.

status: :in\_progress | :completed | :cancelled | :failed

The status of the vector store file, which can be either `in_progress`, `completed`, `cancelled`, or `failed`. The status `completed` indicates that the vector store file is ready for use.

One of the following:

:in\_progress

:completed

:cancelled

:failed

usage\_bytes: Integer

The total vector store usage in bytes. Note that this may be different from the original file size.

vector\_store\_id: String

The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) that the [File](https://platform.openai.com/docs/api-reference/files) is attached to.

attributes: Hash[Symbol, String | Float | bool]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.

One of the following:

String = String

Float = Float

UnionMember2 = bool

chunking\_strategy: [FileChunkingStrategy](/api/reference/ruby/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20file_chunking_strategy%20%3E%20(schema))

The strategy used to chunk the file.

One of the following:

class StaticFileChunkingStrategyObject { static, type }

static: [StaticFileChunkingStrategy](/api/reference/ruby/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy%20%3E%20(schema)) { chunk\_overlap\_tokens, max\_chunk\_size\_tokens }

chunk\_overlap\_tokens: Integer

The number of tokens that overlap between chunks. The default value is `400`.

Note that the overlap must not exceed half of `max_chunk_size_tokens`.

max\_chunk\_size\_tokens: Integer

The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

minimum100

maximum4096

type: :static

Always `static`.

class OtherFileChunkingStrategyObject { type }

This is returned when the chunking strategy is unknown. Typically, this is because the file was indexed before the `chunking_strategy` concept was introduced in the API.

type: :other

Always `other`.

### Retrieve vector store file

Ruby

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

vector_store_file = openai.vector_stores.files.retrieve("file-abc123", vector_store_id: "vs_abc123")

puts(vector_store_file)

  "id": "file-abc123",
  "object": "vector_store.file",
  "created_at": 1699061776,
  "vector_store_id": "vs_abcd",
  "status": "completed",
  "last_error": null

##### Returns Examples

  "id": "file-abc123",
  "object": "vector_store.file",
  "created_at": 1699061776,
  "vector_store_id": "vs_abcd",
  "status": "completed",
  "last_error": null
