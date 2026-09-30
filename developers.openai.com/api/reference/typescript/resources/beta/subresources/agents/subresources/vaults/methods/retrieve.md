<!-- source: https://developers.openai.com/api/reference/typescript/resources/beta/subresources/agents/subresources/vaults/methods/retrieve/ -->

## Retrieve a vault

`client.beta.agents.vaults.retrieve(stringvaultID, RequestOptionsoptions?): Vault`

**get** `/vaults/{vault_id}`

Retrieves a vault by its ID. See [vaults](/api/docs/guides/agents-api/tools/vaults).

- `vaultID: string`

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

const vault = await client.beta.agents.vaults.retrieve('vault_id');

console.log(vault.id);

  "metadata": {
    "foo": "string"
  "object": "vault"
