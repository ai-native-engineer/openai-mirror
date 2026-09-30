<!-- source: https://developers.openai.com/api/reference/ruby/resources/beta/subresources/agents/subresources/vaults/subresources/credentials/methods/delete/ -->

## Delete a vault credential

`beta.agents.vaults.credentials.delete(credential_id, **kwargs) -> CredentialDeleted`

**delete** `/vaults/{vault_id}/credentials/{credential_id}`

Deletes a vault credential. See [vaults](/api/docs/guides/agents-api/tools/vaults).

- `vault_id: String`

- `credential_id: String`

- `class CredentialDeleted`

  Confirmation that a vault credential was deleted.

  - `id: String`

    The ID of the deleted credential.

  - `deleted: bool`

    Whether the resource was deleted. Always `true`.

  - `object: :"vault.credential.deleted"`

    The object type. Always `vault.credential.deleted`.

    - `:"vault.credential.deleted"`

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

credential_deleted = openai.beta.agents.vaults.credentials.delete("credential_id", vault_id: "vault_id")

puts(credential_deleted)

  "deleted": true,
  "object": "vault.credential.deleted"
