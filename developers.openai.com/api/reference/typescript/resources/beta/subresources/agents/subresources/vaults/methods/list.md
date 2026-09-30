<!-- source: https://developers.openai.com/api/reference/typescript/resources/beta/subresources/agents/subresources/vaults/methods/list/ -->

## List vaults

`client.beta.agents.vaults.list(VaultListParamsquery?, RequestOptionsoptions?): CursorPage<Vault>`

**get** `/vaults`

Lists vaults using ID-based pagination. See [vaults](/api/docs/guides/agents-api/tools/vaults).

- `query: VaultListParams`

  - `after?: string`

    Return resources after this resource ID in the selected order.

  - `limit?: number | null`

    The maximum number of resources to return. Defaults to 20. Values are clamped between 1 and 100.

  - `order?: "asc" | "desc"`

    Sort order by the `created_at` timestamp. Use `asc` for ascending order or `desc` for descending order. Defaults to `desc`.

    - `"asc"`

      Returns resources in ascending order.

    - `"desc"`

      Returns resources in descending order.

  - `status?: VaultStatusFilter`

    Filter by one status or a list, such as `status=active` or `status[]=active&status[]=archived`. Both statuses are included by default.

    - `VaultStatus = "active" | "archived"`

      Whether a vault or credential is active or archived.

      - `"active"`

      - `"archived"`

    - `Array<VaultStatus>`

      - `"active"`

      - `"archived"`

- `Vault`

  A collection of credentials for MCP servers and OpenAI-hosted environments.

  - `id: string`

    The ID of the vault.

  - `created_at: number`

    The Unix timestamp, in seconds, when the vault was created.

  - `metadata: Record<string, string>`

    Key-value pairs associated with the vault, such as an application or team identifier.

  - `name: string | null`

    The human-readable name of the vault, if set.

  - `object: "vault"`

    The object type. Always `vault`.

    - `"vault"`

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const vault of client.beta.agents.vaults.list()) {
  console.log(vault.id);

  "data": [
      "metadata": {
        "foo": "string"
      "object": "vault"
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
