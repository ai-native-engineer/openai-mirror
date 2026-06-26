<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/methods/delete/ -->

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

# Delete project model permissions

client.Admin.Organization.Projects.ModelPermissions.Delete(ctx, projectID) (\*[ProjectModelPermissionsDeleted](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.model_permissions%20%3E%20(model)%20project_model_permissions_deleted%20%3E%20(schema)), error)

DELETE/organization/projects/{project\_id}/model\_permissions

Deletes model permissions for a project.

##### ParametersExpand Collapse

projectID string

##### ReturnsExpand Collapse

type ProjectModelPermissionsDeleted struct{…}

Confirmation payload returned after deleting project model permissions.

Deleted bool

Whether the project model permissions were deleted.

Object ProjectModelPermissionsDeleted

The object type, which is always `project.model_permissions.deleted`.

### Delete project model permissions

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
  projectModelPermissionsDeleted, err := client.Admin.Organization.Projects.ModelPermissions.Delete(context.TODO(), "project_id")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", projectModelPermissionsDeleted.Deleted)

    "object": "project.model_permissions.deleted",
    "deleted": true

##### Returns Examples

    "object": "project.model_permissions.deleted",
    "deleted": true
