<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/agents/subresources/vaults/methods/list/ -->

## List vaults

`VaultListPage beta().agents().vaults().list(VaultListParamsparams = VaultListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/vaults`

Lists vaults using ID-based pagination. See [vaults](/api/docs/guides/agents-api/tools/vaults).

- `VaultListParams params`

  - `Optional<String> after`

    Return resources after this resource ID in the selected order.

  - `Optional<Long> limit`

    The maximum number of resources to return. Defaults to 20. Values are clamped between 1 and 100.

  - `Optional<Order> order`

    Sort order by the `created_at` timestamp. Use `asc` for ascending order or `desc` for descending order. Defaults to `desc`.

    - `ASC("asc")`

      Returns resources in ascending order.

    - `DESC("desc")`

      Returns resources in descending order.

  - `Optional<VaultStatusFilter> status`

    Filter by one status or a list, such as `status=active` or `status[]=active&status[]=archived`. Both statuses are included by default.

    - `enum VaultStatus:`

      Whether a vault or credential is active or archived.

      - `ACTIVE("active")`

      - `ARCHIVED("archived")`

    - `List<VaultStatus>`

      - `ACTIVE("active")`

      - `ARCHIVED("archived")`

- `class Vault:`

  A collection of credentials for MCP servers and OpenAI-hosted environments.

  - `String id`

    The ID of the vault.

  - `long createdAt`

    The Unix timestamp, in seconds, when the vault was created.

  - `Metadata metadata`

    Key-value pairs associated with the vault, such as an application or team identifier.

  - `Optional<String> name`

    The human-readable name of the vault, if set.

  - `JsonValue; object_ "vault"constant`

    The object type. Always `vault`.

    - `VAULT("vault")`

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.vaults.VaultListPage;
import com.openai.models.beta.agents.vaults.VaultListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        VaultListPage page = client.beta().agents().vaults().list();

  "data": [
      "metadata": {
        "foo": "string"
      "object": "vault"
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
