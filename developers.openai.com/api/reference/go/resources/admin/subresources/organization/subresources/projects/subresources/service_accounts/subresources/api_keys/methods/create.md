<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/subresources/api_keys/methods/create/ -->

[API Reference](/api/reference/go)

[Admin](/api/reference/go/resources/admin)

[Organization](/api/reference/go/resources/admin/subresources/organization)

[Projects](/api/reference/go/resources/admin/subresources/organization/subresources/projects)

[Service Accounts](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts)

[API Keys](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/subresources/api_keys)

# Create project service account API key

client.Admin.Organization.Projects.ServiceAccounts.APIKeys.New(ctx, projectID, serviceAccountID, body) (\*[AdminOrganizationProjectServiceAccountAPIKeyNewResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.service_accounts.api_keys%20%3E%20(model)%20AdminOrganizationProjectServiceAccountAPIKeyNewResponse%20%3E%20(schema)), error)

POST/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}/api\_keys

Creates an API key for a service account in the project.

##### ParametersExpand Collapse

projectID string

serviceAccountID string

body AdminOrganizationProjectServiceAccountAPIKeyNewParams

Name param.Field[string]Optional

API key name.

Scopes param.Field[[]string]Optional

API key scopes.

##### ReturnsExpand Collapse

type AdminOrganizationProjectServiceAccountAPIKeyNewResponse struct{…}

ID string

CreatedAt int64

formatunixtime

Name string

Object OrganizationProjectServiceAccountAPIKey

The object type, which is always `organization.project.service_account.api_key`

Value string

### Create project service account API key

Go

package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAdminAPIKey("My Admin API Key"),
  )
  apiKey, err := client.Admin.Organization.Projects.ServiceAccounts.APIKeys.New(
    context.TODO(),
    "project_id",
    "service_account_id",
    openai.AdminOrganizationProjectServiceAccountAPIKeyNewParams{

    },
  )
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", apiKey.ID)

    "object": "organization.project.service_account.api_key",
    "value": "sk-abcdefghijklmnop123",
    "name": "Production App",
    "created_at": 1711471533,
    "id": "key_abc"

    "object": "organization.project.service_account.api_key",
    "value": "sk-abcdefghijklmnop123",
    "name": "Production App",
    "created_at": 1711471533,
    "id": "key_abc"
