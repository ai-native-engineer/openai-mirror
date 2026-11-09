<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/agents/subresources/vaults/methods/update/ -->

## Update a vault

`Vault beta().agents().vaults().update(VaultUpdateParamsparams = VaultUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/vaults/{vault_id}`

Updates the name or metadata of an active vault. Omitted fields remain unchanged. See [vaults](/api/docs/guides/agents-api/tools/vaults).

- `VaultUpdateParams params`

  - `Optional<String> vaultId`

    `minLength: 0`, `maxLength: 1048576`

  - `Optional<Metadata> metadata`

    Replaces all metadata. Omit to leave unchanged, or pass {} to clear it. Up to 16 string key-value pairs, with keys up to 64 and values up to 512 characters.

  - `Optional<String> name`

    A replacement name. Omit to leave unchanged, or pass null to clear it. The name is trimmed before storage. It must contain 1 to 256 UTF-8 bytes after trimming.

    `minLength: 1`, `maxLength: 1048576`

- `class Vault:`

  A collection of credentials for MCP servers and OpenAI-hosted environments.

  - `String id`

    The ID of the vault.

    `minLength: 0`

  - `long createdAt`

    The Unix timestamp, in seconds, when the vault was created.

    `format: int64`

  - `Metadata metadata`

    Key-value pairs associated with the vault, such as an application or team identifier.

  - `Optional<String> name`

    The human-readable name of the vault, if set.

    `minLength: 0`

  - `JsonValue; object_ "vault"constant`

    The object type. Always `vault`.

    - `VAULT("vault")`

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.vaults.Vault;
import com.openai.models.beta.agents.vaults.VaultUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        Vault vault = client.beta().agents().vaults().update("vault_id");

  "metadata": {
    "foo": "string"
  "object": "vault"
