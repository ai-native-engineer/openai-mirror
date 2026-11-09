<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/agents/subresources/vaults/methods/update/ -->

## Update a vault

`client.Beta.Agents.Vaults.Update(ctx, vaultID, body) (*Vault, error)`

**post** `/vaults/{vault_id}`

Updates the name or metadata of an active vault. Omitted fields remain unchanged. See [vaults](/api/docs/guides/agents-api/tools/vaults).

- `vaultID string`

  `minLength: 0`, `maxLength: 1048576`

- `body BetaAgentVaultUpdateParams`

  - `Metadata param.Field[map[string, string]]`

    Replaces all metadata. Omit to leave unchanged, or pass {} to clear it. Up to 16 string key-value pairs, with keys up to 64 and values up to 512 characters.

  - `Name param.Field[string]`

    A replacement name. Omit to leave unchanged, or pass null to clear it. The name is trimmed before storage. It must contain 1 to 256 UTF-8 bytes after trimming.

    `minLength: 1`, `maxLength: 1048576`

- `type Vault struct{…}`

  A collection of credentials for MCP servers and OpenAI-hosted environments.

  - `ID string`

    The ID of the vault.

    `minLength: 0`

  - `CreatedAt int64`

    The Unix timestamp, in seconds, when the vault was created.

    `format: int64`

  - `Metadata map[string, string]`

    Key-value pairs associated with the vault, such as an application or team identifier.

  - `Name string`

    The human-readable name of the vault, if set.

    `minLength: 0`

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
  vault, err := client.Beta.Agents.Vaults.Update(
    context.TODO(),
    "vault_id",
    openai.BetaAgentVaultUpdateParams{
      Name: openai.String("Research vault"),
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", vault.ID)

  "metadata": {
    "foo": "string"
  "object": "vault"
