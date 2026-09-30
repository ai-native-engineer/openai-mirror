<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/agents/subresources/environments/subresources/files/methods/create/ -->

## Create an agent environment file

`client.Beta.Agents.Environments.Files.New(ctx, environmentID, body) (*EnvironmentFile, error)`

**post** `/agents/environments/{environment_id}/files`

Copies inline bytes or a Files API file into a connected execution environment. See [environment files](/api/docs/guides/agents-api/environments/files).

- `environmentID string`

- `body BetaAgentEnvironmentFileNewParams`

  - `FileID param.Field[string]`

    The ID of the uploaded file.

  - `Path param.Field[string]`

    The absolute destination path inside `/workspace`.

  - `Type param.Field[FileID]`

    The type of the object. Always `file_id`.

    - `const FileIDFileID FileID = "file_id"`

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
  environmentFile, err := client.Beta.Agents.Environments.Files.New(
    context.TODO(),
    "environment_id",
    openai.BetaAgentEnvironmentFileNewParams{
      HostedEnvironmentFileParamUnionResp: map[string]any{},
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", environmentFile.EnvironmentID)

  "environment_id": "environment_id",
  "object": "agent.environment.file",
  "path": "path",
  "size_bytes": 0
