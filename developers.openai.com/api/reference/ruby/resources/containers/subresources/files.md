<!-- source: https://developers.openai.com/api/reference/ruby/resources/containers/subresources/files/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Containers](/api/reference/ruby/resources/containers)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Files

##### [List container files](/api/reference/ruby/resources/containers/subresources/files/methods/list)

containers.files.list(container\_id, \*\*kwargs) -> CursorPage<[FileListResponse](/api/reference/ruby/resources/containers#(resource)%20containers.files%20%3E%20(model)%20file_list_response%20%3E%20(schema)) { id, bytes, container\_id, 4 more } >

GET/containers/{container\_id}/files

##### [Create container file](/api/reference/ruby/resources/containers/subresources/files/methods/create)

containers.files.create(container\_id, \*\*kwargs) -> [FileCreateResponse](/api/reference/ruby/resources/containers#(resource)%20containers.files%20%3E%20(model)%20file_create_response%20%3E%20(schema)) { id, bytes, container\_id, 4 more }

POST/containers/{container\_id}/files

##### [Retrieve container file](/api/reference/ruby/resources/containers/subresources/files/methods/retrieve)

containers.files.retrieve(file\_id, \*\*kwargs) -> [FileRetrieveResponse](/api/reference/ruby/resources/containers#(resource)%20containers.files%20%3E%20(model)%20file_retrieve_response%20%3E%20(schema)) { id, bytes, container\_id, 4 more }

GET/containers/{container\_id}/files/{file\_id}

##### [Delete a container file](/api/reference/ruby/resources/containers/subresources/files/methods/delete)

containers.files.delete(file\_id, \*\*kwargs) -> void

DELETE/containers/{container\_id}/files/{file\_id}

##### ModelsExpand Collapse

class FileListResponse { id, bytes, container\_id, 4 more }

id: String

Unique identifier for the file.

bytes: Integer

Size of the file in bytes.

container\_id: String

The container this file belongs to.

created\_at: Integer

Unix timestamp (in seconds) when the file was created.

formatunixtime

object: :"container.file"

The type of this object (`container.file`).

path: String

Path of the file in the container.

source: String

Source of the file (e.g., `user`, `assistant`).

class FileCreateResponse { id, bytes, container\_id, 4 more }

id: String

Unique identifier for the file.

bytes: Integer

Size of the file in bytes.

container\_id: String

The container this file belongs to.

created\_at: Integer

Unix timestamp (in seconds) when the file was created.

formatunixtime

object: :"container.file"

The type of this object (`container.file`).

path: String

Path of the file in the container.

source: String

Source of the file (e.g., `user`, `assistant`).

class FileRetrieveResponse { id, bytes, container\_id, 4 more }

id: String

Unique identifier for the file.

bytes: Integer

Size of the file in bytes.

container\_id: String

The container this file belongs to.

created\_at: Integer

Unix timestamp (in seconds) when the file was created.

formatunixtime

object: :"container.file"

The type of this object (`container.file`).

path: String

Path of the file in the container.

source: String

Source of the file (e.g., `user`, `assistant`).

#### FilesContent

##### [Retrieve container file content](/api/reference/ruby/resources/containers/subresources/files/subresources/content/methods/retrieve)

containers.files.content.retrieve(file\_id, \*\*kwargs) -> StringIO

GET/containers/{container\_id}/files/{file\_id}/content
