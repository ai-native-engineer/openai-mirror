<!-- source: https://developers.openai.com/api/reference/python/resources/containers/methods/retrieve/ -->

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

# Retrieve container

containers.retrieve(strcontainer\_id)  -> [ContainerRetrieveResponse](/api/reference/python/resources/containers#(resource)%20containers%20%3E%20(model)%20container_retrieve_response%20%3E%20(schema))

GET/containers/{container\_id}

Retrieve Container

##### ParametersExpand Collapse

container\_id: str

##### ReturnsExpand Collapse

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

### Retrieve container

Python

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
container = client.containers.retrieve(
    "container_id",
print(container.id)

    "id": "cntr_682dfebaacac8198bbfe9c2474fb6f4a085685cbe3cb5863",
    "object": "container",
    "created_at": 1747844794,
    "status": "running",
    "expires_after": {
        "anchor": "last_active_at",
        "minutes": 20
    "last_active_at": 1747844794,
    "memory_limit": "4g",
    "name": "My Container"

##### Returns Examples

    "id": "cntr_682dfebaacac8198bbfe9c2474fb6f4a085685cbe3cb5863",
    "object": "container",
    "created_at": 1747844794,
    "status": "running",
    "expires_after": {
        "anchor": "last_active_at",
        "minutes": 20
    "last_active_at": 1747844794,
    "memory_limit": "4g",
    "name": "My Container"
