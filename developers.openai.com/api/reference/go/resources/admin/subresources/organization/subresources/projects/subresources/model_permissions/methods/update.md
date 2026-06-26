<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/methods/update/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Admin](/api/reference/go/resources/admin)

[Organization](/api/reference/go/resources/admin/subresources/organization)

[Projects](/api/reference/go/resources/admin/subresources/organization/subresources/projects)

[Model Permissions](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Modify project model permissions

client.Admin.Organization.Projects.ModelPermissions.Update(ctx, projectID, body) (\*[ProjectModelPermissions](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.model_permissions%20%3E%20(model)%20project_model_permissions%20%3E%20(schema)), error)

POST/organization/projects/{project\_id}/model\_permissions

Updates model permissions for a project.

##### ParametersExpand Collapse

projectID string

body AdminOrganizationProjectModelPermissionUpdateParams

Mode param.Field[[AdminOrganizationProjectModelPermissionUpdateParamsMode](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/methods/update#(resource)%20admin.organization.projects.model_permissions%20%3E%20(method)%20update%20%3E%20(params)%20default%20%3E%20(param)%20mode%20%3E%20(schema))]

The model permissions mode to apply.

const AdminOrganizationProjectModelPermissionUpdateParamsModeAllowList [AdminOrganizationProjectModelPermissionUpdateParamsMode](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/methods/update#(resource)%20admin.organization.projects.model_permissions%20%3E%20(method)%20update%20%3E%20(params)%20default%20%3E%20(param)%20mode%20%3E%20(schema)) = "allow\_list"

const AdminOrganizationProjectModelPermissionUpdateParamsModeDenyList [AdminOrganizationProjectModelPermissionUpdateParamsMode](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/methods/update#(resource)%20admin.organization.projects.model_permissions%20%3E%20(method)%20update%20%3E%20(params)%20default%20%3E%20(param)%20mode%20%3E%20(schema)) = "deny\_list"

ModelIDs param.Field[[]string]

The model IDs included in this permissions policy.

##### ReturnsExpand Collapse

type ProjectModelPermissions struct{…}

Represents the model allowlist or denylist policy for a project.

Mode ProjectModelPermissionsMode

Whether the project uses an allowlist or a denylist.

One of the following:

const ProjectModelPermissionsModeAllowList ProjectModelPermissionsMode = "allow\_list"

const ProjectModelPermissionsModeDenyList ProjectModelPermissionsMode = "deny\_list"

ModelIDs []string

The model IDs included in the model permissions policy.

Object ProjectModelPermissions

The object type, which is always `project.model_permissions`.

### Modify project model permissions

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
    option.WithAdminAPIKey("My Admin API Key"),
  projectModelPermissions, err := client.Admin.Organization.Projects.ModelPermissions.Update(
    context.TODO(),
    "project_id",
    openai.AdminOrganizationProjectModelPermissionUpdateParams{
      Mode: openai.AdminOrganizationProjectModelPermissionUpdateParamsModeAllowList,
      ModelIDs: []string{"string"},
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", projectModelPermissions.ModelIDs)

    "object": "project.model_permissions",
    "mode": "deny_list",
    "model_ids": [
        "o3"
    ]

##### Returns Examples

    "object": "project.model_permissions",
    "mode": "deny_list",
    "model_ids": [
        "o3"
    ]
