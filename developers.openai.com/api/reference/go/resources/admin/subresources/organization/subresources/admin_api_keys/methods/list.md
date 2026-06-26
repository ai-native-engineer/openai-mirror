<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/admin_api_keys/methods/list/ -->

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

# List all organization and project API keys.

client.Admin.Organization.AdminAPIKeys.List(ctx, query) (\*CursorPage[[AdminAPIKey](/api/reference/go/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key%20%3E%20(schema))], error)

GET/organization/admin\_api\_keys

List organization API keys

##### ParametersExpand Collapse

query AdminOrganizationAdminAPIKeyListParams

After param.Field[string]Optional

Return keys with IDs that come after this ID in the pagination order.

Limit param.Field[int64]Optional

Maximum number of keys to return.

Order param.Field[[AdminOrganizationAdminAPIKeyListParamsOrder](/api/reference/go/resources/admin/subresources/organization/subresources/admin_api_keys/methods/list#(resource)%20admin.organization.admin_api_keys%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))]Optional

Order results by creation time, ascending or descending.

const AdminOrganizationAdminAPIKeyListParamsOrderAsc [AdminOrganizationAdminAPIKeyListParamsOrder](/api/reference/go/resources/admin/subresources/organization/subresources/admin_api_keys/methods/list#(resource)%20admin.organization.admin_api_keys%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)) = "asc"

const AdminOrganizationAdminAPIKeyListParamsOrderDesc [AdminOrganizationAdminAPIKeyListParamsOrder](/api/reference/go/resources/admin/subresources/organization/subresources/admin_api_keys/methods/list#(resource)%20admin.organization.admin_api_keys%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)) = "desc"

##### ReturnsExpand Collapse

type AdminAPIKey struct{…}

Represents an individual Admin API key in an org.

ID string

The identifier, which can be referenced in API endpoints

CreatedAt int64

The Unix timestamp (in seconds) of when the API key was created

formatunixtime

ExpiresAt int64

The Unix timestamp (in seconds) of when the API key expires

formatunixtime

Object OrganizationAdminAPIKey

The object type, which is always `organization.admin_api_key`

Owner AdminAPIKeyOwner

ID stringOptional

The identifier, which can be referenced in API endpoints

CreatedAt int64Optional

The Unix timestamp (in seconds) of when the user was created

formatunixtime

Name stringOptional

The name of the user

Object stringOptional

The object type, which is always organization.user

Role stringOptional

Always `owner`

Type stringOptional

Always `user`

RedactedValue string

The redacted value of the API key

LastUsedAt int64Optional

The Unix timestamp (in seconds) of when the API key was last used

formatunixtime

Name stringOptional

The name of the API key

### List all organization and project API keys.

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
  page, err := client.Admin.Organization.AdminAPIKeys.List(context.TODO(), openai.AdminOrganizationAdminAPIKeyListParams{

  })
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", page)

  "object": "list",
  "data": [
      "object": "organization.admin_api_key",
      "id": "key_abc",
      "name": "Main Admin Key",
      "redacted_value": "sk-admin...def",
      "created_at": 1711471533,
      "expires_at": 1714063533,
      "last_used_at": 1711471534,
      "owner": {
        "type": "service_account",
        "object": "organization.service_account",
        "id": "sa_456",
        "name": "My Service Account",
        "created_at": 1711471533,
        "role": "member"
  ],
  "first_id": "key_abc",
  "last_id": "key_abc",
  "has_more": false

##### Returns Examples

  "object": "list",
  "data": [
      "object": "organization.admin_api_key",
      "id": "key_abc",
      "name": "Main Admin Key",
      "redacted_value": "sk-admin...def",
      "created_at": 1711471533,
      "expires_at": 1714063533,
      "last_used_at": 1711471534,
      "owner": {
        "type": "service_account",
        "object": "organization.service_account",
        "id": "sa_456",
        "name": "My Service Account",
        "created_at": 1711471533,
        "role": "member"
  ],
  "first_id": "key_abc",
  "last_id": "key_abc",
  "has_more": false
