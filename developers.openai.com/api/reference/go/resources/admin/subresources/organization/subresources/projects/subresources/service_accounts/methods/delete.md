<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/delete/ -->

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

# Delete project service account

client.Admin.Organization.Projects.ServiceAccounts.Delete(ctx, projectID, serviceAccountID) (\*[AdminOrganizationProjectServiceAccountDeleteResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20AdminOrganizationProjectServiceAccountDeleteResponse%20%3E%20(schema)), error)

DELETE/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}

Deletes a service account from the project.

Returns confirmation of service account deletion, or an error if the project
is archived (archived projects have no service accounts).

##### ParametersExpand Collapse

projectID string

serviceAccountID string

##### ReturnsExpand Collapse

type AdminOrganizationProjectServiceAccountDeleteResponse struct{…}

ID string

Deleted bool

Object OrganizationProjectServiceAccountDeleted

### Delete project service account

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
  serviceAccount, err := client.Admin.Organization.Projects.ServiceAccounts.Delete(
    context.TODO(),
    "project_id",
    "service_account_id",
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", serviceAccount.ID)

    "object": "organization.project.service_account.deleted",
    "id": "svc_acct_abc",
    "deleted": true

##### Returns Examples

    "object": "organization.project.service_account.deleted",
    "id": "svc_acct_abc",
    "deleted": true
