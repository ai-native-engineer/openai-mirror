<!-- source: https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/data_retention/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Data Retention

##### [Retrieve organization data retention](/api/reference/resources/admin/subresources/organization/subresources/data_retention/methods/retrieve)

GET/organization/data\_retention

##### [Update organization data retention](/api/reference/resources/admin/subresources/organization/subresources/data_retention/methods/update)

POST/organization/data\_retention

##### ModelsExpand Collapse

OrganizationDataRetention object { object, type }

Represents the organization’s data retention control setting.

object: "organization.data\_retention"

The object type, which is always `organization.data_retention`.

type: "zero\_data\_retention" or "modified\_abuse\_monitoring" or "enhanced\_zero\_data\_retention" or "enhanced\_modified\_abuse\_monitoring"

The configured organization data retention type.

One of the following:

"zero\_data\_retention"

"modified\_abuse\_monitoring"

"enhanced\_zero\_data\_retention"

"enhanced\_modified\_abuse\_monitoring"
