<!-- source: https://developers.openai.com/api/reference/typescript/resources/beta/subresources/agents/subresources/vaults/methods/update/ -->

## Update a vault

`client.beta.agents.vaults.update(stringvaultID, VaultUpdateParamsbody, RequestOptionsoptions?): Vault`

**post** `/vaults/{vault_id}`

Updates the name or metadata of an active vault. Omitted fields remain unchanged. See [vaults](/api/docs/guides/agents-api/tools/vaults).

- `vaultID: string`

  `minLength: 0`, `maxLength: 1048576`

- `body: VaultUpdateParams`

  - `metadata?: Record<string, string>`

    Replaces all metadata. Omit to leave unchanged, or pass {} to clear it. Up to 16 string key-value pairs, with keys up to 64 and values up to 512 characters.

  - `name?: string | null`

    A replacement name. Omit to leave unchanged, or pass null to clear it. The name is trimmed before storage. It must contain 1 to 256 UTF-8 bytes after trimming.

    `minLength: 1`, `maxLength: 1048576`

- `Vault`

  A collection of credentials for MCP servers and OpenAI-hosted environments.

  - `id: string`

    The ID of the vault.

    `minLength: 0`

  - `created_at: number`

    The Unix timestamp, in seconds, when the vault was created.

    `format: int64`

  - `metadata: Record<string, string>`

    Key-value pairs associated with the vault, such as an application or team identifier.

  - `name: string | null`

    The human-readable name of the vault, if set.

    `minLength: 0`

  - `object: "vault"`

    The object type. Always `vault`.

    - `"vault"`

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const vault = await client.beta.agents.vaults.update('vault_id', { name: 'Research vault' });

console.log(vault.id);

  "metadata": {
    "foo": "string"
  "object": "vault"
