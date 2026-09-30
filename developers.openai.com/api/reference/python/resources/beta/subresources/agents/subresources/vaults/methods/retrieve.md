<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/agents/subresources/vaults/methods/retrieve/ -->

## Retrieve a vault

`beta.agents.vaults.retrieve(strvault_id)  -> Vault`

**get** `/vaults/{vault_id}`

Retrieves a vault by its ID. See [vaults](/api/docs/guides/agents-api/tools/vaults).

- `vault_id: str`

- `class Vault: …`

  A collection of credentials for MCP servers and OpenAI-hosted environments.

  - `id: str`

    The ID of the vault.

  - `created_at: int`

    The Unix timestamp, in seconds, when the vault was created.

  - `metadata: Dict[str, str]`

    Key-value pairs associated with the vault, such as an application or team identifier.

  - `name: Optional[str]`

    The human-readable name of the vault, if set.

  - `object: Literal["vault"]`

    The object type. Always `vault`.

    - `"vault"`

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
vault = client.beta.agents.vaults.retrieve(
    "vault_id",
print(vault.id)

  "metadata": {
    "foo": "string"
  "object": "vault"
