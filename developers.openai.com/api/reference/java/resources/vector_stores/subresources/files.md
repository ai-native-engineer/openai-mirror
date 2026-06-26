<!-- source: https://developers.openai.com/api/reference/java/resources/vector_stores/subresources/files/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Vector Stores](/api/reference/java/resources/vector_stores)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Files

##### [List vector store files](/api/reference/java/resources/vector_stores/subresources/files/methods/list)

FileListPage vectorStores().files().list(FileListParamsparams = FileListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/vector\_stores/{vector\_store\_id}/files

##### [Create vector store file](/api/reference/java/resources/vector_stores/subresources/files/methods/create)

[VectorStoreFile](/api/reference/java/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema)) vectorStores().files().create(FileCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/vector\_stores/{vector\_store\_id}/files

##### [Update vector store file attributes](/api/reference/java/resources/vector_stores/subresources/files/methods/update)

[VectorStoreFile](/api/reference/java/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema)) vectorStores().files().update(FileUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/vector\_stores/{vector\_store\_id}/files/{file\_id}

##### [Retrieve vector store file](/api/reference/java/resources/vector_stores/subresources/files/methods/retrieve)

[VectorStoreFile](/api/reference/java/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema)) vectorStores().files().retrieve(FileRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/vector\_stores/{vector\_store\_id}/files/{file\_id}

##### [Delete vector store file](/api/reference/java/resources/vector_stores/subresources/files/methods/delete)

[VectorStoreFileDeleted](/api/reference/java/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file_deleted%20%3E%20(schema)) vectorStores().files().delete(FileDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

DELETE/vector\_stores/{vector\_store\_id}/files/{file\_id}

##### [Retrieve vector store file content](/api/reference/java/resources/vector_stores/subresources/files/methods/content)

FileContentPage vectorStores().files().content(FileContentParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/vector\_stores/{vector\_store\_id}/files/{file\_id}/content

##### ModelsExpand Collapse

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

class VectorStoreFileDeleted:

String id

boolean deleted

JsonValue; object\_ "vector\_store.file.deleted"constant"vector\_store.file.deleted"constant
