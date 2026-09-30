<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/agents/subresources/environments/subresources/templates/methods/delete/ -->

## Delete an agent environment template

`client.Beta.Agents.Environments.Templates.Delete(ctx, environmentTemplateID) (*EnvironmentTemplateDeleted, error)`

**delete** `/agents/environments/templates/{environment_template_id}`

Deletes reusable environment configuration and all confidential template inputs. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

- `environmentTemplateID string`

- `type EnvironmentTemplateDeleted struct{…}`

  A deleted reusable environment template.

  - `ID string`

    The ID of the deleted environment template.

  - `Deleted bool`

    Whether the environment template was deleted. Always `true`.

  - `Object AgentEnvironmentTemplateDeleted`

    The object type. Always `agent.environment.template.deleted`.

    - `const AgentEnvironmentTemplateDeletedAgentEnvironmentTemplateDeleted AgentEnvironmentTemplateDeleted = "agent.environment.template.deleted"`

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
  environmentTemplateDeleted, err := client.Beta.Agents.Environments.Templates.Delete(context.TODO(), "environment_template_id")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", environmentTemplateDeleted.ID)

  "deleted": true,
  "object": "agent.environment.template.deleted"
