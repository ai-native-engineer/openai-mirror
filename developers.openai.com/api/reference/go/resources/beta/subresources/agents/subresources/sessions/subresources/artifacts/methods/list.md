<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/agents/subresources/sessions/subresources/artifacts/methods/list/ -->

## List agent session artifacts

`client.Beta.Agents.Sessions.Artifacts.List(ctx, sessionID, query) (*CursorPage[SessionArtifact], error)`

**get** `/agents/sessions/{session_id}/artifacts`

Lists immutable artifacts published by completed hosted session turns. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

- `sessionID string`

- `query BetaAgentSessionArtifactListParams`

  - `After param.Field[string]`

    Return artifacts after this immutable artifact ID.

  - `EnvironmentID param.Field[string]`

    Restrict the listing to artifacts produced by this environment.

  - `Limit param.Field[int64]`

    The maximum number of artifacts to return, between 1 and 100.

  - `Order param.Field[BetaAgentSessionArtifactListParamsOrder]`

    Sort by creation time and ID. Defaults to descending.

    - `const BetaAgentSessionArtifactListParamsOrderAsc BetaAgentSessionArtifactListParamsOrder = "asc"`

      Returns resources in ascending order.

    - `const BetaAgentSessionArtifactListParamsOrderDesc BetaAgentSessionArtifactListParamsOrder = "desc"`

      Returns resources in descending order.

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
  page, err := client.Beta.Agents.Sessions.Artifacts.List(
    context.TODO(),
    "session_id",
    openai.BetaAgentSessionArtifactListParams{

  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", page)

  "data": [
      "environment_id": "environment_id",
      "object": "agent.session.artifact",
      "path": "path",
      "session_id": "session_id",
      "size_bytes": 0,
      "turn_id": "turn_id"
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
