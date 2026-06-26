<!-- source: https://developers.openai.com/api/reference/typescript/resources/containers/methods/list/ -->

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

# List containers

client.containers.list(ContainerListParams { after, limit, name, order } query?, RequestOptionsoptions?): CursorPage<[ContainerListResponse](/api/reference/typescript/resources/containers#(resource)%20containers%20%3E%20(model)%20container_list_response%20%3E%20(schema)) { id, created\_at, name, 6 more } >

GET/containers

List Containers

##### ParametersExpand Collapse

query: ContainerListParams { after, limit, name, order }

after?: string

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

limit?: number

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

name?: string

Filter results by container name.

order?: "asc" | "desc"

Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

One of the following:

"asc"

"desc"

##### ReturnsExpand Collapse

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

### List containers

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

// Automatically fetches more pages as needed.
for await (const containerListResponse of client.containers.list()) {
  console.log(containerListResponse.id);

  "object": "list",
  "data": [
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
  ],
  "first_id": "container_123",
  "last_id": "container_123",
  "has_more": false

##### Returns Examples

  "object": "list",
  "data": [
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
  ],
  "first_id": "container_123",
  "last_id": "container_123",
  "has_more": false
