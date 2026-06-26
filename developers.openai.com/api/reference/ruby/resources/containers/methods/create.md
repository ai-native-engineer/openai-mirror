<!-- source: https://developers.openai.com/api/reference/ruby/resources/containers/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Containers](/api/reference/ruby/resources/containers)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create container

containers.create(\*\*kwargs) -> [ContainerCreateResponse](/api/reference/ruby/resources/containers#(resource)%20containers%20%3E%20(model)%20container_create_response%20%3E%20(schema)) { id, created\_at, name, 6 more }

POST/containers

Create Container

##### ParametersExpand Collapse

name: String

Name of the container to create.

expires\_after: ExpiresAfter{ anchor, minutes}

Container expiration time in seconds relative to the ‘anchor’ time.

anchor: :last\_active\_at

Time anchor for the expiration time. Currently only ‘last\_active\_at’ is supported.

minutes: Integer

file\_ids: Array[String]

IDs of files to copy to the container.

memory\_limit: :"1g" | :"4g" | :"16g" | :"64g"

Optional memory limit for the container. Defaults to “1g”.

One of the following:

:"1g"

:"4g"

:"16g"

:"64g"

network\_policy: [ContainerNetworkPolicyDisabled](/api/reference/ruby/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_disabled%20%3E%20(schema)) { type }  | [ContainerNetworkPolicyAllowlist](/api/reference/ruby/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

One of the following:

class ContainerNetworkPolicyDisabled { type }

type: :disabled

Disable outbound network access. Always `disabled`.

class ContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array[String]

A list of allowed domains when type is `allowlist`.

type: :allowlist

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: Array[[ContainerNetworkPolicyDomainSecret](/api/reference/ruby/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } ]

Optional domain-scoped secrets for allowlisted domains.

domain: String

The domain associated with the secret.

minLength1

name: String

The name of the secret to inject for the domain.

minLength1

value: String

The secret value to inject for the domain.

maxLength10485760

minLength1

skills: Array[[SkillReference](/api/reference/ruby/resources/responses#(resource)%20responses%20%3E%20(model)%20skill_reference%20%3E%20(schema)) { skill\_id, type, version }  | [InlineSkill](/api/reference/ruby/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill%20%3E%20(schema)) { description, name, source, type } ]

An optional list of skills referenced by id or inline data.

One of the following:

class SkillReference { skill\_id, type, version }

skill\_id: String

The ID of the referenced skill.

maxLength64

minLength1

type: :skill\_reference

References a skill created with the /v1/skills endpoint.

version: String

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

class InlineSkill { description, name, source, type }

description: String

The description of the skill.

name: String

The name of the skill.

source: [InlineSkillSource](/api/reference/ruby/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill_source%20%3E%20(schema)) { data, media\_type, type }

Inline skill payload

data: String

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

media\_type: :"application/zip"

The media type of the inline skill payload. Must be `application/zip`.

type: :base64

The type of the inline skill source. Must be `base64`.

type: :inline

Defines an inline skill for this request.

##### ReturnsExpand Collapse

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

### Create container

Ruby

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

container = openai.containers.create(name: "name")

puts(container)

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
