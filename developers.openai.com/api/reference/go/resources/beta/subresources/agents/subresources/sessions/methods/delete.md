<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/agents/subresources/sessions/methods/delete/ -->

## Delete an agent session

`client.Beta.Agents.Sessions.Delete(ctx, sessionID) (*AgentSessionDeleted, error)`

**delete** `/agents/sessions/{session_id}`

Removes a managed agent session from the public API and returns a deletion confirmation. If backend execution has ended, deletion can cancel a still-open public turn and abandon unpublished outputs. Running execution must be cancelled first. Physical cleanup may continue asynchronously. See [managing sessions](/api/docs/guides/agents-api/sessions/manage).

- `sessionID string`

- `type AgentSessionDeleted struct{…}`

  A Managed Agents session removed from the public API. Physical cleanup may continue asynchronously.

  - `ID string`

    The ID of the deleted session.

  - `Deleted bool`

    Whether the session has been removed from the public API. Always `true`. Physical cleanup may still be in progress.

  - `Object AgentSessionDeleted`

    The object type. Always `agent.session.deleted`.

    - `const AgentSessionDeletedAgentSessionDeleted AgentSessionDeleted = "agent.session.deleted"`

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
  agentSessionDeleted, err := client.Beta.Agents.Sessions.Delete(context.TODO(), "session_id")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", agentSessionDeleted.ID)

  "deleted": true,
  "object": "agent.session.deleted"
