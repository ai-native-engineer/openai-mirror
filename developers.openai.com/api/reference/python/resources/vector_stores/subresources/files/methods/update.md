<!-- source: https://developers.openai.com/api/reference/python/resources/vector_stores/subresources/files/methods/update/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Vector Stores](/api/reference/python/resources/vector_stores)

[Files](/api/reference/python/resources/vector_stores/subresources/files)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Update vector store file attributes

vector\_stores.files.update(strfile\_id, FileUpdateParams\*\*kwargs)  -> [VectorStoreFile](/api/reference/python/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema))

POST/vector\_stores/{vector\_store\_id}/files/{file\_id}

Update attributes on a vector store file.

##### ParametersExpand Collapse

vector\_store\_id: str

file\_id: str

attributes: Optional[Dict[str, Union[str, float, bool]]]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.

One of the following:

str

float

bool

##### ReturnsExpand Collapse

class VectorStoreFile: …

A list of files attached to a vector store.

id: str

The identifier, which can be referenced in API endpoints.

created\_at: int

The Unix timestamp (in seconds) for when the vector store file was created.

formatunixtime

last\_error: Optional[LastError]

The last error associated with this vector store file. Will be `null` if there are no errors.

code: Literal["server\_error", "unsupported\_file", "invalid\_file"]

One of `server_error`, `unsupported_file`, or `invalid_file`.

One of the following:

"server\_error"

"unsupported\_file"

"invalid\_file"

message: str

A human-readable description of the error.

object: Literal["vector\_store.file"]

The object type, which is always `vector_store.file`.

status: Literal["in\_progress", "completed", "cancelled", "failed"]

The status of the vector store file, which can be either `in_progress`, `completed`, `cancelled`, or `failed`. The status `completed` indicates that the vector store file is ready for use.

One of the following:

"in\_progress"

"completed"

"cancelled"

"failed"

usage\_bytes: int

The total vector store usage in bytes. Note that this may be different from the original file size.

vector\_store\_id: str

The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) that the [File](https://platform.openai.com/docs/api-reference/files) is attached to.

attributes: Optional[Dict[str, Union[str, float, bool]]]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.

One of the following:

str

float

bool

chunking\_strategy: Optional[FileChunkingStrategy]

The strategy used to chunk the file.

One of the following:

class StaticFileChunkingStrategyObject: …

static: [StaticFileChunkingStrategy](/api/reference/python/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy%20%3E%20(schema))

chunk\_overlap\_tokens: int

The number of tokens that overlap between chunks. The default value is `400`.

Note that the overlap must not exceed half of `max_chunk_size_tokens`.

max\_chunk\_size\_tokens: int

The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

minimum100

maximum4096

type: Literal["static"]

Always `static`.

class OtherFileChunkingStrategyObject: …

This is returned when the chunking strategy is unknown. Typically, this is because the file was indexed before the `chunking_strategy` concept was introduced in the API.

type: Literal["other"]

Always `other`.

### Update vector store file attributes

Python

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
vector_store_file = client.vector_stores.files.update(
    file_id="file-abc123",
    vector_store_id="vs_abc123",
    attributes={
        "foo": "string"
print(vector_store_file.id)

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
