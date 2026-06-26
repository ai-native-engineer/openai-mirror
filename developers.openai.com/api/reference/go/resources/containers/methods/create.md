<!-- source: https://developers.openai.com/api/reference/go/resources/containers/methods/create/ -->

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

# Create container

client.Containers.New(ctx, body) (\*[ContainerNewResponse](/api/reference/go/resources/containers#(resource)%20containers%20%3E%20(model)%20ContainerNewResponse%20%3E%20(schema)), error)

POST/containers

Create Container

##### ParametersExpand Collapse

body ContainerNewParams

Name param.Field[string]

Name of the container to create.

ExpiresAfter param.Field[[ContainerNewParamsExpiresAfter](/api/reference/go/resources/containers/methods/create#(resource)%20containers%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20expires_after%20%3E%20(schema))]Optional

Container expiration time in seconds relative to the ‘anchor’ time.

Anchor string

Time anchor for the expiration time. Currently only ‘last\_active\_at’ is supported.

Minutes int64

FileIDs param.Field[[]string]Optional

IDs of files to copy to the container.

MemoryLimit param.Field[[ContainerNewParamsMemoryLimit](/api/reference/go/resources/containers/methods/create#(resource)%20containers%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20memory_limit%20%3E%20(schema))]Optional

Optional memory limit for the container. Defaults to “1g”.

const ContainerNewParamsMemoryLimit1g [ContainerNewParamsMemoryLimit](/api/reference/go/resources/containers/methods/create#(resource)%20containers%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20memory_limit%20%3E%20(schema)) = "1g"

const ContainerNewParamsMemoryLimit4g [ContainerNewParamsMemoryLimit](/api/reference/go/resources/containers/methods/create#(resource)%20containers%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20memory_limit%20%3E%20(schema)) = "4g"

const ContainerNewParamsMemoryLimit16g [ContainerNewParamsMemoryLimit](/api/reference/go/resources/containers/methods/create#(resource)%20containers%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20memory_limit%20%3E%20(schema)) = "16g"

const ContainerNewParamsMemoryLimit64g [ContainerNewParamsMemoryLimit](/api/reference/go/resources/containers/methods/create#(resource)%20containers%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20memory_limit%20%3E%20(schema)) = "64g"

NetworkPolicy param.Field[[ContainerNewParamsNetworkPolicyUnion](/api/reference/go/resources/containers/methods/create#(resource)%20containers%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20network_policy%20%3E%20(schema))]Optional

Network access policy for the container.

type ContainerNetworkPolicyDisabled struct{…}

Type Disabled

Disable outbound network access. Always `disabled`.

type ContainerNetworkPolicyAllowlist struct{…}

AllowedDomains []string

A list of allowed domains when type is `allowlist`.

Type Allowlist

Allow outbound network access only to specified domains. Always `allowlist`.

DomainSecrets [][ContainerNetworkPolicyDomainSecret](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema))Optional

Optional domain-scoped secrets for allowlisted domains.

Domain string

The domain associated with the secret.

minLength1

Name string

The name of the secret to inject for the domain.

minLength1

Value string

The secret value to inject for the domain.

maxLength10485760

minLength1

Skills param.Field[[]ContainerNewParamsSkillUnion]Optional

An optional list of skills referenced by id or inline data.

type SkillReference struct{…}

SkillID string

The ID of the referenced skill.

maxLength64

minLength1

Type SkillReference

References a skill created with the /v1/skills endpoint.

Version stringOptional

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

type InlineSkill struct{…}

Description string

The description of the skill.

Name string

The name of the skill.

Source [InlineSkillSource](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill_source%20%3E%20(schema))

Inline skill payload

Data string

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

MediaType ApplicationZip

The media type of the inline skill payload. Must be `application/zip`.

Type Base64

The type of the inline skill source. Must be `base64`.

Type Inline

Defines an inline skill for this request.

##### ReturnsExpand Collapse

type ContainerNewResponse struct{…}

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

ExpiresAfter ContainerNewResponseExpiresAfterOptional

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

MemoryLimit ContainerNewResponseMemoryLimitOptional

The memory limit configured for the container.

One of the following:

const ContainerNewResponseMemoryLimit1g ContainerNewResponseMemoryLimit = "1g"

const ContainerNewResponseMemoryLimit4g ContainerNewResponseMemoryLimit = "4g"

const ContainerNewResponseMemoryLimit16g ContainerNewResponseMemoryLimit = "16g"

const ContainerNewResponseMemoryLimit64g ContainerNewResponseMemoryLimit = "64g"

NetworkPolicy ContainerNewResponseNetworkPolicyOptional

Network access policy for the container.

Type string

The network policy mode.

One of the following:

const ContainerNewResponseNetworkPolicyTypeAllowlist ContainerNewResponseNetworkPolicyType = "allowlist"

const ContainerNewResponseNetworkPolicyTypeDisabled ContainerNewResponseNetworkPolicyType = "disabled"

AllowedDomains []stringOptional

Allowed outbound domains when `type` is `allowlist`.

### Create container

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
  container, err := client.Containers.New(context.TODO(), openai.ContainerNewParams{
    Name: "name",
  })
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", container.ID)

    "id": "cntr_682e30645a488191b6363a0cbefc0f0a025ec61b66250591",
    "object": "container",
    "created_at": 1747857508,
    "status": "running",
    "expires_after": {
        "anchor": "last_active_at",
        "minutes": 20
    "last_active_at": 1747857508,
    "network_policy": {
        "type": "allowlist",
        "allowed_domains": ["api.buildkite.com"]
    "memory_limit": "4g",
    "name": "My Container"

##### Returns Examples

    "id": "cntr_682e30645a488191b6363a0cbefc0f0a025ec61b66250591",
    "object": "container",
    "created_at": 1747857508,
    "status": "running",
    "expires_after": {
        "anchor": "last_active_at",
        "minutes": 20
    "last_active_at": 1747857508,
    "network_policy": {
        "type": "allowlist",
        "allowed_domains": ["api.buildkite.com"]
    "memory_limit": "4g",
    "name": "My Container"
