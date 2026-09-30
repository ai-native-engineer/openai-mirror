<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/agents/subresources/sessions/subresources/artifacts/methods/retrieve/ -->

## Retrieve an agent session artifact

`client.Beta.Agents.Sessions.Artifacts.Get(ctx, sessionID, artifactID) (*SessionArtifact, error)`

**get** `/agents/sessions/{session_id}/artifacts/{artifact_id}`

Retrieves immutable metadata for one durable session artifact. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

- `sessionID string`

- `artifactID string`

- `type SessionArtifact struct{…}`

  An immutable file published by a completed hosted session turn.

  - `ID string`

    The immutable artifact ID.

  - `CreatedAt int64`

    The Unix timestamp, in seconds, when the artifact was published.

  - `EnvironmentID string`

    The ID of the environment that produced the artifact.

  - `Object AgentSessionArtifact`

    The object type. Always `agent.session.artifact`.

    - `const AgentSessionArtifactAgentSessionArtifact AgentSessionArtifact = "agent.session.artifact"`

  - `Path string`

    The original absolute file path in the execution environment.

  - `SessionID string`

    The ID of the session that owns the artifact.

  - `SizeBytes int64`

    The immutable artifact size in bytes.

  - `TurnID string`

    The ID of the completed turn that published the artifact.

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
  sessionArtifact, err := client.Beta.Agents.Sessions.Artifacts.Get(
    context.TODO(),
    "session_id",
    "artifact_id",
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", sessionArtifact.ID)

  "environment_id": "environment_id",
  "object": "agent.session.artifact",
  "path": "path",
  "session_id": "session_id",
  "size_bytes": 0,
  "turn_id": "turn_id"
