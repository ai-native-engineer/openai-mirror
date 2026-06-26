<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/delete/ -->

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

# Delete project API key

client.Admin.Organization.Projects.APIKeys.Delete(ctx, projectID, apiKeyID) (\*[AdminOrganizationProjectAPIKeyDeleteResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20AdminOrganizationProjectAPIKeyDeleteResponse%20%3E%20(schema)), error)

DELETE/organization/projects/{project\_id}/api\_keys/{api\_key\_id}

Deletes an API key from the project.

Returns confirmation of the key deletion, or an error if the key belonged to
a service account.

##### ParametersExpand Collapse

projectID string

apiKeyID string

##### ReturnsExpand Collapse

type AdminOrganizationProjectAPIKeyDeleteResponse struct{…}

ID string

Deleted bool

Object OrganizationProjectAPIKeyDeleted

### Delete project API key

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
  apiKey, err := client.Admin.Organization.Projects.APIKeys.Delete(
    context.TODO(),
    "project_id",
    "api_key_id",
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", apiKey.ID)

    "object": "organization.project.api_key.deleted",
    "id": "key_abc",
    "deleted": true

##### Returns Examples

    "object": "organization.project.api_key.deleted",
    "id": "key_abc",
    "deleted": true
