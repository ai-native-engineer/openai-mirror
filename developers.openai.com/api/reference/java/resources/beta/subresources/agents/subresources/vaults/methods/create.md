<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/agents/subresources/vaults/methods/create/ -->

## Create a vault

`Vault beta().agents().vaults().create(VaultCreateParamsparams = VaultCreateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/vaults`

Creates a vault for the current project. See [vaults](/api/docs/guides/agents-api/tools/vaults).

- `VaultCreateParams params`

  - `Optional<Metadata> metadata`

    Key-value pairs to associate with the vault, such as an application or team identifier.

  - `Optional<String> name`

    The name is trimmed before storage. It must contain 1 to 256 UTF-8 bytes after trimming.

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
import com.openai.models.beta.agents.vaults.VaultCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        Vault vault = client.beta().agents().vaults().create();

  "metadata": {
    "foo": "string"
  "object": "vault"
