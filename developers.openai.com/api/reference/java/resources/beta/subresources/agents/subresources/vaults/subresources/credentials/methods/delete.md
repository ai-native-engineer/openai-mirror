<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/agents/subresources/vaults/subresources/credentials/methods/delete/ -->

## Delete a vault credential

`CredentialDeleted beta().agents().vaults().credentials().delete(CredentialDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/vaults/{vault_id}/credentials/{credential_id}`

Deletes a vault credential. See [vaults](/api/docs/guides/agents-api/tools/vaults).

- `CredentialDeleteParams params`

  - `String vaultId`

  - `Optional<String> credentialId`

- `class CredentialDeleted:`

  Confirmation that a vault credential was deleted.

  - `String id`

    The ID of the deleted credential.

  - `boolean deleted`

    Whether the resource was deleted. Always `true`.

  - `JsonValue; object_ "vault.credential.deleted"constant`

    The object type. Always `vault.credential.deleted`.

    - `VAULT_CREDENTIAL_DELETED("vault.credential.deleted")`

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.vaults.credentials.CredentialDeleteParams;
import com.openai.models.beta.agents.vaults.credentials.CredentialDeleted;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        CredentialDeleteParams params = CredentialDeleteParams.builder()
            .vaultId("vault_id")
            .credentialId("credential_id")
            .build();
        CredentialDeleted credentialDeleted = client.beta().agents().vaults().credentials().delete(params);

  "deleted": true,
  "object": "vault.credential.deleted"
