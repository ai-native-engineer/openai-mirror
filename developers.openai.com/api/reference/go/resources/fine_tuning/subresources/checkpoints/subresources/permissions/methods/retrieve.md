<!-- source: https://developers.openai.com/api/reference/go/resources/fine_tuning/subresources/checkpoints/subresources/permissions/methods/retrieve/ -->

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

# List checkpoint permissions

Deprecated: Retrieve is deprecated. Please swap to the paginated list method instead.

client.FineTuning.Checkpoints.Permissions.Get(ctx, fineTunedModelCheckpoint, query) (\*[FineTuningCheckpointPermissionGetResponse](/api/reference/go/resources/fine_tuning#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20FineTuningCheckpointPermissionGetResponse%20%3E%20(schema)), error)

GET/fine\_tuning/checkpoints/{fine\_tuned\_model\_checkpoint}/permissions

**NOTE:** This endpoint requires an [admin API key](../admin-api-keys).

Organization owners can use this endpoint to view all permissions for a fine-tuned model checkpoint.

##### ParametersExpand Collapse

fineTunedModelCheckpoint string

query FineTuningCheckpointPermissionGetParams

After param.Field[string]Optional

Identifier for the last permission ID from the previous pagination request.

Limit param.Field[int64]Optional

Number of permissions to retrieve.

Order param.Field[[FineTuningCheckpointPermissionGetParamsOrder](/api/reference/go/resources/fine_tuning/subresources/checkpoints/subresources/permissions/methods/retrieve#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(method)%20retrieve%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))]Optional

The order in which to retrieve permissions.

const FineTuningCheckpointPermissionGetParamsOrderAscending [FineTuningCheckpointPermissionGetParamsOrder](/api/reference/go/resources/fine_tuning/subresources/checkpoints/subresources/permissions/methods/retrieve#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(method)%20retrieve%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)) = "ascending"

const FineTuningCheckpointPermissionGetParamsOrderDescending [FineTuningCheckpointPermissionGetParamsOrder](/api/reference/go/resources/fine_tuning/subresources/checkpoints/subresources/permissions/methods/retrieve#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(method)%20retrieve%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)) = "descending"

ProjectID param.Field[string]Optional

The ID of the project to get permissions for.

##### ReturnsExpand Collapse

type FineTuningCheckpointPermissionGetResponse struct{…}

Data []FineTuningCheckpointPermissionGetResponseData

ID string

The permission identifier, which can be referenced in the API endpoints.

CreatedAt int64

The Unix timestamp (in seconds) for when the permission was created.

formatunixtime

Object CheckpointPermission

The object type, which is always “checkpoint.permission”.

ProjectID string

The project identifier that the permission is for.

HasMore bool

Object List

FirstID stringOptional

LastID stringOptional

### List checkpoint permissions

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
  permission, err := client.FineTuning.Checkpoints.Permissions.Get(
    context.TODO(),
    "ft-AF1WoRqd3aJAHsqc9NY7iL8F",
    openai.FineTuningCheckpointPermissionGetParams{

  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", permission.FirstID)

  "object": "list",
  "data": [
      "object": "checkpoint.permission",
      "id": "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
      "created_at": 1721764867,
      "project_id": "proj_abGMw1llN8IrBb6SvvY5A1iH"
      "object": "checkpoint.permission",
      "id": "cp_enQCFmOTGj3syEpYVhBRLTSy",
      "created_at": 1721764800,
      "project_id": "proj_iqGMw1llN8IrBb6SvvY5A1oF"
  ],
  "first_id": "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
  "last_id": "cp_enQCFmOTGj3syEpYVhBRLTSy",
  "has_more": false

##### Returns Examples

  "object": "list",
  "data": [
      "object": "checkpoint.permission",
      "id": "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
      "created_at": 1721764867,
      "project_id": "proj_abGMw1llN8IrBb6SvvY5A1iH"
      "object": "checkpoint.permission",
      "id": "cp_enQCFmOTGj3syEpYVhBRLTSy",
      "created_at": 1721764800,
      "project_id": "proj_iqGMw1llN8IrBb6SvvY5A1oF"
  ],
  "first_id": "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
  "last_id": "cp_enQCFmOTGj3syEpYVhBRLTSy",
  "has_more": false
