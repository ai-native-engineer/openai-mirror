<!-- source: https://developers.openai.com/api/reference/cli/resources/containers/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Containers](/api/reference/cli/resources/containers)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create container

$ openai containers create

POST/containers

Create Container

##### ParametersExpand Collapse

--name: string

Name of the container to create.

--expires-after: optional object { anchor, minutes }

Container expiration time in seconds relative to the ‘anchor’ time.

--file-id: optional array of string

IDs of files to copy to the container.

--memory-limit: optional "1g" or "4g" or "16g" or "64g"

Optional memory limit for the container. Defaults to “1g”.

--network-policy: optional [ContainerNetworkPolicyDisabled](/api/reference/cli/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_disabled%20%3E%20(schema)) { type }  or [ContainerNetworkPolicyAllowlist](/api/reference/cli/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

--skill: optional array of [SkillReference](/api/reference/cli/resources/responses#(resource)%20responses%20%3E%20(model)%20skill_reference%20%3E%20(schema)) { skill\_id, type, version }  or [InlineSkill](/api/reference/cli/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill%20%3E%20(schema)) { description, name, source, type }

An optional list of skills referenced by id or inline data.

##### ReturnsExpand Collapse

ContainerNewResponse: object { id, created\_at, name, 6 more }

id: string

Unique identifier for the container.

created\_at: number

Unix timestamp (in seconds) when the container was created.

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

"last\_active\_at"

minutes: optional number

The number of minutes after the anchor before the container expires.

last\_active\_at: optional number

Unix timestamp (in seconds) when the container was last active.

memory\_limit: optional "1g" or "4g" or "16g" or "64g"

The memory limit configured for the container.

"1g"

"4g"

"16g"

"64g"

network\_policy: optional object { type, allowed\_domains }

Network access policy for the container.

type: "allowlist" or "disabled"

The network policy mode.

"allowlist"

"disabled"

allowed\_domains: optional array of string

Allowed outbound domains when `type` is `allowlist`.

### Create container

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai containers create \
  --api-key 'My API Key' \
  --name name

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
