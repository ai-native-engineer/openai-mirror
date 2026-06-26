<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Admin](/api/reference/go/resources/admin)

[Organization](/api/reference/go/resources/admin/subresources/organization)

[Projects](/api/reference/go/resources/admin/subresources/organization/subresources/projects)

[Service Accounts](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve project service account

client.Admin.Organization.Projects.ServiceAccounts.Get(ctx, projectID, serviceAccountID) (\*[ProjectServiceAccount](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20project_service_account%20%3E%20(schema)), error)

GET/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}

Retrieves a service account in the project.

##### ParametersExpand Collapse

projectID string

serviceAccountID string

##### ReturnsExpand Collapse

type ProjectServiceAccount struct{…}

Represents an individual service account in a project.

ID string

The identifier, which can be referenced in API endpoints

CreatedAt int64

The Unix timestamp (in seconds) of when the service account was created

formatunixtime

Name string

The name of the service account

Object OrganizationProjectServiceAccount

The object type, which is always `organization.project.service_account`

Role ProjectServiceAccountRole

`owner` or `member`

One of the following:

const ProjectServiceAccountRoleOwner ProjectServiceAccountRole = "owner"

const ProjectServiceAccountRoleMember ProjectServiceAccountRole = "member"

### Retrieve project service account

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
  projectServiceAccount, err := client.Admin.Organization.Projects.ServiceAccounts.Get(
    context.TODO(),
    "project_id",
    "service_account_id",
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", projectServiceAccount.ID)

    "object": "organization.project.service_account",
    "id": "svc_acct_abc",
    "name": "Service Account",
    "role": "owner",
    "created_at": 1711471533

##### Returns Examples

    "object": "organization.project.service_account",
    "id": "svc_acct_abc",
    "name": "Service Account",
    "role": "owner",
    "created_at": 1711471533
