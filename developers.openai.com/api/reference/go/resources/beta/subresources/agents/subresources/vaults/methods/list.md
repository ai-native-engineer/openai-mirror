<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/agents/subresources/vaults/methods/list/ -->

## List vaults

`client.Beta.Agents.Vaults.List(ctx, query) (*CursorPage[Vault], error)`

**get** `/vaults`

Lists vaults using ID-based pagination. See [vaults](/api/docs/guides/agents-api/tools/vaults).

- `query BetaAgentVaultListParams`

  - `After param.Field[string]`

    Return resources after this resource ID in the selected order.

  - `Limit param.Field[int64]`

    The maximum number of resources to return. Defaults to 20. Values are clamped between 1 and 100.

  - `Order param.Field[BetaAgentVaultListParamsOrder]`

    Sort order by the `created_at` timestamp. Use `asc` for ascending order or `desc` for descending order. Defaults to `desc`.

    - `const BetaAgentVaultListParamsOrderAsc BetaAgentVaultListParamsOrder = "asc"`

      Returns resources in ascending order.

    - `const BetaAgentVaultListParamsOrderDesc BetaAgentVaultListParamsOrder = "desc"`

      Returns resources in descending order.

  - `Status param.Field[VaultStatusFilterUnion]`

    Filter by one status or a list, such as `status=active` or `status[]=active&status[]=archived`. Both statuses are included by default.

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
  page, err := client.Beta.Agents.Vaults.List(context.TODO(), openai.BetaAgentVaultListParams{

  })
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", page)

  "data": [
      "metadata": {
        "foo": "string"
      "object": "vault"
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
