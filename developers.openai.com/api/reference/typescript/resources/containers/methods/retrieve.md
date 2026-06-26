<!-- source: https://developers.openai.com/api/reference/typescript/resources/containers/methods/retrieve/ -->

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

# Retrieve container

client.containers.retrieve(stringcontainerID, RequestOptionsoptions?): [ContainerRetrieveResponse](/api/reference/typescript/resources/containers#(resource)%20containers%20%3E%20(model)%20container_retrieve_response%20%3E%20(schema)) { id, created\_at, name, 6 more }

GET/containers/{container\_id}

Retrieve Container

##### ParametersExpand Collapse

containerID: string

##### ReturnsExpand Collapse

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

### Retrieve container

TypeScript

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted

const container = await client.containers.retrieve('container_id');

console.log(container.id);

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
