<!-- source: https://developers.openai.com/api/reference/typescript/resources/containers/subresources/files/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Containers](/api/reference/typescript/resources/containers)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Files

##### [List container files](/api/reference/typescript/resources/containers/subresources/files/methods/list)

client.containers.files.list(stringcontainerID, FileListParams { after, limit, order } query?, RequestOptionsoptions?): CursorPage<[FileListResponse](/api/reference/typescript/resources/containers#(resource)%20containers.files%20%3E%20(model)%20file_list_response%20%3E%20(schema)) { id, bytes, container\_id, 4 more } >

GET/containers/{container\_id}/files

##### [Create container file](/api/reference/typescript/resources/containers/subresources/files/methods/create)

client.containers.files.create(stringcontainerID, FileCreateParams { file, file\_id } body, RequestOptionsoptions?): [FileCreateResponse](/api/reference/typescript/resources/containers#(resource)%20containers.files%20%3E%20(model)%20file_create_response%20%3E%20(schema)) { id, bytes, container\_id, 4 more }

POST/containers/{container\_id}/files

##### [Retrieve container file](/api/reference/typescript/resources/containers/subresources/files/methods/retrieve)

client.containers.files.retrieve(stringfileID, FileRetrieveParams { container\_id } params, RequestOptionsoptions?): [FileRetrieveResponse](/api/reference/typescript/resources/containers#(resource)%20containers.files%20%3E%20(model)%20file_retrieve_response%20%3E%20(schema)) { id, bytes, container\_id, 4 more }

GET/containers/{container\_id}/files/{file\_id}

##### [Delete a container file](/api/reference/typescript/resources/containers/subresources/files/methods/delete)

client.containers.files.delete(stringfileID, FileDeleteParams { container\_id } params, RequestOptionsoptions?): void

DELETE/containers/{container\_id}/files/{file\_id}

##### ModelsExpand Collapse

FileListResponse { id, bytes, container\_id, 4 more }

id: string

Unique identifier for the file.

bytes: number

Size of the file in bytes.

container\_id: string

The container this file belongs to.

created\_at: number

Unix timestamp (in seconds) when the file was created.

formatunixtime

object: "container.file"

The type of this object (`container.file`).

path: string

Path of the file in the container.

source: string

Source of the file (e.g., `user`, `assistant`).

FileCreateResponse { id, bytes, container\_id, 4 more }

id: string

Unique identifier for the file.

bytes: number

Size of the file in bytes.

container\_id: string

The container this file belongs to.

created\_at: number

Unix timestamp (in seconds) when the file was created.

formatunixtime

object: "container.file"

The type of this object (`container.file`).

path: string

Path of the file in the container.

source: string

Source of the file (e.g., `user`, `assistant`).

FileRetrieveResponse { id, bytes, container\_id, 4 more }

id: string

Unique identifier for the file.

bytes: number

Size of the file in bytes.

container\_id: string

The container this file belongs to.

created\_at: number

Unix timestamp (in seconds) when the file was created.

formatunixtime

object: "container.file"

The type of this object (`container.file`).

path: string

Path of the file in the container.

source: string

Source of the file (e.g., `user`, `assistant`).

#### FilesContent

##### [Retrieve container file content](/api/reference/typescript/resources/containers/subresources/files/subresources/content/methods/retrieve)

client.containers.files.content.retrieve(stringfileID, ContentRetrieveParams { container\_id } params, RequestOptionsoptions?): Response

GET/containers/{container\_id}/files/{file\_id}/content
