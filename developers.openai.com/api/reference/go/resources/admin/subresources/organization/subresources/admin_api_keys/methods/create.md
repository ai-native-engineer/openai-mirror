<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/admin_api_keys/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Admin](/api/reference/go/resources/admin)

[Organization](/api/reference/go/resources/admin/subresources/organization)

[Admin API Keys](/api/reference/go/resources/admin/subresources/organization/subresources/admin_api_keys)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create admin API key

client.Admin.Organization.AdminAPIKeys.New(ctx, body) (\*[AdminOrganizationAdminAPIKeyNewResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20AdminOrganizationAdminAPIKeyNewResponse%20%3E%20(schema)), error)

POST/organization/admin\_api\_keys

Create an organization admin API key

##### ParametersExpand Collapse

body AdminOrganizationAdminAPIKeyNewParams

Name param.Field[string]

ExpiresInSeconds param.Field[int64]Optional

The number of seconds until the API key expires. Omit this field for a key that does not expire.

minimum1

maximum31536000

##### ReturnsExpand Collapse

type AdminOrganizationAdminAPIKeyNewResponse struct{…}

Represents an individual Admin API key in an org.

Value string

The value of the API key. Only shown on create.

### Create admin API key

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
  adminAPIKey, err := client.Admin.Organization.AdminAPIKeys.New(context.TODO(), openai.AdminOrganizationAdminAPIKeyNewParams{
    Name: "New Admin Key",
  })
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", adminAPIKey)

  "object": "organization.admin_api_key",
  "id": "key_xyz",
  "name": "New Admin Key",
  "redacted_value": "sk-admin...xyz",
  "created_at": 1711471533,
  "expires_at": 1714063533,
  "last_used_at": 1711471534,
  "owner": {
    "type": "user",
    "object": "organization.user",
    "id": "user_123",
    "name": "John Doe",
    "created_at": 1711471533,
    "role": "owner"
  "value": "sk-admin-1234abcd"

##### Returns Examples

  "object": "organization.admin_api_key",
  "id": "key_xyz",
  "name": "New Admin Key",
  "redacted_value": "sk-admin...xyz",
  "created_at": 1711471533,
  "expires_at": 1714063533,
  "last_used_at": 1711471534,
  "owner": {
    "type": "user",
    "object": "organization.user",
    "id": "user_123",
    "name": "John Doe",
    "created_at": 1711471533,
    "role": "owner"
  "value": "sk-admin-1234abcd"
