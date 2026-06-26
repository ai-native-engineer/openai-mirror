<!-- source: https://developers.openai.com/api/reference/go/resources/fine_tuning/subresources/checkpoints/subresources/permissions/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Fine Tuning](/api/reference/go/resources/fine_tuning)

[Checkpoints](/api/reference/go/resources/fine_tuning/subresources/checkpoints)

[Permissions](/api/reference/go/resources/fine_tuning/subresources/checkpoints/subresources/permissions)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create checkpoint permissions

client.FineTuning.Checkpoints.Permissions.New(ctx, fineTunedModelCheckpoint, body) (\*Page[[FineTuningCheckpointPermissionNewResponse](/api/reference/go/resources/fine_tuning#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20FineTuningCheckpointPermissionNewResponse%20%3E%20(schema))], error)

POST/fine\_tuning/checkpoints/{fine\_tuned\_model\_checkpoint}/permissions

**NOTE:** Calling this endpoint requires an [admin API key](../admin-api-keys).

This enables organization owners to share fine-tuned models with other projects in their organization.

##### ParametersExpand Collapse

fineTunedModelCheckpoint string

body FineTuningCheckpointPermissionNewParams

ProjectIDs param.Field[[]string]

The project identifiers to grant access to.

##### ReturnsExpand Collapse

type FineTuningCheckpointPermissionNewResponse struct{…}

The `checkpoint.permission` object represents a permission for a fine-tuned model checkpoint.

ID string

The permission identifier, which can be referenced in the API endpoints.

CreatedAt int64

The Unix timestamp (in seconds) for when the permission was created.

formatunixtime

Object CheckpointPermission

The object type, which is always “checkpoint.permission”.

ProjectID string

The project identifier that the permission is for.

### Create checkpoint permissions

Go

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  page, err := client.FineTuning.Checkpoints.Permissions.New(
    context.TODO(),
    "ft:gpt-4o-mini-2024-07-18:org:weather:B7R9VjQd",
    openai.FineTuningCheckpointPermissionNewParams{
      ProjectIDs: []string{"string"},
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", page)

  "object": "list",
  "data": [
      "object": "checkpoint.permission",
      "id": "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
      "created_at": 1721764867,
      "project_id": "proj_abGMw1llN8IrBb6SvvY5A1iH"
  ],
  "first_id": "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
  "last_id": "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
  "has_more": false

##### Returns Examples

  "object": "list",
  "data": [
      "object": "checkpoint.permission",
      "id": "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
      "created_at": 1721764867,
      "project_id": "proj_abGMw1llN8IrBb6SvvY5A1iH"
  ],
  "first_id": "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
  "last_id": "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
  "has_more": false
