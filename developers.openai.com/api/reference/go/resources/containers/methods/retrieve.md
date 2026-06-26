<!-- source: https://developers.openai.com/api/reference/go/resources/containers/methods/retrieve/ -->

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

# Retrieve container

client.Containers.Get(ctx, containerID) (\*[ContainerGetResponse](/api/reference/go/resources/containers#(resource)%20containers%20%3E%20(model)%20ContainerGetResponse%20%3E%20(schema)), error)

GET/containers/{container\_id}

Retrieve Container

##### ParametersExpand Collapse

containerID string

##### ReturnsExpand Collapse

type ContainerGetResponse struct{…}

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

ExpiresAfter ContainerGetResponseExpiresAfterOptional

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

MemoryLimit ContainerGetResponseMemoryLimitOptional

The memory limit configured for the container.

One of the following:

const ContainerGetResponseMemoryLimit1g ContainerGetResponseMemoryLimit = "1g"

const ContainerGetResponseMemoryLimit4g ContainerGetResponseMemoryLimit = "4g"

const ContainerGetResponseMemoryLimit16g ContainerGetResponseMemoryLimit = "16g"

const ContainerGetResponseMemoryLimit64g ContainerGetResponseMemoryLimit = "64g"

NetworkPolicy ContainerGetResponseNetworkPolicyOptional

Network access policy for the container.

Type string

The network policy mode.

One of the following:

const ContainerGetResponseNetworkPolicyTypeAllowlist ContainerGetResponseNetworkPolicyType = "allowlist"

const ContainerGetResponseNetworkPolicyTypeDisabled ContainerGetResponseNetworkPolicyType = "disabled"

AllowedDomains []stringOptional

Allowed outbound domains when `type` is `allowlist`.

### Retrieve container

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
  container, err := client.Containers.Get(context.TODO(), "container_id")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", container.ID)

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
