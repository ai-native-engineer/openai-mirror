<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/data_retention/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Admin](/api/reference/typescript/resources/admin)

[Organization](/api/reference/typescript/resources/admin/subresources/organization)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Data Retention

##### [Retrieve organization data retention](/api/reference/typescript/resources/admin/subresources/organization/subresources/data_retention/methods/retrieve)

client.admin.organization.dataRetention.retrieve(RequestOptionsoptions?): [OrganizationDataRetention](/api/reference/typescript/resources/admin#(resource)%20admin.organization.data_retention%20%3E%20(model)%20organization_data_retention%20%3E%20(schema)) { object, type }

GET/organization/data\_retention

##### [Update organization data retention](/api/reference/typescript/resources/admin/subresources/organization/subresources/data_retention/methods/update)

client.admin.organization.dataRetention.update(DataRetentionUpdateParams { retention\_type } body, RequestOptionsoptions?): [OrganizationDataRetention](/api/reference/typescript/resources/admin#(resource)%20admin.organization.data_retention%20%3E%20(model)%20organization_data_retention%20%3E%20(schema)) { object, type }

POST/organization/data\_retention

##### ModelsExpand Collapse

OrganizationDataRetention { object, type }

Represents the organization’s data retention control setting.

object: "organization.data\_retention"

The object type, which is always `organization.data_retention`.

type: "zero\_data\_retention" | "modified\_abuse\_monitoring" | "enhanced\_zero\_data\_retention" | "enhanced\_modified\_abuse\_monitoring"

The configured organization data retention type.

One of the following:

"zero\_data\_retention"

"modified\_abuse\_monitoring"

"enhanced\_zero\_data\_retention"

"enhanced\_modified\_abuse\_monitoring"
