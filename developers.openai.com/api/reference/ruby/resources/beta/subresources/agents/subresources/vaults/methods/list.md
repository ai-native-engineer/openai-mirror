<!-- source: https://developers.openai.com/api/reference/ruby/resources/beta/subresources/agents/subresources/vaults/methods/list/ -->

## List vaults

`beta.agents.vaults.list(**kwargs) -> CursorPage<Vault>`

**get** `/vaults`

Lists vaults using ID-based pagination. See [vaults](/api/docs/guides/agents-api/tools/vaults).

- `after: String`

  Return resources after this resource ID in the selected order.

- `limit: Integer`

  The maximum number of resources to return. Defaults to 20. Values are clamped between 1 and 100.

- `order: :asc | :desc`

  Sort order by the `created_at` timestamp. Use `asc` for ascending order or `desc` for descending order. Defaults to `desc`.

  - `:asc`

    Returns resources in ascending order.

  - `:desc`

    Returns resources in descending order.

- `status: VaultStatusFilter`

  Filter by one status or a list, such as `status=active` or `status[]=active&status[]=archived`. Both statuses are included by default.

  - `VaultStatus = :active | :archived`

    Whether a vault or credential is active or archived.

    - `:active`

    - `:archived`

  - `UnionMember1 = Array[VaultStatus]`

    - `:active`

    - `:archived`

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

page = openai.beta.agents.vaults.list

puts(page)

  "data": [
      "metadata": {
        "foo": "string"
      "object": "vault"
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
