<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/projects/methods/update/ -->

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

# Modify project

client.Admin.Organization.Projects.Update(ctx, projectID, body) (\*[Project](/api/reference/go/resources/admin#(resource)%20admin.organization.projects%20%3E%20(model)%20project%20%3E%20(schema)), error)

POST/organization/projects/{project\_id}

Modifies a project in the organization.

##### ParametersExpand Collapse

projectID string

body AdminOrganizationProjectUpdateParams

ExternalKeyID param.Field[string]Optional

External key ID to associate with the project.

Geography param.Field[string]Optional

Geography for the project.

Name param.Field[string]Optional

The updated name of the project, this name appears in reports.

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

### Modify project

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
  project, err := client.Admin.Organization.Projects.Update(
    context.TODO(),
    "project_id",
    openai.AdminOrganizationProjectUpdateParams{

  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", project.ID)

200 example

  "id": "id",
  "created_at": 0,
  "object": "organization.project",
  "archived_at": 0,
  "external_key_id": "external_key_id",
  "name": "name",
  "status": "status"

##### Returns Examples

200 example

  "id": "id",
  "created_at": 0,
  "object": "organization.project",
  "archived_at": 0,
  "external_key_id": "external_key_id",
  "name": "name",
  "status": "status"
