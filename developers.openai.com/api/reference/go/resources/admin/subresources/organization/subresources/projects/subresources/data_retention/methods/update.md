<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/data_retention/methods/update/ -->

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

# Update project data retention

client.Admin.Organization.Projects.DataRetention.Update(ctx, projectID, body) (\*[ProjectDataRetention](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.data_retention%20%3E%20(model)%20project_data_retention%20%3E%20(schema)), error)

POST/organization/projects/{project\_id}/data\_retention

Updates project data retention controls.

##### ParametersExpand Collapse

projectID string

body AdminOrganizationProjectDataRetentionUpdateParams

RetentionType param.Field[[AdminOrganizationProjectDataRetentionUpdateParamsRetentionType](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/data_retention/methods/update#(resource)%20admin.organization.projects.data_retention%20%3E%20(method)%20update%20%3E%20(params)%20default%20%3E%20(param)%20retention_type%20%3E%20(schema))]

The desired project data retention type.

const AdminOrganizationProjectDataRetentionUpdateParamsRetentionTypeOrganizationDefault [AdminOrganizationProjectDataRetentionUpdateParamsRetentionType](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/data_retention/methods/update#(resource)%20admin.organization.projects.data_retention%20%3E%20(method)%20update%20%3E%20(params)%20default%20%3E%20(param)%20retention_type%20%3E%20(schema)) = "organization\_default"

const AdminOrganizationProjectDataRetentionUpdateParamsRetentionTypeNone [AdminOrganizationProjectDataRetentionUpdateParamsRetentionType](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/data_retention/methods/update#(resource)%20admin.organization.projects.data_retention%20%3E%20(method)%20update%20%3E%20(params)%20default%20%3E%20(param)%20retention_type%20%3E%20(schema)) = "none"

const AdminOrganizationProjectDataRetentionUpdateParamsRetentionTypeZeroDataRetention [AdminOrganizationProjectDataRetentionUpdateParamsRetentionType](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/data_retention/methods/update#(resource)%20admin.organization.projects.data_retention%20%3E%20(method)%20update%20%3E%20(params)%20default%20%3E%20(param)%20retention_type%20%3E%20(schema)) = "zero\_data\_retention"

const AdminOrganizationProjectDataRetentionUpdateParamsRetentionTypeModifiedAbuseMonitoring [AdminOrganizationProjectDataRetentionUpdateParamsRetentionType](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/data_retention/methods/update#(resource)%20admin.organization.projects.data_retention%20%3E%20(method)%20update%20%3E%20(params)%20default%20%3E%20(param)%20retention_type%20%3E%20(schema)) = "modified\_abuse\_monitoring"

const AdminOrganizationProjectDataRetentionUpdateParamsRetentionTypeEnhancedZeroDataRetention [AdminOrganizationProjectDataRetentionUpdateParamsRetentionType](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/data_retention/methods/update#(resource)%20admin.organization.projects.data_retention%20%3E%20(method)%20update%20%3E%20(params)%20default%20%3E%20(param)%20retention_type%20%3E%20(schema)) = "enhanced\_zero\_data\_retention"

const AdminOrganizationProjectDataRetentionUpdateParamsRetentionTypeEnhancedModifiedAbuseMonitoring [AdminOrganizationProjectDataRetentionUpdateParamsRetentionType](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/data_retention/methods/update#(resource)%20admin.organization.projects.data_retention%20%3E%20(method)%20update%20%3E%20(params)%20default%20%3E%20(param)%20retention_type%20%3E%20(schema)) = "enhanced\_modified\_abuse\_monitoring"

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

### Update project data retention

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
  projectDataRetention, err := client.Admin.Organization.Projects.DataRetention.Update(
    context.TODO(),
    "project_id",
    openai.AdminOrganizationProjectDataRetentionUpdateParams{
      RetentionType: openai.AdminOrganizationProjectDataRetentionUpdateParamsRetentionTypeOrganizationDefault,
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", projectDataRetention.Object)

    "object": "project.data_retention",
    "type": "modified_abuse_monitoring"

##### Returns Examples

    "object": "project.data_retention",
    "type": "modified_abuse_monitoring"
