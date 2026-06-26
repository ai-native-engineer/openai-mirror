<!-- source: https://developers.openai.com/api/reference/python/resources/containers/subresources/files/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Containers](/api/reference/python/resources/containers)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Files

##### [List container files](/api/reference/python/resources/containers/subresources/files/methods/list)

containers.files.list(strcontainer\_id, FileListParams\*\*kwargs)  -> SyncCursorPage[[FileListResponse](/api/reference/python/resources/containers#(resource)%20containers.files%20%3E%20(model)%20file_list_response%20%3E%20(schema))]

GET/containers/{container\_id}/files

##### [Create container file](/api/reference/python/resources/containers/subresources/files/methods/create)

containers.files.create(strcontainer\_id, FileCreateParams\*\*kwargs)  -> [FileCreateResponse](/api/reference/python/resources/containers#(resource)%20containers.files%20%3E%20(model)%20file_create_response%20%3E%20(schema))

POST/containers/{container\_id}/files

##### [Retrieve container file](/api/reference/python/resources/containers/subresources/files/methods/retrieve)

containers.files.retrieve(strfile\_id, FileRetrieveParams\*\*kwargs)  -> [FileRetrieveResponse](/api/reference/python/resources/containers#(resource)%20containers.files%20%3E%20(model)%20file_retrieve_response%20%3E%20(schema))

GET/containers/{container\_id}/files/{file\_id}

##### [Delete a container file](/api/reference/python/resources/containers/subresources/files/methods/delete)

containers.files.delete(strfile\_id, FileDeleteParams\*\*kwargs)

DELETE/containers/{container\_id}/files/{file\_id}

##### ModelsExpand Collapse

class FileListResponse: …

id: str

Unique identifier for the file.

bytes: int

Size of the file in bytes.

container\_id: str

The container this file belongs to.

created\_at: int

Unix timestamp (in seconds) when the file was created.

formatunixtime

object: Literal["container.file"]

The type of this object (`container.file`).

path: str

Path of the file in the container.

source: str

Source of the file (e.g., `user`, `assistant`).

class FileCreateResponse: …

id: str

Unique identifier for the file.

bytes: int

Size of the file in bytes.

container\_id: str

The container this file belongs to.

created\_at: int

Unix timestamp (in seconds) when the file was created.

formatunixtime

object: Literal["container.file"]

The type of this object (`container.file`).

path: str

Path of the file in the container.

source: str

Source of the file (e.g., `user`, `assistant`).

class FileRetrieveResponse: …

id: str

Unique identifier for the file.

bytes: int

Size of the file in bytes.

container\_id: str

The container this file belongs to.

created\_at: int

Unix timestamp (in seconds) when the file was created.

formatunixtime

object: Literal["container.file"]

The type of this object (`container.file`).

path: str

Path of the file in the container.

source: str

Source of the file (e.g., `user`, `assistant`).

#### FilesContent

##### [Retrieve container file content](/api/reference/python/resources/containers/subresources/files/subresources/content/methods/retrieve)

containers.files.content.retrieve(strfile\_id, ContentRetrieveParams\*\*kwargs)  -> BinaryResponseContent

GET/containers/{container\_id}/files/{file\_id}/content
