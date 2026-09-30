<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/agents/subresources/vaults/methods/delete/ -->

## Delete a vault

`client.Beta.Agents.Vaults.Delete(ctx, vaultID) (*VaultDeleted, error)`

**delete** `/vaults/{vault_id}`

Deletes a vault and all its credentials. See [vaults](/api/docs/guides/agents-api/tools/vaults).

- `vaultID string`

- `type VaultDeleted struct{…}`

  Confirmation that a vault was deleted.

  - `ID string`

    The ID of the deleted vault.

  - `Deleted bool`

    Whether the resource was deleted. Always `true`.

  - `Object VaultDeleted`

    The object type. Always `vault.deleted`.

    - `const VaultDeletedVaultDeleted VaultDeleted = "vault.deleted"`

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
  vaultDeleted, err := client.Beta.Agents.Vaults.Delete(context.TODO(), "vault_id")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", vaultDeleted.ID)

  "deleted": true,
  "object": "vault.deleted"
