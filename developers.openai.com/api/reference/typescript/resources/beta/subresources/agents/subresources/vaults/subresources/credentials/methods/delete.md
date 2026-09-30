<!-- source: https://developers.openai.com/api/reference/typescript/resources/beta/subresources/agents/subresources/vaults/subresources/credentials/methods/delete/ -->

## Delete a vault credential

`client.beta.agents.vaults.credentials.delete(stringcredentialID, CredentialDeleteParamsparams, RequestOptionsoptions?): CredentialDeleted`

**delete** `/vaults/{vault_id}/credentials/{credential_id}`

Deletes a vault credential. See [vaults](/api/docs/guides/agents-api/tools/vaults).

- `credentialID: string`

- `params: CredentialDeleteParams`

  - `vault_id: string`

    The ID of the vault.

- `CredentialDeleted`

  Confirmation that a vault credential was deleted.

  - `id: string`

    The ID of the deleted credential.

  - `deleted: boolean`

    Whether the resource was deleted. Always `true`.

  - `object: "vault.credential.deleted"`

    The object type. Always `vault.credential.deleted`.

    - `"vault.credential.deleted"`

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const credentialDeleted = await client.beta.agents.vaults.credentials.delete('credential_id', {
  vault_id: 'vault_id',
});

console.log(credentialDeleted.id);

  "deleted": true,
  "object": "vault.credential.deleted"
