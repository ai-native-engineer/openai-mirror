<!-- source: https://developers.openai.com/api/reference/typescript/resources/containers/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Containers

##### [List containers](/api/reference/typescript/resources/containers/methods/list)

client.containers.list(ContainerListParams { after, limit, name, order } query?, RequestOptionsoptions?): CursorPage<[ContainerListResponse](/api/reference/typescript/resources/containers#(resource)%20containers%20%3E%20(model)%20container_list_response%20%3E%20(schema)) { id, created\_at, name, 6 more } >

GET/containers

##### [Create container](/api/reference/typescript/resources/containers/methods/create)

client.containers.create(ContainerCreateParams { name, expires\_after, file\_ids, 3 more } body, RequestOptionsoptions?): [ContainerCreateResponse](/api/reference/typescript/resources/containers#(resource)%20containers%20%3E%20(model)%20container_create_response%20%3E%20(schema)) { id, created\_at, name, 6 more }

POST/containers

##### [Retrieve container](/api/reference/typescript/resources/containers/methods/retrieve)

client.containers.retrieve(stringcontainerID, RequestOptionsoptions?): [ContainerRetrieveResponse](/api/reference/typescript/resources/containers#(resource)%20containers%20%3E%20(model)%20container_retrieve_response%20%3E%20(schema)) { id, created\_at, name, 6 more }

GET/containers/{container\_id}

##### [Delete a container](/api/reference/typescript/resources/containers/methods/delete)

client.containers.delete(stringcontainerID, RequestOptionsoptions?): void

DELETE/containers/{container\_id}

##### ModelsExpand Collapse

ContainerListResponse { id, created\_at, name, 6 more }

id: string

Unique identifier for the container.

created\_at: number

Unix timestamp (in seconds) when the container was created.

formatunixtime

name: string

Name of the container.

object: string

The type of this object.

status: string

Status of the container (e.g., active, deleted).

expires\_after?: ExpiresAfter { anchor, minutes }

The container will expire after this time period.
The anchor is the reference point for the expiration.
The minutes is the number of minutes after the anchor before the container expires.

anchor?: "last\_active\_at"

The reference point for the expiration.

minutes?: number

The number of minutes after the anchor before the container expires.

last\_active\_at?: number

Unix timestamp (in seconds) when the container was last active.

formatunixtime

memory\_limit?: "1g" | "4g" | "16g" | "64g"

The memory limit configured for the container.

One of the following:

"1g"

"4g"

"16g"

"64g"

network\_policy?: NetworkPolicy { type, allowed\_domains }

Network access policy for the container.

type: "allowlist" | "disabled"

The network policy mode.

One of the following:

"allowlist"

"disabled"

allowed\_domains?: Array<string>

Allowed outbound domains when `type` is `allowlist`.

ContainerCreateResponse { id, created\_at, name, 6 more }

id: string

Unique identifier for the container.

created\_at: number

Unix timestamp (in seconds) when the container was created.

formatunixtime

name: string

Name of the container.

object: string

The type of this object.

status: string

Status of the container (e.g., active, deleted).

expires\_after?: ExpiresAfter { anchor, minutes }

The container will expire after this time period.
The anchor is the reference point for the expiration.
The minutes is the number of minutes after the anchor before the container expires.

anchor?: "last\_active\_at"

The reference point for the expiration.

minutes?: number

The number of minutes after the anchor before the container expires.

last\_active\_at?: number

Unix timestamp (in seconds) when the container was last active.

formatunixtime

memory\_limit?: "1g" | "4g" | "16g" | "64g"

The memory limit configured for the container.

One of the following:

"1g"

"4g"

"16g"

"64g"

network\_policy?: NetworkPolicy { type, allowed\_domains }

Network access policy for the container.

type: "allowlist" | "disabled"

The network policy mode.

One of the following:

"allowlist"

"disabled"

allowed\_domains?: Array<string>

Allowed outbound domains when `type` is `allowlist`.

ContainerRetrieveResponse { id, created\_at, name, 6 more }

id: string

Unique identifier for the container.

created\_at: number

Unix timestamp (in seconds) when the container was created.

formatunixtime

name: string

Name of the container.

object: string

The type of this object.

status: string

Status of the container (e.g., active, deleted).

expires\_after?: ExpiresAfter { anchor, minutes }

The container will expire after this time period.
The anchor is the reference point for the expiration.
The minutes is the number of minutes after the anchor before the container expires.

anchor?: "last\_active\_at"

The reference point for the expiration.

minutes?: number

The number of minutes after the anchor before the container expires.

last\_active\_at?: number

Unix timestamp (in seconds) when the container was last active.

formatunixtime

memory\_limit?: "1g" | "4g" | "16g" | "64g"

The memory limit configured for the container.

One of the following:

"1g"

"4g"

"16g"

"64g"

network\_policy?: NetworkPolicy { type, allowed\_domains }

Network access policy for the container.

type: "allowlist" | "disabled"

The network policy mode.

One of the following:

"allowlist"

"disabled"

allowed\_domains?: Array<string>

Allowed outbound domains when `type` is `allowlist`.

#### ContainersFiles

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

#### ContainersFilesContent

##### [Retrieve container file content](/api/reference/typescript/resources/containers/subresources/files/subresources/content/methods/retrieve)

client.containers.files.content.retrieve(stringfileID, ContentRetrieveParams { container\_id } params, RequestOptionsoptions?): Response

GET/containers/{container\_id}/files/{file\_id}/content
