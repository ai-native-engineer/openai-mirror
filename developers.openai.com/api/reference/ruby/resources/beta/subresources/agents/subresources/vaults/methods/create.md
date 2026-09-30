<!-- source: https://developers.openai.com/api/reference/ruby/resources/beta/subresources/agents/subresources/vaults/methods/create/ -->

## Create a vault

`beta.agents.vaults.create(**kwargs) -> Vault`

**post** `/vaults`

Creates a vault for the current project. See [vaults](/api/docs/guides/agents-api/tools/vaults).

- `metadata: Hash[Symbol, String]`

  Key-value pairs to associate with the vault, such as an application or team identifier.

- `name: String`

  The name is trimmed before storage. It must contain 1 to 256 UTF-8 bytes after trimming.

- `class Vault`

  A collection of credentials for MCP servers and OpenAI-hosted environments.

  - `id: String`

    The ID of the vault.

  - `created_at: Integer`

    The Unix timestamp, in seconds, when the vault was created.

  - `metadata: Hash[Symbol, String]`

    Key-value pairs associated with the vault, such as an application or team identifier.

  - `name: String`

    The human-readable name of the vault, if set.

  - `object: :vault`

    The object type. Always `vault`.

    - `:vault`

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

vault = openai.beta.agents.vaults.create

puts(vault)

  "metadata": {
    "foo": "string"
  "object": "vault"
