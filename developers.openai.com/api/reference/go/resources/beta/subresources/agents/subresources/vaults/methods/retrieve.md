<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/agents/subresources/vaults/methods/retrieve/ -->

## Retrieve a vault

`client.Beta.Agents.Vaults.Get(ctx, vaultID) (*Vault, error)`

**get** `/vaults/{vault_id}`

Retrieves a vault by its ID. See [vaults](/api/docs/guides/agents-api/tools/vaults).

- `vaultID string`

- `type Vault struct{…}`

  A collection of credentials for MCP servers and OpenAI-hosted environments.

  - `ID string`

    The ID of the vault.

  - `CreatedAt int64`

    The Unix timestamp, in seconds, when the vault was created.

  - `Metadata map[string, string]`

    Key-value pairs associated with the vault, such as an application or team identifier.

  - `Name string`

    The human-readable name of the vault, if set.

  - `Object Vault`

    The object type. Always `vault`.

    - `const VaultVault Vault = "vault"`

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
  vault, err := client.Beta.Agents.Vaults.Get(context.TODO(), "vault_id")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", vault.ID)

  "metadata": {
    "foo": "string"
  "object": "vault"
