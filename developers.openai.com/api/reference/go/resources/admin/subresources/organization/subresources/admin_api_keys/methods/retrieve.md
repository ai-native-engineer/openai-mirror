<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/admin_api_keys/methods/retrieve/ -->

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

# Retrieve admin API key

client.Admin.Organization.AdminAPIKeys.Get(ctx, keyID) (\*[AdminAPIKey](/api/reference/go/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key%20%3E%20(schema)), error)

GET/organization/admin\_api\_keys/{key\_id}

Retrieve a single organization API key

##### ParametersExpand Collapse

keyID string

The ID of the API key.

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

### Retrieve admin API key

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
  adminAPIKey, err := client.Admin.Organization.AdminAPIKeys.Get(context.TODO(), "key_id")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", adminAPIKey.ID)

  "object": "organization.admin_api_key",
  "id": "key_abc",
  "name": "Main Admin Key",
  "redacted_value": "sk-admin...xyz",
  "created_at": 1711471533,
  "last_used_at": 1711471534,
  "owner": {
    "type": "user",
    "object": "organization.user",
    "id": "user_123",
    "name": "John Doe",
    "created_at": 1711471533,
    "role": "owner"

##### Returns Examples

  "object": "organization.admin_api_key",
  "id": "key_abc",
  "name": "Main Admin Key",
  "redacted_value": "sk-admin...xyz",
  "created_at": 1711471533,
  "last_used_at": 1711471534,
  "owner": {
    "type": "user",
    "object": "organization.user",
    "id": "user_123",
    "name": "John Doe",
    "created_at": 1711471533,
    "role": "owner"
