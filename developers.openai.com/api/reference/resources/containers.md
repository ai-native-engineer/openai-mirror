<!-- source: https://developers.openai.com/api/reference/resources/containers/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Containers

##### [List containers](/api/reference/resources/containers/methods/list)

GET/containers

##### [Create container](/api/reference/resources/containers/methods/create)

POST/containers

##### [Retrieve container](/api/reference/resources/containers/methods/retrieve)

GET/containers/{container\_id}

##### [Delete a container](/api/reference/resources/containers/methods/delete)

DELETE/containers/{container\_id}

##### ModelsExpand Collapse

ContainerListResponse object { id, created\_at, name, 6 more }

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

expires\_after: optional object { anchor, minutes }

The container will expire after this time period.
The anchor is the reference point for the expiration.
The minutes is the number of minutes after the anchor before the container expires.

anchor: optional "last\_active\_at"

The reference point for the expiration.

minutes: optional number

The number of minutes after the anchor before the container expires.

last\_active\_at: optional number

Unix timestamp (in seconds) when the container was last active.

formatunixtime

memory\_limit: optional "1g" or "4g" or "16g" or "64g"

The memory limit configured for the container.

One of the following:

"1g"

"4g"

"16g"

"64g"

network\_policy: optional object { type, allowed\_domains }

Network access policy for the container.

type: "allowlist" or "disabled"

The network policy mode.

One of the following:

"allowlist"

"disabled"

allowed\_domains: optional array of string

Allowed outbound domains when `type` is `allowlist`.

ContainerCreateResponse object { id, created\_at, name, 6 more }

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

expires\_after: optional object { anchor, minutes }

The container will expire after this time period.
The anchor is the reference point for the expiration.
The minutes is the number of minutes after the anchor before the container expires.

anchor: optional "last\_active\_at"

The reference point for the expiration.

minutes: optional number

The number of minutes after the anchor before the container expires.

last\_active\_at: optional number

Unix timestamp (in seconds) when the container was last active.

formatunixtime

memory\_limit: optional "1g" or "4g" or "16g" or "64g"

The memory limit configured for the container.

One of the following:

"1g"

"4g"

"16g"

"64g"

network\_policy: optional object { type, allowed\_domains }

Network access policy for the container.

type: "allowlist" or "disabled"

The network policy mode.

One of the following:

"allowlist"

"disabled"

allowed\_domains: optional array of string

Allowed outbound domains when `type` is `allowlist`.

ContainerRetrieveResponse object { id, created\_at, name, 6 more }

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

expires\_after: optional object { anchor, minutes }

The container will expire after this time period.
The anchor is the reference point for the expiration.
The minutes is the number of minutes after the anchor before the container expires.

anchor: optional "last\_active\_at"

The reference point for the expiration.

minutes: optional number

The number of minutes after the anchor before the container expires.

last\_active\_at: optional number

Unix timestamp (in seconds) when the container was last active.

formatunixtime

memory\_limit: optional "1g" or "4g" or "16g" or "64g"

The memory limit configured for the container.

One of the following:

"1g"

"4g"

"16g"

"64g"

network\_policy: optional object { type, allowed\_domains }

Network access policy for the container.

type: "allowlist" or "disabled"

The network policy mode.

One of the following:

"allowlist"

"disabled"

allowed\_domains: optional array of string

Allowed outbound domains when `type` is `allowlist`.

#### ContainersFiles

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

#### ContainersFilesContent

##### [Retrieve container file content](/api/reference/resources/containers/subresources/files/subresources/content/methods/retrieve)

GET/containers/{container\_id}/files/{file\_id}/content
