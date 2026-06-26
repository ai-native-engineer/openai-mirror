<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/projects/methods/archive/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Admin](/api/reference/go/resources/admin)

[Organization](/api/reference/go/resources/admin/subresources/organization)

[Projects](/api/reference/go/resources/admin/subresources/organization/subresources/projects)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Archive project

client.Admin.Organization.Projects.Archive(ctx, projectID) (\*[Project](/api/reference/go/resources/admin#(resource)%20admin.organization.projects%20%3E%20(model)%20project%20%3E%20(schema)), error)

POST/organization/projects/{project\_id}/archive

Archives a project in the organization. Archived projects cannot be used or updated.

##### ParametersExpand Collapse

projectID string

##### ReturnsExpand Collapse

type Project struct{…}

Represents an individual project.

ID string

The identifier, which can be referenced in API endpoints

CreatedAt int64

The Unix timestamp (in seconds) of when the project was created.

formatunixtime

Object OrganizationProject

The object type, which is always `organization.project`

ArchivedAt int64Optional

The Unix timestamp (in seconds) of when the project was archived or `null`.

formatunixtime

ExternalKeyID stringOptional

The external key associated with the project.

Name stringOptional

The name of the project. This appears in reporting.

Status stringOptional

`active` or `archived`

### Archive project

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
  project, err := client.Admin.Organization.Projects.Archive(context.TODO(), "project_id")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", project.ID)

    "id": "proj_abc",
    "object": "organization.project",
    "name": "Project DEF",
    "created_at": 1711471533,
    "archived_at": 1711471533,
    "status": "archived"

##### Returns Examples

    "id": "proj_abc",
    "object": "organization.project",
    "name": "Project DEF",
    "created_at": 1711471533,
    "archived_at": 1711471533,
    "status": "archived"
