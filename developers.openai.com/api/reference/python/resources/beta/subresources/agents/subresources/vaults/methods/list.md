<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/agents/subresources/vaults/methods/list/ -->

## List vaults

`beta.agents.vaults.list(VaultListParams**kwargs)  -> SyncCursorPage[Vault]`

**get** `/vaults`

Lists vaults using ID-based pagination. See [vaults](/api/docs/guides/agents-api/tools/vaults).

- `after: Optional[str]`

  Return resources after this resource ID in the selected order.

- `limit: Optional[int]`

  The maximum number of resources to return. Defaults to 20. Values are clamped between 1 and 100.

- `order: Optional[Literal["asc", "desc"]]`

  Sort order by the `created_at` timestamp. Use `asc` for ascending order or `desc` for descending order. Defaults to `desc`.

  - `"asc"`

    Returns resources in ascending order.

  - `"desc"`

    Returns resources in descending order.

- `status: Optional[VaultStatusFilterParam]`

  Filter by one status or a list, such as `status=active` or `status[]=active&status[]=archived`. Both statuses are included by default.

  - `Literal["active", "archived"]`

    - `"active"`

    - `"archived"`

  - `List[VaultStatus]`

    - `"active"`

    - `"archived"`

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
page = client.beta.agents.vaults.list()
page = page.data[0]
print(page.id)

  "data": [
      "metadata": {
        "foo": "string"
      "object": "vault"
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
