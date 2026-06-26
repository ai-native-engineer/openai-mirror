<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/methods/retrieve/ -->

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

# Retrieve project model permissions

client.Admin.Organization.Projects.ModelPermissions.Get(ctx, projectID) (\*[ProjectModelPermissions](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.model_permissions%20%3E%20(model)%20project_model_permissions%20%3E%20(schema)), error)

GET/organization/projects/{project\_id}/model\_permissions

Returns model permissions for a project.

##### ParametersExpand Collapse

projectID string

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

### Retrieve project model permissions

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
  projectModelPermissions, err := client.Admin.Organization.Projects.ModelPermissions.Get(context.TODO(), "project_id")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", projectModelPermissions.ModelIDs)

    "object": "project.model_permissions",
    "mode": "allow_list",
    "model_ids": [
        "gpt-4.1",
        "o3"
    ]

##### Returns Examples

    "object": "project.model_permissions",
    "mode": "allow_list",
    "model_ids": [
        "gpt-4.1",
        "o3"
    ]
