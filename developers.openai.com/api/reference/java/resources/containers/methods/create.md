<!-- source: https://developers.openai.com/api/reference/java/resources/containers/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Containers](/api/reference/java/resources/containers)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create container

[ContainerCreateResponse](/api/reference/java/resources/containers#(resource)%20containers%20%3E%20(model)%20ContainerCreateResponse%20%3E%20(schema)) containers().create(ContainerCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/containers

Create Container

##### ParametersExpand Collapse

ContainerCreateParams params

String name

Name of the container to create.

Optional<ExpiresAfter> expiresAfter

Container expiration time in seconds relative to the ‘anchor’ time.

Anchor anchor

Time anchor for the expiration time. Currently only ‘last\_active\_at’ is supported.

long minutes

Optional<List<String>> fileIds

IDs of files to copy to the container.

Optional<MemoryLimit> memoryLimit

Optional memory limit for the container. Defaults to “1g”.

\_1G("1g")

\_4G("4g")

\_16G("16g")

\_64G("64g")

Optional<NetworkPolicy> networkPolicy

Network access policy for the container.

class ContainerNetworkPolicyDisabled:

JsonValue; type "disabled"constant"disabled"constant

Disable outbound network access. Always `disabled`.

class ContainerNetworkPolicyAllowlist:

List<String> allowedDomains

A list of allowed domains when type is `allowlist`.

JsonValue; type "allowlist"constant"allowlist"constant

Allow outbound network access only to specified domains. Always `allowlist`.

Optional<List<[ContainerNetworkPolicyDomainSecret](/api/reference/java/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema))>> domainSecrets

Optional domain-scoped secrets for allowlisted domains.

String domain

The domain associated with the secret.

minLength1

String name

The name of the secret to inject for the domain.

minLength1

String value

The secret value to inject for the domain.

maxLength10485760

minLength1

Optional<List<Skill>> skills

An optional list of skills referenced by id or inline data.

class SkillReference:

String skillId

The ID of the referenced skill.

maxLength64

minLength1

JsonValue; type "skill\_reference"constant"skill\_reference"constant

References a skill created with the /v1/skills endpoint.

Optional<String> version

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

class InlineSkill:

String description

The description of the skill.

String name

The name of the skill.

[InlineSkillSource](/api/reference/java/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill_source%20%3E%20(schema)) source

Inline skill payload

String data

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

JsonValue; mediaType "application/zip"constant"application/zip"constant

The media type of the inline skill payload. Must be `application/zip`.

JsonValue; type "base64"constant"base64"constant

The type of the inline skill source. Must be `base64`.

JsonValue; type "inline"constant"inline"constant

Defines an inline skill for this request.

##### ReturnsExpand Collapse

class ContainerCreateResponse:

String id

Unique identifier for the container.

long createdAt

Unix timestamp (in seconds) when the container was created.

formatunixtime

String name

Name of the container.

String object\_

The type of this object.

String status

Status of the container (e.g., active, deleted).

Optional<ExpiresAfter> expiresAfter

The container will expire after this time period.
The anchor is the reference point for the expiration.
The minutes is the number of minutes after the anchor before the container expires.

Optional<Anchor> anchor

The reference point for the expiration.

Optional<Long> minutes

The number of minutes after the anchor before the container expires.

Optional<Long> lastActiveAt

Unix timestamp (in seconds) when the container was last active.

formatunixtime

Optional<MemoryLimit> memoryLimit

The memory limit configured for the container.

One of the following:

\_1G("1g")

\_4G("4g")

\_16G("16g")

\_64G("64g")

Optional<NetworkPolicy> networkPolicy

Network access policy for the container.

Type type

The network policy mode.

One of the following:

ALLOWLIST("allowlist")

DISABLED("disabled")

Optional<List<String>> allowedDomains

Allowed outbound domains when `type` is `allowlist`.

### Create container

Java

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.containers.ContainerCreateParams;
import com.openai.models.containers.ContainerCreateResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ContainerCreateParams params = ContainerCreateParams.builder()
            .name("name")
            .build();
        ContainerCreateResponse container = client.containers().create(params);

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
