<!-- source: https://developers.openai.com/api/reference/resources/containers/methods/create/ -->

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

# Create container

POST/containers

Create Container

##### Body ParametersJSONExpand Collapse

name: string

Name of the container to create.

expires\_after: optional object { anchor, minutes }

Container expiration time in seconds relative to the ‘anchor’ time.

anchor: "last\_active\_at"

Time anchor for the expiration time. Currently only ‘last\_active\_at’ is supported.

minutes: number

file\_ids: optional array of string

IDs of files to copy to the container.

memory\_limit: optional "1g" or "4g" or "16g" or "64g"

Optional memory limit for the container. Defaults to “1g”.

One of the following:

"1g"

"4g"

"16g"

"64g"

network\_policy: optional [ContainerNetworkPolicyDisabled](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_disabled%20%3E%20(schema)) { type }  or [ContainerNetworkPolicyAllowlist](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

One of the following:

ContainerNetworkPolicyDisabled object { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

ContainerNetworkPolicyAllowlist object { allowed\_domains, type, domain\_secrets }

allowed\_domains: array of string

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: optional array of [ContainerNetworkPolicyDomainSecret](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value }

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

minLength1

name: string

The name of the secret to inject for the domain.

minLength1

value: string

The secret value to inject for the domain.

maxLength10485760

minLength1

skills: optional array of [SkillReference](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20skill_reference%20%3E%20(schema)) { skill\_id, type, version }  or [InlineSkill](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill%20%3E%20(schema)) { description, name, source, type }

An optional list of skills referenced by id or inline data.

One of the following:

SkillReference object { skill\_id, type, version }

skill\_id: string

The ID of the referenced skill.

maxLength64

minLength1

type: "skill\_reference"

References a skill created with the /v1/skills endpoint.

version: optional string

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

InlineSkill object { description, name, source, type }

description: string

The description of the skill.

name: string

The name of the skill.

source: [InlineSkillSource](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill_source%20%3E%20(schema)) { data, media\_type, type }

Inline skill payload

data: string

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

media\_type: "application/zip"

The media type of the inline skill payload. Must be `application/zip`.

type: "base64"

The type of the inline skill source. Must be `base64`.

type: "inline"

Defines an inline skill for this request.

##### ReturnsExpand Collapse

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

### Create container

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
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
        "name": "My Container",
        "memory_limit": "4g",
        "skills": [
            "type": "skill_reference",
            "skill_id": "skill_4db6f1a2c9e73508b41f9da06e2c7b5f"
            "type": "skill_reference",
            "skill_id": "openai-spreadsheets",
            "version": "latest"
        ],
        "network_policy": {
          "type": "allowlist",
          "allowed_domains": ["api.buildkite.com"]
      }'

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
