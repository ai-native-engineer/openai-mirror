<!-- source: https://developers.openai.com/api/reference/python/resources/containers/methods/create/ -->

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

# Create container

containers.create(ContainerCreateParams\*\*kwargs)  -> [ContainerCreateResponse](/api/reference/python/resources/containers#(resource)%20containers%20%3E%20(model)%20container_create_response%20%3E%20(schema))

POST/containers

Create Container

##### ParametersExpand Collapse

name: str

Name of the container to create.

expires\_after: Optional[[ExpiresAfter](/api/reference/python/resources/containers/methods/create#(resource)%20containers%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20expires_after%20%3E%20(schema))]

Container expiration time in seconds relative to the ‘anchor’ time.

anchor: Literal["last\_active\_at"]

Time anchor for the expiration time. Currently only ‘last\_active\_at’ is supported.

minutes: int

file\_ids: Optional[Sequence[str]]

IDs of files to copy to the container.

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

Optional memory limit for the container. Defaults to “1g”.

One of the following:

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[[NetworkPolicy](/api/reference/python/resources/containers/methods/create#(resource)%20containers%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20network_policy%20%3E%20(schema))]

Network access policy for the container.

One of the following:

class ContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

Disable outbound network access. Always `disabled`.

class ContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

A list of allowed domains when type is `allowlist`.

type: Literal["allowlist"]

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: Optional[List[[ContainerNetworkPolicyDomainSecret](/api/reference/python/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema))]]

Optional domain-scoped secrets for allowlisted domains.

domain: str

The domain associated with the secret.

minLength1

name: str

The name of the secret to inject for the domain.

minLength1

value: str

The secret value to inject for the domain.

maxLength10485760

minLength1

skills: Optional[Iterable[Skill]]

An optional list of skills referenced by id or inline data.

One of the following:

class SkillReference: …

skill\_id: str

The ID of the referenced skill.

maxLength64

minLength1

type: Literal["skill\_reference"]

References a skill created with the /v1/skills endpoint.

version: Optional[str]

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

class InlineSkill: …

description: str

The description of the skill.

name: str

The name of the skill.

source: [InlineSkillSource](/api/reference/python/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill_source%20%3E%20(schema))

Inline skill payload

data: str

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

media\_type: Literal["application/zip"]

The media type of the inline skill payload. Must be `application/zip`.

type: Literal["base64"]

The type of the inline skill source. Must be `base64`.

type: Literal["inline"]

Defines an inline skill for this request.

##### ReturnsExpand Collapse

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

### Create container

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
container = client.containers.create(
    name="name",
print(container.id)

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
