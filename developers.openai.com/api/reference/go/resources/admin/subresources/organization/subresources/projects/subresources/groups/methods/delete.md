<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Admin](/api/reference/go/resources/admin)

[Organization](/api/reference/go/resources/admin/subresources/organization)

[Projects](/api/reference/go/resources/admin/subresources/organization/subresources/projects)

[Groups](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/groups)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Remove project group

client.Admin.Organization.Projects.Groups.Delete(ctx, projectID, groupID) (\*[AdminOrganizationProjectGroupDeleteResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20AdminOrganizationProjectGroupDeleteResponse%20%3E%20(schema)), error)

DELETE/organization/projects/{project\_id}/groups/{group\_id}

Revokes a group’s access to a project.

##### ParametersExpand Collapse

projectID string

groupID string

##### ReturnsExpand Collapse

type AdminOrganizationProjectGroupDeleteResponse struct{…}

Confirmation payload returned after removing a group from a project.

Deleted bool

Whether the group membership in the project was removed.

Object ProjectGroupDeleted

Always `project.group.deleted`.

### Remove project group

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
  group, err := client.Admin.Organization.Projects.Groups.Delete(
    context.TODO(),
    "project_id",
    "group_id",
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", group.Deleted)

    "object": "project.group.deleted",
    "deleted": true

##### Returns Examples

    "object": "project.group.deleted",
    "deleted": true
