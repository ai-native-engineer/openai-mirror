<!-- source: https://developers.openai.com/api/reference/resources/beta/subresources/agents/subresources/vaults/methods/list/ -->

[Vaults](/api/reference/resources/beta/subresources/agents/subresources/vaults)

# List vaults

GET/vaults

Lists vaults using ID-based pagination. See [vaults](/api/docs/guides/agents-api/tools/vaults).

##### Query ParametersExpand Collapse

after: optional string

Return resources after this resource ID in the selected order.

limit: optional number or null

The maximum number of resources to return. Defaults to 20. Values are clamped between 1 and 100.

minimum0

order: optional "asc" or "desc"

Sort order by the `created_at` timestamp. Use `asc` for ascending order or `desc` for descending order. Defaults to `desc`.

"asc"

Returns resources in ascending order.

"desc"

Returns resources in descending order.

status: optional [VaultStatusFilter](/api/reference/resources/beta#(resource)%20beta.agents.vaults%20%3E%20(model)%20vault_status_filter%20%3E%20(schema))

Filter by one status or a list, such as `status=active` or `status[]=active&status[]=archived`. Both statuses are included by default.

VaultStatus = "active" or "archived"

Whether a vault or credential is active or archived.

"active"

"archived"

array of [VaultStatus](/api/reference/resources/beta#(resource)%20beta.agents.vaults%20%3E%20(model)%20vault_status%20%3E%20(schema))

"active"

"archived"

data: array of [Vault](/api/reference/resources/beta#(resource)%20beta.agents.vaults%20%3E%20(model)%20vault%20%3E%20(schema)) { id, created\_at, metadata, 2 more }

The resources returned in this page, in the requested sort order.

The ID of the vault.

The Unix timestamp, in seconds, when the vault was created.

metadata: map[string]

Key-value pairs associated with the vault, such as an application or team identifier.

name: string or null

The human-readable name of the vault, if set.

object: "vault"

The object type. Always `vault`.

first\_id: string or null

The ID of the first resource in `data`, or `null` if the page is empty.

has\_more: boolean

Whether there are more resources to retrieve after this page.

last\_id: string or null

The ID of the last resource in `data`, or `null` if the page is empty. Pass this as `after` with the same order and filters.

object: "list"

The object type, which is always `list`.

### List vaults

curl https://api.openai.com/v1/vaults \

  "data": [
      "created_at": 0,
      "metadata": {
        "foo": "string"
      },
      "name": "name",
      "object": "vault"
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"

  "data": [
      "created_at": 0,
      "metadata": {
        "foo": "string"
      },
      "name": "name",
      "object": "vault"
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
