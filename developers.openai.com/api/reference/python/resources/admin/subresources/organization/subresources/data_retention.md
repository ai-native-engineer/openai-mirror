<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/data_retention/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Admin](/api/reference/python/resources/admin)

[Organization](/api/reference/python/resources/admin/subresources/organization)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Data Retention

##### [Retrieve organization data retention](/api/reference/python/resources/admin/subresources/organization/subresources/data_retention/methods/retrieve)

admin.organization.data\_retention.retrieve()  -> [OrganizationDataRetention](/api/reference/python/resources/admin#(resource)%20admin.organization.data_retention%20%3E%20(model)%20organization_data_retention%20%3E%20(schema))

GET/organization/data\_retention

##### [Update organization data retention](/api/reference/python/resources/admin/subresources/organization/subresources/data_retention/methods/update)

admin.organization.data\_retention.update(DataRetentionUpdateParams\*\*kwargs)  -> [OrganizationDataRetention](/api/reference/python/resources/admin#(resource)%20admin.organization.data_retention%20%3E%20(model)%20organization_data_retention%20%3E%20(schema))

POST/organization/data\_retention

##### ModelsExpand Collapse

class OrganizationDataRetention: …

Represents the organization’s data retention control setting.

object: Literal["organization.data\_retention"]

The object type, which is always `organization.data_retention`.

type: Literal["zero\_data\_retention", "modified\_abuse\_monitoring", "enhanced\_zero\_data\_retention", "enhanced\_modified\_abuse\_monitoring"]

The configured organization data retention type.

One of the following:

"zero\_data\_retention"

"modified\_abuse\_monitoring"

"enhanced\_zero\_data\_retention"

"enhanced\_modified\_abuse\_monitoring"
