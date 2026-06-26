<!-- source: https://developers.openai.com/api/reference/python/resources/containers/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Containers

##### [List containers](/api/reference/python/resources/containers/methods/list)

containers.list(ContainerListParams\*\*kwargs)  -> SyncCursorPage[[ContainerListResponse](/api/reference/python/resources/containers#(resource)%20containers%20%3E%20(model)%20container_list_response%20%3E%20(schema))]

GET/containers

##### [Create container](/api/reference/python/resources/containers/methods/create)

containers.create(ContainerCreateParams\*\*kwargs)  -> [ContainerCreateResponse](/api/reference/python/resources/containers#(resource)%20containers%20%3E%20(model)%20container_create_response%20%3E%20(schema))

POST/containers

##### [Retrieve container](/api/reference/python/resources/containers/methods/retrieve)

containers.retrieve(strcontainer\_id)  -> [ContainerRetrieveResponse](/api/reference/python/resources/containers#(resource)%20containers%20%3E%20(model)%20container_retrieve_response%20%3E%20(schema))

GET/containers/{container\_id}

##### [Delete a container](/api/reference/python/resources/containers/methods/delete)

containers.delete(strcontainer\_id)

DELETE/containers/{container\_id}

##### ModelsExpand Collapse

class ContainerListResponse: …

id: str

Unique identifier for the container.

created\_at: int

Unix timestamp (in seconds) when the container was created.

formatunixtime

name: str

Name of the container.

object: str

The type of this object.

status: str

Status of the container (e.g., active, deleted).

expires\_after: Optional[ExpiresAfter]

The container will expire after this time period.
The anchor is the reference point for the expiration.
The minutes is the number of minutes after the anchor before the container expires.

anchor: Optional[Literal["last\_active\_at"]]

The reference point for the expiration.

minutes: Optional[int]

The number of minutes after the anchor before the container expires.

last\_active\_at: Optional[int]

Unix timestamp (in seconds) when the container was last active.

formatunixtime

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

The memory limit configured for the container.

One of the following:

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

Network access policy for the container.

type: Literal["allowlist", "disabled"]

The network policy mode.

One of the following:

"allowlist"

"disabled"

allowed\_domains: Optional[List[str]]

Allowed outbound domains when `type` is `allowlist`.

class ContainerCreateResponse: …

id: str

Unique identifier for the container.

created\_at: int

Unix timestamp (in seconds) when the container was created.

formatunixtime

name: str

Name of the container.

object: str

The type of this object.

status: str

Status of the container (e.g., active, deleted).

expires\_after: Optional[ExpiresAfter]

The container will expire after this time period.
The anchor is the reference point for the expiration.
The minutes is the number of minutes after the anchor before the container expires.

anchor: Optional[Literal["last\_active\_at"]]

The reference point for the expiration.

minutes: Optional[int]

The number of minutes after the anchor before the container expires.

last\_active\_at: Optional[int]

Unix timestamp (in seconds) when the container was last active.

formatunixtime

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

The memory limit configured for the container.

One of the following:

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

Network access policy for the container.

type: Literal["allowlist", "disabled"]

The network policy mode.

One of the following:

"allowlist"

"disabled"

allowed\_domains: Optional[List[str]]

Allowed outbound domains when `type` is `allowlist`.

class ContainerRetrieveResponse: …

id: str

Unique identifier for the container.

created\_at: int

Unix timestamp (in seconds) when the container was created.

formatunixtime

name: str

Name of the container.

object: str

The type of this object.

status: str

Status of the container (e.g., active, deleted).

expires\_after: Optional[ExpiresAfter]

The container will expire after this time period.
The anchor is the reference point for the expiration.
The minutes is the number of minutes after the anchor before the container expires.

anchor: Optional[Literal["last\_active\_at"]]

The reference point for the expiration.

minutes: Optional[int]

The number of minutes after the anchor before the container expires.

last\_active\_at: Optional[int]

Unix timestamp (in seconds) when the container was last active.

formatunixtime

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

The memory limit configured for the container.

One of the following:

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

Network access policy for the container.

type: Literal["allowlist", "disabled"]

The network policy mode.

One of the following:

"allowlist"

"disabled"

allowed\_domains: Optional[List[str]]

Allowed outbound domains when `type` is `allowlist`.

#### ContainersFiles

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

#### ContainersFilesContent

##### [Retrieve container file content](/api/reference/python/resources/containers/subresources/files/subresources/content/methods/retrieve)

containers.files.content.retrieve(strfile\_id, ContentRetrieveParams\*\*kwargs)  -> BinaryResponseContent

GET/containers/{container\_id}/files/{file\_id}/content
