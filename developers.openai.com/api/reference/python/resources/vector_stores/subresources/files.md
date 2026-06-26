<!-- source: https://developers.openai.com/api/reference/python/resources/vector_stores/subresources/files/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Vector Stores](/api/reference/python/resources/vector_stores)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Files

##### [List vector store files](/api/reference/python/resources/vector_stores/subresources/files/methods/list)

vector\_stores.files.list(strvector\_store\_id, FileListParams\*\*kwargs)  -> SyncCursorPage[[VectorStoreFile](/api/reference/python/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema))]

GET/vector\_stores/{vector\_store\_id}/files

##### [Create vector store file](/api/reference/python/resources/vector_stores/subresources/files/methods/create)

vector\_stores.files.create(strvector\_store\_id, FileCreateParams\*\*kwargs)  -> [VectorStoreFile](/api/reference/python/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema))

POST/vector\_stores/{vector\_store\_id}/files

##### [Update vector store file attributes](/api/reference/python/resources/vector_stores/subresources/files/methods/update)

vector\_stores.files.update(strfile\_id, FileUpdateParams\*\*kwargs)  -> [VectorStoreFile](/api/reference/python/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema))

POST/vector\_stores/{vector\_store\_id}/files/{file\_id}

##### [Retrieve vector store file](/api/reference/python/resources/vector_stores/subresources/files/methods/retrieve)

vector\_stores.files.retrieve(strfile\_id, FileRetrieveParams\*\*kwargs)  -> [VectorStoreFile](/api/reference/python/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema))

GET/vector\_stores/{vector\_store\_id}/files/{file\_id}

##### [Delete vector store file](/api/reference/python/resources/vector_stores/subresources/files/methods/delete)

vector\_stores.files.delete(strfile\_id, FileDeleteParams\*\*kwargs)  -> [VectorStoreFileDeleted](/api/reference/python/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file_deleted%20%3E%20(schema))

DELETE/vector\_stores/{vector\_store\_id}/files/{file\_id}

##### [Retrieve vector store file content](/api/reference/python/resources/vector_stores/subresources/files/methods/content)

vector\_stores.files.content(strfile\_id, FileContentParams\*\*kwargs)  -> SyncPage[[FileContentResponse](/api/reference/python/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20file_content_response%20%3E%20(schema))]

GET/vector\_stores/{vector\_store\_id}/files/{file\_id}/content

##### ModelsExpand Collapse

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

class VectorStoreFileDeleted: …

id: str

deleted: bool

object: Literal["vector\_store.file.deleted"]

class FileContentResponse: …

text: Optional[str]

The text content

type: Optional[str]

The content type (currently only `"text"`)
