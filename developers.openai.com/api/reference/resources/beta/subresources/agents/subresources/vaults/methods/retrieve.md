<!-- source: https://developers.openai.com/api/reference/resources/beta/subresources/agents/subresources/vaults/methods/retrieve/ -->

[Vaults](/api/reference/resources/beta/subresources/agents/subresources/vaults)

# Retrieve a vault

GET/vaults/{vault\_id}

Retrieves a vault by its ID. See [vaults](/api/docs/guides/agents-api/tools/vaults).

vault\_id: string

Vault object { id, created\_at, metadata, 2 more }

A collection of credentials that agent tools can use to authenticate to MCP servers.

The ID of the vault.

The Unix timestamp, in seconds, when the vault was created.

metadata: map[string]

Key-value pairs associated with the vault, such as an application or team identifier.

name: string or null

The human-readable name of the vault, if set.

object: "vault"

The object type. Always `vault`.

### Retrieve a vault

curl https://api.openai.com/v1/vaults/$VAULT_ID \

  "created_at": 0,
  "metadata": {
    "foo": "string"
  },
  "name": "name",
  "object": "vault"

  "created_at": 0,
  "metadata": {
    "foo": "string"
  },
  "name": "name",
  "object": "vault"
