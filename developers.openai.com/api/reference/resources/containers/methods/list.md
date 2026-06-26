<!-- source: https://developers.openai.com/api/reference/resources/containers/methods/list/ -->

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

# List containers

GET/containers

List Containers

##### Query ParametersExpand Collapse

after: optional string

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

limit: optional number

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

name: optional string

Filter results by container name.

order: optional "asc" or "desc"

Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

One of the following:

"asc"

"desc"

##### ReturnsExpand Collapse

data: array of object { id, created\_at, name, 6 more }

A list of containers.

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

first\_id: string

The ID of the first container in the list.

has\_more: boolean

Whether there are more containers available.

last\_id: string

The ID of the last container in the list.

object: "list"

The type of object returned, must be ‘list’.

### List containers

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl https://api.openai.com/v1/containers \
  -H "Authorization: Bearer $OPENAI_API_KEY"

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
