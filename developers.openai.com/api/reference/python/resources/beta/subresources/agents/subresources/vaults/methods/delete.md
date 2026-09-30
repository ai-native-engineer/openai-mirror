<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/agents/subresources/vaults/methods/delete/ -->

## Delete a vault

`beta.agents.vaults.delete(strvault_id)  -> VaultDeleted`

**delete** `/vaults/{vault_id}`

Deletes a vault and all its credentials. See [vaults](/api/docs/guides/agents-api/tools/vaults).

- `vault_id: str`

- `class VaultDeleted: …`

  Confirmation that a vault was deleted.

  - `id: str`

    The ID of the deleted vault.

  - `deleted: bool`

    Whether the resource was deleted. Always `true`.

  - `object: Literal["vault.deleted"]`

    The object type. Always `vault.deleted`.

    - `"vault.deleted"`

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
vault_deleted = client.beta.agents.vaults.delete(
    "vault_id",
print(vault_deleted.id)

  "deleted": true,
  "object": "vault.deleted"
