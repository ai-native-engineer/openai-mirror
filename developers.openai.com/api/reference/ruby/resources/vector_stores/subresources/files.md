<!-- source: https://developers.openai.com/api/reference/ruby/resources/vector_stores/subresources/files/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Vector Stores](/api/reference/ruby/resources/vector_stores)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Files

##### [List vector store files](/api/reference/ruby/resources/vector_stores/subresources/files/methods/list)

vector\_stores.files.list(vector\_store\_id, \*\*kwargs) -> CursorPage<[VectorStoreFile](/api/reference/ruby/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema)) { id, created\_at, last\_error, 6 more } >

GET/vector\_stores/{vector\_store\_id}/files

##### [Create vector store file](/api/reference/ruby/resources/vector_stores/subresources/files/methods/create)

vector\_stores.files.create(vector\_store\_id, \*\*kwargs) -> [VectorStoreFile](/api/reference/ruby/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema)) { id, created\_at, last\_error, 6 more }

POST/vector\_stores/{vector\_store\_id}/files

##### [Update vector store file attributes](/api/reference/ruby/resources/vector_stores/subresources/files/methods/update)

vector\_stores.files.update(file\_id, \*\*kwargs) -> [VectorStoreFile](/api/reference/ruby/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema)) { id, created\_at, last\_error, 6 more }

POST/vector\_stores/{vector\_store\_id}/files/{file\_id}

##### [Retrieve vector store file](/api/reference/ruby/resources/vector_stores/subresources/files/methods/retrieve)

vector\_stores.files.retrieve(file\_id, \*\*kwargs) -> [VectorStoreFile](/api/reference/ruby/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema)) { id, created\_at, last\_error, 6 more }

GET/vector\_stores/{vector\_store\_id}/files/{file\_id}

##### [Delete vector store file](/api/reference/ruby/resources/vector_stores/subresources/files/methods/delete)

vector\_stores.files.delete(file\_id, \*\*kwargs) -> [VectorStoreFileDeleted](/api/reference/ruby/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file_deleted%20%3E%20(schema)) { id, deleted, object }

DELETE/vector\_stores/{vector\_store\_id}/files/{file\_id}

##### [Retrieve vector store file content](/api/reference/ruby/resources/vector_stores/subresources/files/methods/content)

vector\_stores.files.content(file\_id, \*\*kwargs) -> Page<[FileContentResponse](/api/reference/ruby/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20file_content_response%20%3E%20(schema)) { text, type } >

GET/vector\_stores/{vector\_store\_id}/files/{file\_id}/content

##### ModelsExpand Collapse

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

class VectorStoreFileDeleted { id, deleted, object }

id: String

deleted: bool

object: :"vector\_store.file.deleted"

class FileContentResponse { text, type }

text: String

The text content

type: String

The content type (currently only `"text"`)
