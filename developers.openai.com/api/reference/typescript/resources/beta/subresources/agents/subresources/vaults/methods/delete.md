<!-- source: https://developers.openai.com/api/reference/typescript/resources/beta/subresources/agents/subresources/vaults/methods/delete/ -->

## Delete a vault

`client.beta.agents.vaults.delete(stringvaultID, RequestOptionsoptions?): VaultDeleted`

**delete** `/vaults/{vault_id}`

Deletes a vault and all its credentials. See [vaults](/api/docs/guides/agents-api/tools/vaults).

- `vaultID: string`

- `VaultDeleted`

  Confirmation that a vault was deleted.

  - `id: string`

    The ID of the deleted vault.

  - `deleted: boolean`

    Whether the resource was deleted. Always `true`.

  - `object: "vault.deleted"`

    The object type. Always `vault.deleted`.

    - `"vault.deleted"`

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const vaultDeleted = await client.beta.agents.vaults.delete('vault_id');

console.log(vaultDeleted.id);

  "deleted": true,
  "object": "vault.deleted"
