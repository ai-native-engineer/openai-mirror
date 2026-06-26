<!-- source: https://developers.openai.com/api/reference/go/resources/fine_tuning/subresources/checkpoints/subresources/permissions/methods/delete/ -->

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

# Delete checkpoint permission

client.FineTuning.Checkpoints.Permissions.Delete(ctx, fineTunedModelCheckpoint, permissionID) (\*[FineTuningCheckpointPermissionDeleteResponse](/api/reference/go/resources/fine_tuning#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20FineTuningCheckpointPermissionDeleteResponse%20%3E%20(schema)), error)

DELETE/fine\_tuning/checkpoints/{fine\_tuned\_model\_checkpoint}/permissions/{permission\_id}

**NOTE:** This endpoint requires an [admin API key](../admin-api-keys).

Organization owners can use this endpoint to delete a permission for a fine-tuned model checkpoint.

##### ParametersExpand Collapse

fineTunedModelCheckpoint string

permissionID string

##### ReturnsExpand Collapse

type FineTuningCheckpointPermissionDeleteResponse struct{…}

ID string

The ID of the fine-tuned model checkpoint permission that was deleted.

Deleted bool

Whether the fine-tuned model checkpoint permission was successfully deleted.

Object CheckpointPermission

The object type, which is always “checkpoint.permission”.

### Delete checkpoint permission

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
  permission, err := client.FineTuning.Checkpoints.Permissions.Delete(
    context.TODO(),
    "ft:gpt-4o-mini-2024-07-18:org:weather:B7R9VjQd",
    "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", permission.ID)

  "object": "checkpoint.permission",
  "id": "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
  "deleted": true

##### Returns Examples

  "object": "checkpoint.permission",
  "id": "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
  "deleted": true
