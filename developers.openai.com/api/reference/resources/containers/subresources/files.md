<!-- source: https://developers.openai.com/api/reference/resources/containers/subresources/files/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Containers](/api/reference/resources/containers)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Files

##### [List container files](/api/reference/resources/containers/subresources/files/methods/list)

GET/containers/{container\_id}/files

##### [Create container file](/api/reference/resources/containers/subresources/files/methods/create)

POST/containers/{container\_id}/files

##### [Retrieve container file](/api/reference/resources/containers/subresources/files/methods/retrieve)

GET/containers/{container\_id}/files/{file\_id}

##### [Delete a container file](/api/reference/resources/containers/subresources/files/methods/delete)

DELETE/containers/{container\_id}/files/{file\_id}

##### ModelsExpand Collapse

FileListResponse object { id, bytes, container\_id, 4 more }

id: string

Unique identifier for the file.

bytes: number

Size of the file in bytes.

container\_id: string

The container this file belongs to.

created\_at: number

Unix timestamp (in seconds) when the file was created.

formatunixtime

object: string

The type of this object (`container.file`).

path: string

Path of the file in the container.

source: string

Source of the file (e.g., `user`, `assistant`).

FileCreateResponse object { id, bytes, container\_id, 4 more }

id: string

Unique identifier for the file.

bytes: number

Size of the file in bytes.

container\_id: string

The container this file belongs to.

created\_at: number

Unix timestamp (in seconds) when the file was created.

formatunixtime

object: string

The type of this object (`container.file`).

path: string

Path of the file in the container.

source: string

Source of the file (e.g., `user`, `assistant`).

FileRetrieveResponse object { id, bytes, container\_id, 4 more }

id: string

Unique identifier for the file.

bytes: number

Size of the file in bytes.

container\_id: string

The container this file belongs to.

created\_at: number

Unix timestamp (in seconds) when the file was created.

formatunixtime

object: string

The type of this object (`container.file`).

path: string

Path of the file in the container.

source: string

Source of the file (e.g., `user`, `assistant`).

#### FilesContent

##### [Retrieve container file content](/api/reference/resources/containers/subresources/files/subresources/content/methods/retrieve)

GET/containers/{container\_id}/files/{file\_id}/content
