<!-- source: https://developers.openai.com/api/reference/go/resources/containers/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Containers](/api/reference/go/resources/containers)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List containers

client.Containers.List(ctx, query) (\*CursorPage[[ContainerListResponse](/api/reference/go/resources/containers#(resource)%20containers%20%3E%20(model)%20ContainerListResponse%20%3E%20(schema))], error)

GET/containers

List Containers

##### ParametersExpand Collapse

query ContainerListParams

After param.Field[string]Optional

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

Limit param.Field[int64]Optional

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

Name param.Field[string]Optional

Filter results by container name.

Order param.Field[[ContainerListParamsOrder](/api/reference/go/resources/containers/methods/list#(resource)%20containers%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))]Optional

Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

const ContainerListParamsOrderAsc [ContainerListParamsOrder](/api/reference/go/resources/containers/methods/list#(resource)%20containers%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)) = "asc"

const ContainerListParamsOrderDesc [ContainerListParamsOrder](/api/reference/go/resources/containers/methods/list#(resource)%20containers%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)) = "desc"

##### ReturnsExpand Collapse

type ContainerListResponse struct{…}

ID string

Unique identifier for the container.

CreatedAt int64

Unix timestamp (in seconds) when the container was created.

formatunixtime

Name string

Name of the container.

Object string

The type of this object.

Status string

Status of the container (e.g., active, deleted).

ExpiresAfter ContainerListResponseExpiresAfterOptional

The container will expire after this time period.
The anchor is the reference point for the expiration.
The minutes is the number of minutes after the anchor before the container expires.

Anchor stringOptional

The reference point for the expiration.

Minutes int64Optional

The number of minutes after the anchor before the container expires.

LastActiveAt int64Optional

Unix timestamp (in seconds) when the container was last active.

formatunixtime

MemoryLimit ContainerListResponseMemoryLimitOptional

The memory limit configured for the container.

One of the following:

const ContainerListResponseMemoryLimit1g ContainerListResponseMemoryLimit = "1g"

const ContainerListResponseMemoryLimit4g ContainerListResponseMemoryLimit = "4g"

const ContainerListResponseMemoryLimit16g ContainerListResponseMemoryLimit = "16g"

const ContainerListResponseMemoryLimit64g ContainerListResponseMemoryLimit = "64g"

NetworkPolicy ContainerListResponseNetworkPolicyOptional

Network access policy for the container.

Type string

The network policy mode.

One of the following:

const ContainerListResponseNetworkPolicyTypeAllowlist ContainerListResponseNetworkPolicyType = "allowlist"

const ContainerListResponseNetworkPolicyTypeDisabled ContainerListResponseNetworkPolicyType = "disabled"

AllowedDomains []stringOptional

Allowed outbound domains when `type` is `allowlist`.

### List containers

Go

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  page, err := client.Containers.List(context.TODO(), openai.ContainerListParams{

  })
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", page)

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
