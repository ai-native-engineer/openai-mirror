<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/agents/subresources/vaults/methods/update/ -->

## Update a vault

`beta.agents.vaults.update(strvault_id, VaultUpdateParams**kwargs)  -> Vault`

**post** `/vaults/{vault_id}`

Updates the name or metadata of an active vault. Omitted fields remain unchanged. See [vaults](/api/docs/guides/agents-api/tools/vaults).

- `vault_id: str`

  `minLength: 0`, `maxLength: 1048576`

- `metadata: Optional[Dict[str, str]]`

  Replaces all metadata. Omit to leave unchanged, or pass {} to clear it. Up to 16 string key-value pairs, with keys up to 64 and values up to 512 characters.

- `name: Optional[str]`

  A replacement name. Omit to leave unchanged, or pass null to clear it. The name is trimmed before storage. It must contain 1 to 256 UTF-8 bytes after trimming.

  `minLength: 1`, `maxLength: 1048576`

- `class Vault: …`

  A collection of credentials for MCP servers and OpenAI-hosted environments.

  - `id: str`

    The ID of the vault.

    `minLength: 0`

  - `created_at: int`

    The Unix timestamp, in seconds, when the vault was created.

    `format: int64`

  - `metadata: Dict[str, str]`

    Key-value pairs associated with the vault, such as an application or team identifier.

  - `name: Optional[str]`

    The human-readable name of the vault, if set.

    `minLength: 0`

  - `object: Literal["vault"]`

    The object type. Always `vault`.

    - `"vault"`

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
vault = client.beta.agents.vaults.update(
    vault_id="vault_id",
    name="Research vault",
print(vault.id)

  "metadata": {
    "foo": "string"
  "object": "vault"
