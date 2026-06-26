<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Admin](/api/reference/go/resources/admin)

[Organization](/api/reference/go/resources/admin/subresources/organization)

[Projects](/api/reference/go/resources/admin/subresources/organization/subresources/projects)

[API Keys](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/api_keys)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve project API key

client.Admin.Organization.Projects.APIKeys.Get(ctx, projectID, apiKeyID) (\*[ProjectAPIKey](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)), error)

GET/organization/projects/{project\_id}/api\_keys/{api\_key\_id}

Retrieves an API key in the project.

##### ParametersExpand Collapse

projectID string

apiKeyID string

##### ReturnsExpand Collapse

type ProjectAPIKey struct{…}

Represents an individual API key in a project.

ID string

The identifier, which can be referenced in API endpoints

CreatedAt int64

The Unix timestamp (in seconds) of when the API key was created

formatunixtime

LastUsedAt int64

The Unix timestamp (in seconds) of when the API key was last used.

formatunixtime

Name string

The name of the API key

Object OrganizationProjectAPIKey

The object type, which is always `organization.project.api_key`

Owner ProjectAPIKeyOwner

ServiceAccount ProjectAPIKeyOwnerServiceAccountOptional

The service account that owns a project API key.

ID string

The identifier, which can be referenced in API endpoints

CreatedAt int64

The Unix timestamp (in seconds) of when the service account was created.

formatunixtime

Name string

The name of the service account.

Role string

The service account’s project role.

Type stringOptional

`user` or `service_account`

One of the following:

const ProjectAPIKeyOwnerTypeUser ProjectAPIKeyOwnerType = "user"

const ProjectAPIKeyOwnerTypeServiceAccount ProjectAPIKeyOwnerType = "service\_account"

User ProjectAPIKeyOwnerUserOptional

The user that owns a project API key.

ID string

The identifier, which can be referenced in API endpoints

CreatedAt int64

The Unix timestamp (in seconds) of when the user was created.

formatunixtime

Email string

The email address of the user.

Name string

The name of the user.

Role string

The user’s project role.

RedactedValue string

The redacted value of the API key

### Retrieve project API key

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
  projectAPIKey, err := client.Admin.Organization.Projects.APIKeys.Get(
    context.TODO(),
    "project_id",
    "api_key_id",
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", projectAPIKey.ID)

    "object": "organization.project.api_key",
    "redacted_value": "sk-abc...def",
    "name": "My API Key",
    "created_at": 1711471533,
    "last_used_at": 1711471534,
    "id": "key_abc",
    "owner": {
        "type": "user",
        "user": {
            "id": "user_abc",
            "name": "First Last",
            "email": "user@example.com",
            "role": "owner",
            "created_at": 1711471533

##### Returns Examples

    "object": "organization.project.api_key",
    "redacted_value": "sk-abc...def",
    "name": "My API Key",
    "created_at": 1711471533,
    "last_used_at": 1711471534,
    "id": "key_abc",
    "owner": {
        "type": "user",
        "user": {
            "id": "user_abc",
            "name": "First Last",
            "email": "user@example.com",
            "role": "owner",
            "created_at": 1711471533
