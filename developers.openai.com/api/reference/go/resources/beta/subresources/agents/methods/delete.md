<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/agents/methods/delete/ -->

## Delete an agent

`client.Beta.Agents.Delete(ctx, agentID) (*AgentDeleted, error)`

**delete** `/agents/{agent_id}`

Deletes a reusable agent. See [agent configuration](/api/docs/guides/agents-api/configuration).

- `agentID string`

- `type AgentDeleted struct{…}`

  A deleted reusable agent.

  - `ID string`

    The ID of the deleted agent.

  - `Deleted bool`

    Whether the agent was deleted. Always `true`.

  - `Object AgentDeleted`

    The object type. Always `agent.deleted`.

    - `const AgentDeletedAgentDeleted AgentDeleted = "agent.deleted"`

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
  agentDeleted, err := client.Beta.Agents.Delete(context.TODO(), "agent_id")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", agentDeleted.ID)

  "deleted": true,
  "object": "agent.deleted"
