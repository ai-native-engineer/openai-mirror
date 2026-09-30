<!-- source: https://developers.openai.com/api/reference/ruby/resources/beta/subresources/agents/subresources/vaults/methods/delete/ -->

## Delete a vault

`beta.agents.vaults.delete(vault_id) -> VaultDeleted`

**delete** `/vaults/{vault_id}`

Deletes a vault and all its credentials. See [vaults](/api/docs/guides/agents-api/tools/vaults).

- `vault_id: String`

- `class VaultDeleted`

  Confirmation that a vault was deleted.

  - `id: String`

    The ID of the deleted vault.

  - `deleted: bool`

    Whether the resource was deleted. Always `true`.

  - `object: :"vault.deleted"`

    The object type. Always `vault.deleted`.

    - `:"vault.deleted"`

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

vault_deleted = openai.beta.agents.vaults.delete("vault_id")

puts(vault_deleted)

  "deleted": true,
  "object": "vault.deleted"
