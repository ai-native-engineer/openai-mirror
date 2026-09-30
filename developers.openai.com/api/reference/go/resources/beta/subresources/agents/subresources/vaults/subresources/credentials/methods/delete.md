<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/agents/subresources/vaults/subresources/credentials/methods/delete/ -->

## Delete a vault credential

`client.Beta.Agents.Vaults.Credentials.Delete(ctx, vaultID, credentialID) (*CredentialDeleted, error)`

**delete** `/vaults/{vault_id}/credentials/{credential_id}`

Deletes a vault credential. See [vaults](/api/docs/guides/agents-api/tools/vaults).

- `vaultID string`

- `credentialID string`

- `type CredentialDeleted struct{…}`

  Confirmation that a vault credential was deleted.

  - `ID string`

    The ID of the deleted credential.

  - `Deleted bool`

    Whether the resource was deleted. Always `true`.

  - `Object VaultCredentialDeleted`

    The object type. Always `vault.credential.deleted`.

    - `const VaultCredentialDeletedVaultCredentialDeleted VaultCredentialDeleted = "vault.credential.deleted"`

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  credentialDeleted, err := client.Beta.Agents.Vaults.Credentials.Delete(
    context.TODO(),
    "vault_id",
    "credential_id",
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", credentialDeleted.ID)

  "deleted": true,
  "object": "vault.credential.deleted"
