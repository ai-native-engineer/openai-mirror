<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Admin](/api/reference/go/resources/admin)

[Organization](/api/reference/go/resources/admin/subresources/organization)

[Projects](/api/reference/go/resources/admin/subresources/organization/subresources/projects)

[Users](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/users)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create project user

client.Admin.Organization.Projects.Users.New(ctx, projectID, body) (\*[ProjectUser](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.users%20%3E%20(model)%20project_user%20%3E%20(schema)), error)

POST/organization/projects/{project\_id}/users

Adds a user to the project. Users must already be members of the organization to be added to a project.

##### ParametersExpand Collapse

projectID string

body AdminOrganizationProjectUserNewParams

Role param.Field[string]

`owner` or `member`

Email param.Field[string]Optional

Email of the user to add.

UserID param.Field[string]Optional

The ID of the user.

##### ReturnsExpand Collapse

type ProjectUser struct{…}

Represents an individual user in a project.

ID string

The identifier, which can be referenced in API endpoints

AddedAt int64

The Unix timestamp (in seconds) of when the project was added.

formatunixtime

Object OrganizationProjectUser

The object type, which is always `organization.project.user`

Role string

`owner` or `member`

Email stringOptional

The email address of the user

Name stringOptional

The name of the user

### Create project user

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
  projectUser, err := client.Admin.Organization.Projects.Users.New(
    context.TODO(),
    "project_id",
    openai.AdminOrganizationProjectUserNewParams{
      Role: "role",
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", projectUser.ID)

    "object": "organization.project.user",
    "id": "user_abc",
    "email": "user@example.com",
    "role": "owner",
    "added_at": 1711471533

##### Returns Examples

    "object": "organization.project.user",
    "id": "user_abc",
    "email": "user@example.com",
    "role": "owner",
    "added_at": 1711471533
