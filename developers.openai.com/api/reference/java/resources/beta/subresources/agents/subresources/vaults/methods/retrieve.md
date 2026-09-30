<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/agents/subresources/vaults/methods/retrieve/ -->

## Retrieve a vault

`Vault beta().agents().vaults().retrieve(VaultRetrieveParamsparams = VaultRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/vaults/{vault_id}`

Retrieves a vault by its ID. See [vaults](/api/docs/guides/agents-api/tools/vaults).

- `VaultRetrieveParams params`

  - `Optional<String> vaultId`

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
import com.openai.models.beta.agents.vaults.Vault;
import com.openai.models.beta.agents.vaults.VaultRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        Vault vault = client.beta().agents().vaults().retrieve("vault_id");

  "metadata": {
    "foo": "string"
  "object": "vault"
