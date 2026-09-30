<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/agents/subresources/vaults/methods/delete/ -->

## Delete a vault

`VaultDeleted beta().agents().vaults().delete(VaultDeleteParamsparams = VaultDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/vaults/{vault_id}`

Deletes a vault and all its credentials. See [vaults](/api/docs/guides/agents-api/tools/vaults).

- `VaultDeleteParams params`

  - `Optional<String> vaultId`

- `class VaultDeleted:`

  Confirmation that a vault was deleted.

  - `String id`

    The ID of the deleted vault.

  - `boolean deleted`

    Whether the resource was deleted. Always `true`.

  - `JsonValue; object_ "vault.deleted"constant`

    The object type. Always `vault.deleted`.

    - `VAULT_DELETED("vault.deleted")`

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.vaults.VaultDeleteParams;
import com.openai.models.beta.agents.vaults.VaultDeleted;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        VaultDeleted vaultDeleted = client.beta().agents().vaults().delete("vault_id");

  "deleted": true,
  "object": "vault.deleted"
