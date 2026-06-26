<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/admin_api_keys/methods/delete/ -->

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

# Delete admin API key

client.Admin.Organization.AdminAPIKeys.Delete(ctx, keyID) (\*[AdminOrganizationAdminAPIKeyDeleteResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20AdminOrganizationAdminAPIKeyDeleteResponse%20%3E%20(schema)), error)

DELETE/organization/admin\_api\_keys/{key\_id}

Delete an organization admin API key

##### ParametersExpand Collapse

keyID string

The ID of the API key to be deleted.

##### ReturnsExpand Collapse

type AdminOrganizationAdminAPIKeyDeleteResponse struct{…}

ID string

Deleted bool

Object OrganizationAdminAPIKeyDeleted

### Delete admin API key

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
  adminAPIKey, err := client.Admin.Organization.AdminAPIKeys.Delete(context.TODO(), "key_id")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", adminAPIKey.ID)

  "id": "key_abc",
  "object": "organization.admin_api_key.deleted",
  "deleted": true

##### Returns Examples

  "id": "key_abc",
  "object": "organization.admin_api_key.deleted",
  "deleted": true
