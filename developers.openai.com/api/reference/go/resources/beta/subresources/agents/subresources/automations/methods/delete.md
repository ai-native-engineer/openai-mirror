<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/agents/subresources/automations/methods/delete/ -->

## Delete an automation

`client.Beta.Agents.Automations.Delete(ctx, automationID) (*AutomationDeleted, error)`

**delete** `/agents/automations/{automation_id}`

Deletes the automation and prevents future invocations without deleting its target session.

- `automationID string`

  `minLength: 0`, `maxLength: 1048576`

- `type AutomationDeleted struct{…}`

  - `ID string`

    The deleted automation ID.

    `minLength: 0`

  - `Deleted bool`

    Always true.

  - `Object AgentAutomationDeleted`

    Always `agent.automation.deleted`.

    - `const AgentAutomationDeletedAgentAutomationDeleted AgentAutomationDeleted = "agent.automation.deleted"`

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
  automationDeleted, err := client.Beta.Agents.Automations.Delete(context.TODO(), "automation_id")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", automationDeleted.ID)

  "deleted": true,
  "object": "agent.automation.deleted"
