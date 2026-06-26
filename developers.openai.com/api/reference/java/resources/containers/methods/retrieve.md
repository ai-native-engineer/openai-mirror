<!-- source: https://developers.openai.com/api/reference/java/resources/containers/methods/retrieve/ -->

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

# Retrieve container

[ContainerRetrieveResponse](/api/reference/java/resources/containers#(resource)%20containers%20%3E%20(model)%20ContainerRetrieveResponse%20%3E%20(schema)) containers().retrieve(ContainerRetrieveParamsparams = ContainerRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/containers/{container\_id}

Retrieve Container

##### ParametersExpand Collapse

ContainerRetrieveParams params

Optional<String> containerId

##### ReturnsExpand Collapse

class ContainerRetrieveResponse:

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

### Retrieve container

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
import com.openai.models.containers.ContainerRetrieveParams;
import com.openai.models.containers.ContainerRetrieveResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ContainerRetrieveResponse container = client.containers().retrieve("container_id");

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
