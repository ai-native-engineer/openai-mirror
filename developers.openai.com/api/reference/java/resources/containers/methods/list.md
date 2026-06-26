<!-- source: https://developers.openai.com/api/reference/java/resources/containers/methods/list/ -->

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

# List containers

ContainerListPage containers().list(ContainerListParamsparams = ContainerListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/containers

List Containers

##### ParametersExpand Collapse

ContainerListParams params

Optional<String> after

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

Optional<Long> limit

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

Optional<String> name

Filter results by container name.

Optional<[Order](/api/reference/java/resources/containers/methods/list#(resource)%20containers%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))> order

Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

ASC("asc")

DESC("desc")

##### ReturnsExpand Collapse

class ContainerListResponse:

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

### List containers

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
import com.openai.models.containers.ContainerListPage;
import com.openai.models.containers.ContainerListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ContainerListPage page = client.containers().list();

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
