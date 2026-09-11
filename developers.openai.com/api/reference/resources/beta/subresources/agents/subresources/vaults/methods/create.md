<!-- source: https://developers.openai.com/api/reference/resources/beta/subresources/agents/subresources/vaults/methods/create/ -->

[Vaults](/api/reference/resources/beta/subresources/agents/subresources/vaults)

# Create a vault

POST/vaults

Creates a vault for the current project. See [vaults](/api/docs/guides/agents-api/tools/vaults).

##### Body ParametersJSONExpand Collapse

metadata: optional map[string] or null

Key-value pairs to associate with the vault, such as an application or team identifier.

name: optional string

The name is trimmed before storage. It must contain 1 to 256 UTF-8 bytes after trimming.

minLength1

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

### Create a vault

curl https://api.openai.com/v1/vaults \
    -X POST \

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
