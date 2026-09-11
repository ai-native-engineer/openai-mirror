<!-- source: https://developers.openai.com/api/reference/resources/beta/subresources/agents/subresources/vaults/subresources/credentials/methods/delete/ -->

[Vaults](/api/reference/resources/beta/subresources/agents/subresources/vaults)

[Credentials](/api/reference/resources/beta/subresources/agents/subresources/vaults/subresources/credentials)

# Delete a vault credential

DELETE/vaults/{vault\_id}/credentials/{credential\_id}

Deletes a vault credential. See [vaults](/api/docs/guides/agents-api/tools/vaults).

vault\_id: string

credential\_id: string

CredentialDeleted object { id, deleted, object }

Confirmation that a vault credential was deleted.

The ID of the deleted credential.

deleted: boolean

Whether the resource was deleted. Always `true`.

object: "vault.credential.deleted"

The object type. Always `vault.credential.deleted`.

### Delete a vault credential

curl https://api.openai.com/v1/vaults/$VAULT_ID/credentials/$CREDENTIAL_ID \
    -X DELETE \

  "deleted": true,
  "object": "vault.credential.deleted"

  "deleted": true,
  "object": "vault.credential.deleted"
