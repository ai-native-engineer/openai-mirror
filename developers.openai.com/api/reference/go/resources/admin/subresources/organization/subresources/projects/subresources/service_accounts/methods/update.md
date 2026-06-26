<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/update/ -->

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

# Update project service account

client.Admin.Organization.Projects.ServiceAccounts.Update(ctx, projectID, serviceAccountID, body) (\*[ProjectServiceAccount](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20project_service_account%20%3E%20(schema)), error)

POST/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}

Updates a service account in the project.

##### ParametersExpand Collapse

projectID string

serviceAccountID string

body AdminOrganizationProjectServiceAccountUpdateParams

Name param.Field[string]Optional

The updated service account name.

Role param.Field[[AdminOrganizationProjectServiceAccountUpdateParamsRole](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/update#(resource)%20admin.organization.projects.service_accounts%20%3E%20(method)%20update%20%3E%20(params)%20default%20%3E%20(param)%20role%20%3E%20(schema))]Optional

The updated service account role.

const AdminOrganizationProjectServiceAccountUpdateParamsRoleMember [AdminOrganizationProjectServiceAccountUpdateParamsRole](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/update#(resource)%20admin.organization.projects.service_accounts%20%3E%20(method)%20update%20%3E%20(params)%20default%20%3E%20(param)%20role%20%3E%20(schema)) = "member"

const AdminOrganizationProjectServiceAccountUpdateParamsRoleOwner [AdminOrganizationProjectServiceAccountUpdateParamsRole](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/update#(resource)%20admin.organization.projects.service_accounts%20%3E%20(method)%20update%20%3E%20(params)%20default%20%3E%20(param)%20role%20%3E%20(schema)) = "owner"

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

### Update project service account

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
  projectServiceAccount, err := client.Admin.Organization.Projects.ServiceAccounts.Update(
    context.TODO(),
    "project_id",
    "service_account_id",
    openai.AdminOrganizationProjectServiceAccountUpdateParams{

  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", projectServiceAccount.ID)

    "object": "organization.project.service_account",
    "id": "svc_acct_abc",
    "name": "Updated service account",
    "role": "member",
    "created_at": 1711471533

##### Returns Examples

    "object": "organization.project.service_account",
    "id": "svc_acct_abc",
    "name": "Updated service account",
    "role": "member",
    "created_at": 1711471533
