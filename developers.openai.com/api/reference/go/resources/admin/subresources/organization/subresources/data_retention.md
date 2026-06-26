<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/data_retention/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Admin](/api/reference/go/resources/admin)

[Organization](/api/reference/go/resources/admin/subresources/organization)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Data Retention

##### [Retrieve organization data retention](/api/reference/go/resources/admin/subresources/organization/subresources/data_retention/methods/retrieve)

client.Admin.Organization.DataRetention.Get(ctx) (\*[OrganizationDataRetention](/api/reference/go/resources/admin#(resource)%20admin.organization.data_retention%20%3E%20(model)%20organization_data_retention%20%3E%20(schema)), error)

GET/organization/data\_retention

##### [Update organization data retention](/api/reference/go/resources/admin/subresources/organization/subresources/data_retention/methods/update)

client.Admin.Organization.DataRetention.Update(ctx, body) (\*[OrganizationDataRetention](/api/reference/go/resources/admin#(resource)%20admin.organization.data_retention%20%3E%20(model)%20organization_data_retention%20%3E%20(schema)), error)

POST/organization/data\_retention

##### ModelsExpand Collapse

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
