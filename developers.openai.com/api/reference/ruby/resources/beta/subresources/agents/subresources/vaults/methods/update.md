<!-- source: https://developers.openai.com/api/reference/ruby/resources/beta/subresources/agents/subresources/vaults/methods/update/ -->

## Update a vault

`beta.agents.vaults.update(vault_id, **kwargs) -> Vault`

**post** `/vaults/{vault_id}`

Updates the name or metadata of an active vault. Omitted fields remain unchanged. See [vaults](/api/docs/guides/agents-api/tools/vaults).

- `vault_id: String`

  `minLength: 0`, `maxLength: 1048576`

- `metadata: Hash[Symbol, String]`

  Replaces all metadata. Omit to leave unchanged, or pass {} to clear it. Up to 16 string key-value pairs, with keys up to 64 and values up to 512 characters.

- `name: String`

  A replacement name. Omit to leave unchanged, or pass null to clear it. The name is trimmed before storage. It must contain 1 to 256 UTF-8 bytes after trimming.

  `minLength: 1`, `maxLength: 1048576`

- `class Vault`

  A collection of credentials for MCP servers and OpenAI-hosted environments.

  - `id: String`

    The ID of the vault.

    `minLength: 0`

  - `created_at: Integer`

    The Unix timestamp, in seconds, when the vault was created.

    `format: int64`

  - `metadata: Hash[Symbol, String]`

    Key-value pairs associated with the vault, such as an application or team identifier.

  - `name: String`

    The human-readable name of the vault, if set.

    `minLength: 0`

  - `object: :vault`

    The object type. Always `vault`.

    - `:vault`

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

vault = openai.beta.agents.vaults.update("vault_id")

puts(vault)

  "metadata": {
    "foo": "string"
  "object": "vault"
