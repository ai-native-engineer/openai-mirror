<!-- source: https://developers.openai.com/api/reference/ruby/resources/containers/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Containers

##### [List containers](/api/reference/ruby/resources/containers/methods/list)

containers.list(\*\*kwargs) -> CursorPage<[ContainerListResponse](/api/reference/ruby/resources/containers#(resource)%20containers%20%3E%20(model)%20container_list_response%20%3E%20(schema)) { id, created\_at, name, 6 more } >

GET/containers

##### [Create container](/api/reference/ruby/resources/containers/methods/create)

containers.create(\*\*kwargs) -> [ContainerCreateResponse](/api/reference/ruby/resources/containers#(resource)%20containers%20%3E%20(model)%20container_create_response%20%3E%20(schema)) { id, created\_at, name, 6 more }

POST/containers

##### [Retrieve container](/api/reference/ruby/resources/containers/methods/retrieve)

containers.retrieve(container\_id) -> [ContainerRetrieveResponse](/api/reference/ruby/resources/containers#(resource)%20containers%20%3E%20(model)%20container_retrieve_response%20%3E%20(schema)) { id, created\_at, name, 6 more }

GET/containers/{container\_id}

##### [Delete a container](/api/reference/ruby/resources/containers/methods/delete)

containers.delete(container\_id) -> void

DELETE/containers/{container\_id}

##### ModelsExpand Collapse

class ContainerListResponse { id, created\_at, name, 6 more }

id: String

Unique identifier for the container.

created\_at: Integer

Unix timestamp (in seconds) when the container was created.

formatunixtime

name: String

Name of the container.

object: String

The type of this object.

status: String

Status of the container (e.g., active, deleted).

expires\_after: ExpiresAfter{ anchor, minutes}

The container will expire after this time period.
The anchor is the reference point for the expiration.
The minutes is the number of minutes after the anchor before the container expires.

anchor: :last\_active\_at

The reference point for the expiration.

minutes: Integer

The number of minutes after the anchor before the container expires.

last\_active\_at: Integer

Unix timestamp (in seconds) when the container was last active.

formatunixtime

memory\_limit: :"1g" | :"4g" | :"16g" | :"64g"

The memory limit configured for the container.

One of the following:

:"1g"

:"4g"

:"16g"

:"64g"

network\_policy: NetworkPolicy{ type, allowed\_domains}

Network access policy for the container.

type: :allowlist | :disabled

The network policy mode.

One of the following:

:allowlist

:disabled

allowed\_domains: Array[String]

Allowed outbound domains when `type` is `allowlist`.

class ContainerCreateResponse { id, created\_at, name, 6 more }

id: String

Unique identifier for the container.

created\_at: Integer

Unix timestamp (in seconds) when the container was created.

formatunixtime

name: String

Name of the container.

object: String

The type of this object.

status: String

Status of the container (e.g., active, deleted).

expires\_after: ExpiresAfter{ anchor, minutes}

The container will expire after this time period.
The anchor is the reference point for the expiration.
The minutes is the number of minutes after the anchor before the container expires.

anchor: :last\_active\_at

The reference point for the expiration.

minutes: Integer

The number of minutes after the anchor before the container expires.

last\_active\_at: Integer

Unix timestamp (in seconds) when the container was last active.

formatunixtime

memory\_limit: :"1g" | :"4g" | :"16g" | :"64g"

The memory limit configured for the container.

One of the following:

:"1g"

:"4g"

:"16g"

:"64g"

network\_policy: NetworkPolicy{ type, allowed\_domains}

Network access policy for the container.

type: :allowlist | :disabled

The network policy mode.

One of the following:

:allowlist

:disabled

allowed\_domains: Array[String]

Allowed outbound domains when `type` is `allowlist`.

class ContainerRetrieveResponse { id, created\_at, name, 6 more }

id: String

Unique identifier for the container.

created\_at: Integer

Unix timestamp (in seconds) when the container was created.

formatunixtime

name: String

Name of the container.

object: String

The type of this object.

status: String

Status of the container (e.g., active, deleted).

expires\_after: ExpiresAfter{ anchor, minutes}

The container will expire after this time period.
The anchor is the reference point for the expiration.
The minutes is the number of minutes after the anchor before the container expires.

anchor: :last\_active\_at

The reference point for the expiration.

minutes: Integer

The number of minutes after the anchor before the container expires.

last\_active\_at: Integer

Unix timestamp (in seconds) when the container was last active.

formatunixtime

memory\_limit: :"1g" | :"4g" | :"16g" | :"64g"

The memory limit configured for the container.

One of the following:

:"1g"

:"4g"

:"16g"

:"64g"

network\_policy: NetworkPolicy{ type, allowed\_domains}

Network access policy for the container.

type: :allowlist | :disabled

The network policy mode.

One of the following:

:allowlist

:disabled

allowed\_domains: Array[String]

Allowed outbound domains when `type` is `allowlist`.

#### ContainersFiles

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

#### ContainersFilesContent

##### [Retrieve container file content](/api/reference/ruby/resources/containers/subresources/files/subresources/content/methods/retrieve)

containers.files.content.retrieve(file\_id, \*\*kwargs) -> StringIO

GET/containers/{container\_id}/files/{file\_id}/content
