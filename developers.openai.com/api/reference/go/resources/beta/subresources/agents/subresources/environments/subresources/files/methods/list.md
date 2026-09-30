<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/agents/subresources/environments/subresources/files/methods/list/ -->

## List agent environment files

`client.Beta.Agents.Environments.Files.List(ctx, environmentID, query) (*TokenPage[EnvironmentFile], error)`

**get** `/agents/environments/{environment_id}/files`

Lists live files on a connected execution environment with optional directory filtering and opaque cursor pagination. See [environment files](/api/docs/guides/agents-api/environments/files).

- `environmentID string`

- `query BetaAgentEnvironmentFileListParams`

  - `Limit param.Field[int64]`

    The maximum number of files to return, between 1 and 100.

  - `Order param.Field[BetaAgentEnvironmentFileListParamsOrder]`

    Sort by case-sensitive path components. Defaults to descending.

    - `const BetaAgentEnvironmentFileListParamsOrderAsc BetaAgentEnvironmentFileListParamsOrder = "asc"`

      Returns resources in ascending order.

    - `const BetaAgentEnvironmentFileListParamsOrderDesc BetaAgentEnvironmentFileListParamsOrder = "desc"`

      Returns resources in descending order.

  - `Page param.Field[string]`

    The opaque token from the previous page. Keep the same path, order, and limit.

  - `Path param.Field[string]`

    Restrict the listing to this absolute workspace directory.

- `type EnvironmentFile struct{…}`

  A live file in an execution environment.

  - `EnvironmentID string`

    The ID of the environment containing this file.

  - `Object AgentEnvironmentFile`

    The object type. Always `agent.environment.file`.

    - `const AgentEnvironmentFileAgentEnvironmentFile AgentEnvironmentFile = "agent.environment.file"`

  - `Path string`

    The absolute file path inside the environment's workspace.

  - `SizeBytes int64`

    The file size in bytes.

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
  page, err := client.Beta.Agents.Environments.Files.List(
    context.TODO(),
    "environment_id",
    openai.BetaAgentEnvironmentFileListParams{

  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", page)

  "data": [
      "environment_id": "environment_id",
      "object": "agent.environment.file",
      "path": "path",
      "size_bytes": 0
  "has_more": true,
  "next": "next",
  "object": "page"
