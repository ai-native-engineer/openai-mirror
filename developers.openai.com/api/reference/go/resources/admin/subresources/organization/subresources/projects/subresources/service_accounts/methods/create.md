<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/create/ -->

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

# Create project service account

client.Admin.Organization.Projects.ServiceAccounts.New(ctx, projectID, body) (\*[AdminOrganizationProjectServiceAccountNewResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20AdminOrganizationProjectServiceAccountNewResponse%20%3E%20(schema)), error)

POST/organization/projects/{project\_id}/service\_accounts

Creates a new service account in the project. This also returns an unredacted API key for the service account.

##### ParametersExpand Collapse

projectID string

body AdminOrganizationProjectServiceAccountNewParams

Name param.Field[string]

The name of the service account being created.

##### ReturnsExpand Collapse

type AdminOrganizationProjectServiceAccountNewResponse struct{…}

ID string

APIKey AdminOrganizationProjectServiceAccountNewResponseAPIKey

ID string

CreatedAt int64

formatunixtime

Name string

Object OrganizationProjectServiceAccountAPIKey

The object type, which is always `organization.project.service_account.api_key`

Value string

CreatedAt int64

formatunixtime

Name string

Object OrganizationProjectServiceAccount

Role Member

Service accounts can only have one role of type `member`

### Create project service account

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
  serviceAccount, err := client.Admin.Organization.Projects.ServiceAccounts.New(
    context.TODO(),
    "project_id",
    openai.AdminOrganizationProjectServiceAccountNewParams{
      Name: "name",
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", serviceAccount.ID)

    "object": "organization.project.service_account",
    "id": "svc_acct_abc",
    "name": "Production App",
    "role": "member",
    "created_at": 1711471533,
    "api_key": {
        "object": "organization.project.service_account.api_key",
        "value": "sk-abcdefghijklmnop123",
        "name": "Secret Key",
        "created_at": 1711471533,
        "id": "key_abc"

##### Returns Examples

    "object": "organization.project.service_account",
    "id": "svc_acct_abc",
    "name": "Production App",
    "role": "member",
    "created_at": 1711471533,
    "api_key": {
        "object": "organization.project.service_account.api_key",
        "value": "sk-abcdefghijklmnop123",
        "name": "Secret Key",
        "created_at": 1711471533,
        "id": "key_abc"
