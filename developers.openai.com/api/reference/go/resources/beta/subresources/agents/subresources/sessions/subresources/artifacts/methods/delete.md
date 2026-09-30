<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/agents/subresources/sessions/subresources/artifacts/methods/delete/ -->

## Delete an agent session artifact

`client.Beta.Agents.Sessions.Artifacts.Delete(ctx, sessionID, artifactID) (*SessionArtifactDeleted, error)`

**delete** `/agents/sessions/{session_id}/artifacts/{artifact_id}`

Deletes an immutable session artifact without deleting its live environment file or original Files API object. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

- `sessionID string`

- `artifactID string`

- `type SessionArtifactDeleted struct{…}`

  Confirmation that an immutable session artifact was deleted.

  - `ID string`

    The ID of the deleted session artifact.

  - `Deleted bool`

    Whether the session artifact was deleted. Always `true`.

  - `Object AgentSessionArtifactDeleted`

    The object type. Always `agent.session.artifact.deleted`.

    - `const AgentSessionArtifactDeletedAgentSessionArtifactDeleted AgentSessionArtifactDeleted = "agent.session.artifact.deleted"`

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
  sessionArtifactDeleted, err := client.Beta.Agents.Sessions.Artifacts.Delete(
    context.TODO(),
    "session_id",
    "artifact_id",
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", sessionArtifactDeleted.ID)

  "deleted": true,
  "object": "agent.session.artifact.deleted"
