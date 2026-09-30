<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/agents/subresources/sessions/subresources/artifacts/methods/content/ -->

## Retrieve agent session artifact content

`client.Beta.Agents.Sessions.Artifacts.Content(ctx, sessionID, artifactID) (*Response, error)`

**get** `/agents/sessions/{session_id}/artifacts/{artifact_id}/content`

Downloads immutable session artifact bytes after the execution environment expires. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

- `sessionID string`

- `artifactID string`

- `type BetaAgentSessionArtifactContentResponse interface{…}`

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
  response, err := client.Beta.Agents.Sessions.Artifacts.Content(
    context.TODO(),
    "session_id",
    "artifact_id",
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", response)
