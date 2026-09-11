<!-- source: https://developers.openai.com/api/reference/resources/beta/subresources/agents/subresources/vaults/methods/delete/ -->

[Vaults](/api/reference/resources/beta/subresources/agents/subresources/vaults)

# Delete a vault

DELETE/vaults/{vault\_id}

Deletes a vault and all its credentials. See [vaults](/api/docs/guides/agents-api/tools/vaults).

vault\_id: string

VaultDeleted object { id, deleted, object }

Confirmation that a vault was deleted.

The ID of the deleted vault.

deleted: boolean

Whether the resource was deleted. Always `true`.

object: "vault.deleted"

The object type. Always `vault.deleted`.

### Delete a vault

curl https://api.openai.com/v1/vaults/$VAULT_ID \
    -X DELETE \

  "deleted": true,
  "object": "vault.deleted"

  "deleted": true,
  "object": "vault.deleted"
