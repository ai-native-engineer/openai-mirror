<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/agents/subresources/vaults/subresources/credentials/methods/delete/ -->

## Delete a vault credential

`beta.agents.vaults.credentials.delete(strcredential_id, CredentialDeleteParams**kwargs)  -> CredentialDeleted`

**delete** `/vaults/{vault_id}/credentials/{credential_id}`

Deletes a vault credential. See [vaults](/api/docs/guides/agents-api/tools/vaults).

- `vault_id: str`

- `credential_id: str`

- `class CredentialDeleted: …`

  Confirmation that a vault credential was deleted.

  - `id: str`

    The ID of the deleted credential.

  - `deleted: bool`

    Whether the resource was deleted. Always `true`.

  - `object: Literal["vault.credential.deleted"]`

    The object type. Always `vault.credential.deleted`.

    - `"vault.credential.deleted"`

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
credential_deleted = client.beta.agents.vaults.credentials.delete(
    credential_id="credential_id",
    vault_id="vault_id",
print(credential_deleted.id)

  "deleted": true,
  "object": "vault.credential.deleted"
