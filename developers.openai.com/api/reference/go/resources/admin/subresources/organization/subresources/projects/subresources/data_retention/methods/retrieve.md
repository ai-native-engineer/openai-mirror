<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/data_retention/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Admin](/api/reference/go/resources/admin)

[Organization](/api/reference/go/resources/admin/subresources/organization)

[Projects](/api/reference/go/resources/admin/subresources/organization/subresources/projects)

[Data Retention](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/data_retention)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve project data retention

client.Admin.Organization.Projects.DataRetention.Get(ctx, projectID) (\*[ProjectDataRetention](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.data_retention%20%3E%20(model)%20project_data_retention%20%3E%20(schema)), error)

GET/organization/projects/{project\_id}/data\_retention

Retrieves project data retention controls.

##### ParametersExpand Collapse

projectID string

##### ReturnsExpand Collapse

type ProjectDataRetention struct{…}

Represents a project’s data retention control setting.

Object ProjectDataRetention

The object type, which is always `project.data_retention`.

Type ProjectDataRetentionType

The configured project data retention type.

One of the following:

const ProjectDataRetentionTypeOrganizationDefault ProjectDataRetentionType = "organization\_default"

const ProjectDataRetentionTypeNone ProjectDataRetentionType = "none"

const ProjectDataRetentionTypeZeroDataRetention ProjectDataRetentionType = "zero\_data\_retention"

const ProjectDataRetentionTypeModifiedAbuseMonitoring ProjectDataRetentionType = "modified\_abuse\_monitoring"

const ProjectDataRetentionTypeEnhancedZeroDataRetention ProjectDataRetentionType = "enhanced\_zero\_data\_retention"

const ProjectDataRetentionTypeEnhancedModifiedAbuseMonitoring ProjectDataRetentionType = "enhanced\_modified\_abuse\_monitoring"

### Retrieve project data retention

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
  projectDataRetention, err := client.Admin.Organization.Projects.DataRetention.Get(context.TODO(), "project_id")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", projectDataRetention.Object)

    "object": "project.data_retention",
    "type": "organization_default"

##### Returns Examples

    "object": "project.data_retention",
    "type": "organization_default"
