<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/data_retention/methods/update/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Admin](/api/reference/go/resources/admin)

[Organization](/api/reference/go/resources/admin/subresources/organization)

[Data Retention](/api/reference/go/resources/admin/subresources/organization/subresources/data_retention)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Update organization data retention

client.Admin.Organization.DataRetention.Update(ctx, body) (\*[OrganizationDataRetention](/api/reference/go/resources/admin#(resource)%20admin.organization.data_retention%20%3E%20(model)%20organization_data_retention%20%3E%20(schema)), error)

POST/organization/data\_retention

Updates organization data retention controls.

##### ParametersExpand Collapse

body AdminOrganizationDataRetentionUpdateParams

RetentionType param.Field[[AdminOrganizationDataRetentionUpdateParamsRetentionType](/api/reference/go/resources/admin/subresources/organization/subresources/data_retention/methods/update#(resource)%20admin.organization.data_retention%20%3E%20(method)%20update%20%3E%20(params)%20default%20%3E%20(param)%20retention_type%20%3E%20(schema))]

The desired organization data retention type.

const AdminOrganizationDataRetentionUpdateParamsRetentionTypeZeroDataRetention [AdminOrganizationDataRetentionUpdateParamsRetentionType](/api/reference/go/resources/admin/subresources/organization/subresources/data_retention/methods/update#(resource)%20admin.organization.data_retention%20%3E%20(method)%20update%20%3E%20(params)%20default%20%3E%20(param)%20retention_type%20%3E%20(schema)) = "zero\_data\_retention"

const AdminOrganizationDataRetentionUpdateParamsRetentionTypeModifiedAbuseMonitoring [AdminOrganizationDataRetentionUpdateParamsRetentionType](/api/reference/go/resources/admin/subresources/organization/subresources/data_retention/methods/update#(resource)%20admin.organization.data_retention%20%3E%20(method)%20update%20%3E%20(params)%20default%20%3E%20(param)%20retention_type%20%3E%20(schema)) = "modified\_abuse\_monitoring"

const AdminOrganizationDataRetentionUpdateParamsRetentionTypeEnhancedZeroDataRetention [AdminOrganizationDataRetentionUpdateParamsRetentionType](/api/reference/go/resources/admin/subresources/organization/subresources/data_retention/methods/update#(resource)%20admin.organization.data_retention%20%3E%20(method)%20update%20%3E%20(params)%20default%20%3E%20(param)%20retention_type%20%3E%20(schema)) = "enhanced\_zero\_data\_retention"

const AdminOrganizationDataRetentionUpdateParamsRetentionTypeEnhancedModifiedAbuseMonitoring [AdminOrganizationDataRetentionUpdateParamsRetentionType](/api/reference/go/resources/admin/subresources/organization/subresources/data_retention/methods/update#(resource)%20admin.organization.data_retention%20%3E%20(method)%20update%20%3E%20(params)%20default%20%3E%20(param)%20retention_type%20%3E%20(schema)) = "enhanced\_modified\_abuse\_monitoring"

##### ReturnsExpand Collapse

type OrganizationDataRetention struct{…}

Represents the organization’s data retention control setting.

Object OrganizationDataRetention

The object type, which is always `organization.data_retention`.

Type OrganizationDataRetentionType

The configured organization data retention type.

One of the following:

const OrganizationDataRetentionTypeZeroDataRetention OrganizationDataRetentionType = "zero\_data\_retention"

const OrganizationDataRetentionTypeModifiedAbuseMonitoring OrganizationDataRetentionType = "modified\_abuse\_monitoring"

const OrganizationDataRetentionTypeEnhancedZeroDataRetention OrganizationDataRetentionType = "enhanced\_zero\_data\_retention"

const OrganizationDataRetentionTypeEnhancedModifiedAbuseMonitoring OrganizationDataRetentionType = "enhanced\_modified\_abuse\_monitoring"

### Update organization data retention

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
  organizationDataRetention, err := client.Admin.Organization.DataRetention.Update(context.TODO(), openai.AdminOrganizationDataRetentionUpdateParams{
    RetentionType: openai.AdminOrganizationDataRetentionUpdateParamsRetentionTypeZeroDataRetention,
  })
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", organizationDataRetention.Object)

    "object": "organization.data_retention",
    "type": "modified_abuse_monitoring"

##### Returns Examples

    "object": "organization.data_retention",
    "type": "modified_abuse_monitoring"
